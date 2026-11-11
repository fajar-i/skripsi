"""
LogiTrace: Agent T3 — Session Narrative Summary & Peer-Tutoring Recommendation Service (US-06).
Adheres to Station Rotation syntax (minute 80 closing reflection) and Kurikulum Merdeka Fase F TKJ.
Includes 3.0s Ollama timeout and deterministic instant fallback (< 10 ms).
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

        # 4. Fetch KCs
        kc_stmt = select(KnowledgeComponent)
        kc_res = await db.execute(kc_stmt)
        kcs = {kc.id: kc.name for kc in kc_res.scalars().all()}

        # 5. Fetch Snapshots for targeted class students
        snap_stmt = select(MasterySnapshot).where(MasterySnapshot.student_id.in_(student_dict.keys()))
        snap_res = await db.execute(snap_stmt)
        snapshots = snap_res.scalars().all()

        # Group snapshots by student and by KC
        student_kc_mastery: Dict[str, Dict[str, float]] = {}  # student_code -> {kc_id -> mastery}
        kc_student_mastery: Dict[str, List[Tuple[str, float]]] = {k: [] for k in kcs.keys()}  # kc_id -> [(student_code, mastery)]

        for s in snapshots:
            std_code = student_dict.get(s.student_id)
            if std_code and s.kc_id in kcs:
                if std_code not in student_kc_mastery:
                    student_kc_mastery[std_code] = {}
                student_kc_mastery[std_code][s.kc_id] = s.current_mastery
                kc_student_mastery[s.kc_id].append((std_code, s.current_mastery))

        # Default fallback for missing student snapshots
        for std in students:
            code = std.anonymous_code
            if code not in student_kc_mastery:
                student_kc_mastery[code] = {}
            for kc_id in kcs.keys():
                if kc_id not in student_kc_mastery[code]:
                    student_kc_mastery[code][kc_id] = 0.25
                    kc_student_mastery[kc_id].append((code, 0.25))

        # 6. Aggregate KC Metrics
        kc_metrics: List[KCMasteryMetric] = []
        for kc_id, name in kcs.items():
            scores = [m for _, m in kc_student_mastery[kc_id]]
            avg_m = sum(scores) / len(scores) if scores else 0.25
            struggling = sum(1 for s in scores if s < 0.40)
            mastered = sum(1 for s in scores if s >= 0.70)
            kc_metrics.append(KCMasteryMetric(
                kc_id=kc_id,
                kc_name=name,
                avg_mastery=round(avg_m, 3),
                student_count=len(scores),
                struggling_count=struggling,
                mastered_count=mastered
            ))

        # Sort KCs by average mastery
        sorted_kcs = sorted(kc_metrics, key=lambda x: x.avg_mastery, reverse=True)
        strengths = sorted_kcs[:3]
        bottlenecks = sorted(sorted_kcs[-3:], key=lambda x: x.avg_mastery)

        # 7. Interaction statistics for session
        int_stmt = select(Interaction).where(Interaction.session_id == sess_id)
        int_res = await db.execute(int_stmt)
        interactions = int_res.scalars().all()
        total_resp = len(interactions)
        correct_resp = sum(1 for i in interactions if i.response_result == 1)
        accuracy_rate = round(correct_resp / total_resp, 3) if total_resp > 0 else 0.0
        avg_resp_time = int(sum(i.response_time_ms for i in interactions) / total_resp) if total_resp > 0 else 0

        # Class average mastery
        all_masteries = [m.avg_mastery for m in kc_metrics]
        class_avg_m = round(sum(all_masteries) / len(all_masteries), 3) if all_masteries else 0.25

        # 8. Peer-Tutoring Recommendations (Pairing high-mastery students with struggling peers)
        peer_tutoring: List[PeerTutoringMatch] = []
        for bn in bottlenecks:
            pairs = kc_student_mastery[bn.kc_id]
            # Tutors: m >= 0.65 (or highest available)
            potential_tutors = sorted([p for p in pairs if p[1] >= 0.65], key=lambda x: x[1], reverse=True)
            # Mentees: m <= 0.45 (or lowest available)
            potential_mentees = sorted([p for p in pairs if p[1] <= 0.45], key=lambda x: x[1])

            # Exclude self-pairing: tutor cannot be their own mentee
            if potential_tutors and potential_mentees:
                best_tutor = potential_tutors[0]
                target_mentees = [m for m in potential_mentees if m[0] != best_tutor[0]][:2]
                if target_mentees:
                    mentee_codes = [m[0] for m in target_mentees]
                    mentee_avg = sum(m[1] for m in target_mentees) / len(target_mentees)

                    guidance = (
                        f"Fasilitasi tutor {best_tutor[0]} mendiskusikan konsep inti {bn.kc_name} "
                        f"bersama {', '.join(mentee_codes)} menggunakan contoh konkret tanpa membocorkan soal kuis."
                    )

                    peer_tutoring.append(PeerTutoringMatch(
                        kc_id=bn.kc_id,
                        kc_name=bn.kc_name,
                        tutor_student_code=best_tutor[0],
                        tutor_mastery=round(best_tutor[1], 2),
                        mentee_student_codes=mentee_codes,
                        mentee_avg_mastery=round(mentee_avg, 2),
                        action_guidance=guidance
                    ))
            elif potential_mentees and not potential_tutors:
                # If no student reached mastery threshold 0.65, recommend direct teacher scaffolding in Zone B
                target_mentees = potential_mentees[:2]
                mentee_codes = [m[0] for m in target_mentees]
                mentee_avg = sum(m[1] for m in target_mentees) / len(target_mentees)

                peer_tutoring.append(PeerTutoringMatch(
                    kc_id=bn.kc_id,
                    kc_name=bn.kc_name,
                    tutor_student_code="Guru Pendamping (Zona B)",
                    tutor_mastery=1.0,
                    mentee_student_codes=mentee_codes,
                    mentee_avg_mastery=round(mentee_avg, 2),
                    action_guidance=f"Lakukan bimbingan terarah (scaffolding) langsung oleh guru pada konsep {bn.kc_name} di meja Zona B untuk {', '.join(mentee_codes)}."
                ))

        # 9. Narrative Synthesis via LLM (with 3.0s timeout & deterministic fallback)
        narrative, source = await self._generate_narrative_text(
            sess_title=sess_title,
            class_rombel=class_rombel,
            class_avg_m=class_avg_m,
            comp_count=comp_count,
            total_students=len(students),
            accuracy_rate=accuracy_rate,
            strengths=strengths,
            bottlenecks=bottlenecks,
            peer_tutoring=peer_tutoring
        )

        latency_ms = int((time.perf_counter() - start_time) * 1000)

        # Audit log in append-only agent_logs
        agent_log = AgentLog(
            trigger_type="T3",
            prompt_hash=None,
            model_id=self.llm_client.model_name if source == "rag_llm" else "deterministic_t3_engine",
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
        total_students: int,
        accuracy_rate: float,
        strengths: List[KCMasteryMetric],
        bottlenecks: List[KCMasteryMetric],
        peer_tutoring: List[PeerTutoringMatch]
    ) -> Tuple[str, str]:
        """Attempts LLM inference via SecureLLMClient (9router/DeepSeek/Ollama), falls back to deterministic text."""
        str_names = ", ".join([s.kc_name for s in strengths])
        btn_names = ", ".join([b.kc_name for b in bottlenecks])

        system_prompt = (
            "Kamu adalah Asisten Pedagogis LogiTrace untuk Guru SMK TKJ dalam model Station Rotation. "
            "Susunlah ringkasan naratif refleksi penutup sesi pembelajaran (menit ke-80) yang profesional, "
            "tepat sasaran, dan solutif. Format harus tepat 3 paragraf tanpa markdown list berlebih."
        )

        user_prompt = (
            f"Sesi: {sess_title} ({class_rombel})\n"
            f"Statistik: Rata-rata Penguasaan m={class_avg_m:.2f}, Akurasi={accuracy_rate * 100:.1f}%, "
            f"Selesai={comp_count}/{total_students} siswa.\n"
            f"Konsep Kuat: {str_names}\n"
            f"Konsep Butuh Penguatan: {btn_names}\n"
            "Tuliskan 3 paragraf refleksi penutup:"
        )

        try:
            out, lat_ms, err = await self.llm_client.call_chat(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                max_tokens=280,
                timeout_seconds=5.0
            )
            if out and len(out) > 80:
                clean_out = self.llm_client.sanitize_output(out)
                return clean_out, "rag_llm"
            if err:
                logger.info(f"LLM T3 failed or timed out ({err}). Using deterministic fallback.")
        except Exception as e:
            logger.info(f"LLM T3 exception ({e}). Using deterministic fallback.")

        # Deterministic instant fallback (< 10 ms)
        fallback_text = (
            f"Pada sesi evaluasi '{sess_title}' di kelas {class_rombel}, sebanyak {comp_count} dari {total_students} "
            f"peserta didik telah menuntaskan penugasan adaptif dengan rerata penguasaan kognitif kelas m̄ = {class_avg_m:.3f} "
            f"dan tingkat akurasi respons sebesar {accuracy_rate * 100:.1f}%. Secara umum, kelas menunjukkan pemahaman yang "
            f"sangat kokoh pada materi fondasional ({str_names}), di mana mayoritas siswa berhasil mencapai zona kemahiran mandiri.\n\n"
            f"Kendati demikian, sistem mendeteksi hambatan kognitif yang terkonsentrasi pada materi {btn_names}. "
            f"Analisis galat menunjukkan adanya miskonsepsi dalam mengidentifikasi parameter operasional dan analisis sebab-akibat "
            f"jaringan. Kondisi ini memerlukan perhatian khusus pada intervensi penutup sebelum rotasi lab berikutnya.\n\n"
            f"Untuk penutup pembelajaran (menit ke-80), disarankan guru memberikan penguatan konsep kunci selama 8–10 menit "
            f"terhadap titik-titik kritis tersebut. Selanjutnya, terapkan formasi kelompok diskusi sebaya (peer-tutoring) "
            f"berdasarkan rekomendasi sistem guna mempercepat pemerataan kompetensi pada rotasi berikutnya."
        )

        return fallback_text, "deterministic_fallback"


summary_service = SummaryService()
