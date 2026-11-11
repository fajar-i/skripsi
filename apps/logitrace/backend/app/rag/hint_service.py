"""
LogiTrace: Socratic Hint Service (Agent T2) & Graceful Fallback Manager.
Integrates SecureLLMClient (Zero-PII Cloud Inference / Ollama) with strict 3.0s SLA
and instant fallback (< 50 ms) to curated static hint bank.
"""

import json
import logging
import os
import time
from typing import Dict, List, Optional, Tuple

from .guardrails import AnswerLeakageGuard
from .secure_client import PIIScrubber, SecureLLMClient

logger = logging.getLogger("hint_service")

FALLBACK_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "fallback_hints", "static_hints.json")
)


class HintService:
    def __init__(self, provider: Optional[str] = None):
        self.guard = AnswerLeakageGuard()
        self.client = SecureLLMClient(provider=provider)
        self.static_hints: Dict[str, Dict[str, str]] = {}
        self._load_static_hints()

    def _load_static_hints(self):
        if os.path.exists(FALLBACK_PATH):
            try:
                with open(FALLBACK_PATH, "r", encoding="utf-8") as f:
                    self.static_hints = json.load(f)
            except Exception as e:
                logger.error(f"Failed to load static hints from {FALLBACK_PATH}: {e}")

    def get_static_fallback_hint(self, kc_id: str, level: int) -> str:
        """Instant fallback (< 50 ms) to curated static hint bank."""
        level_str = str(level)
        kc_hints = self.static_hints.get(kc_id, {})
        if level_str in kc_hints:
            return kc_hints[level_str]
        # Generic pedagogical fallback if KC missing
        return (
            "Tinjau kembali konsep dasar dan spesifikasi teknis terkait "
            "untuk menganalisis perbedaan parameter pada soal ini secara bertahap."
        )

    async def generate_socratic_hint(
        self,
        kc_id: str,
        kc_name: str,
        level: int,
        prompt_text: str,
        correct_answer_text: str,
        options: Dict[str, str],
        timeout_seconds: float = 3.0,
        kc_description: Optional[str] = None,
    ) -> Tuple[str, str, int, bool]:
        """
        Attempts Secure Cloud / Local LLM generation with 3.0s timeout and strict leakage guard.
        Falls back to curated static hints on timeout, error, missing key, or leakage.
        Returns: (hint_text, source: 'rag_llm' | 'fallback_static', latency_ms, is_safe)
        """
        start_time = time.perf_counter()

        # Call Secure LLM Client (Pre-flight Zero-PII sanitization & TLS enforced)
        raw_text, lat_ms, err = await self.client.call_api(
            topic=kc_name,
            level=level,
            question_text=prompt_text,
            timeout_seconds=timeout_seconds,
            kc_description=kc_description,
        )

        # Verify LLM response against Answer Leakage Guard & Sanitize Output
        if raw_text and not err:
            is_safe, reason = self.guard.check_leakage(
                raw_text,
                correct_answer=correct_answer_text,
                options=list(options.values()),
            )
            if is_safe:
                clean_output = self.client.sanitize_output(raw_text)
                return clean_output, "rag_llm", lat_ms, True
            else:
                logger.warning(f"LLM hint dropped due to leakage guard: {reason}")

        # Fallback triggered (< 50 ms)
        fallback_text = self.get_static_fallback_hint(kc_id, level)
        total_lat_ms = int((time.perf_counter() - start_time) * 1000)
        return fallback_text, "fallback_static", total_lat_ms, True


hint_service = HintService()
