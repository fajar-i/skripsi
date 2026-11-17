"""
Authentication tests: teacher password login, student card login (code + PIN + class code),
one device per student, brute-force limit, and route guards.
"""

import os
import sys
import uuid

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import select

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.app import auth
from backend.app.db.database import AsyncSessionLocal, init_db
from backend.app.db.models import AuthEvent, QuizSession, Student
from backend.app.db.seeder import seed_database
from backend.app.main import app

TEACHER_PW = "guru-rahasia-123"


@pytest.fixture(autouse=True)
async def setup(monkeypatch):
    monkeypatch.setenv("LOGITRACE_TEACHER_PASSWORD", TEACHER_PW)
    monkeypatch.setenv("LOGITRACE_SECRET_KEY", "test-secret")
    app.dependency_overrides.clear()
    auth.reset_rate_limits()
    await init_db()
    async with AsyncSessionLocal() as session:
        await seed_database(session)
    yield
    auth.reset_rate_limits()


def client() -> AsyncClient:
    return AsyncClient(transport=ASGITransport(app=app), base_url="http://test")


async def make_class(n_students: int = 2):
    """Isolated class with an active session, so tests never touch XI TKJ 1."""
    tag = uuid.uuid4().hex[:6]
    rombel = f"AUTH_{tag}"
    codes = [f"tstd_a{tag}_{i}" for i in range(n_students)]
    async with AsyncSessionLocal() as s:
        s.add_all([Student(anonymous_code=c, class_rombel=rombel) for c in codes])
        active = QuizSession(class_rombel=rombel, title=f"Auth {tag}", is_active=True, join_code="K7MP")
        closed = QuizSession(class_rombel=rombel, title=f"Lama {tag}", is_active=False, join_code="ZZZZ")
        s.add_all([active, closed])
        await s.commit()
        return rombel, codes, active.id, closed.id


async def teacher_login(c: AsyncClient):
    res = await c.post("/api/auth/teacher/login", json={"password": TEACHER_PW})
    assert res.status_code == 200


async def issue_pins(rombel: str) -> dict:
    async with client() as t:
        await teacher_login(t)
        res = await t.post("/api/auth/students/pins", json={"class_rombel": rombel})
        assert res.status_code == 200
        return {c["student_code"]: c["pin"] for c in res.json()["cards"]}


@pytest.mark.asyncio
async def test_teacher_routes_require_login():
    async with client() as c:
        for method, url in [("get", "/api/teacher/ambient"), ("get", "/api/export/audit-logs"),
                            ("post", "/api/sessions/x/activate"), ("get", "/api/auth/students")]:
            res = await getattr(c, method)(url)
            assert res.status_code == 401, url

        res = await c.post("/api/auth/teacher/login", json={"password": "salah"})
        assert res.status_code == 401

        await teacher_login(c)
        assert (await c.get("/api/teacher/ambient")).status_code == 200
        assert (await c.get("/api/auth/teacher/me")).status_code == 200

        await c.post("/api/auth/teacher/logout")
        assert (await c.get("/api/teacher/ambient")).status_code == 401


@pytest.mark.asyncio
async def test_pins_are_hashed_and_returned_once():
    rombel, codes, _, _ = await make_class()
    pins = await issue_pins(rombel)
    assert set(pins) == set(codes)
    assert all(len(p) == 4 and p.isdigit() for p in pins.values())
    async with AsyncSessionLocal() as s:
        stored = (await s.execute(select(Student).where(Student.anonymous_code == codes[0]))).scalar_one()
        assert stored.pin_hash.startswith("pbkdf2$")
        assert pins[codes[0]] not in stored.pin_hash


@pytest.mark.asyncio
async def test_student_login_needs_pin_and_class_code():
    rombel, codes, active_id, _ = await make_class()
    pins = await issue_pins(rombel)
    code, pin = codes[0], pins[codes[0]]
    wrong_pin = "0000" if pin != "0000" else "1111"

    async with client() as c:
        res = await c.post("/api/auth/student/login", json={"student_code": code, "pin": wrong_pin, "class_code": "K7MP"})
        assert res.status_code == 401
        res = await c.post("/api/auth/student/login", json={"student_code": code, "pin": pin, "class_code": "ZZZZ"})
        assert res.status_code == 401
        assert (await c.get(f"/api/quiz/{code}/next")).status_code == 401

        res = await c.post("/api/auth/student/login", json={"student_code": code, "pin": pin, "class_code": "k7mp"})
        assert res.status_code == 200
        assert (await c.get("/api/auth/student/me")).json()["student_code"] == code

        assert (await c.get(f"/api/quiz/{code}/next", params={"session_id": active_id})).status_code == 200
        # Cannot act as a classmate
        assert (await c.get(f"/api/quiz/{codes[1]}/next")).status_code == 403
        # Cannot use teacher routes
        assert (await c.get("/api/teacher/ambient")).status_code == 401
        assert (await c.post("/api/sessions", json={"title": "x", "class_rombel": rombel})).status_code == 401

    async with AsyncSessionLocal() as s:
        events = (await s.execute(select(AuthEvent.event).join(Student, AuthEvent.student_id == Student.id)
                                  .where(Student.anonymous_code == code))).scalars().all()
        assert "login_ok" in events and events.count("login_fail") == 2


@pytest.mark.asyncio
async def test_second_device_replaces_first():
    rombel, codes, _, _ = await make_class()
    pins = await issue_pins(rombel)
    body = {"student_code": codes[0], "pin": pins[codes[0]], "class_code": "K7MP"}
    async with client() as phone, client() as laptop:
        assert (await phone.post("/api/auth/student/login", json=body)).status_code == 200
        assert (await laptop.post("/api/auth/student/login", json=body)).status_code == 200
        res = await phone.get("/api/auth/student/me")
        assert res.status_code == 401 and res.json()["detail"] == "DEVICE_REPLACED"
        assert (await laptop.get("/api/auth/student/me")).status_code == 200


@pytest.mark.asyncio
async def test_teacher_can_log_out_a_device():
    rombel, codes, _, _ = await make_class()
    pins = await issue_pins(rombel)
    async with client() as phone, client() as teacher:
        await phone.post("/api/auth/student/login",
                         json={"student_code": codes[0], "pin": pins[codes[0]], "class_code": "K7MP"})
        await teacher_login(teacher)
        assert (await teacher.post(f"/api/auth/students/{codes[0]}/logout-device")).status_code == 200
        assert (await phone.get("/api/auth/student/me")).status_code == 401


@pytest.mark.asyncio
async def test_failed_pins_are_rate_limited():
    rombel, codes, _, _ = await make_class()
    pins = await issue_pins(rombel)
    code, pin = codes[0], pins[codes[0]]
    wrong = "0000" if pin != "0000" else "1111"
    async with client() as c:
        for _ in range(auth.MAX_FAILS_PER_STUDENT):
            await c.post("/api/auth/student/login", json={"student_code": code, "pin": wrong, "class_code": "K7MP"})
        res = await c.post("/api/auth/student/login", json={"student_code": code, "pin": pin, "class_code": "K7MP"})
        assert res.status_code == 429


@pytest.mark.asyncio
async def test_student_reset_only_own_attempt_in_active_session():
    rombel, codes, active_id, closed_id = await make_class()
    pins = await issue_pins(rombel)
    async with client() as c:
        await c.post("/api/auth/student/login",
                     json={"student_code": codes[0], "pin": pins[codes[0]], "class_code": "K7MP"})
        assert (await c.post(f"/api/sessions/{active_id}/reset-student/{codes[0]}")).status_code == 200
        assert (await c.post(f"/api/sessions/{closed_id}/reset-student/{codes[0]}")).status_code == 409
        assert (await c.post(f"/api/sessions/{active_id}/reset-student/{codes[1]}")).status_code == 403
        assert (await c.get(f"/api/sessions/{active_id}/student/{codes[1]}/status")).status_code == 403


@pytest.mark.asyncio
async def test_activating_a_session_rotates_class_code():
    rombel, _, active_id, closed_id = await make_class()
    async with client() as t:
        await teacher_login(t)
        res = await t.post(f"/api/sessions/{closed_id}/activate")
        assert res.status_code == 200
        new_code = res.json()["class_code"]
        assert new_code and new_code != "ZZZZ"
        res = await t.get("/api/auth/class-code", params={"class_rombel": rombel})
        assert res.json()["class_code"] == new_code


def test_websocket_requires_teacher_cookie():
    from starlette.testclient import TestClient
    from starlette.websockets import WebSocketDisconnect

    with TestClient(app) as tc:
        with pytest.raises(WebSocketDisconnect):
            with tc.websocket_connect("/api/teacher/ws/ambient") as ws:
                ws.receive_json()
        tc.post("/api/auth/teacher/login", json={"password": TEACHER_PW})
        with tc.websocket_connect("/api/teacher/ws/ambient") as ws:
            assert "heatmap" in ws.receive_json()
