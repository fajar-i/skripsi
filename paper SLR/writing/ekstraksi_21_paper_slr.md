# Ekstraksi Sistematis 21 Paper Ilmiah: AI in Education (AIEd) & Deep Knowledge Tracing (DKT)

Dokumen ini berisi hasil ekstraksi informasi teknis dari 21 paper ilmiah pada subfolder `pdf` secara presisi, objektif, dan faktual berdasarkan teks asli masing-masing dokumen.

---

## PAPER 1
### 1. IDENTITAS PAPER
* **Judul Lengkap:** A Survey of Knowledge Tracing: Models, Variants, and Applications
* **Penulis Utama & Tahun:** Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, Enhong Chen (2021/2022)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Umum (Multi-domain: Matematika, Pemrograman, Sains, Bahasa Inggris)
* **Definisi KC:** Unit pengetahuan atau konsep abstrak (Knowledge Components) kurikuler yang dipelajari dan diuji pada latihan soal (misalnya konsep matematika, sintaks pemrograman, tata bahasa).

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** Taksonomi Model KT Komprehensif (BKT, DKT, DKVMN, SAKT, SAINT, GNN-based KT) & Benchmark EduKTM / EduData
* **Pendekatan Inovatif/Kebaruan Utama:** Merupakan studi survei komprehensif yang mengkaji evolusi model fundamental KT (probabilistik, regresi logistik, deep learning, graph-based, attention-based), variasi berbasis asumsi psikometris ketat (forgetting behavior, learning curve, individualization, exercise features), serta merilis pustaka algoritma terpadu terbuka (*EduData* dan *EduKTM*).
* **Detail Komponen (Singkat):** Mengklasifikasikan arsitektur menjadi *Traditional KT* (HMM/IRT/Factor Analysis), *Deep Learning KT* (RNN/LSTM, Memory Networks), dan *Attentive/Graph KT* (Self-Attention Transformer, Spatio-Temporal Heterogeneous GNN).

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** Komparasi lintas dataset standar benchmark edukasi: ASSISTments (2009, 2012, 2015, 2017), Junyi Academy, Eedi2020, Statics2011, EdNet (KT1–KT4), dan CodeWorkout.
* **Skor AUC (Area Under ROC):** *N/A (Survey Paper)* — Merangkum perbandingan AUC historis model-model fundamental (DKT ~0.71–0.78, AKT ~0.77–0.82, SAINT ~0.74–0.78).
* **Skor Lain (ACC / RMSE / F1-Score):** Menghimpun standardisasi evaluasi lintas metrik (ACC, RMSE, MAE) dan mendokumentasikan implementasi preprocessing di platform terbuka *EduData*.

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Mengulas sistem nyata (*Real ITS Platforms*) seperti ASSISTments, Cognitive Tutor (Carnegie Learning), dan Khan Academy, serta membedah integrasi KT pada subsistem *Adaptive Learning*, *Learning Path Recommendation*, dan *Computerized Adaptive Testing (CAT)*.
* **Temuan Kunci (Kontribusi):** Paper ini menyajikan taksonomi terlengkap model KT dari era BKT hingga era Transformer/GNN. Melalui perilisan repositori *EduData* dan *EduKTM*, paper ini memecahkan masalah inkonsistensi preprocessing dan fragmentasi implementasi kode di komunitas riset AIEd global.

---

## PAPER 2
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Adapting DAS3H Model for a Personalized Distributed Practice Schedule to Improve Long-Term Memorization in Designing an Intelligent Programming Language Tutor
* **Penulis Utama & Tahun:** Mary Jane C. Samonte, Renee Charlene B. Evangelista, Denise Nicole B. Marcelo (2024)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Programming
* **Definisi KC:** Konsep dasar sintaks, terminologi, dan struktur logika pemrograman pengantar (misal: variabel, loop, fungsi, pemecahan instruksi berbasis kode).

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** Adaptasi Model DAS3H (Decay, Activation, Spacing, Short/Long-Term Memory Multi-Skill Model) terintegrasi Case-Based Reasoning (CBR)
* **Pendekatan Inovatif/Kebaruan Utama:** Mengadaptasi model psikometris DAS3H yang memperhitungkan laju kelupaan memori (memory decay) dan penjadwalan latihan terdistribusi (*spaced repetition / distributed practice*) khusus untuk melacak penguasaan simultan banyak konsep pemrograman (*multi-skill programming tasks*).
* **Detail Komponen (Singkat):** Formulasi logistik aditif berbasis IRT dengan parameter *student ability*, *item difficulty*, *exponential decay window*, serta mekanisme retrival CBR untuk umpan balik kontekstual.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** Studi literatur sistematis terhadap 16 studi primer (2018–2023) untuk perancangan sistem prototipe tutor.
* **Skor AUC (Area Under ROC):** *N/A (System Design Proposal / Conceptual Framework)* — Paper berfokus pada spesifikasi desain dan permodelan kognitif alih-alih pelaporan AUC empiris baru.
* **Skor Lain (ACC / RMSE / F1-Score):** *N/A*

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Perancangan arsitektur prototipe antarmuka web Intelligent Programming Tutor (IPT) dengan modul kuis, flashcard digital, dan mesin penjadwalan repetisi adaptif.
* **Temuan Kunci (Kontribusi):** Mengatasi fenomena *memory decay* dan tingginya angka *dropout* pada mata kuliah dasar pemrograman melalui integrasi model pelacakan multi-skill DAS3H. Menghasilkan rancangan ITS pemrograman adaptif yang mengatur interval review otomatis berbasis kesulitan riwayat performa siswa.

---

## PAPER 3
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Affect is key: Enhancing knowledge tracing with hypergraph-based affective state modeling
* **Penulis Utama & Tahun:** Changqin Huang, Xi Cheng, Yi Wang, Huicheng Zeng, Xiaodi Huang, Qionghao Huang (2024/2026)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Math Problem Solving
* **Definisi KC:** Konsep-konsep matematika sekolah menengah (101 konsep pada ASSIST09, 265 konsep pada ASSIST12, 102 konsep pada ASSIST17).

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** AHGKT (Affective Hypergraph Knowledge Tracing)
* **Pendekatan Inovatif/Kebaruan Utama:** Mengintegrasikan dinamika afektif/emosi siswa ke dalam pelacakan pengetahuan menggunakan arsitektur hipergraf dua tingkat (*bilevel hypergraph*): lapisan latihan (*exercise layer*) memodelkan relasi tingkat tinggi antara soal-konsep, dan lapisan afektif memodelkan 4 status emosi (*bored, concentrating, confused, frustrated*) melalui mekanisme *affect-aware hypergraph convolution*.
* **Detail Komponen (Singkat):** Lapisan hipergraf ganda, konvolusi hipergraf multi-layer (*message passing*), modul interaksi afektif-kognitif, dan fungsi rugi (*loss function*) gabungan dengan koefisien penyeimbang $\lambda$.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** ASSISTments2009 (ASSIST09), ASSISTments2012 (ASSIST12), dan ASSISTments2017 (ASSIST17).
* **Skor AUC (Area Under ROC):**
  * ASSISTments2009: **0.8289**
  * ASSISTments2012: **0.8103**
  * ASSISTments2017: **0.7986**
* **Skor Lain (ACC / RMSE / F1-Score):**
  * Accuracy (ACC): **0.7941** (ASSIST09), **0.7936** (ASSIST12), **0.7336** (ASSIST17)

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Model komputasi eksperimental yang divalidasi secara luring (*offline evaluation*) pada log interaksi platform edukasi nyata ASSISTments.
* **Temuan Kunci (Kontribusi):** AHGKT membuktikan bahwa faktor afektif (kebosanan, konsentrasi, kebingungan, frustrasi) merupakan prediktor kuantitatif yang signifikan dalam luaran pembelajaran. Model ini melampaui seluruh baseline SOTA (termasuk DKT, AKT, SAINT, dan ASIKT) dengan peningkatan AUC hingga 5.49% pada dataset yang kaya sinyal emosi.

---

## PAPER 4
### 1. IDENTITAS PAPER
* **Judul Lengkap:** CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer
* **Penulis Utama & Tahun:** Heeseok Jung, Jaesang Yoo, Yohaan Yoon, Yeonju Jang (2024)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Umum (Multi-domain: Matematika, Ilmu Pengetahuan Sosial / IPS, Sains / IPA)
* **Definisi KC:** Standar kompetensi dan konsep kurikulum K-12 lintas disiplin (57 KCs pada NIPS34, 112 KCs pada Algebra05, 123 KCs pada Assist09, 40 KCs pada Social Studies, 76 KCs pada Science).

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** CLST (Cold-start mitigation in knowledge tracing by aligning a generative Language model as a Students' knowledge Tracer)
* **Pendekatan Inovatif/Kebaruan Utama:** Membingkai ulang Knowledge Tracing yang sebelumnya berbasis token ID menjadi tugas *Natural Language Processing* (NLP) menggunakan Generative LLM (*Mistral-7B-Instruct-v0.2*). Memanfaatkan representasi deskripsi soal secara verbal dan transfer pengetahuan eksternal LLM untuk mengatasi masalah *cold-start* (ketika data interaksi siswa sangat sedikit).
* **Detail Komponen (Singkat):** LLM backbone (Mistral-7B) yang di-fine-tune dengan teknik LoRA (*Low-Rank Adaptation*), modul prompt sekuensial interaksi siswa, dan perumusan target biner menggunakan verbalizer token NLP.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** NIPS34, Algebra05, ASSISTments2009 (Assist09), Classting Social Studies, dan Classting Science.
* **Skor AUC (Area Under ROC):** Skor cold-start (evaluasi pada 8, 16, 32, dan 64 siswa):
  * NIPS34: **0.635** (8 siswa), **0.637** (16 siswa), **0.651** (32 siswa), **0.661** (64 siswa)
  * Algebra05: **0.655** (8 siswa), **0.661** (16 siswa), **0.702** (32 siswa), **0.722** (64 siswa)
  * Assist09: **0.689** (8 siswa), **0.682** (16 siswa), **0.697** (32 siswa), **0.718** (64 siswa)
* **Skor Lain (ACC / RMSE / F1-Score):** Peningkatan performa prediksi cold-start mengungguli model baseline hingga 24.52% (Assist09) dan 11.82% (Science), disertai kalibrasi *expected calibration error* (ECE) yang jauh lebih stabil.

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Model komputasi yang diuji coba pada data platform edutech nyata *Classting* (platform edukasi K-12 di Korea Selatan).
* **Temuan Kunci (Kontribusi):** CLST mendemonstrasikan bahwa generative LLM mampu mengeliminasi kendala *cold-start* pada sistem ITS baru dengan memanfaatkan penalaran semantik teks soal tanpa memerlukan fitur metadata eksternal yang kompleks.

---

## PAPER 5
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Data Augmentation for Sparse Multidimensional Learning Performance Data Using Generative AI
* **Penulis Utama & Tahun:** Liang Zhang, Jionghao Lin, John Sabatini, Conrad Borchers, Daniel Weitekamp, Meng Cao, John Hollander, Xiangen Hu, Arthur C. Graesser (2024/2025)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Umum (Pemahaman Bacaan Dewasa / Adult Reading Comprehension)
* **Definisi KC:** Keterampilan kognitif literasi membaca teks, inferensi diskursus, pemahaman gagasan utama, serta giliran percakapan dialog (*conversational trial steps*).

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** Framework Hibrida 3D Tensor Factorization terintegrasi Generative AI (Vanilla GAN & GPT-4o)
* **Pendekatan Inovatif/Kebaruan Utama:** Menggabungkan dekomposisi tensor 3D (*learner × KC × trial*) untuk imputasi data performa siswa yang sangat langka/ompong (80%–90% *missing observations*) dengan augmentasi data sintetis berbasis GenAI (GAN dan LLM).
* **Detail Komponen (Singkat):** Modul faktorisasi tensor matriks linier, generator-diskriminator Vanilla GAN, dan *zero-shot/few-shot prompt pipeline* GPT-4o untuk menghasilkan simulasi lintasan belajar pembelajar baru.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** Dataset interaksi AutoTutor Adult Reading Comprehension (AutoTutor ARC) pada 4 modul pelajaran (Lesson 1 s.d. Lesson 4) dengan tingkat kesulitan *Easy*, *Medium*, *Hard*.
* **Skor AUC (Area Under ROC):** *N/A (Metrik kontinu permodelan regresi tensor/imputasi)*
* **Skor Lain (ACC / RMSE / F1-Score):**
  * Root Mean Square Error (RMSE): Mencapai **0.3715** pada Lesson 2 (Hard), **0.3948** pada Lesson 3 (Hard), **0.4328** pada Lesson 1 (Medium), dan **0.4545** pada Lesson 4 (Hard) — secara konsisten mengungguli baseline BKT, PFA, dan SPARFA-Lite.
  * Mean Absolute Error (MAE): Secara konsisten mencatat error terendah pada imputasi tensor.

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Diimplementasikan dan diuji pada dataset dari ITS percakapan terkemuka *AutoTutor ARC* untuk pembelajar dewasa.
* **Temuan Kunci (Kontribusi):** Mengatasi problem data sparsity ekstrem (hingga 90%) pada sistem ITS tanpa perlu merekrut peserta manusia baru secara masif. Kombinasi faktorisasi tensor dan augmentasi GAN terbukti mempertahankan karakteristik psikometris kurva belajar asli.

---

## PAPER 6
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Design and Implementation of an AI-Enhanced Heuristic Learning System in a Virtual Realm
* **Penulis Utama & Tahun:** Xiaozhu Wang, Shengzhuo Liu, Paul Adams (2024)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Umum (Desain Karakter Animasi 3D / Desain Virtual Reality)
* **Definisi KC:** Konsep pemodelan struktur anatomis, gestur gerak, ekspresi wajah dinamis, proporsi tubuh, dan naturalitas aksi dalam lingkungan simulasi 3D.

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** AI-Driven Smart Learning Partner terintegrasi Virtual Reality (VR) Heuristic Engine
* **Pendekatan Inovatif/Kebaruan Utama:** Mengintegrasikan model tutor AI dialogis cerdas ke dalam lingkungan realitas virtual imersif untuk memfasilitasi pembelajaran heuristik (penemuan mandiri berbasis masalah/desain visual) dengan umpan balik waktu nyata (*real-time multi-dimensional assessment*).
* **Detail Komponen (Singkat):** Modul pengenalan interaksi spasial VR, basis pengetahuan kurikulum desain terstruktur, modul evaluasi parameter visual real-time, dan mesin dialog AI kontekstual.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** Dataset eksperimen mahasiswa mata kuliah *Animation Character Design* (dibagi ke dalam Kelompok Eksperimen AI-VR vs Kelompok Kontrol Konvensional).
* **Skor AUC (Area Under ROC):** *N/A (Studi evaluasi rubrik desain dan pedagogi kualitatif-komparatif)*
* **Skor Lain (ACC / RMSE / F1-Score):** Kelompok eksperimen meraih predikat *Outstanding* pada keseluruhan performa (Struktur: *Reasonable & complete*, Gestur: *Logical*, Ekspresi: *Vivid & expressive*, Aksi: *Smooth & natural*, Kreativitas: *High*) dibandingkan kelompok kontrol yang berada pada tingkat *Average/Ordinary*.

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Diimplementasikan penuh dalam bentuk antarmuka aplikasi Virtual Reality (VR) interaktif dan telah diujicobakan secara riil di kelas universitas.
* **Temuan Kunci (Kontribusi):** Membuktikan bahwa kehadiran mitra cerdas AI dalam ruang VR mampu memandu pembelajaran heuristik kompleks secara mandiri, meningkatkan kreativitas dan penyelesaian karya mahasiswa secara signifikan tanpa ketergantungan konstan pada instruktur fisik.

---

## PAPER 7
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Difficulty aware programming knowledge tracing via large language models
* **Penulis Utama & Tahun:** Lina Yang, Xinjie Sun, Hui Li, Ran Xu, Xuqin Wei (2025/2024)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Programming
* **Definisi KC:** Konsep-konsep pemrograman struktural dan prosedural (misal: *loop, pointer, recursion, array, data structures, conditional branches*).

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** DPKT (Difficulty-aware Programming Knowledge Tracing)
* **Pendekatan Inovatif/Kebaruan Utama:** Memperhitungkan dua dimensi kesulitan pemrograman sekaligus secara eksplisit: kesulitan pemahaman teks soal (*Text Understanding Difficulty - LTD*) dan kesulitan konsep pengetahuan (*Knowledge Concept Difficulty - LKD*) menggunakan anotasi terpandu Large Language Model, yang disematkan dengan CodeBERT dan Graph Attention Network (GAT).
* **Detail Komponen (Singkat):** Pre-trained CodeBERT, embedding kamus kesulitan LLM, mekanisme multi-level attention (Self-Attention & Graph Attention Network), dan lapisan pembaruan *knowledge state* dinamis.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** Project CodeNet (subkoleksi 4 bahasa pemrograman: C++, C, Java, dan Python).
* **Skor AUC (Area Under ROC):**
  * C++ Dataset: **76.2%** (0.762)
  * C Dataset: **75.7%** (0.757)
  * Java Dataset: **75.4%** (0.754)
  * Python Dataset: **76.8%** (0.768)
* **Skor Lain (ACC / RMSE / F1-Score):**
  * Accuracy (ACC): **74.5%** (C++), **71.5%** (C), **72.9%** (Java), **68.1%** (Python)

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Model komputasi yang diuji coba secara ekstensif pada repositori pemrograman skala besar (Project CodeNet), disiapkan sebagai mesin rekomendasi adaptif bagi ITS pemrograman.
* **Temuan Kunci (Kontribusi):** Mengintegrasikan penilaian kesulitan semantik dari LLM mampu mendiagnosis status penguasaan konsep pemrograman secara jauh lebih sensitif dibandingkan model DKT standar yang hanya mengandalkan riwayat benar/salah jawaban siswa.

---

## PAPER 8
### 1. IDENTITAS PAPER
* **Judul Lengkap:** GuideAI: A Real-time Personalized Learning Solution with Adaptive Interventions
* **Penulis Utama & Tahun:** Ananya Shukla, Chaitanya Modi, Satvik Bajpai, Siddharth Siddharth (2024/2026)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Umum (Pemahaman Konseptual Multi-modal)
* **Definisi KC:** Komponen pemahaman konseptual dan dimensi status mental kognitif pembelajar (*cognitive load, attention span, visual focus, fatigue, stress*).

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** GuideAI Multi-Modal Biosensor-Driven LLM Tutoring Framework
* **Pendekatan Inovatif/Kebaruan Utama:** Integrasi loop sensor fisiologis waktu nyata (*real-time biosensory feedback*: eye-tracking Pupil Core, deteksi HRV Max-Health-Band, estimasi postur kamera, dan analisis digital note-taking) dengan agen LLM yang memicu intervensi adaptif multi-modal (perubahan teks, visual/gambar, audio, video, dan penurunan beban kognitif secara otomatis).
* **Detail Komponen (Singkat):** Tiga modul terintegrasi: *Sensor Module* (eye tracker 60 fps, PPG sensor 200 Hz, kamera postur), *Processing Module* (ekstraksi metrik HRV & fiksasi mata berbasis Lab Streaming Layer / LSL), dan *Inference Module* (mesin inferensi kognitif yang memicu prompt re-engineering pada LLM).

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** Dataset studi empiris terkontrol terhadap 25 partisipan (kondisi intervensi adaptif GuideAI vs kontrol LLM standar) dan studi formatif 66 pengguna.
* **Skor AUC (Area Under ROC):** *N/A (Metrik interaksi HCI dan evaluasi pemahaman belajar manusia)*
* **Skor Lain (ACC / RMSE / F1-Score):** Peningkatan skor pemahaman konseptual dan retensi memori secara signifikan ($p < 0.05$); penurunan indeks beban kognitif NASA-TLX (*mental demand, frustration, effort*); skor penerimaan sistem rata-rata di atas 6.2/7.0 pada skala Likert.

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Diimplementasikan penuh sebagai sistem antarmuka Intelligent Tutoring System fisik-digital (*live multi-modal interactive system*) yang diuji coba pada pembelajar manusia secara langsung.
* **Temuan Kunci (Kontribusi):** GuideAI mengatasi kelemahan mendasar model tutor LLM konvensional yang "buta kognitif". Sistem membuktikan bahwa adaptasi modalitas instruksional berbasis biosensor nyata mampu mencegah frustrasi kognitif dan melipatgandakan retensi materi ajar.

---

## PAPER 9
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Guiding, Not Solving: Agentic Scaffolding for LLM Programming Tutors
* **Penulis Utama & Tahun:** Yuchen Wang, Chiraag Singh Anand, Chee Wei Tan (2024)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Programming
* **Definisi KC:** Keterampilan penalaran algoritma dan tahapan tonggak pemecahan bug pemrograman (*milestones*: pemahaman spesifikasi, penanganan batas nilai, alur percabangan, perbaikan logika).

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** SHARP (Socratic Hinting for AI-Reinforced Programming)
* **Pendekatan Inovatif/Kebaruan Utama:** Menggantikan peran LLM yang selama ini sekadar menjadi "mesin pemberi solusi kode langsung" (*code solver*) dengan kerangka agen *scaffolding* Sokratik; menggabungkan *milestone-driven progress estimation* (dengan *contrastive representation/metric learning*) dan *Knowledge Tracing* (KT) untuk menyajikan petunjuk tidak langsung (*indirect guidance*).
* **Detail Komponen (Singkat):** Agen penaksir milestone kode berbasis Triplet Loss, modul pelacak status penguasaan konsep (KT module), modul penyusun hint Sokratik berpedoman kebijakan pedagogis (*stochastic policy $\pi_\theta$*), diintegrasikan ke platform web *AskCodey*.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** Dataset *MULTI-DEBUG* (50 masalah pemrograman dengan injeksi 1, 2, dan 3 bug sintetis) dan studi lapangan pada 42 siswa sekolah menengah.
* **Skor AUC (Area Under ROC):** *N/A (Dievaluasi melalui tingkat keberhasilan penyelesaian tugas / Task Success Rate)*
* **Skor Lain (ACC / RMSE / F1-Score):**
  * Task Success Rate: **98%** (skenario 1-bug), **94%** (skenario 2-bug), **92%** (skenario 3-bug) — mengungguli TreeInstruct (72%) dan Basic Guidance.
  * Rasio Tidak Langsung (*Indirectness Score*): **1.0** (mempertahankan 100% pantangan memberikan kode solusi langsung).

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Diimplementasikan secara penuh pada platform tutoring pemrograman web *AskCodey* dan diujicobakan dalam studi pilot *in-the-wild* pada 42 pelajar sekolah menengah.
* **Temuan Kunci (Kontribusi):** SHARP berhasil memecahkan dilema pedagogis era LLM: menjaga proses pergulatan produktif (*productive struggle*) siswa dalam belajar koding tanpa membiarkan mereka buntu (*stuck*), menghasilkan efisiensi dialog 1.84 giliran per bug dengan akurasi penyelesaian 92%–98%.

---

## PAPER 10
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Infusing Expert Knowledge Into a Deep Neural Network Using Attention Mechanism for Personalized Learning Environments
* **Penulis Utama & Tahun:** Ange Tato, Roger Nkambou (2022)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Logical Reasoning
* **Definisi KC:** Aturan inferensi logika proposisional formal (Modus Ponens/MPP, Modus Tollens/MTT, Affirmation of Consequent/AC, Denial of Antecedent/DA) lintas 3 level konten (familiar, kontrafaktual, abstrak), mencakup 16 unit pengetahuan teramati dan 12 unit laten.

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** DKT+BN (Deep Knowledge Tracing infused with Bayesian Network via Attention Mechanism)
* **Pendekatan Inovatif/Kebaruan Utama:** Menggabungkan *a priori expert knowledge* yang dikodekan dalam Bayesian Network ke dalam jaringan saraf tiruan berulang (LSTM-DKT) menggunakan mekanisme atensi (*attention mechanism*); berhasil mengatasi kelemahan fatal DKT standar yang gagal memprediksi konsep langka atau konsep marginal yang sangat sulit/mudah.
* **Detail Komponen (Singkat):** Layer representasi latihan one-hot, modul prioritas Bayesian Network berbasis graf kausalitas ahli, modul cross-attention untuk pembobotan pengetahuan pakar vs data sekuensial, dan modul *loss masking*.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** Dataset empiris ITS Logic-Muse (294 mahasiswa, 48 latihan penalaran logika) dan dataset gim serius MorALERT (102 partisipan penalaran sosio-moral).
* **Skor AUC (Area Under ROC):** *N/A (Metrik yang dilaporkan secara komprehensif adalah Accuracy dan F1-Score multi-kelas)*
* **Skor Lain (ACC / RMSE / F1-Score):**
  * Overall Accuracy pada Logic-Muse: **0.82** (82%) untuk DKT+BN (meningkat dari 0.74 pada DKT murni dan 0.65 pada BN murni).
  * F1-Score prediksi kebenaran pada konsep tersulit melonjak drastis: DA_A (naik dari 0.0 menjadi **0.80**), AC_CCF (naik dari 0.0 menjadi **0.80**), AC_A (naik dari 0.0 menjadi **0.58**), DA_FFA (naik dari 0.0 menjadi **0.47**).
  * MorALERT Model Final: Accuracy = **0.75**, Precision = **0.72**, Recall = **0.75**, F1-score = **0.73**.

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Diimplementasikan dan diuji coba langsung pada sistem *Intelligent Tutoring System* nyata berbasis web (Logic-Muse) dan gim serius adaptif (MorALERT).
* **Temuan Kunci (Kontribusi):** Model hibrida ini membuktikan bahwa mekanisme atensi mampu "menyuntikkan" kebijaksanaan pakar logika ke dalam model deep learning, sehingga sistem ITS dapat beroperasi sangat akurat pada populasi data kecil (*few samples*) tanpa mengalami bias kegagalan pada konsep-konsep marginal.

---

## PAPER 11
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Knowledge Tracing for Complex Problem Solving: Granular Rank-Based Tensor Factorization
* **Penulis Utama & Tahun:** Chunpai Wang, Shaghayegh Sahebi, Siqian Zhao, Peter Brusilovsky, Laura O. Moraes (2023)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Programming
* **Definisi KC:** Konsep-konsep materi ilmu komputer dan pemrograman berorientasi objek (misal: struktur kontrol, kelas, objek, metode, array, tipe data).

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** GRATE (Granular Rank-based Tensor Factorization)
* **Pendekatan Inovatif/Kebaruan Utama:** Mengakomodasi pemecahan masalah kompleks (*complex problem solving*) di mana siswa melakukan banyak percobaan berturut-turut; GRATE secara adaptif mengelompokkan submisi berulang menjadi episode granular dan menerapkan regularisasi berbasis peringkat (*rank-based pairwise order*) untuk melacak kemajuan relatif siswa alih-alih menganggap seluruh percobaan setara.
* **Detail Komponen (Singkat):** Dekomposisi tensor non-negatif 3 dimensi (*student × concept/problem × time episode*), fungsi utilitas pemeringkatan berpasangan (*pairwise ranking constraint*), dan skema optimasi berbasis *stochastic gradient descent*.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** 3 dataset pemrograman riil: MORF (MOOC data science), CSIntro (mata kuliah pengantar ilmu komputer), dan MasteryGrids (sistem latihan cerdas pemrograman Java).
* **Skor AUC (Area Under ROC):**
  * MasteryGrids (umpan balik biner): **0.7035** (mengungguli DKT 0.6968, DKVMN 0.6881, dan iBKT 0.6048)
* **Skor Lain (ACC / RMSE / F1-Score):**
  * Root Mean Square Error (RMSE): **0.2033** pada MORF; **0.3726** pada CSIntro (secara statistik signifikan lebih baik dari DKT 0.4132 dan DKVMN 0.4202 dengan $p < 0.05$).

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Model komputasi yang divalidasi pada log interaksi nyata platform ITS antarmuka terbuka *Mastery Grids* (University of Pittsburgh) dan platform MOOC.
* **Temuan Kunci (Kontribusi):** Model membuktikan bahwa pada ranah pemrograman yang kompleks, agregasi submisi ke tingkat granular yang dikombinasikan dengan faktorisasi tensor mampu mengungguli model deep neural network (DKT/DKVMN) yang rentan terhadap noise fluktuasi jawaban berturut-turut.

---

## PAPER 12
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Knowledge tracing in mathematical problem-solving processes: a spatio-temporal graph neural network approach
* **Penulis Utama & Tahun:** Xia Li (2026)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Math Problem Solving
* **Definisi KC:** Titik-titik pengetahuan matematika sekolah (*algebraic, arithmetic, and geometric skills*) dan dependensi prasyarat antar konsep.

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** STGNN-MKT (Spatio-Temporal Graph Neural Network for Mathematical Knowledge Tracing)
* **Pendekatan Inovatif/Kebaruan Utama:** Menyatukan korelasi spasial konsep matematika dan dinamika evolusi temporal proses belajar ke dalam graf heterogen terner (*student-exercise-knowledge point*); menggunakan mekanisme *Meta-path-aware Graph Attention* (MAGAT) pada dimensi spasial dan *Gated Temporal Convolutional Network* (Gated TCN) dengan modul gerbang memori kelupaan kurva Ebbinghaus (*FMGM*) pada dimensi temporal.
* **Detail Komponen (Singkat):** Graf heterogen tripartit, agregator atensi berbasis meta-path, konvolusi temporal teredam (*dilated causal TCN*), dan gerbang peluruhan eksponensial nonlinier berbasis interval waktu $\Delta t$ dan frekuensi latihan $n_j$.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** ASSISTments2009 dan KDDCup2010.
* **Skor AUC (Area Under ROC):**
  * ASSISTments2009: **0.901**
  * KDDCup2010: **0.893**
  * Sampel interval jangka panjang (>30 hari): AUC mencapai **0.872**
* **Skor Lain (ACC / RMSE / F1-Score):**
  * ASSISTments2009: Accuracy (ACC) = **0.845**, RMSE = **0.218**
  * KDDCup2010: Accuracy (ACC) = **0.839**, RMSE = **0.224**

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Model komputasi lanjutan yang diuji pada dataset patokan AIEd standar dunia untuk persiapan integrasi ke dalam sistem tutor adaptif matematika.
* **Temuan Kunci (Kontribusi):** Penggabungan atensi meta-path spasial dan konvolusi temporal berpagar kelupaan menghasilkan lonjakan akurasi prediksi sebesar 5.3%–6.7% di atas model grafik terdahulu (seperti GKT dan DGMN), serta mempertahankan prediksi konsisten pada rantai penalaran matematika panjang.

---

## PAPER 13
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Learning Logical Reasoning Using an Intelligent Tutoring System: A Hybrid Approach to Student Modeling
* **Penulis Utama & Tahun:** Roger Nkambou, Janie Brisson, Ange Tato, Serge Robert (2023)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Logical Reasoning
* **Definisi KC:** Unit keterampilan penalaran kondisional formal (inhibisi pengecualian, pembuatan contoh tandingan, dan pengelolaan model mental pada 4 silogisme: MPP, MTT, AC, DA lintas level familiar, kontrafaktual, dan abstrak; total 16 tipe item dan 9 keterampilan inti).

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** Model Hibrida Student Modeling (CDM-DINA terintegrasi DKTm+BN)
* **Pendekatan Inovatif/Kebaruan Utama:** Mengintegrasikan model diagnosis kognitif psikometri formal (DINA CDM) untuk validasi struktur graf dan inisialisasi *prior knowledge* siswa baru (*pre-test initialization*), yang kemudian diumpankan ke arsitektur DKT berbasis LSTM yang dimodifikasi dengan masker fungsi rugi (*loss masking*) dan mekanisme atensi pakar jaringan Bayesian.
* **Detail Komponen (Singkat):** Q-matrix 16×9 tervalidasi pakar logika, modul penaksir psikometri R-CDM DINA, recurrent neural network LSTM dengan *masked cross-entropy*, dan jaringan Bayesian pakar.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** Dataset eksperimen Logic-Muse (294 partisipan daring Prolific Academic, 48 tugas penalaran logika terstruktur).
* **Skor AUC (Area Under ROC):** *N/A (Evaluasi berfokus pada Akurasi Keseluruhan dan F1-Score per Kategori Keterampilan)*
* **Skor Lain (ACC / RMSE / F1-Score):**
  * Akurasi Prediksi Keseluruhan (*Overall Accuracy*):
    * Bayesian Network (BN) murni: **0.65** (65%)
    * DKT standar: **0.74** (74%)
    * DKTm (DKT + masking): **0.80** (80%)
    * **DKTm+BN (Model Hibrida Lengkap): 0.82** (82%)
  * F1-Score pada keterampilan tersulit meningkat drastis (contoh: DA_A naik dari 0.0 menjadi **0.80**, AC_CCF naik dari 0.0 menjadi **0.80**, DA_CCF naik dari 0.0 menjadi **0.72**).

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Diimplementasikan dan diuji secara riil dalam ekosistem *Intelligent Tutoring System* Logic-Muse.
* **Temuan Kunci (Kontribusi):** Model hibrida ini berhasil memecahkan kendala representasi data biner DKT pada domain logika; DKTm+BN mempertahankan kemampuan prediksi akurat pada keterampilan-keterampilan marginal yang jarang muncul, membuktikan efektivitas integrasi psikometri kognitif dan deep learning.

---

## PAPER 14
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Let GPT be a Math Tutor: Teaching Math Word Problem Solvers with Customized Exercise Generation
* **Penulis Utama & Tahun:** Zhenwen Liang, Wenhao Yu, Tanmay Rajpurohit, Peter Clark, Xiangliang Zhang, Ashwin Kalyan (2023)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Math Problem Solving
* **Definisi KC:** Pemecahan soal cerita matematika (*Math Word Problems - MWP*), pemetaan persamaan aritmatika, inferensi logika kuantitatif, dan penetapan variabel matematis.

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** CEMAL (Customized Exercise for MAth Learning)
* **Pendekatan Inovatif/Kebaruan Utama:** Menggunakan model bahasa raksasa (GPT-3.5-turbo) sebagai "Guru Tutor Matematika" yang menganalisis kelemahan model siswa (*student solver* RoBERTa/LSTM), lalu menghasilkan buku latihan soal kustom yang dirancang khusus untuk menutup kelemahan spesifik model pembelajar tersebut secara berulang (*adaptive distillation loop*).
* **Detail Komponen (Singkat):** Modul generator buku latihan berbasis prompt GPT-3.5, modul diagnosis kesalahan inferensi matematis, dan model *student solver* berbobot ringan (RoBERTa 144M/377M & LSTM 20M).

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** 4 benchmark soal cerita matematika: MAWPS, ASDiv-a, SVAMP (In-Distribution), dan SVAMP (Out-of-Distribution).
* **Skor AUC (Area Under ROC):** *N/A (Evaluasi berbasis akurasi pemecahan soal / Solve Accuracy)*
* **Skor Lain (ACC / RMSE / F1-Score):**
  * Akurasi Pemecahan (*Solve Accuracy* - Solver Large 377M):
    * MAWPS (ID): **94.7%**
    * ASDiv-a (ID): **93.3%**
    * SVAMP (ID): **85.4%**
    * SVAMP (OOD): **76.4%**
  * Solver Base (144M): **93.9%** (MAWPS), **90.9%** (ASDiv-a), **81.5%** (SVAMP ID), **68.6%** (SVAMP OOD).

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Kerangka kerja tutor-siswa berbasis komputasi AI (*machine teaching / distillation framework*) yang menyimulasikan siklus ITS nyata dalam pengajaran pemecahan masalah matematika.
* **Temuan Kunci (Kontribusi):** Model membuktikan bahwa latihan adaptif yang disesuaikan dengan titik lemah pembelajar jauh lebih efektif daripada metode distilasi konvensional berbasis penjelasan *Chain-of-Thought* (CoT), memungkinkan model kecil melampaui model berparameter 20× lipat lebih besar.

---

## PAPER 15
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Leveraging LLM and Multiscale Knowledge States to Improve Knowledge Tracing in Programming Tasks
* **Penulis Utama & Tahun:** Mingxing Shao, Tiancheng Zhang, Yifang Yin, Wenhui Wu, Zikai Li, Minghe Yu, Fangling Leng (2025/2026)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Programming
* **Definisi KC:** Komponen pengetahuan kode berskala jamak (*multiscale*): konsep modul bahasa, fungsi logika program, serta kategori galat/kesalahan semantik spesifik hasil diagnosis LLM (18 konsep pada Code-S/F, 106 konsep pada BePKT).

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** MIE+MLPKT (Multi-level Information Extraction + Multi-level Programming Knowledge Tracing)
* **Pendekatan Inovatif/Kebaruan Utama:** Mengatasi keterbatasan pelabelan biner kasar (*pass/fail test cases*) dengan menggunakan LLM (DeepSeek-V3) untuk mengekstrak vektor penyebab kesalahan koding siswa (*error reason vectors*) dan memberikan penilaian parsial kontinu (skor 0–1); memodelkan *knowledge state* siswa pada tiga level terpisah: konsep, masalah, dan penalaran logika kode.
* **Detail Komponen (Singkat):** Modul ekstraksi informasi multi-level berbasis LLM, representasi graph embedding untuk relasi kode-soal, dan multi-layer attention mechanism untuk fusi ketiga tingkatan status pengetahuan.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** 3 dataset pemrograman: Code-S, Code-F, dan BePKT.
* **Skor AUC (Area Under ROC):**
  * Code-S Dataset: **0.8926**
  * Code-F Dataset: **0.8738**
  * BePKT Dataset: **0.8380**
* **Skor Lain (ACC / RMSE / F1-Score):**
  * Accuracy (ACC): **0.8451** (Code-S), **0.8305** (Code-F), **0.8408** (BePKT)
  * Root Mean Square Error (RMSE): **0.1904** (Code-S), **0.2015** (Code-F), **0.1735** (BePKT)
  * Mean Absolute Error (MAE): **0.1430** (Code-S), **0.1521** (Code-F), **0.1319** (BePKT)

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Model komputasi canggih yang diuji secara empiris pada 3 repositori koding berskala besar untuk integrasi langsung ke platform penilaian koding otomatis dan ITS pemrograman.
* **Temuan Kunci (Kontribusi):** Mengganti skor biner kaku dengan umpan balik multi-skala berbasis LLM meningkatkan akurasi dan AUC secara substansial di atas 18 baseline mutakhir, membuktikan bahwa alasan kesalahan sintaks/logika adalah sinyal paling deterministik dalam pelacakan kompetensi koding siswa.

---

## PAPER 16
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Modeling Student Performance Using Feature Crosses Information for Knowledge Tracing
* **Penulis Utama & Tahun:** Lixiang Xu, Zhanlong Wang, Suojuan Zhang, Xin Yuan, Minjuan Wang, Enhong Chen (2024)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Math Problem Solving / Umum
* **Definisi KC:** Konsep pengetahuan laten (*latent concepts*) matematika dan keahlian soal pada platform pembelajaran adaptif.

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** FCIKT (Feature Crosses Information Knowledge Tracing)
* **Pendekatan Inovatif/Kebaruan Utama:** Mempelajari relasi nonlinier orde tinggi (*higher-order relationships*) antara tingkat kesulitan butir soal, konsep pengetahuan laten, dan identitas pertanyaan melalui mekanisme *feature crosses*; dilengkapi jaringan atensi multi-kepala (*multi-head attention*) berbatas kesamaan (*similarity constraint*) untuk menyaring representasi yang tidak relevan.
* **Detail Komponen (Singkat):** Jaringan perlintasan fitur non-linear (Cross Network), modul Multi-Head Self-Attention dengan parameter *Similarity Constraint* ($Sim\_C = 0.7$), lapisan embedding gabungan berdimensi 100, dan RNN untuk perambatan sekuensial.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** ASSISTments2009 (ASSIST09), ASSISTments2012 (ASSIST12), dan EdNet.
* **Skor AUC (Area Under ROC):**
  * Melampaui seluruh baseline terkuat (GIKT, GAKT, DKVMN, DKT+, BKT, KTM).
  * Keunggulan peningkatan margin AUC: Mengungguli GIKT sebesar **+3.01% pada ASSIST12**, **+0.59% pada EdNet**, dan **+0.31% pada ASSIST09**; serta mengungguli DKVMN sebesar **3.62%–7.37%**.
* **Skor Lain (ACC / RMSE / F1-Score):** Menghasilkan konvergensi fungsi rugi yang stabil dengan laju *decay rate* 0.92 dan pencegahan overfiting optimal pada dropout 0.8.

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Model komputasi eksperimental yang diuji pada dataset benchmark publik untuk lingkungan pembelajaran adaptif cerdas.
* **Temuan Kunci (Kontribusi):** Paper ini membuktikan bahwa penyederhanaan riwayat siswa menjadi urutan konsep linier adalah kelemahan fatal DKT lama. Penyilangan fitur eksplisit antara kesulitan soal dan konsep laten secara dramatis memperkuat akurasi prediksi respons siswa.

---

## PAPER 17
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Optimizing Mastery Learning by Fast-Forwarding Over-Practice Steps
* **Penulis Utama & Tahun:** Meng Xia, Robin Schmucker, Conrad Borchers, Vincent Aleven (2025)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Math Problem Solving / Umum
* **Definisi KC:** Sub-keterampilan kognitif per langkah soal multi-tahap (misal: mencari penyebut persekutuan terkecil, konversi pecahan, penjumlahan pembilang pada materi pecahan).

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** Fast-Forwarding Algorithmic Scaffolding terintegrasi Bayesian Knowledge Tracing (BKT / CogTutor)
* **Pendekatan Inovatif/Kebaruan Utama:** Pendekatan adaptivitas tingkat langkah (*step-level adaptivity*) baru yang secara otomatis mengisi atau melompati langkah-langkah soal yang keterampilan kognitifnya telah dikuasai siswa (*mastered skills*); memotong fenomena *overpractice* (latihan berlebih yang menjemukan) tanpa merusak keutuhan konteks pemecahan masalah bertahap dan tanpa perlu perancangan ulang kurikulum.
* **Detail Komponen (Singkat):** Pelacak status penguasaan BKT step-level, mesin inferensi dependensi langkah berbasis Knowledge Component, dan mekanisme otomatisasi input langkah (*fast-forwarding step engine*).

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** Kurikulum empiris pecahan Cognitive Tutor (Fraction Addition curriculum: 5 KC, 32 problem multi-step) yang dievaluasi melalui simulasi kognitif pembelajar berskala besar.
* **Skor AUC (Area Under ROC):** *N/A (Metrik efisiensi pedagogis dan pengurangan beban latihan)*
* **Skor Lain (ACC / RMSE / F1-Score):**
  * Reduksi Overpractice: Mengurangi langkah latihan berlebih hingga **35.7%** (sekitar sepertiga) pada selector latihan berbasis kesulitan.
  * Penalti Underpractice: **0.00** (tidak menimbulkan efek samping kurang latihan; $M = 0.44$ vs $0.43$).

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Dirancang spesifik untuk Cognitive Tutors / sistem ITS berbasis langkah (*step-based Intelligent Tutoring Systems* seperti CTAT / Cognitive Tutor) dan divalidasi melalui permodelan simulasi kognitif komprehensif.
* **Temuan Kunci (Kontribusi):** Fast-Forwarding membuktikan bahwa adaptivitas mikro pada tingkat langkah soal mampu menghemat sepertiga waktu belajar siswa dari latihan redundan tanpa mengorbankan ketuntasan pemahaman materi sedikit pun.

---

## PAPER 18
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Remembering is Not Applying: Interpretable Knowledge Tracing for Problem-solving Processes
* **Penulis Utama & Tahun:** Tao Huang, Xinjia Ou, Huali Yang, Shengze Hu, Jing Geng, Junjie Hu, Zhuoran Xu (2024)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Math Problem Solving / Umum
* **Definisi KC:** Konsep pengetahuan kurikuler dan keterampilan pemecahan masalah terapan (termuat dalam kurikulum matematika dan tes standar).

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** PSKT (Problem-Solving Process-Oriented Knowledge Tracing)
* **Pendekatan Inovatif/Kebaruan Utama:** Memisahkan penguasaan teoretis (*theoretical remembering*) dari kemampuan aplikasi praktis (*practical applying*) siswa ke dalam 3 fase pedagogis: (1) Pra-penyelesaian (persepsi subjektif soal), (2) Saat-penyelesaian (permodelan level aplikasi dengan parameter psikometris yang dapat diinterpretasikan), dan (3) Pasca-penyelesaian (indikator internalisasi pengetahuan dan peluruhan memori kelupaan waktu).
* **Detail Komponen (Singkat):** Modul persepsi kesulitan personal, modul representasi tingkat penerapan pengetahuan berbasis IRT/m-IRT, dan modul pembaruan internalisasi berbasis kurva forgetting.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** 5 dataset benchmark riil: ASSISTments2012 (ASSIST-12), ASSISTments2017 (ASSIST-17), EdNet-KT1, Junyi, dan Eedi.
* **Skor AUC (Area Under ROC):**
  * ASSISTments2012: **0.8252**
  * ASSISTments2017: **0.8182**
  * EdNet-KT1: **0.7749**
  * Junyi Academy: **0.8057**
  * Eedi: **0.8201**
  *(Seluruh skor AUC terbaik bercetak tebal dan signifikan dengan $p < 0.05$ terhadap 11 baseline SOTA)*
* **Skor Lain (ACC / RMSE / F1-Score):**
  * Accuracy (ACC): **0.7838** (ASSIST12), **0.7503** (ASSIST17), **0.7318** (EdNet-KT1), **0.8558** (Junyi), **0.7571** (Eedi)
  * RMSE: **0.3858** (ASSIST12), **0.4075** (ASSIST17), **0.4220** (EdNet-KT1), **0.3296** (Junyi), **0.4045** (Eedi)

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Model komputasi teruji pada log interaksi platform online tutoring skala raksasa untuk menghadirkan inferensi *knowledge state* yang transparan dan dapat dijelaskan (*interpretable learner modeling*).
* **Temuan Kunci (Kontribusi):** Menjawab paradoks pendidikan bahwa siswa sering kali "ingat teorinya tetapi tidak bisa menerapkannya". PSKT secara konsisten mengalahkan model monolitik (DKT, AKT, SAINT) di kelima dataset sekaligus menyajikan parameter status belajar yang bermakna bagi guru.

---

## PAPER 19
### 1. IDENTITAS PAPER
* **Judul Lengkap:** SageJavon: A scalable AI tutor for personalized programming learning
* **Penulis Utama & Tahun:** Hanyu Zhao, Yuzhuo Wu, Zhufeng Lu, Xiaohua Yu, Weikai Miao, Liangyu Chen (2024/2026)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Programming
* **Definisi KC:** Konsep-konsep graf pengetahuan pemrograman Java (*Java Knowledge Graph*: dasar Java, OOP, enkapsulasi, pewarisan, polimorfisme, penanganan eksepsi, struktur data).

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** SageJavon Framework ("Learn-Practice-Evaluate-Support") terintegrasi RAG, LLM, dan GIKT
* **Pendekatan Inovatif/Kebaruan Utama:** Kerangka kerja tutor AI berbasis Taksonomi Bloom yang menggabungkan *Large Language Models* dengan *Retrieval-Augmented Generation* (RAG) dan pelacakan pengetahuan berbasis graf relasi soal (*Graph-based Interaction Knowledge Tracing - GIKT*) untuk mengontrol beban kognitif serta memberikan bimbingan koding adaptif waktu nyata.
* **Detail Komponen (Singkat):** Modul interaksi multimodal (Learn, Practice, Evaluate, Support), repositori Java Knowledge Graph berstruktur ontologi relasi, agen RAG terhubung vektor dokumen perkuliahan, dan modul GIKT untuk prediksi penguasaan materi koding.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** Dataset mata kuliah pemrograman Java nyata (*Our Dataset*) ditambah evaluasi validasi GIKT pada ASSIST09, ASSIST12, dan EdNet.
* **Skor AUC (Area Under ROC):** Menggunakan evaluasi berbasis graf interaksi (GIKT) dengan konsistensi prediksi tinggi.
* **Skor Lain (ACC / RMSE / F1-Score):**
  * Akurasi Prediksi (ACC) modul GIKT: **0.7932** pada *Our Dataset (Java)*, **0.7931** pada ASSIST09, **0.7823** pada ASSIST12, dan **0.7612** pada EdNet.
  * Skor evaluasi kualitatif dan transfer belajar: Penurunan beban kognitif secara signifikan ($p < 0.01$), peningkatan skor kepuasan siswa (rata-rata di atas 4.3/5.0), dan korelasi evaluasi kegunaan kode FUPS-Score tertinggi.

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Diimplementasikan dan disebarkan (*deployed*) secara langsung pada platform sistem Intelligent Tutoring System nyata dalam perkuliahan pemrograman Java riil yang diikuti oleh 85 mahasiswa universitas.
* **Temuan Kunci (Kontribusi):** SageJavon membuktikan bahwa sinergi antara graf pengetahuan kurikulum koding, pelacakan kompetensi berbasis graf (GIKT), dan retrieval LLM mampu menurunkan cognitive load pembelajar, mendorong transfer pengetahuan yang jauh lebih mendalam dibanding perkakas konvensional.

---

## PAPER 20
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Tracing Mathematical Proficiency Through Problem-Solving Processes
* **Penulis Utama & Tahun:** Jungyang Park, Suho Kang, Jaewoo Park, Jaehong Kim, Jaewoo Shin, Seonjoon Park, Youngjae Yu (2024/2025)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Math Problem Solving
* **Definisi KC:** Indikator Kemahiran Matematika multi-dimensi (*Mathematical Proficiency - MP*) merujuk pada standar *National Research Council* (NRC): pemahaman konseptual, kelancaran prosedural, kompetensi strategis, penalaran adaptif, dan disposisi produktif.

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** STATUSKT (State-aware TrAcing via TUring-tested Student modeling in Knowledge Tracing)
* **Pendekatan Inovatif/Kebaruan Utama:** Mengekstrak dan memanfaatkan jejak goresan tulisan tangan pemecahan masalah siswa (*written problem-solving processes - PSPs*) melalui teknologi OCR, yang kemudian disuling menggunakan arsitektur kolaboratif *Teacher GPT* dan *Student GPT* menjadi indikator kemahiran matematika terstruktur, menggantikan ketergantungan sempit pada sekadar benar/salah jawaban akhir.
* **Detail Komponen (Singkat):** Modul OCR pemroses tulisan tangan, pipeline prompting Teacher-Student GPT untuk ekstraksi indikator penalaran matematis, modul pembuat representasi diskrit status kognitif, dan integrasi fleksibel ke 10 model dasar KT (DKT, AKT, SAINT, stableKT, dll).

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** Dataset kurikulum matematika KT-PSP-25 (dikumpulkan dari platform edukasi mobile interaktif *QANDA / Mathpresso*).
* **Skor AUC (Area Under ROC):** Skor STATUSKT pada model-model KT inti:
  * STATUSKT + stableKT: **0.6773** (Baseline: 0.6735)
  * STATUSKT + simpleKT: **0.6639** (Baseline: 0.6591)
  * STATUSKT + AKT: **0.6629** (Baseline: 0.6524)
  * STATUSKT + SAINT: **0.6401** (Baseline: 0.6201)
  * STATUSKT + DKVMN: **0.6220** (Baseline: 0.6049)
  * STATUSKT + DKT: **0.6197** (Baseline: 0.6165)
* **Skor Lain (ACC / RMSE / F1-Score):**
  * Accuracy (ACC): **0.7459** (simpleKT), **0.7435** (AKT), **0.7421** (stableKT), **0.7410** (DKVMN), **0.7377** (SAINT), **0.7235** (DKT).

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Diuji menggunakan jutaan data tulisan tangan nyata dari platform bimbingan belajar komersial *QANDA* (aplikasi edutech mobile berskala internasional).
* **Temuan Kunci (Kontribusi):** Menunjukkan bahwa sekadar memasukkan teks bebas proses pengerjaan menimbulkan noise, namun mendistilasinya menjadi indikator penalaran kognitif terstruktur (STATUSKT) secara konsisten meningkatkan daya prediksi seluruh keluarga model KT dan menyajikan diagnosa kelemahan siswa yang dapat dijelaskan secara pedagogis.

---

## PAPER 21
### 1. IDENTITAS PAPER
* **Judul Lengkap:** Unlocking Math Potential: EDSense - A Personalized Intervention Tool for Children with Dyscalculia
* **Penulis Utama & Tahun:** Dipti Jadhav, Sarat Kumar Chettri, Amiya Kumar Tripathy, Om Ghate, Raj Chaudhari, Sarvesh Avhad (2023)

### 2. DOMAIN PEMBELAJARAN & KNOWLEDGE COMPONENTS (KC)
* **Domain Kognitif:** Math Problem Solving (Pendidikan Khusus / Diskalkulia Anak Usia Dini)
* **Definisi KC:** Fondasi kepekaan bilangan (*number sense*) dan keterampilan matematika primer: perbandingan titik (*dot comparison*), subitasi (*subitizing*), perbandingan angka, garis bilangan mental, pencacahan (*counting*), penjumlahan, pengurangan, dan perkalian.

### 3. ARSITEKTUR AI & PENDEKATAN INOVATIF
* **Nama Arsitektur Inti:** EDSense Bayesian Knowledge Tracing (BKT) berbasis Directed Acyclic Graph (DAG)
* **Pendekatan Inovatif/Kebaruan Utama:** Menyesuaikan model probabilistik Bayesian Knowledge Tracing khusus untuk karakteristik anak penderita diskalkulia (gangguan belajar berhitung); mengintegrasikan parameter kecepatan respon/waktu pengerjaan (*response speed & completion time*) bersama parameter ketepatan (*accuracy*) untuk diagnosis dini dan rekomendasi latihan visual multisensori.
* **Detail Komponen (Singkat):** Graf asiklik terarah (DAG) permodelan dependensi probabilitas transisi konsep belajar, 4 parameter psikometri standar BKT ($P(L_0), P(T), S, G$), antarmuka interaktif audio-visual ramah anak, dan modul diagnosis klinis.

### 4. DATASET & METRIK PERFORMA
* **Nama Dataset:** Dataset studi empiris 137 anak usia 6–10 tahun di Mumbai yang dievaluasi menggunakan platform pembelajaran matematika adaptif daring *Smartick*.
* **Skor AUC (Area Under ROC):** *N/A (Studi klinis/kasus komparatif berbasis psikometri deskriptif dan akurasi waktu)*
* **Skor Lain (ACC / RMSE / F1-Score):** Evaluasi akurasi performa pengerjaan, kecepatan respon (*speed*), dan waktu penyelesaian tugas terdistribusi; validasi prototipe berhasil diuji dan diverifikasi oleh pakar penanganan diskalkulia.

### 5. IMPLEMENTASI ITS & TEMUAN KUNCI
* **Status Implementasi ITS:** Diimplementasikan sebagai prototipe perangkat lunak antarmuka sistem intervensi cerdas teruji (EDSense prototype) berbasis asesmen platform edukasi adaptif Smartick.
* **Temuan Kunci (Kontribusi):** Memperluas cakupan Intelligent Tutoring System ke ranah pendidikan inklusif anak berkebutuhan khusus. EDSense membuktikan bahwa pemodelan probabilistik BKT yang diperkaya metrik waktu mampu mendeteksi pola kelemahan diskalkulia secara dini dan menyediakan intervensi ajar yang tepat sasaran.
