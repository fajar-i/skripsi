"""
LogiTrace: Pydantic Schemas for Teacher Ambient Awareness Dashboard (US-04).
Implements minimal cognitive load priority cards and 34 x 12 heatmap payload.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel


class TopStuckStudent(BaseModel):
    student_code: str
    stuck_kc_id: str
    stuck_kc_name: str
    current_mastery: float
    consecutive_errors: int
    recommended_action: str  # Actionable guidance for roving teacher in Zone B


class HeatmapCell(BaseModel):
    student_code: str
    kc_id: str
    mastery: float
    confidence: str  # "high" or "low" (striped pattern on UI)


class TeacherAmbientState(BaseModel):
    class_rombel: str = "XI TKJ 1"
    active_students_count: int
    class_average_mastery: float
    top_stuck_students: List[TopStuckStudent]
    heatmap: List[HeatmapCell]
    timestamp: str
    session_id: Optional[str] = None
    session_title: Optional[str] = None
    session_number: Optional[int] = None
    not_started_count: Optional[int] = None
    in_progress_count: Optional[int] = None
    completed_count: Optional[int] = None
