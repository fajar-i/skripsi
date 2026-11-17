"""
Unit tests for SecureLLMClient (9router-only) and PIIScrubber.
"""

import asyncio
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.app.rag import secure_client as sc  # noqa: E402
from backend.app.rag.secure_client import PIIScrubber, SecureLLMClient, mask_secret  # noqa: E402
from backend.app.rag.hint_service import HintService, GENERIC_HINT  # noqa: E402


def test_pii_scrubber_redaction():
    dirty_text = (
        "Siswa S07 (kode std_07) bernama Budi Santoso (NISN 0061234567, no hp 081234567890, "
        "email budi@smk4.sch.id) di SMK Negeri 4 Bandung sedang bingung pada soal WLAN frekuensi 2.4 GHz."
    )
    clean_text, had_pii = PIIScrubber.scrub(dirty_text)

    assert had_pii is True
    for leaked in ("0061234567", "081234567890", "budi@smk4.sch.id", "SMK Negeri 4 Bandung",
                   "S07", "std_07", "Budi", "Santoso"):
        assert leaked not in clean_text, leaked
    assert "2.4 GHz" in clean_text


@pytest.mark.parametrize("text,leaked", [
    ("NISN: 0061 2345 67", "0061 2345 67"),
    ("NIK 3273-0112-3456-0001", "3273-0112-3456-0001"),
    ("hp +62 812-3456-7890", "812-3456-7890"),
    ("SMKN 4 Bandung", "SMKN 4 Bandung"),
    ("SMK Negeri 4 Kota Bandung", "Bandung"),
    ("Nama saya Siti Aminah", "Siti"),
])
def test_pii_scrubber_format_variants(text, leaked):
    clean, had_pii = PIIScrubber.scrub(text)
    assert had_pii is True
    assert leaked not in clean


@pytest.mark.parametrize("text", [
    "Sebuah access point mengalami tabrakan frame pada kanal 6 di frekuensi 2.4 GHz.",
    "Throughput 1300000000 bps pada 802.11ac dengan subnet 192.168.100.0/24.",
    "Ping dengan ukuran paket 1472 byte dan TTL 64 menghasilkan RTT 12 ms.",
])
def test_pii_scrubber_leaves_technical_text_untouched(text):
    res, had_pii = PIIScrubber.scrub(text)
    assert had_pii is False
    assert res == text


def test_prompt_length_cap():
    res, _ = PIIScrubber.scrub("a" * 5000)
    assert len(res) == sc.MAX_PROMPT_CHARS


def test_secret_key_masking():
    assert mask_secret(None) == "<EMPTY>"
    assert mask_secret("") == "<EMPTY>"
    assert mask_secret("short") == "****"
    assert mask_secret("sk-deepseek-1234567890abcdef") == "****cdef"


def test_output_sanitization():
    client = SecureLLMClient()
    dirty_output = '```json\n{"petunjuk": "<script>alert(1)</script> Perhatikan pita frekuensi."}\n```'
    clean = client.sanitize_output(dirty_output)
    assert "<script>" not in clean
    assert "&lt;script&gt;" in clean
    assert "```" not in clean


def test_9router_is_the_only_provider(monkeypatch):
    monkeypatch.setenv("NINEROUTER_API_KEY", "sk-test-9router-key-12345678")
    monkeypatch.setenv("NINEROUTER_MODEL", "ag/gemini-3.8-flash")
    monkeypatch.setenv("NINEROUTER_API_URL", "http://localhost:20128/v1/chat/completions")
    client = SecureLLMClient()
    assert client.provider == "9router"
    assert client.endpoint_url == "http://localhost:20128/v1/chat/completions"
    assert client.model_name == "ag/gemini-3.8-flash"
    assert not hasattr(sc, "PROVIDERS")  # no Ollama / DeepSeek / Groq table any more


@pytest.mark.asyncio
async def test_missing_key_returns_error_without_network(monkeypatch):
    monkeypatch.setenv("NINEROUTER_API_KEY", "")
    text, lat, err = await SecureLLMClient().call_chat("sys", "user")
    assert text is None
    assert "NINEROUTER_API_KEY" in err


@pytest.mark.asyncio
async def test_total_deadline_is_enforced(monkeypatch):
    """A provider that never answers must be cut at the SLA, not at a per-phase timeout."""
    monkeypatch.setenv("NINEROUTER_API_KEY", "sk-test-9router-key-12345678")
    client = SecureLLMClient()

    async def slow_post(*args, **kwargs):
        await asyncio.sleep(10)

    monkeypatch.setattr(client, "_post", slow_post)
    text, lat_ms, err = await client.call_chat("sys", "user", timeout_seconds=0.3)
    assert text is None
    assert "Timeout" in err
    assert lat_ms < 600


@pytest.mark.asyncio
async def test_hint_service_fallback_on_missing_key():
    service = HintService()  # conftest blanks the key -> offline
    hint, source, lat_ms, reason = await service.generate_socratic_hint(
        kc_id="WLAN_STANDARDS",
        kc_name="WLAN Standards",
        level=1,
        prompt_text="Siswa S01 kesulitan membedakan 802.11n vs 802.11ax.",
        correct_answer_text="802.11ax",
        options={"A": "802.11b", "B": "802.11ax"},
    )
    assert source == "fallback_static"
    assert "NINEROUTER_API_KEY" in reason
    assert len(hint) > 10
    assert lat_ms < 100


@pytest.mark.asyncio
async def test_hint_service_rejects_leaky_llm_output(monkeypatch):
    service = HintService()

    async def fake_call_api(**kwargs):
        return "Pilih kanal 11 karena tidak tumpang tindih.", 120, None

    monkeypatch.setattr(service.client, "call_api", fake_call_api)
    hint, source, _, reason = await service.generate_socratic_hint(
        kc_id="WLAN_FREQ_CHANNEL", kc_name="Kanal", level=1, prompt_text="Kanal mana?",
        correct_answer_text="Kanal 11", options={"A": "Kanal 3", "B": "Kanal 11"},
    )
    assert source == "fallback_static"
    assert reason.startswith("Leakage guard")
    assert "kanal 11" not in hint.lower()


def test_static_fallback_is_guarded_per_item():
    """A static hint that names this item's answer must be replaced by the generic hint."""
    service = HintService()
    service.static_hints = {"ICMP_CONNECTIVITY": {"1": "Perhatikan keluaran perintah ping dan nilai RTT."}}
    hint = service.get_static_fallback_hint(
        "ICMP_CONNECTIVITY", 1, correct_answer_text="ping",
        options={"A": "ping", "B": "tracert", "C": "ipconfig", "D": "netstat"},
    )
    assert hint == GENERIC_HINT


@pytest.mark.asyncio
async def test_deadline_holds_under_17_concurrent_requests(monkeypatch):
    """Regression: per-request AsyncClient creation (~0.5 s sync SSL load) once made
    17 concurrent hints wait ~10 s despite a 3 s deadline. Every call must return near the deadline."""
    import time

    async def handler(reader, writer):
        try:
            await reader.read(65536)
            await asyncio.sleep(5)  # provider never answers in time
        except Exception:
            pass
        finally:
            writer.close()

    server = await asyncio.start_server(handler, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    monkeypatch.setenv("NINEROUTER_API_URL", f"http://127.0.0.1:{port}/v1/chat/completions")
    monkeypatch.setenv("NINEROUTER_API_KEY", "sk-test-9router-key-12345678")
    client = SecureLLMClient()

    async def one():
        t0 = time.perf_counter()
        _, _, err = await client.call_chat("s", "u", timeout_seconds=0.4)
        return time.perf_counter() - t0, err

    try:
        results = await asyncio.gather(*[one() for _ in range(17)])
    finally:
        server.close()
    assert all("Timeout" in err for _, err in results)
    assert max(w for w, _ in results) < 0.7
