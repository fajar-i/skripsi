"""
LogiTrace: Teacher Ambient Dashboard Router & WebSocket (US-04).
Presents Top-3 Stuck Students priority cards and 34 x 12 mastery heatmap.
"""

from datetime import datetime, timezone
from typing import Dict, List, Set, Optional
from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from sqlalchemy import desc, func, select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.database import get_db, AsyncSessionLocal
from ..db.models import Student, KnowledgeComponent, Interaction, MasterySnapshot, QuizSession, StudentAttempt, Item, AgentLog
from ..schemas.ambient import TeacherAmbientState, TopStuckStudent, HeatmapCell
from ..schemas.summary import SessionSummaryResponse
from ..schemas.labeling import ItemLabelRequest, ItemLabelResult, ReviewQueueItem, LabelApprovalRequest
from ..rag.summary_service import summary_service
from ..rag.labeling_service import labeling_service

router = APIRouter(prefix="/api/teacher", tags=["Teacher Ambient Dashboard"])


class ConnectionManager:
    """Manages active WebSocket connections for teacher ambient dashboards."""
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast_state(self, state_dict: dict):
        dead_connections = []
        for connection in list(self.active_connections):
            try:
                await connection.send_json(state_dict)
            except Exception:
                dead_connections.append(connection)
        for dead in dead_connections:
            self.disconnect(dead)


ws_manager = ConnectionManager()


async def compute_ambient_state(db: AsyncSession, session_id: Optional[str] = None) -> TeacherAmbientState:
    """Computes Top-3 Stuck Students and 34x12 class heatmap, optionally filtered by session."""
    # 0. Resolve target session & LMS student attempt metrics
    target_session = None
    if session_id:
        target_session = await db.get(QuizSession, session_id)
    if not target_session:
        stmt_active = select(QuizSession).where(
            QuizSession.class_rombel == "XI TKJ 1",
            QuizSession.is_active == True
        ).order_by(desc(QuizSession.created_at))
        res_active = await db.execute(stmt_active)
        target_session = res_active.scalar_one_or_none()

    not_started_cnt = 0
    in_progress_cnt = 0
    completed_cnt = 0
    attempt_map: Dict[str, StudentAttempt] = {}
    if target_session:
        att_stmt = select(StudentAttempt).where(StudentAttempt.session_id == target_session.id)
        att_res = await db.execute(att_stmt)
        for att in att_res.scalars().all():
            attempt_map[att.student_id] = att
            if att.status == "NOT_STARTED":
                not_started_cnt += 1
            elif att.status == "IN_PROGRESS":
                in_progress_cnt += 1
            elif att.status == "COMPLETED":
                completed_cnt += 1

    # 1. Fetch all students
    std_stmt = select(Student).order_by(Student.anonymous_code)
    std_res = await db.execute(std_stmt)
    students = std_res.scalars().all()

    # 2. Fetch all KCs
    kc_stmt = select(KnowledgeComponent)
    kc_res = await db.execute(kc_stmt)
    kcs = {kc.id: kc.name for kc in kc_res.scalars().all()}

    # 3. Fetch all snapshots
    snap_stmt = select(MasterySnapshot)
    snap_res = await db.execute(snap_stmt)
    snapshots = snap_res.scalars().all()

    # Map (student_id, kc_id) -> snapshot
    snap_map = {(s.student_id, s.kc_id): s for s in snapshots}

    # 4. Build Heatmap Cells
    heatmap_cells: List[HeatmapCell] = []
    total_mastery_sum = 0.0
    total_mastery_count = 0

    for student in students:
        for kc_id in kcs.keys():
            snap = snap_map.get((student.id, kc_id))
            m = snap.current_mastery if snap else 0.25
            conf = snap.confidence if snap else "low"
            heatmap_cells.append(
                HeatmapCell(
                    student_code=student.anonymous_code,
                    kc_id=kc_id,
                    mastery=round(m, 2),
                    confidence=conf
                )
            )
            total_mastery_sum += m
            total_mastery_count += 1

    class_avg = total_mastery_sum / total_mastery_count if total_mastery_count > 0 else 0.25

    # 5. Detect Top-3 Stuck Students
    recent_int_stmt = (
        select(Interaction)
        .options(selectinload(Interaction.item))
        .order_by(desc(Interaction.created_at))
        .limit(200)
    )
    if target_session:
        recent_int_stmt = recent_int_stmt.where(Interaction.session_id == target_session.id)
    recent_int_res = await db.execute(recent_int_stmt)
    recent_interactions = recent_int_res.scalars().all()

    # Calculate consecutive errors per student per KC
    stuck_candidates = []
    for student in students:
        # Avoid false alerts: skip students who have not started or have no answered items in this session
        if target_session:
            att = attempt_map.get(student.id)
            if not att or att.status == "NOT_STARTED" or not att.answered_item_ids:
                continue

        # Find lowest mastery KC for this student
        lowest_kc_id = None
        min_m = 1.0
        for kc_id in kcs.keys():
            snap = snap_map.get((student.id, kc_id))
            m = snap.current_mastery if snap else 0.25
            if m < min_m:
                min_m = m
                lowest_kc_id = kc_id

        if lowest_kc_id and min_m < 0.50:
            # Count consecutive errors on this KC
            consecutive_errs = 0
            has_attempts = False
            for it in recent_interactions:
                if it.student_id == student.id and it.item.primary_kc_id == lowest_kc_id:
                    has_attempts = True
                    if it.response_result == 0:
                        consecutive_errs += 1
                    else:
                        break

            # Only flag as stuck if student has actively attempted and experienced errors (avoids cold-start false alerts)
            if consecutive_errs >= 1 or (has_attempts and min_m < 0.30):
                stuck_candidates.append({
                    "student_code": student.anonymous_code,
                    "kc_id": lowest_kc_id,
                    "kc_name": kcs.get(lowest_kc_id, lowest_kc_id),
                    "mastery": min_m,
                    "consecutive_errors": consecutive_errs
                })

    # Sort candidates by lowest mastery and highest consecutive errors
    stuck_candidates.sort(key=lambda x: (x["mastery"], -x["consecutive_errors"]))
    top_3_data = stuck_candidates[:3]

    top_3_stuck: List[TopStuckStudent] = []
    for c in top_3_data:
        action_text = (
            f"Kunjungi meja siswa di Zona B; berikan bimbingan terarah "
            f"pada konsep dasar {c['kc_name']} tanpa menyebut jawaban kuis."
        )
        top_3_stuck.append(
            TopStuckStudent(
                student_code=c["student_code"],
                stuck_kc_id=c["kc_id"],
                stuck_kc_name=c["kc_name"],
                current_mastery=round(c["mastery"], 2),
                consecutive_errors=c["consecutive_errors"],
                recommended_action=action_text
            )
        )

    return TeacherAmbientState(
        class_rombel="XI TKJ 1",
        active_students_count=len(students),
        class_average_mastery=round(class_avg, 3),
        top_stuck_students=top_3_stuck,
        heatmap=heatmap_cells,
        timestamp=datetime.now(timezone.utc).isoformat(),
        session_id=target_session.id if target_session else None,
        session_title=target_session.title if target_session else None,
        session_number=target_session.session_number if target_session else None,
        not_started_count=not_started_cnt,
        in_progress_count=in_progress_cnt,
        completed_count=completed_cnt
    )


@router.get("/ambient", response_model=TeacherAmbientState)
async def get_teacher_ambient(session_id: Optional[str] = None, db: AsyncSession = Depends(get_db)):
    """REST endpoint for ambient dashboard initial hydration, optionally filtered by session."""
    return await compute_ambient_state(db, session_id=session_id)


@router.websocket("/ws/ambient")
async def websocket_teacher_ambient(websocket: WebSocket):
    """WebSocket stream for real-time ambient telemetry in Zone B."""
    await ws_manager.connect(websocket)
    try:
        async with AsyncSessionLocal() as session:
            initial_state = await compute_ambient_state(session)
            await websocket.send_json(initial_state.model_dump())

        while True:
            # Keep socket open and handle incoming pings
            data = await websocket.receive_text()
            if data == "ping":
                await websocket.send_text("pong")
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
    except Exception:
        ws_manager.disconnect(websocket)


@router.get("/session-summary", response_model=SessionSummaryResponse)
@router.post("/session-summary", response_model=SessionSummaryResponse)
async def get_session_summary(
    session_id: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """
    US-06: Agent T3 — Session Narrative Summary & Peer-Tutoring Recommendations.
    Generates structured reflection for closing session (minute 80) and peer pairs.
    """
    return await summary_service.generate_session_summary(db=db, session_id=session_id)


@router.post("/items/label", response_model=ItemLabelResult)
async def label_new_item(
    req: ItemLabelRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    US-05: Agent T1 — Automatic Semantic Item Labeling.
    Categorizes item prompt into KC, TOLT, difficulty, and confidence score.
    """
    return await labeling_service.label_item(req=req, db=db)


@router.get("/items/review-queue", response_model=List[ReviewQueueItem])
async def get_item_review_queue(
    db: AsyncSession = Depends(get_db)
):
    """
    US-05: Teacher Review Queue for items requiring verification or calibration.
    """
    stmt = select(Item).order_by(desc(Item.created_at)).limit(10)
    res = await db.execute(stmt)
    items = res.scalars().all()

    queue: List[ReviewQueueItem] = []
    for item in items:
        # Check if item has confidence or compute confidence estimate
        is_calib = item.is_calibration
        queue.append(ReviewQueueItem(
            item_id=item.id,
            prompt_text=item.prompt_text,
            options=item.options,
            current_primary_kc_id=item.primary_kc_id,
            current_tolt_dimension=item.tolt_dimension,
            current_difficulty=item.difficulty_nominal,
            confidence=0.92 if not is_calib else 0.85,
            status="approved" if not is_calib else "calibrated"
        ))
    return queue


@router.post("/items/{item_id}/approve-label")
async def approve_item_label(
    item_id: str,
    req: LabelApprovalRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    US-05: Allows the teacher to approve or edit labels for an item in the bank.
    """
    item = await db.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item '{item_id}' not found")

    # Validate that primary_kc_id exists in Knowledge Component registry
    kc = await db.get(KnowledgeComponent, req.primary_kc_id)
    if not kc:
        raise HTTPException(status_code=400, detail=f"Knowledge Component '{req.primary_kc_id}' tidak valid atau tidak terdaftar.")

    item.primary_kc_id = req.primary_kc_id
    item.tolt_dimension = req.tolt_dimension
    item.difficulty_nominal = req.difficulty_nominal

    # Log teacher approval in AgentLog
    agent_log = AgentLog(
        trigger_type="T1_REVIEW",
        prompt_hash=None,
        model_id="teacher_human_in_the_loop",
        raw_output=f"Approved item {item_id}: KC={req.primary_kc_id}, TOLT={req.tolt_dimension}, Diff={req.difficulty_nominal}. Notes: {req.teacher_notes or '-'}",
        is_accepted=True,
        latency_ms=0
    )
    db.add(agent_log)
    await db.commit()

    return {
        "status": "success",
        "message": f"Label untuk butir '{item_id}' berhasil diverifikasi dan diperbarui.",
        "item_id": item_id,
        "primary_kc_id": item.primary_kc_id,
        "tolt_dimension": item.tolt_dimension,
        "difficulty_nominal": item.difficulty_nominal
    }
