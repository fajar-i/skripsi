"""
Seed SYNTHETIC classroom data into a COPY of the LogiTrace database, for UI preview only.

Never run against the real logitrace.db: the `interactions` table is an append-only audit
trail, so synthetic rows written there could never be removed and would contaminate study data.

Usage (from apps/logitrace):
    python tools/seed_preview.py                 # copies logitrace.db -> logitrace_preview.db, then seeds
    python tools/seed_preview.py --fresh-copy    # same, overwriting an existing preview DB

Then serve the preview DB on another port:
    LOGITRACE_DB_URL=sqlite+aiosqlite:///<abs path>/logitrace_preview.db \
        python -m uvicorn logitrace.backend.app.main:app --port 8001   (run from apps/)
"""

import argparse
import json
import os
import random
import shutil
import sqlite3
import sys
import uuid
from datetime import datetime, timedelta, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOURCE_DB = os.path.join(ROOT, "logitrace.db")
PREVIEW_DB = os.path.join(ROOT, "logitrace_preview.db")

SESSION_TITLE = "Sesi 3: Diagnosis Gangguan Jaringan Nirkabel (Data Sintetis)"
SESSION_NUMBER = 3
MAX_ITEMS = 20

# Quiz order: the first 9 KCs get answered, the last 3 stay "belum dijawab".
KC_ORDER = [
    "WLAN_STANDARDS", "WLAN_TOPOLOGY_BSS", "IP_PEER_CONFIG", "WLAN_FREQ_CHANNEL",
    "WLAN_SECURITY_AUTH", "WLAN_HOST_HARDENING", "WLAN_SIGNAL_PROP", "WLAN_ROAMING_PROB",
    "WLAN_CHANNEL_COLLISION", "ICMP_CONNECTIVITY", "ICMP_TROUBLE_DHU", "ICMP_TROUBLE_RTO",
]
ANSWERED_KCS = KC_ORDER[:9]

# Per-topic difficulty shift, to give the dashboards a realistic shape:
#   FREQ_CHANNEL  -> weak class-wide, but strong students master it (student tutor groups)
#   HOST_HARDENING -> nobody masters it (teacher-led group)
KC_OFFSET = {
    "WLAN_STANDARDS": +0.12, "WLAN_TOPOLOGY_BSS": +0.18, "IP_PEER_CONFIG": -0.12,
    "WLAN_FREQ_CHANNEL": -0.28, "WLAN_SECURITY_AUTH": -0.05, "WLAN_HOST_HARDENING": -0.40,
    "WLAN_SIGNAL_PROP": +0.05, "WLAN_ROAMING_PROB": 0.0, "WLAN_CHANNEL_COLLISION": -0.02,
}
KC_CAP = {"WLAN_HOST_HARDENING": 0.62}

N_NOT_STARTED, N_COMPLETED = 8, 8   # the rest are IN_PROGRESS
N_STUCK = 3
GUESS, SLIP = 0.20, 0.10


def ts(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S.%f")


def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fresh-copy", action="store_true", help="overwrite logitrace_preview.db from logitrace.db")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    if os.path.exists(PREVIEW_DB) and not args.fresh_copy:
        sys.exit(f"{PREVIEW_DB} already exists. Re-run with --fresh-copy to rebuild it.")
    shutil.copyfile(SOURCE_DB, PREVIEW_DB)
    assert os.path.abspath(PREVIEW_DB) != os.path.abspath(SOURCE_DB)

    rng = random.Random(args.seed)
    db = sqlite3.connect(PREVIEW_DB)
    cur = db.cursor()

    # Drop leftover pytest accounts (tstd_*) from the copy so the preview shows a clean 34-student class.
    test_ids = [r[0] for r in cur.execute("SELECT id FROM students WHERE anonymous_code NOT LIKE 'std\\_%' ESCAPE '\\'")]
    for table in ("interactions", "student_attempts", "mastery_snapshot", "hint_events"):
        cur.executemany(f"DELETE FROM {table} WHERE student_id=?", [(i,) for i in test_ids])
    cur.executemany("DELETE FROM students WHERE id=?", [(i,) for i in test_ids])

    students = cur.execute(
        "SELECT id, anonymous_code FROM students WHERE class_rombel='XI TKJ 1' ORDER BY anonymous_code"
    ).fetchall()
    items_by_kc = {}
    for item_id, kc_id, correct in cur.execute(
        "SELECT id, primary_kc_id, correct_answer FROM items WHERE is_active=1 AND is_calibration=0"
    ):
        items_by_kc.setdefault(kc_id, []).append((item_id, correct))
    classroom = cur.execute("SELECT id FROM classrooms WHERE name='XI TKJ 1'").fetchone()

    now = datetime.now(timezone.utc).replace(tzinfo=None)
    start = now - timedelta(minutes=30)

    # 1. New active session
    session_id = str(uuid.uuid4())
    cur.execute("UPDATE quiz_sessions SET is_active=0 WHERE class_rombel='XI TKJ 1'")
    cur.execute(
        "INSERT INTO quiz_sessions (id, classroom_id, class_rombel, title, session_number, max_items, is_active, created_at)"
        " VALUES (?,?,?,?,?,?,1,?)",
        (session_id, classroom[0] if classroom else None, "XI TKJ 1", SESSION_TITLE, SESSION_NUMBER, MAX_ITEMS, ts(start)),
    )

    # 2. Mastery snapshots are per student (not per session): rebuild them all in the preview copy
    cur.execute("DELETE FROM mastery_snapshot")

    order = students[:]
    rng.shuffle(order)
    not_started = {s[0] for s in order[:N_NOT_STARTED]}
    completed = {s[0] for s in order[N_NOT_STARTED:N_NOT_STARTED + N_COMPLETED]}
    in_progress = [s for s in order[N_NOT_STARTED + N_COMPLETED:]]
    # Stuck students: weakest in-progress students
    ability = {s[0]: clamp(rng.gauss(0.62, 0.17), 0.18, 0.95) for s in students}
    stuck = {s[0] for s in sorted(in_progress, key=lambda s: ability[s[0]])[:N_STUCK]}
    for sid in stuck:
        ability[sid] = min(ability[sid], 0.30)

    interactions = []  # rows appended in chronological order per student
    late_rows = []     # stuck students' final wrong streak, timestamped last
    counts = {"NOT_STARTED": 0, "IN_PROGRESS": 0, "COMPLETED": 0}

    for sid, code in students:
        if sid in not_started:
            status, kcs = "NOT_STARTED", []
        elif sid in completed:
            status, kcs = "COMPLETED", ANSWERED_KCS
        else:
            status, kcs = "IN_PROGRESS", ANSWERED_KCS[: rng.randint(4, 8)]
        counts[status] += 1

        final_m = {}
        for kc in kcs:
            m = clamp(ability[sid] + KC_OFFSET.get(kc, 0) + rng.gauss(0, 0.09), 0.06, 0.96)
            final_m[kc] = min(m, KC_CAP.get(kc, 1.0))
        if sid in stuck and kcs:
            weakest = min(kcs, key=lambda k: final_m[k])
            final_m[weakest] = rng.uniform(0.10, 0.20)

        # Interactions: 2 items per KC, ~20 items for a completed student
        seq, answered = 0, []
        t = start + timedelta(seconds=rng.randint(0, 240))
        for kc in kcs:
            pool = items_by_kc.get(kc, [])
            picks = rng.sample(pool, k=min(2, len(pool)))
            m_before = 0.25
            for i, (item_id, correct) in enumerate(picks):
                m_after = m_before + (final_m[kc] - m_before) * (i + 1) / len(picks)
                p = GUESS + (1 - SLIP - GUESS) * m_before
                result = 1 if rng.random() < GUESS + (1 - SLIP - GUESS) * final_m[kc] else 0
                choice = correct if result else rng.choice([c for c in "ABCD" if c != correct])
                seq += 1
                t += timedelta(seconds=rng.randint(35, 90))
                interactions.append((sid, item_id, seq, result, choice, p, m_before, m_after,
                                     rng.randint(9000, 75000), rng.choice([0, 0, 0, 1]), t))
                answered.append(item_id)
                m_before = m_after

        if sid in stuck and kcs:
            weakest = min(kcs, key=lambda k: final_m[k])
            pool = items_by_kc[weakest]
            used = set(answered)
            extra = [it for it in pool if it[0] not in used][:3]
            for j, (item_id, correct) in enumerate(extra):
                seq += 1
                choice = rng.choice([c for c in "ABCD" if c != correct])
                late_rows.append((sid, item_id, seq, 0, choice, 0.3, final_m[weakest], final_m[weakest],
                                  rng.randint(40000, 110000), 1, now - timedelta(seconds=90 - j * 20)))
                answered.append(item_id)

        # Snapshots: measured topics = high confidence, the rest = prior 0.25 / low confidence
        for kc in KC_ORDER:
            m, conf = (final_m[kc], "high") if kc in final_m else (0.25, "low")
            cur.execute(
                "INSERT INTO mastery_snapshot (id, student_id, kc_id, current_mastery, confidence, last_updated_at)"
                " VALUES (?,?,?,?,?,?)",
                (str(uuid.uuid4()), sid, kc, round(m, 4), conf, ts(now)),
            )

        started_at = ts(start) if status != "NOT_STARTED" else None
        cur.execute(
            "INSERT INTO student_attempts (id, student_id, session_id, status, current_sequence, answered_item_ids,"
            " final_mastery, started_at, completed_at, created_at) VALUES (?,?,?,?,?,?,?,?,?,?)",
            (str(uuid.uuid4()), sid, session_id, status, seq, json.dumps(answered),
             round(sum(final_m.values()) / len(final_m), 4) if status == "COMPLETED" else None,
             started_at, ts(t) if status == "COMPLETED" else None, ts(start)),
        )

    for sid, item_id, seq, res, choice, p, mb, ma, rt, hint, t in interactions + late_rows:
        cur.execute(
            "INSERT INTO interactions (id, student_id, item_id, session_id, session_number, sequence_number,"
            " response_result, student_choice, predicted_p, mastery_before, mastery_after, response_time_ms,"
            " hint_level_used, is_calibration, created_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,0,?)",
            (str(uuid.uuid4()), sid, item_id, session_id, SESSION_NUMBER, seq, res, choice,
             round(p, 4), round(mb, 4), round(ma, 4), rt, hint, ts(min(t, now))),
        )

    db.commit()
    db.close()
    print(f"Preview DB: {PREVIEW_DB}")
    print(f"Session: {SESSION_TITLE} ({session_id})")
    print(f"Students: {counts} | interactions: {len(interactions) + len(late_rows)} | stuck: {N_STUCK}")


if __name__ == "__main__":
    main()
