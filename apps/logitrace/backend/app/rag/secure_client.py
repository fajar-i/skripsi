"""
LogiTrace: Secure LLM API Client (9router single-provider).

All LLM calls go through one OpenAI-compatible endpoint: the local 9router proxy.
There is no local-CPU (Ollama) mode and no direct cloud provider mode.

Protections, in request order:
1. Outbound PII redaction (PIIScrubber) + prompt length cap.
2. API key kept server-side, masked in logs.
3. Hard end-to-end deadline (asyncio.wait_for), not only per-phase httpx timeouts.
4. Post-flight leakage check (done by the caller via AnswerLeakageGuard) and HTML escaping.
5. Caller falls back to the static hint bank / deterministic template on any failure.
"""

import asyncio
import html
import logging
import os
import re
import ssl
import time
from typing import Optional, Tuple

from dotenv import load_dotenv
import certifi
import httpx

load_dotenv()

logger = logging.getLogger("secure_llm_client")

# ---------------------------------------------------------------------------
# 1. PII PATTERNS (OUTBOUND REDACTION)
# ---------------------------------------------------------------------------
# Order matters: labelled/specific patterns run before the bare-digit patterns.
PII_PATTERNS = [
    # Email addresses
    (re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"), "[REDACTED_EMAIL]"),
    # Labelled identifiers, digits may be split by spaces/dashes: "NISN 0061 2345 67", "NIK: 3273-..."
    (re.compile(r"\b(NISN|NIK|NIS|NIP)(\s*[:=]?\s*)\d[\d\s\-]{5,22}\d", re.IGNORECASE),
     r"\1\2[REDACTED_ID_NUMBER]"),
    # Phone numbers: +62 / 62 / 08xx, allowing spaces and dashes
    (re.compile(r"(?<![\w.])(?:\+62|62|0)\s?8\d{1,3}[\s\-]?\d{3,4}[\s\-]?\d{3,5}\b"), "[REDACTED_PHONE]"),
    # Unlabelled NIK (16 digits) and NISN (10 digits with the usual '00' prefix)
    (re.compile(r"\b\d{16}\b"), "[REDACTED_NIK]"),
    (re.compile(r"\b00\d{8}\b"), "[REDACTED_NISN]"),
    # Student identity tags: 'Siswa S01', 'std_07', 'absen 12'
    (re.compile(r"\b(?:siswa|user|murid|absen)\s*[:=]?\s*(?:S|std_)?\d{1,3}\b", re.IGNORECASE),
     "[REDACTED_STUDENT_ID]"),
    (re.compile(r"\bstd_\d{1,3}\b", re.IGNORECASE), "[REDACTED_STUDENT_ID]"),
    # Explicit name introductions: 'nama saya Budi Santoso', 'bernama Budi', 'Nama: Siti Aminah'
    (re.compile(
        r"\b((?:[Nn]ama\s+saya|[Nn]amaku|[Bb]ernama|[Nn]ama\s*[:=])\s*)"
        r"[A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3}"
    ), r"\1[REDACTED_NAME]"),
    # School names: 'SMK Negeri 4 Bandung', 'SMKN 4 Bandung', 'SMAN 1 Kota Bandung', 'SMK Telkom Bandung'
    (re.compile(
        r"\b(?:SMK|SMA|SMP|SD|MTs|MA|MI)N?\s+(?:Negeri\s+|Swasta\s+)?(?:\d+\s+)?"
        r"(?:Kota\s+|Kabupaten\s+|Kab\.\s+)?[A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)?"
    ), "[REDACTED_SCHOOL]"),
]

MAX_PROMPT_CHARS = 1000


class PIIScrubber:
    """Outbound redaction layer. Best-effort: regex cannot catch every free-text name.

    The primary privacy control is data minimisation: T2 prompts contain only item-bank
    content, and T3 prompts contain only class aggregates (no student codes).
    """

    @classmethod
    def scrub(cls, text: str) -> Tuple[str, bool]:
        if not text:
            return "", False

        cleaned = text
        had_pii = False
        for pattern, replacement in PII_PATTERNS:
            if pattern.search(cleaned):
                had_pii = True
                cleaned = pattern.sub(replacement, cleaned)

        if len(cleaned) > MAX_PROMPT_CHARS:
            cleaned = cleaned[:MAX_PROMPT_CHARS]

        return cleaned, had_pii


# ---------------------------------------------------------------------------
# 2. PROVIDER CONFIGURATION (9router only)
# ---------------------------------------------------------------------------
def mask_secret(secret: Optional[str]) -> str:
    """Masks secrets for logging. Reveals at most the last 4 characters."""
    if not secret:
        return "<EMPTY>"
    if len(secret) <= 12:
        return "****"
    return f"****{secret[-4:]}"


# Requests abandoned at the deadline keep running in the background until httpx cleans up.
# Holding a reference prevents them from being garbage-collected mid-flight.
_ORPHANED: set = set()


def _reap_orphan(task: "asyncio.Future") -> None:
    _ORPHANED.discard(task)
    if not task.cancelled():
        task.exception()  # mark retrieved; abandoned requests' errors are irrelevant


DEFAULT_9ROUTER_URL = "http://localhost:20128/v1/chat/completions"
DEFAULT_9ROUTER_MODEL = "ag/gemini-3.8-flash-low"


class SecureLLMClient:
    """OpenAI-compatible client bound to the local 9router proxy."""

    provider = "9router"

    def __init__(self):
        self.endpoint_url = os.getenv("NINEROUTER_API_URL", DEFAULT_9ROUTER_URL)
        self.model_name = os.getenv("NINEROUTER_MODEL", DEFAULT_9ROUTER_MODEL)
        self.api_key = os.getenv("NINEROUTER_API_KEY", "")
        self._client: Optional[httpx.AsyncClient] = None
        self._client_loop = None
        # Build the SSL context once, at startup, so no request pays for it.
        self._ssl_context = ssl.create_default_context(cafile=certifi.where())

        logger.info(
            f"Initialized SecureLLMClient [Provider: 9ROUTER, Endpoint: {self.endpoint_url}, "
            f"Model: {self.model_name}, Key: {mask_secret(self.api_key)}]"
        )

    def _http(self) -> httpx.AsyncClient:
        """One shared HTTP client per event loop.

        Creating an httpx.AsyncClient loads an SSL context synchronously (~0.5 s on the
        4-core test laptop) and blocks the whole event loop. Creating one per request made
        17 concurrent hint requests wait ~10 s. The client is created once and reused.
        """
        loop = asyncio.get_running_loop()
        if self._client is None or self._client_loop is not loop or self._client.is_closed:
            self._client = httpx.AsyncClient(
                verify=self._ssl_context,
                limits=httpx.Limits(max_connections=64, max_keepalive_connections=32),
            )
            self._client_loop = loop
        return self._client

    async def _post(self, payload: dict, headers: dict, timeout_seconds: float) -> httpx.Response:
        return await self._http().post(
            self.endpoint_url, json=payload, headers=headers, timeout=timeout_seconds
        )

    async def call_chat(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int = 250,
        timeout_seconds: float = 5.0,
    ) -> Tuple[Optional[str], int, Optional[str]]:
        """
        Chat completion through 9router with PII redaction and a hard total deadline.
        Returns: (response_text | None, latency_ms, error_msg | None)
        """
        clean_user, had_pii = PIIScrubber.scrub(user_prompt)
        clean_sys, _ = PIIScrubber.scrub(system_prompt)
        if had_pii:
            logger.warning("Sanitizer redacted detected PII in chat call.")

        if not self.api_key:
            return None, 0, "Missing NINEROUTER_API_KEY"

        payload = {
            "model": self.model_name,
            "messages": [
                {"role": "system", "content": clean_sys},
                {"role": "user", "content": clean_user},
            ],
            "temperature": 0.0,
            "max_tokens": max_tokens,
            "stream": False,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        start_t = time.perf_counter()
        # Hard end-to-end deadline. asyncio.wait_for() is NOT used: on cancel it waits for
        # httpx to close the connection, which on Windows/under load can take as long as the
        # provider takes to answer (measured up to 10 s for a 0.5 s deadline). Instead the
        # request runs as a detached task; on deadline we cancel it and return immediately.
        task = asyncio.ensure_future(self._post(payload, headers, timeout_seconds))
        done, _ = await asyncio.wait({task}, timeout=timeout_seconds)
        if not done:
            task.cancel()
            _ORPHANED.add(task)
            task.add_done_callback(_reap_orphan)
            lat_ms = int((time.perf_counter() - start_t) * 1000)
            return None, lat_ms, f"Timeout exceeded ({timeout_seconds}s SLA)"
        try:
            res = task.result()
        except httpx.TimeoutException:
            lat_ms = int((time.perf_counter() - start_t) * 1000)
            return None, lat_ms, f"Timeout exceeded ({timeout_seconds}s SLA)"
        except Exception as e:
            lat_ms = int((time.perf_counter() - start_t) * 1000)
            return None, lat_ms, f"Connection error: {str(e)[:100]}"

        lat_ms = int((time.perf_counter() - start_t) * 1000)
        if res.status_code == 200:
            try:
                data = res.json()
                choices = data.get("choices", [])
                msg = choices[0].get("message", {}) if choices else {}
                text_out = (msg.get("content") or "").strip()
            except Exception as e:
                return None, lat_ms, f"Malformed provider response: {str(e)[:100]}"
            return text_out, lat_ms, None
        if res.status_code == 429:
            return None, lat_ms, "Rate limit reached (HTTP 429)"
        return None, lat_ms, f"Provider HTTP {res.status_code}: {res.text[:100]}"

    async def call_api(
        self,
        topic: str,
        level: int,
        question_text: str,
        timeout_seconds: float = 3.0,
        kc_description: Optional[str] = None,
    ) -> Tuple[Optional[str], int, Optional[str]]:
        """
        Socratic hint call (Agent T2). The prompt contains only item-bank content:
        KC name, KC description, hint level and the question stem. Options and the
        answer key are never sent.
        """
        system_content = (
            "Kamu adalah Guru Pendamping TKJ Sokratik. Berikan satu petunjuk bimbingan penalaran "
            "maksimal 60 kata dalam Bahasa Indonesia untuk membantu siswa memecahkan masalah tanpa membocorkan jawaban. "
            "Prinsip utama: Guiding, Not Solving. DILARANG KERAS menyebutkan jawaban benar, opsi yang benar, "
            "atau frasa 'jawabannya adalah'. Langsung berikan kalimat petunjuk tanpa pengantar."
        )
        kc_context = f"Konsep L1: {kc_description}\n" if kc_description else ""
        user_content = (
            f"Topik: {topic}\n"
            f"{kc_context}"
            f"Tingkat Bantuan: Level {level} (1: Arahkan fokus, 2: Langkah antara, 3: Kerangka berpikir)\n"
            f"Soal: {question_text}\n"
            "Tuliskan petunjuk bimbingan singkat:"
        )
        return await self.call_chat(
            system_prompt=system_content,
            user_prompt=user_content,
            max_tokens=120,
            timeout_seconds=timeout_seconds,
        )

    def sanitize_output(self, text: str) -> str:
        """Strips markdown code fences and escapes HTML to prevent XSS."""
        if not text:
            return ""
        cleaned = re.sub(r"```[a-zA-Z]*", "", text)
        cleaned = cleaned.replace("```", "").strip('"\n\r\t ')
        return html.escape(cleaned)
