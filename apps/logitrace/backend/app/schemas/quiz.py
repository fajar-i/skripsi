"""
LogiTrace: Pydantic v2 Schemas for Student Quiz API.
Ensures zero answer leakage in public item retrieval schemas.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class ItemPresentation(BaseModel):
    """Schema served to student smartphone: strictly excludes correct answer!"""
    item_id: str
    sequence_number: int
    is_calibration: bool
    primary_kc: str
    kc_name: str
    difficulty: int
    prompt_text: str
    options: Dict[str, str]
    session_id: Optional[str] = None
    max_items: int = 20
    is_completed: bool = False


class SubmitAnswerRequest(BaseModel):
    student_code: str = Field(..., examples=["std_01"])
    item_id: str = Field(..., examples=["ITEM_WLAN_STANDARDS_1_01"])
    choice: str = Field(..., min_length=1, max_length=1, examples=["A"])
    session_id: Optional[str] = None
    response_time_ms: int = Field(default=0, ge=0)
    used_hint: bool = Field(default=False)
    hint_level: int = Field(default=0, ge=0, le=3)


class SubmitAnswerResponse(BaseModel):
    is_correct: bool
    correct_choice: str
    explanation: Optional[str] = None
    predicted_p: float
    mastery_before: float
    mastery_after: float
    mastery_delta: float
    is_calibration: bool
    sequence_number: int
    is_completed: bool = False
    session_id: Optional[str] = None


class HintRequest(BaseModel):
    student_code: str = Field(..., examples=["std_01"])
    item_id: str = Field(..., examples=["ITEM_WLAN_STANDARDS_1_01"])
    requested_level: int = Field(default=1, ge=1, le=3)


class HintResponse(BaseModel):
    item_id: str
    hint_level: int
    hint_text: str
    source: str  # "rag_llm" or "fallback_static"
    word_count: int
