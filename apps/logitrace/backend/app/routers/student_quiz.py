"""
LogiTrace: Student Adaptive Quiz Router.
Handles question delivery, answer submission with L3 updates, and Socratic hints.
"""

import json
import os
from datetime import timezone
from typing import Dict, List, Optional, Set
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import desc, func, select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.database import get_db
from ..db.models import (
    Student,
    Item,
    KnowledgeComponent,
    Interaction,
    MasterySnapshot,
    AgentLog,
    QuizSession,
    StudentAttempt,
    HintEvent,
    utc_now
)
from ..engine.cognitive import calculate_predicted_p, update_mastery, apply_temporal_decay
from ..engine.zpd_selector import ZPDSelector, ItemCandidate
from ..engine.calibration import CalibrationManager, CalibrationItem
from ..rag.hint_service import hint_service
from .teacher_ambient import ws_manager, compute_ambient_state
from ..schemas.quiz import (
    ItemPresentation,
    SubmitAnswerRequest,
    SubmitAnswerResponse,
    HintRequest,
    HintResponse
)

router = APIRouter(prefix="/api/quiz", tags=["Student Quiz"])

# Load DAG edges and KC IDs for prerequisite gating & cold-start calibration
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "data"))
DAG_PATH = os.path.join(DATA_DIR, "l1_knowledge_base", "dag_prerequisites.json")
KCS_PATH = os.path.join(DATA_DIR, "l1_knowledge_base", "kcs.json")
dag_edges = []
all_kc_ids = []
if os.path.exists(DAG_PATH):
    with open(DAG_PATH, "r", encoding="utf-8") as f:
        dag_data = json.load(f)
        dag_edges = dag_data.get("edges", [])
        all_kc_ids = list(dag_data.get("in_degrees", {}).keys())
if not all_kc_ids and os.path.exists(KCS_PATH):
    with open(KCS_PATH, "r", encoding="utf-8") as f:
        all_kc_ids = [kc["id"] for kc in json.load(f)]

zpd_selector = ZPDSelector(dag_edges)
calibration_manager = CalibrationManager(all_kc_ids)


def _days_since(ts) -> float:
    """Elapsed days since a stored timestamp (SQLite returns naive datetimes = UTC)."""
    if ts is None:
        return 0.0
    if ts.tzinfo is None:
        ts = ts.replace(tzinfo=timezone.utc)
    return max(0.0, (utc_now() - ts).total_seconds() / 86400.0)


def _read_mastery(snapshot) -> float:
    """On-read Ebbinghaus decay: m(t) = m(t_last) * exp(-dt / tau)."""
    if snapshot is None:
        return 0.25
    return apply_temporal_decay(snapshot.current_mastery, _days_since(snapshot.last_updated_at))


async def _resolve_session(db: AsyncSession, student: Student, session_id: Optional[str]):
    target_session = None
    if session_id:
        target_session = await db.get(QuizSession, session_id)
    if not target_session:
        sess_stmt = (
            select(QuizSession)
            .where(QuizSession.class_rombel == student.class_rombel, QuizSession.is_active == True)
            .order_by(desc(QuizSession.created_at))
        )
        sess_res = await db.execute(sess_stmt)
        target_session = sess_res.scalars().first()
    return target_session


@router.get("/{student_code}/next", response_model=ItemPresentation)
async def get_next_question(
    student_code: str,
    session_id: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """
    Fetches the next appropriate item for the student in the active session/assignment.
    Supports resuming in-progress evaluations or restarting cleanly per session.
    """
    # 1. Look up student
    stmt = select(Student).where(Student.anonymous_code == student_code)
    res = await db.execute(stmt)
    student = res.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=404, detail=f"Student '{student_code}' not found")

    # 2. Resolve active QuizSession
    target_session = None
    if session_id:
        target_session = await db.get(QuizSession, session_id)
    if not target_session:
        # Get active session for student's class
        sess_stmt = (
            select(QuizSession)
            .where(QuizSession.class_rombel == student.class_rombel, QuizSession.is_active == True)
            .order_by(desc(QuizSession.created_at))
        )
        sess_res = await db.execute(sess_stmt)
        target_session = sess_res.scalar_one_or_none()

    # 3. Resolve or create StudentAttempt for this session
    answered_item_ids = set()
    current_seq = 0
    max_items = target_session.max_items if target_session else 20
    sess_id = target_session.id if target_session else None

    if target_session:
        att_stmt = select(StudentAttempt).where(
            StudentAttempt.student_id == student.id,
            StudentAttempt.session_id == target_session.id
        )
        att_res = await db.execute(att_stmt)
        attempt = att_res.scalar_one_or_none()
        if not attempt:
            attempt = StudentAttempt(
                student_id=student.id,
                session_id=target_session.id,
                status="NOT_STARTED",
                current_sequence=0,
                answered_item_ids=[]
            )
            db.add(attempt)
            await db.flush()

        current_seq = attempt.current_sequence
        answered_item_ids = set(attempt.answered_item_ids or [])

        # Check if attempt is already completed
        if attempt.status == "COMPLETED" or current_seq >= max_items:
            return ItemPresentation(
                item_id="COMPLETED",
                sequence_number=max_items,
                is_calibration=False,
                primary_kc="NONE",
                kc_name="Sesi Selesai",
                difficulty=1,
                prompt_text="Anda telah menyelesaikan evaluasi pada sesi ini.",
                options={"A": "Selesai"},
                session_id=sess_id,
                max_items=max_items,
                is_completed=True
            )
    else:
        int_stmt = select(Interaction.item_id).where(Interaction.student_id == student.id)
        int_res = await db.execute(int_stmt)
        answered_item_ids = {r[0] for r in int_res.all()}
        current_seq = len(answered_item_ids)

    # 4. Cold-Start Calibration Phase (Items 1 - 6)
    selected_item = None
    if calibration_manager.is_calibrating(current_seq):
        cal_stmt = select(Item).where(Item.is_calibration == True, Item.is_active == True)
        cal_res = await db.execute(cal_stmt)
        calibration_items = cal_res.scalars().all()

        cal_candidates = [
            CalibrationItem(
                id=item.id,
                primary_kc=item.primary_kc_id,
                difficulty=item.difficulty_nominal,
                is_calibration=item.is_calibration
            )
            for item in calibration_items
        ]
        chosen_cal = calibration_manager.get_next_calibration_item(cal_candidates, answered_item_ids)
        if chosen_cal:
            selected_item = next((it for it in calibration_items if it.id == chosen_cal.id), None)

    # 5. Adaptive ZPD Phase (Items 7+)
    if not selected_item:
        # Get current mastery snapshot
        snap_stmt = select(MasterySnapshot).where(MasterySnapshot.student_id == student.id)
        snap_res = await db.execute(snap_stmt)
        snapshots = snap_res.scalars().all()
        student_mastery = {s.kc_id: _read_mastery(s) for s in snapshots}

        # Last KC answered
        last_int_stmt = (
            select(Interaction)
            .options(selectinload(Interaction.item))
            .where(Interaction.student_id == student.id)
            .order_by(desc(Interaction.created_at))
            .limit(1)
        )
        last_int_res = await db.execute(last_int_stmt)
        last_it = last_int_res.scalar_one_or_none()
        last_kc_id = last_it.item.primary_kc_id if last_it and last_it.item else None

        item_stmt = select(Item).where(Item.is_active == True)
        item_res = await db.execute(item_stmt)
        all_items = item_res.scalars().all()

        candidates = [
            ItemCandidate(
                id=item.id,
                primary_kc=item.primary_kc_id,
                difficulty=item.difficulty_nominal,
                is_calibration=item.is_calibration
            )
            for item in all_items
        ]

        chosen_candidate = zpd_selector.select_next_item(
            candidate_items=candidates,
            student_mastery=student_mastery,
            answered_item_ids=answered_item_ids,
            last_kc_id=last_kc_id,
            allow_relaxation=True
        )

        if chosen_candidate:
            selected_item = next((it for it in all_items if it.id == chosen_candidate.id), None)

    if not selected_item:
        # Fallback to any active unattempted item
        for it in all_items:
            if it.id not in answered_item_ids:
                selected_item = it
                break

    if not selected_item:
        raise HTTPException(status_code=404, detail="No further items available in item bank")

    # Fetch KC name
    kc = await db.get(KnowledgeComponent, selected_item.primary_kc_id)
    kc_name = kc.name if kc else selected_item.primary_kc_id

    return ItemPresentation(
        item_id=selected_item.id,
        sequence_number=current_seq + 1,
        is_calibration=selected_item.is_calibration,
        primary_kc=selected_item.primary_kc_id,
        kc_name=kc_name,
        difficulty=selected_item.difficulty_nominal,
        prompt_text=selected_item.prompt_text,
        options=selected_item.options,
        session_id=sess_id,
        max_items=max_items,
        is_completed=False
    )


@router.post("/submit", response_model=SubmitAnswerResponse)
async def submit_answer(req: SubmitAnswerRequest, db: AsyncSession = Depends(get_db)):
    """
    Evaluates response, deterministically updates cognitive mastery (< 1 ms),
    and records an append-only interaction audit row.
    """
    # 1. Load student and item
    stmt = select(Student).where(Student.anonymous_code == req.student_code)
    res = await db.execute(stmt)
    student = res.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=404, detail=f"Student '{req.student_code}' not found")

    item = await db.get(Item, req.item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item '{req.item_id}' not found")

    # 2. Resolve active QuizSession and StudentAttempt
    target_session = None
    if req.session_id:
        target_session = await db.get(QuizSession, req.session_id)
    if not target_session:
        sess_stmt = (
            select(QuizSession)
            .where(QuizSession.class_rombel == student.class_rombel, QuizSession.is_active == True)
            .order_by(desc(QuizSession.created_at))
        )
        sess_res = await db.execute(sess_stmt)
        target_session = sess_res.scalar_one_or_none()

    attempt = None
    max_items = target_session.max_items if target_session else 20
    if target_session:
        att_stmt = select(StudentAttempt).where(
            StudentAttempt.student_id == student.id,
            StudentAttempt.session_id == target_session.id
        )
        att_res = await db.execute(att_stmt)
        attempt = att_res.scalar_one_or_none()
        if not attempt:
            attempt = StudentAttempt(
                student_id=student.id,
                session_id=target_session.id,
                status="IN_PROGRESS",
                current_sequence=0,
                answered_item_ids=[],
                started_at=utc_now()
            )
            db.add(attempt)
            await db.flush()
        elif attempt.status == "NOT_STARTED":
            attempt.status = "IN_PROGRESS"
            attempt.started_at = utc_now()

        seq_num = attempt.current_sequence + 1
    else:
        count_stmt = select(func.count(Interaction.id)).where(Interaction.student_id == student.id)
        count_res = await db.execute(count_stmt)
        past_count = count_res.scalar() or 0
        seq_num = past_count + 1

    is_calibration = seq_num <= 6

    # 3. Retrieve current mastery for this KC
    snap_stmt = select(MasterySnapshot).where(
        MasterySnapshot.student_id == student.id,
        MasterySnapshot.kc_id == item.primary_kc_id
    )
    snap_res = await db.execute(snap_stmt)
    snapshot = snap_res.scalar_one_or_none()
    current_m = _read_mastery(snapshot)

    # 4. Check correctness
    is_correct = (req.choice.strip().upper() == item.correct_answer.strip().upper())
    result_binary = 1 if is_correct else 0

    # 5. Deterministic L3 Calculations (< 1 ms)
    # Hint usage is taken from the server-side hint log, not from the client flag.
    hint_stmt = select(func.max(HintEvent.hint_level)).where(
        HintEvent.student_id == student.id,
        HintEvent.item_id == item.id,
        HintEvent.session_id == (target_session.id if target_session else None),
    )
    max_hint_level = (await db.execute(hint_stmt)).scalar() or 0
    used_hint = max_hint_level > 0

    p_hat = calculate_predicted_p(current_m, item.difficulty_nominal)
    new_m = update_mastery(
        current_m=current_m,
        response_result=result_binary,
        difficulty=item.difficulty_nominal,
        used_hint=used_hint
    )
    m_delta = new_m - current_m

    # 6. Append interaction to database (STRICTLY APPEND-ONLY)
    sess_id_val = target_session.id if target_session else None
    sess_num_val = target_session.session_number if target_session else 1

    interaction = Interaction(
        student_id=student.id,
        item_id=item.id,
        session_id=sess_id_val,
        session_number=sess_num_val,
        sequence_number=seq_num,
        response_result=result_binary,
        student_choice=req.choice.strip().upper(),
        predicted_p=round(p_hat, 4),
        mastery_before=round(current_m, 4),
        mastery_after=round(new_m, 4),
        response_time_ms=req.response_time_ms,
        hint_level_used=max_hint_level,
        is_calibration=is_calibration
    )
    db.add(interaction)

    # 7. Update StudentAttempt progress
    is_completed = False
    if attempt:
        attempt.current_sequence = seq_num
        attempt.answered_item_ids = list(set((attempt.answered_item_ids or []) + [item.id]))
        if seq_num >= max_items:
            attempt.status = "COMPLETED"
            attempt.completed_at = utc_now()
            attempt.final_mastery = round(new_m, 4)
            is_completed = True

    # 8. Update mastery snapshot & estimate unmeasured KCs from prerequisite clusters (US-01)
    if snapshot:
        snapshot.current_mastery = round(new_m, 4)
        snapshot.confidence = "high"
        snapshot.last_updated_at = utc_now()
    else:
        new_snap = MasterySnapshot(
            student_id=student.id,
            kc_id=item.primary_kc_id,
            current_mastery=round(new_m, 4),
            confidence="high",
            last_updated_at=utc_now()
        )
        db.add(new_snap)
    await db.flush()

    # Estimate unmeasured KCs from prerequisite clusters and mark confidence='low'
    all_snaps_stmt = select(MasterySnapshot).where(MasterySnapshot.student_id == student.id)
    all_snaps_res = await db.execute(all_snaps_stmt)
    existing_snaps = {s.kc_id: s for s in all_snaps_res.scalars().all()}

    current_mastery_map = {kc_id: s.current_mastery for kc_id, s in existing_snaps.items()}
    measured_kcs = {kc_id for kc_id, s in existing_snaps.items() if s.confidence == "high"}
    estimations = calibration_manager.estimate_unmeasured_kcs(current_mastery_map, measured_kcs, dag_edges)

    for kc_id, est in estimations.items():
        if est["confidence"] == "low":
            if kc_id in existing_snaps:
                existing_snaps[kc_id].current_mastery = round(est["m"], 4)
                existing_snaps[kc_id].confidence = "low"
            else:
                db.add(
                    MasterySnapshot(
                        student_id=student.id,
                        kc_id=kc_id,
                        current_mastery=round(est["m"], 4),
                        confidence="low",
                        last_updated_at=utc_now()
                    )
                )

    await db.commit()

    # Broadcast real-time ambient telemetry update to connected teacher dashboards
    try:
        ambient_state = await compute_ambient_state(db)
        await ws_manager.broadcast_state(ambient_state.model_dump())
    except Exception:
        pass

    return SubmitAnswerResponse(
        is_correct=is_correct,
        correct_choice=item.correct_answer,
        explanation=item.explanation,
        predicted_p=round(p_hat, 4),
        mastery_before=round(current_m, 4),
        mastery_after=round(new_m, 4),
        mastery_delta=round(m_delta, 4),
        is_calibration=is_calibration,
        sequence_number=seq_num,
        is_completed=is_completed,
        session_id=sess_id_val
    )


@router.post("/hint", response_model=HintResponse)
async def request_socratic_hint(req: HintRequest, db: AsyncSession = Depends(get_db)):
    """
    Socratic hint (Agent T2) via 9router with a hard 3.0 s deadline and static fallback.
    Every served hint is recorded in hint_events so the mastery update can apply h = 0.5.
    """
    stmt = select(Student).where(Student.anonymous_code == req.student_code)
    student = (await db.execute(stmt)).scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=404, detail=f"Student '{req.student_code}' not found")

    item = await db.get(Item, req.item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item '{req.item_id}' not found")

    target_session = await _resolve_session(db, student, req.session_id)

    kc = await db.get(KnowledgeComponent, item.primary_kc_id)
    kc_name = kc.name if kc else item.primary_kc_id
    kc_desc = kc.description if kc else None

    correct_answer_text = item.options.get(item.correct_answer, item.correct_answer)

    hint_text, source, latency_ms, fallback_reason = await hint_service.generate_socratic_hint(
        kc_id=item.primary_kc_id,
        kc_name=kc_name,
        level=req.requested_level,
        prompt_text=item.prompt_text,
        correct_answer_text=correct_answer_text,
        options=item.options,
        kc_description=kc_desc
    )

    db.add(HintEvent(
        student_id=student.id,
        item_id=item.id,
        session_id=target_session.id if target_session else None,
        hint_level=req.requested_level,
        source=source,
    ))
    db.add(AgentLog(
        trigger_type="T2",
        prompt_hash=None,
        model_id=hint_service.client.model_name if source == "llm_9router" else "static_bank",
        raw_output=hint_text,
        is_accepted=(source == "llm_9router"),
        rejection_reason=(fallback_reason or "")[:255] or None,
        latency_ms=latency_ms
    ))
    await db.commit()

    return HintResponse(
        item_id=item.id,
        hint_level=req.requested_level,
        hint_text=hint_text,
        source=source,
        word_count=len(hint_text.split())
    )
