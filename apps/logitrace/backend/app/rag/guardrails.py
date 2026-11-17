"""
LogiTrace: Answer Leakage Checker & Scaffolding Guardrails.

Rule-based (regex + literal match) check. It catches explicit disclosure phrases and
verbatim mentions of the answer key or option texts. It does NOT detect paraphrased
or semantic leakage.
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
MIN_ANSWER_CHARS = 3   # answer key texts shorter than this are too generic to match
MIN_OPTION_CHARS = 4   # option texts shorter than this are skipped


def _contains_phrase(haystack: str, phrase: str) -> bool:
    """Case-insensitive whole-phrase match (phrase boundaries, not substrings of words)."""
    escaped = re.escape(phrase.strip().lower())
    return re.search(rf"(?<![\w]){escaped}(?![\w])", haystack) is not None


class AnswerLeakageGuard:
    def __init__(self, custom_forbidden: Optional[List[str]] = None):
        patterns = FORBIDDEN_PHRASES + (custom_forbidden or [])
        self.forbidden_regexes = [re.compile(p, re.IGNORECASE) for p in patterns]

    def check_leakage(
        self,
        hint_text: str,
        correct_answer: str,
        options: Optional[List[str]] = None,
    ) -> Tuple[bool, str]:
        """
        Returns (is_safe, reason). is_safe == False means the hint must not be shown.
        Checks, in order: empty text, > 60 words, disclosure phrases,
        verbatim answer key (>= 3 chars), verbatim option text (>= 4 chars).
        """
        if not hint_text or not hint_text.strip():
            return False, "Empty hint text"

        words = hint_text.strip().split()
        if len(words) > MAX_HINT_WORDS:
            return False, f"Word count exceeded: {len(words)} > {MAX_HINT_WORDS}"

        normalized_hint = hint_text.lower()

        for regex in self.forbidden_regexes:
            if regex.search(normalized_hint):
                return False, f"Forbidden disclosure phrasing detected: {regex.pattern}"

        clean_answer = (correct_answer or "").strip()
        if len(clean_answer) >= MIN_ANSWER_CHARS and _contains_phrase(normalized_hint, clean_answer):
            return False, f"Direct correct answer string detected in hint text: '{correct_answer}'"

        for opt in options or []:
            opt_clean = (opt or "").strip()
            if len(opt_clean) >= MIN_OPTION_CHARS and _contains_phrase(normalized_hint, opt_clean):
                return False, f"Option text detected in hint text: '{opt_clean[:60]}'"

        return True, "Passed"
