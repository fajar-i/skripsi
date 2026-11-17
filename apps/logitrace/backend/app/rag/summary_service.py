"""
LogiTrace: Agent T3 — Session Narrative Summary & Peer-Tutoring Recommendation Service (US-06).
Adheres to Station Rotation syntax (minute 80 closing reflection) and Kurikulum Merdeka Fase F TKJ.
Narrative via 9router (5.0 s hard deadline) with a data-driven deterministic fallback.
"""

from datetime import datetime, timezone
import logging
import os
import time
from typing import Dict, List, Optional, Tuple
from sqlalchemy import desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.models import (
    AgentLog,
    Interaction,
    KnowledgeComponent,
    MasterySnapshot,
    QuizSession,
    Student,
    StudentAttempt
)
from ..schemas.summary import (
    KCMasteryMetric,
    PeerTutoringMatch,
    SessionSummaryResponse
)

from .secure_client import SecureLLMClient

logger = logging.getLogger("summary_service")

TUTOR_MIN_M = 0.70          # same threshold as "mastered" in the paper (Section 2.2)
MENTEE_MAX_M = 0.45
MAX_MENTEES_PER_TUTOR = 2

# Teacher-facing wording. Thresholds match the dashboard legend (frontend/teacher/app.js LEVELS).
WEAK_TOPIC_MAX = 0.55     # topics below this are worth re-teaching
STRONG_TOPIC_MIN = 0.75   # topics at/above this count as mastered by the class


def _pct(m: float) -> str:
    return f"{round(m * 100)}%"


def _level(m: float) -> str:
    if m < 0.35:
        return "belum paham"
    if m < 0.55:
        return "berkembang"
    if m < 0.75:
        return "cakap"
    return "mahir"


def _join_id(items: List[str]) -> str:
    """Indonesian list join: 'A', 'A dan B', 'A, B, dan C'."""
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} dan {items[1]}"
    return f"{', '.join(items[:-1])}, dan {items[-1]}"


class SummaryService:
    """Agent T3 Pedagogical Summary & Peer-Tutoring Orchestrator."""

    def __init__(self, llm_client: Optional[SecureLLMClient] = None):
        self.llm_client = llm_client or SecureLLMClient()

    async def generate_session_summary(
        self,
        db: AsyncSession,
        session_id: Optional[str] = None
    ) -> SessionSummaryResponse:
        start_time = time.perf_counter()

        # 1. Resolve target session
        target_session = None
        if session_id:
            target_session = await db.get(QuizSession, session_id)
        if not target_session:
            stmt_active = select(QuizSession).where(
                QuizSession.class_rombel == "XI TKJ 1",
                QuizSession.is_active == True
            ).order_by(desc(QuizSession.created_at))
            res_active = await db.execute(stmt_active)
            target_session = res_active.scalar_one_or_none()

        sess_id = target_session.id if target_session else "session_01"
        sess_title = target_session.title if target_session else "Sesi 1: Evaluasi Adaptif Instalasi Jaringan (TP 2.1 & 2.2)"
        class_rombel = target_session.class_rombel if target_session else "XI TKJ 1"

        # 2. Fetch all students
        std_stmt = select(Student).where(Student.class_rombel == class_rombel).order_by(Student.anonymous_code)
        std_res = await db.execute(std_stmt)
        students = std_res.scalars().all()
        student_dict = {s.id: s.anonymous_code for s in students}

        # 3. Fetch attempts for progress counters
        att_stmt = select(StudentAttempt).where(StudentAttempt.session_id == sess_id)
        att_res = await db.execute(att_stmt)
        attempts = att_res.scalars().all()
        comp_count = sum(1 for a in attempts if a.status == "COMPLETED")
        in_prog_count = sum(1 for a in attempts if a.status == "IN_PROGRESS")
        not_start_count = len(students) - (comp_count + in_prog_count)
        active_student_ids = {
            a.student_id for a in attempts
            if a.status in ("IN_PROGRESS", "COMPLETED") and a.answered_item_ids
        }

        # 4. Fetch KCs
        kc_stmt = select(KnowledgeComponent)
        kc_res = await db.execute(kc_stmt)
        kcs = {kc.id: kc.name for kc in kc_res.scalars().all()}

        # 5. Directly measured mastery only (confidence == 'high'), for students who
        #    actually answered items in this session. Prior values (0.25) and values
        #    inherited from DAG parents are NOT evidence and are excluded.
        snap_stmt = select(MasterySnapshot).where(
            MasterySnapshot.student_id.in_(active_student_ids),
            MasterySnapshot.confidence == "high",
        )
        snap_res = await db.execute(snap_stmt)
        snapshots = snap_res.scalars().all()

        kc_student_mastery: Dict[str, List[Tuple[str, float]]] = {k: [] for k in kcs.keys()}
        for s in snapshots:
            std_code = student_dict.get(s.student_id)
            if std_code and s.kc_id in kcs:
                kc_student_mastery[s.kc_id].append((std_code, s.current_mastery))

        # 6. Aggregate KC metrics (only KCs with at least one measured student)
        kc_metrics: List[KCMasteryMetric] = []
        for kc_id, name in kcs.items():
            scores = [m for _, m in kc_student_mastery[kc_id]]
            if not scores:
                continue
            kc_metrics.append(KCMasteryMetric(
                kc_id=kc_id,
                kc_name=name,
                avg_mastery=round(sum(scores) / len(scores), 3),
                student_count=len(scores),
                struggling_count=sum(1 for v in scores if v <= MENTEE_MAX_M),
                mastered_count=sum(1 for v in scores if v >= TUTOR_MIN_M),
            ))

        sorted_kcs = sorted(kc_metrics, key=lambda x: x.avg_mastery, reverse=True)
        strengths = sorted_kcs[:3]
        bottlenecks = sorted(sorted_kcs[-3:], key=lambda x: x.avg_mastery) if sorted_kcs else []

        # 7. Interaction statistics for session
        int_stmt = select(Interaction).where(Interaction.session_id == sess_id)
        int_res = await db.execute(int_stmt)
        interactions = int_res.scalars().all()
        total_resp = len(interactions)
        correct_resp = sum(1 for i in interactions if i.response_result == 1)
        accuracy_rate = round(correct_resp / total_resp, 3) if total_resp > 0 else 0.0
        avg_resp_time = int(sum(i.response_time_ms for i in interactions) / total_resp) if total_resp > 0 else 0

        all_measured = [m for pairs in kc_student_mastery.values() for _, m in pairs]
        class_avg_m = round(sum(all_measured) / len(all_measured), 3) if all_measured else 0.0

        # 8. Peer-tutoring: greedy one-to-two assignment per bottleneck KC.
        #    Each student is used at most once as tutor and at most once as mentee per session.
        peer_tutoring: List[PeerTutoringMatch] = []
        used_tutors: set = set()
        used_mentees: set = set()
        for bn in bottlenecks:
            pairs = kc_student_mastery[bn.kc_id]
            tutors = sorted(
                [p for p in pairs if p[1] >= TUTOR_MIN_M and p[0] not in used_tutors and p[0] not in used_mentees],
                key=lambda x: x[1], reverse=True,
            )
            mentees = sorted(
                [p for p in pairs if p[1] <= MENTEE_MAX_M and p[0] not in used_mentees and p[0] not in used_tutors],
                key=lambda x: x[1],
            )
            if not mentees:
                continue

            if not tutors:
                group = mentees[:MAX_MENTEES_PER_TUTOR]
                for code, _ in group:
                    used_mentees.add(code)
                codes = [c for c, _ in group]
                peer_tutoring.append(PeerTutoringMatch(
                    kc_id=bn.kc_id,
                    kc_name=bn.kc_name,
                    tutor_student_code="Guru Pendamping (Zona B)",
                    tutor_mastery=1.0,
                    mentee_student_codes=codes,
                    mentee_avg_mastery=round(sum(m for _, m in group) / len(group), 2),
                    action_guidance=(
                        f"Belum ada siswa yang menguasai {bn.kc_name}, jadi belum bisa dipasangkan "
                        f"dengan teman. Dampingi langsung {_join_id(codes)}."
                    ),
                ))
                continue

            mentee_queue = list(mentees)
            for tutor_code, tutor_m in tutors:
                if not mentee_queue:
                    break
                group = mentee_queue[:MAX_MENTEES_PER_TUTOR]
                mentee_queue = mentee_queue[MAX_MENTEES_PER_TUTOR:]
                used_tutors.add(tutor_code)
                for code, _ in group:
                    used_mentees.add(code)
                codes = [c for c, _ in group]
                peer_tutoring.append(PeerTutoringMatch(
                    kc_id=bn.kc_id,
                    kc_name=bn.kc_name,
                    tutor_student_code=tutor_code,
                    tutor_mastery=round(tutor_m, 2),
                    mentee_student_codes=codes,
                    mentee_avg_mastery=round(sum(m for _, m in group) / len(group), 2),
                    action_guidance=(
                        f"Minta {tutor_code} menjelaskan ulang {bn.kc_name} kepada {_join_id(codes)} "
                        "dengan contoh nyata, tanpa memberi kunci jawaban kuis."
                    ),
                ))

        # 9. Narrative Synthesis via LLM (with 3.0s timeout & deterministic fallback)
        narrative, source = await self._generate_narrative_text(
            sess_title=sess_title,
            class_rombel=class_rombel,
            class_avg_m=class_avg_m,
            comp_count=comp_count,
            in_prog_count=in_prog_count,
            total_students=len(students),
            accuracy_rate=accuracy_rate,
            total_responses=total_resp,
            strengths=strengths,
            bottlenecks=bottlenecks,
            peer_tutoring=peer_tutoring
        )

        latency_ms = int((time.perf_counter() - start_time) * 1000)

        # Audit log in append-only agent_logs
        agent_log = AgentLog(
            trigger_type="T3",
            prompt_hash=None,
            model_id=self.llm_client.model_name if source == "llm_9router" else "deterministic_t3_engine",
            raw_output=narrative,
            is_accepted=True,
            latency_ms=latency_ms
        )
        db.add(agent_log)
        await db.commit()

        return SessionSummaryResponse(
            session_id=sess_id,
            session_title=sess_title,
            class_rombel=class_rombel,
            total_students=len(students),
            completed_students=comp_count,
            in_progress_students=in_prog_count,
            not_started_students=not_start_count,
            class_avg_mastery=class_avg_m,
            accuracy_rate=accuracy_rate,
            total_responses=total_resp,
            avg_response_time_ms=avg_resp_time,
            strengths=strengths,
            bottlenecks=bottlenecks,
            narrative_summary=narrative,
            peer_tutoring_recommendations=peer_tutoring,
            source=source,
            latency_ms=latency_ms,
            timestamp=datetime.now(timezone.utc).isoformat()
        )

    async def _generate_narrative_text(
        self,
        sess_title: str,
        class_rombel: str,
        class_avg_m: float,
        comp_count: int,
        in_prog_count: int,
        total_students: int,
        accuracy_rate: float,
        total_responses: int,
        strengths: List[KCMasteryMetric],
        bottlenecks: List[KCMasteryMetric],
        peer_tutoring: List[PeerTutoringMatch]
    ) -> Tuple[str, str]:
        """Teacher-facing session notes (plain Indonesian, percentages, no research notation).

        Tries 9router first, falls back to a deterministic text that states only what the data shows.
        """
        started = comp_count + in_prog_count
        low_coverage = total_students > 0 and started / total_students < 0.5

        # No measured data: do not ask the LLM to narrate nothing.
        if not strengths:
            return (
                f"Sesi '{sess_title}' di kelas {class_rombel} belum memiliki jawaban siswa "
                f"({comp_count} dari {total_students} siswa selesai). "
                "Ringkasan akan tersedia setelah siswa mulai menjawab soal."
            ), "deterministic_fallback"

        strong = [s for s in strengths if s.avg_mastery >= STRONG_TOPIC_MIN]
        weak = [b for b in bottlenecks if b.avg_mastery < WEAK_TOPIC_MAX]
        peer_groups = [p for p in peer_tutoring if not p.tutor_student_code.startswith("Guru")]
        teacher_groups = [p for p in peer_tutoring if p.tutor_student_code.startswith("Guru")]

        strong_txt = _join_id([f"{s.kc_name} ({_pct(s.avg_mastery)})" for s in strong]) or "belum ada"
        weak_txt = _join_id([
            f"{b.kc_name} ({_pct(b.avg_mastery)}, {b.struggling_count} dari {b.student_count} siswa belum paham)"
            for b in weak
        ]) or "tidak ada"
        group_lines = [
            f"- {p.tutor_student_code} mengajari {_join_id(p.mentee_student_codes)} topik {p.kc_name}"
            for p in peer_groups
        ] + [
            f"- guru mendampingi langsung {_join_id(p.mentee_student_codes)} pada topik {p.kc_name}"
            for p in teacher_groups
        ]

        system_prompt = (
            "Kamu membantu guru SMK TKJ menulis catatan penutup sesi untuk jurnal mengajar. "
            "Tulis dalam bahasa Indonesia yang sederhana dan langsung, seperti guru berbicara kepada rekan guru. "
            "Aturan: tepat 3 paragraf pendek (maksimal 3 kalimat per paragraf), tanpa judul, tanpa poin-poin, "
            "tanpa markdown. Tulis penguasaan sebagai persen. Jangan memakai istilah 'm', 'KC', 'knowledge component', "
            "'BKT', atau angka desimal. Jangan menambah data yang tidak diberikan. "
            "Paragraf 1: kondisi kelas. Paragraf 2: topik yang sudah dikuasai dan yang perlu diulang. "
            "Paragraf 3: langkah konkret untuk pertemuan berikutnya, termasuk kelompok belajar bila ada."
        )

        user_prompt = (
            f"Sesi: {sess_title} ({class_rombel})\n"
            f"Siswa selesai: {comp_count} dari {total_students}; masih mengerjakan: {in_prog_count}\n"
            f"Jawaban benar: {_pct(accuracy_rate)} dari {total_responses} soal\n"
            f"Penguasaan rata-rata: {_pct(class_avg_m)} ({_level(class_avg_m)})\n"
            f"Topik sudah dikuasai: {strong_txt}\n"
            f"Topik perlu diulang: {weak_txt}\n"
            "Kelompok belajar:\n" + ("\n".join(group_lines) if group_lines else "- tidak diperlukan") + "\n"
            + (f"Catatan: baru {started} dari {total_students} siswa mengerjakan, sebutkan bahwa "
               "ringkasan ini belum mewakili seluruh kelas.\n" if low_coverage else "")
            + "Tulis catatannya:"
        )

        try:
            out, lat_ms, err = await self.llm_client.call_chat(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                max_tokens=320,
                timeout_seconds=5.0
            )
            if out and len(out) > 80:
                clean_out = self.llm_client.sanitize_output(out)
                return clean_out, "llm_9router"
            if err:
                logger.info(f"LLM T3 failed or timed out ({err}). Using deterministic fallback.")
        except Exception as e:
            logger.info(f"LLM T3 exception ({e}). Using deterministic fallback.")

        # Deterministic fallback: states only what the data shows.
        p1 = (
            f"Pada sesi '{sess_title}' di kelas {class_rombel}, {comp_count} dari {total_students} siswa "
            f"sudah selesai mengerjakan"
            + (f" dan {in_prog_count} masih mengerjakan" if in_prog_count else "")
            + f". Jawaban benar mencapai {_pct(accuracy_rate)} dari {total_responses} soal, "
            f"dengan penguasaan rata-rata {_pct(class_avg_m)} ({_level(class_avg_m)})."
        )
        if low_coverage:
            p1 += (
                f" Karena baru {started} siswa yang mengerjakan, ringkasan ini belum mewakili seluruh kelas."
            )

        p2_parts = []
        if strong:
            p2_parts.append(f"Topik yang sudah dikuasai: {strong_txt}.")
        if weak:
            p2_parts.append(f"Topik yang perlu diulang: {weak_txt}.")
        else:
            p2_parts.append("Tidak ada topik yang lemah pada sesi ini.")
        p2_parts.append("Persentase hanya dihitung dari topik yang benar-benar dijawab siswa.")
        p2 = " ".join(p2_parts)

        if not weak:
            p3 = "Untuk pertemuan berikutnya, kelas dapat langsung melanjutkan ke materi baru."
        else:
            p3 = f"Untuk pertemuan berikutnya, awali dengan membahas ulang {_join_id([b.kc_name for b in weak])}."
            if peer_groups:
                p3 += (
                    f" Bentuk {len(peer_groups)} kelompok belajar, yaitu siswa yang sudah paham "
                    "mengajari 1-2 teman yang belum."
                )
            if teacher_groups:
                mentees = [c for p in teacher_groups for c in p.mentee_student_codes]
                p3 += (
                    f" Dampingi langsung {_join_id(mentees)}, karena belum ada teman sekelas "
                    "yang menguasai topiknya."
                )
            p3 += " Rekomendasi ini dapat Anda sesuaikan dengan kondisi kelas."

        return f"{p1}\n\n{p2}\n\n{p3}", "deterministic_fallback"


summary_service = SummaryService()
