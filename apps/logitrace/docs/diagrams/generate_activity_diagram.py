"""
Script to generate the Station Rotation Activity Diagram for LogiTrace RAG-KT
in draw.io XML format, compliant with drawio-skill specifications.
"""

import xml.sax.saxutils as saxutils

def generate_drawio_xml():
    # Widths and positions
    LANE_SISWA_X = 40
    LANE_GURU_X = 500
    LANE_SYS_X = 960
    LANE_WIDTH = 440
    TOTAL_WIDTH = 1440
    TOTAL_HEIGHT = 3520

    # Colors
    C_SISWA_FILL = "#dae8fc"
    C_SISWA_STROKE = "#6c8ebf"
    C_GURU_FILL = "#fff2cc"
    C_GURU_STROKE = "#d6b656"
    C_SYS_FILL = "#e1d5e7"
    C_SYS_STROKE = "#9673a6"
    C_DECISION_FILL = "#ffe6cc"
    C_DECISION_STROKE = "#d79b00"
    C_ALERT_FILL = "#ffcdd2"
    C_ALERT_STROKE = "#e53935"
    C_START_FILL = "#d5e8d4"
    C_START_STROKE = "#82b366"
    C_END_FILL = "#f8cecc"
    C_END_STROKE = "#b85450"

    cells = []
    cell_id = 2

    def add_cell(tag, **attrs):
        nonlocal cell_id
        cid = str(cell_id)
        cell_id += 1
        return cid, attrs

    # Root elements
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<mxfile host="drawio" version="26.0.0">',
        '  <diagram name="Activity-Station-Rotation">',
        f'    <mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{TOTAL_WIDTH}" pageHeight="{TOTAL_HEIGHT}" math="0" shadow="0">',
        '      <root>',
        '        <mxCell id="0" />',
        '        <mxCell id="1" parent="0" />',
    ]

    # Helper functions
    def node(nid, label, style, x, y, w, h, parent="1"):
        val = saxutils.escape(label).replace("\n", "&#xa;")
        return f'        <mxCell id="{nid}" value="{val}" style="{style}" vertex="1" parent="{parent}">\n          <mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry" />\n        </mxCell>'

    def edge(eid, label, src, tgt, style_extra="", points=None):
        val = saxutils.escape(label).replace("\n", "&#xa;")
        st = f"edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;fontSize=10;{style_extra}"
        res = f'        <mxCell id="{eid}" value="{val}" style="{st}" edge="1" parent="1" source="{src}" target="{tgt}">\n          <mxGeometry relative="1" as="geometry">'
        if points:
            res += '\n            <Array as="points">'
            for px, py in points:
                res += f'\n              <mxPoint x="{px}" y="{py}" />'
            res += '\n            </Array>'
        res += '\n          </mxGeometry>\n        </mxCell>'
        return res

    def phase_banner(pid, title, y_pos):
        st = "rounded=0;whiteSpace=wrap;html=1;fillColor=#37474f;strokeColor=none;fontColor=#ffffff;fontStyle=1;fontSize=12;align=left;spacingLeft=15;"
        return node(pid, title, st, LANE_SISWA_X, y_pos, LANE_WIDTH * 3 + 40, 30)

    # 1. Swimlane headers
    lane_style_siswa = f"swimlane;startSize=40;fillColor=#e1f5fe;strokeColor=#0288d1;fontStyle=1;fontSize=13;fontColor=#01579b;align=center;horizontal=1;collapsible=0;pointerEvents=0;"
    lane_style_guru = f"swimlane;startSize=40;fillColor=#fff8e1;strokeColor=#ffa000;fontStyle=1;fontSize=13;fontColor=#ff6f00;align=center;horizontal=1;collapsible=0;pointerEvents=0;"
    lane_style_sys = f"swimlane;startSize=40;fillColor=#f3e5f5;strokeColor=#8e24aa;fontStyle=1;fontSize=13;fontColor=#4a148c;align=center;horizontal=1;collapsible=0;pointerEvents=0;"

    xml_lines.append(node("lane_siswa", "Siswa (Kelompok A & Kelompok B / 34 Siswa)", lane_style_siswa, LANE_SISWA_X, 40, LANE_WIDTH, TOTAL_HEIGHT - 60))
    xml_lines.append(node("lane_guru", "Guru Pengampu (Roving Teacher / Fasilitator)", lane_style_guru, LANE_GURU_X, 40, LANE_WIDTH, TOTAL_HEIGHT - 60))
    xml_lines.append(node("lane_sys", "Sistem LogiTrace (Mesin L3 & RAG Orchestrator)", lane_style_sys, LANE_SYS_X, 40, LANE_WIDTH, TOTAL_HEIGHT - 60))

    # STYLES
    ST_SISWA = f"rounded=1;whiteSpace=wrap;html=1;fillColor={C_SISWA_FILL};strokeColor={C_SISWA_STROKE};fontSize=11;"
    ST_GURU = f"rounded=1;whiteSpace=wrap;html=1;fillColor={C_GURU_FILL};strokeColor={C_GURU_STROKE};fontSize=11;"
    ST_SYS = f"rounded=1;whiteSpace=wrap;html=1;fillColor={C_SYS_FILL};strokeColor={C_SYS_STROKE};fontSize=11;"
    ST_DEC = f"rhombus;whiteSpace=wrap;html=1;fillColor={C_DECISION_FILL};strokeColor={C_DECISION_STROKE};fontSize=10;"
    ST_ALERT = f"rounded=1;whiteSpace=wrap;html=1;fillColor={C_ALERT_FILL};strokeColor={C_ALERT_STROKE};fontSize=10;fontColor=#b71c1c;"
    ST_START = f"ellipse;whiteSpace=wrap;html=1;fillColor={C_START_FILL};strokeColor={C_START_STROKE};fontStyle=1;fontSize=12;"
    ST_END = f"ellipse;shape=doubleEllipse;whiteSpace=wrap;html=1;fillColor={C_END_FILL};strokeColor={C_END_STROKE};fontStyle=1;fontSize=12;"

    # -------------------------------------------------------------
    # FASE 1: PEMBUKAAN & PEMBAGIAN ZONA (00:00 - 05:00)
    # -------------------------------------------------------------
    xml_lines.append(phase_banner("b1", "FASE 1: PEMBUKAAN, APERSEPSI & PEMBAGIAN ZONA (00:00 - 05:00 WIB / 5 Menit)", 90))

    xml_lines.append(node("act_start", "Mulai Pembelajaran\n(TP 2.1 & TP 2.2)", ST_START, LANE_GURU_X + 130, 130, 160, 40))
    xml_lines.append(node("act_g_open", "Membuka kelas, salam, apersepsi,\ndan menjelaskan skenario Station Rotation", ST_GURU, LANE_GURU_X + 90, 190, 240, 50))
    xml_lines.append(node("act_g_split", "Membagi rombel XI TKJ 1 (34 siswa):\n- Kelompok A (17 siswa) -> Zona A\n- Kelompok B (17 siswa) -> Zona B", ST_GURU, LANE_GURU_X + 90, 260, 240, 50))
    xml_lines.append(node("act_s_prep", "Mendengarkan pengarahan dan\nbergerak menuju zona yang ditentukan", ST_SISWA, LANE_SISWA_X + 90, 260, 240, 50))

    # -------------------------------------------------------------
    # FASE 2: SIKLUS ROTASI 1 (05:00 - 40:00 / 35 Menit)
    # -------------------------------------------------------------
    xml_lines.append(phase_banner("b2", "FASE 2: SIKLUS ROTASI 1 (05:00 - 40:00 WIB / 35 Menit) — KEL. A (ZONA A) & KEL. B (ZONA B)", 330))

    # Zona A (Praktik Lab)
    xml_lines.append(node("act_s_zona_a1", "KELOMPOK A (Zona A - Lab PC 1:1):\nMenjalankan Jobsheet Praktik Konfigurasi\nJaringan Kabel & Nirkabel (MikroTik/Cisco)", ST_SISWA, LANE_SISWA_X + 20, 380, 200, 70))
    
    # Zona B (Evaluasi Adaptif Mandiri)
    xml_lines.append(node("act_s_zona_b1", "KELOMPOK B (Zona B - Meja Kuis):\nBuka Smartphone, akses LogiTrace Web,\ndan lakukan login akun siswa", ST_SISWA, LANE_SISWA_X + 230, 380, 190, 70))
    xml_lines.append(node("act_sys_auth", "Autentikasi akun, muat state kognitif:\nm_{s,k} = 0.25 (baseline 12 KCs)", ST_SYS, LANE_SYS_X + 90, 380, 240, 50))

    # Sub-fase Cold Start (Butir 1-6)
    xml_lines.append(node("act_sys_coldstart", "Sajikan 6 Butir Kalibrasi Acak Seimbang\n(d1, d2, d3 across KCs)\nFlag: is_calibration = TRUE", ST_SYS, LANE_SYS_X + 90, 460, 240, 60))
    xml_lines.append(node("act_s_coldstart", "Siswa mengerjakan 6 butir kalibrasi\ntanpa bantuan petunjuk (cold-start baseline)", ST_SISWA, LANE_SISWA_X + 230, 460, 190, 60))
    xml_lines.append(node("act_sys_eval_cold", "Evaluasi respon r in {0,1},\nkalkulasi m awal tiap KC,\ninsert append-only interactions", ST_SYS, LANE_SYS_X + 90, 550, 240, 60))

    # Sub-fase ZPD Adaptive Engine (Butir 7-20)
    xml_lines.append(node("act_sys_calc_zpd", "Hitung estimasi probabilitas sukses:\np_hat(q) = sigmoid(logit(m) + theta_d)\nFilter kandidat butir: p_hat in [0.60, 0.85]\nPrioritaskan KC terendah", ST_SYS, LANE_SYS_X + 90, 640, 250, 70))
    xml_lines.append(node("act_sys_serve_zpd", "Kirim butir adaptif terpilih ke client smartphone siswa", ST_SYS, LANE_SYS_X + 90, 740, 240, 45))
    xml_lines.append(node("act_s_read_item", "Siswa membaca soal adaptif ZPD\ndan menganalisis opsi jawaban", ST_SISWA, LANE_SISWA_X + 100, 740, 220, 50))

    # Decision Hint Request
    xml_lines.append(node("dec_s_hint", "Butuh Petunjuk\nSokratik?", ST_DEC, LANE_SISWA_X + 150, 820, 120, 70))

    # Jalur Hint Request (Agen T2)
    xml_lines.append(node("act_s_req_hint", "Klik 'Minta Petunjuk'\n(Trigger Agen T2)", ST_SISWA, LANE_SISWA_X + 280, 895, 140, 45))
    xml_lines.append(node("act_sys_t2_rag", "Agen T2: Retrieve konteks KB dari pgvector,\ngenerate prompt sokratik ke LLM Lokal\n(Qwen2.5-3B, max 60 kata, guiding not solving)", ST_SYS, LANE_SYS_X + 80, 885, 260, 65))
    xml_lines.append(node("dec_sys_guard", "Lolos Leakage Guard\n& Latency <= 3.0s?", ST_DEC, LANE_SYS_X + 140, 975, 140, 70))

    # Jalur Hint Lolos vs Fallback
    xml_lines.append(node("act_sys_hint_ok", "Sajikan T2 Socratic Hint ke siswa\n(Set pengali mastery h = 0.5)", ST_SYS, LANE_SYS_X + 20, 1065, 200, 50))
    xml_lines.append(node("act_sys_hint_fb", "Fallback instan (<50ms) ke Static Curated Hint Bank\n(Set pengali mastery h = 0.5)", ST_ALERT, LANE_SYS_X + 240, 1065, 180, 50))
    xml_lines.append(node("act_s_view_hint", "Membaca petunjuk scaffolding dan menganalisis ulang soal", ST_SISWA, LANE_SISWA_X + 190, 1140, 220, 45))

    # Submit Jawaban
    xml_lines.append(node("act_s_submit", "Memilih opsi dan submit jawaban", ST_SISWA, LANE_SISWA_X + 90, 1210, 220, 45))
    xml_lines.append(node("act_sys_update_m", "Mesin L3 Deterministic Update (<1 ms):\n- Jika r=1: m = m + alpha_d * (1-m) * h\n- Jika r=0: m = m - gamma_d * m\nStrict clipping: m in [0.02, 0.98]\nAppend-only log interactions", ST_SYS, LANE_SYS_X + 80, 1200, 260, 75))
    xml_lines.append(node("act_sys_ws_push", "WebSocket broadcast update metrik\nke Dasbor Ambient Guru real-time", ST_SYS, LANE_SYS_X + 90, 1300, 240, 45))

    # Monitoring Ambient Guru & Intervensi Roving
    xml_lines.append(node("act_g_ambient", "Dasbor Ambient Guru update real-time:\nRadar 12 KCs kelas & Top-3 Stuck Students", ST_GURU, LANE_GURU_X + 80, 1300, 250, 45))
    xml_lines.append(node("dec_g_stuck", "Deteksi Siswa Stuck?\n(Hint >= 2 / Waktu > 120s\n/ Delta m < 0)", ST_DEC, LANE_GURU_X + 125, 1370, 160, 80))
    xml_lines.append(node("act_g_intervene", "Intervensi Klinis Tatap Muka:\nGuru mendatangi meja siswa, memberikan\nscaffolding lisan (guiding, not solving)", ST_GURU, LANE_GURU_X + 80, 1475, 250, 60))
    xml_lines.append(node("act_s_receive_scaff", "Siswa menerima bimbingan guru dan\nmemperbaiki penalaran teknis", ST_SISWA, LANE_SISWA_X + 90, 1480, 220, 50))
    xml_lines.append(node("act_g_roving_cont", "Guru terus berkeliling mengawasi\nZona A (praktik) dan Zona B (kuis)", ST_GURU, LANE_GURU_X + 80, 1560, 250, 45))

    # Loop Adaptive Check
    xml_lines.append(node("dec_sys_done", "Butir adaptif ke-20\nsudah selesai?", ST_DEC, LANE_SYS_X + 130, 1465, 160, 70))
    xml_lines.append(node("act_s_eval_done", "Menyelesaikan 20 butir soal,\nmelihat profil penguasaan pribadi (Rotasi 1)", ST_SISWA, LANE_SISWA_X + 90, 1560, 230, 50))

    # -------------------------------------------------------------
    # FASE 3: TRANSISI ROTASI ZONA (40:00 - 42:00 / 2 Menit)
    # -------------------------------------------------------------
    xml_lines.append(phase_banner("b3", "FASE 3: TRANSISI PERGANTIAN STASIUN (40:00 - 42:00 WIB / 2 Menit)", 1640))

    xml_lines.append(node("act_g_bell", "Guru membunyikan lonceng sinyal rotasi\n(Timer 35 menit Rotasi 1 berakhir)", ST_GURU, LANE_GURU_X + 90, 1690, 240, 50))
    xml_lines.append(node("act_s_rotate", "TRANSISI ROTASI STASIUN:\n- Kelompok A: Rapikan PC Lab, bergerak ke meja Zona B\n- Kelompok B: Rapikan meja, bergerak ke PC Lab Zona A", ST_SISWA, LANE_SISWA_X + 70, 1685, 280, 60))

    # -------------------------------------------------------------
    # FASE 4: SIKLUS ROTASI 2 (42:00 - 77:00 / 35 Menit)
    # -------------------------------------------------------------
    xml_lines.append(phase_banner("b4", "FASE 4: SIKLUS ROTASI 2 (42:00 - 77:00 WIB / 35 Menit) — KEL. B (ZONA A) & KEL. A (ZONA B)", 1770))

    xml_lines.append(node("act_s_zona_a2", "KELOMPOK B (Zona A - Lab PC 1:1):\nPraktik konfigurasi jaringan kabel & nirkabel\n(mengikuti alur jobsheet)", ST_SISWA, LANE_SISWA_X + 20, 1820, 200, 65))
    xml_lines.append(node("act_s_zona_b2", "KELOMPOK A (Zona B - Meja Kuis):\nEvaluasi Formatif Adaptif LogiTrace\n(Cold-start 6 butir -> ZPD Adaptive 14 butir)", ST_SISWA, LANE_SISWA_X + 230, 1820, 190, 65))
    xml_lines.append(node("act_g_roving2", "Guru melanjutkan pemantauan roving,\ninspeksi dasbor ambient, dan\nintervensi scaffolding terarah", ST_GURU, LANE_GURU_X + 90, 1820, 240, 65))
    xml_lines.append(node("act_sys_cycle2", "LogiTrace memproses interaksi Kelompok A,\nupdate mastery L3, dan deteksi stuck", ST_SYS, LANE_SYS_X + 90, 1820, 240, 65))
    xml_lines.append(node("act_s_all_done", "Seluruh siswa (34 siswa XI TKJ 1)\ntelah menuntaskan 20 butir evaluasi formatif", ST_SISWA, LANE_SISWA_X + 80, 1915, 260, 50))

    # -------------------------------------------------------------
    # FASE 5: REFLEKSI AKHIR & PEER-TUTORING (77:00 - 85:00 / 8 Menit)
    # -------------------------------------------------------------
    xml_lines.append(phase_banner("b5", "FASE 5: SESI PLENO REFLEKSI & REKOMENDASI PEER-TUTORING (77:00 - 85:00 WIB / 8 Menit)", 1990))

    xml_lines.append(node("act_s_gather", "Seluruh siswa (34 siswa) berkumpul kembali\ndi ruang tengah untuk sesi pleno kelas", ST_SISWA, LANE_SISWA_X + 80, 2040, 260, 50))
    xml_lines.append(node("act_g_req_t3", "Guru menekan tombol 'Generate Summary\n& Peer Tutoring' di Dasbor Ambient", ST_GURU, LANE_GURU_X + 90, 2040, 240, 50))
    xml_lines.append(node("act_sys_t3_engine", "Agen T3 mengeksekusi analisis akhir sesi:\n1. Agregasi data 34 siswa pada 12 KCs\n2. Algoritma Bipartite Matching Peer-Tutoring:\n   Tutor (m >= 0.70) <-> Mentee (m < 0.40)\n3. Prompting LLM Qwen2.5-3B untuk narasi refleksi", ST_SYS, LANE_SYS_X + 80, 2030, 270, 80))
    xml_lines.append(node("act_sys_t3_show", "Kirim narasi refleksi kelas & matriks rekomendasi\npasangan tutor sebaya ke Dasbor Guru", ST_SYS, LANE_SYS_X + 90, 2140, 250, 50))
    xml_lines.append(node("act_g_review_t3", "Guru memaparkan temuan miskonsepsi kelas,\nulasan KCs terlemah, dan mengumumkan\npasangan tutor sebaya tindak lanjut", ST_GURU, LANE_GURU_X + 80, 2135, 260, 60))
    xml_lines.append(node("act_s_reflect", "Siswa menyimak refleksi bersama,\nmenerima pasangan peer-tutoring,\ndan mencatat target penguatan kompetensi", ST_SISWA, LANE_SISWA_X + 80, 2225, 260, 60))
    xml_lines.append(node("act_g_close", "Guru memberikan apresiasi, motivasi,\ndan menutup pembelajaran dengan doa", ST_GURU, LANE_GURU_X + 90, 2225, 240, 60))
    xml_lines.append(node("act_end", "Selesai Pembelajaran\nStation Rotation", ST_END, LANE_GURU_X + 130, 2315, 160, 50))

    # -------------------------------------------------------------
    # EDGES (CONNECTORS)
    # -------------------------------------------------------------
    edges = [
        # Fase 1
        ("e1", "", "act_start", "act_g_open"),
        ("e2", "", "act_g_open", "act_g_split"),
        ("e3", "Instruksi Pembagian Zona", "act_g_split", "act_s_prep", "exitX=0;exitY=0.5;entryX=1;entryY=0.5;"),
        
        # Ke Fase 2
        ("e4", "Kel. A (Zona A)", "act_s_prep", "act_s_zona_a1", "exitX=0.25;exitY=1;entryX=0.5;entryY=0;"),
        ("e5", "Kel. B (Zona B)", "act_s_prep", "act_s_zona_b1", "exitX=0.75;exitY=1;entryX=0.5;entryY=0;"),
        ("e6", "Request Auth", "act_s_zona_b1", "act_sys_auth", "exitX=1;exitY=0.5;entryX=0;entryY=0.5;"),
        ("e7", "", "act_sys_auth", "act_sys_coldstart"),
        ("e8", "Sajikan Butir 1-6", "act_sys_coldstart", "act_s_coldstart", "exitX=0;exitY=0.5;entryX=1;entryY=0.5;"),
        ("e9", "Submit Jawaban Kalibrasi", "act_s_coldstart", "act_sys_eval_cold", "exitX=1;exitY=0.5;entryX=0;entryY=0.5;"),
        ("e10", "", "act_sys_eval_cold", "act_sys_calc_zpd"),
        ("e11", "", "act_sys_calc_zpd", "act_sys_serve_zpd"),
        ("e12", "Butir Adaptif ZPD", "act_sys_serve_zpd", "act_s_read_item", "exitX=0;exitY=0.5;entryX=1;entryY=0.5;"),
        ("e13", "", "act_s_read_item", "dec_s_hint"),
        
        # Hint branch
        ("e14", "Ya", "dec_s_hint", "act_s_req_hint", "exitX=1;exitY=0.5;entryX=0.5;entryY=0;"),
        ("e15", "Kueri Konteks & Prompt", "act_s_req_hint", "act_sys_t2_rag", "exitX=1;exitY=0.5;entryX=0;entryY=0.5;"),
        ("e16", "", "act_sys_t2_rag", "dec_sys_guard"),
        ("e17", "Lolos Guard\n(<=3s)", "dec_sys_guard", "act_sys_hint_ok", "exitX=0;exitY=0.5;entryX=0.5;entryY=0;"),
        ("e18", "Bocor / Timeout\n(>3s)", "dec_sys_guard", "act_sys_hint_fb", "exitX=1;exitY=0.5;entryX=0.5;entryY=0;"),
        ("e19", "Petunjuk Sokratik", "act_sys_hint_ok", "act_s_view_hint", "exitX=0;exitY=0.5;entryX=1;entryY=0.25;", [(LANE_SYS_X - 60, 1090), (LANE_SISWA_X + 410, 1150)]),
        ("e20", "Static Hint", "act_sys_hint_fb", "act_s_view_hint", "exitX=0.5;exitY=1;entryX=1;entryY=0.75;", [(LANE_SYS_X + 330, 1170), (LANE_SISWA_X + 410, 1170)]),
        ("e21", "Lanjut Menjawab", "act_s_view_hint", "act_s_submit", "exitX=0.5;exitY=1;entryX=0.75;entryY=0;"),
        ("e22", "Tidak (Langsung Jawab)", "dec_s_hint", "act_s_submit", "exitX=0.5;exitY=1;entryX=0.25;entryY=0;"),
        
        # Submit & Update
        ("e23", "Submit Pilihan", "act_s_submit", "act_sys_update_m", "exitX=1;exitY=0.5;entryX=0;entryY=0.5;"),
        ("e24", "", "act_sys_update_m", "act_sys_ws_push"),
        ("e25", "WebSocket Push", "act_sys_ws_push", "act_g_ambient", "exitX=0;exitY=0.5;entryX=1;entryY=0.5;"),
        ("e26", "", "act_g_ambient", "dec_g_stuck"),
        ("e27", "Ya (Stuck)", "dec_g_stuck", "act_g_intervene", "exitX=0.5;exitY=1;entryX=0.5;entryY=0;"),
        ("e28", "Tatap Muka", "act_g_intervene", "act_s_receive_scaff", "exitX=0;exitY=0.5;entryX=1;entryY=0.5;"),
        ("e29", "Selesai Bimbingan", "act_s_receive_scaff", "act_s_read_item", "exitX=0;exitY=0.5;entryX=0;entryY=0.5;", [(LANE_SISWA_X + 50, 1505), (LANE_SISWA_X + 50, 765)]),
        ("e30", "Tidak", "dec_g_stuck", "act_g_roving_cont", "exitX=1;exitY=0.5;entryX=1;entryY=0.5;", [(LANE_GURU_X + 350, 1410), (LANE_GURU_X + 350, 1582)]),
        
        # Adaptive check loop
        ("e31", "", "act_sys_ws_push", "dec_sys_done", "exitX=0.5;exitY=1;entryX=0.5;entryY=0;"),
        ("e32", "Belum (N < 20)", "dec_sys_done", "act_sys_calc_zpd", "exitX=1;exitY=0.5;entryX=1;entryY=0.5;", [(LANE_SYS_X + 370, 1500), (LANE_SYS_X + 370, 675)]),
        ("e33", "Ya (N = 20)", "dec_sys_done", "act_s_eval_done", "exitX=0;exitY=0.5;entryX=1;entryY=0.5;"),
        
        # Transisi
        ("e34", "35 Mnt Selesai", "act_g_roving_cont", "act_g_bell", "exitX=0.5;exitY=1;entryX=0.5;entryY=0;"),
        ("e35", "Bel Rotasi", "act_g_bell", "act_s_rotate", "exitX=0;exitY=0.5;entryX=1;entryY=0.5;"),
        
        # Fase 4 (Rotasi 2)
        ("e36", "Kel. B ke Zona A", "act_s_rotate", "act_s_zona_a2", "exitX=0.25;exitY=1;entryX=0.5;entryY=0;"),
        ("e37", "Kel. A ke Zona B", "act_s_rotate", "act_s_zona_b2", "exitX=0.75;exitY=1;entryX=0.5;entryY=0;"),
        ("e38", "", "act_g_bell", "act_g_roving2", "exitX=0.5;exitY=1;entryX=0.5;entryY=0;"),
        ("e39", "Interaksi Kuis Kel. A", "act_s_zona_b2", "act_sys_cycle2", "exitX=1;exitY=0.5;entryX=0;entryY=0.5;"),
        ("e40", "Selesai Rotasi 2", "act_s_zona_a2", "act_s_all_done", "exitX=0.5;exitY=1;entryX=0.25;entryY=0;", [(LANE_SISWA_X + 120, 1940)]),
        ("e41", "", "act_s_zona_b2", "act_s_all_done", "exitX=0.5;exitY=1;entryX=0.75;entryY=0;"),
        
        # Fase 5 (Refleksi)
        ("e42", "Kumpul Pleno", "act_s_all_done", "act_s_gather", "exitX=0.5;exitY=1;entryX=0.5;entryY=0;"),
        ("e43", "Trigger Sesi Selesai", "act_g_roving2", "act_g_req_t3", "exitX=0.5;exitY=1;entryX=0.5;entryY=0;"),
        ("e44", "Generate Request", "act_g_req_t3", "act_sys_t3_engine", "exitX=1;exitY=0.5;entryX=0;entryY=0.5;"),
        ("e45", "", "act_sys_t3_engine", "act_sys_t3_show"),
        ("e46", "Kirim Laporan T3", "act_sys_t3_show", "act_g_review_t3", "exitX=0;exitY=0.5;entryX=1;entryY=0.5;"),
        ("e47", "Pemaparan Refleksi", "act_g_review_t3", "act_s_reflect", "exitX=0;exitY=0.5;entryX=1;entryY=0.5;"),
        ("e48", "Tindak Lanjut & Penutupan", "act_g_review_t3", "act_g_close", "exitX=0.5;exitY=1;entryX=0.5;entryY=0;"),
        ("e49", "", "act_g_close", "act_end", "exitX=0.5;exitY=1;entryX=0.5;entryY=0;"),
    ]

    edge_id_start = 500
    for eid, lbl, src, tgt, *rest in edges:
        st_extra = rest[0] if len(rest) > 0 else ""
        pts = rest[1] if len(rest) > 1 else None
        xml_lines.append(edge(f"edge_{edge_id_start}", lbl, src, tgt, st_extra, pts))
        edge_id_start += 1

    # Close tags
    xml_lines.extend([
        '      </root>',
        '    </mxGraphModel>',
        '  </diagram>',
        '</mxfile>'
    ])

    return "\n".join(xml_lines)

if __name__ == "__main__":
    out_path = "logitrace/docs/diagrams/activity_diagram_station_rotation.drawio"
    content = generate_drawio_xml()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully generated {out_path} ({len(content)} bytes)")
