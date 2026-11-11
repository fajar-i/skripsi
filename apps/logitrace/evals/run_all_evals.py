"""
LogiTrace: Master Evaluation Suite (E1 - E6).
Orchestrates and verifies all 6 empirical evaluation tracks against
the Key Performance Indicators (KPIs) in PRD-LogiTrace-RAG-KT.md.
"""

import json
import os
import sys
import time
from typing import Dict, List

# Add evals to path
EVALS_DIR = os.path.dirname(os.path.abspath(__file__))
if EVALS_DIR not in sys.path:
    sys.path.insert(0, EVALS_DIR)

from e1_content_validity import run_e1_evaluation
from e2_socratic_quality import run_e2_evaluation
from e3_predictive_accuracy import run_e3_evaluation
from e4_llm_reliability import run_e4_evaluation
from e5_latency_usability import run_e5_evaluation
from e6_learning_impact import run_e6_evaluation


def run_full_suite() -> Dict:
    print("\n" + "=" * 80)
    print("LOGITRACE EMPIRICAL EVALUATION SUITE (E1 - E6)")
    print("Skripsi R&D: Model ADDIE 14 Minggu • SMK Negeri 4 Bandung (XI TKJ 1)")
    print("=" * 80 + "\n")

    t_start = time.perf_counter()

    # E1
    print("[1/6] Menjalankan E1: Validitas Isi & Pemetaan Semantik (Aiken's V & Cohen's Kappa)...")
    res_e1 = run_e1_evaluation()
    print(f"      -> Status: {res_e1['status']} (Aiken's V = {res_e1['aikens_v']['mean']}, Kappa = {res_e1['cohens_kappa']['kappa']})")

    # E2
    print("[2/6] Menjalankan E2: Mutu Petunjuk Sokratik & Zero Answer Leakage Guard...")
    res_e2 = run_e2_evaluation()
    print(f"      -> Status: {res_e2['status']} (Zero Leakage = {res_e2['zero_answer_leakage']['leakage_violations']} bocoran, ICC(2,1) = {res_e2['icc_inter_rater_reliability']['icc_score']})")

    # E3
    print("[3/6] Menjalankan E3: Akurasi Prediksi Pasca-Kalibrasi (Butir 7-20 vs 3 Baseline)...")
    res_e3 = run_e3_evaluation()
    print(f"      -> Status: {res_e3['status']} (Akurasi L3 = {res_e3['accuracies']['LogiTrace (L3 Deterministic)']}% vs Best {res_e3['comparison_vs_best_baseline']['best_baseline_accuracy']}%, Delta = +{res_e3['comparison_vs_best_baseline']['accuracy_advantage_pp']} pp, McNemar p = {res_e3['mcnemar_test']['p_value']})")

    # E4
    print("[4/6] Menjalankan E4: Reliabilitas Sistem LLM Lokal (Konsistensi 3x Run & Format JSON)...")
    res_e4 = run_e4_evaluation()
    print(f"      -> Status: {res_e4['status']} (Konsistensi = {res_e4['consistency']['consistency_rate']}, JSON Valid = {res_e4['json_schema_validity']['validity_rate']})")

    # E5
    print("[5/6] Menjalankan E5: Kelayakan Teknis & UX (Latensi L3, RAG, Fallback & Skor SUS)...")
    res_e5 = run_e5_evaluation()
    print(f"      -> Status: {res_e5['status']} (L3 p95 = {res_e5['l3_deterministic_engine']['p95_ms']} ms, Fallback = {res_e5['instant_fallback_latency']['p95_ms']} ms, SUS = {res_e5['system_usability_scale']['mean_sus_score']})")

    # E6
    print("[6/6] Menjalankan E6: Dampak Belajar, Keseimbangan TOLT & Validitas Kontrol NEDV...")
    res_e6 = run_e6_evaluation()
    print(f"      -> Status: {res_e6['status']} (N-Gain = {res_e6['normalized_gain']['mean_n_gain']}, Cohen's dz = {res_e6['paired_effect_size']['cohens_dz']}, Dosis r = {res_e6['dosage_response_analysis']['pearson_r']}, NEDV p = {res_e6['nedv_control_items']['paired_t_p_value']})")

    t_total = time.perf_counter() - t_start

    all_passed = all([
        res_e1["status"] == "PASS",
        res_e2["status"] == "PASS",
        res_e3["status"] == "PASS",
        res_e4["status"] == "PASS",
        res_e5["status"] == "PASS",
        res_e6["status"] == "PASS",
    ])

    report = {
        "suite_name": "LogiTrace Empirical Evaluation Suite (E1 - E6)",
        "overall_status": "ALL PASSED" if all_passed else "SOME FAILED",
        "total_runtime_seconds": round(t_total, 2),
        "scorecard": [
            {
                "kpi_id": "KPI-1",
                "evaluation": "E1: Validitas Isi & Pemetaan Semantik",
                "target": "Aiken's V >= 0.70 & Cohen's Kappa >= 0.60",
                "actual": f"V = {res_e1['aikens_v']['mean']:.4f}, Kappa = {res_e1['cohens_kappa']['kappa']:.4f}",
                "status": res_e1["status"]
            },
            {
                "kpi_id": "KPI-2",
                "evaluation": "E2: Mutu Petunjuk Sokratik",
                "target": "100% Zero Leakage & ICC(2,1) >= 0.70",
                "actual": f"Leakage = {res_e2['zero_answer_leakage']['leakage_violations']}, ICC = {res_e2['icc_inter_rater_reliability']['icc_score']:.4f}",
                "status": res_e2["status"]
            },
            {
                "kpi_id": "KPI-3",
                "evaluation": "E3: Akurasi Prediksi Pasca-Kalibrasi",
                "target": "Akurasi >= Best Baseline + 5.0 pp & McNemar p < 0.05",
                "actual": f"Advantage = +{res_e3['comparison_vs_best_baseline']['accuracy_advantage_pp']:.2f} pp, McNemar p = {res_e3['mcnemar_test']['p_value']:.4f}",
                "status": res_e3["status"]
            },
            {
                "kpi_id": "KPI-4",
                "evaluation": "E4: Reliabilitas LLM Lokal",
                "target": "Konsistensi 3x Run >= 95% & JSON >= 98%",
                "actual": f"Konsistensi = {res_e4['consistency']['consistency_rate']}, JSON = {res_e4['json_schema_validity']['validity_rate']}",
                "status": res_e4["status"]
            },
            {
                "kpi_id": "KPI-5",
                "evaluation": "E5: Kelayakan Teknis & UX",
                "target": "L3 p95 <= 10ms, Fallback < 50ms, SUS >= 68.0",
                "actual": f"L3 = {res_e5['l3_deterministic_engine']['p95_ms']:.4f} ms, Fallback = {res_e5['instant_fallback_latency']['p95_ms']:.4f} ms, SUS = {res_e5['system_usability_scale']['mean_sus_score']:.2f}",
                "status": res_e5["status"]
            },
            {
                "kpi_id": "KPI-6",
                "evaluation": "E6: Dampak Belajar & Validitas NEDV",
                "target": "N-Gain >= 0.30, d_z sig, Dosis r >= 0.35, NEDV p > 0.05",
                "actual": f"N-Gain = {res_e6['normalized_gain']['mean_n_gain']:.4f}, d_z = {res_e6['paired_effect_size']['cohens_dz']:.4f}, Dosis r = {res_e6['dosage_response_analysis']['pearson_r']:.4f}, NEDV p = {res_e6['nedv_control_items']['paired_t_p_value']:.4f}",
                "status": res_e6["status"]
            }
        ],
        "detailed_results": {
            "e1": res_e1,
            "e2": res_e2,
            "e3": res_e3,
            "e4": res_e4,
            "e5": res_e5,
            "e6": res_e6
        }
    }

    # Print Formatted Table
    print("\n" + "=" * 90)
    print(f"{'ID':<7} | {'Dimensi Evaluasi':<32} | {'Target KPI':<30} | {'Status':<8}")
    print("-" * 90)
    for row in report["scorecard"]:
        print(f"{row['kpi_id']:<7} | {row['evaluation']:<32} | {row['actual']:<30} | {row['status']:<8}")
    print("=" * 90)
    print(f"KESIMPULAN AKHIR: {report['overall_status']} (Total waktu: {t_total:.2f} detik)\n")

    # Export Report JSON
    out_path = os.path.join(EVALS_DIR, "evaluation_report.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"[*] Laporan lengkap diekspor ke: {out_path}\n")

    return report


if __name__ == "__main__":
    rep = run_full_suite()
    if rep["overall_status"] != "ALL PASSED":
        sys.exit(1)
