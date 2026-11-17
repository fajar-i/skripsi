"""
LogiTrace: login endpoints for teacher and students, class code, and login-card management.
"""

import hmac
import socket
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from pydantic import BaseModel, Field
from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from .. import auth
from ..auth import Principal, require_student, require_teacher
from ..db.database import get_db
from ..db.models import QuizSession, Student

router = APIRouter(prefix="/api/auth", tags=["Authentication"])


class TeacherLoginRequest(BaseModel):
    password: str = Field(..., min_length=1, max_length=200)


class StudentLoginRequest(BaseModel):
    student_code: str = Field(..., min_length=1, max_length=32)
    pin: str = Field(..., min_length=4, max_length=4, pattern=r"^\d{4}$")
    class_code: str = Field(..., min_length=4, max_length=8)


class RegeneratePinsRequest(BaseModel):
    student_codes: Optional[List[str]] = None  # None = every student in the class
    class_rombel: str = "XI TKJ 1"


async def _active_session(db: AsyncSession, class_rombel: str) -> Optional[QuizSession]:
    res = await db.execute(
        select(QuizSession)
        .where(QuizSession.class_rombel == class_rombel, QuizSession.is_active == True)
        .order_by(desc(QuizSession.created_at))
    )
    return res.scalars().first()


async def ensure_join_code(db: AsyncSession, session: QuizSession) -> str:
    if not session.join_code:
        session.join_code = auth.new_class_code()
        await db.commit()
    return session.join_code


# ------------------------------------------------------------------ teacher ----

@router.post("/teacher/login")
async def teacher_login(req: TeacherLoginRequest, request: Request, response: Response,
                        db: AsyncSession = Depends(get_db)):
    ip = auth.client_ip(request)
    auth.check_rate_limit("__teacher__", ip)
    if not hmac.compare_digest(req.password.encode(), auth.teacher_password().encode()):
        auth.record_failure("__teacher__", ip)
        await auth.log_event(db, "teacher", "login_fail", request)
        await db.commit()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Kata sandi guru salah.")
    auth.set_cookie(response, auth.TEACHER_COOKIE, auth.teacher_cookie_value(), auth.TEACHER_TTL_SECONDS)
    await auth.log_event(db, "teacher", "login_ok", request)
    await db.commit()
    return {"status": "ok"}


@router.post("/teacher/logout")
async def teacher_logout(response: Response):
    auth.clear_cookie(response, auth.TEACHER_COOKIE)
    return {"status": "ok"}


@router.get("/teacher/me")
async def teacher_me(_: Principal = Depends(require_teacher)):
    return {"role": "teacher"}


@router.get("/class-code")
async def get_class_code(class_rombel: str = "XI TKJ 1", db: AsyncSession = Depends(get_db),
                         _: Principal = Depends(require_teacher)):
    session = await _active_session(db, class_rombel)
    if not session:
        return {"session_id": None, "session_title": None, "class_code": None}
    code = await ensure_join_code(db, session)
    return {"session_id": session.id, "session_title": session.title, "class_code": code}


@router.post("/class-code/rotate")
async def rotate_class_code(class_rombel: str = "XI TKJ 1", db: AsyncSession = Depends(get_db),
                            _: Principal = Depends(require_teacher)):
    session = await _active_session(db, class_rombel)
    if not session:
        raise HTTPException(status_code=404, detail="Belum ada sesi aktif.")
    session.join_code = auth.new_class_code()
    await db.commit()
    return {"session_id": session.id, "class_code": session.join_code}


@router.get("/students")
async def list_student_logins(class_rombel: str = "XI TKJ 1", db: AsyncSession = Depends(get_db),
                              _: Principal = Depends(require_teacher)):
    res = await db.execute(
        select(Student).where(Student.class_rombel == class_rombel).order_by(Student.anonymous_code)
    )
    return [
        {
            "student_code": s.anonymous_code,
            "has_pin": bool(s.pin_hash),
            "pin_set_at": s.pin_set_at.isoformat() if s.pin_set_at else None,
            "device_active": bool(s.device_token_hash),
            "last_login_at": s.device_login_at.isoformat() if s.device_login_at else None,
        }
        for s in res.scalars().all()
    ]


@router.post("/students/pins")
async def regenerate_pins(req: RegeneratePinsRequest, request: Request, db: AsyncSession = Depends(get_db),
                          _: Principal = Depends(require_teacher)):
    """Issue new PINs. Plain PINs are returned once, for printing, and only their hashes are stored.
    Devices that are already logged in stay logged in; old cards stop working."""
    stmt = select(Student).where(Student.class_rombel == req.class_rombel)
    if req.student_codes:
        stmt = stmt.where(Student.anonymous_code.in_(req.student_codes))
    res = await db.execute(stmt.order_by(Student.anonymous_code))
    students = res.scalars().all()
    if not students:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan.")

    now = auth.utc_now()
    cards = []
    for s in students:
        pin = auth.new_pin()
        s.pin_hash = auth.hash_pin(pin)
        s.pin_set_at = now
        cards.append({"student_code": s.anonymous_code, "pin": pin})
        await auth.log_event(db, "teacher", "pin_reset", request, student_id=s.id)
    await db.commit()
    return {"class_rombel": req.class_rombel, "cards": cards}


@router.post("/students/{student_code}/logout-device")
async def force_logout_device(student_code: str, request: Request, db: AsyncSession = Depends(get_db),
                              _: Principal = Depends(require_teacher)):
    res = await db.execute(select(Student).where(Student.anonymous_code == student_code))
    student = res.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan.")
    student.device_token_hash = None
    await auth.log_event(db, "teacher", "device_revoked", request, student_id=student.id)
    await db.commit()
    return {"status": "ok"}


@router.get("/server-info")
async def server_info(request: Request, _: Principal = Depends(require_teacher)):
    """Addresses students can type or scan, so cards never print 'localhost'."""
    port = request.url.port or (443 if request.url.scheme == "https" else 80)
    ips = set()
    try:
        for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
            if not ip.startswith("127."):
                ips.add(ip)
    except OSError:
        pass
    try:  # the interface used for outbound traffic (no packet is sent)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("10.255.255.255", 1))
            ips.add(sock.getsockname()[0])
    except OSError:
        pass
    host = request.url.hostname or ""
    is_local = host in ("localhost", "127.0.0.1", "::1")
    urls = [f"{request.url.scheme}://{ip}:{port}/student/" for ip in sorted(ips)]
    if not is_local:
        urls.insert(0, f"{request.url.scheme}://{request.url.netloc}/student/")
    return {"student_urls": list(dict.fromkeys(urls)), "opened_via_localhost": is_local}


# ------------------------------------------------------------------ student ----

@router.post("/student/login")
async def student_login(req: StudentLoginRequest, request: Request, response: Response,
                        db: AsyncSession = Depends(get_db)):
    ip = auth.client_ip(request)
    code = req.student_code.strip()
    auth.check_rate_limit(code, ip)

    res = await db.execute(select(Student).where(Student.anonymous_code == code))
    student = res.scalar_one_or_none()

    async def fail(reason: str, message: str, http_status: int = status.HTTP_401_UNAUTHORIZED):
        auth.record_failure(code, ip)
        await auth.log_event(db, "student", "login_fail", request,
                             student_id=student.id if student else None, detail=reason)
        await db.commit()
        raise HTTPException(status_code=http_status, detail=message)

    if not student or not student.pin_hash:
        await fail("no_card", "Kode siswa atau PIN salah. Periksa kartumu atau tanya guru.")

    session = await _active_session(db, student.class_rombel)
    if not session or not session.join_code:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Belum ada sesi aktif. Tunggu guru membuka sesi.")
    if req.class_code.strip().upper() != session.join_code:
        await fail("bad_class_code", "Kode kelas salah. Lihat kode di layar guru.")
    if not auth.check_pin(req.pin, student.pin_hash):
        await fail("bad_pin", "Kode siswa atau PIN salah. Periksa kartumu atau tanya guru.")

    replaced = bool(student.device_token_hash)
    raw_token = auth.secrets.token_urlsafe(32)
    student.device_token_hash = auth.token_hash(raw_token)
    student.device_login_at = auth.utc_now()
    if replaced:
        await auth.log_event(db, "student", "device_replaced", request, student_id=student.id)
    await auth.log_event(db, "student", "login_ok", request, student_id=student.id)
    await db.commit()

    auth.set_cookie(response, auth.STUDENT_COOKIE, auth.student_cookie_value(student.id, raw_token),
                    auth.STUDENT_TTL_SECONDS)
    return {"student_code": student.anonymous_code, "class_rombel": student.class_rombel}


@router.post("/student/logout")
async def student_logout(request: Request, response: Response, db: AsyncSession = Depends(get_db)):
    try:
        principal = await auth.require_student(request, db)
        student = await db.get(Student, principal.student_id)
        student.device_token_hash = None
        await auth.log_event(db, "student", "logout", request, student_id=student.id)
        await db.commit()
    except HTTPException:
        pass
    auth.clear_cookie(response, auth.STUDENT_COOKIE)
    return {"status": "ok"}


@router.get("/student/me")
async def student_me(principal: Principal = Depends(require_student), db: AsyncSession = Depends(get_db)):
    student = await db.get(Student, principal.student_id)
    return {"student_code": student.anonymous_code, "class_rombel": student.class_rombel}
