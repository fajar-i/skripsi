"""
Unit Tests for Answer Leakage Guard & Scaffolding Filters (KPI-2).
Verifies 100% Zero Answer Leakage and strict word count limit (<= 60 words).
"""

import pytest
from backend.app.rag.guardrails import AnswerLeakageGuard, MAX_HINT_WORDS


@pytest.fixture
def guard():
    return AnswerLeakageGuard()


def test_clean_socratic_hint_passes(guard):
    """Socratic hint guiding without disclosure should pass."""
    hint = "Perhatikan perbedaan antara frekuensi 2.4 GHz dan 5 GHz dalam hal jangkauan dan interferensi."
    is_safe, reason = guard.check_leakage(hint, correct_answer="802.11ax")
    assert is_safe is True
    assert reason == "Passed"


def test_forbidden_disclosure_phrasing_rejected(guard):
    """Phrases like 'jawabannya adalah' or 'pilihan yang benar' must be rejected."""
    bad_hints = [
        "Jawabannya adalah opsi kedua karena frekuensi lebih tinggi.",
        "Pilihan yang benar yaitu standar nirkabel generasi keenam.",
        "Kunci jawaban untuk soal ini adalah konfigurasi BSS.",
        "The correct answer is channel 6.",
    ]
    for bad in bad_hints:
        is_safe, reason = guard.check_leakage(bad, correct_answer="WPA3")
        assert is_safe is False
        assert "Forbidden" in reason or "detected" in reason


def test_direct_answer_token_leakage_rejected(guard):
    """Direct mention of the correct answer string must be rejected."""
    hint = "Kamu harus memilih WPA3-SAE karena memberikan keamanan terhadap kamus offline."
    is_safe, reason = guard.check_leakage(hint, correct_answer="WPA3-SAE")
    assert is_safe is False
    assert "Direct correct answer" in reason


def test_word_count_exceeded_rejected(guard):
    """Hints longer than 60 words must be rejected."""
    long_hint = " ".join(["kata"] * (MAX_HINT_WORDS + 5))
    is_safe, reason = guard.check_leakage(long_hint, correct_answer="802.11b")
    assert is_safe is False
    assert "Word count exceeded" in reason


def test_option_text_leakage_rejected(guard):
    """Verbatim option texts (>= 4 chars) must be rejected, as described in the paper."""
    hint = "Bandingkan dengan IEEE 802.11a yang bekerja di pita lain."
    is_safe, reason = guard.check_leakage(
        hint, correct_answer="IEEE 802.11g",
        options=["IEEE 802.11g", "IEEE 802.11a", "IEEE 802.11ac", "IEEE 802.11ax"],
    )
    assert is_safe is False
    assert "Option text" in reason


def test_answer_must_match_whole_phrase(guard):
    """'ping' inside 'mapping' is not a leak; standalone 'ping' is."""
    assert guard.check_leakage("Perhatikan mapping alamat pada tabel ARP.", correct_answer="ping")[0] is True
    assert guard.check_leakage("Gunakan ping untuk menguji.", correct_answer="ping")[0] is False
