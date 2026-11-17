"""
LogiTrace: T1 — Rule-based item labeling for teacher review (US-05).

Keyword-matching classifier (no LLM call). Suggests primary KC, secondary KCs,
TOLT dimension, nominal difficulty (1-3) and a heuristic confidence score.
Items with confidence < 0.60 are flagged for mandatory teacher review.
"""

from datetime import datetime, timezone
import json
import logging
import os
import re
import time
from typing import Dict, List, Optional, Tuple
import httpx
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.models import AgentLog
from ..schemas.labeling import ItemLabelRequest, ItemLabelResult

logger = logging.getLogger("labeling_service")

# 12 KCs and their semantic keyword triggers
KC_KEYWORDS = {
    "WLAN_STANDARDS": ["802.11", "standar", "throughput", "mimo", "wifi 4", "wifi 5", "wifi 6", "frekuensi nominal", "kecepatan transfer"],
    "WLAN_TOPOLOGY_BSS": ["topologi", "ad-hoc", "bss", "infrastructure", "access point", "ibss", "distribution system", "client mode"],
    "IP_PEER_CONFIG": ["ip address", "ipv4", "subnet", "cidr", "mask", "gateway", "pengalamatan", "oktet", "host id", "network id"],
    "WLAN_FREQ_CHANNEL": ["kanal", "channel", "overlapping", "2.4 ghz", "5 ghz", "interferensi kanal", "kanal 1", "kanal 6", "kanal 11", "lebar pita"],
    "WLAN_SECURITY_AUTH": ["keamanan", "wpa", "wpa2", "wpa3", "psk", "sae", "enkripsi", "autentikasi", "handshake", "brute force"],
    "WLAN_HOST_HARDENING": ["mac filtering", "firewall", "hardening", "isolasi", "hidden ssid", "keamanan host", "akses kontrol", "port filtering"],
    "WLAN_SIGNAL_PROP": ["dbm", "rssi", "redaman", "path loss", "propagasi", "atenuasi", "daya pancar", "sinyal", "obstakel", "jarak"],
    "WLAN_ROAMING_PROB": ["roaming", "histeresis", "reassociation", "threshold roaming", "fast transition", "pindah ap", "cakupan"],
    "WLAN_CHANNEL_COLLISION": ["collision", "csma/ca", "kepadatan", "utilisasi kanal", "congestion", "airtime", "backoff"],
    "ICMP_CONNECTIVITY": ["icmp", "ping", "rtt", "latency", "echo request", "echo reply", "konektivitas", "delay"],
    "ICMP_TROUBLE_DHU": ["destination host unreachable", "dhu", "unreachable", "gateway salah", "kabel putus", "rute hilang"],
    "ICMP_TROUBLE_RTO": ["request timed out", "rto", "timeout", "drop paket", "firewall drop", "intermiten", "sinyal lemah"]
}

KC_NAMES = {
    "WLAN_STANDARDS": "Standar Jaringan Nirkabel 802.11",
    "WLAN_TOPOLOGY_BSS": "Topologi Jaringan WLAN (Ad-Hoc & BSS)",
    "IP_PEER_CONFIG": "Pengalamatan IPv4 & Subnetting Peer",
    "WLAN_FREQ_CHANNEL": "Alokasi Frekuensi & Kanal Non-Overlapping",
    "WLAN_SECURITY_AUTH": "Keamanan & Autentikasi WLAN (WPA2/WPA3)",
    "WLAN_HOST_HARDENING": "Penyederhanaan & Hardening Host Jaringan",
    "WLAN_SIGNAL_PROP": "Propagasi Sinyal & Redaman RSSI",
    "WLAN_ROAMING_PROB": "Transisi & Roaming Klien Nirkabel",
    "WLAN_CHANNEL_COLLISION": "Kepadatan & Tabrakan Kanal (Collision)",
    "ICMP_CONNECTIVITY": "Pengujian Konektivitas Dasar ICMP",
    "ICMP_TROUBLE_DHU": "Diagnosa Galat Destination Host Unreachable",
    "ICMP_TROUBLE_RTO": "Diagnosa Galat Request Timed Out"
}

# TOLT Dimensions and keyword markers
TOLT_KEYWORDS = {
    "Controlling Variables": ["variabel", "kontrol", "tetap", "diubah", "membandingkan", "faktor", "hanya satu"],
    "Proportional Reasoning": ["perbandingan", "proporsional", "rasio", "dbm", "jarak", "dua kali lipat", "setengah"],
    "Probabilistic Reasoning": ["probabilitas", "peluang", "kemungkinan", "acak", "fluktuasi", "collision rate"],
    "Correlational Reasoning": ["korelasi", "hubungan", "semakin", "mempengaruhi", "akibat", "sebab"],
    "Combinatorial Reasoning": ["kombinasi", "alternatif", "susunan", "konfigurasi yang mungkin", "pasangan"]
}


class LabelingService:
    """Rule-based keyword labeler (T1). Deterministic; does not call an LLM."""

    async def label_item(
        self,
        req: ItemLabelRequest,
        db: Optional[AsyncSession] = None
    ) -> ItemLabelResult:
        start_time = time.perf_counter()

        full_text = f"{req.prompt_text} {' '.join(req.options.values())} {req.explanation or ''}".lower()

        # Step 1: Lexical & Semantic score for each KC
        scores: Dict[str, float] = {}
        for kc_id, keywords in KC_KEYWORDS.items():
            score = 0.0
            for kw in keywords:
                if re.search(r'\b' + re.escape(kw) + r'\b', full_text, re.IGNORECASE):
                    score += 1.5
                elif kw in full_text:
                    score += 0.8
            scores[kc_id] = score

        # Sort KCs by score
        ranked_kcs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top_kc, top_score = ranked_kcs[0]
        second_kcs = [kc for kc, s in ranked_kcs[1:3] if s > 0.8]

        # Step 2: Classify TOLT dimension
        tolt_scores: Dict[str, float] = {}
        for dim, kw_list in TOLT_KEYWORDS.items():
            t_score = sum(1.0 for kw in kw_list if kw in full_text)
            tolt_scores[dim] = t_score

        best_tolt = max(tolt_scores.items(), key=lambda x: x[1])
        predicted_tolt = best_tolt[0] if best_tolt[1] > 0 else "Correlational Reasoning"

        # Step 3: Classify nominal difficulty (1, 2, or 3)
        # 1: Identify, state, what is (factual/C1-C2)
        # 2: Calculate, configure, compare (application/C3)
        # 3: Diagnose, troubleshoot, evaluate (analysis/C4-C5)
        diff = 2
        diff_3_words = ["analisis", "analisa", "diagnosa", "troubleshoot", "mengapa", "investigasi", "penyebab utama", "kerusakan"]
        diff_1_words = ["apa itu", "sebutkan", "manakah standar", "definisi", "pengertian", "singkatan"]

        if any(w in full_text for w in diff_3_words):
            diff = 3
        elif any(w in full_text for w in diff_1_words):
            diff = 1

        # Step 4: Calculate confidence
        # Confidence is high if top_score is distinctly higher than second best, or above threshold
        second_score = ranked_kcs[1][1] if len(ranked_kcs) > 1 else 0.0
        if top_score >= 3.0 and (top_score - second_score >= 1.0):
            confidence = min(0.95, 0.70 + (top_score * 0.05))
            rationale = (
                f"Terdeteksi kata kunci kuat untuk materi '{KC_NAMES.get(top_kc, top_kc)}' "
                f"dengan pola penalaran {predicted_tolt} (Skor kecocokan: {top_score:.1f})."
            )
        elif top_score >= 1.5:
            confidence = min(0.75, 0.55 + (top_score * 0.05))
            rationale = (
                f"Terdeteksi kata kunci moderat untuk materi '{KC_NAMES.get(top_kc, top_kc)}' "
                f"dengan pola penalaran {predicted_tolt} (Skor kecocokan: {top_score:.1f})."
            )
        elif top_score > 0.0:
            confidence = 0.45
            rationale = (
                f"Kecocokan kata kunci rendah untuk '{KC_NAMES.get(top_kc, top_kc)}' "
                f"(Skor: {top_score:.1f}). Keyakinan < 0.60; membutuhkan verifikasi manual oleh guru."
            )
        else:
            confidence = 0.20
            rationale = (
                "Tidak terdeteksi kata kunci spesifik untuk 12 KC kejuruan (Skor kecocokan: 0.0). "
                "Butir otomatis dialihkan ke antrean tinjauan guru."
            )

        needs_review = confidence < 0.60
        if needs_review and top_score > 0.0 and "verifikasi manual" not in rationale:
            rationale += " Tingkat keyakinan < 0.60; membutuhkan verifikasi manual oleh guru."

        latency_ms = int((time.perf_counter() - start_time) * 1000)

        # Audit log in AgentLog if db provided
        if db:
            agent_log = AgentLog(
                trigger_type="T1",
                prompt_hash=None,
                model_id="semantic_classifier_t1",
                raw_output=json.dumps({
                    "primary_kc": top_kc,
                    "tolt": predicted_tolt,
                    "difficulty": diff,
                    "confidence": confidence
                }),
                is_accepted=not needs_review,
                rejection_reason="Confidence < 0.60 (Pending Teacher Review)" if needs_review else None,
                latency_ms=latency_ms
            )
            db.add(agent_log)
            await db.commit()

        return ItemLabelResult(
            primary_kc_id=top_kc,
            primary_kc_name=KC_NAMES.get(top_kc, top_kc),
            secondary_kc_ids=second_kcs,
            tolt_dimension=predicted_tolt,
            nominal_difficulty=diff,
            confidence=round(confidence, 2),
            needs_teacher_review=needs_review,
            rationale=rationale,
            source="semantic_classifier",
            latency_ms=latency_ms
        )


labeling_service = LabelingService()
