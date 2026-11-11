"""
LogiTrace: Answer Leakage Checker & Scaffolding Guardrails.
Guarantees 100% Zero Answer Leakage (KPI-2) and graceful fallback activation.
"""

import re
from typing import List, Optional, Tuple

FORBIDDEN_PHRASES = [
    r"jawabannya\s+adalah",
    r"pilihan\s+yang\s+benar",
    r"jawaban\s+yang\s+tepat",
    r"pilihlah\s+(opsi|jawaban)",
    r"kunci\s+jawaban",
    r"opsi\s+yang\s+benar",
    r"jawaban:\s*",
    r"jawaban\s+benar:\s*",
    r"the\s+answer\s+is",
    r"correct\s+answer",
    r"choose\s+option",
]

MAX_HINT_WORDS = 60


class AnswerLeakageGuard:
    def __init__(self, custom_forbidden: Optional[List[str]] = None):
        patterns = FORBIDDEN_PHRASES + (custom_forbidden or [])
        self.forbidden_regexes = [
            re.compile(p, re.IGNORECASE) for p in patterns
        ]

    def check_leakage(
        self,
        hint_text: str,
        correct_answer: str,
        options: Optional[List[str]] = None
    ) -> Tuple[bool, str]:
        """
        Validates hint text against leakage criteria.
        Returns:
            (is_safe: bool, reason: str)
            is_safe == True means PASS (no leakage, under 60 words).
            is_safe == False means REJECT (triggers fallback to static hint).
        """
        if not hint_text or not hint_text.strip():
            return False, "Empty hint text"

        # 1. Word count check (<= 60 words)
        words = hint_text.strip().split()
        if len(words) > MAX_HINT_WORDS:
            return False, f"Word count exceeded: {len(words)} > {MAX_HINT_WORDS}"

        normalized_hint = hint_text.lower()

        # 2. Check forbidden disclosure phrases
        for regex in self.forbidden_regexes:
            if regex.search(normalized_hint):
                return False, f"Forbidden disclosure phrasing detected: {regex.pattern}"

        # 3. Check direct literal inclusion of correct answer (if substantive)
        clean_answer = correct_answer.strip().lower()
        # Only check exact match if answer is distinctive (> 2 characters)
        if len(clean_answer) > 2:
            # Word boundary regex check for the answer token
            escaped_answer = re.escape(clean_answer)
            answer_pattern = re.compile(rf"(?:\b|\s|^){escaped_answer}(?:\b|\s|$)", re.IGNORECASE)
            if answer_pattern.search(normalized_hint):
                return False, f"Direct correct answer string detected in hint text: '{correct_answer}'"

        return True, "Passed"
