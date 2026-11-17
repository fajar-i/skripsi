# Review Panel — "Rancang Bangun Arsitektur Tiga Lapis (RAG-KT) Multi-Provider ... LogiTrace"

Mode: `full` (5 seat, role-separated; satu sesi, bukan reviewer independen — tidak ada klaim independensi error). Naskah **tidak diubah** (read-only). Target: jurnal SINTA 3 (pendidikan/informatika). Cross-model track: tidak aktif.

---

## Phase 0 — Konfigurasi Panel

| Seat | Persona | Fokus |
|---|---|---|
| Journal-Fit (EIC) | Editor jurnal teknologi pendidikan/informatika Indonesia terakreditasi | kesesuaian venue, kebaruan, kelayakan klaim |
| R1 Metodologi | Peneliti DSR + evaluasi sistem/benchmark | desain evaluasi, statistik, reprodusibilitas |
| R2 Domain | Peneliti knowledge tracing / ITS / psikometri | model kognitif, literatur, validitas |
| R3 Perspektif | Peneliti privasi data pendidikan + HCI/pendidikan kejuruan | UU PDP, keamanan, pedagogi kelas, kebergunaan |
| DA | Devil's Advocate (tetap) | tantang argumen inti |

Paper: system/design paper (DSR), evaluasi hanya teknis/in-silico, tanpa data siswa nyata. Kematangan: draf skripsi-ke-artikel, pra-submit.

---

## Seat 1 — Journal-Fit Reviewer (EIC)

**Rekomendasi sinyal: Major Revision.**

Kekuatan nyata:
- Masalah jelas dan relevan (small-data, perangkat terbatas, privasi). Lingkup keterbatasan jujur (Bab 4: belum ada learning gain).
- Artefak konkret, kode dibuka, pengujian terautomasi, matematika Tabel 3 hampir seluruhnya benar saat dihitung ulang.
- Pola fallback statis adalah keputusan rekayasa yang masuk akal.

Masalah utama kesesuaian:
1. **Klaim melampaui bukti.** Judul/abstrak/kesimpulan memakai "membuktikan", "patuh privasi", "tangguh", "siap diimplementasikan", "zero outage", "100%". Bukti: 1 mesin, 1 run per kondisi, n=10–16, 41 unit test, screenshot Playwright. Tidak ada satu pun data siswa atau ahli.
2. **Kontribusi ilmiah tidak terartikulasi sebagai pengetahuan DSR.** Tidak ada design principles / kriteria evaluasi artefak (Hevner dkk.), tidak ada evaluasi oleh pemangku kepentingan (guru).
3. **Judul tidak konsisten dengan isi.** "RAG-KT" hanya muncul di judul Indonesia dan tidak ada retrieval di T2 (lihat R2/DA). Judul Inggris berbeda dari judul Indonesia. Terlalu panjang (~25 kata).
4. **Format:** abstrak Indonesia ~380 kata dan penuh identifier kode (`9router`, `ag/gemini-3.8-flash`); jurnal biasanya 150–250 kata. Teks utama memakai backtick/identifier kode di mana-mana. Placeholder `[Nama Dosen Pembimbing]`, `[email@upi.edu]` belum diisi.
5. **Anonimitas:** jika jurnal double-blind, nama penulis tertanam di URL repositori (`github.com/fajari-arkan/...`) dan nama sekolah mitra tertulis. Siapkan versi anonim.
6. Zona A/B, *Station Rotation*, *roving teacher* dipakai di Bab 3 tanpa pernah didefinisikan di Pendahuluan/Metode.

Kelayakan sebagai artikel: bisa, setelah di-*reframe* menjadi "rancangan dan studi kelayakan teknis" dengan klaim diturunkan, plus minimal satu evaluasi validitas model kognitif (simulasi) dan satu evaluasi ahli.

---

## Seat 2 — R1 Metodologi

Temuan (anchor = lokasi di draf).

**M1 [Critical] Desain uji konkurensi lemah dan tidak mengukur klaim produksinya.**
- §2.5/Tabel 4: timeout soket benchmark 30 s; kelolosan SLA dihitung *pasca-ukur* (`lat <= 3.0`). Perilaku produksi (putus di 3,0 s lalu fallback) **tidak pernah dieksekusi/diukur**. Kalimat "siswa tidak pernah menunggu lebih dari 3,05 detik" (§3.3) adalah ekstrapolasi, bukan hasil.
- Kolom "Terpicu Fallback" (16,7%, 100%) diturunkan dari latensi, bukan dari fallback yang benar-benar jalan. Latensi fallback 12,3 ms (Tabel 2) diukur terpisah, tanpa beban CPU bersamaan.
- "Gangguan jaringan" disebut di abstrak sebagai skenario teruji; §2.5 tidak memuat uji injeksi kegagalan (putus jaringan, HTTP 429, key invalid) selain satu unit test.

**M2 [Critical] Statistik tidak memadai.**
- n=10 (k=1), 12, 16, 16; satu run, tidak ada ulangan antar-sesi, tidak ada warm-up/cold-start model dilaporkan. **p95 dari n=10 praktis = nilai maksimum**; melaporkan p95 dengan dua desimal menyesatkan.
- "100% lolos SLA" = 10/10; batas bawah CI 95% Wilson ≈ **72%**. "83,3%" = 10/12; CI 95% ≈ **55–95%**. Perlu CI, atau jumlah sampel jauh lebih besar (≥100/kondisi) dan ≥5 ulangan.
- Pada k=2 p95 = 3,06 s **melampaui** SLA 3,0 s, tetapi abstrak/Tabel 4 menyebutnya "operasi optimal / batas kapasitas optimal".
- "Optimal pada k=2" tidak punya dasar throughput. Dari tabel sendiri: throughput agregat = k/latensi rerata = 0,57 → 0,76 → 0,84 → 0,90 req/s (terus naik). Yang "optimal" hanya terhadap ambang SLA, bukan kapasitas. Pisahkan istilahnya.

**M3 [Major] Konfigurasi Ollama tidak dilaporkan.** `OLLAMA_NUM_PARALLEL`, `num_ctx`, `num_thread`, versi Ollama, kuantisasi/penyedia GGUF, keep-alive. Tanpa ini pola 1,74 → 2,64 → 4,74 → 8,90 s tidak dapat ditafsirkan: bisa murni antrean serial, bukan "saturasi jalur memori DDR4". Penjelasan mekanisme (bandwidth DDR4, kontensi thread) tidak didukung profiling apa pun.

**M4 [Major] Pengukuran sumber daya ambigu/inkonsisten (Tabel 5).**
- RAM "awal" 4.314 MB: proses Ollama, atau sistem? Qwen2.5-3B Q4_K_M berukuran ± 2 GB di disk; angka ~4,3–4,5 GB (Pendahuluan: 4,5 GB; §2.5: 4,3 GB) perlu dirinci (model + KV cache + OS?).
- ΔRAM tidak monoton (k=4: +132,7; k=8: +27,4) tanpa penjelasan.
- "Saturasi 98,5%" adalah **puncak**, rerata hanya 28,4%. Laju "28–32 token/detik" untuk 3B Q4 di Ryzen 5700U (DDR4) tinggi; sertakan sumbernya (eval_count/eval_duration Ollama).
- Abstrak/Kesimpulan menyebut "CPU 8-thread"; §2.5 menyebut 8 core/16 thread.

**M5 [Major] Klaim latensi mode cloud/proxy (Tabel 6) tanpa metode.** Latensi `9router`, DeepSeek, Groq (1,2–2,8 s; 0,6–0,9 s; 0,3–0,5 s) tidak diukur di §2.5. Hanya Ollama yang di-benchmark. Tandai sebagai estimasi vendor, atau ukur dengan protokol sama.

**M6 [Major] Inkonsistensi parameter.** `max_tokens = 120` (§2.4) vs `MAX_TOKENS = 150` (§2.5). Target mesin deterministik "< 1 ms" (§2.1) vs target ZPD "< 10 ms" (Tabel 2); fallback T3 "< 50 ms" vs target "< 10 ms" di Tabel 2. Mode provider: abstrak/§2.4 tiga mode, Gambar 3 memberi nomor Mode 1–3, Tabel 6 empat mode dengan penomoran berbeda.

**M7 [Major] Model Poisson (§3.3) tidak sahih untuk kelas.**
- Aritmetika benar (μ ≈ 0,098; P(X≥3) ≈ 1,5×10⁻⁴), tetapi asumsi independensi kedatangan salah untuk kelas: soal tampil serempak, guru memberi aba-aba, siswa sinkron di butir yang sama → **burst terkorelasi**, justru skenario yang diuji k=4–8.
- "Rata-rata 2 permintaan per siswa" tanpa data; petunjuk 3 tingkat berarti sampai 3 panggilan per butir.
- Kesimpulan ">99,9% mencukupi" bergantung penuh pada asumsi ini. Ganti dengan simulasi kelas (34 siswa virtual, think-time empiris, kedatangan berkelompok) atau kurangi klaim.

**M8 [Major] Evaluasi sistem terpisah-pisah.** Uji LLM jalan sendiri; uji API/WebSocket/PostgreSQL untuk 34 klien tidak ada. Ollama menghabiskan CPU host yang sama dengan FastAPI + PostgreSQL (puncak 98,5%) — dampak ke endpoint kuis dan WebSocket tidak diukur. Perlu uji beban end-to-end (mis. Locust/Playwright multi-konteks).

**M9 [Major] DSR tidak lengkap.** Peffers dkk. (2007) punya **enam** aktivitas (termasuk *Communication*); naskah menulis "lima". "Evaluasi" = benchmark teknis; tidak ada kriteria evaluasi artefak yang diturunkan dari tujuan di tahap 2, tidak ada evaluasi utilitas oleh guru/ahli.

**M10 [Minor] Playwright.** "Tanpa regresi visual" (abstrak) tidak sah: 9 tangkapan layar bukan visual regression (tidak ada baseline/diff). Ganti menjadi "9 alur fungsional berjalan". Lampirkan assertion yang dipakai.

**M11 [Minor] Reprodusibilitas.** Pin versi model + tanggal akses untuk model cloud (alias `ag/gemini-3.8-flash` perlu dijelaskan: model apa, via apa, siapa penyedia hulunya). Laporkan seed/urutan permintaan, commit hash repositori.

---

## Seat 3 — R2 Domain (Knowledge Tracing / Psikometri)

**D1 [Critical] Validitas model kognitif tidak diuji sama sekali.** Tujuan intro adalah menandingi BKT/Elo/DKT di data kecil, namun tidak ada perbandingan prediktif (AUC/RMSE/ACC) dengan BKT, Elo, PFA, atau baseline sederhana pada data apa pun (publik maupun sintetis). Aturan update m (§2.3) adalah heuristik ad hoc; tidak ada alasan ia lebih baik daripada BKT dengan prior wajar. Klaim "keterauditan" benar untuk BKT/Elo juga.
Saran praktis, konsisten dengan klaim "in-silico": **studi simulasi dengan siswa sintetis** (ground-truth mastery diketahui, guess/slip, 12 KC dengan DAG) → bandingkan LogiTrace vs BKT vs Elo vs urutan acak/tetap pada: korelasi m dengan truth, butir-menuju-ketuntasan, salah-klasifikasi "mastered/tutor", sensitivitas ke guess/slip.

**D2 [Critical] Tabel 3 mengandung kesalahan dan tidak konsisten dengan seleksi ZPD.**
- Baris α₀ = 0,40, mode mandiri: α₂ = 0,56 → m₁ = 0,25 + 0,56×0,75 = **0,670 ≥ 0,60**, jadi **1 butir**, bukan "2 butir (m₂ = 0,855)". Akibatnya klaim "tidak membedakan mandiri vs berbantuan" untuk α₀=0,40 salah (1 vs 2 butir tetap berbeda), dan argumen eksklusif untuk α₀=0,30 (§3.2 poin 2) gugur sebagian. (Baris lain saya hitung ulang: benar.)
- Simulasi mengasumsikan butir d=2 terus-menerus dari m=0,25. Dengan rumus §2.3, untuk d=2, p̂ = m; butir baru masuk pita ZPD [0,60; 0,85] hanya jika m ≥ 0,60. Untuk d=1 (θ=+0,9) p̂ ≥ 0,60 membutuhkan m ≥ 0,379. Artinya **siswa dengan m < 0,379 tidak punya kandidat butir sama sekali** (himpunan kosong; perilaku tidak didefinisikan), dan lintasan di Tabel 3 tidak akan pernah dihasilkan oleh selector. Setelah m₁ = 0,565 pun selector memilih d=1, bukan d=2.
- "Analisis sensitivitas" hanya memvariasikan satu parameter dalam skenario deterministik tanpa derau; kriteria pilihan ("2 vs 3 butir") dirancang sendiri → sirkular. γ₀, β, θ, p_target = 0,72, τ = 60 hari, m₀ = 0,25, ambang 0,60/0,70 tidak ada pembenaran/sensitivitas.

**D3 [Major] Dua jawaban benar mandiri (m=0,748) → "kandidat tutor sebaya" (≥ 0,70).** Tanpa guess/slip, kepercayaan diri m berlebihan; dua tebakan beruntung (dua-tier masih bisa ditebak) memenuhi syarat tutor. Perlu estimasi ketidakpastian atau jumlah bukti minimum.

**D4 [Major] Hilangnya informasi dua-tier.** Nilai benar hanya jika kedua tingkat benar (r ∈ {0,1}); kombinasi (benar, alasan salah) = miskonsepsi tipikal yang menjadi alasan memakai instrumen dua-tier, dibuang. Pertimbangkan pembaruan/diagnosis terpisah.

**D5 [Major] Peluruhan Ebbinghaus.** m(t)=m·exp(−Δt/τ) meluruh menuju 0 (bukan prior), bisa jatuh di bawah m₀; τ = 60 hari seragam untuk 12 KC tanpa dasar. Hanya klaim konsep, tidak ada evaluasi.

**D6 [Major] Pemetaan KC–TOLT dan DAG tidak divalidasi pakar.**
- Tobin & Capie (1981) mendefinisikan 5 subskala TOLT; mereka **tidak** menyediakan pemetaan ke konsep WLAN/ICMP. "Berbeda dari kategorisasi subjektif" tidak benar: pemetaan di Tabel 1 adalah penilaian penulis, dengan sitasi sebagai otoritas semu. Beberapa pemetaan dipertanyakan (KC-03 IP statis → *Controlling Variables*; KC-09 CSMA/CA → *Proportional*).
- Dimensi TOLT **tidak dipakai** mesin L3 atau dasbor manapun yang dijelaskan → kontribusi dekoratif. Jelaskan fungsi operasionalnya atau hapus dari klaim.
- DAG hanya sebagai ASCII ambigu (Gambar 2), tanpa tabel sisi. Dependensi tampak aneh secara kurikuler: ICMP *connectivity* (KC-10) bergantung pada *signal propagation* (KC-07); *WLAN security* (KC-05) bergantung pada *IP config* (KC-03); *roaming* tidak bergantung pada BSS/ESS (KC-02) secara langsung. Perlu justifikasi tiap sisi + validasi pakar (Delphi/CVI, inter-rater, kappa).
- Judul/§2.2 menyebut "jaringan kabel dan nirkabel", tetapi 12 KC hanya WLAN dan ICMP; cakupan kabel nihil.

**D7 [Major] Bank soal.** 180 butir "terkurasi" tanpa proses: siapa penyusun, validitas isi, uji coba, indeks kesulitan empiris, kualitas distraktor, reliabilitas. Kesulitan d ∈ {1,2,3} ditentukan dari heuristik/Agen T1 (kecocokan kata kunci), bukan data. Model embedding untuk `pgvector` (nama, dimensi, indeks) tidak disebut, dan peran pencarian semantik dalam loop adaptif tidak jelas.

**D8 [Major] "RAG" dan "Agen" diberi label berlebihan.** §3.4: prompt T2 hanya berisi nama KC, level, dan teks soal — **tidak ada konteks hasil retrieval**, tidak ada respons/riwayat siswa. T1 = pencocokan leksikal-semantik; T3 = sebagian algoritma *bipartite matching* deterministik + templat. Tidak ada otonomi/penggunaan alat/perencanaan. Pakai istilah "layanan berbasis LLM" atau tunjukkan retrieval/otonomi yang sebenarnya; hapus "RAG-KT" dari judul bila tidak ada RAG.

**D9 [Major] Literatur: sitasi tidak mendukung klaim.**
- Xia dkk. (Optimizing mastery learning by fast-forwarding over-practice) dikutip untuk ambang prasyarat DAG 0,60/0,70 dan "batas kognitif kokoh"; Jadhav dkk. (alat disleksia/diskalkulia EDSense) untuk "DAG terbukti memberi batas kognitif" — keduanya tidak mendukung klaim itu.
- Tato & Nkambou (2022) menyuntikkan pengetahuan pakar **ke jaringan saraf dalam**; dipakai sebagai bukti bahwa struktur pakar lebih efektif daripada *training*, dan untuk mendukung pendekatan "bebas pelatihan" — overstated.
- Wing (2006) (computational thinking) dikutip untuk penalaran logis formal di jaringan.
- "≥ 100.000 baris data" ambang DKT tanpa sumber.
- Tabel 9 membandingkan kategori berbeda (DKT = model; Logic-Muse/SageJavon = sistem) dan menetapkan atribut "rentan transmisi awan", "ketergantungan awan tunggal" ke karya lain tanpa bukti dari karya tersebut. Perbandingan wajib dengan **BKT/Elo/AFM/PFA** dan sistem ITS ringan lain (bukan DKT sebagai strawman).
- Literatur LLM-tutor/hint generation dengan evaluasi kualitas dan LLM-based KT (selain Wang 2026; Zhao 2026) tipis.

**D10 [Minor]** Rentang m "≥ 0,65–0,70" / "≤ 0,40–0,45" (§2.4) vs 0,70/0,45 (§3.6) — tetapkan satu nilai. `test_calibration` menguji "pewarisan estimasi klaster DAG" yang tidak pernah dijelaskan di Metode. Istilah "kalibrasi" menyesatkan: 6 butir awal tidak mengkalibrasi parameter apa pun.

---

## Seat 4 — R3 Perspektif (Privasi, Keamanan, Pedagogi, Kebergunaan)

**P1 [Critical] "Zero-PII" dan "patuh privasi" tidak terbukti, dan tidak sama dengan kepatuhan UU PDP.**
- Bukti = beberapa kasus uji (mis. NISN `0061234567`, nama, sekolah). Tidak ada korpus uji PII berlabel dengan variasi format (spasi/tanda hubung pada telepon, `+62 8xx`, NISN berformat, nama lengkap bebas), tidak ada recall/FN-rate. "Menyaring 100%" dari n kecil: batas atas FN 95% ≈ 3/n (aturan tiga).
- Tabel 8 menyebut nama `Budi` tersensor 100%, tetapi daftar PIIScrubber (§2.4 Layer 1) **tidak mencantumkan nama orang**; regex tidak dapat menangkap nama bebas. Jelaskan (NER? daftar nama?) atau koreksi klaim.
- **Model ancaman tidak dinyatakan.** Payload T2 hanya berisi nama KC, level, teks butir (konten bank soal, bukan data siswa). Jadi PII tidak mungkin ada di T2 *by construction*; hanya T3 (kode siswa/agregat kelas). Maka "Zero-PII" lebih jujur dinyatakan sebagai *data minimization by design* + scrubber sebagai lapis cadangan; uraikan data apa yang benar-benar melewati batas ke penyedia luar.
- "Zero-PII" mengesankan sistem tanpa PII, padahal basis data menyimpan login siswa, kode/identitas, respons. Perlindungan *at-rest*, otentikasi/otorisasi siswa-guru, retensi, enkripsi, log, akses dasbor WebSocket tidak dibahas. Judul "Zero-PII Hardening" overclaim → "redaksi PII keluar (outbound)".
- Aspek hukum: rujuk pasal UU 27/2022 yang relevan (mis. data anak, persetujuan orang tua/wali; transfer data lintas yurisdiksi bila memakai API luar negeri; kewajiban pengendali/prosesor, perjanjian pemrosesan data). Verifikasi nomor pasal sebelum dikutip. Mode proxy `9router`→Gemini dan DeepSeek/Groq mengirim teks ke luar negeri; tentukan posisi hukumnya.
- Keandalan/ToS: bergantung pada proxy lokal pihak ketiga (`9router`) sebagai **mode default**. Jelaskan asalnya, kebijakan penggunaan, risiko kuota/pemutusan akses, dan kelayakannya untuk produksi sekolah.

**P2 [Major] "Lima lapis keamanan" mencampur keamanan dengan keandalan.** Timeout (L3) dan fallback (L5) adalah ketahanan layanan; `stream=False` dan `verify=True` adalah konfigurasi, bukan lapis pertahanan. Prompt-injection dibahas hanya via pemotongan 1.000 karakter — tidak memadai dan tidak diuji. Masking kunci `sk-d****cdef` membocorkan 8 karakter (kunci pendek bermasalah).

**P3 [Major] Kebocoran jawaban.** (a) Guard (regex + substring ≥ 4 karakter) tidak menangkap parafrase/kebocoran semantik; tidak ada evaluasi (recall pada set petunjuk adversarial). (b) Pada Gambar 3, jalur fallback statis tidak melewati guard; contoh statis di Tabel 7 memuat ambang numerik (−65/−75 dBm) yang bisa langsung menjawab butir sejenis. Jalankan guard pada seluruh 36 petunjuk statis × 180 butir sebagai uji.

**P4 [Major] "Evaluasi kualitas pedagogis" (§3.4) tidak ada.** 3 contoh yang dipilih penulis, tanpa rubrik, tanpa penilai ahli, tanpa penilaian buta, tanpa keterangan model/penyedia pembuat keluaran dinamis. Klaim "lebih tajam" adalah opini. Minimal: 2–3 guru/ahli menilai ≥ 60 petunjuk dengan rubrik (ketepatan teknis, kepatuhan Socratic/tanpa bocor, kejelasan), plus tingkat halusinasi. Terutama untuk **Qwen2.5-3B Q4 berbahasa Indonesia untuk istilah jaringan** — kualitas belum teruji padahal inilah mode luring yang dibela.

**P5 [Major] Data pada Gambar 4–5 tampaknya sintetis** (S14, 34 siswa, m = 0,18, +0,225) tetapi tidak dinyatakan. Deklarasi etika bilang tak ada subjek manusia — maka tulis eksplisit "data peragaan sintetis". Hindari kesan hasil lapangan.

**P6 [Major] Kebergunaan guru/siswa tidak dievaluasi.** Klaim "mengurangi beban kognitif/split-attention", "tanpa stigma", "mulus", "ergonomis ≥ 44 px" tanpa pengukuran (SUS/NASA-TLX, uji kebergunaan kecil dengan guru, audit aksesibilitas). Satu sesi uji dengan 2–3 guru TKJ sudah menaikkan nilai artikel besar.

**P7 [Minor] Representativitas perangkat.** Laptop Ryzen 7 / 16 GB disebut "representatif laboratorium sekolah" tanpa survei. Pendahuluan sendiri menyebut rasio komputer 1:2 dan RAM 4,5 GB untuk model; spesifikasi riil SMKN 4 Bandung (dan fakta bahwa lab sering 4–8 GB RAM) perlu dicantumkan. Rasio "1:2" (Pendahuluan) vs "1:1" (Agenda lanjutan) perlu dijelaskan (setengah kelas per zona?).

---

## Seat 5 — Devil's Advocate

**Counter-argument terkuat.** Seluruh bab konkurensi menyelesaikan masalah yang dibuat sendiri oleh pilihan desain. Menurut §3.4, prompt T2 hanya fungsi dari (KC, level, teks soal), `temperature = 0`, tidak ada riwayat/jawaban siswa. Artinya keluaran adalah **fungsi deterministik dari (butir, level)** — korpus tertutup 180 butir × 3 level = 540 petunjuk. Seluruh petunjuk dapat dibangkitkan **sekali, luring**, memakai model terbaik (cloud, tanpa batas latensi), ditinjau guru (human-in-the-loop, yang sudah ada di T1), lalu dilayani statis dalam < 50 ms. Hasilnya: latensi nol, tanpa beban CPU/RAM 4,5 GB, tanpa risiko PII keluar saat runtime, tanpa risiko kebocoran jawaban saat runtime (kualitas ditinjau), tanpa kebutuhan Poisson, tanpa multi-provider. Arsitektur runtime LLM, `SecureLLMClient`, lima lapis pertahanan, dan uji konkurensi menjadi tidak perlu. Naskah tidak pernah menjawab mengapa generasi *real-time* diperlukan (tidak ada adaptasi terhadap kesalahan siswa).

Isu CRITICAL DA:

- **[DA-CRITICAL-1] Nilai tambah runtime LLM tidak ditunjukkan.** Bukti pedagogis hanya 3 contoh pilihan penulis; pada k ≥ 4 *100%* respons berasal dari bank statis (Tabel 4), sehingga di kondisi beban inilah LLM nol kontribusi. *Rekomendasi:* tambahkan baseline "540 petunjuk pra-generasi + ulasan guru" dan bandingkan kualitas, biaya, risiko; atau tunjukkan adaptasi per-siswa (mis. melibatkan jawaban salah/alasan yang dipilih) yang membenarkan inferensi runtime. [Adjudikasi sintetis: **valid** — memblokir klaim "kebaruan arsitektur", tidak memblokir publikasi sebagai studi kelayakan.]
- **[DA-CRITICAL-2] Mesin "kognitif" tidak punya bukti bahwa ia mengukur kognisi.** Kecepatan 0,18 ms bukan kontribusi (operasi float sederhana); hal yang berarti — apakah m mendekati penguasaan sebenarnya — tidak diuji. Parameter dipilih agar "2 vs 3 butir" terlihat rapi (sirkular), tabel pemilihannya mengandung kesalahan hitung, dan simulasinya melanggar aturan selektornya sendiri. [**valid.**]
- **[DA-CRITICAL-3] "Zero outage" bersifat tautologis.** Fallback menjamin *ada respons*, bukan layanan yang bermanfaat; di k ≥ 4 sistem sepenuhnya mundur ke 36 petunjuk generik per KC. Definisi "outage" menyingkirkan kegagalan kualitas. Dan itu belum diukur dengan benar (M1). [**valid.**]

Isu MAJOR DA:
- Cherry-picking: contoh Tabel 7 bersih; tak ada contoh gagal/bocor/halusinasi. Pengujian 41 unit adalah pengujian *kode yang ditulis penulis untuk kasus yang dipilih penulis*.
- Generalisasi berlebih: dari 1 laptop → "tangguh, siap diimplementasikan"; dari 34 siswa fiktif → "mencukupi > 99,9% pola kedatangan".
- Titik buta pemangku kepentingan: guru (beban kurasi 180 butir, kepercayaan pada rekomendasi), siswa (kecemasan *surveillance* dasbor, privasi antar-siswa), pihak sekolah/Dinas (DPA, tata kelola, pemeliharaan jangka panjang; siapa mengurus Ollama/kunci API/proxy?).
- Jalur alternatif tidak dibahas: model lebih kecil (1.5B), *streaming* (TTFT < 1 s walau latensi penuh 4,7 s; guard bisa jalan sesudahnya atau pada kalimat), `num_parallel`, pengendalian antrean/pembatasan laju per kelas, server sekolah/mini-PC bersama bukan laptop guru.
- Uji "So what?": jika artikel ini lolos, apa yang pembaca pelajari? Pola fallback — nilai nyata tapi umum. Perlu rumusan pengetahuan desain (design principles) yang dapat ditransfer.

Pengamatan non-cacat: arsitektur terpisah rapi (L1–L3), keterbukaan kode, keterbatasan ditulis jelas.

---

## Editorial Decision Letter

**Keputusan: MAJOR REVISION** (menurut standar jurnal terakreditasi nasional; tidak layak Accept; belum Reject karena artefak nyata, lingkup jujur, dan perbaikan dapat dilakukan tanpa data lapangan).

**Konsensus (≥ 4 seat sepakat):**
1. Klaim melampaui bukti (100%, zero outage, patuh privasi, siap implementasi).
2. Evaluasi konkurensi: n kecil, satu run, tanpa CI, SLA pasca-ukur, fallback tidak diukur, k=2 dilabeli "optimal" meski p95 > SLA, Poisson tak sah.
3. Model kognitif tidak divalidasi (tidak ada baseline BKT/Elo, tidak ada simulasi ground-truth); Tabel 3 salah hitung dan tak konsisten dengan ZPD.
4. "RAG"/"Agen"/"Zero-PII" label tidak sesuai isi.
5. Tidak ada validasi pakar (DAG, TOLT, bank soal, petunjuk) dan tidak ada evaluasi guru.

**Perbedaan pendapat:** EIC menganggap artikel layak terbit sebagai studi kelayakan setelah *reframing*; DA menilai kontribusi arsitektur tidak terbukti dibanding pra-generasi petunjuk. Arbitrase: DA-CRITICAL-1 divalidasi sebagian — penulis dapat mempertahankan arsitektur runtime hanya bila memberi argumen/bukti nilai tambah per-siswa, atau mengubah posisi artikel menjadi "dua mode (pra-generasi vs runtime) beserta trade-off".

**Provenance panel:** semua lima seat dijalankan oleh satu model dalam satu sesi; persona terpisah ≠ error independen. Cross-model: tidak aktif. Pemeriksaan DOI Crossref saya jalankan sendiri (lihat Lampiran).

---

## Revision Roadmap (prioritas)

**P0 — wajib sebelum submit**
1. Koreksi Tabel 3 (baris α₀=0,40 mandiri → 1 butir, m₁=0,670) dan teks §3.2 poin 2; selaraskan simulasi dengan selector (atau jelaskan perilaku saat tak ada kandidat ZPD, mis. m < 0,379).
2. Turunkan klaim: hapus "membuktikan/100%/zero outage/patuh privasi/tanpa regresi visual/siap". Ubah judul/abstrak: "studi kelayakan teknis"; "Zero-PII" → "redaksi PII keluar"; hapus "RAG-KT" bila tak ada retrieval.
3. **Ukur ulang konkurensi:** ≥ 5 ulangan, ≥ 100 permintaan/kondisi, warm-up, laporkan konfigurasi Ollama penuh, CI, throughput; jalankan **timeout 3,0 s sungguhan** dengan fallback nyata; tambahkan k=3; tambahkan uji kegagalan (putus jaringan/429/kunci salah).
4. Ganti Poisson dengan simulasi kelas berkorelasi atau hapus klaim ">99,9%".
5. **Simulasi validitas L3** (siswa sintetis) vs BKT/Elo/baseline acak.
6. Verifikasi referensi: DOI **Komalasari dkk. (2023)** dan **Nurbaeti dkk. (2024)** tidak terdaftar di Crossref (404). Cari sumber asli (judul/jurnal/DOI) atau ganti; jangan kutip yang tidak dapat dilacak. Perbaiki tahun Xia dkk. (Crossref: 2025). Ganti sitasi yang tidak mendukung klaim (Xia, Jadhav, Wing, Tato & Nkambou).
7. Nyatakan data Gambar 4–5 sebagai sintetis; selaraskan dengan deklarasi etika.

**P1 — sangat dianjurkan**
8. Tabel sisi DAG (induk→anak) + validasi 2–3 pakar (CVI/kappa); jelaskan fungsi TOLT atau keluarkan dari kontribusi; sesuaikan klaim "kabel & nirkabel".
9. Dokumentasi bank soal (penyusun, validasi, d, embedding model); uraikan peran pgvector.
10. Evaluasi kualitas petunjuk: ≥ 60 petunjuk, rubrik, 2–3 penilai, uji adversarial leakage termasuk 36 petunjuk statis; sebutkan model/penyedia di Tabel 7.
11. Model ancaman + pengujian PII dengan korpus berlabel (recall/FN + CI); jelaskan penanganan nama; ringkas aspek UU PDP dengan pasal terverifikasi; bahas status hukum `9router`/API luar negeri.
12. Bandingkan dengan baseline "540 petunjuk pra-generasi + tinjau guru"; bahas streaming, model lebih kecil, `num_parallel`.
13. Uji end-to-end 34 klien (API+DB+WebSocket) saat CPU dibebani inferensi.
14. Uji kebergunaan kecil dengan guru TKJ; ukur SUS.

**P2 — kerapian**
15. Lengkapi aktivitas DSR (6 tahap, termasuk Communication) dan kriteria evaluasi artefak; rumuskan design principles.
16. Persingkat abstrak (≤ 250 kata), kurangi identifier kode; seragamkan angka (max_tokens 120/150; 0,65–0,70; mode 3 vs 4; 8-thread vs 8-core/16-thread; target < 1/10/50 ms; RAM 4,3 vs 4,5 GB).
17. Definisikan Station Rotation/Zona A–B di Pendahuluan; lengkapi placeholder penulis/email; siapkan versi anonim bila blind-review; perjelas istilah CRediT.
18. Tabel 6: tandai latensi cloud sebagai estimasi atau ukur. Tabel 5: perjelas apa yang diukur `psutil`.

---

## Lampiran — Pemeriksaan yang saya lakukan

- Hitung ulang Tabel 3 (semua 5 baris α₀): 9 dari 10 sel (jumlah butir) benar; **1 salah** (α₀=0,40 mandiri).
- Hitung ulang Poisson §3.3: μ ≈ 0,0982; P(X≥3) ≈ 1,46×10⁻⁴ (angka naskah benar; asumsi yang bermasalah).
- Hitung CI Wilson 95%: 10/10 → ≥ 72%; 10/12 → 55–95%.
- Throughput agregat dari Tabel 4: 0,57 / 0,76 / 0,84 / 0,90 req/s.
- Jumlah uji Tabel 8: 6+4+7+3+3+8+10 = 41 (konsisten).
- DOI Crossref: 13 dari 15 terselesaikan dan judul cocok; **2 gagal (404):** `10.17509/invotec.v19i2.56412` (Komalasari), `10.29408/edumatic.v8i1.21890` (Nurbaeti). Dua DOI arXiv tidak diperiksa lewat Crossref. Tidak memverifikasi isi artikel (hanya keberadaan DOI + judul).
- Tidak diverifikasi: nama model `ag/gemini-3.8-flash`, angka latensi/RAM yang diklaim (bukan hasil saya), isi repositori GitHub, isi gambar (tidak dilihat; `figures/` tidak ada di folder yang saya baca).
