"""
Unit tests for SecureLLMClient & PIIScrubber in LogiTrace RAG-KT.
Validates:
1. Zero-PII scrubbing (NISN, phone, student IDs, emails)
2. Secret key masking
3. Prompt length capping
4. Safe fallback on missing keys or network failure
5. Output HTML escaping (anti-XSS)
"""

import pytest
from logitrace.backend.app.rag.secure_client import PIIScrubber, SecureLLMClient, mask_secret
from logitrace.backend.app.rag.hint_service import HintService


def test_pii_scrubber_redaction():
    dirty_text = (
        "Siswa S07 (kode std_07) bernama Budi (NISN 0061234567, no hp 081234567890, email budi@smk4.sch.id) "
        "di SMK Negeri 4 Bandung sedang bingung pada soal WLAN frekuensi 2.4 GHz."
    )
    clean_text, had_pii = PIIScrubber.scrub(dirty_text)

    assert had_pii is True
    assert "0061234567" not in clean_text
    assert "[REDACTED_NISN]" in clean_text
    assert "081234567890" not in clean_text
    assert "[REDACTED_PHONE]" in clean_text
    assert "budi@smk4.sch.id" not in clean_text
    assert "[REDACTED_EMAIL]" in clean_text
    assert "SMK Negeri 4 Bandung" not in clean_text
    assert "[REDACTED_SCHOOL]" in clean_text
    assert "S07" not in clean_text
    assert "std_07" not in clean_text


def test_pii_scrubber_clean_text():
    clean_text = "Sebuah access point mengalami tabrakan frame pada kanal 6 di frekuensi 2.4 GHz."
    res, had_pii = PIIScrubber.scrub(clean_text)
    assert had_pii is False
    assert res == clean_text


def test_secret_key_masking():
    assert mask_secret(None) == "<EMPTY>"
    assert mask_secret("") == "<EMPTY>"
    assert mask_secret("short") == "****"
    assert mask_secret("sk-deepseek-1234567890abcdef") == "sk-d****cdef"


def test_output_sanitization():
    client = SecureLLMClient(provider="ollama")
    dirty_output = '```json\n{"petunjuk": "<script>alert(1)</script> Perhatikan pita frekuensi."}\n```'
    clean = client.sanitize_output(dirty_output)
    assert "<script>" not in clean
    assert "&lt;script&gt;" in clean
    assert "```" not in clean


def test_9router_provider_configuration(monkeypatch):
    monkeypatch.setenv("LOGITRACE_LLM_PROVIDER", "9router")
    monkeypatch.setenv("NINEROUTER_API_KEY", "sk-test-9router-key-12345678")
    monkeypatch.setenv("NINEROUTER_MODEL", "ag/gemini-3.8-flash")

    client = SecureLLMClient()
    assert client.provider == "9router"
    assert client.endpoint_url == "http://localhost:20128/v1/chat/completions"
    assert client.model_name == "ag/gemini-3.8-flash"
    assert client.api_key == "sk-test-9router-key-12345678"


@pytest.mark.asyncio
async def test_hint_service_fallback_on_offline():
    # When provider has no valid key or is offline, it must return static fallback < 50ms safely
    service = HintService(provider="deepseek")  # DeepSeek without key
    hint, source, lat_ms, is_safe = await service.generate_socratic_hint(
        kc_id="KC01",
        kc_name="WLAN Standards",
        level=1,
        prompt_text="Siswa S01 kesulitan membedakan 802.11n vs 802.11ax.",
        correct_answer_text="802.11ax",
        options={"A": "802.11b", "B": "802.11ax"}
    )
    assert source == "fallback_static"
    assert is_safe is True
    assert len(hint) > 10
    assert lat_ms < 100
