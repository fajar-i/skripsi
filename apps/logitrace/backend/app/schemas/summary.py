"""
LogiTrace: Pydantic Schemas for Agent T3 (Session Reflection & Peer-Tutoring - US-06).
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class KCMasteryMetric(BaseModel):
    kc_id: str
    kc_name: str
    avg_mastery: float
    student_count: int
    struggling_count: int  # students with m < 0.40
    mastered_count: int    # students with m >= 0.70


class PeerTutoringMatch(BaseModel):
    kc_id: str
    kc_name: str
    tutor_student_code: str
    tutor_mastery: float
    mentee_student_codes: List[str]
    mentee_avg_mastery: float
    action_guidance: str


class SessionSummaryResponse(BaseModel):
    session_id: str
    session_title: str
    class_rombel: str
    total_students: int
    completed_students: int
    in_progress_students: int
    not_started_students: int
    class_avg_mastery: float
    accuracy_rate: float
    total_responses: int
    avg_response_time_ms: int
    strengths: List[KCMasteryMetric]
    bottlenecks: List[KCMasteryMetric]
    narrative_summary: str
    peer_tutoring_recommendations: List[PeerTutoringMatch]
    source: str  # "rag_llm" or "deterministic_fallback"
    latency_ms: int
    timestamp: str
