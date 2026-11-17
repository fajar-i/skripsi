"""
LogiTrace: authentication for the classroom.

Teacher: one shared password (LOGITRACE_TEACHER_PASSWORD, else auto-generated into
teacher_password.txt). Login sets a signed, HttpOnly cookie valid for one school day.

Student: anonymous code + 4-digit PIN from a printed card + the class code shown on the
teacher's screen for the active session. Login sets an HttpOnly device cookie. Each student
has one active device; logging in elsewhere replaces it.

Every login, failed login, device replacement and PIN change is written to auth_events.
"""

import base64
import hashlib
import hmac
import json
import logging
import os
import secrets
import time
from collections import defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Deque, Dict, Optional

from fastapi import Depends, HTTPException, Response, status
from fastapi.requests import HTTPConnection
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .db.database import get_db
from .db.models import AuthEvent, Student

logger = logging.getLogger("logitrace_auth")

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SECRET_FILE = os.path.join(ROOT_DIR, ".secret_key")
TEACHER_PASSWORD_FILE = os.path.join(ROOT_DIR, "teacher_password.txt")

TEACHER_COOKIE = "lt_teacher"
STUDENT_COOKIE = "lt_student"
TEACHER_TTL_SECONDS = 12 * 3600
STUDENT_TTL_SECONDS = 14 * 24 * 3600

CLASS_CODE_ALPHABET = "ABCDEFGHJKMNPQRSTUVWXYZ23456789"  # no 0/O, 1/I/L
PIN_ITERATIONS = 120_000

# Brute-force limits (in-memory, per process): failures inside the window
FAIL_WINDOW_SECONDS = 60
MAX_FAILS_PER_STUDENT = 5
MAX_FAILS_PER_IP = 20


def utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None)


# ---------------------------------------------------------------- secrets ----

_secret_cache: Optional[bytes] = None


def _read_or_create(path: str, factory) -> str:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            value = f.read().strip()
        if value:
            return value
    value = factory()
    with open(path, "w", encoding="utf-8") as f:
        f.write(value + "\n")
    return value


def secret_key() -> bytes:
    env = os.getenv("LOGITRACE_SECRET_KEY")
    if env:
        return env.encode()
    global _secret_cache
    if _secret_cache is None:
        _secret_cache = _read_or_create(SECRET_FILE, lambda: secrets.token_hex(32)).encode()
    return _secret_cache


def teacher_password() -> str:
    env = os.getenv("LOGITRACE_TEACHER_PASSWORD")
    if env:
        return env
    return _read_or_create(
        TEACHER_PASSWORD_FILE,
        lambda: "".join(secrets.choice(CLASS_CODE_ALPHABET.lower()) for _ in range(10)),
    )


def describe_teacher_password_source() -> str:
    if os.getenv("LOGITRACE_TEACHER_PASSWORD"):
        return "LOGITRACE_TEACHER_PASSWORD (.env)"
    teacher_password()  # make sure the file exists
    return TEACHER_PASSWORD_FILE


# ---------------------------------------------------------- signed tokens ----

def _b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def _unb64(text: str) -> bytes:
    return base64.urlsafe_b64decode(text + "=" * (-len(text) % 4))


def sign(payload: dict) -> str:
    body = _b64(json.dumps(payload, separators=(",", ":")).encode())
    mac = _b64(hmac.new(secret_key(), body.encode(), hashlib.sha256).digest())
    return f"{body}.{mac}"


def verify(token: Optional[str]) -> Optional[dict]:
    if not token or "." not in token:
        return None
    body, mac = token.rsplit(".", 1)
    expected = _b64(hmac.new(secret_key(), body.encode(), hashlib.sha256).digest())
    if not hmac.compare_digest(mac, expected):
        return None
    try:
        payload = json.loads(_unb64(body))
    except (ValueError, json.JSONDecodeError):
        return None
    if payload.get("exp", 0) < time.time():
        return None
    return payload


# -------------------------------------------------------------- PIN & codes ----

def hash_pin(pin: str) -> str:
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", pin.encode(), salt, PIN_ITERATIONS)
    return f"pbkdf2${PIN_ITERATIONS}${salt.hex()}${digest.hex()}"


def check_pin(pin: str, stored: Optional[str]) -> bool:
    if not stored:
        return False
    try:
        _, iterations, salt_hex, digest_hex = stored.split("$")
        digest = hashlib.pbkdf2_hmac("sha256", pin.encode(), bytes.fromhex(salt_hex), int(iterations))
    except (ValueError, TypeError):
        return False
    return hmac.compare_digest(digest.hex(), digest_hex)


def new_pin() -> str:
    return f"{secrets.randbelow(10_000):04d}"


def new_class_code(length: int = 4) -> str:
    return "".join(secrets.choice(CLASS_CODE_ALPHABET) for _ in range(length))


def token_hash(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


# ---------------------------------------------------------- rate limiting ----

_fails: Dict[str, Deque[float]] = defaultdict(deque)


def _recent(key: str) -> Deque[float]:
    q = _fails[key]
    cutoff = time.time() - FAIL_WINDOW_SECONDS
    while q and q[0] < cutoff:
        q.popleft()
    return q


def check_rate_limit(student_code: str, ip: str) -> None:
    if len(_recent(f"s:{student_code}")) >= MAX_FAILS_PER_STUDENT or len(_recent(f"ip:{ip}")) >= MAX_FAILS_PER_IP:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Terlalu banyak percobaan. Tunggu 1 menit lalu coba lagi.",
        )


def record_failure(student_code: str, ip: str) -> None:
    now = time.time()
    _fails[f"s:{student_code}"].append(now)
    _fails[f"ip:{ip}"].append(now)


def reset_rate_limits() -> None:
    _fails.clear()


def client_ip(conn: HTTPConnection) -> str:
    return conn.client.host if conn.client else "unknown"


# ---------------------------------------------------------------- cookies ----

def set_cookie(response: Response, name: str, value: str, max_age: int) -> None:
    # HttpOnly: page scripts cannot read it. Secure is off because the classroom LAN is plain HTTP.
    response.set_cookie(name, value, max_age=max_age, httponly=True, samesite="strict", path="/")


def clear_cookie(response: Response, name: str) -> None:
    response.delete_cookie(name, path="/", samesite="strict")


def teacher_cookie_value() -> str:
    return sign({"r": "teacher", "exp": int(time.time()) + TEACHER_TTL_SECONDS})


def student_cookie_value(student_id: str, raw_token: str) -> str:
    return f"{student_id}:{raw_token}"


async def log_event(db: AsyncSession, actor: str, event: str, conn: Optional[HTTPConnection] = None,
                    student_id: Optional[str] = None, detail: Optional[str] = None) -> None:
    db.add(AuthEvent(actor=actor, event=event, student_id=student_id, detail=detail,
                     ip=client_ip(conn) if conn else None))


# ----------------------------------------------------------- dependencies ----

@dataclass
class Principal:
    is_teacher: bool = False
    student_id: Optional[str] = None
    student_code: Optional[str] = None
    wildcard: bool = False  # tests only: may act as any student

    def assert_is_student(self, code: str) -> None:
        if self.wildcard or (self.student_code is not None and self.student_code == code):
            return
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Kamu hanya boleh mengakses akunmu sendiri.")


TEACHER = Principal(is_teacher=True)


def is_teacher_request(conn: HTTPConnection) -> bool:
    payload = verify(conn.cookies.get(TEACHER_COOKIE))
    return bool(payload and payload.get("r") == "teacher")


async def require_teacher(conn: HTTPConnection) -> Principal:
    if not is_teacher_request(conn):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="TEACHER_AUTH_REQUIRED")
    return TEACHER


async def _student_from_cookie(conn: HTTPConnection, db: AsyncSession) -> Principal:
    raw = conn.cookies.get(STUDENT_COOKIE)
    if not raw or ":" not in raw:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="STUDENT_AUTH_REQUIRED")
    student_id, token = raw.split(":", 1)
    student = await db.get(Student, student_id)
    if not student or not student.device_token_hash:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="STUDENT_AUTH_REQUIRED")
    if not hmac.compare_digest(student.device_token_hash, token_hash(token)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="DEVICE_REPLACED")
    login_at = student.device_login_at
    if login_at and (utc_now() - login_at).total_seconds() > STUDENT_TTL_SECONDS:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="STUDENT_AUTH_REQUIRED")
    return Principal(student_id=student.id, student_code=student.anonymous_code)


async def require_student(conn: HTTPConnection, db: AsyncSession = Depends(get_db)) -> Principal:
    return await _student_from_cookie(conn, db)


async def require_teacher_or_student(conn: HTTPConnection, db: AsyncSession = Depends(get_db)) -> Principal:
    if is_teacher_request(conn):
        return TEACHER
    return await _student_from_cookie(conn, db)
