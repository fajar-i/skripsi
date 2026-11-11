"""
Script to generate the Use Case Diagram for LogiTrace RAG-KT Station Rotation
in draw.io XML format, compliant with drawio-skill specifications.
"""

import xml.sax.saxutils as saxutils
import subprocess
import os

def generate_use_case_xml():
    TOTAL_WIDTH = 1350
    TOTAL_HEIGHT = 1200

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<mxfile host="drawio" version="26.0.0">',
        '  <diagram name="UseCase-Station-Rotation">',
        f'    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{TOTAL_WIDTH}" pageHeight="{TOTAL_HEIGHT}" math="0" shadow="0">',
        '      <root>',
        '        <mxCell id="0" />',
        '        <mxCell id="1" parent="0" />',
    ]

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

    # STYLES
    ST_ACTOR = "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1;fontSize=12;"
    ST_SYSTEM_ACTOR = "rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;fontStyle=1;fontSize=11;"
    ST_BOUNDARY = "swimlane;startSize=30;fillColor=#f8f9fa;strokeColor=#495057;fontStyle=1;fontSize=13;fontColor=#212529;align=center;horizontal=1;collapsible=0;pointerEvents=0;"
    ST_UC = "ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=11;align=center;"
    ST_UC_RAG = "ellipse;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=11;align=center;fontStyle=1;"
    ST_UC_TEACHER = "ellipse;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;align=center;"
    ST_UC_EXT = "ellipse;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=10;align=center;dashed=1;"
    ST_UC_INC = "ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=10;align=center;dashed=1;"

    # System boundary box
    xml_lines.append(node("box_sys", "Sistem LogiTrace (RAG-KT Formatif Adaptif SMK TKJ)", ST_BOUNDARY, 260, 40, 800, 1100))

    # Left Actors (Human Actors)
    xml_lines.append(node("act_siswa", "Siswa XI TKJ 1\n(Zona A & Zona B)", ST_ACTOR, 60, 260, 70, 110))
    xml_lines.append(node("act_guru", "Guru Pengampu\n(Roving Teacher)", ST_ACTOR, 60, 720, 70, 110))

    # Right Actors (Secondary / Engine Actors)
    xml_lines.append(node("act_l3_engine", "Deterministic\nMath Engine L3\n(Cognitive Tracing)", ST_SYSTEM_ACTOR, 1100, 250, 150, 70))
    xml_lines.append(node("act_llm_qwen", "LLM Lokal Qwen2.5-3B\n& RAG pgvector\n(Agen T1, T2, T3)", ST_SYSTEM_ACTOR, 1100, 520, 160, 70))
    xml_lines.append(node("act_db_append", "PostgreSQL / SQLite\nAppend-Only Audit\n(Interactions Table)", ST_SYSTEM_ACTOR, 1100, 840, 150, 70))

    # USE CASES INSIDE SYSTEM BOUNDARY
    # Core Student Use Cases
    xml_lines.append(node("uc1", "UC-01: Autentikasi &\nInisialisasi Sesi Siswa", ST_UC, 310, 100, 180, 65))
    xml_lines.append(node("uc2", "UC-02: Mengerjakan Butir\nKalibrasi (Cold-Start 1–6)", ST_UC, 310, 200, 190, 65))
    xml_lines.append(node("uc3", "UC-03: Mengerjakan Butir\nAdaptif ZPD (Butir 7–20)", ST_UC, 310, 310, 190, 70))
    xml_lines.append(node("uc4", "UC-04: Meminta Bantuan Sokratik\n(Agen T2 Guiding Hint)", ST_UC_RAG, 320, 440, 200, 70))
    
    # Internal Engine / Sub-use cases (Include/Extend)
    xml_lines.append(node("uc_inc_math", "Hitung Mastery m\n& Estimasi p_hat (<1ms)", ST_UC_INC, 640, 240, 180, 60))
    xml_lines.append(node("uc_inc_guard", "Answer Leakage Guard\n& Fallback Static (<50ms)", ST_UC_INC, 640, 440, 190, 65))
    xml_lines.append(node("uc_inc_append", "Append-Only Logging\n(Audit Trail Interaksi)", ST_UC_INC, 640, 350, 180, 60))

    # Teacher Use Cases
    xml_lines.append(node("uc5", "UC-05: Memantau Dasbor Ambient\nReal-Time (Radar 12 KCs)", ST_UC_TEACHER, 310, 580, 200, 70))
    xml_lines.append(node("uc_inc_stuck", "Deteksi Otomatis\nTop-3 Stuck Students", ST_UC_INC, 640, 580, 180, 60))
    xml_lines.append(node("uc6", "UC-06: Melakukan Intervensi Klinis\nTatap Muka (Roving Scaffolding)", ST_UC_TEACHER, 310, 700, 210, 70))
    xml_lines.append(node("uc7", "UC-07: Pembangkitan Refleksi Sesi\n& Peer-Tutoring (Agen T3)", ST_UC_RAG, 320, 820, 210, 75))
    xml_lines.append(node("uc_inc_match", "Bipartite Matching\nTutor (>=0.7) & Mentee (<0.4)", ST_UC_INC, 640, 825, 200, 65))
    xml_lines.append(node("uc8", "UC-08: Pelabelan Semantik Butir\n& Kurasi Bank Soal (Agen T1)", ST_UC_RAG, 320, 940, 210, 70))
    xml_lines.append(node("uc9", "UC-09: Manajemen & Reset Sesi\nKelas Formatif (Standar LMS)", ST_UC_TEACHER, 320, 1040, 210, 65))

    # CONNECTIONS (ACTOR TO USE CASES)
    lines_meta = [
        # Siswa to UCs
        ("e1", "", "act_siswa", "uc1", "endArrow=none;"),
        ("e2", "", "act_siswa", "uc2", "endArrow=none;"),
        ("e3", "", "act_siswa", "uc3", "endArrow=none;"),
        ("e4", "", "act_siswa", "uc4", "endArrow=none;"),
        ("e5", "", "act_siswa", "uc6", "endArrow=none;"), # Siswa menerima intervensi guru
        
        # Guru to UCs
        ("e6", "", "act_guru", "uc5", "endArrow=none;"),
        ("e7", "", "act_guru", "uc6", "endArrow=none;"),
        ("e8", "", "act_guru", "uc7", "endArrow=none;"),
        ("e9", "", "act_guru", "uc8", "endArrow=none;"),
        ("e10", "", "act_guru", "uc9", "endArrow=none;"),

        # Includes & Extends (Dashed with open arrow)
        ("e11", "&lt;&lt;include&gt;&gt;", "uc2", "uc_inc_math", "dashed=1;endArrow=open;strokeColor=#82b366;"),
        ("e12", "&lt;&lt;include&gt;&gt;", "uc3", "uc_inc_math", "dashed=1;endArrow=open;strokeColor=#82b366;"),
        ("e13", "&lt;&lt;include&gt;&gt;", "uc3", "uc_inc_append", "dashed=1;endArrow=open;strokeColor=#82b366;"),
        ("e14", "&lt;&lt;extend&gt;&gt;", "uc4", "uc3", "dashed=1;endArrow=open;strokeColor=#d79b00;"),
        ("e15", "&lt;&lt;include&gt;&gt;", "uc4", "uc_inc_guard", "dashed=1;endArrow=open;strokeColor=#82b366;"),
        ("e16", "&lt;&lt;include&gt;&gt;", "uc5", "uc_inc_stuck", "dashed=1;endArrow=open;strokeColor=#82b366;"),
        ("e17", "&lt;&lt;include&gt;&gt;", "uc7", "uc_inc_match", "dashed=1;endArrow=open;strokeColor=#82b366;"),

        # UCs to System Actors
        ("e18", "", "uc_inc_math", "act_l3_engine", "endArrow=none;strokeColor=#666666;"),
        ("e19", "", "uc4", "act_llm_qwen", "endArrow=none;strokeColor=#666666;"),
        ("e20", "", "uc7", "act_llm_qwen", "endArrow=none;strokeColor=#666666;"),
        ("e21", "", "uc8", "act_llm_qwen", "endArrow=none;strokeColor=#666666;"),
        ("e22", "", "uc_inc_append", "act_db_append", "endArrow=none;strokeColor=#666666;"),
        ("e23", "", "uc9", "act_db_append", "endArrow=none;strokeColor=#666666;"),
    ]

    edge_id = 800
    for eid, lbl, src, tgt, st_extra in lines_meta:
        xml_lines.append(edge(f"edge_{edge_id}", lbl, src, tgt, st_extra))
        edge_id += 1

    xml_lines.extend([
        '      </root>',
        '    </mxGraphModel>',
        '  </diagram>',
        '</mxfile>'
    ])

    return "\n".join(xml_lines)

if __name__ == "__main__":
    out_path = "logitrace/docs/diagrams/use_case_diagram_station_rotation.drawio"
    content = generate_use_case_xml()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully generated {out_path} ({len(content)} bytes)")

    # Export using draw.io CLI
    drawio_exe = r"C:\Program Files\draw.io\draw.io.exe"
    base_dir = r"C:\kuliah\semester_7\skripsi\apps\logitrace\docs\diagrams"
    png_out = os.path.join(base_dir, "use_case_diagram_station_rotation.png")
    drawio_png_out = os.path.join(base_dir, "use_case_diagram_station_rotation.drawio.png")
    svg_out = os.path.join(base_dir, "use_case_diagram_station_rotation.svg")
    repair_script = r"C:\Users\user\.gemini\config\skills\drawio-skill\scripts\repair_png.py"

    if os.path.exists(drawio_exe):
        subprocess.run([drawio_exe, "-x", "-f", "png", "-s", "2", "-o", png_out, out_path, "--disable-gpu"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run([drawio_exe, "-x", "-f", "png", "-e", "-s", "2", "-o", drawio_png_out, out_path, "--disable-gpu"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run([drawio_exe, "-x", "-f", "svg", "-e", "-o", svg_out, out_path, "--disable-gpu"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(repair_script) and os.path.exists(drawio_png_out):
            subprocess.run(["python", repair_script, drawio_png_out])
        print("Exported Use Case Diagram to PNG, Drawio PNG, and SVG!")
