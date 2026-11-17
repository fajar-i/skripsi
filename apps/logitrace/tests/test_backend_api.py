"""
Integration & Unit Tests for LogiTrace FastAPI Backend.
Verifies API endpoints, L3 runtime cognitive updates, append-only integrity,
Socratic hint delivery, and teacher ambient dashboard.
"""

import asyncio
import os
import sys
import uuid
import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy import select, update, delete

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.app.main import app
from backend.app.db.database import AsyncSessionLocal, init_db
from backend.app.db.models import Interaction, Student, MasterySnapshot
from backend.app.db.seeder import seed_database


@pytest.fixture(autouse=True)
async def setup_test_db():
    await init_db()
    async with AsyncSessionLocal() as session:
        await seed_database(session)


@pytest.fixture(autouse=True)
def bypass_auth():
    """These tests cover domain logic; login itself is covered in test_auth.py."""
    from backend.app.auth import Principal, require_student, require_teacher, require_teacher_or_student
    wildcard = Principal(is_teacher=True, wildcard=True)
    app.dependency_overrides[require_teacher] = lambda: wildcard
    app.dependency_overrides[require_student] = lambda: Principal(wildcard=True)
    app.dependency_overrides[require_teacher_or_student] = lambda: wildcard
    yield
    app.dependency_overrides.clear()


@pytest.mark.asyncio
async def test_health_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        res = await client.get("/health")
        assert res.status_code == 200
        data = res.json()
        assert data["status"] == "healthy"
        assert "Deterministic L3" in data["engine"]


@pytest.mark.asyncio
async def test_student_next_question_calibration():
    """First item for new student must be a calibration item (is_calibration=True)."""
    # Create fresh unique test student
    fresh_code = f"tstd_{uuid.uuid4().hex[:6]}"
    async with AsyncSessionLocal() as session:
        new_student = Student(anonymous_code=fresh_code, class_rombel="XI TKJ 1")
        session.add(new_student)
        await session.commit()

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        res = await client.get(f"/api/quiz/{fresh_code}/next")
        assert res.status_code == 200
        item = res.json()
        assert item["sequence_number"] == 1
        assert item["is_calibration"] is True
        assert "correct_answer" not in item  # ZERO ANSWER LEAKAGE in public schema
        assert len(item["options"]) == 4


@pytest.mark.asyncio
async def test_student_submit_answer_deterministic_update():
    """Submitting answer updates mastery deterministically and appends interaction."""
    # Create fresh unique test student
    fresh_code = f"tstd_{uuid.uuid4().hex[:6]}"
    async with AsyncSessionLocal() as session:
        new_student = Student(anonymous_code=fresh_code, class_rombel="XI TKJ 1")
        session.add(new_student)
        await session.commit()

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # 1. Get next question
        q_res = await client.get(f"/api/quiz/{fresh_code}/next")
        assert q_res.status_code == 200
        item = q_res.json()

        # 2. Submit response
        submit_payload = {
            "student_code": fresh_code,
            "item_id": item["item_id"],
            "choice": "A",
            "response_time_ms": 1450,
            "used_hint": False,
            "hint_level": 0
        }
        sub_res = await client.post("/api/quiz/submit", json=submit_payload)
        assert sub_res.status_code == 200
        result = sub_res.json()

        assert "is_correct" in result
        assert result["sequence_number"] == 1
        assert result["is_calibration"] is True
        assert 0.02 <= result["mastery_after"] <= 0.98

        # If correct, mastery must increase; if incorrect, mastery must decrease
        if result["is_correct"]:
            assert result["mastery_after"] > result["mastery_before"]
        else:
            assert result["mastery_after"] < result["mastery_before"]

        # Verify unmeasured child KC was estimated from parent cluster with confidence='low'
        async with AsyncSessionLocal() as session:
            child_stmt = select(MasterySnapshot).where(
                MasterySnapshot.student_id == new_student.id,
                MasterySnapshot.kc_id == "WLAN_FREQ_CHANNEL"
            )
            child_res = await session.execute(child_stmt)
            child_snap = child_res.scalar_one_or_none()
            assert child_snap is not None
            assert child_snap.confidence == "low"
            assert pytest.approx(child_snap.current_mastery, abs=1e-3) == result["mastery_after"]


@pytest.mark.asyncio
async def test_append_only_integrity_enforcement():
    """Direct SQL UPDATE or DELETE on interactions table MUST raise PermissionError."""
    async with AsyncSessionLocal() as session:
        # Find an existing interaction
        stmt = select(Interaction).limit(1)
        res = await session.execute(stmt)
        interaction = res.scalar_one_or_none()

        if interaction:
            # Test UPDATE block
            interaction.response_result = 999
            with pytest.raises(PermissionError) as exc_info:
                await session.flush()
            assert "strictly append-only" in str(exc_info.value).lower()
            await session.rollback()

            # Test DELETE block
            with pytest.raises(PermissionError) as exc_info:
                await session.delete(interaction)
                await session.flush()
            assert "strictly append-only" in str(exc_info.value).lower()
            await session.rollback()


@pytest.mark.asyncio
async def test_socratic_hint_delivery():
    """Requesting hint returns pedagogical hint with zero leakage within 60 words."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        hint_payload = {
            "student_code": "std_03",
            "item_id": "ITEM_WLAN_STANDARDS_1_01",
            "requested_level": 1
        }
        res = await client.post("/api/quiz/hint", json=hint_payload)
        assert res.status_code == 200
        data = res.json()
        assert data["hint_level"] == 1
        assert data["word_count"] <= 60
        assert data["source"] in ("llm_9router", "fallback_static")
        assert len(data["hint_text"]) > 10


@pytest.mark.asyncio
async def test_teacher_ambient_dashboard():
    """Ambient endpoint returns 34 students, heatmap, and Top-3 Stuck priority cards."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        res = await client.get("/api/teacher/ambient")
        assert res.status_code == 200
        state = res.json()
        assert state["class_rombel"] == "XI TKJ 1"
        assert state["active_students_count"] >= 34
        assert len(state["heatmap"]) >= 34 * 12  # At least 34 students x 12 KCs
        assert isinstance(state["top_stuck_students"], list)
        assert len(state["top_stuck_students"]) <= 3


@pytest.mark.asyncio
async def test_export_audit_logs():
    """Audit logs export contains anonymous codes and strictly append-only policy."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        res = await client.get("/api/export/audit-logs")
        assert res.status_code == 200
        data = res.json()
        assert "records" in data
        assert "Strictly Append-Only" in data["audit_policy"]


@pytest.mark.asyncio
async def test_session_lifecycle_and_reset():
    """Tests LMS session management: listing, creation, activation, and full class reset."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # 1. List sessions
        res = await client.get("/api/sessions")
        assert res.status_code == 200
        sessions = res.json()
        assert len(sessions) >= 1
        active_sess = next((s for s in sessions if s["is_active"]), sessions[0])
        session_id = active_sess["id"]

        # 2. Create new session
        create_payload = {
            "title": "Sesi 2: Perawatan & Perbaikan Jaringan Nirkabel",
            "class_rombel": "XI TKJ 1",
            "session_number": 2,
            "max_items": 20
        }
        res_create = await client.post("/api/sessions", json=create_payload)
        assert res_create.status_code == 200
        new_session_id = res_create.json()["session_id"]
        assert new_session_id is not None

        # 3. Activate new session
        res_act = await client.post(f"/api/sessions/{new_session_id}/activate")
        assert res_act.status_code == 200
        assert res_act.json()["active_session_id"] == new_session_id

        # 4. Check teacher ambient with new session_id
        res_amb = await client.get(f"/api/teacher/ambient?session_id={new_session_id}")
        assert res_amb.status_code == 200
        amb_data = res_amb.json()
        assert amb_data["session_id"] == new_session_id
        assert amb_data["session_title"] == "Sesi 2: Perawatan & Perbaikan Jaringan Nirkabel"
        assert amb_data["not_started_count"] >= 34

        # 5. Reset individual student
        res_reset_std = await client.post(f"/api/sessions/{new_session_id}/reset-student/std_01")
        assert res_reset_std.status_code == 200
        assert res_reset_std.json()["student_code"] == "std_01"

        # 5b. Reset with invalid session ID returns 404
        res_invalid_sess = await client.post("/api/sessions/invalid_session_uuid/reset-student/std_01")
        assert res_invalid_sess.status_code == 404

        # 6. Reset all students for session
        res_reset_all = await client.post(f"/api/sessions/{new_session_id}/reset-all")
        assert res_reset_all.status_code == 200
        assert res_reset_all.json()["reset_students_count"] >= 34

        # 7. In newly reset session, no students should be falsely flagged as stuck
        res_amb_clean = await client.get(f"/api/teacher/ambient?session_id={new_session_id}")
        assert res_amb_clean.status_code == 200
        assert len(res_amb_clean.json()["top_stuck_students"]) == 0


@pytest.mark.asyncio
async def test_agent_t3_session_summary_and_peer_tutoring():
    """
    US-06: T3 summary uses only directly measured mastery of students who answered in
    this session. Students who never started, prior values and DAG-inherited values
    must not produce tutors or mentees.
    """
    from backend.app.db.models import QuizSession, StudentAttempt

    tag = uuid.uuid4().hex[:6]
    rombel = f"T3_{tag}"
    kc = "WLAN_STANDARDS"
    async with AsyncSessionLocal() as session:
        sess = QuizSession(class_rombel=rombel, title=f"Sesi uji {tag}", is_active=True)
        session.add(sess)
        await session.flush()

        def add_student(code, status, snaps):
            st = Student(anonymous_code=f"{code}_{tag}", class_rombel=rombel)
            session.add(st)
            return st, status, snaps

        rows = [
            add_student("tutor", "IN_PROGRESS", [(kc, 0.85, "high")]),
            add_student("m1", "IN_PROGRESS", [(kc, 0.30, "high")]),
            add_student("m2", "COMPLETED", [(kc, 0.35, "high")]),
            add_student("inherited", "IN_PROGRESS", [(kc, 0.90, "low")]),
            add_student("idle", "NOT_STARTED", [(kc, 0.25, "low")]),
        ]
        await session.flush()
        for st, status, snaps in rows:
            session.add(StudentAttempt(
                student_id=st.id, session_id=sess.id, status=status,
                answered_item_ids=[] if status == "NOT_STARTED" else ["ITEM_X"],
            ))
            for kc_id, m, conf in snaps:
                session.add(MasterySnapshot(student_id=st.id, kc_id=kc_id, current_mastery=m, confidence=conf))
        await session.commit()
        session_id = sess.id

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        res = await client.get("/api/teacher/session-summary", params={"session_id": session_id})
        assert res.status_code == 200
        data = res.json()

        assert data["session_id"] == session_id
        assert data["class_rombel"] == rombel
        assert data["total_students"] == 5
        # class average from measured values only: (0.85 + 0.30 + 0.35) / 3
        assert data["class_avg_mastery"] == pytest.approx(0.5, abs=1e-3)
        assert [s["kc_id"] for s in data["strengths"]] == [kc]
        assert data["source"] in ("llm_9router", "deterministic_fallback")
        assert "sangat kokoh" not in data["narrative_summary"]

        pairs = data["peer_tutoring_recommendations"]
        assert len(pairs) == 1
        assert pairs[0]["tutor_student_code"] == f"tutor_{tag}"
        assert sorted(pairs[0]["mentee_student_codes"]) == sorted([f"m1_{tag}", f"m2_{tag}"])
        involved = {pairs[0]["tutor_student_code"], *pairs[0]["mentee_student_codes"]}
        assert f"idle_{tag}" not in involved
        assert f"inherited_{tag}" not in involved


@pytest.mark.asyncio
async def test_agent_t3_summary_without_data_says_so():
    from backend.app.db.models import QuizSession

    tag = uuid.uuid4().hex[:6]
    async with AsyncSessionLocal() as session:
        sess = QuizSession(class_rombel=f"EMPTY_{tag}", title=f"Kosong {tag}", is_active=True)
        session.add(sess)
        await session.commit()
        session_id = sess.id

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        data = (await client.get("/api/teacher/session-summary", params={"session_id": session_id})).json()
        assert data["strengths"] == []
        assert data["peer_tutoring_recommendations"] == []
        assert "belum memiliki jawaban siswa" in data["narrative_summary"]


@pytest.mark.asyncio
async def test_agent_t1_semantic_labeling_and_review():
    """
    US-05: Agent T1 semantically categorizes new item prompt into KC, TOLT,
    difficulty (1-3), and computes confidence score.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # 1. Label a WLAN security question
        label_payload = {
            "prompt_text": "Siswa diminta mengkonfigurasi SSID laboratorium dengan enkripsi WPA3-SAE untuk mencegah serangan brute force dictionary attack.",
            "options": {
                "A": "Mengaktifkan WPA3-SAE",
                "B": "Mengaktifkan WEP 64-bit",
                "C": "Menonaktifkan broadcast SSID",
                "D": "Menggunakan WPA-PSK TKIP"
            },
            "explanation": "WPA3 menggunakan Simultaneous Authentication of Equals (SAE) yang tahan terhadap offline dictionary attack."
        }
        res = await client.post("/api/teacher/items/label", json=label_payload)
        assert res.status_code == 200
        label_data = res.json()

        assert label_data["primary_kc_id"] == "WLAN_SECURITY_AUTH"
        assert 0.0 <= label_data["confidence"] <= 1.0
        assert label_data["nominal_difficulty"] in (1, 2, 3)
        assert label_data["bloom_level"] in ("C1", "C2", "C3", "C4", "C5")

        # 2. Check Teacher Review Queue
        res_queue = await client.get("/api/teacher/items/review-queue")
        assert res_queue.status_code == 200
        queue = res_queue.json()
        assert len(queue) > 0
        first_item = queue[0]

        # 3. Approve / edit label for item in review queue
        approve_payload = {
            "primary_kc_id": "WLAN_STANDARDS",
            "bloom_level": "C2",
            "indikator_id": "IND-01.1",
            "jonassen_phase": "SYMPTOM_RECOGNITION",
            "difficulty_nominal": 2,
            "teacher_notes": "Ditinjau oleh Guru TKJ: Terkonfirmasi sesuai materi 802.11"
        }
        res_app = await client.post(f"/api/teacher/items/{first_item['item_id']}/approve-label", json=approve_payload)
        assert res_app.status_code == 200
        app_data = res_app.json()
        assert app_data["status"] == "success"
        assert app_data["primary_kc_id"] == "WLAN_STANDARDS"
        assert app_data["difficulty_nominal"] == 2
        assert app_data["bloom_level"] == "C2"
        assert app_data["indikator_id"] == "IND-01.1"
        assert app_data["label_status"] == "ditinjau_guru"

        # 4. Validation error on out-of-range difficulty_nominal (> 3)
        bad_diff_payload = {
            "primary_kc_id": "WLAN_STANDARDS",
            "bloom_level": "C2",
            "difficulty_nominal": 999
        }
        res_bad_diff = await client.post(f"/api/teacher/items/{first_item['item_id']}/approve-label", json=bad_diff_payload)
        assert res_bad_diff.status_code == 422

        # 5. Validation error on non-existent primary_kc_id
        bad_kc_payload = {
            "primary_kc_id": "NON_EXISTENT_KC",
            "bloom_level": "C2",
            "difficulty_nominal": 2
        }
        res_bad_kc = await client.post(f"/api/teacher/items/{first_item['item_id']}/approve-label", json=bad_kc_payload)
        assert res_bad_kc.status_code == 400


@pytest.mark.asyncio
async def test_feedback_audio_assets_served():
    """Student quiz and landing demo feedback audio files must be served over /assets/audio/."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        for filename in ("correct_answer.mp3", "wrong_answer.mp3"):
            res = await client.get(f"/assets/audio/{filename}")
            assert res.status_code == 200, f"Expected 200 for {filename}, got {res.status_code}"
            assert "audio" in res.headers.get("content-type", ""), f"Expected audio content-type for {filename}"
            assert len(res.content) > 1000


@pytest.mark.asyncio
async def test_hint_usage_is_tracked_server_side():
    """h = 0.5 must come from the server hint log; a client claiming no hint cannot bypass it."""
    from backend.app.engine.cognitive import update_mastery

    code = f"tstd_{uuid.uuid4().hex[:6]}"
    async with AsyncSessionLocal() as session:
        session.add(Student(anonymous_code=code, class_rombel="XI TKJ 1"))
        await session.commit()

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        item = (await client.get(f"/api/quiz/{code}/next")).json()
        hint = await client.post("/api/quiz/hint", json={
            "student_code": code, "item_id": item["item_id"], "requested_level": 2,
            "session_id": item.get("session_id"),
        })
        assert hint.status_code == 200

        from backend.app.db.models import Item
        async with AsyncSessionLocal() as session:
            db_item = await session.get(Item, item["item_id"])
            correct = db_item.correct_answer
            difficulty = db_item.difficulty_nominal

        res = (await client.post("/api/quiz/submit", json={
            "student_code": code, "item_id": item["item_id"], "choice": correct,
            "session_id": item.get("session_id"), "used_hint": False, "hint_level": 0,
        })).json()

        assert res["is_correct"] is True
        expected = update_mastery(res["mastery_before"], 1, difficulty, used_hint=True)
        assert res["mastery_after"] == pytest.approx(round(expected, 4), abs=1e-4)


@pytest.mark.asyncio
async def test_inactive_session_rejects_student_work():
    """Students may only work in their class's active session; inactive ones are review-only."""
    from backend.app.db.models import Item, QuizSession, StudentAttempt

    tag = uuid.uuid4().hex[:6]
    rombel = f"GUARD_{tag}"
    async with AsyncSessionLocal() as session:
        student = Student(anonymous_code=f"tstd_g{tag}", class_rombel=rombel)
        other = Student(anonymous_code=f"tstd_o{tag}", class_rombel=f"OTHER_{tag}")
        active = QuizSession(class_rombel=rombel, title=f"Aktif {tag}", is_active=True)
        closed = QuizSession(class_rombel=rombel, title=f"Tutup {tag}", is_active=False)
        done = QuizSession(class_rombel=rombel, title=f"Selesai {tag}", is_active=False)
        session.add_all([student, other, active, closed, done])
        await session.flush()
        session.add(StudentAttempt(student_id=student.id, session_id=done.id, status="COMPLETED",
                                   current_sequence=20, answered_item_ids=[]))
        item_id = (await session.execute(select(Item.id).limit(1))).scalar_one()
        await session.commit()
        ids = (active.id, closed.id, done.id)

    active_id, closed_id, done_id = ids
    code = f"tstd_g{tag}"
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        res = await client.get(f"/api/quiz/{code}/next", params={"session_id": closed_id})
        assert res.status_code == 409
        assert "SESSION_INACTIVE" in res.json()["detail"]

        res = await client.post("/api/quiz/submit", json={
            "student_code": code, "item_id": item_id, "choice": "A",
            "session_id": closed_id, "response_time_ms": 1000,
        })
        assert res.status_code == 409

        res = await client.post("/api/quiz/hint", json={
            "student_code": code, "item_id": item_id, "session_id": closed_id, "requested_level": 1,
        })
        assert res.status_code == 409

        # A finished inactive session may still be opened to see the result screen
        res = await client.get(f"/api/quiz/{code}/next", params={"session_id": done_id})
        assert res.status_code == 200
        assert res.json()["is_completed"] is True

        # Another class's session is refused
        res = await client.get(f"/api/quiz/tstd_o{tag}/next", params={"session_id": active_id})
        assert res.status_code == 403

        # The active session works
        res = await client.get(f"/api/quiz/{code}/next", params={"session_id": active_id})
        assert res.status_code == 200
