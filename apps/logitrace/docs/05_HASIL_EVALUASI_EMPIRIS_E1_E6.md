# MODUL 05: STATUS EVALUASI

> **Koreksi (17 Nov 2026).** Versi sebelumnya dokumen ini memuat angka E1–E6 (Aiken's V,
> kappa, ICC, SUS, N-Gain, "validasi oleh 5 pakar") yang **dihasilkan oleh skrip simulasi
> berbasis bilangan acak**, bukan dari pakar, guru, atau siswa. Angka tersebut tidak sah
> sebagai hasil penelitian dan telah dihapus.

## Yang sudah ada (teknis, dapat direproduksi)

| Evaluasi | Skrip | Keluaran |
|---|---|---|
| Latensi mesin L3 & fallback statis | `evals/benchmark_l3_engine.py` | `evals/results/l3_engine_*.json` |
| Latensi & fallback petunjuk T2 via 9router | `evals/benchmark_concurrency_9router.py` | `evals/results/concurrency_9router_*.jsonl` + ringkasan `.json` |
| Uji unit & integrasi | `pytest` | keluaran konsol |

## Yang belum ada (memerlukan subjek manusia)

- Validasi isi butir & pemetaan KC/TOLT/DAG oleh pakar.
- Penilaian kualitas petunjuk Sokratik oleh guru/ahli.
- Uji kebergunaan (SUS) dengan guru dan siswa.
- Dampak belajar (pre-test/post-test, N-Gain).

Skrip rancangan analisis untuk butir-butir di atas ada di `old/evals_simulated/`. Skrip itu
membangkitkan data acak untuk menguji jalannya kode analisis saja. **Jangan mengutip
keluarannya sebagai hasil.**
