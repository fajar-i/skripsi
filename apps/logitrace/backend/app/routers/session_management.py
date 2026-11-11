"""
LogiTrace: LMS Session & Classroom Management Router (Google Classroom Standard).
Enables creating reusable evaluation sessions, tracking student attempts,
resetting individual or class-wide sessions, and restarting evaluations from Question 1.
"""

from datetime import datetime, timezone
from typing import Dict, List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.database import get_db
from ..db.models import ClassRoom, QuizSession, StudentAttempt, Student, MasterySnapshot, KnowledgeComponent

router = APIRouter(prefix="/api/sessions", tags=["LMS Session Management"])


class CreateSessionRequest(BaseModel):
    title: str = Field(..., examples=["Sesi 2: Perawatan & Perbaikan Jaringan Nirkabel"])
    class_rombel: str = Field(default="XI TKJ 1", examples=["XI TKJ 1"])
    session_number: int = Field(default=2, ge=1)
    max_items: int = Field(default=20, ge=6, le=50)


class SessionSummary(BaseModel):
    id: str
    class_rombel: str
    title: str
    session_number: int
    max_items: int
    is_active: bool
    created_at: str
    total_students: int
    not_started_count: int
    in_progress_count: int
    completed_count: int


@router.get("", response_model=List[SessionSummary])
async def list_sessions(class_rombel: Optional[str] = None, db: AsyncSession = Depends(get_db)):
    """Lists all evaluation assignments/sessions with LMS progress metrics."""
    stmt = select(QuizSession).order_by(desc(QuizSession.created_at))
    if class_rombel:
        stmt = stmt.where(QuizSession.class_rombel == class_rombel)
    res = await db.execute(stmt)
    sessions = res.scalars().all()

    # Pre-aggregate attempt counts in a single query (O(1) database roundtrip)
    session_ids = [s.id for s in sessions]
    counts_map: Dict[str, Dict[str, int]] = {}
    if session_ids:
        att_stmt = (
            select(StudentAttempt.session_id, StudentAttempt.status, func.count(StudentAttempt.id))
            .where(StudentAttempt.session_id.in_(session_ids))
            .group_by(StudentAttempt.session_id, StudentAttempt.status)
        )
        att_res = await db.execute(att_stmt)
        for sid, att_status, cnt in att_res.all():
            if sid not in counts_map:
                counts_map[sid] = {}
            counts_map[sid][att_status] = cnt

    summaries = []
    for s in sessions:
        s_counts = counts_map.get(s.id, {})
        not_started = s_counts.get("NOT_STARTED", 0)
        in_progress = s_counts.get("IN_PROGRESS", 0)
        completed = s_counts.get("COMPLETED", 0)
        total = not_started + in_progress + completed

        summaries.append(
            SessionSummary(
                id=s.id,
                class_rombel=s.class_rombel,
                title=s.title,
                session_number=s.session_number,
                max_items=s.max_items,
                is_active=s.is_active,
                created_at=s.created_at.isoformat(),
                total_students=total,
                not_started_count=not_started,
                in_progress_count=in_progress,
                completed_count=completed
            )
        )
    return summaries


@router.get("/active")
async def get_active_session(class_rombel: str = "XI TKJ 1", db: AsyncSession = Depends(get_db)):
    """Returns currently active evaluation session for classroom."""
    stmt = select(QuizSession).where(
        QuizSession.class_rombel == class_rombel,
        QuizSession.is_active == True
    ).order_by(desc(QuizSession.created_at))
    res = await db.execute(stmt)
    active = res.scalar_one_or_none()
    if not active:
        # Fallback to the latest session
        stmt_latest = select(QuizSession).where(QuizSession.class_rombel == class_rombel).order_by(desc(QuizSession.created_at))
        res_latest = await db.execute(stmt_latest)
        active = res_latest.scalar_one_or_none()
        if not active:
            raise HTTPException(status_code=404, detail="No session found. Please initialize sessions.")

    return {
        "id": active.id,
        "title": active.title,
        "session_number": active.session_number,
        "max_items": active.max_items,
        "class_rombel": active.class_rombel,
        "is_active": active.is_active
    }


@router.post("", response_model=Dict)
async def create_new_session(req: CreateSessionRequest, db: AsyncSession = Depends(get_db)):
    """
    Teacher creates a new evaluation assignment/session (like in Google Classroom).
    Automatically enrolls class students with fresh NOT_STARTED attempts.
    """
    # Deactivate older sessions in this class so new session becomes active
    old_stmt = select(QuizSession).where(QuizSession.class_rombel == req.class_rombel)
    old_res = await db.execute(old_stmt)
    for old_s in old_res.scalars().all():
        old_s.is_active = False

    new_session = QuizSession(
        class_rombel=req.class_rombel,
        title=req.title,
        session_number=req.session_number,
        max_items=req.max_items,
        is_active=True
    )
    db.add(new_session)
    await db.flush()

    # Query students in this class
    std_stmt = select(Student).where(Student.class_rombel == req.class_rombel)
    std_res = await db.execute(std_stmt)
    students = std_res.scalars().all()

    # Create NOT_STARTED attempt for each student
    for st in students:
        attempt = StudentAttempt(
            student_id=st.id,
            session_id=new_session.id,
            status="NOT_STARTED",
            current_sequence=0,
            answered_item_ids=[]
        )
        db.add(attempt)

    await db.commit()
    return {
        "status": "success",
        "message": f"Session '{new_session.title}' created with {len(students)} enrolled students.",
        "session_id": new_session.id
    }


@router.post("/{session_id}/activate")
async def activate_session(session_id: str, db: AsyncSession = Depends(get_db)):
    """
    Sets this session as the active assignment for the classroom.
    """
    session = await db.get(QuizSession, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    stmt = select(QuizSession).where(QuizSession.class_rombel == session.class_rombel)
    res = await db.execute(stmt)
    for s in res.scalars().all():
        s.is_active = (s.id == session_id)
    await db.commit()

    return {
        "status": "success",
        "message": f"Sesi '{session.title}' sekarang aktif sebagai tugas utama kelas.",
        "active_session_id": session_id
    }


@router.post("/{session_id}/reset-all")
async def reset_session_for_all(session_id: str, db: AsyncSession = Depends(get_db)):
    """
    RESTART FROM SCRATCH (ULANG PROSES DARI AWAL).
    Resets all student attempts in this session to Question 1 (NOT_STARTED).
    Resets baseline mastery snapshots for all enrolled students back to prior 0.25.
    """
    session = await db.get(QuizSession, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    # Fetch attempts
    att_stmt = select(StudentAttempt).where(StudentAttempt.session_id == session_id)
    att_res = await db.execute(att_stmt)
    attempts = att_res.scalars().all()

    for att in attempts:
        att.status = "NOT_STARTED"
        att.current_sequence = 0
        att.answered_item_ids = []
        att.final_mastery = None
        att.started_at = None
        att.completed_at = None

    # Reset mastery snapshots to prior baseline (0.25, confidence: low)
    std_stmt = select(Student.id).where(Student.class_rombel == session.class_rombel)
    std_res = await db.execute(std_stmt)
    student_ids = [r[0] for r in std_res.all()]

    snap_stmt = select(MasterySnapshot).where(MasterySnapshot.student_id.in_(student_ids))
    snap_res = await db.execute(snap_stmt)
    for snap in snap_res.scalars().all():
        snap.current_mastery = 0.25
        snap.confidence = "low"

    await db.commit()

    return {
        "status": "success",
        "message": f"Sesi '{session.title}' berhasil di-reset total dari awal! Seluruh {len(attempts)} siswa dapat memulai kembali dari Soal 1.",
        "session_id": session_id,
        "reset_students_count": len(attempts)
    }


@router.post("/{session_id}/reset-student/{student_code}")
async def reset_student_attempt(session_id: str, student_code: str, db: AsyncSession = Depends(get_db)):
    """
    Teacher resets an individual student's attempt to restart from Question 1.
    """
    session = await db.get(QuizSession, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    std_stmt = select(Student).where(Student.anonymous_code == student_code)
    std_res = await db.execute(std_stmt)
    student = std_res.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=404, detail=f"Student '{student_code}' not found")

    att_stmt = select(StudentAttempt).where(
        StudentAttempt.session_id == session_id,
        StudentAttempt.student_id == student.id
    )
    att_res = await db.execute(att_stmt)
    attempt = att_res.scalar_one_or_none()
    if not attempt:
        # Create fresh attempt if missing
        attempt = StudentAttempt(
            student_id=student.id,
            session_id=session_id,
            status="NOT_STARTED",
            current_sequence=0,
            answered_item_ids=[]
        )
        db.add(attempt)
    else:
        attempt.status = "NOT_STARTED"
        attempt.current_sequence = 0
        attempt.answered_item_ids = []
        attempt.final_mastery = None
        attempt.started_at = None
        attempt.completed_at = None

    # Reset student's mastery snapshots to baseline
    snap_stmt = select(MasterySnapshot).where(MasterySnapshot.student_id == student.id)
    snap_res = await db.execute(snap_stmt)
    for snap in snap_res.scalars().all():
        snap.current_mastery = 0.25
        snap.confidence = "low"

    await db.commit()

    return {
        "status": "success",
        "message": f"Siswa {student_code} berhasil di-reset ke Soal 1 untuk sesi ini.",
        "student_code": student_code
    }


@router.get("/{session_id}/student/{student_code}/status")
async def get_student_session_status(session_id: str, student_code: str, db: AsyncSession = Depends(get_db)):
    """
    Google Classroom style card: shows student their current status in this assignment:
    NOT_STARTED, IN_PROGRESS (item X of 20), or COMPLETED.
    """
    std_stmt = select(Student).where(Student.anonymous_code == student_code)
    std_res = await db.execute(std_stmt)
    student = std_res.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=404, detail=f"Student '{student_code}' not found")

    session = await db.get(QuizSession, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    att_stmt = select(StudentAttempt).where(
        StudentAttempt.session_id == session_id,
        StudentAttempt.student_id == student.id
    )
    att_res = await db.execute(att_stmt)
    attempt = att_res.scalar_one_or_none()

    if not attempt:
        return {
            "status": "NOT_STARTED",
            "current_sequence": 0,
            "max_items": session.max_items,
            "session_title": session.title,
            "final_mastery": None
        }

    return {
        "status": attempt.status,
        "current_sequence": attempt.current_sequence,
        "max_items": session.max_items,
        "session_title": session.title,
        "final_mastery": attempt.final_mastery
    }
