"""
LogiTrace: 34-Student End-to-End Simulation Runner.
Simulates a full class (34 students of XI TKJ 1) in Zone B station rotation:
- Each student completes 20 items (6 calibration + 14 adaptive ZPD items)
- Total 680 interactions recorded in append-only database
- Exercises cognitive engine, hint scaffolding, and ambient dashboard telemetry
"""

import asyncio
import json
import os
import sys
import time
from typing import Dict, List
import numpy as np

# Ensure backend app is in sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from backend.app.db.database import AsyncSessionLocal, init_db
from backend.app.db.models import Student, Item, KnowledgeComponent, Interaction, MasterySnapshot
from backend.app.db.seeder import seed_database
from backend.app.engine.cognitive import calculate_predicted_p, update_mastery
from backend.app.engine.zpd_selector import ZPDSelector, ItemCandidate
from backend.app.routers.teacher_ambient import compute_ambient_state


async def run_simulation():
    print("=" * 70)
    print("LOGITRACE E2E SIMULATION: 34 SISWA KELAS XI TKJ 1 (ZONA B)")
    print("=" * 70)

    # 1. Initialize database & seed
    await init_db()
    async with AsyncSessionLocal() as session:
        counts = await seed_database(session)
        print(f"[*] Database seeded: {counts}")

    # Load DAG
    dag_path = os.path.join(BASE_DIR, "data", "l1_knowledge_base", "dag_prerequisites.json")
    with open(dag_path, "r", encoding="utf-8") as f:
        dag_edges = json.load(f).get("edges", [])
    selector = ZPDSelector(dag_edges)

    # 2. Simulate 34 Students
    t_start = time.perf_counter()
    total_interactions = 0
    total_hints = 0

    async with AsyncSessionLocal() as db:
        # Load the 34 XI TKJ 1 students explicitly (filtering out test students)
        from sqlalchemy import select
        stmt = (
            select(Student)
            .where(Student.anonymous_code.like("std_%"))
            .order_by(Student.anonymous_code)
        )
        res = await db.execute(stmt)
        all_stds = res.scalars().all()
        # Ensure only std_01 through std_34
        students = [s for s in all_stds if len(s.anonymous_code) == 6 and s.anonymous_code[4:].isdigit()]

        # Load all items
        item_res = await db.execute(select(Item).where(Item.is_active == True))
        all_items = item_res.scalars().all()
        item_map = {it.id: it for it in all_items}

        candidates = [
            ItemCandidate(
                id=item.id,
                primary_kc=item.primary_kc_id,
                difficulty=item.difficulty_nominal,
                is_calibration=item.is_calibration
            )
            for item in all_items
        ]

        calibration_items = [it for it in all_items if it.is_calibration]

        print(f"[*] Loaded {len(students)} students and {len(all_items)} candidate items.")
        print("[*] Commencing 20-item adaptive evaluation per student...")

        for s_idx, student in enumerate(students):
            # Load mastery snapshots for this student
            snap_res = await db.execute(select(MasterySnapshot).where(MasterySnapshot.student_id == student.id))
            snapshots = {s.kc_id: s for s in snap_res.scalars().all()}
            mastery_dict = {kc: snap.current_mastery for kc, snap in snapshots.items()}

            # Student latent capability (heterogeneous: some fast, some stuck)
            latent_ability = np.random.uniform(0.20, 0.85)
            answered_ids = set()
            last_kc = None

            for seq in range(1, 21):
                is_calibration = (seq <= 6)

                # Select Item
                selected_item = None
                if is_calibration:
                    for c_item in calibration_items:
                        if c_item.id not in answered_ids:
                            selected_item = c_item
                            break
                else:
                    rec = selector.select_next_item(
                        candidate_items=candidates,
                        student_mastery=mastery_dict,
                        answered_item_ids=answered_ids,
                        last_kc_id=last_kc
                    )
                    if rec:
                        selected_item = item_map[rec.id]

                if not selected_item:
                    # Fallback to any unattempted item
                    for it in all_items:
                        if it.id not in answered_ids:
                            selected_item = it
                            break

                answered_ids.add(selected_item.id)
                last_kc = selected_item.primary_kc_id

                # Calculate P_hat
                current_m = mastery_dict.get(selected_item.primary_kc_id, 0.25)
                p_hat = calculate_predicted_p(current_m, selected_item.difficulty_nominal)

                # Simulate Hint request if difficult or stuck
                used_hint = False
                hint_lvl = 0
                if selected_item.difficulty_nominal == 3 or (current_m < 0.35 and np.random.random() < 0.60):
                    used_hint = True
                    hint_lvl = np.random.choice([1, 2, 3])
                    total_hints += 1

                # Simulate Student response (Slip & Guess)
                prob_success = p_hat if not used_hint else min(p_hat + 0.20, 0.95)
                is_correct = 1 if np.random.random() < prob_success else 0

                # L3 Update rule
                new_m = update_mastery(
                    current_m=current_m,
                    response_result=is_correct,
                    difficulty=selected_item.difficulty_nominal,
                    used_hint=used_hint
                )

                # Record interaction (strictly append-only)
                inter = Interaction(
                    student_id=student.id,
                    item_id=selected_item.id,
                    session_number=1,
                    sequence_number=seq,
                    response_result=is_correct,
                    student_choice=selected_item.correct_answer if is_correct else "B",
                    predicted_p=round(p_hat, 4),
                    mastery_before=round(current_m, 4),
                    mastery_after=round(new_m, 4),
                    response_time_ms=int(np.random.normal(25000, 5000)),
                    hint_level_used=hint_lvl if used_hint else 0,
                    is_calibration=is_calibration
                )
                db.add(inter)
                total_interactions += 1

                # Update memory & snapshot
                mastery_dict[selected_item.primary_kc_id] = new_m
                if selected_item.primary_kc_id in snapshots:
                    snapshots[selected_item.primary_kc_id].current_mastery = round(new_m, 4)
                    snapshots[selected_item.primary_kc_id].confidence = "high"

            await db.commit()
            if (s_idx + 1) % 10 == 0 or s_idx == len(students) - 1:
                print(f"  -> {s_idx + 1}/34 Siswa selesai ({total_interactions} interaksi terekam)")

        # 3. Ambient Dashboard verification
        print("[*] Computing Teacher Ambient Dashboard state...")
        ambient_state = await compute_ambient_state(db)

    t_elapsed = time.perf_counter() - t_start

    print("\n" + "=" * 70)
    print("SIMULATION RESULTS SUMMARY:")
    print("=" * 70)
    print(f"Total Siswa XI TKJ 1       : {len(students)}")
    print(f"Total Interaksi Append-Only: {total_interactions} (Ekspektasi: 680)")
    print(f"Total Permintaan Petunjuk  : {total_hints}")
    print(f"Durasi Eksekusi Simulasi   : {t_elapsed:.2f} detik")
    print(f"Rata-rata Penguasaan Kelas : m = {ambient_state.class_average_mastery:.3f}")
    print(f"Top-3 Stuck Students Terdeteksi: {len(ambient_state.top_stuck_students)}")

    for i, s in enumerate(ambient_state.top_stuck_students, 1):
        print(f"  #{i} {s.student_code} | KC: {s.stuck_kc_name} | m = {s.current_mastery:.2f} | Gagal: {s.consecutive_errors}x")

    assert total_interactions == 680, f"Expected 680 interactions, got {total_interactions}"
    print("\n[SUCCESS] E2E Simulasi 34 Siswa berhasil 100% tanpa kendala!")
    return True


if __name__ == "__main__":
    asyncio.run(run_simulation())
