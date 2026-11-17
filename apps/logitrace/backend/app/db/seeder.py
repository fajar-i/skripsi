"""
LogiTrace: Database Seeder Script.
Seeds 12 KCs, 180 adaptive items, and 34 anonymous students for XI TKJ 1.
"""

import json
import logging
import os
import sys
from typing import Dict, List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .database import AsyncSessionLocal, init_db
from .models import Student, KnowledgeComponent, Item, MasterySnapshot, ClassRoom, QuizSession, StudentAttempt

logger = logging.getLogger("seeder")

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "data"))
KCS_PATH = os.path.join(DATA_DIR, "l1_knowledge_base", "kcs.json")
ITEMS_PATH = os.path.join(DATA_DIR, "l2_item_bank", "items_adaptive_180.json")


async def seed_database(session: AsyncSession) -> Dict[str, int]:
    counts = {"kcs": 0, "items": 0, "students": 0, "snapshots": 0}

    # 1. Seed Knowledge Components (12 KCs)
    if os.path.exists(KCS_PATH):
        with open(KCS_PATH, "r", encoding="utf-8") as f:
            kcs_data = json.load(f)

        for kc_dict in kcs_data:
            existing = await session.get(KnowledgeComponent, kc_dict["id"])
            if not existing:
                kc_obj = KnowledgeComponent(
                    id=kc_dict["id"],
                    name=kc_dict["name"],
                    description=kc_dict.get("description", ""),
                    prerequisites=kc_dict.get("prerequisites", [])
                )
                session.add(kc_obj)
                counts["kcs"] += 1
        await session.flush()

    # 2. Seed Items (180 items)
    if os.path.exists(ITEMS_PATH):
        with open(ITEMS_PATH, "r", encoding="utf-8") as f:
            items_data = json.load(f)

        for item_dict in items_data:
            existing = await session.get(Item, item_dict["id"])
            if not existing:
                item_obj = Item(
                    id=item_dict["id"],
                    primary_kc_id=item_dict["primary_kc"],
                    prompt_text=item_dict["prompt_text"],
                    options=item_dict["options"],
                    correct_answer=item_dict["correct_answer"],
                    difficulty_nominal=item_dict["difficulty"],
                    indikator_id=item_dict.get("indikator_id"),
                    bloom_level=item_dict.get("bloom_level"),
                    jonassen_phase=item_dict.get("jonassen_phase"),
                    label_status=item_dict.get("label_status", "draf_ai"),
                    is_calibration=item_dict.get("is_calibration", False),
                    is_active=True,
                    explanation=item_dict.get("explanation", "")
                )
                session.add(item_obj)
                counts["items"] += 1
            elif existing.bloom_level is None:
                # Backfill kisi-kisi metadata on databases created before the schema change
                existing.indikator_id = item_dict.get("indikator_id")
                existing.bloom_level = item_dict.get("bloom_level")
                existing.jonassen_phase = item_dict.get("jonassen_phase")
                existing.label_status = item_dict.get("label_status", "draf_ai")
        await session.flush()

    # 3. Seed 34 Anonymous Students (std_01 to std_34)
    # Query all KC IDs for initial mastery snapshots
    kc_stmt = select(KnowledgeComponent.id)
    kc_result = await session.execute(kc_stmt)
    all_kc_ids = [row[0] for row in kc_result.all()]

    for i in range(1, 35):
        student_code = f"std_{i:02d}"
        stmt = select(Student).where(Student.anonymous_code == student_code)
        res = await session.execute(stmt)
        student_obj = res.scalar_one_or_none()

        if not student_obj:
            student_obj = Student(
                anonymous_code=student_code,
                class_rombel="XI TKJ 1"
            )
            session.add(student_obj)
            await session.flush()
            counts["students"] += 1

            # Seed initial mastery snapshots (m = 0.25, confidence = low)
            for kc_id in all_kc_ids:
                snapshot = MasterySnapshot(
                    student_id=student_obj.id,
                    kc_id=kc_id,
                    current_mastery=0.25,
                    confidence="low"
                )
                session.add(snapshot)
                counts["snapshots"] += 1

    # 4. Seed Classroom & Default Quiz Session (Google Classroom standard)
    cls_stmt = select(ClassRoom).where(ClassRoom.name == "XI TKJ 1")
    cls_res = await session.execute(cls_stmt)
    classroom = cls_res.scalar_one_or_none()
    if not classroom:
        classroom = ClassRoom(
            name="XI TKJ 1",
            subject="Teknologi Jaringan Kabel dan Nirkabel",
            teacher_name="Pak Budi"
        )
        session.add(classroom)
        await session.flush()

    sess_stmt = select(QuizSession).where(QuizSession.id == "session_01")
    sess_res = await session.execute(sess_stmt)
    default_session = sess_res.scalar_one_or_none()
    if not default_session:
        default_session = QuizSession(
            id="session_01",
            classroom_id=classroom.id,
            class_rombel="XI TKJ 1",
            title="Sesi 1: Evaluasi Formatif Adaptif (Instalasi Jaringan Nirkabel - TP 2.1 & 2.2)",
            session_number=1,
            max_items=20,
            is_active=True
        )
        session.add(default_session)
        await session.flush()

    # Seed student attempts for default session if not existing
    all_stds_stmt = select(Student).where(Student.class_rombel == "XI TKJ 1")
    all_stds_res = await session.execute(all_stds_stmt)
    all_class_stds = all_stds_res.scalars().all()

    for st in all_class_stds:
        att_stmt = select(StudentAttempt).where(
            StudentAttempt.session_id == default_session.id,
            StudentAttempt.student_id == st.id
        )
        att_res = await session.execute(att_stmt)
        if not att_res.scalar_one_or_none():
            attempt = StudentAttempt(
                student_id=st.id,
                session_id=default_session.id,
                status="NOT_STARTED",
                current_sequence=0,
                answered_item_ids=[]
            )
            session.add(attempt)

    await session.commit()
    return counts


async def main():
    await init_db()
    async with AsyncSessionLocal() as session:
        counts = await seed_database(session)
        print(f"Seeded: {counts}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
