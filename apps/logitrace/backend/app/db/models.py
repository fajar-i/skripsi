"""
LogiTrace: Relational Data Models (PRD §4.3).
Enforces strictly append-only integrity for student interactions.
"""

import uuid
from datetime import datetime, timezone
from typing import Dict, List, Optional
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    JSON,
    String,
    Text,
    event
)
from sqlalchemy.orm import relationship
from .database import Base


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def generate_uuid() -> str:
    return str(uuid.uuid4())


class ClassRoom(Base):
    """LMS Class / Rombel standard (Google Classroom model)."""
    __tablename__ = "classrooms"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    name = Column(String(100), unique=True, nullable=False)  # e.g. "XI TKJ 1"
    subject = Column(String(150), nullable=False, default="Teknologi Jaringan Kabel dan Nirkabel")
    teacher_name = Column(String(100), nullable=False, default="Pak Budi")
    created_at = Column(DateTime, default=utc_now, nullable=False)

    sessions = relationship("QuizSession", back_populates="classroom", cascade="all")


class QuizSession(Base):
    """
    Standard LMS Assignment / Evaluation Session (Google Classroom model).
    Allows creating multiple sessions, resetting attempts, and selecting active sessions.
    """
    __tablename__ = "quiz_sessions"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    classroom_id = Column(String(36), ForeignKey("classrooms.id"), nullable=True)
    class_rombel = Column(String(64), nullable=False, default="XI TKJ 1")
    title = Column(String(255), nullable=False)  # e.g. "Sesi 1: Evaluasi Adaptif Instalasi Jaringan (TP 2.1 & 2.2)"
    session_number = Column(Integer, nullable=False, default=1)
    max_items = Column(Integer, nullable=False, default=20)
    is_active = Column(Boolean, nullable=False, default=True)
    join_code = Column(String(8), nullable=True)  # class code shown on the teacher screen; students need it to log in
    created_at = Column(DateTime, default=utc_now, nullable=False)

    classroom = relationship("ClassRoom", back_populates="sessions")
    attempts = relationship("StudentAttempt", back_populates="session", cascade="all")


class StudentAttempt(Base):
    """
    Tracks each student's attempt on a specific session.
    Enables resuming in-progress attempts or resetting attempts cleanly to restart from item 1.
    """
    __tablename__ = "student_attempts"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    student_id = Column(String(36), ForeignKey("students.id"), nullable=False, index=True)
    session_id = Column(String(36), ForeignKey("quiz_sessions.id"), nullable=False, index=True)
    status = Column(String(32), nullable=False, default="NOT_STARTED")  # NOT_STARTED, IN_PROGRESS, COMPLETED
    current_sequence = Column(Integer, nullable=False, default=0)
    answered_item_ids = Column(JSON, nullable=False, default=list)  # list of item IDs answered in this attempt
    final_mastery = Column(Float, nullable=True)
    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=utc_now, nullable=False)

    student = relationship("Student")
    session = relationship("QuizSession", back_populates="attempts")


class Student(Base):
    __tablename__ = "students"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    anonymous_code = Column(String(32), unique=True, nullable=False, index=True)  # e.g., "std_01"
    class_rombel = Column(String(64), nullable=False, default="XI TKJ 1")
    created_at = Column(DateTime, default=utc_now, nullable=False)
    # Login card: hashed 4-digit PIN (printed on the student's card) and the one active device token
    pin_hash = Column(String(160), nullable=True)
    pin_set_at = Column(DateTime, nullable=True)
    device_token_hash = Column(String(64), nullable=True, index=True)
    device_login_at = Column(DateTime, nullable=True)

    interactions = relationship("Interaction", back_populates="student", cascade="all")
    mastery_snapshots = relationship("MasterySnapshot", back_populates="student", cascade="all")


class KnowledgeComponent(Base):
    __tablename__ = "kc"

    id = Column(String(64), primary_key=True)  # e.g., "WLAN_STANDARDS"
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    prerequisites = Column(JSON, nullable=False, default=list)
    created_at = Column(DateTime, default=utc_now, nullable=False)

    items = relationship("Item", back_populates="kc")


class Item(Base):
    __tablename__ = "items"

    id = Column(String(64), primary_key=True)  # e.g., "ITEM_WLAN_STANDARDS_1_01"
    primary_kc_id = Column(String(64), ForeignKey("kc.id"), nullable=False, index=True)
    prompt_text = Column(Text, nullable=False)
    options = Column(JSON, nullable=False)  # {"A": "...", "B": "...", "C": "...", "D": "..."}
    correct_answer = Column(String(8), nullable=False)  # e.g., "A"
    difficulty_nominal = Column(Integer, nullable=False)  # 1, 2, or 3
    # Kisi-kisi metadata (replaces the former TOLT dimension)
    indikator_id = Column(String(16), nullable=True, index=True)      # e.g. IND-04.3
    bloom_level = Column(String(4), nullable=True)                   # C1..C6
    jonassen_phase = Column(String(48), nullable=True)               # troubleshooting phase
    label_status = Column(String(32), nullable=True, default="draf_ai")
    is_calibration = Column(Boolean, default=False, nullable=False, index=True)
    is_active = Column(Boolean, default=True, nullable=False)
    explanation = Column(Text, nullable=True)
    created_at = Column(DateTime, default=utc_now, nullable=False)

    kc = relationship("KnowledgeComponent", back_populates="items")
    interactions = relationship("Interaction", back_populates="item")


class Interaction(Base):
    """
    Append-Only Student Interaction Logs (PRD §4.3 & Directive #3).
    Strictly prohibited from UPDATE and DELETE statements.
    """
    __tablename__ = "interactions"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    student_id = Column(String(36), ForeignKey("students.id"), nullable=False, index=True)
    item_id = Column(String(64), ForeignKey("items.id"), nullable=False, index=True)
    session_id = Column(String(36), nullable=True, index=True)
    session_number = Column(Integer, nullable=False, default=1)
    sequence_number = Column(Integer, nullable=False)
    response_result = Column(Integer, nullable=False)  # 1 for correct, 0 for incorrect
    student_choice = Column(String(8), nullable=False)
    predicted_p = Column(Float, nullable=False)
    mastery_before = Column(Float, nullable=False)
    mastery_after = Column(Float, nullable=False)
    response_time_ms = Column(Integer, nullable=False, default=0)
    hint_level_used = Column(Integer, nullable=False, default=0)  # 0: none, 1: level 1, etc.
    is_calibration = Column(Boolean, nullable=False, default=False, index=True)
    created_at = Column(DateTime, default=utc_now, nullable=False, index=True)

    student = relationship("Student", back_populates="interactions")
    item = relationship("Item", back_populates="interactions")


# Enforcement of Strict Append-Only Integrity
@event.listens_for(Interaction, "before_update")
def block_interaction_update(mapper, connection, target):
    raise PermissionError("Audit Trail Integrity Violation: Table 'interactions' is strictly append-only. SQL UPDATE is prohibited.")


@event.listens_for(Interaction, "before_delete")
def block_interaction_delete(mapper, connection, target):
    raise PermissionError("Audit Trail Integrity Violation: Table 'interactions' is strictly append-only. SQL DELETE is prohibited.")


class MasterySnapshot(Base):
    """Current mastery state per student and KC."""
    __tablename__ = "mastery_snapshot"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    student_id = Column(String(36), ForeignKey("students.id"), nullable=False, index=True)
    kc_id = Column(String(64), ForeignKey("kc.id"), nullable=False, index=True)
    current_mastery = Column(Float, nullable=False, default=0.25)
    confidence = Column(String(16), nullable=False, default="high")  # 'high' or 'low'
    last_updated_at = Column(DateTime, default=utc_now, nullable=False)

    student = relationship("Student", back_populates="mastery_snapshots")


class AgentLog(Base):
    """Audit logs for RAG agent calls (T1, T2, T3)."""
    __tablename__ = "agent_logs"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    trigger_type = Column(String(16), nullable=False)  # 'T1', 'T2', 'T3'
    prompt_hash = Column(String(64), nullable=True)
    model_id = Column(String(64), nullable=False, default="unknown")
    raw_output = Column(Text, nullable=True)
    is_accepted = Column(Boolean, nullable=False, default=True)
    rejection_reason = Column(String(255), nullable=True)
    latency_ms = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, default=utc_now, nullable=False)


class HintEvent(Base):
    """Server-side record of every hint served to a student for an item.

    The mastery update uses this table (not a client-supplied flag) to decide whether
    the assistance factor h = 0.5 applies.
    """
    __tablename__ = "hint_events"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    student_id = Column(String(36), ForeignKey("students.id"), nullable=False, index=True)
    item_id = Column(String(64), ForeignKey("items.id"), nullable=False, index=True)
    session_id = Column(String(36), nullable=True, index=True)
    hint_level = Column(Integer, nullable=False)
    source = Column(String(32), nullable=False)  # 'llm_9router' | 'fallback_static'
    created_at = Column(DateTime, default=utc_now, nullable=False)


class AuthEvent(Base):
    """
    Append-style log of logins, failed logins, device replacements and PIN changes.
    Lets the study show that every answer came from an authenticated device.
    """
    __tablename__ = "auth_events"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    actor = Column(String(16), nullable=False)          # 'teacher' | 'student'
    student_id = Column(String(36), ForeignKey("students.id"), nullable=True, index=True)
    event = Column(String(48), nullable=False)          # e.g. 'login_ok', 'login_fail', 'device_replaced'
    detail = Column(String(255), nullable=True)
    ip = Column(String(64), nullable=True)
    created_at = Column(DateTime, default=utc_now, nullable=False, index=True)
