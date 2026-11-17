"""
LogiTrace: DRAFT blueprint labels (kisi-kisi) for the 180-item adaptive bank.

What this script does
- Writes data/l1_knowledge_base/indikator.json (CP/TP -> 36 competency indicators, 3 per KC).
- Adds to every item in items_adaptive_180.json:
    indikator_id, bloom_level (C1-C6), tujuan_pembelajaran, label_status, catatan_telaah
  and removes the obsolete tolt_dimension field (TOLT is no longer used as an indicator).

STATUS: DRAFT. Indicators, Bloom levels and review notes were drafted with AI assistance
(Claude) from the item text, on 17 Nov 2026. They are NOT validated. Every label must be
reviewed by the researcher and content experts before use (label_status stays "draf_ai"
until changed by a reviewer).

Bloom levels follow the revised taxonomy (Anderson & Krathwohl, 2001):
C1 mengingat, C2 memahami, C3 menerapkan, C4 menganalisis, C5 mengevaluasi, C6 mencipta.
C6 is not used: multiple-choice items cannot require the learner to produce a new artefact.

Re-running is idempotent. items_adaptive_180.json is now the source of truth; the original
template generator was moved to old/data_generators/ because re-running it would drop these labels.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS_PATH = os.path.join(HERE, "items_adaptive_180.json")
INDIKATOR_PATH = os.path.join(HERE, "..", "l1_knowledge_base", "indikator.json")

CP_ELEMEN = (
    "Elemen Teknologi Jaringan Kabel dan Nirkabel, CP Fase F Konsentrasi Keahlian TKJ "
    "(Keputusan Kepala BSKAP No. 033/H/KR/2022)"
)
TP = {
    "TP 2.1": "Menerapkan instalasi jaringan kabel dan nirkabel.",
    "TP 2.2": "Menerapkan perawatan dan perbaikan jaringan kabel dan nirkabel.",
}

# KC -> (TP, [indicator 1, 2, 3])
INDIKATOR = {
    "WLAN_STANDARDS": ("TP 2.1", [
        "Mengidentifikasi standar IEEE 802.11 (b/g/n/ac/ax) beserta pita frekuensi dan kecepatan teoretisnya.",
        "Membandingkan karakteristik pita 2,4 GHz dan 5 GHz terhadap jangkauan dan kecepatan.",
        "Menjelaskan fitur peningkatan kinerja WLAN (MIMO, OFDMA, BSS Coloring, TWT, MCS, channel bonding).",
    ]),
    "WLAN_TOPOLOGY_BSS": ("TP 2.1", [
        "Mengidentifikasi mode topologi WLAN (Ad-Hoc/IBSS, BSS, ESS) dan komponennya (SSID, BSSID, DS).",
        "Menjelaskan cara kerja komponen topologi WLAN (beacon, distribution system, ESS).",
        "Menentukan topologi WLAN yang sesuai kebutuhan dan menganalisis masalah topologi.",
    ]),
    "IP_PEER_CONFIG": ("TP 2.1", [
        "Menerapkan pengalamatan IPv4 dan subnet mask pada perangkat klien.",
        "Menghitung parameter subnet (jumlah host, alamat broadcast, rentang alamat) sesuai kebutuhan jaringan.",
        "Menganalisis masalah konfigurasi IP (gateway, APIPA, konflik IP, ARP, DHCP).",
    ]),
    "WLAN_FREQ_CHANNEL": ("TP 2.1", [
        "Mengidentifikasi kanal non-overlapping dan karakteristik lebar kanal pada pita 2,4/5 GHz.",
        "Menganalisis jenis dan sumber interferensi kanal (co-channel, adjacent channel, non-802.11).",
        "Merancang alokasi kanal untuk meminimalkan interferensi antar-AP.",
    ]),
    "WLAN_SECURITY_AUTH": ("TP 2.2", [
        "Menjelaskan mekanisme dan kelemahan protokol keamanan WLAN (WEP, WPA2, WPA3).",
        "Menghitung kekuatan kata sandi terhadap serangan brute force.",
        "Menentukan konfigurasi autentikasi yang tepat untuk mencegah serangan pada WLAN.",
    ]),
    "WLAN_HOST_HARDENING": ("TP 2.2", [
        "Mengidentifikasi teknik pengamanan dasar AP dan klien (client isolation, MAC filtering, kredensial default, HTTPS).",
        "Menerapkan aturan firewall dan pembatasan akses pada router/AP.",
        "Mengevaluasi efektivitas teknik pengamanan dan segmentasi jaringan nirkabel.",
    ]),
    "WLAN_SIGNAL_PROP": ("TP 2.2", [
        "Menginterpretasikan nilai kekuatan sinyal (RSSI dalam dBm) dan pola pancaran antena.",
        "Menghitung redaman dan anggaran daya sinyal (FSPL, EIRP, SNR).",
        "Menganalisis penyebab degradasi sinyal (material penghalang, zona Fresnel, multipath, adaptasi MCS).",
    ]),
    "WLAN_ROAMING_PROB": ("TP 2.2", [
        "Menjelaskan konsep roaming, ambang roaming, dan sticky client.",
        "Menjelaskan mekanisme percepatan roaming (histeresis, IEEE 802.11k/v/r).",
        "Menentukan konfigurasi roaming untuk mengatasi masalah perpindahan klien.",
    ]),
    "WLAN_CHANNEL_COLLISION": ("TP 2.2", [
        "Menjelaskan sifat media nirkabel bersama dan mekanisme CSMA/CA.",
        "Menganalisis penyebab dan dampak tabrakan frame (hidden/exposed node, kepadatan kanal).",
        "Menentukan mekanisme mitigasi tabrakan (RTS/CTS, prioritas QoS/WMM).",
    ]),
    "ICMP_CONNECTIVITY": ("TP 2.1", [
        "Menggunakan perintah ping dan menginterpretasikan keluarannya (RTT, TTL, packet loss).",
        "Menganalisis penyebab anomali hasil uji konektivitas (jitter, TTL expired, bufferbloat).",
        "Menerapkan utilitas diagnostik (tracert, ping dengan opsi ukuran/DF) untuk pengujian konektivitas.",
    ]),
    "ICMP_TROUBLE_DHU": ("TP 2.2", [
        "Menjelaskan arti dan sumber pesan galat Destination Host Unreachable.",
        "Mendiagnosis penyebab Destination Host Unreachable dari konfigurasi IP, subnet, gateway, ARP, atau routing.",
        "Menentukan tindakan perbaikan untuk mengatasi Destination Host Unreachable.",
    ]),
    "ICMP_TROUBLE_RTO": ("TP 2.2", [
        "Menjelaskan arti pesan Request Timed Out dan membedakannya dari Destination Host Unreachable.",
        "Mendiagnosis penyebab Request Timed Out (firewall, sinyal lemah, kabel, routing asimetris, MTU).",
        "Menentukan tindakan perbaikan dan verifikasi untuk mengatasi Request Timed Out.",
    ]),
}

KC_CODE = {
    "WLAN_STANDARDS": "01", "WLAN_TOPOLOGY_BSS": "02", "IP_PEER_CONFIG": "03",
    "WLAN_FREQ_CHANNEL": "04", "WLAN_SECURITY_AUTH": "05", "WLAN_HOST_HARDENING": "06",
    "WLAN_SIGNAL_PROP": "07", "WLAN_ROAMING_PROB": "08", "WLAN_CHANNEL_COLLISION": "09",
    "ICMP_CONNECTIVITY": "10", "ICMP_TROUBLE_DHU": "11", "ICMP_TROUBLE_RTO": "12",
}

# Review notes (catatan_telaah) — codes:
CAKUPAN = "Materi kemungkinan di luar cakupan Fase F SMK; perlu ditelaah pakar."
FASE = "Soal bersifat hafalan/pemahaman; kesesuaian fase Jonassen perlu ditelaah."
KC = "Isi soal lebih dekat ke KC lain; kesesuaian KC perlu ditelaah."

# item id suffix -> (indicator number 1..3, bloom level, [notes])
LABELS = {
    # KC-01 WLAN_STANDARDS
    "WLAN_STANDARDS_1_01": (1, "C1", [FASE]), "WLAN_STANDARDS_1_02": (1, "C1", []),
    "WLAN_STANDARDS_1_03": (2, "C2", [FASE]), "WLAN_STANDARDS_1_04": (1, "C1", []),
    "WLAN_STANDARDS_1_05": (1, "C1", [FASE]), "WLAN_STANDARDS_2_01": (2, "C4", []),
    "WLAN_STANDARDS_2_02": (3, "C2", [FASE]), "WLAN_STANDARDS_2_03": (3, "C3", []),
    "WLAN_STANDARDS_2_04": (3, "C2", []), "WLAN_STANDARDS_2_05": (3, "C2", []),
    "WLAN_STANDARDS_3_01": (3, "C3", [CAKUPAN]), "WLAN_STANDARDS_3_02": (3, "C5", []),
    "WLAN_STANDARDS_3_03": (3, "C4", []), "WLAN_STANDARDS_3_04": (3, "C2", []),
    "WLAN_STANDARDS_3_05": (3, "C5", []),
    # KC-02 WLAN_TOPOLOGY_BSS
    "WLAN_TOPOLOGY_BSS_1_01": (1, "C1", []), "WLAN_TOPOLOGY_BSS_1_02": (1, "C1", []),
    "WLAN_TOPOLOGY_BSS_1_03": (1, "C1", [FASE]), "WLAN_TOPOLOGY_BSS_1_04": (1, "C1", []),
    "WLAN_TOPOLOGY_BSS_1_05": (1, "C1", []), "WLAN_TOPOLOGY_BSS_2_01": (2, "C2", []),
    "WLAN_TOPOLOGY_BSS_2_02": (3, "C4", []), "WLAN_TOPOLOGY_BSS_2_03": (1, "C1", [FASE]),
    "WLAN_TOPOLOGY_BSS_2_04": (3, "C3", []), "WLAN_TOPOLOGY_BSS_2_05": (2, "C2", []),
    "WLAN_TOPOLOGY_BSS_3_01": (3, "C5", []), "WLAN_TOPOLOGY_BSS_3_02": (3, "C4", []),
    "WLAN_TOPOLOGY_BSS_3_03": (2, "C2", [KC]), "WLAN_TOPOLOGY_BSS_3_04": (3, "C4", []),
    "WLAN_TOPOLOGY_BSS_3_05": (3, "C5", [CAKUPAN]),
    # KC-03 IP_PEER_CONFIG
    "IP_PEER_CONFIG_1_01": (1, "C3", []), "IP_PEER_CONFIG_1_02": (1, "C3", []),
    "IP_PEER_CONFIG_1_03": (3, "C1", []), "IP_PEER_CONFIG_1_04": (2, "C3", []),
    "IP_PEER_CONFIG_1_05": (3, "C2", []), "IP_PEER_CONFIG_2_01": (2, "C3", []),
    "IP_PEER_CONFIG_2_02": (3, "C4", []), "IP_PEER_CONFIG_2_03": (3, "C2", []),
    "IP_PEER_CONFIG_2_04": (2, "C3", []), "IP_PEER_CONFIG_2_05": (3, "C2", []),
    "IP_PEER_CONFIG_3_01": (2, "C3", []), "IP_PEER_CONFIG_3_02": (3, "C2", [KC]),
    "IP_PEER_CONFIG_3_03": (3, "C4", []), "IP_PEER_CONFIG_3_04": (3, "C5", []),
    "IP_PEER_CONFIG_3_05": (2, "C3", []),
    # KC-04 WLAN_FREQ_CHANNEL
    "WLAN_FREQ_CHANNEL_1_01": (1, "C1", [FASE]), "WLAN_FREQ_CHANNEL_1_02": (1, "C1", []),
    "WLAN_FREQ_CHANNEL_1_03": (1, "C2", []), "WLAN_FREQ_CHANNEL_1_04": (1, "C2", []),
    "WLAN_FREQ_CHANNEL_1_05": (2, "C2", []), "WLAN_FREQ_CHANNEL_2_01": (2, "C2", []),
    "WLAN_FREQ_CHANNEL_2_02": (3, "C3", []), "WLAN_FREQ_CHANNEL_2_03": (1, "C4", []),
    "WLAN_FREQ_CHANNEL_2_04": (1, "C2", []), "WLAN_FREQ_CHANNEL_2_05": (2, "C2", []),
    "WLAN_FREQ_CHANNEL_3_01": (3, "C5", []), "WLAN_FREQ_CHANNEL_3_02": (2, "C3", []),
    "WLAN_FREQ_CHANNEL_3_03": (2, "C4", []), "WLAN_FREQ_CHANNEL_3_04": (2, "C4", []),
    "WLAN_FREQ_CHANNEL_3_05": (2, "C2", [KC]),
    # KC-05 WLAN_SECURITY_AUTH
    "WLAN_SECURITY_AUTH_1_01": (1, "C2", []), "WLAN_SECURITY_AUTH_1_02": (1, "C2", [FASE]),
    "WLAN_SECURITY_AUTH_1_03": (2, "C1", [FASE]), "WLAN_SECURITY_AUTH_1_04": (1, "C1", []),
    "WLAN_SECURITY_AUTH_1_05": (2, "C3", []), "WLAN_SECURITY_AUTH_2_01": (1, "C2", []),
    "WLAN_SECURITY_AUTH_2_02": (1, "C2", []), "WLAN_SECURITY_AUTH_2_03": (3, "C3", []),
    "WLAN_SECURITY_AUTH_2_04": (2, "C3", []), "WLAN_SECURITY_AUTH_2_05": (3, "C4", []),
    "WLAN_SECURITY_AUTH_3_01": (3, "C5", []), "WLAN_SECURITY_AUTH_3_02": (2, "C3", []),
    "WLAN_SECURITY_AUTH_3_03": (3, "C2", []), "WLAN_SECURITY_AUTH_3_04": (1, "C2", []),
    "WLAN_SECURITY_AUTH_3_05": (3, "C4", []),
    # KC-06 WLAN_HOST_HARDENING
    "WLAN_HOST_HARDENING_1_01": (1, "C1", []), "WLAN_HOST_HARDENING_1_02": (1, "C1", []),
    "WLAN_HOST_HARDENING_1_03": (1, "C1", [FASE]), "WLAN_HOST_HARDENING_1_04": (1, "C1", []),
    "WLAN_HOST_HARDENING_1_05": (3, "C4", []), "WLAN_HOST_HARDENING_2_01": (3, "C4", []),
    "WLAN_HOST_HARDENING_2_02": (2, "C3", []), "WLAN_HOST_HARDENING_2_03": (2, "C3", [KC]),
    "WLAN_HOST_HARDENING_2_04": (1, "C2", []), "WLAN_HOST_HARDENING_2_05": (3, "C4", []),
    "WLAN_HOST_HARDENING_3_01": (3, "C5", []), "WLAN_HOST_HARDENING_3_02": (2, "C4", []),
    "WLAN_HOST_HARDENING_3_03": (3, "C2", [CAKUPAN]), "WLAN_HOST_HARDENING_3_04": (2, "C3", [KC]),
    "WLAN_HOST_HARDENING_3_05": (3, "C5", [CAKUPAN]),
    # KC-07 WLAN_SIGNAL_PROP
    "WLAN_SIGNAL_PROP_1_01": (1, "C1", []), "WLAN_SIGNAL_PROP_1_02": (1, "C2", []),
    "WLAN_SIGNAL_PROP_1_03": (1, "C1", []), "WLAN_SIGNAL_PROP_1_04": (3, "C2", [FASE]),
    "WLAN_SIGNAL_PROP_1_05": (1, "C2", []), "WLAN_SIGNAL_PROP_2_01": (2, "C3", []),
    "WLAN_SIGNAL_PROP_2_02": (3, "C2", []), "WLAN_SIGNAL_PROP_2_03": (3, "C4", []),
    "WLAN_SIGNAL_PROP_2_04": (2, "C3", []), "WLAN_SIGNAL_PROP_2_05": (3, "C4", []),
    "WLAN_SIGNAL_PROP_3_01": (2, "C3", []), "WLAN_SIGNAL_PROP_3_02": (3, "C4", []),
    "WLAN_SIGNAL_PROP_3_03": (3, "C4", []), "WLAN_SIGNAL_PROP_3_04": (2, "C4", []),
    "WLAN_SIGNAL_PROP_3_05": (3, "C2", [CAKUPAN]),
    # KC-08 WLAN_ROAMING_PROB
    "WLAN_ROAMING_PROB_1_01": (1, "C1", []), "WLAN_ROAMING_PROB_1_02": (1, "C2", []),
    "WLAN_ROAMING_PROB_1_03": (3, "C3", []), "WLAN_ROAMING_PROB_1_04": (1, "C2", []),
    "WLAN_ROAMING_PROB_1_05": (1, "C1", [FASE]), "WLAN_ROAMING_PROB_2_01": (2, "C2", []),
    "WLAN_ROAMING_PROB_2_02": (2, "C2", []), "WLAN_ROAMING_PROB_2_03": (3, "C1", []),
    "WLAN_ROAMING_PROB_2_04": (1, "C4", []), "WLAN_ROAMING_PROB_2_05": (2, "C2", []),
    "WLAN_ROAMING_PROB_3_01": (3, "C5", []), "WLAN_ROAMING_PROB_3_02": (2, "C4", []),
    "WLAN_ROAMING_PROB_3_03": (2, "C1", [FASE]), "WLAN_ROAMING_PROB_3_04": (1, "C4", []),
    "WLAN_ROAMING_PROB_3_05": (3, "C5", [CAKUPAN]),
    # KC-09 WLAN_CHANNEL_COLLISION
    "WLAN_CHANNEL_COLLISION_1_01": (1, "C1", []), "WLAN_CHANNEL_COLLISION_1_02": (1, "C1", []),
    "WLAN_CHANNEL_COLLISION_1_03": (1, "C2", []), "WLAN_CHANNEL_COLLISION_1_04": (2, "C2", []),
    "WLAN_CHANNEL_COLLISION_1_05": (1, "C2", []), "WLAN_CHANNEL_COLLISION_2_01": (1, "C2", []),
    "WLAN_CHANNEL_COLLISION_2_02": (2, "C2", []), "WLAN_CHANNEL_COLLISION_2_03": (3, "C2", [FASE]),
    "WLAN_CHANNEL_COLLISION_2_04": (2, "C4", []), "WLAN_CHANNEL_COLLISION_2_05": (2, "C4", []),
    "WLAN_CHANNEL_COLLISION_3_01": (3, "C4", []), "WLAN_CHANNEL_COLLISION_3_02": (2, "C2", [CAKUPAN]),
    "WLAN_CHANNEL_COLLISION_3_03": (3, "C4", []), "WLAN_CHANNEL_COLLISION_3_04": (2, "C2", [FASE]),
    "WLAN_CHANNEL_COLLISION_3_05": (3, "C2", []),
    # KC-10 ICMP_CONNECTIVITY
    "ICMP_CONNECTIVITY_1_01": (1, "C1", []), "ICMP_CONNECTIVITY_1_02": (1, "C1", [FASE]),
    "ICMP_CONNECTIVITY_1_03": (1, "C2", []), "ICMP_CONNECTIVITY_1_04": (1, "C2", []),
    "ICMP_CONNECTIVITY_1_05": (1, "C2", []), "ICMP_CONNECTIVITY_2_01": (2, "C4", []),
    "ICMP_CONNECTIVITY_2_02": (2, "C4", []), "ICMP_CONNECTIVITY_2_03": (3, "C3", []),
    "ICMP_CONNECTIVITY_2_04": (1, "C2", [FASE]), "ICMP_CONNECTIVITY_2_05": (2, "C4", []),
    "ICMP_CONNECTIVITY_3_01": (3, "C2", [FASE]), "ICMP_CONNECTIVITY_3_02": (2, "C4", []),
    "ICMP_CONNECTIVITY_3_03": (3, "C4", []), "ICMP_CONNECTIVITY_3_04": (3, "C3", []),
    "ICMP_CONNECTIVITY_3_05": (2, "C4", [CAKUPAN]),
    # KC-11 ICMP_TROUBLE_DHU
    "ICMP_TROUBLE_DHU_1_01": (1, "C2", []), "ICMP_TROUBLE_DHU_1_02": (1, "C1", []),
    "ICMP_TROUBLE_DHU_1_03": (2, "C4", []), "ICMP_TROUBLE_DHU_1_04": (1, "C1", [KC]),
    "ICMP_TROUBLE_DHU_1_05": (1, "C2", []), "ICMP_TROUBLE_DHU_2_01": (2, "C4", []),
    "ICMP_TROUBLE_DHU_2_02": (2, "C4", []), "ICMP_TROUBLE_DHU_2_03": (2, "C4", []),
    "ICMP_TROUBLE_DHU_2_04": (2, "C4", []), "ICMP_TROUBLE_DHU_2_05": (2, "C4", []),
    "ICMP_TROUBLE_DHU_3_01": (2, "C4", []), "ICMP_TROUBLE_DHU_3_02": (2, "C4", [CAKUPAN]),
    "ICMP_TROUBLE_DHU_3_03": (3, "C3", [CAKUPAN]), "ICMP_TROUBLE_DHU_3_04": (2, "C4", []),
    "ICMP_TROUBLE_DHU_3_05": (2, "C4", [CAKUPAN]),
    # KC-12 ICMP_TROUBLE_RTO
    "ICMP_TROUBLE_RTO_1_01": (1, "C2", []), "ICMP_TROUBLE_RTO_1_02": (2, "C4", []),
    "ICMP_TROUBLE_RTO_1_03": (1, "C2", [FASE]), "ICMP_TROUBLE_RTO_1_04": (2, "C4", []),
    "ICMP_TROUBLE_RTO_1_05": (2, "C4", []), "ICMP_TROUBLE_RTO_2_01": (2, "C4", []),
    "ICMP_TROUBLE_RTO_2_02": (2, "C2", []), "ICMP_TROUBLE_RTO_2_03": (2, "C4", []),
    "ICMP_TROUBLE_RTO_2_04": (2, "C4", []), "ICMP_TROUBLE_RTO_2_05": (3, "C3", []),
    "ICMP_TROUBLE_RTO_3_01": (2, "C4", []), "ICMP_TROUBLE_RTO_3_02": (2, "C4", []),
    "ICMP_TROUBLE_RTO_3_03": (2, "C4", []), "ICMP_TROUBLE_RTO_3_04": (2, "C4", []),
    "ICMP_TROUBLE_RTO_3_05": (2, "C4", [CAKUPAN]),
}


def indikator_id(kc: str, n: int) -> str:
    return f"IND-{KC_CODE[kc]}.{n}"


def build_indikator_doc():
    return {
        "status": "draf_ai — belum divalidasi pakar",
        "capaian_pembelajaran": CP_ELEMEN,
        "tujuan_pembelajaran": TP,
        "level_kognitif": {
            "C1": "Mengingat", "C2": "Memahami", "C3": "Menerapkan",
            "C4": "Menganalisis", "C5": "Mengevaluasi", "C6": "Mencipta",
        },
        "indikator": [
            {"id": indikator_id(kc, i + 1), "kc_id": kc, "tujuan_pembelajaran": tp, "rumusan": text}
            for kc, (tp, texts) in INDIKATOR.items()
            for i, text in enumerate(texts)
        ],
    }


def main():
    with open(ITEMS_PATH, encoding="utf-8") as f:
        items = json.load(f)

    missing = [it["id"] for it in items if it["id"].replace("ITEM_", "") not in LABELS]
    if missing:
        raise SystemExit(f"No draft label for: {missing}")

    for it in items:
        n, bloom, notes = LABELS[it["id"].replace("ITEM_", "")]
        kc = it["primary_kc"]
        it.pop("tolt_dimension", None)
        it["tujuan_pembelajaran"] = INDIKATOR[kc][0]
        it["indikator_id"] = indikator_id(kc, n)
        it["bloom_level"] = bloom
        it.setdefault("label_status", "draf_ai")
        it["catatan_telaah"] = notes

    with open(ITEMS_PATH, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
        f.write("\n")
    with open(INDIKATOR_PATH, "w", encoding="utf-8") as f:
        json.dump(build_indikator_doc(), f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Labelled {len(items)} items; wrote {os.path.relpath(INDIKATOR_PATH, HERE)}")


if __name__ == "__main__":
    main()
