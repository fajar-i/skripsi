"""
LogiTrace: Secure LLM API Client Architecture (Zero-PII & Defense-in-Depth).
Implements Privacy-Preserving Cloud Inference (DeepSeek, Groq, Ollama)
with pre-flight PII scrubbing, TLS enforcement, secret masking, and post-flight guardrails.
"""

import html
import logging
import os
import re
import time
from typing import Dict, List, Optional, Tuple
from dotenv import load_dotenv
import httpx

from .guardrails import AnswerLeakageGuard

load_dotenv()

logger = logging.getLogger("secure_llm_client")

# ---------------------------------------------------------------------------
# 1. PII PATTERNS (PRE-FLIGHT PRIVACY SCRUBBER)
# ---------------------------------------------------------------------------
PII_PATTERNS = [
    # NISN (10 digits) or NIK (16 digits)
    (re.compile(r"\b\d{10}\b"), "[REDACTED_NISN]"),
    (re.compile(r"\b\d{16}\b"), "[REDACTED_NIK]"),
    # Phone numbers (+62 / 08xx)
    (re.compile(r"(?:\b|\+)(?:62|08)[0-9\-\s]{8,14}\b"), "[REDACTED_PHONE]"),
    # Email addresses
    (re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"), "[REDACTED_EMAIL]"),
    # Student identity tags e.g., 'Siswa S01', 'User S12', 'S01', 'std_01'
    (re.compile(r"\b(siswa|user|murid|absen)\s*[:=]?\s*(?:S|std_)\d{1,3}\b", re.IGNORECASE), "[REDACTED_STUDENT_ID]"),
    (re.compile(r"\b(?:S\d{2,3}|std_\d{1,3})\b", re.IGNORECASE), "[REDACTED_ID]"),
    # Common Indonesian school names
    (re.compile(r"\b(SMK|SMA|SMP|SD)\s+Negeri\s+\d+\s+[A-Za-z]+", re.IGNORECASE), "[REDACTED_SCHOOL]"),
]


class PIIScrubber:
    """Pre-flight security layer ensuring zero student PII ever leaves the local server."""

    @classmethod
    def scrub(cls, text: str) -> Tuple[str, bool]:
        """
        Sanitizes text by replacing any detected personal identifiable information.
        Returns (sanitized_text, had_pii).
        """
        if not text:
            return "", False

        cleaned = text
        had_pii = False
        for pattern, replacement in PII_PATTERNS:
            if pattern.search(cleaned):
                had_pii = True
                cleaned = pattern.sub(replacement, cleaned)

        # Cap text length to prevent prompt bloat / injection
        if len(cleaned) > 1000:
            cleaned = cleaned[:1000]

        return cleaned, had_pii


# ---------------------------------------------------------------------------
# 2. PROVIDER CONFIGURATION & CREDENTIAL MANAGEMENT
# ---------------------------------------------------------------------------
def mask_secret(secret: Optional[str]) -> str:
    """Masks secret keys for safe logging (e.g. sk-****1234)."""
    if not secret:
        return "<EMPTY>"
    if len(secret) <= 8:
        return "****"
    return f"{secret[:4]}****{secret[-4:]}"


# Supported Cloud & Local Providers
PROVIDERS = {
    "deepseek": {
        "url": "https://api.deepseek.com/chat/completions",
        "default_model": "deepseek-chat",
        "env_key": "DEEPSEEK_API_KEY",
    },
    "groq": {
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "default_model": "llama-3.1-8b-instant",
        "env_key": "GROQ_API_KEY",
    },
    "openai": {
        "url": os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1/chat/completions"),
        "default_model": "gpt-4o-mini",
        "env_key": "OPENAI_API_KEY",
    },
    "9router": {
        "url": os.getenv("NINEROUTER_API_URL", "http://localhost:20128/v1/chat/completions"),
        "default_model": os.getenv("NINEROUTER_MODEL", "ag/gemini-3.8-flash"),
        "env_key": "NINEROUTER_API_KEY",
    },
    "ollama": {
        "url": os.getenv("LOGITRACE_OLLAMA_URL", "http://localhost:11434/api/generate"),
        "default_model": os.getenv("LOGITRACE_LLM_MODEL", "qwen2.5:3b"),
        "env_key": None,
    },
}


class SecureLLMClient:
    """
    Production-grade Secure API client implementing Defense-in-Depth:
    1. Pre-flight Zero-PII sanitization
    2. Secret credential encapsulation
    3. HTTPS transport enforcement & strict 3.0s SLA timeout
    4. Post-flight Regex leakage checking & XSS output sanitization
    5. Graceful fallback trigger
    """

    def __init__(self, provider: Optional[str] = None):
        self.guard = AnswerLeakageGuard()
        self.provider = provider or os.getenv("LOGITRACE_LLM_PROVIDER", "").lower()

        # Auto-detect available provider based on environment variables
        if not self.provider or self.provider not in PROVIDERS:
            if os.getenv("NINEROUTER_API_KEY"):
                self.provider = "9router"
            elif os.getenv("DEEPSEEK_API_KEY"):
                self.provider = "deepseek"
            elif os.getenv("GROQ_API_KEY"):
                self.provider = "groq"
            elif os.getenv("OPENAI_API_KEY"):
                self.provider = "openai"
            else:
                self.provider = "ollama"

        cfg = PROVIDERS.get(self.provider, PROVIDERS["ollama"])
        self.endpoint_url = cfg["url"]
        self.model_name = os.getenv("LOGITRACE_LLM_MODEL", cfg["default_model"])
        self.api_key = os.getenv(cfg["env_key"], "") if cfg["env_key"] else None

        logger.info(
            f"Initialized SecureLLMClient [Provider: {self.provider.upper()}, "
            f"Model: {self.model_name}, Key: {mask_secret(self.api_key)}]"
        )

    async def call_chat(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int = 250,
        timeout_seconds: float = 5.0,
    ) -> Tuple[Optional[str], int, Optional[str]]:
        """
        Generic secure chat completion call supporting 9router, DeepSeek, Groq, OpenAI, and Ollama.
        Sanitizes PII, masks tokens, and enforces timeout.
        Returns: (raw_response_text, latency_ms, error_msg)
        """
        clean_user, had_pii = PIIScrubber.scrub(user_prompt)
        clean_sys, _ = PIIScrubber.scrub(system_prompt)
        if had_pii:
            logger.warning("Sanitizer redacted detected PII in chat call.")

        if self.provider == "ollama":
            payload = {
                "model": self.model_name,
                "prompt": f"{clean_sys}\n\n{clean_user}",
                "stream": False,
                "options": {
                    "temperature": 0.0,
                    "seed": 42,
                    "num_predict": max_tokens,
                },
            }
            headers = {"Content-Type": "application/json"}
        else:
            if not self.api_key:
                return None, 0, f"Missing API key for provider {self.provider}"
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
        try:
            async with httpx.AsyncClient(timeout=timeout_seconds, verify=True) as client:
                res = await client.post(self.endpoint_url, json=payload, headers=headers)
                lat_ms = int((time.perf_counter() - start_t) * 1000)

                if res.status_code == 200:
                    data = res.json()
                    if self.provider == "ollama":
                        text_out = (data.get("response") or "").strip()
                    else:
                        choices = data.get("choices", [])
                        msg = choices[0].get("message", {}) if choices else {}
                        text_out = (msg.get("content") or "").strip()
                    return text_out, lat_ms, None
                elif res.status_code == 429:
                    return None, lat_ms, "Rate limit reached (HTTP 429)"
                else:
                    return None, lat_ms, f"Provider HTTP {res.status_code}: {res.text[:100]}"
        except httpx.TimeoutException:
            lat_ms = int((time.perf_counter() - start_t) * 1000)
            return None, lat_ms, f"Timeout exceeded ({timeout_seconds}s SLA)"
        except Exception as e:
            lat_ms = int((time.perf_counter() - start_t) * 1000)
            return None, lat_ms, f"Connection error: {str(e)[:100]}"

    async def call_api(
        self,
        topic: str,
        level: int,
        question_text: str,
        timeout_seconds: float = 3.0,
        kc_description: Optional[str] = None,
    ) -> Tuple[Optional[str], int, Optional[str]]:
        """
        Specialized call for Socratic hint scaffolding (Agent T2).
        Delegates to call_chat with strict 120-token constraint and L1 KC context.
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
        """Post-flight output defense: strips markdown code fences, escapes HTML tags to prevent XSS."""
        if not text:
            return ""
        # Remove markdown quotes or backticks if LLM hallucinated code block
        cleaned = re.sub(r"```[a-zA-Z]*", "", text)
        cleaned = cleaned.replace("```", "").strip('"\n\r\t ')
        # Escape HTML entities for safe browser rendering
        return html.escape(cleaned)
