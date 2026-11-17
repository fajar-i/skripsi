"""
LogiTrace: export the item-bank blueprint (kisi-kisi) to Excel for researcher/expert review.

Usage:
    python data/l2_item_bank/export_kisi_kisi.py [--out docs/kisi_kisi_bank_soal.xlsx]

Sheets:
  Petunjuk         status of the labels and how to fill the review columns
  Kisi-kisi        one row per competency indicator: TP, KC, indicator, item count per C-level, item numbers
  Matriks          KC x C-level and KC x difficulty counts
  Daftar Butir     all 180 items with labels + empty review columns for experts
  Catatan Telaah   items flagged for expert attention (scope, KC fit, Jonassen phase fit)
  Sebaran          overall distribution of C-level, phase, difficulty; indicators with < 3 items
"""

import argparse
import json
import os
from collections import Counter, defaultdict

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
ITEMS = os.path.join(HERE, "items_adaptive_180.json")
INDIKATOR = os.path.join(HERE, "..", "l1_knowledge_base", "indikator.json")
KCS = os.path.join(HERE, "..", "l1_knowledge_base", "kcs.json")

LEVELS = ["C1", "C2", "C3", "C4", "C5", "C6"]
PHASE_LABEL = {
    "SYMPTOM_RECOGNITION": "1. Pengenalan gejala",
    "PROBLEM_SPACE_CONSTRUCTION": "2. Konstruksi ruang masalah",
    "FAULT_HYPOTHESIS_GENERATION": "3. Perumusan hipotesis gangguan",
    "HYPOTHESIS_TESTING_EVALUATION": "4. Pengujian & evaluasi hipotesis",
    "CORRECTIVE_ACTION_VERIFICATION": "5. Tindakan korektif & verifikasi",
}
DIFF_LABEL = {1: "Mudah", 2: "Sedang", 3: "Sulit"}

HEAD_FILL = PatternFill("solid", fgColor="1F4E78")
HEAD_FONT = Font(bold=True, color="FFFFFF")
REVIEW_FILL = PatternFill("solid", fgColor="FFF2CC")
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")


def write_table(ws, headers, rows, widths, review_cols=()):
    ws.append(headers)
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=c)
        cell.font, cell.fill, cell.alignment, cell.border = HEAD_FONT, HEAD_FILL, WRAP, BORDER
    for r in rows:
        ws.append(r)
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, max_col=len(headers)):
        for cell in row:
            cell.alignment, cell.border = WRAP, BORDER
            if headers[cell.column - 1] in review_cols:
                cell.fill = REVIEW_FILL
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "A2"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(ROOT, "docs", "kisi_kisi_bank_soal.xlsx"))
    args = ap.parse_args()

    items = json.load(open(ITEMS, encoding="utf-8"))
    ind_doc = json.load(open(INDIKATOR, encoding="utf-8"))
    kc_names = {k["id"]: k["name"] for k in json.load(open(KCS, encoding="utf-8"))}
    kc_order = list(dict.fromkeys(i["kc_id"] for i in ind_doc["indikator"]))
    kc_code = {kc: f"KC-{n:02d}" for n, kc in enumerate(kc_order, start=1)}
    indikator = {i["id"]: i for i in ind_doc["indikator"]}
    number = {it["id"]: n for n, it in enumerate(items, start=1)}

    wb = Workbook()

    # Petunjuk
    ws = wb.active
    ws.title = "Petunjuk"
    lines = [
        ["Kisi-kisi Bank Soal Adaptif LogiTrace (180 butir)"],
        [f"Status label: {ind_doc['status']}. Label indikator, level kognitif, dan catatan telaah disusun "
         "dengan bantuan AI dan BELUM divalidasi. Wajib ditelaah peneliti dan pakar sebelum dipakai."],
        [f"Capaian Pembelajaran: {ind_doc['capaian_pembelajaran']}"],
        *[[f"{k}: {v}"] for k, v in ind_doc["tujuan_pembelajaran"].items()],
        ["Level kognitif: Taksonomi Bloom revisi (Anderson & Krathwohl, 2001). C6 tidak dipakai karena "
         "soal pilihan ganda tidak menuntut siswa menghasilkan produk baru."],
        ["Fase troubleshooting: Jonassen & Hung (2006), menggantikan dimensi TOLT."],
        ["Tingkat kesulitan nominal (1-3) adalah perkiraan awal; tetapkan ulang dari indeks kesukaran hasil uji coba."],
        ["Cara menelaah: isi kolom berlatar kuning pada sheet 'Daftar Butir'. Untuk Aiken's V, beri skor 1-5 "
         "pada kolom 'Skor kesesuaian indikator (1-5)'."],
    ]
    for line in lines:
        ws.append(line)
    ws["A1"].font = Font(bold=True, size=14)
    ws.column_dimensions["A"].width = 140
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")

    # Kisi-kisi
    by_ind = defaultdict(list)
    for it in items:
        by_ind[it["indikator_id"]].append(it)
    rows = []
    for ind in ind_doc["indikator"]:
        its = by_ind.get(ind["id"], [])
        lv = Counter(i["bloom_level"] for i in its)
        rows.append([
            ind["tujuan_pembelajaran"], f"{kc_code[ind['kc_id']]} {kc_names.get(ind['kc_id'], ind['kc_id'])}",
            ind["id"], ind["rumusan"], *[lv.get(l, 0) for l in LEVELS], len(its),
            ", ".join(str(number[i["id"]]) for i in its),
            ", ".join(sorted({PHASE_LABEL[i["jonassen_phase"]].split(". ")[0] for i in its})),
        ])
    ws = wb.create_sheet("Kisi-kisi")
    write_table(ws, ["TP", "Knowledge Component", "ID Indikator", "Indikator", *LEVELS, "Jumlah",
                     "Nomor butir", "Fase Jonassen"],
                rows, [8, 30, 11, 60, 5, 5, 5, 5, 5, 5, 8, 30, 12])

    # Matriks
    ws = wb.create_sheet("Matriks")
    rows = []
    for kc in kc_order:
        its = [i for i in items if i["primary_kc"] == kc]
        lv = Counter(i["bloom_level"] for i in its)
        df = Counter(i["difficulty"] for i in its)
        rows.append([f"{kc_code[kc]} {kc_names.get(kc, kc)}", *[lv.get(l, 0) for l in LEVELS],
                     df.get(1, 0), df.get(2, 0), df.get(3, 0), len(its)])
    tot = Counter(i["bloom_level"] for i in items)
    tdf = Counter(i["difficulty"] for i in items)
    rows.append(["TOTAL", *[tot.get(l, 0) for l in LEVELS], tdf[1], tdf[2], tdf[3], len(items)])
    write_table(ws, ["Knowledge Component", *LEVELS, "Mudah", "Sedang", "Sulit", "Jumlah"], rows,
                [40, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8])

    # Daftar Butir
    review = ["Indikator sesuai? (Y/T)", "Skor kesesuaian indikator (1-5)", "Level kognitif menurut penelaah",
              "Fase menurut penelaah", "Kunci benar? (Y/T)", "Catatan penelaah"]
    rows = []
    for it in items:
        ind = indikator[it["indikator_id"]]
        o = it["options"]
        rows.append([
            number[it["id"]], it["id"], it["tujuan_pembelajaran"], kc_code[it["primary_kc"]],
            it["indikator_id"], ind["rumusan"], it["bloom_level"], PHASE_LABEL[it["jonassen_phase"]],
            DIFF_LABEL[it["difficulty"]], "Ya" if it["is_calibration"] else "", it["prompt_text"],
            o.get("A", ""), o.get("B", ""), o.get("C", ""), o.get("D", ""), it["correct_answer"],
            it.get("explanation", ""), "; ".join(it.get("catatan_telaah", [])), it.get("label_status", ""),
            *[""] * len(review),
        ])
    ws = wb.create_sheet("Daftar Butir")
    write_table(ws, ["No", "ID Butir", "TP", "KC", "ID Indikator", "Indikator", "Level kognitif (draf)",
                     "Fase Jonassen (draf)", "Kesulitan nominal", "Kalibrasi", "Soal", "A", "B", "C", "D",
                     "Kunci", "Pembahasan", "Catatan telaah (draf)", "Status label", *review],
                rows, [5, 30, 7, 7, 10, 40, 9, 22, 9, 8, 55, 25, 25, 25, 25, 6, 40, 35, 11, 10, 10, 12, 16, 9, 30],
                review_cols=review)

    # Catatan Telaah
    ws = wb.create_sheet("Catatan Telaah")
    rows = [[number[it["id"]], it["id"], kc_code[it["primary_kc"]], it["bloom_level"],
             PHASE_LABEL[it["jonassen_phase"]], note, it["prompt_text"]]
            for it in items for note in it.get("catatan_telaah", [])]
    write_table(ws, ["No", "ID Butir", "KC", "Level", "Fase", "Catatan", "Soal"], rows,
                [5, 30, 7, 7, 26, 50, 70])

    # Sebaran
    ws = wb.create_sheet("Sebaran")
    rows = [["Level kognitif", l, tot.get(l, 0), f"{tot.get(l, 0) / len(items):.1%}"] for l in LEVELS]
    ph = Counter(i["jonassen_phase"] for i in items)
    rows += [["Fase Jonassen", PHASE_LABEL[p], ph.get(p, 0), f"{ph.get(p, 0) / len(items):.1%}"] for p in PHASE_LABEL]
    rows += [["Kesulitan nominal", DIFF_LABEL[d], tdf[d], f"{tdf[d] / len(items):.1%}"] for d in (1, 2, 3)]
    thin = [i for i in ind_doc["indikator"] if len(by_ind.get(i["id"], [])) < 3]
    rows += [["Indikator < 3 butir", f"{i['id']} {i['rumusan']}", len(by_ind.get(i["id"], [])), ""] for i in thin]
    write_table(ws, ["Aspek", "Kategori", "Jumlah", "Persen"], rows, [22, 80, 9, 9])

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    wb.save(args.out)
    print(f"Saved {args.out}")


if __name__ == "__main__":
    main()
