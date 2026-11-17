# Catatan perbaikan draf_artikel_logitrace_sinta3.md

Backup versi lama: `draf_artikel_logitrace_sinta3.v1_backup.md`. Review asal: `review_draf_artikel_logitrace_sinta3.md`.
Semua penanda `[PENULIS: ...]` dan `[PERIKSA: ...]` di naskah = butuh data/keputusan kamu. Hapus setelah diisi.

## A. Sudah diperbaiki di naskah (tanpa perlu data baru)

| # | Perbaikan |
|---|---|
| 1 | **Tabel 3**: baris α₀=0,40 mandiri → 1 butir (m₁=0,670). Teks §3.2 poin 2 ditulis ulang. Label "Optimal" → "Kompromi". Ditambah catatan bahwa simulasi mengasumsikan d=2 terus-menerus (tidak sama dengan perilaku selector) dan bahwa 2 jawaban benar sudah memenuhi syarat tutor karena tebakan/slip tidak dimodelkan. |
| 2 | **Judul & abstrak** (ID+EN) ditulis ulang: ≤ ~250 kata, tanpa "membuktikan/100%/zero outage/patuh privasi/tanpa regresi visual/siap". "RAG-KT" dan "Zero-PII" keluar dari judul/keywords. Hanya angka yang memang ada di tabel dipakai (mis. k=2: 10 dari 12 ≤ 3,0 s). |
| 3 | **Kesimpulan** ditulis ulang. **Keterbatasan** diperluas jadi 8 butir. **Agenda lanjutan** diberi langkah pra-lapangan (simulasi vs BKT/Elo, validasi pakar, rubrik petunjuk, uji beban terpadu). |
| 4 | **Tabel 4**: kolom/label diganti jujur ("Akan Dialihkan ke Fallback", "Seluruh > 3,0 s"), catatan di bawah tabel: simpangan baku, p95 indikatif, CI Wilson (10/10 → 72–100%; 10/12 → 55–95%), throughput agregat 0,57→0,90 req/s, arti "optimal". §2.5 menyatakan bahwa kolom fallback diturunkan dari latensi, bukan fallback yang dieksekusi. |
| 5 | **§3.3**: "tidak pernah menunggu > 3,05 s" → "waktu tunggu terburuk yang dirancang", dengan pernyataan bahwa timeout→fallback di bawah beban belum diuji terpadu. Penjelasan mekanisme (bandwidth DDR4, saturasi thread) diganti "belum diprofilkan". Tabel 5 sel "Implikasi" diperbaiki (puncak CPU 98,5% vs rerata 28,4%). |
| 6 | **Poisson**: angka dikoreksi menjadi ≈1,5×10⁻⁴; ditandai optimistis (kedatangan berkelompok, jumlah permintaan per siswa belum diukur, belum divalidasi log nyata). ">99,9% mencukupi" dihapus dari kesimpulan. |
| 7 | **Konsistensi**: 8-thread → 8 core/16 thread; ambang tutor/mentee 0,70/0,45 di mana-mana; target Tabel 2 (ZPD <1 ms, T3 fallback <50 ms) diselaraskan dengan teks; penomoran mode di Gambar 3 diselaraskan dengan Tabel 6; DSR jadi 6 aktivitas Peffers (+Komunikasi). |
| 8 | **Istilah**: "Tri-Agen RAG" → "Tri-Agen berbasis LLM" + catatan istilah bahwa tidak ada retrieval dan T2 hanya menerima nama KC, level, teks soal. Judul bagian 3.4 diganti "Ilustrasi…" (bukan "Evaluasi Kualitas Pedagogis"); Tabel 7 diberi label contoh pilihan penulis. |
| 9 | **PII/keamanan**: paragraf minimisasi data (payload T2 tanpa data siswa); pemotongan 1.000 karakter tidak lagi diklaim sebagai pertahanan prompt-injection; Layer 3 & 5 ditandai ketahanan layanan, bukan kontrol keamanan; "Zero Answer Leakage" → "minimisasi konteks" + batasannya; Tabel 8 diberi catatan bahwa itu uji kode pada kasus penulis. |
| 10 | **Tabel 6**: latensi Mode 1–3 ditandai perkiraan (tidak diukur) + peringatan hukum transfer data/`9router`. **Tabel 9**: ditandai kualitatif, sel karya lain perlu diverifikasi, tidak ada perbandingan empiris; angka "≥100.000" dihapus. |
| 11 | **TOLT**: klaim "bukan kategorisasi subjektif" dihapus; dinyatakan pemetaan awal penulis, belum divalidasi pakar, belum masuk persamaan. Ambang 0,60/0,70 dinyatakan parameter rancangan (bukan dari Xia). |
| 12 | **Referensi**: Jadhav (2023) dan Wing (2006) dihapus dari teks+daftar (tidak mendukung klaim). Xia → 2025 (sesuai Crossref). Kalimat Nkambou/Tato dilunakkan. Dua DOI bermasalah ditandai `[PERIKSA]`. |
| 13 | Playwright dinyatakan bukan regresi visual/kebergunaan; klaim "ergonomis" jadi "dirancang"; Station Rotation/Zona A–B didefinisikan di Pendahuluan. |

## B. Butuh perhatian/keputusan kamu (tidak bisa saya pastikan)

**Prioritas tinggi (jangan submit sebelum ini):**
1. **Dua referensi tidak terdaftar di Crossref (404):** Komalasari dkk. 2023 (INVOTEC) dan Nurbaeti dkk. 2024 (Edumatic). Keduanya satu-satunya dukungan klaim "1 komputer untuk 2 siswa" dan "evaluasi statis/lambat" di Pendahuluan. Kalau tidak bisa ditemukan di sumber asli, hapus klaim atau ganti sumber. Jangan sitasi yang tak bisa dilacak. Asal-usul kedua entri ini (apakah dihasilkan AI) perlu kamu telusuri.
2. **Tabel 8 / `Budi`:** daftar PIIScrubber tidak memuat nama orang, tapi tabel bilang `Budi` tersensor. Cek kode: kalau memang tidak ada penyensoran nama, hapus klaim itu. Jika ada, jelaskan mekanismenya di §2.4.
3. **Data Gambar 4–5 & Tabel 7:** apakah sintetis/seed? Naskah (dan deklarasi etika) harus menyatakan itu. Saya tidak tahu, jadi hanya menaruh penanda.
4. **Aturan cadangan ZPD:** untuk siswa m < 0,379 tidak ada butir yang memenuhi pita ZPD. Apa yang dilakukan kode? Isi `[PENULIS]` di §2.3. Kalau kodenya tidak menangani (mis. error/butir acak), itu bug nyata yang sebaiknya diperbaiki dulu.
5. **`max_tokens` 120 (produksi) vs 150 (benchmark):** selaraskan, atau ulang benchmark pada nilai produksi.
6. **Konfigurasi Ollama** (`OLLAMA_NUM_PARALLEL`, `num_ctx`, `num_thread`, versi), jumlah ulangan/warm-up, dan apakah RAM/CPU = proses Ollama atau seluruh sistem. Tanpa ini Tabel 4–5 tidak bisa direproduksi. Angka 28–32 token/detik juga perlu sumber (eval_count/eval_duration).
7. **Nama model `ag/gemini-3.8-flash` dan proxy `9router`:** jelaskan model hulunya, penyedia, syarat penggunaan, dan apakah layak untuk sekolah. Ini mode *default* naskah.

**Butuh kerja baru (saya tidak bisa menggantikan):**
8. **Ulang uji konkurensi:** ≥5 ulangan, ≥100 permintaan/kondisi, warm-up, k=3, timeout 3,0 s sungguhan (fallback dieksekusi), uji gagal-jaringan/429/key salah. Lalu perbarui Tabel 4/5.
9. **Simulasi siswa sintetis** (ground-truth mastery diketahui, guess/slip) membandingkan L3 vs BKT vs Elo vs acak. Ini bukti validitas yang paling hemat biaya, dan sesuai klaim "in-silico".
10. **Validasi pakar** (2–3 guru TKJ): pemetaan KC–TOLT, sisi DAG, bank 180 butir, ± 60 petunjuk dengan rubrik.
11. **Daftar sisi DAG** sebagai tabel (induk→anak). Gambar 2 (ASCII) ambigu, dan beberapa dependensi tampak janggal (KC-10 ICMP bergantung KC-07 sinyal radio; KC-05 keamanan bergantung KC-03 IP). Saya tidak mengubahnya karena itu keputusan kurikuler.
12. **Dokumentasi bank soal:** penyusun, validasi, asal tingkat kesulitan, model embedding pgvector.
13. **Argumen Devil's Advocate** yang paling serius: petunjuk T2 = fungsi dari (butir, level) saja, jadi 540 petunjuk bisa dibangkitkan sekali dan ditinjau guru. Putuskan: (a) tambahkan baseline itu, (b) tunjukkan adaptasi per-siswa yang membenarkan LLM runtime, atau (c) bingkai artikel sebagai perbandingan dua mode. Belum saya sentuh karena mengubah kontribusi inti.

**Administratif:**
14. Isi `[Nama Dosen Pembimbing 1/2]` dan `[email@upi.edu]`.
15. Jika jurnal **double-blind**: nama penulis ada di URL repo `github.com/fajari-arkan/...`; siapkan versi anonim.
16. Periksa ulang klaim tentang karya lain (Nkambou 2023: N=294; Zhao 2026; Tato & Nkambou) terhadap naskah aslinya. Saya hanya memverifikasi bahwa DOI ada dan judulnya cocok.
17. Pasal UU PDP belum dikutip. Tambahkan pasal yang relevan (data anak/persetujuan wali; transfer lintas yurisdiksi) setelah diverifikasi sendiri.
18. Rasio PC lab: Pendahuluan "1:2", Agenda lanjutan "1:1". Jelaskan (mis. separuh kelas per zona).
19. Sesuaikan jumlah kata/format dengan pedoman jurnal tujuan (belum disebut nama jurnalnya).
20. `figures/` tidak ada di folder yang saya lihat; pastikan gambar ikut terkirim.
