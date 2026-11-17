"""
LogiTrace: Socratic Hint Service (Agent T2) & Fallback Manager.

Tries the 9router LLM with a hard 3.0 s deadline. On timeout, error, missing key or a
failed leakage check, it falls back to the curated static hint bank. Static hints are
also passed through the leakage guard; if a static hint would leak for this item,
a generic hint is used instead.
"""

import json
import logging
import os
import time
from typing import Dict, Optional, Tuple

from .guardrails import AnswerLeakageGuard
from .secure_client import SecureLLMClient

logger = logging.getLogger("hint_service")

FALLBACK_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "fallback_hints", "static_hints.json")
)

GENERIC_HINT = (
    "Tinjau kembali konsep dasar dan spesifikasi teknis terkait "
    "untuk menganalisis perbedaan parameter pada soal ini secara bertahap."
)


class HintService:
    def __init__(self, client: Optional[SecureLLMClient] = None):
        self.guard = AnswerLeakageGuard()
        self.client = client or SecureLLMClient()
        self.static_hints: Dict[str, Dict[str, str]] = {}
        self._load_static_hints()

    def _load_static_hints(self):
        if os.path.exists(FALLBACK_PATH):
            try:
                with open(FALLBACK_PATH, "r", encoding="utf-8") as f:
                    self.static_hints = json.load(f)
            except Exception as e:
                logger.error(f"Failed to load static hints from {FALLBACK_PATH}: {e}")

    def get_static_fallback_hint(
        self,
        kc_id: str,
        level: int,
        correct_answer_text: str = "",
        options: Optional[Dict[str, str]] = None,
    ) -> str:
        """Static hint for (KC, level), guarded against leaking this item's answer/options."""
        hint = self.static_hints.get(kc_id, {}).get(str(level))
        if not hint:
            return GENERIC_HINT
        is_safe, reason = self.guard.check_leakage(
            hint, correct_answer=correct_answer_text, options=list((options or {}).values())
        )
        if not is_safe:
            logger.warning(f"Static hint {kc_id}/L{level} rejected for this item: {reason}")
            return GENERIC_HINT
        return hint

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
    ) -> Tuple[str, str, int, Optional[str]]:
        """
        Returns: (hint_text, source: 'llm_9router' | 'fallback_static', latency_ms, fallback_reason)
        latency_ms is the total time the student waits, including any failed LLM attempt.
        """
        start_time = time.perf_counter()

        raw_text, _, err = await self.client.call_api(
            topic=kc_name,
            level=level,
            question_text=prompt_text,
            timeout_seconds=timeout_seconds,
            kc_description=kc_description,
        )

        reason = err
        if raw_text and not err:
            is_safe, guard_reason = self.guard.check_leakage(
                raw_text, correct_answer=correct_answer_text, options=list(options.values())
            )
            if is_safe:
                total_ms = int((time.perf_counter() - start_time) * 1000)
                return self.client.sanitize_output(raw_text), "llm_9router", total_ms, None
            reason = f"Leakage guard: {guard_reason}"
            logger.warning(f"LLM hint dropped: {guard_reason}")
        elif not raw_text and not err:
            reason = "Empty LLM response"

        fallback_text = self.get_static_fallback_hint(kc_id, level, correct_answer_text, options)
        total_ms = int((time.perf_counter() - start_time) * 1000)
        return fallback_text, "fallback_static", total_ms, reason


hint_service = HintService()
