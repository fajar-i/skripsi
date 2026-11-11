# 📝 WRITING PLAN: SYSTEMATIC LITERATURE REVIEW (SLR)
# Deep Knowledge Tracing untuk Penalaran Logis dan Computational Thinking dalam Pembelajaran Adaptif (2021–2026)

---

## 📌 1. Paper Configuration Record (Spesifikasi Naskah)

* **Judul Naskah (Tentatif - Dwibahasa):**
  * *Bahasa Indonesia:* **Tinjauan Sistematis Deep Knowledge Tracing untuk Pemodelan Penalaran Logis dan Berpikir Komputasional dalam Lingkungan Pembelajaran Adaptif (2021–2026)**
  * *English:* **A Systematic Review of Deep Knowledge Tracing for Modeling Logical Reasoning and Computational Thinking in Adaptive Learning Environments (2021–2026)**
* **Jenis Naskah:** Systematic Literature Review (SLR) berbasis Pedoman **PRISMA 2020** (*Preferred Reporting Items for Systematic Reviews and Meta-Analyses*).
* **Target Publikasi:** Jurnal Ilmiah Nasional Terakreditasi **SINTA 3** (Rumpun Pendidikan Ilmu Komputer, Pembelajaran Digital, atau Teknologi Informasi).
* **Format Gaya Selingkung / Sitasi:** APA 7th Edition (*American Psychological Association*) / Mendeley-ready.
* **Target Alokasi Kata Total:** 5.000 – 7.000 kata (eksklusif daftar pustaka).
* **Jumlah Literatur Terinklusi:** **21 artikel** jurnal dan prosiding internasional bereputasi (Scopus indexed) dengan ketersediaan *full-text PDF*.

---

## 🎯 2. Research Questions (Pertanyaan Penelitian)

Penyusunan sintesis literatur akan diarahkan secara tegas oleh 3 Pertanyaan Penelitian (*Research Questions / RQs*):

* **RQ1 (Evolusi Arsitektur & Integrasi LLM):**  
  *Bagaimana lintasan perkembangan arsitektur Deep Knowledge Tracing (DKT)—mulai dari model recurrent tradisional (LSTM/GRU), model berbasis graf (GNN/Hypergraph), hingga integrasi Large Language Models (LLM)—dalam merepresentasikan proses penalaran logis siswa?*
* **RQ2 (Pemodelan Kognitif, Konteks Tugas, & Afektif):**  
  *Bagaimana penelitian terkini mengintegrasikan kompleksitas tugas (tingkat kesulitan kode/soal, dependensi konsep bertingkat) serta dimensi afektif/psikologis siswa ke dalam ruang status pengetahuan (knowledge states)?*
* **RQ3 (Karakteristik Dataset, Metrik Evaluasi, & Efektivitas Intervensi ITS):**  
  *Apa saja dataset benchmark dan metrik performa (AUC, ACC, RMSE) yang dominan digunakan untuk memvalidasi model penalaran, serta bagaimana model tersebut diwujudkan dalam bentuk intervensi pedagogis adaptif (Intelligent Tutoring Systems)?*

---

## 📐 3. Struktur Bab & Alokasi Target Kata

```
Total Target: ~5.500 - 6.500 kata
├── 0. Judul, Abstrak (Bilingual), & Kata Kunci (~250 kata)
├── 1. Pendahuluan (Introduction) (~1.000 kata)
│   ├── 1.1 Latar Belakang & Urgensi Pemodelan Penalaran dalam ITS
│   ├── 1.2 Keterbatasan DKT Konvensional pada Domain Logika/Pemrograman
│   ├── 1.3 Motivasi dan Kebutuhan Tinjauan Sistematis
│   └── 1.4 Rumusan Masalah & Kontribusi Tulisan
├── 2. Metodologi Tinjauan Sistematis (Systematic Review Methodology) (~900 kata)
│   ├── 2.1 Desain Protokol Tinjauan (PRISMA 2020 Statement)
│   ├── 2.2 Strategi Penelusuran & Kueri Basis Data Scopus
│   ├── 2.3 Kriteria Inklusi dan Eksklusi (Kelayakan & Aksesibilitas)
│   ├── 2.4 Alur Seleksi PRISMA (Identification, Screening, Retrieval, Inclusion)
│   └── 2.5 Prosedur Ekstraksi Data dan Penilaian Kualitas (Quality Assessment)
├── 3. Hasil dan Sintesis Literatur (Results & Thematic Synthesis) (~2.400 kata)
│   ├── 3.1 Demografi & Tren Publikasi Literatur Terpilih (Tahun, Venues, Tipe Dokumen)
│   ├── 3.2 Sintesis RQ1: Taksonomi Arsitektur AI (Sequential, Graph-based, Hybrid-LLM)
│   ├── 3.3 Sintesis RQ2: Representasi Multiskala, Graph Reasoning, & Status Afektif
│   └── 3.4 Sintesis RQ3: Pemetaan Dataset, Analisis Komparatif Performa (AUC), & Intervensi ITS
├── 4. Pembahasan & Diskusi Kritis (Discussion) (~1.200 kata)
│   ├── 4.1 Pergeseran Paradigma: Dari Prediksi Skor Biner ke Diagnosis Penalaran
│   ├── 4.2 Tantangan Cold-Start, Explainability, & Keterbatasan Data pada Problem Solving
│   ├── 4.3 Implikasi Praktis bagi Desain Intelligent Tutoring System (ITS)
│   └── 4.4 Ancaman Validitas Tinjauan (Threats to Validity & Limitations)
├── 5. Kesimpulan & Rekomendasi Riset Mendatang (Conclusion) (~500 kata)
│   ├── 5.1 Rangkuman Temuan Kunci
│   └── 5.2 Agenda Riset Masa Depan (Future Research Agenda)
└── 6. Daftar Pustaka (References APA 7th Edition)
```

---

## 📋 4. Rancangan Detil Konten Tiap Bab

### Bab 1: Pendahuluan (Introduction)
* **Opening Hook**: Pembelajaran adaptif kini menuntut lebih dari sekadar pelacakan hapalan konsep sederhana; kurikulum modern menuntut penguasaan *computational thinking* dan penalaran logis (*logical reasoning*).
* **The Problem**: Model DKT generasi pertama (Piech et al., 2015; berbasis LSTM murni) mengasumsikan respons biner (benar/salah) independen per butir soal, sehingga gagal menangkap proses *multi-step problem solving* atau logika pemecahan kode pada pemrograman.
* **The Research Gap**: Meskipun terdapat survei umum tentang Knowledge Tracing (misal survey Abdelrahman et al., 2023), belum ada SLR mutakhir yang mengkaji secara komprehensif bagaimana arsitektur AI terbaru (khususnya 2021–2026, era pasca-LLM dan GNN spasial-temporal) dirancang khusus untuk memodelkan penalaran kognitif tingkat tinggi dan implementasinya pada ITS interaktif.
* **Tujuan & Struktur**: Memaparkan 3 Research Questions dan signifikansi temuan bagi pengembang platform edukasi cerdas di Indonesia maupun internasional.

### Bab 2: Metodologi Tinjauan Sistematis (Methodology)
* **Kerangka Kerja**: Mengikuti protokol **PRISMA 2020** secara ketat.
* **Strategi Penelusuran**:
  * Basis data: Scopus (indeks global primer).
  * Rentang publikasi: 2021 hingga publikasi terkini 2026.
  * Tipe dokumen: Artikel Jurnal (`ar`) dan Prosiding Konferensi (`cp`).
* **Kriteria Kelayakan (Eligibility Criteria)**:
  * *Inklusi:* Naskah berfokus pada kombinasi Knowledge Tracing + Adaptive Learning/ITS + Penalaran Logis/Problem Solving/Computational Thinking; naskah berbahasa Inggris/Indonesia; naskah lengkap (*full-text*) berhasil diverifikasi.
  * *Eksklusi:* Naskah di luar tema edukasi/penalaran; naskah yang tidak menyertakan pemodelan komputasi/algoritma pelacakan pengetahuan; naskah duplikat; naskah yang tidak dapat diakses teks lengkapnya secara legal (*reports not retrieved*).
* **Tabel Justifikasi Eksklusi Tahap Retrieval**:
  * Total hasil pencarian: 34 dokumen.
  * Reports not retrieved: 13 dokumen (12 naskah berbayar tertutup di bawah lisensi institusi penerbit berbayar tanpa salinan repositori terbuka, dan 1 naskah repositori open access dengan berkas rusak/tidak dapat diunduh).
  * Included final: 21 dokumen naskah lengkap.

### Bab 3: Hasil dan Sintesis Tematik (Results)
Bab ini disusun secara analitis terstruktur dalam bentuk teks naratif, didukung tabel perbandingan matriks komprehensif dan visualisasi tematik:
1. **Analisis Bibliometrik/Demografis Singkat**: Distribusi tahun penerbitan (2021–2026) dan dominasi platform penerbit (IEEE, ACM, Springer, Elsevier).
2. **Sintesis RQ1 (Taksonomi Arsitektur)**:
   * *Model Sekuensial & Feature Crosses*: Peningkatan model berbasis feature interaction untuk merekam riwayat latihan.
   * *Model Berbasis Graf (GNN, Spatio-Temporal, Hypergraph)*: Menangkap relasi non-linear antar konsep dan tahapan sub-masalah (*problem-solving process*).
   * *Model Integrasi Generative AI & Large Language Models (LLM)*: Penggunaan LLM sebagai knowledge tracer (*CLST*), difficulty-aware encoder (*DPKT*), atau scaffolding agent (*SageJavon, Guiding Not Solving*).
3. **Sintesis RQ2 (Dimensi Kognitif & Kontekstual)**:
   * Pemodelan status afektif (kebosanan, kebingungan, motivasi) dengan hypergraph (*Affect is Key*).
   * Integrasi memori jangka panjang dan distributed practice (*DAS3H*).
   * Dekomposisi tugas multi-skala pada penulisan kode (*Multiscale Knowledge States*).
4. **Sintesis RQ3 (Dataset & Metrik Evaluasi)**:
   * Dataset publik benchmark (misal: Assistments, EdNet, CodeChef/OJ, Junyi, dataset kustom penalaran matematika).
   * Perbandingan kuantitatif metrik performa (Area Under Curve / AUC, Akurasi, RMSE).
   * Dampak nyata dalam lingkungan belajar adaptif (kecepatan ketuntasan belajar, pencegahan *over-practice*, peningkatan retensi memori).

### Bab 4: Pembahasan (Discussion)
* **Sintesis Kritis (Cross-Cutting Synthesis)**: Bagaimana integrasi LLM melengkapi kelemahan GNN dan representasi simbolik tradisional.
* **Tantangan Utama & Kesenjangan**:
  * Masalah *Cold-Start* pada siswa baru saat menghadapi soal logika kompleks.
  * *Explainability* (keterjelian): Guru dan siswa membutuhkan rekomendasi materi yang transparan mengapa suatu materi disarankan, bukan sekadar probabilitas probabilitas hitam (*black box*).
  * Beban komputasi inferensi *real-time* model LLM/GNN pada server sekolah/kampus.
* **Implikasi Desain**: Panduan bagi pengembang *Intelligent Tutoring System* dan pengajar dalam memanfaatkan model DKT hibrida.
* **Keterbatasan Tinjauan (Limitations)**: Ketergantungan pada satu basis data utama (Scopus) dan pembatasan pada literatur *accessible full-text* (21 dokumen).

### Bab 5: Kesimpulan & Rekomendasi (Conclusion)
* Sintesis jawaban ringkas terhadap RQ1, RQ2, dan RQ3.
* Pernyataan konseptual tentang arah masa depan: Konvergensi *Neuro-Symbolic AI*, *Agentic AI Tutors*, dan pelacakan afektif waktu-nyata dalam pendidikan era kecerdasan artifisial.

---

## 📊 5. Spesifikasi Kolom Matriks Ekstraksi Data (21 Paper)

Untuk memastikan data teknis yang diolah akurat dan dapat ditabulasi dengan rapi ke dalam naskah, disiapkan **Matriks Ekstraksi 8-Kolom**:

1. **ID & Sitasi**: Nomor urut paper, nama penulis pertama et al., dan tahun publikasi.
2. **Domain Pembelajaran**: Pemrograman (*Programming*), Penalaran Matematika (*Mathematical Problem Solving*), Logika Formal, dsb.
3. **Arsitektur Model / Inti AI**: Jenis algoritma DKT (LSTM, Transformer, Spatio-Temporal GNN, Tensor Factorization, LLM Alignment, dsb).
4. **Pendekatan Inovatif**: Apa yang baru? (misal: pemodelan afektif hypergraph, difficulty-aware prompt, mitigasi cold-start).
5. **Dataset yang Digunakan**: Nama dataset (misal: CodeNet, Assistments, Math Word Problem, Dataset Eksperimental Lapangan).
6. **Metrik Evaluasi & Nilai Utama**: Nilai performa kuantitatif (AUC, ACC, F1, RMSE).
7. **Bentuk Implementasi / ITS**: Apakah hanya model teoritis, atau sudah diuji coba pada antarmuka *Intelligent Tutoring System* interaktif?
8. **Temuan Kunci / Kontribusi**: Kesimpulan utama studi yang relevan dengan pertanyaan penelitian kita.

---

## ⏱️ 6. Timeline & Milestone Eksekusi Penulisan

| Tahap | Aktivitas | Target Luaran | Status |
|:---:|:---|:---|:---:|
| **Fase 1** | Sinkronisasi Korpus & Verifikasi Naskah Lengkap (21 PDF) | Korpus 21 PDF terverifikasi & Diagram PRISMA terkunci | **SELESAI (DONE)** |
| **Fase 2** | Pengisian Matriks Ekstraksi 21 PDF via Ekstraksi AI | Dokumen matriks ekstraksi lengkap (`ekstraksi_21_paper_slr.md`) | **SELESAI (DONE)** |
| **Fase 3** | Penulisan Draf Bab 1 (Pendahuluan) & Bab 2 (Metodologi PRISMA) | Draf Bab 1 & 2 lengkap dengan justifikasi kriteria inklusi | **SELESAI (DONE)** |
| **Fase 4** | Penulisan Draf Bab 3 (Hasil & Sintesis Tematik RQ1-RQ3) | Draf komparasi teknis antar-arsitektur dan tabulasi AUC | **SELESAI (DONE)** |
| **Fase 5** | Penulisan Draf Bab 4 (Pembahasan) & Bab 5 (Kesimpulan) | Sintesis kritis, agenda riset masa depan, dan implikasi ITS | **SELESAI (DONE)** |
| **Fase 6** | Audit Kepatuhan Sitasi (APA 7th), Penyusunan Abstrak Bilingual, & Quality Review | Naskah final siap submit ke Jurnal Sinta 3 (`naskah_slr_lengkap.md`) | **SELESAI (DONE)** |

---

## 🛡️ 7. Standar Mutu Akademis (Quality Gate)

Sesuai protokol keahlian `academic-paper`:
* **Bebas Pola AI Generik**: Tidak menggunakan frasa klise (*delve into, paramount, testament to, realm of, interplay*), tidak menggunakan kalimat pasif monoton, dan struktur argumen berbasis klaim-bukti (*claim-evidence chain*).
* **Integritas Angka & Metrik**: Semua angka evaluasi (AUC, akurasi) harus bersumber langsung dari hasil eksperimen riil di dalam 21 PDF yang diekstrak.
* **Justifikasi Metodologis Kebal Penolakan**: Penjelasan 13 paper yang dieksklusi ditulis dengan terminologi standar metodologi PRISMA 2020 (*reports not retrieved due to paywall/access barrier*) untuk menjamin transparansi riset ilmiah.
