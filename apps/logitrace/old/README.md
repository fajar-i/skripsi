# old/ — file yang tidak lagi dipakai LogiTrace

Disimpan untuk jejak riwayat, bukan untuk dijalankan. Aplikasi, tes, dan skrip evaluasi aktif
tidak membaca apa pun dari folder ini.

| Folder | Isi | Alasan dipindahkan |
|---|---|---|
| `data_tolt/` | `tolt_test_parallel.json`, `tolt_dimensions.json`, `balance_instruments.py` | TOLT tidak lagi dipakai sebagai indikator; diganti indikator kompetensi, level kognitif C1–C6, dan fase troubleshooting Jonassen & Hung (2006) |
| `data_generators/` | `generate_curated_bank.py`, `curated_blueprints_extra.py`, `items_adaptive_180.backup.json` | Generator templat bank soal lama (masih memakai TOLT). `data/l2_item_bank/items_adaptive_180.json` sekarang menjadi sumber tunggal; menjalankan generator ini akan menghapus label kisi-kisi |
| `item_view/` | `build_html_view.py`, `pembagian_soal_*.html` | Tampilan HTML bank soal berbasis TOLT; digantikan `docs/kisi_kisi_bank_soal.xlsx` (dibuat oleh `data/l2_item_bank/export_kisi_kisi.py`) |
| `evals_simulated/` | Skrip E1–E6, `simulate_34_students.py`, `evaluation_report_SIMULATED.json` | **Data hasil bilangan acak, bukan hasil penelitian.** Lihat `evals_simulated/README.md`. Jangan dikutip |
| `evals_results_invalid/` | Data mentah dua run benchmark 9router (17 Nov 2026) | Run pertama tercemar bug batas waktu (pembuatan klien HTTP per permintaan); run kedua dihentikan setelah 52 permintaan. Tidak dipakai untuk naskah |
| `scripts/` | `run_tests.py` | Runner `unittest` lama; tes sekarang dijalankan dengan `pytest` |
| `logitrace_dev.db` | Basis data dev lama (data sintetis) | Aplikasi memakai `logitrace.db` (lihat `.env`). Tidak dilacak git |
