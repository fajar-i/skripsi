# RANGKUMAN EKSEKUTIF SKRIPSI: PROYEK LOGITRACE (UPI 2026)
**Dokumen Konteks Penuh untuk AI Sesi Baru & Panduan Komunikasi Dosen Pembimbing**

---

## 1. IDENTITAS PENELITI DAN PROYEK

* **Nama Peneliti:** Fajari Arkan Fadhlurrahman
* **NIM:** 2304794
* **Program Studi:** Pendidikan Ilmu Komputer (S-1)
* **Departemen / Fakultas:** Departemen Pendidikan Ilmu Komputer, FPMIPA, Universitas Pendidikan Indonesia (UPI)
* **Tahun Akademik:** 2026 (Semester 7)
* **Judul Skripsi:**  
  > *"Pengembangan Web Evaluasi Formatif Adaptif Berbasis Knowledge Tracing dan Retrieval-Augmented Generation (LogiTrace) dalam Pembelajaran Station Rotation untuk Meningkatkan Logical Thinking Siswa SMK"*
* **Sekolah Mitra & Subjek:** SMKN 4 Bandung, Kelas XI Konsentrasi Keahlian Teknik Komputer dan Jaringan (TKJ) 1.
* **Jumlah Subjek:** Sensus 34 Siswa (1 rombongan belajar penuh).
* **Guru Mitra:** Bapak Yofi Fikri Islami Anshary, S.Pd. (Guru Mata Pelajaran Kejuruan TKJ).
* **Materi Domain:** Teknologi Jaringan Kabel dan Nirkabel (Khususnya Jaringan Nirkabel / WLAN, Topologi, SSID, Keamanan, dan Troubleshooting ICMP).
* **Status Naskah Saat Ini:** Bab I, Bab II, Bab III, Daftar Pustaka (APA 7th), dan 5 Lampiran telah selesai disusun dalam format Markdown (`proposal_skripsi_bab_1_2_3.md`) dan Microsoft Word resmi (`proposal_skripsi_bab_1_2_3.docx`).

---

## 2. PANDUAN PENJELASAN KE DOSEN PEMBIMBING (ELEVATOR PITCH)

Jika dosen pembimbing bertanya: *"Bagaimana perubahan judul proposal Anda dan mengapa konsep ini jauh lebih kuat dari judul lama?"*, jelaskan dengan 4 poin inti berikut:

1. **Seluruh Metodologi Proposal Lama Dipertahankan Penuh:**  
   Alur R&D model ADDIE/Borg & Gall, instrumen validitas LORI 2.0, angket usabilitas SUS, desain pra-eksperimen *One-Group Pretest-Posttest*, kalkulasi daya pembeda & reliabilitas CTT, serta analisis statistik $N\text{-Gain}$ dan uji parametrik/non-parametrik dari proposal lama yang telah disetujui dosen **tetap dipakai 100%**.
2. **Berpijak pada Masalah Riil Lab SMKN 4 Bandung:**  
   Observasi menunjukkan kelas XI TKJ 1 memiliki tingkat remedial tertinggi pada materi jaringan nirkabel. Masalah siswa bukan pada pemasangan fisik kabel, melainkan kelemahan **berpikir logis (*Logical Thinking*)** saat menganalisis kegagalan koneksi (*troubleshooting* ICMP/Ping). Ditambah lagi, rasio komputer lab adalah **1 PC : 2 siswa**, yang memicu fenomena siswa dominan vs siswa pasif.
3. **Didukung Landasan SLR Empiris 21 Artikel Scopus (2021–2026):**  
   Berdasarkan tinjauan sistematis, model *Deep Knowledge Tracing* (DKT) monolitik konvensional berbasis jaringan saraf (RNN/LSTM) **pasti gagal (*overfitting* parah)** jika dilatih pada kelas kecil (34 siswa SMK hanya menghasilkan ~3.000 log interaksi, menghasilkan rasio timpang 440 parameter per data). Belum pernah ada penelitian DKT yang mengukur penalaran logis pada kurikulum kejuruan jaringan komputer.
4. **Solusi Inovatif "LogiTrace" + "Station Rotation":**  
   * **LogiTrace (*Training-Free Knowledge Tracing*):** Menggeser kebutuhan data dari korpus perilaku siswa (yang tidak ada) ke korpus konten kurikulum resmi (CP/ATP pemerintah). Pelacakan status penguasaan kognitif dilakukan dengan **aturan deterministik transparan (< 1 ms)** dipadukan dengan LLM lokal beku (*frozen*) untuk indeks semantik teks soal dan bantuan Sokratik ber-*guardrail* anti-bocor (*Guiding, Not Solving*).
   * **Station Rotation 3 Stasiun + Device-Purpose Split:** Mengatasi rasio lab 1:2. Siswa berotasi di 3 stasiun: Stasiun 1 (Teori/Fisik), Stasiun 2 (Kuis Adaptif LogiTrace di **HP pribadi masing-masing siswa** sehingga pelacakan 100% individual murni), dan Stasiun 3 (Praktik Simulasi Cisco Packet Tracer di **PC Lab**).

---

## 3. LATAR BELAKANG & TEMUAN SYSTEMATIC LITERATURE REVIEW (SLR)

Penelitian ini didasari oleh korpus **21 artikel Scopus (2021–2026)** mengenai *Knowledge Tracing* (KT), penalaran logis, dan *Intelligent Tutoring Systems* (ITS) dari naskah SLR penulis.

### Tiga Kesenjangan Kritis (Critical Research Gaps):
1. **Kegagalan Matematis DKT pada Data Terbatas (*Small-Data Regime*):**  
   DKT konvensional membutuhkan $10^5 - 10^6$ interaksi. Pelatihan dari nol (*from scratch*) pada 34 siswa memicu kegagalan prediksi kelas langka ($F_1 = 0{,}0$, Nkambou et al., 2023). Pendekatan transfer generatif mutakhir seperti CLST (Jung et al., 2025) pada data sedikit tetap menuntut korpus luar yang besar.
2. **Kekosongan Konstruk Penalaran Logis di Pendidikan Vokasi:**  
   Mayoritas riset KT dunia terkonsentrasi pada matematika (ASSISTments) dan pemrograman umum. Dari 21 artikel Scopus terkini, hanya 2 studi yang meneliti logika formal (Nkambou et al., 2023; Tato & Nkambou, 2022 pada ITS Logic-Muse), dan **tidak ada satu pun artikel yang meneliti penalaran logis pada kurikulum kejuruan teknik komputer dan jaringan (TKJ)**. Tidak ada dataset perilaku publik untuk materi jaringan SMK.
3. **Kelemahan Pedagogis LLM Interaktif:**  
   LLM umum kerap bertindak sebagai penjawab reaktif instan (*instant solvers*) yang merusak pergulatan kognitif produktif siswa (*productive struggle*, Wang et al., 2026).

### Pergeseran Paradigma (The Paradigm Shift):
> *"Kebutuhan data digeser dari korpus perilaku log interaksi siswa (yang tidak tersedia pada domain baru) menuju korpus konten kurikulum (yang dapat dispesifikasikan secara terstruktur oleh pendidik berbasis Capaian Pembelajaran pemerintah)."*

---

## 4. SPESIFIKASI ARSITEKTUR TIGA LAPIS SISTEM LOGITRACE

Sistem LogiTrace dibangun tanpa melatih model saraf dari nol (*Training-Free*), menggunakan tiga lapisan:

```
┌────────────────────────────────────────────────────────────────────────┐
│ LAPISAN 1 (L1) - BASIS PENGETAHUAN KURIKULUM (KNOWLEDGE BASE)          │
│ • 12 Knowledge Components (KC) diekstraksi resmi dari CP/ATP TKJ       │
│ • Directed Acyclic Graph (DAG) hirarki prasyarat (Nkambou et al. 2023) │
│ • Rubrik 5 Dimensi TOLT & 24 Contoh Pengerjaan (Worked-Examples)       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Konteks Kurikulum
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ LAPISAN 2 (L2) - INDEKS BUTIR & PELABELAN SEMANTIK                     │
│ • Ekstraksi teks soal & diagnosis miskonsepsi via LLM Lokal Beku       │
│ • Pelabelan ganda KC x TOLT otomatis (Yang et al. & Shao et al. 2025)  │
│ • Bank Butir 180 Soal Kuis Adaptif + 10 Butir Tes TOLT + 6 NEDV       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Parameter Butir (d, KC, TOLT)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ LAPISAN 3 (L3) - MESIN RUNTIME DETERMINISTIK & AGEN RAG BER-GUARDRAIL   │
│ • Estimasi Penguasaan m_t: Update deterministik (alpha_d, gamma_d,     │
│   beta, peluruhan lupa tau=60 hari) -> runtime < 1 ms tanpa GPU        │
│ • Seleksi Butir Adaptif: Pita ZPD (0.60 <= p_hat <= 0.85) & DAG gating │
│ • Agen RAG Sokratik: Pemicu T1/T2 ("Guiding, Not Solving", Wang 2026)  │
│ • 3 Lapis Guardrail: NLI Entailment, Masking Jawaban, & Verifikasi     │
│ • Dasbor Guru (Pemicu T3): Pemantauan kelas real-time via WebSocket   │
└────────────────────────────────────────────────────────────────────────┘
```

### Formula Matematika Utama di L3:
1. **Prediksi Peluang Sukses ($\hat{p}$):**
   $$\hat{p} = \frac{1}{1 + e^{-k(m_t - d)}}$$
   *(di mana $m_t$ adalah status penguasaan konsep, $d$ adalah tingkat kesulitan butir, dan $k=4$)*.
2. **Pembaruan Status Penguasaan ($m_{t+1}$):**
   * *Jika Benar Mandiri:* $m_{t+1} = \min(1{,}0, \, m_t + \alpha_d (1 - m_t))$
   * *Jika Salah:* $m_{t+1} = \max(0{,}0, \, m_t - \gamma_d \cdot m_t)$
   * *Jika Benar Berbantuan Scaffolding:* $m_{t+1} = m_t + \beta \cdot \alpha_d (1 - m_t)$, dengan faktor diskon $\beta = 0{,}40$.
   * *Peluruhan Lupa Ebbinghaus:* $m(t + \Delta t) = m(t) \cdot e^{-\Delta t / \tau}$, dengan $\tau = 60\text{ hari}$.
3. **Pita Adaptasi ZPD & Prasyarat:**
   Butir soal berikutnya dipilih jika $0{,}60 \le \hat{p} \le 0{,}85$ dan seluruh prasyarat langsung pada graf DAG telah memenuhi ambang batas $m_{\text{prasyarat}} \ge 0{,}60$.

---

## 5. PEMETAAN 12 KNOWLEDGE COMPONENTS (KC) DARI CP/ATP PEMERINTAH

Knowledge Components diturunkan langsung dari **Capaian Pembelajaran (CP) dan Alur Tujuan Pembelajaran (ATP) Kurikulum Merdeka Fase F Konsentrasi Keahlian TKJ** (Mata Pelajaran Teknologi Jaringan Kabel dan Nirkabel):

| Kode KC | Nama Knowledge Component | Indikator Kompetensi Kurikulum | Prasyarat Langsung (DAG) |
| :--- | :--- | :--- | :--- |
| `KC-01` | Karakteristik Frekuensi Nirkabel | Membedakan karakteristik propagasi spektrum 2.4 GHz vs 5 GHz | *(Root / Konsep Dasar)* |
| `KC-02` | Topologi Jaringan Nirkabel | Menganalisis perbedaan mode Ad-Hoc, BSS, dan ESS | *(Root / Konsep Dasar)* |
| `KC-03` | Alokasi Kanal & Interferensi | Menentukan alokasi kanal *non-overlapping* (1, 6, 11) | `KC-01` |
| `KC-04` | Atenuasi Sinyal & Redaman | Menganalisis pengaruh penghalang fisik dan interferensi | `KC-01` |
| `KC-05` | Autentikasi & Keamanan WLAN | Mengonfigurasi protokol enkripsi Open, WPA2-PSK, dan WPA3 | `KC-02` |
| `KC-06` | Pengalamatan IP & DHCP Pool | Menerapkan konfigurasi IP dinamis dan gateway pada AP | `KC-02` |
| `KC-07` | Diagnostik Konektivitas ICMP | Menguji komunikasi *peer-to-peer* dan membaca status *Ping* | `KC-04`, `KC-06` |
| `KC-08` | Logika Subnetting & Gateway | Mendiagnosis anomali kegagalan koneksi akibat beda segmen | `KC-06`, `KC-07` |
| `KC-09` | Kontrol Akses & Keamanan Lanjut | Menerapkan MAC Filtering dan analisis resiko Hidden SSID | `KC-05` |
| `KC-10` | Analisis Roaming & Handover | Mendiagnosis perilaku perpindahan klien di antara beberapa AP | `KC-03`, `KC-04` |
| `KC-11` | Optimasi Bandwidth & Throughput | Menganalisis alokasi bandwidth dan fenomena antrean paket | `KC-07` |
| `KC-12` | Troubleshooting WLAN Komprehensif | Menemukan akar masalah kegagalan konektivitas kompleks | `KC-08`, `KC-09`, `KC-10` |

---

## 6. HAKIKAT LOGICAL THINKING: KERANGKA KERJA TOLT

Kemampuan berpikir logis diukur berdasarkan kerangka kerja terstandar **Test of Logical Thinking (TOLT)** dari Tobin & Capie (1981) yang dioperasionalkan ke domain teknologi jaringan nirkabel:

1. **Penalaran Proporsional (*Proportional Reasoning*):**  
   Perhitungan atenuasi sinyal berbanding terbalik dengan kuadrat jarak ($1/r^2$), pembagian kapasitas throughput per klien, dan kalkulasi subnet IP.
2. **Pengontrolan Variabel (*Controlling Variables*):**  
   Mendiagnosis sumber galat koneksi secara ilmiah dengan mengisolasi satu parameter konfigurasi (misal mengubah kanal frekuensi dengan mempertahankan posisi dan daya pemancar tetap sama).
3. **Penalaran Probabilistik (*Probabilistic Reasoning*):**  
   Analisis risiko tabrakan paket (*packet collision*) dan interferensi pada kanal bersama (*co-channel interference*).
4. **Penalaran Korelasional (*Correlational Reasoning*):**  
   Menghubungkan indikator kekuatan sinyal (RSSI) dan *Signal-to-Noise Ratio* (SNR) dengan stabilitas *latency ICMP* dan persentase *packet loss*.
5. **Penalaran Kombinatorial (*Combinatorial Reasoning*):**  
   Menganalisis permutasi konfigurasi keamanan, mode otentikasi, dan segmentasi VLAN nirkabel untuk memenuhi syarat konektivitas multi-pengguna.

---

## 7. MODEL PEMBELAJARAN STATION ROTATION DI RUANG KELAS

Model ini memecah 34 siswa menjadi 3 kelompok heterogen yang berputar secara terstruktur dalam 4 sesi tatap muka:

```
            ┌──────────────────────────────────────────────┐
            │        STASIUN 1: PEMBELAJARAN FISIK         │
            │  (Investigasi Perangkat Keras AP & Teori)    │
            └──────────────────────┬───────────────────────┘
                                   │ Rotasi (25-30 menit)
                                   ▼
┌──────────────────────────────────────────────┐      ┌──────────────────────────────────────────────┐
│       STASIUN 3: SIMULASI VIRTUAL            │      │        STASIUN 2: EVALUASI LOGITRACE         │
│ (Cisco Packet Tracer di PC Lab - Rasio 1:2)  │◄─────┤ (Kuis Adaptif Sokratik di HP Pribadi Siswa)  │
└──────────────────────────────────────────────┘      └──────────────────────────────────────────────┘
```

* **Device-Purpose Split:**  
  * **Smartphone Pribadi Siswa:** Khusus digunakan di Stasiun 2 untuk mengakses LogiTrace. Tiap siswa login mandiri sehingga data pelacakan penguasaan pengetahuan $m_t$ murni individual tanpa terdistorsi rekan kelompok.
  * **Komputer PC Lab:** Dikhususkan untuk Stasiun 3 untuk menjalankan simulasi topologi jaringan Cisco Packet Tracer yang membutuhkan layar lebar dan tetikus. Karena hanya 1/3 rombel yang berada di stasiun ini pada satu waktu (~11 siswa), rasio 1:2 teratasi dan setiap siswa bisa memegang PC secara leluasa.

---

## 8. METODOLOGI PENELITIAN & RENCANA EVALUASI 6 JALUR (E1–E6)

* **Model Pengembangan:** ADDIE (Branch, 2009) yang diselaraskan dengan Borg & Gall (Judijanto et al., 2024).
* **Desain Eksperimen:** *One-Group Pretest-Posttest Design* (Sugiyono, 2019; Creswell, 2014) dengan instrumen tes paralel (Form A dan Form B).
* **Kontrol Validitas Internal Ketat (NEDV):**  
  Menyisipkan **6 butir kontrol Non-Equivalent Dependent Variable (NEDV)** bertopik *Teori Antrean M/M/1* yang membutuhkan penalaran analitis setara namun materinya tidak diajarkan sama sekali. Kriteria keberhasilan validitas internal: peningkatan nilai $N\text{-Gain}$ butir NEDV harus mendekati nol ($g_{\text{NEDV}} \approx 0$), membuktikan peningkatan skor tes murni akibat sistem LogiTrace, bukan faktor kematangan usia atau efek latihan tes (*testing effect*).
* **Sampel:** Sensus 34 siswa kelas XI TKJ 1 SMKN 4 Bandung ($d_z \approx 0{,}48$ pada power $1-\beta = 0{,}80, \alpha = 0{,}05$).

### Struktur Evaluasi Komprehensif Enam Jalur:
* **E1 (Validitas Isi & Pemetaan Semantik):** Aiken's $V \ge 0{,}80$ dan kesepakatan Cohen's $\kappa$ antara pelabelan LLM lokal dan konsensus pakar.
* **E2 (Evaluasi Mutu Scaffolding RAG):** *Intraclass Correlation Coefficient* (ICC) $> 0{,}75$ pada rubrik kesesuaian bimbingan Sokratik.
* **E3 (Akurasi Prediksi KT Pasca-Kalibrasi):** Mengukur AUC, RMSE, dan stabilitas transisi status penguasaan.
* **E4 (Keandalan Model & Guardrail Anti-Leakage):** Tingkat kebocoran kunci jawaban pada petunjuk Sokratik wajib $\le 1\%$.
* **E5 (Kualitas Media & Usabilitas):** Validasi ahli media LORI 2.0 (target $\ge 80\%$) dan kuesioner usabilitas siswa System Usability Scale / SUS (target $\ge 70$, kategori *Good/Acceptable*).
* **E6 (Dampak Belajar & Keseimbangan Dimensi):** Perhitungan $N\text{-Gain}$ Hake (1999), uji beda *Paired t-test* / Wilcoxon, dan uji kesetaraan peningkatan antar-dimensi via *One-Way ANOVA*.
* **Treatment Fidelity Index:** Pemantauan kesetiaan perlakuan sintaks *Station Rotation* dengan target keterlaksanaan $\ge 85\%$.

---

## 9. INVENTARIS BERKAS PROYEK DI WORKSPACE

Semua berkas proyek tersimpan terstruktur di folder `c:\kuliah\semester_7\skripsi\proposal\`:

1. `proposal_skripsi_bab_1_2_3.md`: Naskah akademik master Bab I, II, III, Daftar Pustaka lengkap, dan 5 Lampiran instrumen.
2. `proposal_skripsi_bab_1_2_3.docx`: Berkas naskah resmi Microsoft Word siap cetak / kirim ke dosen pembimbing (Standar Pedoman Karya Ilmiah UPI A4, Margin 4-3-3-3 cm, Times New Roman 12pt, Tabel rapi).
3. `todolist_skripsi_logitrace.html`: Aplikasi to-do list & roadmap interaktif mandiri (*single-file* HTML) untuk melacak eksekusi penelitian secara offline dengan *auto-save* dan *backup JSON*.
4. `rangkuman_skripsi_fajari_logitrace.md`: Berkas rangkuman eksekutif ini untuk transfer konteks cepat ke AI sesi berikutnya.
5. Dokumen Master Pendukung:
   * `..\master\desain-final-rag-kt-logitrace.md`: Cetak biru detail spesifikasi matematis, basis data, dan aturan transisi L1/L2/L3.
   * `..\master\tanya-jawab-penguji-rag-kt.md`: Panduan tanya-jawab dan pertahanan sidang proposal menghadapi dewan penguji.
   * `naskah_slr_lengkap(4).md`: Naskah kajian sistematis literatur 21 artikel Scopus (2021–2026).
   * `proposal_lama.md`: Naskah proposal terdahulu yang rujukan metodologinya telah disetujui dosen.

---
*Dokumen ini disusun untuk memastikan kontinuitas konteks akademik dan teknis penelitian skripsi Fajari Arkan Fadhlurrahman (NIM 2304794).*
