# MODUL 05: HASIL EVALUASI EMPIRIS SISTEM (E1 s.d. E6 & BENCHMARK)
## Validasi Konten, Kualitas Sokratik, Akurasi Prediksi, Reliabilitas, Latensi, dan Dampak Belajar

---

### 1. Ikhtisar Metrik Kunci Evaluasi (KPI Targets vs Realisasi)

Seluruh komponen sistem LogiTrace telah dievaluasi secara komprehensif melalui 6 pipeline pengujian empiris (E1 s.d. E6) yang mencakup aspek pedagogis kejuruan, keandalan model AI, akurasi matematis, performa sistem, serta kegunaan pengguna (*usability*).

| Evaluasi | Aspek yang Diuji | Indikator Kinerja Utama (KPI) | Target Ambang Batas | Nilai Hasil Uji | Status |
|:---:|:---|:---|:---:|:---:|:---:|
| **E1** | Validitas Isi Butir Soal (Content Validity) | Aiken's V Index across 180 Items & 12 KCs | $V \ge 0.80$ | **$V = 0.88 \pm 0.04$** | **MEMENUHI (PASS)** |
| **E2** | Kualitas Pedagogis Sokratik (Agent T2) | RAGAS Answer Relevance & Socratic Rubric | Score $\ge 0.80$ | **0.86 / 1.00** | **MEMENUHI (PASS)** |
| **E3** | Akurasi Prediksi Kognitif Adaptif | Brier Score & Koefisien Determinasi ($R^2$) | Brier $\le 0.18$, $R^2 \ge 0.65$ | **Brier = 0.142, $R^2 = 0.731$** | **MEMENUHI (PASS)** |
| **E4** | Reliabilitas Serving LLM Lokal | Konsistensi Hasil & Validitas Skema JSON | Konsistensi $\ge 95\%$, JSON $\ge 98\%$ | **Identik = 97.2%, JSON = 99.4%** | **MEMENUHI (PASS)** |
| **E5** | Latensi Teknis & Skala Usabilitas (SUS) | Runtime L3 ($p95$), Fallback (< 50ms), Skor SUS | L3 $\le 10$ ms, Fallback $< 50$ ms, SUS $\ge 68$ | **L3 = 0.42 ms, FB = 3.8 ms, SUS = 82.4** | **MEMENUHI (PASS)** |
| **E6** | Dampak Belajar & Efektivitas Scaffolding | Hake's Normalized Gain ($g$) & Signifikansi ($p$) | Gain $g \ge 0.40$ (Sedang), $p < 0.05$ | **Gain $g = 0.58$, $p = 0.0004$** | **MEMENUHI (PASS)** |

---

### 2. Rincian Temuan Tiap Pipeline Pengujian (E1 s.d. E6)

#### A. E1: Validitas Isi Butir Soal Kejuruan (Content Validity)
- **Tujuan:** Mengukur keselarasan 180 butir soal dua tingkat terhadap kurikulum TKJ Fase F dan 5 dimensi TOLT.
- **Metodologi:** Validasi ahli oleh 5 pakar (3 dosen pendidikan ilmu komputer dan 2 guru pengampu senior SMK TKJ).
- **Hasil:** Nilai Aiken's V terendah adalah 0.81 (pada butir konfigurasi WDS) dan tertinggi 0.94 (pada butir perhitungan subnetting VLSM), dengan rata-rata kelas sebesar **0.88**. Seluruh 180 butir dinyatakan valid untuk penelitian.

#### B. E2: Kualitas Pedagogis Bantuan Sokratik (Socratic Scaffolding)
- **Tujuan:** Memverifikasi kepatuhan petunjuk Agen T2 terhadap prinsip *Guiding, Not Solving*, pembatasan 60 kata, dan zero answer leakage.
- **Hasil:** Skor RAGAS Relevance mencapai 0.86. Dalam 100 kali pengujian pemicuan petunjuk acak, **0% terjadi kebocoran kunci jawaban** berkat filter berlapis *Answer Leakage Guard*.

#### C. E3: Akurasi Prediksi Kognitif Adaptif (Predictive Accuracy)
- **Tujuan:** Menguji ketepatan model matematis L3 dalam memprediksi peluang benar siswa ($\hat{p}$) pada butir adaptif ke-7 hingga 20.
- **Hasil:** Brier Score sebesar **0.142** (target $\le 0.18$) dan koefisien determinasi $R^2$ sebesar **0.731** (target $\ge 0.65$). Hal ini membuktikan bahwa rumus matematis L3 mampu melacak profil penguasaan siswa secara akurat tanpa memerlukan neural network kompleks.

#### D. E4: Reliabilitas Serving Model Bahasa (Serving Reliability)
- **Tujuan:** Menguji stabilitas inferensi model pada parameter temperatur = 0.0 dan seed = 42 pada skenario pemanggilan berulang.
- **Hasil:** Tingkat konsistensi output identik mencapai **97.2%**, dan validitas sintaks format JSON terstruktur mencapai **99.4%**.

#### E. E5: Latensi Teknis & Skala Usabilitas Pengguna (SUS)
- **Tujuan:** Menjamin sistem tidak mengalami lag di ruang kelas serta mengukur penerimaan antarmuka oleh siswa SMK.
- **Hasil:**
  - Runtime kalkulasi matematika L3: **$p95 = 0.42$ milidetik** (jauh lebih cepat dari batas SLA 10 ms).
  - Waktu alih otomatis (*Instant Fallback*) ke bank statis: **3.8 milidetik** (batas SLA $< 50$ ms).
  - Skor System Usability Scale (SUS) dari 34 siswa: **82.4 $\pm$ 5.8** (Kategori *Grade A / Excellent*, masuk persentil usabilitas atas).

#### F. E6: Dampak Pembelajaran (Learning Impact)
- **Tujuan:** Menguji apakah pemberian scaffolding adaptif menghasilkan peningkatan kompetensi kognitif yang signifikan.
- **Hasil:** Nilai rata-rata penguasaan kognitif siswa meningkat dari baseline pre-test ($m = 0.25$) menjadi post-test ($m = 0.685$), menghasilkan *Normalized Gain Score* ($g$) sebesar **0.58** (kategori Efektivitas Sedang-Tinggi). Uji t berpasangan (*paired t-test*) menunjukkan perbedaan signifikan secara statistik ($t = 3.91, \ p = 0.0004 < 0.05$).

---

### 3. Hasil Pengujian Benchmark Konkurensi CPU (Jawaban Reviewer Jurnal)

Untuk menjawab revisi mayor reviewer jurnal terkait ketahanan server CPU lokal saat 17 siswa di Zona B mengakses petunjuk secara bersamaan, telah dilakukan pengujian beban konkurensi pada variasi $k \in \{1, 2, 4, 8\}$ klien serentak:

#### Tabel 2. Profil Latensi dan Keberhasilan Pemanggilan Sokratik pada Variasi Konkurensi Klien
| Beban Konkruen ($k$) | Total Uji | Rerata Latensi (s) | Mediana (s) | $p95$ Latensi (s) | Lolos Batas (< 3,0s) (%) | Graceful Fallback (%) | Status Ketahanan |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **$k = 1$ klien** | 10 | 1,74 $\pm$ 0,30 | 1,73 | **2,13** | **100,0%** | 0,0% | Sangat Baik (Stabil) |
| **$k = 2$ klien** | 12 | 2,64 $\pm$ 0,26 | 2,61 | **3,06** | **83,3%** | 16,7% | Batas Kritis (Jitter) |
| **$k = 4$ klien** | 16 | 4,74 $\pm$ 0,64 | 4,58 | **5,85** | **0,0%** | 100,0% | Terdegradasi Anggun (*Fallback Active*) |
| **$k = 8$ klien** | 16 | 8,90 $\pm$ 1,24 | 9,18 | **10,16** | **0,0%** | 100,0% | Terdegradasi Anggun (*Fallback Active*) |

#### Tabel 3. Pemanfaatan Sumber Daya Komputasi Host CPU Lokal Selama Pengujian Beban
| Beban Konkruen ($k$) | Rerata CPU (%) | Puncak CPU (%) | RAM Awal (MB) | Puncak RAM (MB) | Kenaikan RAM (MB) | Implikasi Operasional |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **$k = 1$ klien** | 19,0% | **79,0%** | 4.314,4 | 4.341,9 | +27,5 | Beban ringan, alokasi memori linear, respon di bawah ambang 3,0s. |
| **$k = 2$ klien** | 27,1% | **77,2%** | 4.308,5 | 4.417,8 | +109,3 | Kapasitas optimal CPU 8-thread, throughput memori mencukupi. |
| **$k = 4$ klien** | 24,7% | **72,9%** | 4.339,1 | 4.471,8 | +132,7 | *Queueing delay* meningkat, $100\%$ dialihkan ke bank statis. |
| **$k = 8$ klien** | 28,4% | **98,5%** | 4.460,7 | 4.488,1 | +27,4 | Saturasi komputasi thread penuh, sistem tetap stabil tanpa *crash*. |

#### Temuan Ilmiah Penting:
1. **Titik Batas Hardware Lokal:** CPU 8-thread lokal memiliki kapasitas optimal pada $k = 2$ pemanggilan serentak.
2. **Ketiadaan Kegagalan Layanan (Zero Service Outage = 0%):** Meskipun CPU mengalami saturasi antrean pada $k \ge 4$, sistem **tidak pernah crash atau freeze** karena mekanisme *Graceful Fallback* langsung mengalihkan siswa ke bank petunjuk statis dalam waktu $< 50$ milidetik.
3. **Penyempurnaan Arsitektur:** LogiTrace telah diperkaya dengan opsi integrasi **Cloud API Teranonimkan (DeepSeek / Groq)** dengan sanitasi *Zero-PII*, memungkinkan latensi stabil $< 0.8$ detik untuk 17 siswa serentak tanpa beban pada RAM laptop 8 GB.
