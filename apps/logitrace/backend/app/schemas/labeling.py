"""
LogiTrace: Pydantic Schemas for Agent T1 (Semantic Item Labeling & Teacher Review - US-05).
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class ItemLabelRequest(BaseModel):
    prompt_text: str = Field(..., min_length=10, description="Teks pertanyaan / skenario butir soal")
    options: Dict[str, str] = Field(..., description="Pilihan jawaban A, B, C, D")
    explanation: Optional[str] = Field(None, description="Pembahasan atau rasional butir soal")


class ItemLabelResult(BaseModel):
    primary_kc_id: str
    primary_kc_name: str
    secondary_kc_ids: List[str]
    bloom_level: str         # suggested C1..C5 (rule-based, needs teacher review)
    nominal_difficulty: int  # 1, 2, or 3
    confidence: float        # 0.0 - 1.0
    needs_teacher_review: bool
    rationale: str
    source: str              # "semantic_classifier" (rule-based keyword matcher)
    latency_ms: int


class ReviewQueueItem(BaseModel):
    item_id: str
    prompt_text: str
    options: Dict[str, str]
    current_primary_kc_id: str
    current_indikator_id: Optional[str] = None
    current_bloom_level: Optional[str] = None
    current_jonassen_phase: Optional[str] = None
    current_difficulty: int
    confidence: float
    status: str  # "pending_review", "approved", "modified"


class LabelApprovalRequest(BaseModel):
    primary_kc_id: str = Field(..., description="ID Knowledge Component utama")
    bloom_level: str = Field(..., pattern=r"^C[1-6]$", description="Level kognitif Bloom revisi (C1-C6)")
    indikator_id: Optional[str] = Field(None, description="ID indikator kompetensi, mis. IND-04.3")
    jonassen_phase: Optional[str] = Field(None, description="Fase troubleshooting Jonassen & Hung (2006)")
    difficulty_nominal: int = Field(..., ge=1, le=3, description="Tingkat kesulitan nominal (1, 2, atau 3)")
    teacher_notes: Optional[str] = None
