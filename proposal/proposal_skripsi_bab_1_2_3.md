# PROPOSAL SKRIPSI

## PENGEMBANGAN WEB EVALUASI FORMATIF ADAPTIF BERBASIS KNOWLEDGE TRACING DAN RETRIEVAL-AUGMENTED GENERATION (LOGITRACE) DALAM PEMBELAJARAN STATION ROTATION UNTUK MENINGKATKAN LOGICAL THINKING SISWA SMK

Disusun untuk memenuhi salah satu syarat memperoleh gelar Sarjana Pendidikan (S.Pd.) pada Program Studi Pendidikan Ilmu Komputer

**Oleh:**  
**Fajari Arkan Fadhlurrahman**  
**NIM. 2304794**

---

**PROGRAM STUDI PENDIDIKAN ILMU KOMPUTER**  
**FAKULTAS PENDIDIKAN MATEMATIKA DAN ILMU PENGETAHUAN ALAM**  
**UNIVERSITAS PENDIDIKAN INDONESIA**  
**BANDUNG**  
**2026**

---

# KATA PENGANTAR

Puji dan syukur senantiasa penulis panjatkan ke hadirat Tuhan Yang Maha Esa atas limpahan rahmat, taufik, serta hidayah-Nya, sehingga penulis dapat menyelesaikan penyusunan naskah proposal skripsi yang berjudul **"Pengembangan Web Evaluasi Formatif Adaptif Berbasis Knowledge Tracing dan Retrieval-Augmented Generation (LogiTrace) dalam Pembelajaran Station Rotation untuk Meningkatkan Logical Thinking Siswa SMK"** dengan baik dan tepat waktu. Proposal skripsi ini diajukan sebagai salah satu syarat akademis untuk menempuh mata kuliah Skripsi pada Program Studi Pendidikan Ilmu Komputer, Fakultas Pendidikan Matematika dan Ilmu Pengetahuan Alam, Universitas Pendidikan Indonesia.

Penyusunan penelitian ini berakar dari permasalahan empiris di lapangan mengenai kesenjangan evaluasi formatif kejuruan dan keterbatasan fasilitas laboratorium komputer di Sekolah Menengah Kejuruan (SMK). Mengacu pada temuan **Tinjauan Sistematis (*Systematic Literature Review* / SLR)** terhadap 21 artikel Scopus (2021–2026) mengenai pemodelan penalaran logis dalam *Knowledge Tracing* (KT) dan *Intelligent Tutoring Systems* (ITS), terungkap bahwa model *Deep Knowledge Tracing* (DKT) monolitik konvensional yang dilatih pada ratusan ribu data interaksi tidak layak diterapkan pada domain kurikulum kejuruan skala kelas (34 siswa) karena ketiadaan dataset perilaku publik dan risiko *overfitting* yang parah. Berangkat dari kesenjangan tersebut, penelitian ini mengembangkan sistem **LogiTrace**. LogiTrace menerapkan paradigma *Training-Free Knowledge Tracing* yang menggeser kebutuhan data dari korpus perilaku siswa ke korpus konten kurikulum melalui integrasi *Retrieval-Augmented Generation* (RAG) dan model bahasa besar (*Large Language Model* / LLM) lokal yang dibekukan (*frozen*), dipadukan dengan aturan pembaruan penguasaan kognitif deterministik yang transparan dan dapat diaudit. Sistem ini diorkestrasikan ke dalam ruang kelas kejuruan melalui model *Station Rotation* dengan strategi *Device-Purpose Split* guna memperkuat kemampuan berpikir logis (*Logical Thinking*) siswa pada materi teknologi jaringan nirkabel.

Penulis menyadari sepenuhnya bahwa penyelesaian proposal ini tidak terlepas dari bimbingan, arahan metodologis, dan doa dari berbagai pihak. Oleh sebab itu, penulis menyampaikan rasa hormat dan terima kasih yang mendalam kepada:
1. Bapak/Ibu Dosen Pembimbing Skripsi Departemen Pendidikan Ilmu Komputer FPMIPA UPI yang senantiasa meluangkan waktu, memberikan bimbingan yang kritis, arahan metodologis yang ketat, serta motivasi berharga bagi penyempurnaan desain penelitian ini.
2. Ketua dan Sekretaris Departemen Pendidikan Ilmu Komputer FPMIPA UPI beserta seluruh jajaran dosen dan tenaga kependidikan atas bekal keilmuan dan fasilitasi selama masa perkuliahan.
3. Bapak Yofi Fikri Islami Anshary, S.Pd., selaku guru kejuruan Konsentrasi Keahlian Teknik Komputer dan Jaringan (TKJ) SMKN 4 Bandung, atas keterbukaan kemitraan, wawasan empiris kondisi laboratorium, dan kerja sama selama studi pendahuluan.
4. Kedua orang tua dan keluarga tercinta atas untaian doa yang tiada putus, pengorbanan, kasih sayang, dan dukungan moral material yang senantiasa menjadi sumber kekuatan penulis.
5. Rekan-rekan mahasiswa Program Studi Pendidikan Ilmu Komputer FPMIPA UPI angkatan 2023 atas diskusi ilmiah, solidaritas, dan kebersamaan dalam proses akademik.

Penulis menyadari bahwa naskah proposal ini masih memiliki keterbatasan. Kritik dan masukan yang membangun sangat penulis harapkan demi kesempurnaan implementasi penelitian di masa mendatang. Semoga karya ini dapat memberikan sumbangsih nyata bagi inovasi teknologi pendidikan kejuruan di Indonesia.

Bandung, 2026  
Penulis,  

**Fajari Arkan Fadhlurrahman**  
NIM. 2304794  

---

# DAFTAR ISI

- **KATA PENGANTAR**
- **DAFTAR ISI**
- **BAB I PENDAHULUAN**
  - 1.1 Latar Belakang Masalah
  - 1.2 Rumusan Masalah
  - 1.3 Tujuan Penelitian
  - 1.4 Manfaat Penelitian
  - 1.5 Struktur Organisasi Skripsi
- **BAB II TINJAUAN PUSTAKA**
  - 2.1 Peta Literatur dan Paradigma Pergeseran Data Berbasis SLR (2021–2026)
  - 2.2 Evaluasi Formatif Adaptif dan Scaffolding Sokratik
    - 2.2.1 Konsep dan Fungsi Evaluasi Formatif Diagnostik
    - 2.2.2 Personalisasi Pembelajaran dan Asesmen Adaptif dalam ZPD
  - 2.3 Pelacakan Pengetahuan: Dari BKT, DKT, Menuju RAG-KT Tanpa Pelatihan
    - 2.3.1 Konsep Knowledge Tracing dan Keterbatasan Model Berbasis Korpus Perilaku
    - 2.3.2 Paradigma Training-Free Knowledge Tracing Berbasis Konten Kurikulum
  - 2.4 Arsitektur Tiga Lapis Sistem LogiTrace Berlandaskan Temuan SLR
    - 2.4.1 Lapisan 1 (L1) — Basis Pengetahuan (Knowledge Base)
    - 2.4.2 Lapisan 2 (L2) — Indeks Butir dan Pelabelan Semantik Otomatis
    - 2.4.3 Lapisan 3 (L3) — Mesin Runtime Deterministik dan Agen RAG Tiga Pemicu
  - 2.5 Model Pembelajaran Blended Learning Tipe Station Rotation
    - 2.5.1 Konsep Dasar Blended Learning dan Model Rotasi
    - 2.5.2 Sintaks Pembelajaran Station Rotation 3 Stasiun Terpadu
    - 2.5.3 Strategi Device-Purpose Split untuk Mengatasi Rasio Lab (1 PC : 2 Siswa)
  - 2.6 Kemampuan Logical Thinking dalam Bidang Jaringan Komputer
    - 2.6.1 Hakikat Logical Thinking dan Perkembangan Kognitif Formal
    - 2.6.2 Kerangka Kerja Penalaran Kausal dan Troubleshooting Jonassen & Hung (2006)
    - 2.6.3 Operasionalisasi 5 Fase Kognitif Troubleshooting pada Materi Jaringan Nirkabel TKJ
  - 2.7 Materi Teknologi Jaringan Nirkabel sebagai Domain Pengetahuan
    - 2.7.1 Konsep Dasar dan Topologi Jaringan Nirkabel (Ad-Hoc vs Infrastruktur)
    - 2.7.2 Konfigurasi Perangkat Nirkabel, SSID, dan Keamanan Autentikasi
    - 2.7.3 Troubleshooting Konektivitas Nirkabel dan Pengujian Diagnostik ICMP
  - 2.8 Kajian Metodologis
    - 2.8.1 Model Pengembangan Sistem R&D (Borg & Gall, Judijanto et al., ADDIE Branch)
    - 2.8.2 Perangkat Pengembangan Sistem Web Cerdas dan Arsitektur Model Bahasa Klien Aman (Zero-PII)
    - 2.8.3 Instrumen Evaluasi Kualitas Media (Validitas LORI 2.0 & Usabilitas SUS)
    - 2.8.4 Desain Penelitian Pra-Eksperimen (One-Group Pretest-Posttest Design & Sensus Kelas)
    - 2.8.5 Asesmen Kemampuan Kognitif dan Analisis Kualitas Butir Tes (Teori Tes Klasik / CTT)
    - 2.8.6 Teknik Pengumpulan Data dan Skala Pengukuran (Skala Likert 4 Poin)
    - 2.8.7 Teknik Analisis Data Statistik (N-Gain, Uji Prasyarat, Paired t-Test, dan Repeated Measures ANOVA Antar-Dimensi)
  - 2.9 Kajian Penelitian Terdahulu yang Relevan (Matriks Sintesis Literatur 21 Artikel SLR)
  - 2.10 Kerangka Berpikir (Conceptual Framework)
- **BAB III METODOLOGI PENELITIAN**
  - 3.1 Jenis dan Model Pengembangan Penelitian (Model ADDIE)
  - 3.2 Prosedur Penelitian dan Pengembangan Sistem LogiTrace
    - 3.2.1 Tahap Studi Pendahuluan (General Research Phase)
    - 3.2.2 Tahap Pengembangan Sistem LogiTrace (Model ADDIE)
      - A. Tahap Analisis (Analysis)
      - B. Tahap Perancangan (Design)
      - C. Tahap Pengembangan (Development)
      - D. Tahap Implementasi (Implementation)
      - E. Tahap Evaluasi (Evaluation)
    - 3.2.3 Tahap Akhir dan Pelaporan (Reporting Phase)
  - 3.3 Desain Uji Coba Produk dan Pembelajaran
    - 3.3.1 Desain Pra-Eksperimen Satu Kelompok dengan Kontrol Efek Tes (Bentuk Paralel & NEDV)
    - 3.3.2 Subjek, Tempat Penelitian, dan Analisis Kekuatan Statistik (Power Analysis)
  - 3.4 Instrumen Pengumpulan Data
    - 3.4.1 Instrumen Non-Tes (Lembar Validasi LORI 2.0 & Angket Usability SUS)
    - 3.4.2 Bank Butir Soal Kuis Adaptif dan Instrumen Tes Penalaran Troubleshooting Jaringan
    - 3.4.3 Pengujian Kualitas Butir Tes Berbasis Teori Tes Klasik (CTT)
    - 3.4.4 Skema Basis Data dan Log Transaksi Interaksi (Append-Only)
    - 3.4.5 Teknik Pengumpulan Data Komprehensif (Observasi, Wawancara, Angket, Tes)
  - 3.5 Rencana Evaluasi Sistem Komprehensif (Jalur E1 hingga E6 Menjawab Agenda Riset SLR)
    - 3.5.1 Jalur E1 — Validitas Isi dan Akurasi Pemetaan Semantik (Cohen's Kappa & Aiken's V)
    - 3.5.2 Jalur E2 — Evaluasi Kualitas Mutu Petunjuk Sokratik RAG (ICC)
    - 3.5.3 Jalur E3 — Evaluasi Akurasi Prediksi Pasca-Kalibrasi terhadap Tiga Model Pembanding
    - 3.5.4 Jalur E4 — Pengujian Reliabilitas dan Stabilitas Model Bahasa (Multi-Provider)
    - 3.5.5 Jalur E5 — Evaluasi Kelayakan Teknis, Latensi, dan Usability Pengguna (SUS)
    - 3.5.6 Jalur E6 — Analisis Indikasi Awal Dampak Belajar (N-Gain, Cohen's d_z, dan Repeated Measures ANOVA)
    - 3.5.7 Pemantauan Kesetiaan Perlakuan (Treatment Fidelity)
  - 3.6 Etika Penelitian dan Keamanan Data Siswa
  - 3.7 Keterbatasan Penelitian
  - 3.8 Jadwal dan Peta Jalan Penelitian (14 Minggu)
- **DAFTAR PUSTAKA**
- **LAMPIRAN**
  - Lampiran 1. Kisi-kisi Rubrik Validasi Ahli Media (Adaptasi LORI 2.0)
  - Lampiran 2. Kisi-kisi Rubrik Validasi Ahli Materi (Materi Jaringan Nirkabel & Penalaran Logis)
  - Lampiran 3. Kuesioner System Usability Scale (SUS)
  - Lampiran 4. Kisi-kisi Instrumen Tes Kemampuan Logical Thinking Berbasis Penalaran Troubleshooting Jaringan
  - Lampiran 5. Contoh Struktur Dokumen Knowledge Component (KC) dan DAG Prasyarat

---

# BAB I
# PENDAHULUAN

## 1.1 Latar Belakang Masalah

Perkembangan teknologi kecerdasan buatan (*Artificial Intelligence*) dan transformasi digital pada era Industri 4.0 dan Society 5.0 telah mendisrupsi lanskap pendidikan kejuruan dan kualifikasi tenaga kerja global. Ekosistem industri jaringan komputer modern kini tidak lagi sekadar menuntut teknisi yang menguasai keterampilan operasional prosedural, melainkan menuntut sumber daya manusia yang memiliki kecakapan kognitif tingkat tinggi, khususnya kemampuan berpikir logis (*logical thinking*) dalam menganalisis relasi kausalitas sistem, mendiagnosis anomali konektivitas, serta memecahkan permasalahan teknis yang kompleks (Bohle Carbonell et al., 2014; Wardani et al., 2022). Sejalan dengan pergeseran kurikulum global yang menekankan *computational thinking* dan pemecahan masalah multi-langkah (Wing, 2006), pemanfaatan kecerdasan buatan dalam pendidikan (*Artificial Intelligence in Education* / AIEd) berkembang pesat guna menghadirkan sistem evaluasi formatif adaptif yang mampu mempersonalisasi bimbingan belajar sesuai dinamika pemahaman masing-masing peserta didik.

Secara ideal, pendidikan kejuruan berfungsi menyiapkan peserta didik agar memiliki kompetensi kerja yang relevan, mandiri, dan berdaya adaptasi tinggi terhadap dinamika industri, sebagaimana diamanatkan dalam Undang-Undang Nomor 20 Tahun 2003 tentang Sistem Pendidikan Nasional (Republik Indonesia, 2003). Untuk mencapai standar mutu tersebut, proses pembelajaran kejuruan idealnya ditopang oleh evaluasi formatif yang bersifat diagnostik dan berkelanjutan. Evaluasi formatif yang efektif berfungsi memetakan lintasan pemahaman konsep peserta didik secara berkala, mendeteksi miskonsepsi secara dini, memberikan umpan balik tepat waktu, serta melatih daya nalar logis agar siswa mampu memahami relasi sebab-akibat dari setiap parameter konfigurasi teknis (Black & Wiliam, 1998; Hattie & Timperley, 2007; Sadler, 1989). Dengan pemahaman logika formal yang matang, peserta didik bertransformasi menjadi praktisi yang adaptif (*adaptive experts*) dan terhindar dari ketergantungan hafalan prosedural yang kaku (*procedural rigidity*).

Kendati demikian, kenyataan di lapangan menunjukkan adanya kesenjangan yang signifikan dari kondisi ideal tersebut. Praktik evaluasi formatif pada pembelajaran kejuruan di Sekolah Menengah Kejuruan (SMK) selama ini umumnya masih bersifat konvensional, seragam, dan statis (Robins et al., 2003; Sudira, 2017). Asesmen formatif kerap direduksi menjadi sekadar tes berkala yang mendistribusikan butir soal yang identik kepada seluruh siswa tanpa mempertimbangkan keberagaman kecepatan belajar individu. Di sisi lain, proses pembelajaran praktik kejuruan cenderung terdistorsi pada pencapaian tugas fisik semata (*task completion* mekanis), di mana siswa sekadar meniru buku panduan operasional tanpa menginternalisasi landasan logika di balik instruksi kerja yang dilakukan (Sudira, 2017).

Fakta kesenjangan ini terkonfirmasi secara nyata melalui studi pendahuluan yang dilaksanakan di SMKN 4 Bandung pada Konsentrasi Keahlian Teknik Komputer dan Jaringan (TKJ). Berdasarkan wawancara mendalam dengan guru mata pelajaran kejuruan (Bapak Yofi Fikri Islami Anshary, S.Pd.) dan observasi kelas pada mata pelajaran Teknologi Jaringan Kabel dan Nirkabel di kelas XI TKJ 1, terungkap bahwa kelas tersebut merupakan rombongan belajar dengan proporsi siswa remedial tertinggi pada evaluasi formatif sementara dibandingkan kelas paralel lainnya. Guru mengungkapkan bahwa dalam pembelajaran materi jaringan nirkabel (*WLAN*), kendala terbesar siswa bukan terletak pada pemasangan fisik perangkat, melainkan pada kelemahan penalaran logika saat menghubungkan konsep topologi dengan pengujian komunikasi antar-perangkat (*challenge pengujian ICMP peer-to-peer*). Siswa kerap mengalami disorientasi dan kebuntuan saat mencari akar penyebab mengapa dua laptop tidak dapat saling bertukar data padahal *Service Set Identifier* (SSID) telah terasosiasi. Ketika menghadapi galat sistem, guru membiasakan siswa untuk mencoba menelusuri secara mandiri sebelum meminta bantuan; namun ketiadaan panduan bertahap (*scaffolding*) yang adaptif menyebabkan sebagian besar siswa terjebak pada spekulasi acak atau bergantung sepenuhnya pada rekan sekelas.

Kondisi tersebut semakin diperberat oleh keterbatasan fasilitas laboratorium komputer sekolah. Ketersediaan unit komputer di laboratorium berada pada rasio rata-rata 1 unit PC digunakan bersama oleh 2 orang siswa (1:2) yang dibagikan secara acak. Guru mengonfirmasi bahwa pola kerja berpasangan ini memicu fenomena pasangan dominan-pasif (*dominant-passive pair*), di mana siswa yang lebih aktif mendominasi papan ketik dan tetikus, sementara pasangannya pasif sekadar mengamati. Situasi ini menyulitkan pendidik dalam mengukur capaian kognitif murni tiap individu karena penilaian praktikum kerap bercampur dengan hasil kerja kelompok. Di sisi lain, bimbingan diagnostik terarah (*targeted scaffolding*) baru dapat diberikan oleh guru secara manual saat sesi remedial di ujung pokok bahasan karena keterbatasan alokasi waktu jam pelajaran tatap muka (Truitt & Ku, 2018).

Untuk memecahkan persoalan personalisasi evaluasi, literatur komputasi pendidikan secara luas mengajukan paradigma *Knowledge Tracing* (KT) guna memetakan status penguasaan konsep (*knowledge state*) siswa secara berkelanjutan (Corbett & Anderson, 1994; Piech et al., 2015; Abdelrahman et al., 2023; Shen et al., 2024). Namun demikian, berdasarkan **Tinjauan Sistematis (*Systematic Literature Review* / SLR)** yang komprehensif terhadap 21 artikel Scopus (2021–2026) mengenai pemodelan penalaran logis dalam KT dan *Intelligent Tutoring Systems* (ITS), terungkap adanya **tiga kesenjangan kritis (*critical gaps*)** yang melandasi urgensi desain penelitian ini:
1. **Keterbatasan Matematis DKT pada Data Terbatas (*Small Data Regime*):**  
   Model *Deep Knowledge Tracing* (DKT) monolitik konvensional berbasis jaringan saraf tiruan (RNN/LSTM) mensyaratkan korpus data perilaku siswa dalam jumlah masif (sering kali 100.000 hingga jutaan interaksi). Pada penelitian skala kelas kejuruan (34 siswa), melatih jaringan saraf DKT dari nol (*from scratch*) menghasilkan rasio parameter terhadap data yang sangat timpang (~440 parameter per interaksi), sehingga model mengalami *overfitting* parah di mana jaringan menghafal identitas siswa alih-alih mengabstraksi konsep. Temuan SLR mengonfirmasi bahwa pada domain penalaran logika formal dengan sampel terbatas, DKT standar bahkan gagal memprediksi kelas langka dengan nilai $F_1 = 0{,}0$ (Nkambou et al., 2023). Pendekatan mutakhir yang mencoba mentransfer representasi generatif seperti CLST (Jung et al., 2025) pada kondisi data sedikit (8 siswa) hanya mencapai AUC 0,635–0,689 dan tetap menuntut *fine-tuning* LoRA pada korpus data siswa lain.
2. **Ketiadaan Konstruk Penalaran Logis Terukur pada Domain Kejuruan:**  
   Temuan SLR membuktikan bahwa dari 21 studi terkini, mayoritas terkonsentrasi pada matematika dan pemrograman umum dengan dataset standar seperti ASSISTments (6 artikel) dan EdNet (3 artikel). Hanya dua artikel dari satu kelompok peneliti (Nkambou et al., 2023; Tato & Nkambou, 2022) yang menangani logika formal (keduanya berbasis ITS Logic-Muse), dan **tidak ada satu pun artikel yang mendefinisikan *computational thinking* atau *logical thinking* sebagai konstruk kognitif terukur** pada kurikulum kejuruan teknologi informasi dan jaringan. Terlebih lagi, **tidak tersedia dataset publik terbuka untuk materi jaringan komputer vokasi**.
3. **Kesenjangan antara Akurasi Prediksi Luring dan Intervensi Kelas Nyata:**  
   Mayoritas studi KT mengevaluasi model secara luring (*offline*) pada log interaksi statis, dan sangat sedikit yang menguji dampaknya secara langsung pada kelas fisik dengan kontrol desain terstandar (Shukla et al., 2026; Wang et al., 2024, 2026; Zhao et al., 2026). Selain itu, sistem bimbingan belajar berbasis LLM kerap kali bertindak sebagai penjawab reaktif langsung (*instant solvers*) yang justru merusak proses pergulatan kognitif produktif (*productive struggle*) siswa (Wang et al., 2026).

Menghadapi ketiga kesenjangan tersebut, penelitian ini merumuskan pergeseran paradigma mendasar: **kebutuhan data digeser dari korpus perilaku siswa (yang tidak tersedia) menuju korpus konten kurikulum (yang dapat ditulis secara terstruktur oleh pendidik)**. Pergeseran ini melahirkan pendekatan *Training-Free Knowledge Tracing* yang diwujudkan melalui sistem **LogiTrace**. LogiTrace memanfaatkan teknologi *Retrieval-Augmented Generation* (RAG) yang dipadukan dengan model bahasa besar (*Large Language Model* / LLM) lokal yang dibekukan (*frozen*). Dalam LogiTrace, LLM tidak dilatih ulang dan tidak digunakan untuk menghitung probabilitas matematis; LLM difungsikan secara spesifik untuk membaca teks butir soal, melakukan pelabelan semantik ganda ke dalam *Knowledge Component* (KC) dan dimensi *Logical Thinking*, serta menyusun bantuan petunjuk Sokratik berjenjang mengadopsi prinsip *"Guiding, Not Solving"* (Wang et al., 2026). Sementara itu, status penguasaan kognitif siswa dimodelkan dan diperbarui menggunakan **aturan deterministik berbasis bukti yang transparan, dapat diaudit, dan dieksekusi secara seketika (< 1 ms)**.

Agar sistem perangkat lunak ini tidak terisolasi sebagai aplikasi daring mandiri semata di ruang hampa, LogiTrace diintegrasikan langsung ke dalam dinamika ruang kelas kejuruan melalui model *blended learning* tipe **Station Rotation satu ruangan (*single-room lab zoning*)** dengan menerapkan strategi **Device-Purpose Split**. Model pembelajaran ini diposisikan sebagai satu kesatuan ekosistem pembelajaran terpadu (*integrated instructional ecosystem*). Melalui penataan zonasi terpadu di dalam laboratorium komputer sekolah, separuh rombongan belajar (17 siswa) mengerjakan evaluasi kognitif adaptif secara mandiri melalui telepon pintar (*smartphone*) pribadi di stasiun digital sehingga menjamin kemurnian data rekaman kognitif individu (*pure individual cognitive trace*), di mana pendidik berperan aktif berkeliling (*roving teacher*) memberikan bimbingan diagnostik terarah secara privat kepada siswa yang mengalami kebuntuan berdasarkan pemantauan dasbor seketika (*ambient real-time dashboard*). Pada saat yang bersamaan, separuh rombongan belajar lainnya melaksanakan unjuk kerja konfigurasi jaringan fisik di meja komputer laboratorium dengan rasio ideal 1 PC untuk 1 siswa. Pengaturan ini meniadakan waktu perpindahan antar-ruangan (*zero transit loss*), mengeliminasi stigma sosial pemisahan siswa remedial, serta memastikan bahwa perbaikan rasio fasilitas laboratorium (1:1) merupakan bagian yang sengaja direkayasa (*deliberate instructional design*) dari model rotasi tersebut.

Berdasarkan latar belakang masalah, urgensi personalisasi asesmen, serta landasan empiris tinjauan sistematis literatur terkini, maka penelitian pengembangan (*Research and Development*) ini diberi judul:

> **"Pengembangan Web Evaluasi Formatif Adaptif Berbasis Knowledge Tracing dan Retrieval-Augmented Generation (LogiTrace) dalam Pembelajaran Station Rotation untuk Meningkatkan Logical Thinking Siswa SMK"**

---

## 1.2 Rumusan Masalah

Berdasarkan batasan masalah dan identifikasi kesenjangan di atas, rumusan masalah dalam penelitian ini dirumuskan sebagai berikut:
1. Bagaimana rancang bangun sistem web evaluasi formatif adaptif LogiTrace berbasis arsitektur tiga lapis (*Knowledge Base*, *Item Indexing*, dan *Deterministic Runtime Engine* dengan agen RAG tiga pemicu) yang terintegrasi ke dalam model pembelajaran *Station Rotation*?
2. Bagaimana kelayakan (validitas isi, mutu petunjuk, dan kepraktisan) sistem LogiTrace berdasarkan penilaian ahli materi dan ahli media mengacu pada rubrik LORI 2.0, kesepakatan pelabelan semantik Cohen's $\kappa$, serta respons penerimaan siswa menggunakan instrumen *System Usability Scale* (SUS)?
3. Bagaimana akurasi prediksi status penguasaan konsep sistem LogiTrace pada fase pasca-kalibrasi apabila dibandingkan secara empiris terhadap tiga model pembanding tanpa-latih (*base rate*, *running accuracy*, dan *difficulty-only model*)?
4. Bagaimana peningkatan kemampuan *Logical Thinking* siswa setelah mengikuti model pembelajaran *Station Rotation* berbantuan LogiTrace sebagai satu kesatuan ekosistem pembelajaran terpadu, bagaimana profil ukuran efek peningkatannya di seluruh fase kognitif penalaran troubleshooting Jonassen (*Symptom Recognition*, *Problem Space Construction*, *Fault Hypothesis Generation*, *Hypothesis Testing & Evaluation*, dan *Corrective Action & Verification*), serta bagaimana kontribusi spesifik interaksi digital siswa dianalisis melalui hubungan dosis-respons (*dosage-response*)?

---

## 1.3 Tujuan Penelitian

Berdasarkan rumusan masalah tersebut, tujuan yang hendak dicapai dalam penelitian ini adalah:
1. Menghasilkan produk web evaluasi formatif adaptif LogiTrace dengan arsitektur tiga lapis yang menghubungkan basis pengetahuan kurikulum, pelabelan otomatis LLM, mesin inferensi penguasaan deterministik, dan tiga pemicu agen RAG ke dalam sintaks pembelajaran *Station Rotation*.
2. Menguji kelayakan sistem LogiTrace ditinjau dari validitas media dan materi berbasis LORI 2.0, konsistensi pelabelan pakar versus model, mutu pedagogis petunjuk Sokratik, serta tingkat kepraktisan pengguna (*usability*) berbasis skor SUS.
3. Mengukur dan membuktikan akurasi prediktif sistem LogiTrace pasca-kalibrasi secara ketat terhadap tiga model *baseline* tanpa pelatihan menggunakan metrik akurasi, Brier score, dan uji signifikansi McNemar serta bootstrap.
4. Menganalisis besaran peningkatan kemampuan *Logical Thinking* siswa melalui analisis *N-Gain* dan ukuran efek berpasangan *Cohen's* $d_z$, memetakan profil keseimbangan peningkatan di seluruh fase kognitif penalaran troubleshooting Jonassen melalui analisis komparatif ukuran efek dan uji Repeated Measures ANOVA, serta membuktikan kontribusi empiris interaksi sistem melalui analisis hubungan dosis-respons (*dosage-response relationship*).

---

## 1.4 Manfaat Penelitian

Adapun manfaat teoretis dan praktis dari hasil penelitian pengembangan ini adalah sebagai berikut:
1. **Manfaat Teoretis:**  
   Memberikan bukti empiris bahwa pelacakan pengetahuan (*Knowledge Tracing*) dapat diimplementasikan secara valid pada rezim tanpa korpus data perilaku berskala besar (*training-free regime*) dengan menggeser representasi domain ke basis pengetahuan konten kurikulum yang dapat dibaca mesin. Selain itu, penelitian ini menyumbangkan kerangka kerja operasionalisasi penalaran logis formal ke dalam label ganda *Knowledge Component* (KC) $\times$ dimensi TOLT pada domain rekayasa jaringan komputer.
2. **Manfaat Praktis bagi Sekolah dan Guru:**  
   Menyediakan solusi manajerial kelas (*Device-Purpose Split*) untuk mengatasi keterbatasan rasio laboratorium komputer (1 PC : 2 siswa) menjadi rasio ideal (1 PC : 1 siswa) tanpa menambah pengadaan unit perangkat keras baru. Guru memperoleh instrumen evaluasi formatif cerdas yang dilengkapi dasbor orkestrasi seketika (*real-time*) untuk memandu bimbingan kelompok kecil yang tepat sasaran.
3. **Manfaat Praktis bagi Siswa:**  
   Memberikan pengalaman evaluasi yang terpersonalisasi di mana setiap siswa menerima tantangan soal sesuai zona perkembangan proksimalnya (*ZPD*), memperoleh bantuan petunjuk Sokratik bertahap tanpa membocorkan jawaban akhir, serta memperoleh hak mandiri penuh dalam mengoperasikan unit PC saat sesi praktikum laboratorium.

---

## 1.5 Struktur Organisasi Skripsi

Sistematika penulisan skripsi ini disusun sebagai berikut:

* **BAB I Pendahuluan:** Memuat latar belakang masalah pergeseran paradigma data evaluasi formatif berbasis tinjauan sistematis literatur Scopus 2021–2026, fenomena rasio lab di SMK mitra, rumusan masalah, tujuan, manfaat, dan sistematika penulisan.
* **BAB II Tinjauan Pustaka:** Menguraikan landasan teoretis evaluasi formatif diagnostik, sintesis tinjauan sistematis KT (2021–2026), pergeseran dari DKT konvensional menuju RAG-KT, spesifikasi arsitektur tiga lapis LogiTrace, model *Station Rotation*, kerangka kerja TOLT, materi teknologi jaringan nirkabel, kajian metodologis komprehensif (R&D, LORI, SUS, pra-eksperimen satu kelompok, CTT, dan Repeated Measures ANOVA), telaah 21 penelitian terdahulu yang relevan dari korpus SLR, serta kerangka berpikir penelitian.
* **BAB III Metodologi Penelitian:** Menjelaskan prosedur R&D model ADDIE yang diselaraskan dengan tahapan umum R&D, desain uji coba satu kelompok dengan instrumen paralel A/B dan butir kontrol NEDV, karakteristik sensus 34 siswa kelas XI TKJ 1 SMKN 4 Bandung, bank butir 180 soal, skema basis data *append-only*, serta rencana evaluasi sistem enam jalur (E1–E6) yang menjawab agenda riset SLR lengkap dengan etika dan batasan penelitian.
* **BAB IV Hasil Penelitian dan Pembahasan:** Menyajikan data hasil perancangan sistem LogiTrace, temuan validasi ahli materi dan media, hasil pengujian akurasi pelabelan semantik (E1), evaluasi mutu petunjuk Sokratik (E2), bukti empiris akurasi prediksi pasca-kalibrasi terhadap tiga baseline (E3), reliabilitas model bahasa (E4), kepraktisan SUS (E5), serta capaian peningkatan *Logical Thinking* dan uji keseimbangan profil penalaran TOLT via Repeated Measures ANOVA (E6) beserta analisis kesetiaan perlakuan (*fidelity*).
* **BAB V Kesimpulan, Implikasi, dan Rekomendasi:** Menyajikan simpulan akhir ketercapaian tujuan penelitian, implikasi pedagogis dan teknologis, keterbatasan penelitian yang teridentifikasi, serta rekomendasi bagi riset AIEd lanjutan.

---

# BAB II
# TINJAUAN PUSTAKA

## 2.1 Peta Literatur dan Paradigma Pergeseran Data Berbasis SLR (2021–2026)

Penelitian ini dibangun di atas sintesis kritis **Tinjauan Sistematis (*Systematic Literature Review* / SLR)** terhadap 21 artikel Scopus (2021–2026) yang mengkaji penerapan *Knowledge Tracing* (KT) dalam pemodelan penalaran logis, pemecahan masalah, dan pemrograman pada lingkungan pembelajaran adaptif dan ITS. Peta konseptual yang menghubungkan domain kejuruan teknik jaringan komputer dengan inovasi pemodelan kognitif cerdas tanpa pelatihan (*Training-Free Knowledge Tracing*) diilustrasikan pada Gambar 2.1.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            DOMAIN PENGETAHUAN                               │
│              Teknologi Jaringan Nirkabel & Troubleshooting ICMP             │
│            - 12 Knowledge Components (KC) Terstruktur & DAG Prasyarat        │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            KONSTRUK KOGNITIF                                │
│                   Logical Thinking (Tobin & Capie, 1981)                    │
│    5 Dimensi: Controlling Variables, Proportional, Combinatorial,           │
│               Probabilistic, dan Correlational Reasoning                    │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      SISTEM LOGITRACE (RAG-KT ENGINE)                       │
│      L1: Basis Pengetahuan (12 KC, DAG Prasyarat, 5 Fase Jonassen, 24 Contoh)        │
│      L2: Indeks Butir Semantik & Pelabelan Otomatis LLM Lokal (Frozen)      │
│      L3: Aturan Penguasaan Deterministik (<1 ms) & Agen RAG 3 Pemicu        │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ORKESTRASI INSTRUKSIONAL                            │
│     Model Station Rotation Satu Ruangan Lab dengan Device-Purpose Split     │
│      - Zona A (Stasiun Praktik Lab Mandiri): Rasio Optimal 1 PC : 1 Siswa   │
│      - Zona B (Stasiun Evaluasi Adaptif Mandiri & Bimbingan Terarah):       │
│        * Pengerjaan Kuis Adaptif Individual via Smartphone Pribadi Siswa    │
│        * Bimbingan Guru Bergerak (Roving Teacher) Berbasis Dasbor Real-Time │
│      - Transisi Instan Antar-Zona (1–2 Menit, Zero Transit Loss)            │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            LUARAN PENELITIAN                                │
│    Peningkatan Logical Thinking Ekosistemik, Keseimbangan Profil Kognitif,  │
│         dan Pemecahan Nyata Kendala Fasilitas Lab Sekolah Vokasi            │
└─────────────────────────────────────────────────────────────────────────────┘
```
**Gambar 2.1** Peta Konseptual Integrasi Sistem LogiTrace dalam Pembelajaran Kejuruan

Berdasarkan sintesis SLR, literatur KT mutakhir dikelompokkan ke dalam empat arus arsitektur utama:
1. **Model Psikometrik, Probabilistik, dan Faktorisasi:** Menangani data jarang dan granularitas langkah tanpa jaringan saraf berulang (Jadhav et al., 2023; Samonte et al., 2024; Wang et al., 2021; Xia et al., 2026; Zhang et al., 2025).
2. **Model Sekuensial dan Atensi Berpengetahuan Pakar:** Mengintegrasikan struktur graf konsep atau jaringan Bayesian buatan pakar untuk menstabilkan DKT pada sampel kecil (Huang et al., 2024; Nkambou et al., 2023; Tato & Nkambou, 2022; Xu et al., 2024).
3. **Model Graf dan Hipergraf Spasio-Temporal:** Memodelkan relasi tingkat tinggi antarkonsep serta dimensi afektif siswa (Huang et al., 2026; Li, 2026).
4. **Model Terintegrasi Large Language Models (LLM):** Memanfaatkan kekuatan representasi semantik LLM untuk anotasi kesulitan teks soal, ekstraksi penyebab kesalahan, dan penyusunan petunjuk Sokratik (Jung et al., 2025; Liang et al., 2023; Park et al., 2026; Shao et al., 2026; Shukla et al., 2026; Wang et al., 2026; Yang et al., 2025; Zhao et al., 2026).

Tabel 2.1 mempertegas perbandingan paradigma antara DKT konvensional dengan sistem LogiTrace yang dikembangkan dalam penelitian ini.

**Tabel 2.1** Perbandingan Paradigma: DKT Konvensional vs Sistem LogiTrace (RAG-KT)

| Dimensi Komparasi | Model Jaringan Saraf (DKT / RNN) | Sistem LogiTrace (RAG-KT) |
| :--- | :--- | :--- |
| **Hakikat Pemodelan Kognitif** | Estimasi probabilitas variabel laten (*latent state*) dari data perilaku masa lalu via *backpropagation* | Pembaruan status penguasaan berbasis aturan heuristik deterministik dipadukan dengan indeks semantik kurikulum |
| **Model Prediksi** | Jaringan saraf tiruan dilatih pada 100.000+ data interaksi | Tidak ada pelatihan model (*training-free*); aturan penguasaan deterministik eksplisit (< 1 ms) |
| **Representasi Pengetahuan** | Tersirat (*implicit*) di dalam matriks bobot jaringan numerik | Tertulis eksplisit dalam dokumen basis pengetahuan kurikulum yang dapat dibaca manusia |
| **Adaptasi Materi Baru** | Menuntut pengumpulan dataset baru dan pelatihan ulang (*retraining*) | Cukup menyunting dan memperbarui dokumen basis pengetahuan kurikulum |
| **Pemahaman Butir Soal** | Ko-okurensi statistik biner jawaban benar/salah | Representasi semantik: LLM membaca teks soal dan mencocokkan kemiripan vektor (*embedding*) |
| **Kebutuhan Data Minimum** | Korpus perilaku siswa berskala besar (*behavioral corpus*) | Korpus konten kurikulum yang terstruktur (*content corpus*) |
| **Metrik Evaluasi Utama** | Nilai global AUC (*Area Under ROC Curve*) | Akurasi pemetaan pakar ($\kappa$), akurasi prediksi pasca-kalibrasi, reliabilitas sistem |
| **Transparansi / Keterlacakan** | Kotak hitam (*black box*); sulit diverifikasi logikanya | Deterministik transparan; setiap pembaruan nilai penguasaan memiliki arti pedagogis dan dapat diaudit |

Kalimat kunci yang melandasi kebaruan ini adalah: *"Kebutuhan data bergeser dari korpus perilaku siswa ke korpus konten kurikulum."* Pergeseran inilah yang memungkinkan domain pendidikan vokasi yang tidak memiliki dataset publik berskala besar tetap dapat menerapkan asesmen adaptif cerdas secara valid.

---

## 2.2 Evaluasi Formatif Adaptif dan Scaffolding Sokratik

### 2.2.1 Konsep dan Fungsi Evaluasi Formatif Diagnostik
Evaluasi pendidikan membedakan dua orientasi utama: evaluasi sumatif (*assessment of learning*) yang bertujuan menetapkan vonis nilai akhir, dan evaluasi formatif (*assessment for learning*) yang berfungsi memperbaiki proses pembelajaran yang sedang berjalan (Black & Wiliam, 1998; Shute, 2008). Dalam konteks pendidikan kejuruan, evaluasi formatif mengemban fungsi diagnostik yang vital (Sudira, 2017). Evaluasi formatif diagnostik bertujuan mendeteksi miskonsepsi kognitif siswa sedini mungkin agar tidak berakumulasi menjadi kegagalan performa unjuk kerja di laboratorium.

Umpan balik formatif yang berkualitas harus memenuhi siklus *Feed Up* (kejelasan target kompetensi), *Feed Back* (posisi pemahaman saat ini), dan *Feed Forward* (rekomendasi tindakan perbaikan) (Hattie & Timperley, 2007). Dalam sistem LogiTrace, ketiga fungsi ini dioperasionalkan secara otomatis: sistem mendeteksi titik anomali penalaran siswa, memperbarui status penguasaan konsep, dan mengarahkan siswa ke materi prasyarat atau memberikan bantuan terarah.

### 2.2.2 Personalisasi Pembelajaran dan Asesmen Adaptif dalam ZPD
Personalisasi pembelajaran bertumpu pada teori perkembangan kognitif sosial Vygotsky (1978), khususnya konsep *Zone of Proximal Development* (ZPD). ZPD mendefinisikan rentang antara kemampuan pemecahan masalah mandiri siswa dengan tingkat kemampuan potensial yang dapat dicapai melalui bimbingan orang dewasa atau rekan sebaya yang lebih kompeten. Agar pembelajaran berlangsung efektif di dalam ZPD, lingkungan belajar harus menyediakan bantuan bertahap (*scaffolding*) yang dapat memudar (*fading*) seiring meningkatnya kemandirian siswa (Wood et al., 1976).

Mengadopsi prinsip desain dari Wang et al. (2026) dalam sistem SHARP (*Socratic Hinting for AI-Reinforced Programming*), bantuan pedagogis AI tidak boleh bertindak sebagai penjawab langsung (*direct solver*) yang merampas otonomi pembelajar. Oleh karena itu, bantuan Sokratik pada LogiTrace disajikan secara berjenjang dalam tiga level: Level 1 (mengarahkan fokus perhatian), Level 2 (memberikan satu langkah penalaran perantara), dan Level 3 (menyajikan kerangka konseptual penyelesaian). Bantuan ini dirancang secara ketat dengan pengaman kebocoran (*leakage guard*) agar tidak membocorkan kunci jawaban akhir, sehingga proses pergulatan kognitif produktif (*productive struggle*) siswa tetap terpelihara (Wang et al., 2026).

---

## 2.3 Pelacakan Pengetahuan: Dari BKT, DKT, Menuju RAG-KT Tanpa Pelatihan

### 2.3.1 Konsep Knowledge Tracing dan Keterbatasan Model Berbasis Korpus Perilaku
*Knowledge Tracing* (KT) adalah bidang pemodelan kognitif yang memetakan status penguasaan pengetahuan siswa secara sekuensial berdasarkan riwayat interaksi pengerjaan soal (Corbett & Anderson, 1994; Abdelrahman et al., 2023). Diberikan sekuens interaksi masa lalu $X = (x_1, x_2, \dots, x_t)$, model ditugaskan mengestimasi probabilitas keberhasilan siswa menjawab butir soal berikutnya $x_{t+1}$ pada konsep yang relevan.

Pendekatan klasik *Bayesian Knowledge Tracing* (BKT) menggunakan *Hidden Markov Model* (HMM) dengan asumsi independensi keterampilan yang kaku dan bergantung pada pemetaan graf konsep pakar (Corbett & Anderson, 1994). Untuk mengatasi kekakuan tersebut, Piech et al. (2015) memperkenalkan *Deep Knowledge Tracing* (DKT) berbasis jaringan *Long Short-Term Memory* (LSTM). Meskipun DKT unggul dalam memproses relasi laten non-linear, model ini menuntut ratusan ribu data interaksi (Shen et al., 2024). Pada penelitian skala kelas kejuruan (34 siswa), melatih jaringan saraf DKT secara langsung akan menimbulkan masalah *overfitting* yang parah di mana jaringan menghafal derau siswa alih-alih mengabstraksi struktur pengetahuan kurikulum.

Sebagaimana dibuktikan dalam temuan SLR (Nkambou et al., 2023), DKT monolitik juga rentan gagal pada konsep penalaran logika yang jarang dijawab benar oleh siswa ($F_1 = 0{,}0$). Di sisi lain, model adaptasi transfer semantik seperti CLST (Jung et al., 2025) pada data sedikit (8 siswa) hanya mencapai kisaran AUC 0,635–0,689, jauh di bawah batas stabilitas industri.

### 2.3.2 Klarifikasi Ontologis: Paradigma Training-Free Knowledge Tracing Berbasis Konten Kurikulum
Guna membangun landasan teoretis yang jujur, transparan, dan dapat dipertanggungjawabkan secara epistemologis di hadapan komunitas komputasi pendidikan, perlu ditegaskan batasan ontologis dari sistem LogiTrace dibandingkan model *Knowledge Tracing* (KT) konvensional:

1. **Bukan Estimasi Variabel Laten Probabilistik/Neural:**  
   Dalam literatur klasik AIEd (Corbett & Anderson, 1994; Piech et al., 2015; Abdelrahman et al., 2023), model seperti BKT dan DKT secara definitif memperlakukan pemahaman siswa sebagai **variabel laten tersembunyi (*latent cognitive state*)** yang diestimasi secara statistik dari ribuan sekuens data perilaku interaksi masa lalu (melalui algoritma *Expectation-Maximization* atau perambatan balik gradien kesalahan / *backpropagation*). Berbeda secara fundamental, Lapisan 3 (L3) sistem LogiTrace **tidak melakukan estimasi probabilitas variabel laten dari data riwayat**. Nilai status penguasaan $m_{s,k} \in [0{,}02;\ 0{,}98]$ merupakan **metrik penguasaan berbasis aturan (*rule-based mastery metric*)** yang diperbarui secara deterministik menggunakan aturan heuristik linier-logistik yang proporsional terhadap tingkat kesulitan soal ($d$) dan kemandirian respons ($h$).

2. **Kekuatan Teoretis Integrasi Indeks Semantik Kurikulum (RAG):**  
   Meskipun mesin runtime L3 bersifat deterministik, sistem ini tidak mengalami kekakuan model psikometrik statis karena beban representasi kognitif dialihkan dari bobot numerik jaringan saraf ke **basis pengetahuan semantik kurikulum yang kaya** pada Lapisan 1 (L1) dan Lapisan 2 (L2). Model bahasa besar (*frozen* LLM) dan indeks vektor semantik membaca teks soal, memetakan butir secara dinamis ke dalam ruang konseptual ganda (*Knowledge Component* $\times$ dimensi *Logical Thinking*), serta menyusun bimbingan Sokratik secara kontekstual. Dengan kata lain, kecerdasan sistem LogiTrace berakar pada **pemahaman semantik konten kurikulum (*curriculum content understanding*)**, bukan pada hafalan statistik pola jawaban siswa.

3. **Justifikasi Ilmiah untuk Skala Kelas Vokasi (34 Siswa):**  
   Penggunaan aturan pembaruan heuristik deterministik yang dipadukan dengan indeks kurikulum pakar bukanlah sebuah kelemahan kompromistis, melainkan **pilihan rekayasa instruksional yang paling superior dan rasional untuk rezim data terbatas (*small data regime*)**. Pada rombel 34 siswa vokasi, DKT terbukti secara matematis mengalami *overfitting* parah ($F_1 = 0{,}0$ pada penalaran langka, Nkambou et al., 2023) dan BKT kerap gagal mencapai konvergensi parameter. Sebaliknya, pendekatan heuristik deterministik LogiTrace menjamin: (a) stabilitas matematis tanpa risiko gagal konvergen (*zero convergence failure*), (b) waktu eksekusi instan (< 1 ms), (c) transparansi pedagogis penuh di mana setiap pergeseran nilai $m$ memiliki arti didaktik yang dapat diaudit langsung oleh pendidik (*white-box auditable system*), serta (d) kemudahan adaptasi materi baru tanpa perlu melatih ulang model.

---

## 2.4 Arsitektur Tiga Lapis Sistem LogiTrace Berlandaskan Temuan SLR

Sistem LogiTrace dirancang menggunakan arsitektur modular tiga lapis (*Three-Tier Architecture*), sebagaimana dimodelkan pada Gambar 2.2:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 L1 — BASIS PENGETAHUAN (Offline, Sekali Buat)               │
│  • 12 Dokumen Knowledge Components (Definisi, Prasyarat, Miskonsepsi)       │
│  • Graf Prasyarat Terarah (Prerequisite DAG) — Aturan Gerbang m ≥ 0,60      │
│  • 5 Dokumen Deskripsi Fase Kognitif Troubleshooting Jonassen (2006)                                         │
│  • 24 Contoh Pengerjaan Terstandar (1-2 per KC)                             │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                 L2 — INDEKS BUTIR SOAL (Offline per Butir)                  │
│  • Pembacaan Teks Butir oleh LLM Lokal (Frozen 3B/7B)                       │
│  • Pelabelan Ganda: KC Utama, KC Sekunder, Fase Troubleshooting Jonassen, Kesulitan (1-3)    │
│  • Vektorisasi Teks Butir (Text Embedding untuk Pencarian Kemiripan)        │
│  • Antrean Tinjauan Guru (Review Queue bila Keyakinan < 0,60)               │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                 L3 — MESIN RUNTIME DETERMINISTIK (Real-Time)                 │
│  • Model Peluang Benar: p_hat(q) = sigmoid(logit(m) + theta_d)              │
│  • Aturan Pembaruan Penguasaan Deterministik (< 1 ms)                       │
│  • Peluruhan Memori Temporal Ebbinghaus (tau = 60 hari)                     │
│  • Algoritma Pemilihan Butir Adaptif (Pita Peluang Sasaran 0,60 - 0,85)     │
│  • Protokol Kalibrasi Cold-Start (6 Butir Awal Terstandarisasi)             │
│  • Tiga Pemicu Agen RAG Tetap (T1: Label, T2: Hint Sokratik, T3: Ringkasan)│
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                     ┌─────────────────┴─────────────────┐
                     ▼                                   ▼
        Web Siswa (Mobile-First)             Dasbor Guru (Real-Time)
```
**Gambar 2.2** Arsitektur Tiga Lapis Sistem LogiTrace

### 2.4.1 Lapisan 1 (L1) — Basis Pengetahuan (Knowledge Base)
Basis pengetahuan disusun bersama oleh peneliti dan guru kejuruan, terdiri atas 42 dokumen inti:
1. **12 Dokumen Knowledge Components (KC):** Mendefinisikan unit atomik pengetahuan materi jaringan nirkabel (misalnya: alokasi kanal frekuensi, konfigurasi SSID, enkripsi WPA2/WPA3, subnetting VLSM, dan interpretasi galat ICMP). Setiap dokumen memuat definisi operasional, indikator penguasaan, daftar miskonsepsi umum, dan keterkaitan dimensi TOLT.
2. **Graf Prasyarat Terarah (*Prerequisite DAG*):** Menetapkan urutan dependensi logis antar-konsep. Aturan pemakaian sistem: suatu butir soal hanya dapat disajikan kepada siswa apabila **seluruh KC prasyaratnya telah mencapai estimasi penguasaan $m \ge 0{,}60$**. Mekanisme ini mengadopsi prinsip optimasi penguasaan materi (*mastery learning*) dari Xia et al. (2026) guna mencegah latihan berlebih (*over-practice*).
3. **5 Dokumen Dimensi TOLT:** Berisi definisi operasional dan indikator perilaku untuk kelima dimensi penalaran logis formal.
4. **24 Dokumen Contoh Pengerjaan:** Menyediakan rujukan konteks bagi agen RAG dalam menyusun *scaffolding*.

### 2.4.2 Lapisan 2 (L2) — Indeks Butir dan Pelabelan Semantik Otomatis
Mengadopsi temuan Yang et al. (2025) mengenai pemisahan kesulitan teks soal dan kesulitan konsep, setiap butir soal dalam bank soal (target 180 butir) diproses secara terstruktur:
* **Pelabelan Semantik Otomatis:** LLM lokal membaca teks butir soal dan kunci jawaban dengan menyertakan konteks basis pengetahuan, kemudian mengeluarkan struktur JSON yang memuat: `kc_utama`, `kc_sekunder`, `dimensi_tolt`, tingkat `kesulitan` (1 = mudah, 2 = sedang, 3 = sulit), `alasan` ringkas, dan derajat `keyakinan` (0,0–1,0).
* **Vektorisasi Semantik (*Text Embedding*):** Teks butir soal diubah menjadi vektor representasi menggunakan model *embedding* lokal dan disimpan dalam basis data vektor (*pgvector* / FAISS) untuk pencarian butir serupa.
* **Kendali Mutu dan Jejak Audit:** Butir soal dengan tingkat keyakinan model $< 0{,}60$ atau yang label modelnya berbeda dari label pakar secara otomatis dialihkan ke antrean tinjauan guru (*teacher review queue*). Setiap perubahan label dicatat riwayatnya dalam tabel `item_labels_history`.

### 2.4.3 Lapisan 3 (L3) — Mesin Runtime Deterministik dan Agen RAG Tiga Pemicu

#### A. Model Peluang Benar
Untuk setiap siswa $s$ dan komponen pengetahuan $k$, sistem menyimpan satu nilai status penguasaan kontinu $m_{s,k} \in [0{,}02;\ 0{,}98]$. Peluang keberhasilan siswa menjawab benar butir soal $q$ dengan tingkat kesulitan $d_q \in \{1, 2, 3\}$ dihitung melalui fungsi logistik:

$$\hat{p}(q) = \sigma\big(\mathrm{logit}(m_{s,k_q}) + \theta_{d_q}\big)$$

Di mana $\mathrm{logit}(m) = \ln\left(\frac{m}{1-m}\right)$, $\sigma(z) = \frac{1}{1 + e^{-z}}$, serta bobot tingkat kesulitan ditetapkan: $\theta_1 = +0{,}9$ (butir mudah), $\theta_2 = 0{,}0$ (butir sedang), dan $\theta_3 = -0{,}9$ (butir sulit).

#### B. Aturan Pembaruan Penguasaan Deterministik
Setelah siswa merespons butir soal, nilai penguasaan diperbarui secara instan (< 1 ms) menggunakan aturan deterministik:

$$m \leftarrow \begin{cases} m + \alpha_d (1 - m) h, & \text{jika respons benar } (r = 1) \\ m - \gamma_d m, & \text{jika respons salah } (r = 0) \end{cases}$$

Parameter pembaruan diatur secara proporsional terhadap tingkat kesulitan butir:
$$\alpha_d = \alpha_0 \big(1 + \beta(d - 1)\big), \qquad \gamma_d = \gamma_0 \big(1 + \beta(3 - d)\big)$$

Dengan parameter dasar terstandar: $\alpha_0 = 0{,}30$, $\gamma_0 = 0{,}25$, $\beta = 0{,}4$, serta faktor bobot bantuan petunjuk:
$$h = \begin{cases} 1{,}0, & \text{jika benar mandiri tanpa petunjuk} \\ 0{,}5, & \text{jika benar setelah memanfaatkan petunjuk} \end{cases}$$

Tabel 2.2 merinci nilai laju kenaikan ($\alpha_d$) dan penurunan ($\gamma_d$) berdasarkan tingkat kesulitan.

**Tabel 2.2** Parameter Pembaruan Penguasaan Berdasarkan Tingkat Kesulitan Butir Soal

| Tingkat Kesulitan Butir ($d$) | Laju Kenaikan $\alpha_d$ (Benar) | Laju Penurunan $\gamma_d$ (Salah) | Karakteristik Pedagogis |
| :---: | :---: | :---: | :--- |
| **Tingkat 1 (Mudah)** | 0,30 | 0,45 | Salah pada soal mudah menurunkan estimasi penguasaan lebih tajam |
| **Tingkat 2 (Sedang)** | 0,42 | 0,35 | Keseimbangan bobot kenaikan dan penurunan standar |
| **Tingkat 3 (Sulit)** | 0,54 | 0,25 | Berhasil menjawab soal sulit meningkatkan estimasi penguasaan secara signifikan |

Perlu ditegaskan bahwa parameter $\alpha_0 = 0{,}30$, $\gamma_0 = 0{,}25$, $\beta = 0{,}4$, serta bobot kesulitan $\theta_1 = +0{,}9$, $\theta_2 = 0{,}0$, $\theta_3 = -0{,}9$ pada penelitian ini diposisikan sebagai **nilai dasar heuristik apriori (*baseline heuristic parameters*)**. Untuk menghindari volatilitas estimasi penguasaan yang terlalu sensitif atau terlalu lembam, parameter-parameter dasar ini akan **dikalibrasi dan disempurnakan secara empiris (*empirically fine-tuned*)** pada tahap Uji Coba Terbatas (Kelompok Kecil, Minggu ke-7) berdasarkan analisis kurva karakteristik butir dan laju respons siswa.

Mengadopsi prinsip peluruhan memori Ebbinghaus dari Li (2026) dan Samonte et al. (2024), efek keterlupaan temporal dimodelkan saat sistem membaca profil penguasaan:
$$m_k(t) = m_k(t_{\text{akhir}}) \cdot \exp\left(-\frac{t - t_{\text{akhir}}}{\tau_k}\right), \qquad \tau_k = 60 \text{ hari}$$

Setelah pembaruan, nilai penguasaan selalu dibatasi pada interval tertutup $[0{,}02;\ 0{,}98]$. Karakteristik matematis aturan ini menjamin transparansi penuh: jawaban benar tidak pernah menurunkan $m$, jawaban salah tidak pernah menaikkan $m$, dan seluruh histori dapat direkonstruksi murni dari data log.

#### C. Algoritma Pemilihan Butir Adaptif
Mengacu pada prinsip ZPD pada platform SageJavon (Zhao et al., 2026) dan efisiensi belajar Xia et al. (2026), sistem menyeleksi butir soal berikutnya dari himpunan kandidat yang memenuhi kriteria:
1. Belum pernah dijawab oleh siswa pada sesi bersangkutan;
2. Seluruh konsep prasyarat pada DAG telah mencapai penguasaan $m \ge 0{,}60$; serta
3. Nilai estimasi peluang benar $\hat{p}$ berada dalam **pita sasaran optimal $0{,}60 \le \hat{p} \le 0{,}85$**.

Sistem memilih butir $q$ yang meminimalkan fungsi penalti:
$$\text{Skor}(q) = |\hat{p}(q) - 0{,}72| - 0{,}05 \cdot \mathbb{I}(\text{KC belum tersentuh sesi ini}) + 0{,}10 \cdot \mathbb{I}(\text{KC sama dengan butir sebelumnya})$$
Pita sasaran 0,60–0,85 dengan nilai tengah 0,72 dipilih karena memberikan tantangan instruksional optimal di mana siswa tidak merasa frustrasi (probabilitas $< 0{,}60$) dan tidak mengalami kebosanan (probabilitas $> 0{,}85$).

#### D. Protokol Kalibrasi Cold-Start
Untuk mengatasi permasalahan ketiadaan riwayat belajar pada awal sistem dijalankan (*cold-start*), pada Sesi 1 siswa baru:
1. Seluruh 12 KC diberi nilai awal prioritas rendah $m_k = 0{,}25$.
2. Siswa secara terstandar mengerjakan **6 butir soal kalibrasi** (2 mudah, 2 sedang, 2 sulit) yang dipilih untuk mengukur konsep akar DAG.
3. Nilai penguasaan diperbarui menggunakan aturan yang sama. KC yang belum terukur langsung diestimasi dari nilai rata-rata klaster prasyarat terdekat dan ditandai dengan status `keyakinan: rendah` (arsir pada dasbor guru).
4. Mulai butir ke-7 dan seterusnya, sistem beroperasi dalam mode adaptif penuh. Butir kalibrasi (1–6) secara ketat dikeluarkan dari evaluasi akurasi prediksi model guna menghindari bias evaluasi.

#### E. Tiga Pemicu Agen RAG Tetap
Agen RAG dioperasikan secara terikat hanya pada tiga pemicu fungsional (*fixed triggers*), sebagaimana dirangkum pada Tabel 2.3.

**Tabel 2.3** Spesifikasi Tiga Pemicu Agen RAG Sistem LogiTrace

| Pemicu | Kondisi Pemicu | Konteks Retrieval yang Diambil | Aksi dan Batasan Format Keluaran (*Guardrail*) |
| :--- | :--- | :--- | :--- |
| **T1 — Pelabelan Butir** | Butir baru dimasukkan guru; label kosong atau keyakinan model $< 0{,}60$. | Dokumen 12 KC, 5 dimensi TOLT, dan 5 butir soal termirip (*embedding*). | Menghasilkan struktur JSON usulan KC, TOLT, dan kesulitan untuk antrean tinjauan guru. |
| **T2 — Bantuan Sokratik** | Siswa menekan tombol "Petunjuk" ATAU salah 2 kali berturut-turut pada KC yang sama. | Dokumen KC bersangkutan, daftar miskonsepsi umum, contoh pengerjaan, dan jawaban salah siswa. | Mengadopsi prinsip *Guiding, Not Solving* (Wang et al., 2026): menghasilkan petunjuk Sokratik level 1–3, maksimal 60 kata, **tanpa memuat kunci jawaban akhir (*leakage guard*)**. |
| **T3 — Dasbor Guru** | Akhir sesi pembelajaran ATAU saat guru membuka dasbor pemantauan kelas. | Matriks agregat penguasaan 12 KC dan log waktu respons seluruh siswa di kelas. | Mengadopsi prinsip *Ambient Awareness*: menyajikan ringkasan visual minimalis berupa kartu prioritas **3 siswa teratas yang paling mendesak membutuhkan bimbingan (*Top-3 Stuck Students*)** beserta konsep KC titik kebuntuan, guna mencegah kelebihan beban kognitif guru (*teacher overload*), dilengkapi ringkasan naratif agregat kelas. |

Pengamanan ketat (*guardrails*) dan kedaulatan data diterapkan melalui arsitektur keamanan bertingkat (*Defense-in-Depth* 5 lapis):
1. *Lapisan 1 (Pre-Flight Zero-PII Sanitizer):* Memindai dan menyensor secara otomatis seluruh data sensitif (NISN, NIK, nomor telepon, email, ID siswa, dan nama sekolah) sebelum payload dikirim, sehingga data yang keluar murni hanya berupa teks materi kejuruan;
2. *Lapisan 2 (Credential & Transport Security):* Secret key dienkapsulasi eksklusif di backend `.env` (tidak pernah bocor ke klien) dengan enkripsi transport HTTPS (TLS 1.2+);
3. *Lapisan 3 (Strict SLA Timeout):* Batas latensi inferensi dipatok maksimal 3,0 detik;
4. *Lapisan 4 (Post-Flight Leakage Guard & Anti-XSS):* Memverifikasi panjang teks $\le 60$ kata, memindai string kunci jawaban dan frasa pembocor secara regex, serta melakukan sanitasi entitas HTML (`html.escape`) pencegah serangan Cross-Site Scripting; dan
5. *Lapisan 5 (Graceful Fallback Instan < 50 ms):* Apabila terjadi gangguan jaringan, batas kuota, latensi $> 3$ detik, atau kunci jawaban terdeteksi bocor, sistem seketika mengalihkan respon ke **Bank Petunjuk Statis Terkurasi (*Pre-computed Curated Hints Bank*)** di memori Redis/PostgreSQL, sehingga alur rotasi kelas tetap berjalan lancar tanpa kendala.

---

## 2.5 Model Pembelajaran Blended Learning Tipe Station Rotation

### 2.5.1 Konsep Dasar Blended Learning dan Model Rotasi
*Blended learning* didefinisikan sebagai desain instruksional yang memadukan secara harmonis antara pembelajaran tatap muka di ruang kelas dengan pembelajaran daring berbasis teknologi digital yang memberikan kendali kepada siswa atas kecepatan belajarnya (Graham, 2006). Mengacu pada taksonomi baku dari Horn dan Staker (2014) di *Christensen Institute*, model rotasi (*Rotation Model*) dibedakan menjadi beberapa varian, dengan varian utama mencakup *Station Rotation* dan *Lab Rotation*. Karakteristik pembeda mendasar terletak pada batas ruang fisik: *Station Rotation* secara teoretis mensyaratkan seluruh rotasi aktivitas berlangsung di dalam **satu ruang kelas/laboratorium fisik yang sama (*within a single classroom or laboratory*)**, sedangkan rotasi yang melibatkan perpindahan gedung/ruangan terpisah diklasifikasikan sebagai *Lab Rotation*.

Oleh sebab itu, guna menjaga kemurnian definisi teoretis model serta mengeliminasi hilangnya waktu instruksional akibat mobilisasi siswa (*zero transit loss*), penelitian ini menerapkan model **Station Rotation Satu Ruangan (*Single-Room Station Rotation*)** yang diimplementasikan secara terpadu di dalam Laboratorium Komputer sekolah mitra (Truitt & Ku, 2018).

### 2.5.2 Sintaks Pembelajaran Station Rotation Satu Ruangan Terpadu
Di dalam laboratorium komputer, ruang belajar diorganisasikan ke dalam **dua zona aktivitas terpadu** yang memfasilitasi tiga fungsi stasiun pembelajaran secara simultan, sebagaimana disajikan pada Tabel 2.4.

**Tabel 2.4** Sintaks dan Karakteristik Zonasi Pembelajaran *Station Rotation* Satu Ruangan

| Zona Aktivitas / Stasiun | Lingkungan Fisik & Media | Peran Peserta Didik | Peran Pendidik / Sistem LogiTrace |
| :--- | :--- | :--- | :--- |
| **Zona A: Stasiun Praktik Lab Mandiri (*Collaborative Hands-on Station*)** | Area meja komputer lab; Media: 17 Unit PC Laboratorium (Rasio Optimal 1 PC : 1 Siswa) & perangkat router/AP fisik. | Melaksanakan unjuk kerja konfigurasi jaringan nyata (Cisco Packet Tracer / Router Fisik), menguji logika IP, dan memverifikasi rute ICMP mandiri. | Guru memantau kelancaran teknis praktikum secara visual sepintas (*single-glance supervision*); siswa memvalidasi hipotesis penalaran logika yang dipelajari di zona evaluasi. |
| **Zona B1: Stasiun Evaluasi Adaptif Mandiri (*Online Adaptive Station*)** | Area meja non-PC / meja tengah lab; Media: *Smartphone* pribadi masing-masing siswa terhubung ke Web LogiTrace. | Mengerjakan butir kuis adaptif pada zona perkembangan proksimal (*ZPD*), menerima umpan balik seketika, dan mengeksplorasi petunjuk Sokratik AI. | LogiTrace menyajikan butir soal pada pita peluang optimal ($0{,}60 \le \hat{p} \le 0{,}85$), memperbarui status penguasaan $m$, dan memicu agen RAG T2 (*Guiding, Not Solving*). |
| **Zona B2: Stasiun Bimbingan Terarah Guru (*Roving Teacher-Led Station*)** | Terintegrasi langsung di Zona B; Media: Dasbor Analitik Guru Real-Time (WebSocket) pada laptop instruktur. | Mendiskusikan miskonsepsi logika konfigurasi secara privat bersama guru di mejanya masing-masing saat mengalami kebuntuan kognitif. | Guru berperan sebagai pembimbing bergerak (*roving teacher*): memantau sinyal anomali pada dasbor seketika, lalu mendatangi langsung meja siswa yang membutuhkan bimbingan diagnostik terarah (*stealth targeted scaffolding*). |

Penerapan peran guru bergerak (*roving teacher*) di Zona B memberikan **dua keunggulan pedagogis dan psikososial yang vital**:
1. **Menghilangkan Stigma Sosial Pemisahan Remedial:** Dalam psikologi remaja kejuruan (usia 16–17 tahun), memanggil siswa tertentu untuk berpindah ke "meja bimbingan remedial khusus" berisiko mencederai motivasi dan memicu rasa minder di depan teman-temannya. Dengan guru yang mendatangi meja siswa secara bersahaja, intervensi bimbingan bersifat privat, suportif, dan bebas dari stigma negatif.
2. **Menghilangkan Friksi Logistik Kelas:** Siswa tetap duduk tenang di posisinya tanpa perlu memindahkan kursi, kabel, atau barang bawaan, sehingga suasana kelas tetap kondusif dan fokus belajar tidak terpecah.

Alokasi waktu per sesi pembelajaran (standar 90 menit) diatur sebagai berikut:
1. **Fase Pembuka & Diagnostik Awal (10 Menit):** Seluruh 34 siswa berkumpul di Zona B untuk mengakses Web LogiTrace melalui ponsel cerdas masing-masing guna mengerjakan kuis diagnostik pembuka (Sesi 1: 6 butir kalibrasi; Sesi 2–4: butir adaptif lanjutan).
2. **Fase Rotasi Stasiun (2 x 35 Menit = 70 Menit):** Rombongan belajar dibagi menjadi dua kelompok besar (Kelompok A berisi 17 siswa dan Kelompok B berisi 17 siswa) yang berotasi secara bersilang (*crossover*):
   * *Putaran 1 (35 Menit):* Kelompok A menempati Zona A (Praktik Lab Mandiri dengan rasio optimal 1 PC : 1 Siswa). Sementara itu, Kelompok B menempati Zona B (Evaluasi Adaptif Mandiri via ponsel cerdas dengan pendampingan guru bergerak).
   * *Transisi Cepat (1–2 Menit):* Bel pergantian sesi berbunyi. Siswa bertukar posisi zona di dalam laboratorium yang sama dengan cepat, tertib, dan tanpa kehilangan waktu produktif belajar (*zero transit loss*).
   * *Putaran 2 (35 Menit):* Kelompok B memasuki Zona A (Praktik Lab Mandiri 1:1), sedangkan Kelompok A berpindah ke Zona B (Evaluasi Adaptif Mandiri via ponsel cerdas dan bimbingan guru).
3. **Fase Refleksi & Penutup (8–10 Menit):** Seluruh siswa kembali ke meja diskusi untuk menyimak ulasan umum guru berdasarkan ringkasan naratif otomatis dari agen RAG T3 pada dasbor kelas.

### 2.5.3 Strategi Device-Purpose Split untuk Mengatasi Rasio Lab (1 PC : 2 Siswa)
Hambatan fasilitas laboratorium komputer di sekolah mitra yang berada pada rasio 1 unit PC untuk 2 orang siswa diatasi secara terstruktur melalui strategi **Device-Purpose Split** (Pemisahan Perangkat Berbasis Peran Instruksional):
* **Ponsel Cerdas Pribadi Siswa $\rightarrow$ Dialokasikan Khusus untuk Aktivitas Kognitif-Formatif Individual:** Karena dikerjakan di layar genggam masing-masing di Zona B, integritas data rekaman kognitif siswa terjamin murni individual (*pure individual cognitive trace*), bebas dari bias kerja kelompok atau dominasi rekan sebangku.
* **PC Laboratorium Komputer $\rightarrow$ Dialokasikan Khusus untuk Aktivitas Praktikum Mandiri:** Dengan membagi rombongan belajar ke dalam rotasi 50% di Zona A dan 50% di Zona B, kapasitas laboratorium yang semula 1 PC untuk 2 siswa secara matematis tereduksi menjadi **1 PC untuk 1 Siswa (rasio ideal 1:1)**. Setiap siswa memperoleh kesempatan penuh mengonfigurasi perangkat tanpa harus berebut giliran dengan rekan sekelas.
* **Status Desain Instruksional:** Perbaikan rasio komputer menjadi 1:1 ini bukanlah variabel perancu eksternal yang terjadi secara kebetulan, melainkan **bagian dari rekayasa desain pembelajaran (*deliberate instructional design*)** yang sengaja diciptakan oleh model *Station Rotation* berbantuan LogiTrace guna memecahkan hambatan fisik sekolah vokasi secara sistemik.

---

## 2.6 Kemampuan Logical Thinking dalam Bidang Jaringan Komputer

### 2.6.1 Hakikat Logical Thinking dan Perkembangan Kognitif Formal
Berpikir logis (*logical thinking*) merupakan kemampuan operasional mental untuk menghubungkan premis, menganalisis relasi kausalitas, menarik kesimpulan yang valid berdasarkan kaidah inferensi yang konsisten, serta merumuskan strategi sistematis dalam memecahkan masalah kompleks (Inhelder & Piaget, 1958; Jonassen, 2006; Piaget, 1972). Dalam teori perkembangan intelektual Piaget, peserta didik jenjang SMK (usia 16–17 tahun) secara kronologis berada pada tahap perkembangan operasional formal yang ditandai oleh kemampuan penalaran hipotesis-deduktif, pengisolasian variabel, dan penarikan kesimpulan kausal (Lawson, 1985; Valanides, 1999).

Sebagaimana dicatat dalam tinjauan sistematis (SLR) pada Bab I, literatur AIEd terkini sangat minim mendefinisikan *computational thinking* atau *logical thinking* sebagai konstruk terapan yang terukur (kebanyakan hanya diukur sebagai keberhasilan sintaks kode program atau logika silogisme simbolik murni yang kaku) (Tato & Nkambou, 2022; Wang et al., 2026; Zhao et al., 2026). Oleh karena itu, penelitian ini mengisi celah fundamental tersebut dengan mengadopsi kerangka kerja penalaran pemecahan masalah teknis (*cognitive troubleshooting*) yang autentik dan teruji.

### 2.6.2 Kerangka Kerja Penalaran Kausal dan Troubleshooting Jonassen & Hung (2006)
Dalam konteks pendidikan kejuruan dan rekayasa sistem komputer, kemampuan berpikir logis (*logical thinking*) tidak dapat diukur secara autentik menggunakan instrumen logika abstrak murni seperti *Test of Logical Thinking* (TOLT) Piagetian (Tobin & Capie, 1981) yang berbasis eksperimen sains dasar (seperti bandul ayunan dan kelereng). Jonassen (2006) serta Jonassen dan Hung (2006) menegaskan bahwa bentuk manifestasi berpikir logis paling nyata dan fungsional dalam ranah teknologi komputer adalah **penalaran pemecahan masalah teknis (*troubleshooting as causal problem-solving reasoning*)**. 

Dalam arsitektur teori pemecahan masalah teknis (*A New Theory-Based Design Architecture*), Jonassen dan Hung (2006) memetakan ekosistem *troubleshooting* ke dalam tiga kelompok: kelompok pengetahuan (*system knowledge*), kelompok proses kognitif (*cognitive processes*), dan kelompok karakteristik masalah (*problem characteristics*). Guna mengukur alur berpikir logis siswa secara objektif dan terstandar, penelitian ini memfokuskan pengukuran kemampuan *Logical Thinking* pada **Kelompok 2 (Lima Fase Kognitif Troubleshooting)**:
1. **Symptom Recognition (Identifikasi Gejala):** Kemampuan mengamati, mengenali, dan membedakan perilaku anomali sistem jaringan yang menyimpang dari kondisi operasi normal (misal: menginterpretasikan pesan galat ICMP, status indikator link adapter fisik, atau degradasi performa koneksi).
2. **Problem Space Construction (Konstruksi Ruang Masalah):** Kemampuan memetakan batas subsistem yang bermasalah, mengisolasi komponen yang relevan, serta mengendalikan variabel pengujian (misal: memisahkan dugaan kegagalan pada adapter klien vs konfigurasi *Access Point* pemancar).
3. **Fault Hypothesis Generation (Perumusan Hipotesis Gangguan):** Kemampuan merumuskan dugaan logis mengenai akar penyebab kerusakan (*fault state*) berdasarkan model mental sistem dan penalaran kausal sebab-akibat fisik (misal: pengaruh jarak, sudut kelengkungan kabel, dan hambatan material terhadap pelemahan daya sinyal dBm).
4. **Hypothesis Testing & Evaluation (Pengujian & Evaluasi Hipotesis):** Kemampuan merancang dan mengevaluasi tes diagnostik secara sistematis serta memperhitungkan probabilitas keberhasilan di bawah ketidakpastian (misal: analisis ambang batas *roaming* dan probabilitas tabrakan sinyal nirkabel).
5. **Corrective Action & Verification (Tindakan Korektif & Verifikasi):** Kemampuan memilih kombinasi tindakan perbaikan fisik maupun konfigurasi yang paling optimal, lalu memverifikasi bahwa kontinuitas koneksi sistem telah pulih secara tuntas (misal: penataan kanal *non-overlapping* 1, 6, 11).

### 2.6.3 Operasionalisasi 5 Fase Kognitif Troubleshooting pada Materi Jaringan Nirkabel TKJ
Kelima fase kognitif penalaran *troubleshooting* Jonassen (2006) dikontekstualisasikan ke dalam domain permasalahan konfigurasi dan perawatan jaringan nirkabel SMK, sebagaimana disajikan pada Tabel 2.5.

**Tabel 2.5** Operasionalisasi 5 Fase Kognitif Troubleshooting Jonassen (2006) dalam Domain Jaringan Nirkabel TKJ

| Fase Kognitif Jonassen (2006) | Definisi Kognitif Baku | Manifestasi Keterampilan pada Materi Jaringan Nirkabel | Indikator Perilaku Siswa yang Terukur |
| :--- | :--- | :--- | :--- |
| **1. Symptom Recognition** | Mengamati dan membedakan anomali perilaku sistem dari kondisi normal. | **Interpretasi Gejala Galat & Respons Protokol ICMP:** Mengamati perbedaan respons koneksi ping peer-to-peer (*Destination Host Unreachable* vs *Request Timed Out*) dan status indikator adapter. | Siswa mampu mengidentifikasi karakteristik gejala kerusakan secara presisi dan membedakan apakah anomali terjadi pada rute logis lokal atau ketiadaan jalur balik. |
| **2. Problem Space Construction** | Mengisolasi batas subsistem masalah dan mengendalikan variabel uji. | **Isolasi Batas Masalah Klien vs Pemancar:** Menguji adapter Wi-Fi lokal, kecocokan SSID, dan kata sandi WPA2 secara terisolasi sebelum mengubah setelan AP pemancar bersama. | Siswa mampu memetakan ruang masalah dengan menguji variabel klien secara sekuensial tanpa melakukan tindakan acak yang berisiko mengganggu perangkat lain. |
| **3. Fault Hypothesis Generation** | Merumuskan dugaan kausal penyebab gangguan berbasis model mental fisik. | **Penalaran Kausalitas Redaman Jarak & Hambatan Material (RSSI):** Menghubungkan degradasi daya sinyal (-dBm) dan throughput data dengan pertambahan jarak atau sifat dielektrik partisi dinding. | Siswa mampu merumuskan hipotesis logis mengenai akar penyebab penurunan performa sinyal berdasarkan prinsip propagasi gelombang elektromagnetik. |
| **4. Hypothesis Testing & Evaluation** | Menguji hipotesis diagnostik dan memperhitungkan probabilitas kondisi sistem. | **Pengujian Keputusan Roaming & Evaluasi Tabrakan Sinyal:** Menganalisis probabilitas klien berpindah (*roaming*) ke WLAN Extender serta mengevaluasi potensi tabrakan paket (*collision*) pada kanal padat. | Siswa mampu menguji dugaan gangguan melalui perhitungan probabilitas *failover* sinyal dan utilisasi spektrum nirkabel. |
| **5. Corrective Action & Verification** | Merencanakan tindakan perbaikan optimal dan memverifikasi pemulihan link. | **Perencanaan Alokasi Kanal Non-Overlapping & Verifikasi Koneksi:** Menata kombinasi kanal frekuensi (1, 6, 11 pada 2,4 GHz) serta memverifikasi transfer data end-to-end setelah perbaikan. | Siswa mampu menentukan solusi konfigurasi fisik/logis yang bebas interferensi (*zero co-channel interference*) dan memverifikasi pemulihan performa jaringan secara tuntas. |

---

## 2.7 Materi Teknologi Jaringan Kabel dan Nirkabel sebagai Domain Pengetahuan

### 2.7.1 Kedudukan Kurikuler: Capaian Pembelajaran (CP) dan Alur Tujuan Pembelajaran (ATP) Fase F TKJ
Domain pengetahuan dalam penelitian ini berakar langsung pada kurikulum resmi Sekolah Menengah Kejuruan (SMK) Konsentrasi Keahlian Teknik Komputer dan Jaringan (TKJ). Berdasarkan Keputusan Kepala BSKAP Kemendikbudristek Nomor 033/H/KR/2022 tentang Capaian Pembelajaran pada Pendidikan Anak Usia Dini, Jenjang Pendidikan Dasar, dan Jenjang Pendidikan Menengah pada Kurikulum Merdeka, elemen **Teknologi Jaringan Kabel dan Nirkabel** pada Fase F menetapkan Capaian Pembelajaran (CP) sebagai berikut:

> *"Pada akhir fase F, peserta didik mampu menginstalasi jaringan kabel dan nirkabel, melakukan perawatan dan perbaikan jaringan kabel dan nirkabel, memahami standar jaringan nirkabel, memilih teknologi jaringan nirkabel indoor dan outdoor sesuai kebutuhan, melakukan instalasi perangkat jaringan nirkabel, menguji instalasi perangkat jaringan nirkabel, menjelaskan konsep layanan Voice over IP (VoIP), mengkonfigurasi layanan Voice over IP (VoIP), memahami jaringan fiber optic, memahami jenis-jenis kabel fiber optic, memilih kabel fiber optic, menerapkan fungsi alat kerja fiber optic, menggunakan alat kerja fiber optic, melakukan sambungan fiber optic, dan melakukan perbaikan jaringan fiber optic."*

Elemen CP tersebut diturunkan ke dalam lima **Tujuan Pembelajaran (TP)** resmi:
* **TP 2.1:** Menerapkan instalasi jaringan kabel dan nirkabel.
* **TP 2.2:** Menerapkan perawatan dan perbaikan jaringan kabel dan nirkabel.
* **TP 2.3:** Menerapkan instalasi dan konfigurasi layanan Voice over IP (VoIP).
* **TP 2.4:** Menerapkan instalasi jaringan fiber optik.
* **TP 2.5:** Memahami perbaikan jaringan fiber optik.

Guna menjaga kelayakan instruksional dalam 4 sesi intervensi tatap muka (@ 90 menit) tanpa menimbulkan kelebihan beban kognitif pada siswa, materi pembelajaran dibagi secara terstruktur ke dalam dua fungsi kurikuler:
1. **Materi Target Intervensi (Fokus Pembelajaran 4 Sesi & 10 Butir Tes TOLT-Jaringan):**  
   Difokuskan secara mendalam pada alur **Instalasi Jaringan Kabel dan Nirkabel** yang mengintegrasikan:
   * **TP 2.1:** Menerapkan instalasi jaringan kabel dan nirkabel (mencakup standar IEEE 802.11, frekuensi 2,4 GHz vs 5 GHz, alokasi kanal non-overlapping 1, 6, 11, topologi BSS/Ad-Hoc, pengalamatan IP, dan pengujian konektivitas ICMP peer-to-peer).
   * **TP 2.2:** Menerapkan perawatan dan perbaikan jaringan kabel dan nirkabel (mencakup redaman jarak RSSI, roaming threshold pemancar, autentikasi WPA2/WPA3, proteksi firewall, dan troubleshooting anomali galat ICMP DHU vs RTO).
2. **Materi Kontrol Non-Equivalent Dependent Variable (NEDV, 6 Butir Soal Kontrol):**  
   Diambil secara sah dari Tujuan Pembelajaran lain dalam mata pelajaran resmi yang sama namun **sengaja tidak diajarkan** selama 4 sesi intervensi nirkabel:
   * **TP 2.3:** Layanan Voice over IP / VoIP (2 butir soal kontrol).
   * **TP 2.4 & TP 2.5:** Jaringan dan Perbaikan Fiber Optik (4 butir soal kontrol).  
   Pemisahan kurikuler ini memberikan landasan ilmiah yang sangat kokoh untuk membuktikan bahwa peningkatan kemampuan berpikir logis siswa murni diakibatkan oleh intervensi LogiTrace pada materi target, bukan karena efek latihan tes atau kematangan alami siswa.

### 2.7.2 Konsep Dasar dan Topologi Jaringan Nirkabel (Ad-Hoc vs Infrastruktur)
Standar teknologi Jaringan Area Lokal Nirkabel (*Wireless Local Area Network* / WLAN) didasarkan pada spesifikasi IEEE 802.11 yang beroperasi pada pita frekuensi 2,4 GHz dan 5 GHz (Kurose & Ross, 2021; Tanenbaum et al., 2021). Dalam silabus Fase F Konsentrasi Keahlian TKJ, perancangan arsitektur nirkabel mencakup:
* **Mode Ad-Hoc (IBSS):** Komunikasi langsung *peer-to-peer* antar-perangkat nirkabel tanpa menggunakan Access Point, yang menuntut konfigurasi pengalamatan IP statis mandiri pada satu segmen yang sama.
* **Mode Infrastruktur (BSS dan ESS):** Komunikasi terpusat melalui *Access Point* (AP), yang dapat diperluas jangkauannya menggunakan *WLAN Extender / Repeater* untuk membentuk satu kesatuan identitas jaringan terpadu (Odom, 2020).

### 2.7.3 Konfigurasi Perangkat Nirkabel, SSID, dan Keamanan Autentikasi
Pengoperasian jaringan nirkabel menuntut pemahaman terhadap parameter identitas dan pengamanan:
* **Service Set Identifier (SSID):** Identitas unik jaringan nirkabel yang disiarkan secara berkala melalui *beacon frame*.
* **Keamanan Nirkabel & Host Hardening:** Penerapan enkripsi *Wi-Fi Protected Access* (WPA2-PSK / WPA3-SAE) berbasis algoritma AES, serta konfigurasi proteksi dinding api (*firewall*) dan penyaringan alamat fisik (*MAC Filtering*) (Tanenbaum et al., 2021). Siswa kerap mengalami disorientasi ketika membedakan antara status keterhubungan fisik (*associated*) dengan status keterhubungan logis (*authenticated & IP-assigned*).

### 2.7.4 Troubleshooting Konektivitas Nirkabel dan Pengujian Diagnostik ICMP
Pengujian ketercapaian host (*reachability*) dievaluasi menggunakan utilitas berbasis protokol *Internet Control Message Protocol* (ICMP), khususnya perintah `ping` secara *peer-to-peer* (Kurose & Ross, 2021). Mendiagnosis anomali respon galat:
* **Destination Host Unreachable (DHU):** Berkorelasi dengan kegagalan pemetaan alamat MAC di tabel ARP, salah konfigurasi subnet mask, atau perbedaan segmen alamat IP.
* **Request Timed Out (RTO):** Berkorelasi dengan proteksi firewall perangkat tujuan yang memblokir paket ICMP masuk, redaman sinyal yang parah (RSSI $< -80\text{ dBm}$), atau rute kembali yang terputus.

---

## 2.8 Kajian Metodologis

### 2.8.1 Model Pengembangan Sistem R&D (Borg & Gall, Judijanto et al., ADDIE Branch)
Penelitian ini merupakan penelitian pengembangan (*Research and Development* / R&D) di bidang pendidikan (Borg & Gall, 1983; Richey & Klein, 2007). Mengacu pada Judijanto et al. (2024), prosedur R&D memadukan **Tahapan Umum Penelitian** (Identifikasi Masalah, Perancangan Rencana, Pengumpulan Data, Analisis Data, Interpretasi Hasil, dan Penulisan Laporan) dengan **Tahapan Khusus Pengembangan Produk** menggunakan model instruksional **ADDIE** (*Analysis, Design, Development, Implementation, Evaluation*) yang dikembangkan oleh Branch (2009). Siklus evaluasi formatif yang melekat pada setiap fase ADDIE menjamin integrasi yang harmonis antara konstruksi perangkat lunak dan desain pembelajaran.

### 2.8.2 Perangkat Pengembangan Sistem Web Cerdas dan Arsitektur Model Bahasa Klien Aman (Zero-PII)
Pengembangan perangkat lunak LogiTrace menggunakan tumpukan teknologi modern:
* *Frontend:* Framework reaktif Vue.js / React didukung Tailwind CSS dengan tata letak responsif *mobile-first*.
* *Backend API:* Framework asinkron berkecepatan tinggi FastAPI (Python) berbasis ASGI.
* *Basis Data:* PostgreSQL untuk data relasional terstruktur dan *pgvector* / FAISS untuk penyimpanan vektor semantik butir soal; serta Redis Cache untuk status sesi runtime.
* *Arsitektur Model Bahasa (Hybrid Multi-Provider dengan Zero-PII Defense-in-Depth):* Backend LogiTrace mengimplementasikan modul klien aman (`SecureLLMClient`) yang mendukung integrasi multi-provider berlatensi ultra-rendah (< 0,8 detik seperti Groq Llama-3.1 atau DeepSeek-V3) dan opsi model lokal terkuantisasi (Ollama 3B/7B pada server kampus). Untuk menjamin kepatuhan penuh terhadap prinsip etika dan UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP), sistem menerapkan modul pembersih data pribadi pra-kirim (*Pre-Flight Zero-PII Sanitizer*) di mana seluruh identitas siswa (nama, NISN, NIK, nomor kontak, dan ID siswa) disensor secara deterministik di laptop lokal peneliti sebelum kueri konsep ditransmisikan. Dengan demikian, payload yang dikirim murni hanya berupa teks materi kejuruan, sementara basis data analitik, riwayat respons, dan identitas siswa 100% tersimpan secara aman di server lokal. Biaya komputasi operasional Cloud API sangat terjangkau (di bawah Rp 5.000 untuk keseluruhan sesi satu rombel) atau bernilai Rp 0 melalui *free-tier* Groq / Ollama lokal.

### 2.8.3 Instrumen Evaluasi Kualitas Media (Validitas LORI 2.0 & Usabilitas SUS)
* **Learning Object Review Instrument (LORI 2.0):** Mengadaptasi kerangka kerja baku Leacock dan Nesbit (2007) yang mengevaluasi kualitas media multimedia melalui sembilan dimensi: kualitas konten, keselarasan tujuan, umpan balik dan adaptasi, motivasi, desain presentasi, kemudahan interaksi, aksesibilitas, penggunaan kembali, dan kepatuhan standar.
* **System Usability Scale (SUS):** Mengadopsi instrumen baku terstandarisasi John Brooke (1996) yang terdiri atas 10 butir pernyataan untuk mengukur tingkat penerimaan (*acceptability*) dan kegunaan sistem menurut persepsi pengguna akhir (Bangor et al., 2008, 2009).

### 2.8.4 Desain Penelitian Pra-Eksperimen (One-Group Pretest-Posttest Design & Sensus Kelas)
Penelitian ini menerapkan desain **Pra-Eksperimen: One-Group Pretest-Posttest Design** (Sugiyono, 2019; Creswell, 2014; Shadish et al., 2002):

$$\begin{array}{ccccc}
O_1 & \longrightarrow & X & \longrightarrow & O_2
\end{array}$$

Di mana $O_1$ adalah pengukuran awal (*pre-test*), $X$ adalah perlakuan intervensi model *Station Rotation* berbantuan Web LogiTrace, dan $O_2$ adalah pengukuran akhir (*post-test*). Pendekatan *within-subjects* ini menempatkan setiap siswa sebagai kontrol bagi dirinya sendiri (*self-control*), sehingga mereduksi variansi kesalahan antarsubjek (*inter-subject error variance*) (Shadish et al., 2002).

Penentuan subjek penelitian menggunakan teknik **Purposive Sampling** pada tingkat sekolah/jurusan dengan kriteria rasio laboratorium 1:2 dan tingkat kesulitan belajar materi jaringan nirkabel tertinggi. Pada tingkat rombongan belajar terpilih (kelas XI TKJ 1 SMKN 4 Bandung dengan 34 siswa), penelitian ini melibatkan seluruh siswa secara utuh sehingga berstatus sebagai **sensus kelas** (*complete census* dari populasi terjangkau), bukan penarikan sampel acak parsial.

### 2.8.5 Asesmen Kemampuan Kognitif dan Analisis Kualitas Butir Tes (Teori Tes Klasik / CTT)
Pengukuran konstruk *Logical Thinking* menggunakan instrumen tes objektif pilihan ganda beralasan (*two-tier multiple-choice*) berbasis TOLT (Tobin & Capie, 1981). Guna memperluas rentang varians data, menghindari volatilitas pengukuran pada tes 10 butir, serta mempertahankan fungsi diagnostik formatif, penelitian ini menerapkan **sistem penskoran bergradasi polikotomis tiga tingkat (*polytomous graded scoring*)** mengadopsi kerangka kerja Treagust (1988) dan Azwar (2012):
* **Skor 2 (Penalaran Ilmiah Matang):** Siswa memilih opsi jawaban benar pada tingkat pertama DAN memilih opsi alasan logis yang benar pada tingkat kedua.
* **Skor 1 (Penguasaan Parsial / Miskonsepsi):** Siswa memilih opsi jawaban benar namun alasan logisnya keliru (mengindikasikan hafalan prosedural semu), ATAU siswa memilih opsi jawaban keliru akibat kekeliruan perhitungan teknis minor namun alasan logis penalaran kausalitasnya benar.
* **Skor 0 (Tidak Menguasai Konsep):** Siswa memilih opsi jawaban salah dan alasan salah, atau tidak menjawab.

Melalui penskoran bergradasi ini, skor maksimal instrumen 10 butir adalah sebesar **20 poin**, dan skor maksimal per dimensi penalaran (2 butir) berada pada rentang **0 hingga 4 poin** (5 tingkatan skor: 0, 1, 2, 3, 4). Validitas isi instrumen diverifikasi oleh panel ahli (*expert judgment*, Sari et al., 2021). Karakteristik psikometrik butir tes diuji coba secara empiris menggunakan pendekatan **Teori Tes Klasik (*Classical Test Theory* / CTT)** merujuk pada Shofiah et al. (2023) dan Azwar (2012):
1. **Validitas Empiris Butir:** Dihitung menggunakan rumus korelasi *Pearson Product Moment* (atau korelasi skor butir terhadap skor total terkoreksi / *corrected item-total correlation*); butir dinyatakan valid jika $r_{xy} > r_{\text{tabel}}$ pada taraf signifikansi $\alpha = 0{,}05$.
2. **Reliabilitas Tes:** Mengingat data respon penskoran bersifat polikotomis bergradasi (skor 0, 1, 2), estimasi reliabilitas instrumen dihitung menggunakan koefisien **Cronbach's Alpha ($\alpha$)** (Azwar, 2012; Field, 2018), bukan KR-20 yang dikhususkan untuk data dikotomis murni; instrumen dinyatakan andal jika koefisien $\alpha \ge 0{,}70$ (target minimal 0,60 untuk instrumen penalaran bergradasi).
3. **Tingkat Kesukaran ($TK$):** Diklasifikasikan menjadi Sukar ($0{,}00-0{,}30$), Sedang ($0{,}31-0{,}70$), dan Mudah ($0{,}71-1{,}00$) berbasis proporsi perolehan skor terhadap skor maksimal butir.
4. **Daya Pembeda ($DP$):** Dihitung dari selisih rata-rata perolehan skor kelompok atas dan kelompok bawah; diklasifikasikan menjadi Sangat Baik/Baik ($DP \ge 0{,}30$), Cukup ($0{,}20 \le DP < 0{,}30$), dan Buruk ($DP < 0{,}20$).
5. **Efektivitas Pengecoh (*Distractor*):** Opsi salah pada tier 1 dan alasan distraktor pada tier 2 dinyatakan berfungsi jika dipilih oleh minimal 5% peserta tes dan didominasi oleh kelompok siswa bawah.

### 2.8.6 Teknik Pengumpulan Data dan Skala Pengukuran (Skala Likert 4 Poin)
Teknik pengumpulan data mengacu pada pedoman Sugiyono (2019) yang memadukan observasi keterlaksanaan, wawancara guru dan siswa, tes kemampuan kognitif, serta angket. Lembar validasi ahli menggunakan **Skala Likert 4 poin** (1 = Sangat Tidak Layak hingga 4 = Sangat Layak) guna menghindari bias kecenderungan memusat (*central tendency bias*) responden (Likert, 1932).

### 2.8.7 Teknik Analisis Data Statistik (N-Gain, Uji Prasyarat, Paired t-Test, dan Repeated Measures ANOVA Antar-Dimensi)
1. **Normalized Gain (N-Gain):** Besaran peningkatan kemampuan berpikir logis dihitung menggunakan rumus Hake (1998, 1999):
   $$g = \frac{S_{\text{post}} - S_{\text{pre}}}{S_{\text{maks}} - S_{\text{pre}}}$$
   Kategori: Tinggi ($g \ge 0{,}70$), Sedang ($0{,}30 \le g < 0{,}70$), dan Rendah ($g < 0{,}30$). Dilengkapi dengan pengkategorian statistik hipotetik merujuk Azwar (2012) serta perhitungan ukuran efek *Cohen's* $d_z$ untuk sampel berpasangan.
2. **Uji Prasyarat:** Uji Normalitas menggunakan uji **Shapiro-Wilk** (Shapiro & Wilk, 1965; Field, 2018; Razali & Wah, 2011) yang memiliki kekuatan uji (*power*) superior untuk sampel $N = 34 \le 50$. Uji Homogenitas varians menggunakan *Levene's Test* (Levene, 1960; Field, 2018).
3. **Uji Hipotesis Efektivitas:** Menggunakan uji parametrik berpasangan **Paired Sample t-Test** (jika data normal) atau uji non-parametrik **Wilcoxon Signed-Rank Test** (Siegel, 1956) pada taraf signifikansi $\alpha = 0{,}05$.
4. **Uji Keseimbangan Antar-Dimensi (Repeated Measures ANOVA dan Analisis Profil Ukuran Efek):** Mengingat kelima dimensi penalaran TOLT diukur secara simultan pada subjek siswa yang sama (*within-subjects design*, $n = 34$), pengujian perbedaan peningkatan antar-dimensi menggunakan **One-Way Repeated Measures ANOVA (RM-ANOVA)** (Field, 2018; Girden, 1992). Penggunaan ANOVA biasa (*between-subjects*) dihindari karena melanggar asumsi independensi observasi (*independence of observations*). Model RM-ANOVA secara matematis mengisolasi varians antar-individu dari varians galat, sehingga menghasilkan kekuatan uji statistik (*power*) yang jauh lebih tinggi pada sampel kelas tunggal. Uji asumsi sferisitas (*sphericity*) dievaluasi menggunakan **Mauchly's Test**; apabila asumsi sferisitas dilanggar ($p < 0{,}05$), dilakukan penyesuaian derajat kebebasan menggunakan koreksi **Greenhouse-Geisser** ($\hat{\epsilon} < 0{,}75$) atau **Huynh-Feldt** ($\hat{\epsilon} \ge 0{,}75$). Jika data terbukti tidak berdistribusi normal, digunakan uji non-parametrik ekuivalen yaitu **Uji Friedman** (Field, 2018; Siegel, 1956). Di samping itu, guna menghindari kekeliruan logika penarikan kesimpulan statistika (*Accepting the Null Fallacy*—di mana nilai $p > 0{,}05$ pada sampel kecil kerap keliru diklaim sebagai 'bukti' mutlak bahwa peningkatan merata di semua dimensi), evaluasi keseimbangan profil dianalisis secara komprehensif menggunakan **analisis profil ukuran efek (*Cohen's* $d_z$) per dimensi** yang divisualisasikan melalui diagram radar dan interval kepercayaan 95% (*95% Confidence Interval*).

---

## 2.9 Kajian Penelitian Terdahulu yang Relevan (Matriks Sintesis Literatur 21 Artikel SLR)

Sebagai landasan posisi kebaruan (*novelty*) penelitian ini, dilakukan sintesis terhadap artikel-artikel kunci dari korpus Tinjauan Sistematis (SLR) 2021–2026, sebagaimana disajikan pada Tabel 2.6.

**Tabel 2.6** Matriks Komparasi dan Sintesis Penelitian Terdahulu yang Relevan dari Korpus SLR

| Peneliti & Tahun | Judul Penelitian & Sumber | Model AI / Pendekatan | Temuan Kunci | Relevansi Desain dengan LogiTrace | Celah (*Gap*) yang Diisi oleh Penelitian Ini |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Nkambou et al. (2023)** | *Learning Logical Reasoning Using an ITS: A Hybrid Approach* (AAAI 2023) | CDM-DINA + DKTm + Bayesian Network (BN) buatan pakar | DKT murni gagal pada inferensi langka ($F_1 = 0{,}0$); injeksi struktur pakar meningkatkan akurasi ke 0,82 pada 294 partisipan. | Landasan L1: Struktur basis pengetahuan pakar (DAG & KC) mutlak dibutuhkan untuk menstabilkan model pada data kecil. | Meneliti logika formal murni; belum menyentuh domain terapan kejuruan jaringan nirkabel. |
| **Tato & Nkambou (2022)** | *Infusing Expert Knowledge Into a Deep Neural Network* (Frontiers in AI) | DKT + Jaringan Bayesian via mekanisme atensi | Mengatasi kelangkaan data dengan menyuntikkan model kognitif pakar logika ke representasi laten. | Menegaskan bahwa struktur pakar adalah kompensasi ilmiah terbaik atas keterbatasan korpus data perilaku. | Evaluasi luring pada data kuesioner; belum diintegrasikan ke orkestrasi fisik kelas kejuruan. |
| **Wang et al. (2026)** | *Guiding, Not Solving: Agentic Scaffolding for LLM Tutors* (CEUR AIED 2026) | SHARP: Multi-model scaffolding Sokratik + KT | LLM yang memberikan jawaban langsung merusak *productive struggle*; petunjuk berjenjang menghasilkan *task success* 92–98%. | Landasan Agen T2: Menerapkan prinsip *Guiding, Not Solving* dengan *leakage guard* pencegah bocornya kunci jawaban. | Diterapkan pada *competitive programming*; belum dikontekstualisasikan untuk melacak 5 dimensi TOLT. |
| **Zhao et al. (2026)** | *SageJavon: A Scalable AI Tutor for Programming* (IPM 2026) | SageJavon: LLM + RAG + GIKT pada Taksonomi Bloom | Rekomendasi latihan pada pita probabilitas menengah (ZPD) menurunkan beban kognitif dan meningkatkan retensi. | Landasan Pemilih Butir: Menyeleksi butir adaptif pada pita peluang keberhasilan optimal $0{,}60 \le \hat{p} \le 0{,}85$. | Evaluasi berbasis persepsi diri; pembandingnya mesin pencari Baidu, bukan tutor adaptif lain. |
| **Jung et al. (2025)** | *CLST: Cold-Start Mitigation in Knowledge Tracing* (JEDM 2025) | CLST: Mistral-7B + LoRA fine-tuning lintas domain | Mengatasi *cold start* menggunakan LLM; namun AUC pada 8 siswa hanya mencapai 0,635–0,689. | Menunjukkan batas performa transfer LLM dan perlunya kalibrasi terstandar pada awal sesi. | Masih menuntut korpus data siswa domain sumber untuk *fine-tuning*; LogiTrace sepenuhnya *training-free*. |
| **Huang et al. (2024)** | *Remembering is Not Applying: Interpretable KT* (ACM MM 2024) | PSKT: Model sekuensial tiga fase (Pre, During, Post) | Membedakan mengingat teori dari menerapkan pemecahan masalah; menghasilkan parameter kognitif yang dapat ditafsirkan. | Landasan L3: Menghindari fluktuasi drastis penguasaan melalui aturan pembaruan berbasis bukti unjuk kerja. | Diuji pada matematika sekolah umum; tidak mengatasi kendala fasilitas komputasi laboratorium kejuruan. |
| **Xia et al. (2026)** | *Optimizing Mastery Learning by Fast-Forwarding* (LNCS 2026) | Fast-Forwarding BKT pada dependensi langkah | Melompati langkah yang telah dikuasai memangkas latihan berlebih (*over-practice*) hingga 35,7%. | Landasan Gerbang DAG: Butir soal hanya disajikan bila seluruh konsep prasyarat mencapai $m \ge 0{,}60$. | Evaluasi berbasis simulasi data siswa; belum diuji pada intervensi siswa nyata di kelas fisik. |
| **Li (2026)** | *Knowledge Tracing in Math: Spatio-Temporal GNN* (IJICT 2026) | STGNN-MKT + gerbang kelupaan Ebbinghaus | Pemodelan prasyarat graf dan peluruhan memori menghasilkan prediksi stabil pada interval > 30 hari. | Landasan Peluruhan Memori: Menerapkan fungsi peluruhan retensi memori temporal $\tau = 60$ hari. | Menuntut komputasi graf yang kompleks; LogiTrace menyederhanakannya ke dalam aturan deterministik instan. |
| **Yang et al. (2025)** | *Difficulty Aware Programming KT via LLMs* (Sci. Rep. 2025) | DPKT: CodeBERT + anotasi kesulitan teks via LLM | Memisahkan kesulitan teks soal dari kesulitan konsep pengetahuan meningkatkan akurasi prediksi. | Landasan L2: Memanfaatkan LLM untuk pelabelan semantik dan estimasi kesulitan butir soal dari teks. | Model tetap menuntut pelatihan jaringan saraf berulang; tidak menyelesaikan persoalan *small data*. |
| **Shao et al. (2026)** | *Leveraging LLM and Multiscale Knowledge States* (ACM WWW 2026) | MIE + MLPKT: LLM DeepSeek + status multiskala | Mengganti skor biner dengan skor parsial dan ekstraksi vektor penyebab kesalahan via LLM meningkatkan AUC. | Mempertegas peran LLM sebagai pengekstrak alasan kesalahan dan pendiagnosis miskonsepsi. | Menggunakan model LLM raksasa via API komersial yang menimbulkan kendala latensi dan biaya tinggi di sekolah. |

Berdasarkan telaah sintesis pada Tabel 2.6, **tiga kebaruan utama (*novelty*) dari penelitian ini** adalah:
1. **Adaptasi Tanpa Pelatihan (*Training-Free KT*):** Menggeser kebutuhan data dari korpus perilaku siswa ke korpus konten kurikulum, menyelesaikan kebuntuan penerapan KT pada domain kejuruan tanpa dataset pelatihan publik.
2. **Pelabelan Semantik Ganda KC $\times$ Fase Troubleshooting Jonassen:** Mengoperasionalkan penalaran logis ke dalam pemetaan ganda komponen pengetahuan teknis dan dimensi berpikir logis formal.
3. **Pengukuran Batas Empiris (*Boundary Testing*):** Melaporkan secara jujur batas-batas ketidakmampuan pendekatan tanpa-latih melalui perbandingan ketat terhadap tiga model *baseline*.

---

## 2.10 Kerangka Berpikir (Conceptual Framework)

Kerangka berpikir penelitian ini berakar pada kenyataan bahwa rendahnya kemampuan *Logical Thinking* siswa SMK kelas XI TKJ merupakan akibat dari evaluasi formatif yang bersifat statis seragam serta keterbatasan laboratorium komputer (1 PC : 2 siswa) yang memicu fenomena pasangan dominan-pasif. Solusi terpadu dirumuskan melalui **Pengembangan Web Evaluasi Formatif Adaptif Berbasis Knowledge Tracing dan Retrieval-Augmented Generation (LogiTrace) dalam Pembelajaran Station Rotation dengan Strategi Device-Purpose Split**, sebagaimana digambarkan pada alur Gambar 2.3:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                     KONDISI AWAL                                       │
│ • Praktik evaluasi formatif kejuruan bersifat statis, seragam, dan tidak diagnostik.   │
│ • Keterbatasan lab (1 PC : 2 Siswa) memicu dominant-passive pair & task completion mekanis.│
│ • DKT konvensional tidak layak dijalankan karena ketiadaan korpus perilaku masif.      │
│ • Temuan SLR: Ketiadaan model KT yang mengukur konstruk penalaran logis di SMK.        │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              TINDAKAN / PENGEMBANGAN (R&D)                             │
│ 1. Pengembangan Sistem Web LogiTrace (Arsitektur Tiga Lapis):                          │
│    - L1: Basis Pengetahuan (12 Dokumen KC, DAG Prasyarat, 5 Fase Jonassen, 24 Contoh).          │
│    - L2: Indeks Butir Semantik & Pelabelan Ganda Otomatis LLM Lokal (Frozen).          │
│    - L3: Aturan Penguasaan Determinis (< 1 ms), Pemilih Butir (Pita 0,60-0,85),        │
│          Kalibrasi Cold-Start (6 Butir), dan Tiga Pemicu Agen RAG (Guardrail Ketat).   │
│ 2. Desain Pembelajaran Station Rotation Satu Ruangan dengan Device-Purpose Split:      │
│    - Zona A: Praktik Lab Mandiri dengan Rasio Optimal (1 PC : 1 Siswa).                │
│    - Zona B: Evaluasi Adaptif Mandiri (Smartphone) & Guru Bergerak (Roving Teacher).   │
│    - Orkestrasi Satu Ruang Lab Menjamin Transisi Instan (Zero Transit Loss).           │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               KONDISI AKHIR YANG DIHARAPKAN                            │
│ • Terwujudnya sistem LogiTrace yang teruji valid (LORI, Kappa, ICC) dan praktis (SUS). │
│ • Terbuktinya keunggulan akurasi prediksi pasca-kalibrasi di atas tiga model baseline. │
│ • Peningkatan signifikan Logical Thinking melalui ekosistem Station Rotation terpadu.  │
│ • Keseimbangan profil penalaran troubleshooting Jonassen terpetakan via ukuran efek per fase & RM-ANOVA.│
│ • Terverifikasinya peran interaksi sistem via analisis hubungan dosis-respons.         │
│ • Terselesaikannya kendala rasio lab komputer melalui manajemen kelas rotasi terpadu.  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
**Gambar 2.3** Kerangka Berpikir Pengembangan Sistem LogiTrace dalam Pembelajaran Kejuruan

---

# BAB III
# METODOLOGI PENELITIAN

## 3.1 Jenis dan Model Pengembangan Penelitian (Model ADDIE)

Penelitian ini merupakan penelitian pengembangan (*Research and Development* / R&D) yang bertujuan menghasilkan dan menguji kelayakan sistem web evaluasi formatif adaptif **LogiTrace** yang diintegrasikan ke dalam model pembelajaran *Station Rotation* guna memperkuat kemampuan *Logical Thinking* siswa SMK (Borg & Gall, 1983; Richey & Klein, 2007).

Prosedur pengembangan mengadopsi model instruksional **ADDIE** yang dikembangkan oleh Branch (2009) dan diselaraskan dengan tahapan umum R&D menurut Judijanto et al. (2024). Model ADDIE terdiri atas lima fase iteratif:
1. **Analysis:** Mendiagnosis kesenjangan evaluasi kejuruan mengacu pada temuan SLR, menganalisis hambatan fasilitas lab 1:2, serta mendekomposisi silabus kurikulum jaringan nirkabel ke dalam 12 *Knowledge Components* (KC) dan graf prasyarat DAG.
2. **Design:** Menyusun cetak biru arsitektur tiga lapis LogiTrace berlandaskan prinsip-prinsip desain SLR (Nkambou et al., 2023; Wang et al., 2026; Zhao et al., 2026), merumuskan aturan penguasaan deterministik, memetakan taksonomi butir soal ke dalam matriks ganda KC $\times$ Fase Troubleshooting Jonassen, serta merancang modul ajar *Station Rotation*.
3. **Development:** Mengembangkan kode perangkat lunak (FastAPI, Vue/React, PostgreSQL, Redis, dan integrasi modul klien model bahasa aman bertingkat SecureLLMClient), menyusun bank butir 180 soal, serta melakukan uji validitas ahli materi dan ahli media menggunakan instrumen LORI 2.0.
4. **Implementation:** Menerapkan sistem web LogiTrace dan model *Station Rotation* secara nyata dalam 4 sesi tatap muka pada kelas kejuruan SMK mitra.
5. **Evaluation:** Melaksanakan evaluasi formatif dan sumatif komprehensif melalui enam jalur evaluasi empiris (E1 hingga E6) yang secara langsung menjawab agenda riset SLR, mencakup akurasi pemetaan, mutu petunjuk, akurasi prediksi pasca-kalibrasi terhadap tiga baseline, reliabilitas model, kepraktisan SUS, serta analisis $N\text{-Gain}$ dan uji Repeated Measures ANOVA antar-dimensi TOLT.

---

## 3.2 Prosedur Penelitian dan Pengembangan Sistem LogiTrace

Prosedur penelitian diorganisasikan ke dalam **tiga alur utama** (Judijanto et al., 2024):

### 3.2.1 Tahap Studi Pendahuluan (General Research Phase)
Tahap ini mencakup telaah kritis hasil Tinjauan Sistematis (SLR) terhadap 21 artikel Scopus (2021–2026) mengenai keterbatasan DKT pada data kecil, observasi kondisi laboratorium komputer di SMKN 4 Bandung, wawancara guru kejuruan, identifikasi fenomena pasangan dominan-pasif, serta penyusunan proposal penelitian.

### 3.2.2 Tahap Pengembangan Sistem LogiTrace (Model ADDIE)

#### A. Tahap Analisis (Analysis)
1. **Analisis Kebutuhan Instruksional:** Mengonfirmasi kendala rasio lab 1:2, ketersediaan gawai pintar siswa, infrastruktur Wi-Fi sekolah, serta tingginya tingkat remedial formatif siswa kelas XI TKJ 1 pada materi jaringan nirkabel.
2. **Analisis Kurikulum & Dekomposisi Pengetahuan:** Mendekomposisi materi teknologi jaringan nirkabel dan pengujian ICMP ke dalam 12 KC atomik dan menyusun graf dependensi prasyarat (DAG).
3. **Analisis Karakteristik Kognitif:** Mengidentifikasi defisit penalaran formal siswa, khususnya pada dimensi kombinatorik (alokasi kanal frekuensi) dan korelasional (analisis galat respons ICMP RTO vs DHU).

#### B. Tahap Perancangan (Design)
1. **Perancangan Arsitektur L1 (Basis Pengetahuan):** Menulis 12 dokumen KC, 1 dokumen graf dependensi DAG, 5 dokumen dimensi TOLT, dan 24 dokumen contoh pengerjaan terstandar, mengadopsi struktur pakar Nkambou et al. (2023).
2. **Perancangan Arsitektur L2 (Indeks Butir Semantik):** Merancang format JSON pelabelan otomatis LLM, skema penyimpanan vektor kemiripan teks butir (*embedding*), dan mekanisme antrean tinjauan guru, mengadopsi pemisahan kesulitan semantik Yang et al. (2025).
3. **Perancangan Arsitektur L3 (Mesin Runtime Deterministik & Agen RAG):**
   * Menetapkan model estimasi peluang benar $\hat{p}(q) = \sigma(\text{logit}(m) + \theta_d)$ dengan parameter kesulitan $\theta_1 = +0{,}9$, $\theta_2 = 0{,}0$, $\theta_3 = -0{,}9$.
   * Menetapkan formula pembaruan penguasaan deterministik dengan parameter $\alpha_0 = 0{,}30$, $\gamma_0 = 0{,}25$, $\beta = 0{,}4$, pembobotan petunjuk $h \in \{1{,}0;\ 0{,}5\}$, serta peluruhan memori Ebbinghaus $\tau = 60$ hari (Li, 2026; Samonte et al., 2024).
   * Merumuskan fungsi penalti pemilihan butir adaptif pada pita peluang $0{,}60 \le \hat{p} \le 0{,}85$ dengan titik tengah $0{,}72$ berbasis ZPD (Zhao et al., 2026; Xia et al., 2026).
   * Merancang protokol 6 butir kalibrasi *cold-start* dengan prior awal $m_0 = 0{,}25$.
   * Menetapkan spesifikasi tiga pemicu agen RAG (T1: Pelabelan butir baru; T2: Bantuan Sokratik dengan *leakage guard* mengacu Wang et al., 2026; T3: Ringkasan dasbor guru).
4. **Perancangan Desain Instruksional:** Menyusun RPP / Modul Ajar model *Station Rotation* 3 stasiun yang menerapkan strategi *Device-Purpose Split*.

#### C. Tahap Pengembangan (Development)
1. **Rekayasa Perangkat Lunak:** Mengembangkan antarmuka web responsif (Vue.js/React), API backend (FastAPI), basis data relasional (PostgreSQL), in-memory cache (Redis), serta integrasi modul klien model bahasa aman (`SecureLLMClient`) yang mendukung multi-provider berlatensi rendah (< 0,8s seperti Groq / DeepSeek) dengan sensor data pribadi pra-kirim (*PIIScrubber*) dan opsi fallback luring (Ollama / bank statis < 50 ms).
2. **Konstruksi Bank Butir Soal (Pembangkitan Berbantuan AI & Kurasi Human-in-the-Loop):** Menyusun bank butir soal adaptif sebanyak 180 butir ($\ge 5$ butir per KC per tingkat kesulitan) mengadopsi paradigma *Automated Item Generation* (AIG) berbantuan model bahasa besar (*Large Language Model* / LLM) berbasis dokumen basis pengetahuan L1 (Liang et al., 2023; Zhang et al., 2025). Guna menjamin keabsahan pedagogis dan ketepatan teknis materi, seluruh draf butir yang dibangkitkan AI diperiksa, diverifikasi, dan disunting secara mandiri oleh peneliti (*Human-in-the-Loop Curation*) sebelum diajukan ke tahap pengujian validitas pakar (*expert judgment*). Di samping itu, disusun 10 butir tes TOLT-Jaringan (Bentuk A dan B paralel) dengan sistem penskoran bergradasi polikotomis (skor 0, 1, 2) serta 6 butir kontrol NEDV.
3. **Validasi Ahli (*Expert Judgment*):** Melakukan validasi kelayakan secara komprehensif oleh panel ahli yang melibatkan dosen ahli pendidikan ilmu komputer (sebagai validator independen ahli media dan butir soal) serta dosen materi/guru kejuruan senior (sebagai validator ahli materi jaringan nirkabel) menggunakan instrumen LORI 2.0 dan lembar telaah butir soal hingga mencapai predikat "Sangat Layak".

#### D. Tahap Implementasi (Implementation)
1. **Sesi Orientasi & Pre-Test:** Sosialisasi sistem kepada siswa dan pelaksanaan *pre-test* kemampuan *Logical Thinking* (TOLT-Jaringan Bentuk A).
2. **Pelaksanaan Sesi Intervensi:** Melaksanakan 4 sesi pembelajaran tatap muka (@ 90 menit) materi teknologi jaringan nirkabel secara terpadu di dalam laboratorium komputer sekolah mitra. Pada setiap sesi, siswa mengikuti sintaks *Station Rotation* satu ruangan yang terbagi ke dalam Zona A (Praktik Lab Mandiri rasio 1 PC : 1 Siswa) dan Zona B (Evaluasi Adaptif Mandiri via ponsel cerdas pribadi berbantuan bimbingan guru bergerak). Kelancaran teknis di Zona B ditopang oleh fasilitas penunjang berupa **titik akses (*Access Point*) Wi-Fi lokal terisolasi khusus LogiTrace** (tanpa akses internet komersial luar untuk menjamin kecepatan respons intranet < 50 ms dan mencegah distraksi digital siswa) serta ketersediaan unit daya baterai cadangan (*power-bank* dan terminal daya meja).
3. **Sesi Post-Test & Pengisian SUS:** Pelaksanaan *post-test* kemampuan *Logical Thinking* (TOLT-Jaringan Bentuk B paralel) dan pengisian kuesioner *System Usability Scale* (SUS).

#### E. Tahap Evaluasi (Evaluation)
Mengintegrasikan evaluasi formatif pada setiap tahap ADDIE dan evaluasi sumatif pasca-implementasi melalui enam jalur evaluasi empiris (E1–E6).

### 3.2.3 Tahap Akhir dan Pelaporan (Reporting Phase)
Mengolah data transaksi log, menghitung metrik akurasi, menguji signifikansi statistik inferensial, membahas temuan empiris, dan menyusun laporan skripsi secara tuntas.

---

## 3.3 Desain Uji Coba Produk dan Pembelajaran

### 3.3.1 Desain Pra-Eksperimen Satu Kelompok dengan Kontrol Efek Tes dan Bias Perancu
Penelitian ini menerapkan desain **Pra-Eksperimen: One-Group Pretest-Posttest Design** (Sugiyono, 2019; Creswell, 2014; Shadish et al., 2002).

Secara ontologis, perlakuan intervensi $X$ diposisikan sebagai **Satu Kesatuan Ekosistem Pembelajaran Sosio-Teknis (*Integrated Socio-Technical Instructional Ecosystem*)** yang memadukan model *Station Rotation* satu ruangan lab, strategi *Device-Purpose Split*, bimbingan terarah guru bergerak (*roving teacher*), dan kecerdasan adaptif sistem LogiTrace. Peneliti tidak mengklaim mengisolasi perangkat lunak LogiTrace di ruang hampa yang terlepas dari dinamika kelas nyata, melainkan menguji efektivitas terpadu paket pembelajaran tersebut di mana perbaikan rasio lab (1:1) merupakan bagian rekayasa instruksional yang sengaja diciptakan oleh model rotasi ini.

Untuk memitigasi ancaman terhadap validitas internal (*internal validity*) dan bias perancu (*confounding bias*) karena ketiadaan kelompok kontrol luar, penelitian ini menerapkan **lima mekanisme kontrol ketat**:
1. **Dua Bentuk Tes Paralel (Bentuk A dan Bentuk B):**  
   Instrumen *pre-test* dan *post-test* menggunakan butir soal yang paralel secara kisi-kisi dan tingkat kesukaran namun berbeda redaksi dan konteks kasus, yang dibagikan secara bersilang (*counterbalanced*) untuk mengeliminasi efek ingatan (*memory/testing effect*).
2. **Penyisipan Butir Non-Equivalent Dependent Variable (NEDV):**  
   Instrumen tes menyisipkan **6 butir soal kontrol NEDV** yang diambil secara sah dari elemen CP resmi yang sama (*Teknologi Jaringan Kabel dan Nirkabel*) namun mencakup Tujuan Pembelajaran yang **sengaja tidak diajarkan** selama 4 sesi intervensi nirkabel, yaitu: **TP 2.3** (Layanan Voice over IP / VoIP, 2 butir) serta **TP 2.4 & TP 2.5** (Instalasi dan Perbaikan Jaringan Fiber Optik, 4 butir). Apabila peningkatan skor kognitif murni diakibatkan oleh intervensi pembelajaran LogiTrace pada materi target (TP 2.1 & TP 2.2), maka skor butir NEDV seharusnya **tidak menunjukkan peningkatan yang signifikan** ($p > 0{,}05$). Sebaliknya, jika skor NEDV ikut meningkat signifikan, maka peningkatan kemampuan pada butir target sebagian terbukti merupakan bias efek latihan tes (*testing effect*) atau kematangan (*maturation*). Mekanisme ini menjamin keterisolasian efek perlakuan dan kejujuran inferensi ilmiah.
3. **Analisis Hubungan Dosis-Respons (*Dosage-Response Relationship Analysis*):**  
   Untuk membedakan kontribusi spesifik interaksi digital Web LogiTrace dari efek fasilitas lab 1:1 dan kehadiran guru (di mana seluruh 34 siswa sama-sama menerima fasilitas lab 1:1 dan berada di kelas yang sama), penelitian ini menerapkan analisis korelasi dosis-respons. Melalui basis data *append-only*, sistem merekam variabilitas individual dalam memanfaatkan fitur cerdas LogiTrace (mencakup: frekuensi pemicuan petunjuk Sokratik $h$, estimasi status penguasaan konsep akhir $m$, dan volume butir adaptif yang diselesaikan). Jika siswa dengan tingkat keterlibatan digital yang lebih intensif terbukti memperoleh $N\text{-Gain}$ yang lebih tinggi secara signifikan ($r > 0{,}40, p < 0{,}05$), maka terdapat bukti empiris kokoh bahwa komponen perangkat lunak adaptif memberikan nilai tambah nyata di dalam ekosistem intervensi majemuk tersebut.
4. **Penegasan Konstruk Pengukuran Kognitif TOLT:**  
   Instrumen tes TOLT-Jaringan secara spesifik mengukur operasi kognitif formal abstrak (penalaran kombinatorik alokasi kanal frekuensi, penalaran proporsional redaman jarak sinyal, penalaran probabilitas roaming, dan penalaran korelasional kode galat ICMP), bukan keterampilan psikomotorik operasional fisik lab (seperti mencolokkan kabel atau menekan tombol saklar). Hal ini memastikan bahwa peningkatan skor mencerminkan perkembangan kemampuan berpikir logis, bukan sekadar keterampilan motorik mekanis di laboratorium.
5. **Pemberian Kode Anonim Siswa:**  
   Analisis data dilakukan pada kode anonim siswa guna menghindari bias subjektivitas penguji dan mematuhi etika penelitian.

### 3.3.2 Subjek, Tempat Penelitian, dan Analisis Kekuatan Statistik (Power Analysis)
* **Tempat Penelitian:** SMK Negeri 4 Bandung (Konsentrasi Keahlian Teknik Komputer dan Jaringan / TKJ), Jl. Kliningan No. 6, Kota Bandung.
* **Subjek Penelitian (Sensus Kelas):** Seluruh siswa kelas **XI TKJ 1** tahun ajaran 2026/2027 yang berjumlah **34 orang siswa**. Karena seluruh siswa dalam rombel sasaran dilibatkan secara penuh, status sampel ini adalah **sensus populasi terjangkau**, sehingga tidak mengandung kesalahan penarikan sampel (*sampling error*) pada tingkat kelas tersebut. Generalisasi hasil penelitian diarahkan pada **transferabilitas bersyarat** bagi sekolah dengan karakteristik serupa (SMK dengan lab rasio 1:2), bukan generalisasi statistik populasi tanpa batas.
* **Analisis Kekuatan Statistik (*Statistical Power Analysis*):**  
  Berdasarkan kalkulasi kekuatan uji (*power analysis*) menggunakan perangkat lunak G*Power untuk uji beda rata-rata berpasangan (*paired t-test*) dengan ukuran sampel $n = 34$, taraf signifikansi $\alpha = 0{,}05$, dan kekuatan statistik yang ditargetkan sebesar $1 - \beta = 0{,}80$, **ukuran efek minimal yang dapat dideteksi secara andal oleh penelitian ini adalah sebesar $d_z \approx 0{,}48$** (setara dengan selisih sekitar 1,2 poin pada skala tes 0–10). Peneliti secara eksplisit mencantumkan batas sensitivitas statistik ini di dalam naskah agar pembaca mengetahui batas resolusi pengujian dan tidak mengklaim efek-efek kecil yang tidak terdeteksi.

---

## 3.4 Instrumen Pengumpulan Data

### 3.4.1 Instrumen Non-Tes (Lembar Validasi LORI 2.0 & Angket Usability SUS)
1. **Lembar Validasi Ahli Media (Adaptasi LORI 2.0):** Dinilai oleh dosen ahli pendidikan ilmu komputer / rekayasa perangkat lunak untuk mengevaluasi 9 dimensi baku LORI (Leacock & Nesbit, 2007) dengan Skala Likert 4 poin (Likert, 1932) guna memverifikasi kelayakan arsitektur perangkat lunak, antarmuka responsif, dan fungsionalitas adaptif (Lampiran 1).
2. **Lembar Validasi Ahli Materi dan Butir Soal:** Dinilai oleh dosen ahli kurikulum pendidikan ilmu komputer/jaringan dan guru kejuruan senior untuk mengevaluasi kebenaran substansi konsep jaringan nirkabel, dekomposisi 12 KC, keterkaitan 5 dimensi TOLT, serta kesahihan pedagogis bank 180 butir soal kuis adaptif dan tes TOLT-Jaringan (Lampiran 2).
3. **Kuesioner System Usability Scale (SUS):** Instrumen baku 10 butir pernyataan berskala 1–5 untuk mengukur kepraktisan sistem menurut persepsi 34 siswa (Brooke, 1996; Lampiran 3).
4. **Pedoman Wawancara Guru:** Wawancara semi-terstruktur kepada 3 orang guru kejuruan untuk mengevaluasi kepraktisan implementasi dasbor orkestrasi kelas dan beban kerja pendidik.

### 3.4.2 Bank Butir Soal Kuis Adaptif dan Instrumen Tes Penalaran Troubleshooting Jaringan
1. **Bank Butir Soal Adaptif LogiTrace (180 Butir):**  
   Disusun mencakup 12 KC, di mana setiap KC memiliki minimal 5 butir pada setiap tingkat kesulitan (mudah, sedang, sulit). Guna merealisasikan target 180 butir berkualitas tinggi dalam linimasa penelitian yang realistis, draf awal butir soal dibangkitkan mengadopsi teknik *Automated Item Generation* (AIG) berbantuan model bahasa besar (*Large Language Model*) yang dikontrol secara ketat menggunakan *prompt* berbasis dokumen spesifikasi KC Lapisan 1 (Liang et al., 2023; Zhang et al., 2025). Seluruh draf butir, kunci jawaban, dan opsi distraktor kemudian melalui proses telaah, kurasi mendalam, dan penyuntingan mandiri oleh peneliti (*Human-in-the-Loop Curation*) guna memastikan kebenaran teknis dan ketiadaan distorsi konsep sebelum diajukan ke panel ahli (*expert judgment*). Dilengkapi 6 butir kalibrasi terstandar yang diberi tanda is_calibration = true.
2. **Instrumen Tes Kemampuan Logical Thinking Berbasis Penalaran Troubleshooting Jaringan:**  
   Terdiri atas paket instrumen paralel (Bentuk A untuk *Pre-Test* dan Bentuk B untuk *Post-Test*) dengan masing-masing memuat **30 butir soal target pilihan ganda beralasan dua tingkat (*two-tier multiple choice*)**, mencakup 5 fase kognitif penalaran *troubleshooting* Jonassen (2006) (masing-masing 6 butir per fase) yang direkontekstualisasikan ke materi target kurikulum (TP 2.1 Menerapkan instalasi jaringan kabel dan nirkabel serta TP 2.2 Menerapkan perawatan dan perbaikan jaringan kabel dan nirkabel) (Lampiran 4). Penskoran menggunakan **sistem bergradasi polikotomis tiga tingkat (*polytomous graded scoring*)** mengadopsi kerangka kerja Treagust (1988) dan Azwar (2012):
   * **Skor 2:** Opsi jawaban benar pada *tier* 1 DAN opsi alasan logis benar pada *tier* 2 (mengindikasikan penalaran ilmiah matang).
   * **Skor 1:** Opsi jawaban benar pada *tier* 1 namun alasan keliru pada *tier* 2 (mengindikasikan hafalan prosedural semu), ATAU opsi jawaban keliru akibat salah perhitungan teknis minor namun alasan penalarannya sahih (mengindikasikan penguasaan parsial / miskonsepsi).
   * **Skor 0:** Jawaban dan alasan salah keduanya, atau tidak menjawab (tidak menguasai konsep).  
   Penerapan penskoran bergradasi ini menghasilkan rentang skor total **0 hingga 60 poin** (skor per fase berada pada rentang **0 hingga 12 poin** dengan 7 tingkatan), sehingga memperluas varians data secara signifikan, memitigasi volatilitas pengukuran, serta memperkuat fungsi evaluasi formatif diagnostik. Instrumen ini dilengkapi pula dengan **6 butir kontrol NEDV** (TP 2.3 Layanan VoIP sebanyak 2 butir; TP 2.4 & TP 2.5 Jaringan Fiber Optik sebanyak 4 butir) dengan format dua tingkat dan penskoran bergradasi yang setara (skor 0–2), menghasilkan total **36 butir soal per paket tes**. Skor NEDV dianalisis secara terpisah murni sebagai variabel kontrol validitas internal dan tidak diakumulasikan ke dalam skor capaian target penalaran *troubleshooting*.

### 3.4.3 Pengujian Kualitas Butir Tes Berbasis Teori Tes Klasik (CTT)
Mengacu pada Shofiah et al. (2023) dan Azwar (2012), butir tes diuji coba secara empiris:
* **Validitas Butir:** Rumus korelasi *Pearson Product Moment* (atau *Corrected Item-Total Correlation*); butir dinyatakan valid jika $r_{xy} > r_{\text{tabel}}$ pada taraf signifikansi $\alpha = 0{,}05$.
* **Reliabilitas Tes:** Mengingat data respon bersifat polikotomis bergradasi (skor 0, 1, 2), estimasi reliabilitas dihitung menggunakan rumus **Cronbach's Alpha ($\alpha$)** dengan target $\alpha \ge 0{,}70$ (batas penerimaan minimal 0,60 untuk tes penalaran dua tingkat).
* **Tingkat Kesukaran & Daya Pembeda:** Memverifikasi proporsi tingkat kesukaran sedang ($0{,}31-0{,}70$) dan daya pembeda baik ($DP \ge 0{,}30$) berbasis rata-rata perolehan skor kelompok atas dan kelompok bawah.
* **Efektivitas Distraktor:** Memverifikasi seluruh alternatif pengecoh pada *tier* 1 dan *tier* 2 berfungsi menarik minimal 5% peserta kelompok bawah.

### 3.4.4 Skema Basis Data dan Log Transaksi Interaksi (Append-Only)
Sistem LogiTrace mencatat interaksi siswa ke dalam basis data PostgreSQL dengan aturan integritas *append-only* (tabel interaksi tidak boleh diubah/diupdate, koreksi dilakukan via baris pembalik) untuk menjamin transparansi data audit. Tabel inti meliputi: `students`, `kc`, `items`, `item_labels`, `interactions`, `mastery_snapshot`, `agent_logs`, dan `calibration`.

---

## 3.5 Rencana Evaluasi Sistem Komprehensif (Jalur E1 hingga E6 Menjawab Agenda Riset SLR)

Untuk menjawab rekomendasi agenda riset SLR mengenai perlunya protokol evaluasi terstandar, pelaporan biaya/latensi, dan uji dampak belajar yang dapat dipertanggungjawabkan, penelitian ini menerapkan **enam jalur evaluasi empiris terstruktur**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RENCANA EVALUASI EMPIRIS (E1 HINGGA E6)                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ E1: Validitas Isi & Akurasi Pemetaan (180 butir, Cohen's κ ≥ 0,60, Aiken's V)│
│ E2: Mutu Petunjuk Sokratik RAG (30 sampel, 3 pakar, 4 dimensi, ICC ≥ 0,70)   │
│ E3: Akurasi Prediksi Pasca-Kalibrasi (476 prediksi vs 3 baseline tanpa-latih)│
│ E4: Reliabilitas Sistem LLM Lokal (Run consistency ≥ 95% pada T=0, 3B vs 7B) │
│ E5: Kelayakan Teknis & Usability Pengguna (Latensi < 3s, Biaya 0, SUS ≥ 68) │
│ E6: Indikasi Awal Dampak Belajar (N-Gain, Cohen's d_z, RM-ANOVA 5 Dimensi, NEDV)│
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.5.1 Jalur E1 — Validitas Isi dan Akurasi Pemetaan Semantik (Cohen's Kappa & Aiken's V)
* **Tujuan:** Menguji akurasi pelabelan otomatis LLM pada Lapisan 2 (L2) tanpa memerlukan data respons siswa sama sekali.
* **Prosedur:** Seluruh 180 butir soal dinilai secara independen oleh panel ahli yang melibatkan dosen ahli pendidikan ilmu komputer dan guru TKJ senior untuk menentukan label konsensus KC dan dimensi TOLT.
* **Metrik & Target:** Kesepakatan antar-penilai antara label LLM dan label konsensus pakar dihitung menggunakan koefisien **Cohen's Kappa ($\kappa$)** dengan target $\kappa \ge 0{,}60$ (kesepakatan substansial). Kesesuaian butir dengan indikator kurikulum diukur menggunakan koefisien validitas isi **Aiken's V** dengan target $V \ge 0{,}70$. Matriks konfusi disajikan untuk menganalisis misklasifikasi konsep.

### 3.5.2 Jalur E2 — Evaluasi Kualitas Mutu Petunjuk Sokratik RAG (ICC)
* **Tujuan:** Menilai mutu pedagogis dari petunjuk bantuan Sokratik yang dibangkitkan oleh agen RAG (Pemicu T2) mengacu pada prinsip *Guiding, Not Solving* (Wang et al., 2026).
* **Prosedur:** Mengambil sampel acak berstrata sebanyak 30 petunjuk yang mencakup seluruh KC dan level bantuan (Level 1, 2, dan 3). Tiga orang pakar menilai setiap petunjuk menggunakan rubrik berskala 1–4 pada 4 dimensi: relevansi terhadap konsep, kesesuaian tingkat level bantuan, ketiadaan kebocoran jawaban akhir (*leakage guard*), dan kejelasan instruksi.
* **Metrik & Target:** Konsistensi penilaian dihitung menggunakan *Intraclass Correlation Coefficient* model dua arah efek acak konsistensi rata-rata: **ICC(2,1)** dengan target $\text{ICC} \ge 0{,}70$ (Koo & Li, 2016).

### 3.5.3 Jalur E3 — Evaluasi Akurasi Prediksi Pasca-Kalibrasi terhadap Tiga Model Pembanding
* **Tujuan:** Menguji keandalan prediktif aturan penguasaan Lapisan 3 (L3) secara jujur dan objektif.
* **Prosedur:** Pada setiap siswa, butir 1–6 dialokasikan khusus sebagai fase kalibrasi *cold-start*. Evaluasi akurasi prediksi dilakukan murni pada **butir ke-7 hingga butir ke-20 saja** (total $14 \times 34 = \mathbf{476\text{ prediksi}}$).
* **Tiga Model Pembanding Tanpa-Latih (*Non-Training Baselines*):**
  1. *Base Rate Kelas:* Selalu memprediksi probabilitas benar berdasarkan proporsi rata-rata jawaban benar kelas secara keseluruhan.
  2. *Running Accuracy Siswa:* Memprediksi berdasarkan rata-rata akumulasi jawaban benar siswa yang bersangkutan sejauh ini.
  3. *Difficulty-Only Model:* Memprediksi keberhasilan murni berdasarkan parameter tingkat kesulitan butir soal tanpa memperhitungkan status penguasaan konsep siswa.
* **Metrik & Pengujian Statistik:** Dihitung nilai Akurasi Klasifikasi, *Brier Score*, dan AUC dengan interval kepercayaan 95% berbasis *bootstrap* (1.000 iterasi). Signifikansi keunggulan akurasi LogiTrace terhadap model pembanding terbaik diuji menggunakan **Uji McNemar** untuk pasangan sampel biner. Target: akurasi LogiTrace berada minimal 5 poin persentase di atas model pembanding terbaik secara signifikan ($p < 0{,}05$).

### 3.5.4 Jalur E4 — Pengujian Reliabilitas dan Stabilitas Model Bahasa (Multi-Provider)
* **Tujuan:** Menguji ketahanan, reproduktifitas, dan stabilitas inferensi model bahasa pada integrasi multi-provider (`SecureLLMClient`).
* **Prosedur:** Menjalankan inferensi pelabelan sebanyak 3 kali pengulangan pada parameter `temperature = 0` (target konsistensi $\ge 95\%$ identik), menguji ketahanan terhadap dua variasi redaksi *prompt*, menguji efektivitas penyensoran modul *PIIScrubber*, serta membandingkan stabilitas dan latensi inferensi antar-provider (Cloud API Groq/DeepSeek vs model lokal Ollama 3B/7B).

### 3.5.5 Jalur E5 — Evaluasi Kelayakan Teknis, Latensi, dan Usability Pengguna (SUS)
* **Tujuan:** Menjawab rekomendasi agenda riset SLR mengenai pelaporan latensi teknis dan kelayakan implementasi pada perangkat keras sekolah.
* **Pengukuran Teknis:** Latensi waktu pemrosesan diukur pada persentil ke-50 (p50) dan ke-95 (p95) untuk inferensi aturan (< 10 ms) dan pemanggilan agen RAG (< 0,8 detik untuk Cloud API berkecepatan tinggi / < 3,0 detik untuk model lokal). Sistem diuji ketahanan arsitektur pertahanan berlapisnya (*graceful fallback*): apabila terjadi gangguan jaringan, kuota limit, atau latensi inferensi melampaui 3 detik, sistem secara instan (< 50 ms) mengalihkan respon ke bank petunjuk statis terkurasi guna menjamin alur rotasi kelas tidak terputus. Biaya komputasi operasional dicatat secara transparan (Rp 0 via Groq / Ollama lokal atau < Rp 5.000 via DeepSeek-V3 untuk satu rombel).
* **Pengukuran Usability:** Dihitung rata-rata skor SUS dari 34 siswa responden dengan rumus standar Brooke (1996) dan diklasifikasikan berdasarkan kriteria Bangor et al. (2008, 2009). Target: rata-rata skor $\overline{\text{SUS}} \ge 68{,}0$ (predikat minimal *Good*). Ditambah analisis kualitatif wawancara dengan 3 guru kejuruan.

### 3.5.6 Jalur E6 — Analisis Dampak Belajar, Profil Keseimbangan Dimensi, dan Hubungan Dosis-Respons
* **Tujuan:** Mengevaluasi peningkatan kemampuan berpikir logis siswa, memetakan profil keseimbangan peningkatan di seluruh fase kognitif penalaran troubleshooting Jonassen, serta membuktikan kontribusi empiris interaksi sistem melalui analisis hubungan dosis-respons (*dosage-response*).
* **Metrik Evaluasi:** Dihitung gain skor mentah, *Normalized Gain* ($N\text{-Gain}$ Hake, 1999), dan ukuran efek berpasangan *Cohen's* $d_z$:
  $$d_z = \frac{\bar{D}}{s_D}$$
* **Uji Hipotesis Komparatif:** Uji *Paired Sample t-Test* atau *Wilcoxon Signed-Rank Test* pada taraf $\alpha = 0{,}05$.
* **Pemetaan Profil Keseimbangan Antar-Dimensi (Ukuran Efek $d_z$ dan Repeated Measures ANOVA):**  
  Data perolehan $N\text{-Gain}$ dikelompokkan menjadi 5 fase kognitif penalaran troubleshooting Jonassen:
  * Dimensi 1: *Controlling Variables*
  * Dimensi 2: *Proportional Reasoning*
  * Dimensi 3: *Combinatorial Reasoning*
  * Dimensi 4: *Probabilistic Reasoning*
  * Dimensi 5: *Correlational Reasoning*  
  
  Mengingat kelima dimensi diukur pada 34 siswa yang sama (*within-subject*), uji **One-Way Repeated Measures ANOVA (RM-ANOVA)** (Field, 2018; Girden, 1992) digunakan pada taraf $\alpha = 0{,}05$. Asumsi sferisitas diuji menggunakan **Mauchly's Test**; apabila sferisitas dilanggar ($p < 0{,}05$), diterapkan koreksi derajat kebebasan **Greenhouse-Geisser** atau **Huynh-Feldt**. Jika asumsi normalitas tidak terpenuhi, digunakan uji non-parametrik ekuivalen **Uji Friedman** (Field, 2018; Siegel, 1956). Guna menghindari kekeliruan logika penarikan kesimpulan statistika (*Accepting the Null Fallacy*—di mana nilai $p > 0{,}05$ pada sampel kecil kerap keliru diklaim sebagai 'bukti' mutlak bahwa peningkatan merata di semua dimensi), evaluasi keseimbangan profil dianalisis secara komprehensif menggunakan **analisis profil ukuran efek (*Cohen's* $d_z$) per dimensi** yang divisualisasikan melalui diagram radar dan interval kepercayaan 95% (*95% Confidence Interval*).
* **Analisis Hubungan Dosis-Respons (*Dosage-Response Analysis*):**  
  Guna menguji kontribusi spesifik komponen digital Web LogiTrace di dalam ekosistem intervensi majemuk (di mana seluruh 34 siswa sama-sama mendapatkan fasilitas 1 PC : 1 siswa di lab dan bimbingan guru), peneliti melakukan analisis korelasi (Pearson / Spearman) antara variabel log transaksi individual dengan perolehan $N\text{-Gain}$ TOLT siswa:
  1. *Frekuensi Pemanfaatan Bantuan:* Jumlah klik permintaan petunjuk Sokratik dan level bantuan yang dieksplorasi siswa;
  2. *Status Penguasaan Akhir:* Nilai estimasi penguasaan kognitif ($m$) yang dicapai siswa pada sistem;
  3. *Volume Latihan Mandiri:* Jumlah total butir soal adaptif yang diselesaikan siswa di ponsel pintar.  
  
  Kriteria: Adanya korelasi positif yang signifikan ($r \ge 0{,}35, p < 0{,}05$) membuktikan secara empiris bahwa interaksi adaptif dengan Web LogiTrace memberikan sumbangan nilai tambah nyata terhadap peningkatan kemampuan berpikir logis siswa, bukan semata-mata dipicu oleh fasilitas praktikum lab fisik.
* **Verifikasi Kontrol NEDV:** Menguji selisih skor *pre-test* dan *post-test* pada 6 butir kontrol NEDV (TP 2.3 Layanan VoIP sebanyak 2 butir dan TP 2.4–2.5 Jaringan Fiber Optik sebanyak 4 butir) menggunakan uji beda berpasangan (*paired t-test* / *Wilcoxon*). Jika nilai $p > 0{,}05$ (skor NEDV terbukti tidak mengalami peningkatan yang signifikan), maka diperoleh bukti kausalitas empiris kokoh bahwa lonjakan skor pada materi target nirkabel (TP 2.1 & TP 2.2) murni dipicu oleh ekosistem intervensi pembelajaran LogiTrace, bukan oleh artefak pengujian berulang (*testing effect*) atau kematangan kognitif alami siswa (*maturation*).

### 3.5.7 Pemantauan Kesetiaan Perlakuan (Treatment Fidelity)
Untuk membuktikan bahwa sistem benar-benar beroperasi secara adaptif selama 4 sesi implementasi, peneliti wajib menghimpun dan melaporkan data kesetiaan perlakuan:
1. Distribusi tingkat kesulitan butir soal yang disajikan per sesi;
2. Frekuensi perpindahan pita peluang $\hat{p}$ per siswa;
3. Frekuensi pemicuan agen T1, T2, dan T3;
4. **Korelasi antara estimasi penguasaan ($m$) dan tingkat kesulitan butir yang dipilih sistem:** nilai korelasi wajib bernilai **positif signifikan** (semakin tinggi $m$, sistem terbukti secara otomatis memilih butir soal yang lebih sukar); serta
5. Verifikasi bahwa tepat 6 butir kalibrasi disajikan pada fase awal tiap siswa.

---

## 3.6 Etika Penelitian dan Keamanan Data Siswa

Mengingat subjek penelitian merupakan peserta didik di bawah umur (usia 16–17 tahun), penelitian ini menerapkan protokol etika yang ketat:
1. **Informed Consent & Perizinan:** Memperoleh izin resmi dari pihak manajemen SMKN 4 Bandung, persetujuan tertulis (*informed consent*) dari orang tua/wali seluruh 34 siswa, serta persetujuan sukarela (*assent*) dari siswa bersangkutan.
2. **Kedaulatan dan Privasi Data (Protokol Pre-Flight Zero-PII Sanitization):** Seluruh data sensitif siswa (nama asli, NISN, NIK, nomor telepon, dan identitas rombel) disimpan secara eksklusif di dalam basis data PostgreSQL lokal di laptop peneliti. Apabila sistem memanfaatkan inferensi Cloud API berlatensi ultra-rendah (DeepSeek / Groq), modul `PIIScrubber` secara otomatis menyensor seluruh entitas identitas pribadi pada level lokal (*pre-flight redaction*) sebelum transmisi HTTPS terenkripsi (TLS 1.2+) dilakukan. Data yang dikirimkan ke penyedia inferensi murni hanya berupa teks materi kejuruan jaringan komputer tanpa metadata personal (berstatus *non-personal domain knowledge*). Sistem juga mendukung model lokal (Ollama) serta *graceful fallback* luring 100% instan (< 50 ms) ke bank petunjuk kurasi statis, sehingga kepatuhan terhadap UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP) terpenuhi secara ketat.
3. **Anonimisasi Data:** Seluruh tabel analisis menggunakan kode identifikasi anonim unik. Nama asli siswa hanya disimpan pada tabel operasional otentikasi terpisah yang dienkripsi.
4. **Etika Dasbor Guru:** Dasbor guru hanya menampilkan visualisasi status penguasaan konsep teknis dan bukti log waktu respons; dasbor **dilarang menampilkan pelabelan sifat psikologis atau vonis kecerdasan** siswa (misalnya: dilarang mencantumkan label "siswa bodoh" atau "siswa lamban").
5. **Hak Penarikan Diri (*Right to Withdraw*):** Siswa memiliki hak penuh untuk mengundurkan diri dari sesi penelitian kapan saja tanpa konsekuensi akademis atau pengurangan nilai mata pelajaran.
6. **Retensi Data:** Data log mentah penelitian disimpan secara aman dan akan dimusnahkan selambat-lambatnya 1 tahun setelah sidang skripsi diselenggarakan.

---

## 3.7 Keterbatasan Penelitian

Peneliti menyatakan tujuh keterbatasan metodologis secara transparan:
1. **Konteks Lokasi Tunggal:** Penelitian dilaksanakan pada satu sekolah kejuruan, satu rombongan belajar, dan satu guru pengampu, sehingga efek intervensi sistem tidak sepenuhnya terisolasi dari karakteristik interaksi personal guru bersangkutan.
2. **Ketiadaan Kelompok Kontrol Luar dan Sifat Intervensi Majemuk (*Compound Treatment*):** Penelitian menggunakan desain pra-eksperimen satu kelompok dengan kontrol pembanding internal (butir NEDV, bentuk tes paralel, dan analisis korelasi dosis-respons). Mengingat intervensi pembelajaran melibatkan ekosistem terpadu (model *Station Rotation*, perbaikan rasio lab 1:1, bimbingan guru bergerak, dan Web LogiTrace), kesimpulan efektivitas berlaku bagi keseluruhan paket inovasi instruksional tersebut, di mana kontribusi nilai tambah komponen digital diuji secara spesifik melalui analisis dosis-respons dari data log transaksi sistem.
3. **Penyusunan Basis Pengetahuan oleh Peneliti:** Dokumen basis pengetahuan L1 disusun oleh peneliti bersama guru mitra, sehingga potensi bias penulis mungkin terjadi; mitigasi dilakukan melalui telaah kritis panel ahli independen pada Jalur E1.
4. **Konfigurasi Provider Model Bahasa:** Kinerja semantik dan latensi bergantung pada provider model bahasa yang dipilih (`SecureLLMClient`); versi model, prompt template, dan parameter inferensi (`temperature = 0`) dipatok secara statis selama penelitian untuk menjamin reproduktifitas data.
5. **Ukuran Bank Butir Soal:** Bank butir terdiri atas 180 soal; terdapat kemungkinan siswa melihat variasi soal dengan kemiripan konteks pada sesi yang berdekatan.
6. **Batas Generalisasi:** Generalisasi temuan bersifat transferabilitas bersyarat pada SMK dengan karakteristik fasilitas serupa (rasio komputer 1:2), bukan generalisasi statistik populasi.
7. **Retensi Memori Jangka Panjang:** Pengukuran dampak belajar dilakukan melalui *post-test* pada jarak 1–2 minggu pasca-sesi terakhir; retensi jangka panjang (misalnya 3–6 bulan) berada di luar cakupan penelitian ini.

---

## 3.8 Jadwal dan Peta Jalan Penelitian (14 Minggu)

Rangkaian pelaksanaan penelitian pengembangan LogiTrace direncanakan berlangsung selama 14 minggu, sebagaimana dipetakan pada Tabel 3.1.

**Tabel 3.1** Peta Jalan Pelaksanaan Penelitian Skripsi (14 Minggu)

| Minggu ke- | Fokus Kegiatan Utama | Rincian Luaran dan Tonggak Capaian (*Milestones*) |
| :---: | :--- | :--- |
| **1–2** | Konstruksi Basis Pengetahuan L1 | Penulisan tuntas 12 dokumen KC, 1 graf dependensi DAG, 5 dokumen TOLT, dan 24 contoh pengerjaan terstandar mengacu struktur pakar Nkambou et al. (2023). |
| **2–3** | Penyusunan Bank Butir Soal | Pembangkitan draf 180 butir kuis adaptif berbantuan AI (*AI-assisted item generation*) berbasis dokumen L1, kurasi mandiri intensif oleh peneliti (*human-in-the-loop*), serta penulisan 10 butir tes TOLT-Jaringan (penskoran polikotomis 0–2) Bentuk A dan B beserta 6 butir NEDV. |
| **3** | Pelabelan Semantik & Telaah Pakar | Pelabelan otomatis L2 via LLM lokal dan penelaahan independen 2 pakar; perhitungan koefisien awal Cohen's $\kappa$ dan Aiken's $V$ (Jalur E1). |
| **4** | Pengembangan Mesin Runtime L3 | Pemrograman aturan pembaruan penguasaan deterministik, algoritma pemilihan butir adaptif, protokol kalibrasi, dan 3 pemicu agen RAG. |
| **5** | Rekayasa Antarmuka Pengguna | Pengembangan antarmuka web responsif siswa (*mobile-first*) dan dasbor orkestrasi kelas guru berbasis WebSocket. |
| **6** | Validasi Ahli Materi & Media | Pengujian kelayakan produk oleh dosen ahli menggunakan LORI 2.0; revisi produk hingga predikat "Sangat Layak". |
| **7** | Uji Coba Terbatas (Kelompok Kecil) | Uji coba pada 9–12 siswa (2 sesi); pengujian stabilitas latensi, pengujian empiris CTT butir tes, dan penyesuaian parameter $\alpha_0$ serta $\tau$. |
| **8** | Pembekuan Sistem & Rilis v1.0 | Pembekuan konfigurasi provider model bahasa, penguncian *prompt*, dan verifikasi sistem pengamanan kebocoran jawaban (*leakage guard*). |
| **9–12** | Implementasi Uji Lapangan Penuh | Pelaksanaan 4 sesi pembelajaran tatap muka model *Station Rotation* pada 34 siswa kelas XI TKJ 1 SMKN 4 Bandung (±2.720 interaksi log). |
| **13** | Pengolahan Data & Evaluasi Sistem | Analisis data empiris komprehensif jalur E1 hingga E6 (McNemar, ICC, Bootstrap, N-Gain, Repeated Measures ANOVA, dan SUS). |
| **14** | Penyusunan Laporan Skripsi Akhir | Finalisasi penulisan Bab IV (Hasil dan Pembahasan) dan Bab V (Kesimpulan, Implikasi, dan Rekomendasi). |

---

# DAFTAR PUSTAKA

Abdelrahman, G., Wang, Q., & Nunes, B. (2023). Knowledge tracing: A survey. *ACM Computing Surveys*, 55(11), Article 224, 1–37. https://doi.org/10.1145/3569576

Aiken, L. R. (1985). Three coefficients for analyzing the reliability and validity of ratings. *Educational and Psychological Measurement*, 45(1), 131–142. https://doi.org/10.1177/0013164485451012

Arends, R. (2015). *Learning to teach* (10th ed.). McGraw-Hill Companies.

Arikunto, S. (2013). *Prosedur penelitian: Suatu pendekatan praktik*. Rineka Cipta.

Azwar, S. (2012). *Penyusunan skala psikologi* (Edisi ke-2). Pustaka Pelajar.

Bangor, A., Kortum, P. T., & Miller, J. A. (2008). An empirical evaluation of the System Usability Scale. *International Journal of Human-Computer Interaction*, 24(6), 574–594. https://doi.org/10.1080/10447310802205776

Bangor, A., Kortum, P., & Miller, J. (2009). Determining what individual SUS scores mean: Adding an adjective rating scale. *Journal of Usability Studies*, 4(3), 114–123.

Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice*, 5(1), 7–74. https://doi.org/10.1080/0969595980050102

Bohle Carbonell, K., Stalmeijer, R. E., Könings, K. D., O'Reilly, R., & van Merriënboer, J. J. (2014). How experts deal with novel situations: A review of adaptive expertise. *Educational Research Review*, 12, 14–29. https://doi.org/10.1016/j.edurev.2014.05.001

Borg, W. R., & Gall, M. D. (1983). *Educational research: An introduction* (4th ed.). Longman.

Branch, R. M. (2009). *Instructional design: The ADDIE approach*. Springer. https://doi.org/10.1007/978-0-387-09506-6

Brier, G. W. (1950). Verification of forecasts expressed in terms of probability. *Monthly Weather Review*, 78(1), 1–3.

Brooke, J. (1996). SUS: A ‘quick and dirty’ usability scale. In P. W. Jordan, B. Thomas, B. A. Weerdmeester, & A. L. McClelland (Eds.), *Usability evaluation in industry* (pp. 189–194). Taylor & Francis.

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37–46. https://doi.org/10.1177/001316446002000104

Corbett, A. T., & Anderson, J. R. (1994). Knowledge tracing: Modeling the acquisition of procedural knowledge. *User Modeling and User-Adapted Interaction*, 4(4), 253–278. https://doi.org/10.1007/BF01099821

Creswell, J. W. (2014). *Research design: Qualitative, quantitative, and mixed methods approaches* (4th ed.). SAGE Publications.

Creswell, J. W., & Creswell, J. D. (2018). *Research design: Qualitative, quantitative, and mixed methods approaches* (5th ed.). SAGE Publications.

Efron, B., & Tibshirani, R. J. (1994). *An introduction to the bootstrap*. CRC Press.

Field, A. (2018). *Discovering statistics using IBM SPSS statistics* (5th ed.). SAGE Publications.

Fisher, R. A. (1925). *Statistical methods for research workers*. Oliver and Boyd.

Girden, E. R. (1992). *ANOVA: Repeated measures*. SAGE Publications. https://doi.org/10.4135/9781412983419

Graham, C. R. (2006). Blended learning systems: Definition, current trends, and future directions. In C. J. Bonk & C. R. Graham (Eds.), *The handbook of blended learning: Global perspectives, local designs* (pp. 3–21). Pfeiffer Publishing.

Hake, R. R. (1998). Interactive-engagement versus traditional methods: A six-thousand-student survey of mechanics test data for introductory physics courses. *American Journal of Physics*, 66(1), 64–74. https://doi.org/10.1119/1.18809

Hake, R. R. (1999). Analyzing change/gain scores. *American Educational Research Association's Division D, Newsletter*, 1–4.

Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research*, 77(1), 81–112. https://doi.org/10.3102/003465430298487

Holmes, W., Bialik, M., & Fadel, C. (2019). *Artificial intelligence in education: Promises and implications for teaching and learning*. Center for Curriculum Redesign.

Holstein, K., McLaren, B. M., & Aleven, V. (2019). Co-designing a real-time classroom orchestration tool for teachers. *Journal of Learning Analytics*, 6(2), 27–44. https://doi.org/10.18608/jla.2019.62.3

Horn, M. B., & Staker, H. (2014). *Blended: Using disruptive innovation to improve schools*. Jossey-Bass.

Huang, C., Cheng, X., Wang, Y., Zeng, H., Huang, X., & Huang, Q. (2026). Affect is key: Enhancing knowledge tracing with hypergraph-based affective state modeling. *Expert Systems with Applications*, 331, Article 133323. https://doi.org/10.1016/j.eswa.2026.133323

Huang, T., Ou, X., Yang, H., Hu, S., Geng, J., Hu, J., & Xu, Z. (2024). Remembering is not applying: Interpretable knowledge tracing for problem-solving processes. In *Proceedings of the 32nd ACM International Conference on Multimedia (MM '24)* (pp. 3151–3159). Association for Computing Machinery. https://doi.org/10.1145/3664647.3681049

Inhelder, B., & Piaget, J. (1958). *The growth of logical thinking from childhood to adolescence*. Basic Books.

Jadhav, D., Chettri, S. K., Tripathy, A. K., Ghate, O., Chaudhari, R., & Avhad, S. (2023). Unlocking math potential: EDSense - A personalized intervention tool for children with dyscalculia. In *Proceedings of the 3rd International Conference on Advanced Computing Technologies and Applications (ICACTA 2023)* (pp. 1–6). IEEE. https://doi.org/10.1109/ICACTA58201.2023.10393795

Judijanto, L., Muhammadiah, M. U., Utami, R. N., Suhirman, L., Laka, L., Boari, Y., ... Yunus, M. (2024). *Metodologi research and development: Teori dan penerapan metodologi RnD*. PT. Sonpedia Publishing Indonesia.

Jung, H., Yoon, Y., Yoo, J., & Jang, Y. (2025). CLST: Cold-start mitigation in knowledge tracing by aligning a generative language model as a students' knowledge tracer. *Journal of Educational Data Mining*, 17(2), 86–117.

Koedinger, K. R., Corbett, A. T., & Perfetti, C. (2012). The Knowledge-Learning-Instruction (KLI) framework: Bridging the science-practice chasm to enhance robust student learning. *Cognitive Science*, 36(5), 757–798. https://doi.org/10.1111/j.1551-6709.2012.01245.x

Koo, T. K., & Li, M. Y. (2016). A guideline of selecting and reporting intraclass correlation coefficients for reliability research. *Journal of Chiropractic Medicine*, 15(2), 155–163. https://doi.org/10.1016/j.jcm.2016.02.012

Kurose, J. F., & Ross, K. W. (2021). *Computer networking: A top-down approach* (8th ed.). Pearson.

Lammle, T. (2020). *Cisco Certified Network Associate (CCNA) study guide: Exam 200-301*. Sybex / Wiley.

Lawson, A. E. (1985). A review of research on formal reasoning and science teaching. *Journal of Research in Science Teaching*, 22(7), 569–617. https://doi.org/10.1002/tea.3660220702

Leacock, T. L., & Nesbit, J. C. (2007). A framework for evaluating the quality of multimedia learning resources. *Educational Technology & Society*, 10(2), 44–59.

Levene, H. (1960). Robust tests for equality of variances. In I. Olkin, S. G. Ghurye, W. Hoeffding, W. G. Madow, & H. B. Mann (Eds.), *Contributions to probability and statistics: Essays in honor of Harold Hotelling* (pp. 278–292). Stanford University Press.

Li, X. (2026). Knowledge tracing in mathematical problem-solving processes: A spatio-temporal graph neural network approach. *International Journal of Information and Communication Technology*, 27(14), 23–41. https://doi.org/10.1504/IJICT.2026.10076456

Liang, Z., Yu, W., Rajpurohit, T., Clark, P., Zhang, X., & Kalyan, A. (2023). Let GPT be a math tutor: Teaching math word problem solvers with customized exercise generation. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)* (pp. 14384–14396). Association for Computational Linguistics. https://doi.org/10.18653/v1/2023.emnlp-main.889

Likert, R. (1932). A technique for the measurement of attitudes. *Archives of Psychology*, 140, 1–55.

Luckin, R., Holmes, W., Griffiths, M., & Forcier, L. B. (2016). *Intelligence unleashed: An argument for AI in education*. Pearson Education.

McNemar, Q. (1947). Note on the sampling error of the difference between correlated proportions or percentages. *Psychometrika*, 12(2), 153–157. https://doi.org/10.1007/BF02295996

Nkambou, R., Brisson, J., Tato, A., & Robert, S. (2023). Learning logical reasoning using an intelligent tutoring system: A hybrid approach to student modeling. *Proceedings of the AAAI Conference on Artificial Intelligence*, 37(13), 15930–15937. https://doi.org/10.1609/aaai.v37i13.26891

Odom, W. (2020). *CCNA 200-301 official cert guide, Volume 1 & 2*. Cisco Press.

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., ... Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ*, 372, Article n71. https://doi.org/10.1136/bmj.n71

Park, J., Kang, S., Park, J., Kim, J., Shin, J., Park, S., & Yu, Y. (2026). Tracing mathematical proficiency through problem-solving processes. In *Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL 2026)* (pp. 19251–19269). Association for Computational Linguistics.

Piaget, J. (1972). Intellectual evolution from adolescence to adulthood. *Human Development*, 15(1), 1–12. https://doi.org/10.1159/000271225

Piech, C., Bassen, J., Huang, J., Ganguli, S., Sahami, M., Guibas, L. J., & Sohl-Dickstein, J. (2015). Deep knowledge tracing. *Advances in Neural Information Processing Systems (NeurIPS 2015)*, 28, 505–513.

Razali, N. M., & Wah, Y. B. (2011). Power comparisons of Shapiro-Wilk, Kolmogorov-Smirnov, Lilliefors and Anderson-Darling tests. *Journal of Statistical Modeling and Analytics*, 2(1), 21–33.

Republik Indonesia. (2003). *Undang-Undang Republik Indonesia Nomor 20 Tahun 2003 tentang Sistem Pendidikan Nasional*. Lembaran Negara RI Tahun 2003, No. 78. Sekretariat Negara.

Richey, R. C., & Klein, J. D. (2007). *Design and development research: Methods, strategies, and issues*. Lawrence Erlbaum Associates.

Robins, A., Rountree, J., & Rountree, N. (2003). Learning and teaching programming: A review and discussion. *Computer Science Education*, 13(2), 137–172. https://doi.org/10.1076/csed.13.2.137.14200

Sadler, D. R. (1989). Formative assessment and the design of instructional systems. *Instructional Science*, 18(2), 119–144. https://doi.org/10.1007/BF00117714

Samonte, M. J. C., Evangelista, R. C. B., & Marcelo, D. N. B. (2024). Adapting DAS3H model for a personalized distributed practice schedule to improve long-term memorization in designing an intelligent programming language tutor. In *Proceedings of the 2024 ACM International Conference on Education Technology and Computers* (pp. 75–82). Association for Computing Machinery. https://doi.org/10.1145/3675812.3675854

Sari, E. D. K., Rustam, A., & Yunita, L. (2021). *Pengembangan instrumen penelitian sosial*. Kun Fayakun.

Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and quasi-experimental designs for generalized causal inference*. Houghton Mifflin.

Shao, M., Zhang, T., Yin, Y., Wu, W., Li, Z., Yu, M., Leng, F., & Yu, G. (2026). Leveraging LLM and multiscale knowledge states to improve knowledge tracing in programming tasks. In *WWW 2026: Proceedings of the ACM Web Conference 2026* (pp. 7378–7389). Association for Computing Machinery. https://doi.org/10.1145/3774904.3792525

Shapiro, S. S., & Wilk, M. B. (1965). An analysis of variance test for normality (complete samples). *Biometrika*, 52(3/4), 591–611. https://doi.org/10.1093/biomet/52.3-4.591

Shen, S., Liu, Q., Huang, Z., Zheng, Y., Yin, M., Wang, M., & Chen, E. (2024). A survey of knowledge tracing: Models, variants, and applications. *IEEE Transactions on Learning Technologies*, 17, 1898–1919. https://doi.org/10.1109/TLT.2024.3383325

Shofiah, S., Bachtiar, E., Permatasari, K. D., Syahropi, H., Zaman, N., Salam, ... Hidayat, N. (2023). *Dasar-dasar evaluasi pembelajaran*. PT. Mifandi Mandiri Digital.

Shukla, A., Bajpai, S., Modi, C., & Siddharth, S. (2026). GuideAI: A real-time personalized learning solution with adaptive interventions. In *Proceedings of the 31st International Conference on Intelligent User Interfaces (IUI '26)* (pp. 1218–1234). Association for Computing Machinery. https://doi.org/10.1145/3742413.3789125

Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research*, 78(1), 153–189. https://doi.org/10.3102/0034654307313795

Siegel, S. (1956). *Nonparametric statistics for the behavioral sciences*. McGraw-Hill.

Sudira, P. (2017). *TVET holistik: Pendekatan, model, dan praksis pendidikan kejuruan*. UNY Press.

Sugiyono. (2019). *Metode penelitian kuantitatif, kualitatif, dan R&D*. Alfabeta.

Tanenbaum, A. S., Feamster, N., & Wetherall, D. (2021). *Computer networks* (6th ed.). Pearson.

Tato, A., & Nkambou, R. (2022). Infusing expert knowledge into a deep neural network using attention mechanism for personalized learning environments. *Frontiers in Artificial Intelligence*, 5, Article 921476. https://doi.org/10.3389/frai.2022.921476

Tobin, K. G., & Capie, W. (1981). The development and validation of a group test of logical thinking. *Educational and Psychological Measurement*, 41(2), 413–423. https://doi.org/10.1177/001316448104100220

Truitt, A. A., & Ku, H. Y. (2018). A case study of third grade students' perceptions of the station rotation blended learning model. *Educational Technology Research and Development*, 66(5), 1227–1249. https://doi.org/10.1007/s11423-018-9608-3

Valanides, N. (1999). Formal reasoning abilities and school success in selected science subjects of normal track and technical track Cypriot students. *School Science and Mathematics*, 99(8), 415–424. https://doi.org/10.1111/j.1949-8594.1999.tb17502.x

Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.

Wang, C., Sahebi, S., Zhao, S., Brusilovsky, P., & Moraes, L. O. (2021). Knowledge tracing for complex problem solving: Granular rank-based tensor factorization. In *Proceedings of the 29th ACM Conference on User Modeling, Adaptation and Personalization (UMAP '21)* (pp. 179–188). Association for Computing Machinery. https://doi.org/10.1145/3450613.3456831

Wang, X., Liu, S., & Adams, P. (2024). Design and implementation of an AI-enhanced heuristic learning system in a virtual realm. In *Proceedings of the 2024 7th International Conference on Digital Technology in Education (ICDTE '24)* (pp. 255–263). Association for Computing Machinery. https://doi.org/10.1145/3696230.3696231

Wang, Y., Anand, C. S., & Tan, C. W. (2026). Guiding, not solving: Agentic scaffolding for LLM programming tutors. *CEUR Workshop Proceedings*, 4248, 1–10.

Wardani, R., Harun, H., & Wibawa, A. P. (2022). Vocational education in the industrial revolution 4.0: A systematic literature review. *International Journal of Information and Education Technology*, 12(9), 920–928. https://doi.org/10.18178/ijiet.2022.12.9.1706

Wing, J. M. (2006). Computational thinking. *Communications of the ACM*, 49(3), 33–35. https://doi.org/10.1145/1118178.1118215

Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry*, 17(2), 89–100. https://doi.org/10.1111/j.1469-7610.1976.tb00381.x

Xia, M., Schmucker, R., Borchers, C., & Aleven, V. (2026). Optimizing mastery learning by fast-forwarding over-practice steps. *Lecture Notes in Computer Science*, 16063, 549–563. https://doi.org/10.1007/978-3-032-03870-8_37

Xu, L., Wang, Z., Zhang, S., Yuan, X., Wang, M., & Chen, E. (2024). Modeling student performance using feature crosses information for knowledge tracing. *IEEE Transactions on Learning Technologies*, 17, 1390–1403. https://doi.org/10.1109/TLT.2024.3381045

Yang, L., Sun, X., Li, H., Xu, R., & Wei, X. (2025). Difficulty aware programming knowledge tracing via large language models. *Scientific Reports*, 15(1), Article 11475. https://doi.org/10.1038/s41598-025-96540-3

Zhang, L., Lin, J., Sabatini, J., Borchers, C., Weitekamp, D., Cao, M., Hollander, J., Hu, X., & Graesser, A. C. (2025). Data augmentation for sparse multidimensional learning performance data using generative AI. *IEEE Transactions on Learning Technologies*, 18, 145–164. https://doi.org/10.1109/TLT.2025.3526582

Zhao, H., Wu, Y., Lu, Z., Yu, X., Miao, W., & Chen, L. (2026). SageJavon: A scalable AI tutor for personalized programming learning. *Information Processing & Management*, 63(5), Article 104605. https://doi.org/10.1016/j.ipm.2025.104605

---

# LAMPIRAN

### Lampiran 1. Kisi-kisi Rubrik Validasi Ahli Media (Adaptasi LORI 2.0)

| Aspek Penilaian (LORI 2.0) | Indikator Penilaian Operasional dalam Sistem Web LogiTrace |
| :--- | :--- |
| **Kualitas Konten (*Content Quality*)** | Kebenaran logika penyajian butir adaptif dan ketepatan materi *scaffolding* Sokratik; sistem terbebas dari miskonsepsi teknis jaringan komputer. |
| **Keselarasan Tujuan (*Learning Goal Alignment*)** | Kesesuaian butir kuis dengan Capaian Pembelajaran (CP) Fase F dan indikator 5 dimensi *Logical Thinking* (TOLT). |
| **Umpan Balik & Adaptasi (*Feedback & Adaptation*)** | Ketepatan sistem dalam memperbarui estimasi status penguasaan ($m$), kecepatan algoritma pemilihan butir pada pita $0{,}60 \le \hat{p} \le 0{,}85$, serta ketepatan pemicuan agen RAG T2. |
| **Motivasi (*Motivation*)** | Kemampuan antarmuka kuis dan umpan balik formatif dalam memotivasi siswa untuk menyelesaikan tantangan logika secara mandiri tanpa putus asa. |
| **Desain Presentasi (*Presentation Design*)** | Kualitas estetika tata letak, keterbacaan tipografi teks, kejelasan diagram topologi jaringan nirkabel, dan tata warna antarmuka pengguna (*UI*). |
| **Kemudahan Interaksi (*Interaction Usability*)** | Kemudahan navigasi tombol, responsivitas pemilihan opsi jawaban, kejelasan instruksi, serta ketiadaan galat interaksi antarmuka. |
| **Aksesibilitas (*Accessibility*)** | Aksesibilitas sistem pada peramban ponsel pintar (*mobile browser*), kecepatan waktu pemuatan halaman (*page load speed*), dan efisiensi konsumsi data lokal. |
| **Kepatuhan Standar (*Standards Compliance*)** | Kepatuhan struktur pengkodean web terhadap standar W3C, arsitektur RESTful API FastAPI, dan kestabilan komunikasi WebSocket pada dasbor guru. |
| **Dukungan Penalaran Logis (*Logical Thinking Support*)** | Keberadaan fitur dasbor guru yang memfasilitasi pendidik dalam mendeteksi dimensi penalaran logis yang belum dikuasai siswa secara seketika (*real-time*). |

---

### Lampiran 2. Kisi-kisi Rubrik Validasi Ahli Materi (Materi Jaringan Nirkabel & Penalaran Logis)

| Aspek Penilaian | Indikator Penilaian Operasional |
| :--- | :--- |
| **Substansi Materi Jaringan Nirkabel** | Akurasi konsep topologi Ad-Hoc vs Infrastruktur; kebenaran konsep frekuensi nirkabel dan alokasi kanal *non-overlapping*; kebenaran prosedur konfigurasi SSID dan enkripsi WPA2/WPA3. |
| **Konstruksi Fase Troubleshooting Jonassen** | Keselarasan butir kuis dan butir tes dengan 5 fase kognitif penalaran troubleshooting Jonassen (2006) (*Controlling Variables, Proportional, Combinatorial, Probabilistic, Correlational*). |
| **Taksonomi Knowledge Components (KC)** | Ketepatan dekomposisi materi teknologi jaringan nirkabel ke dalam 12 KC atomik dan kesahihan relasi ketergantungan pada graf dependensi prasyarat (DAG). |
| **Integrasi Sintaks Station Rotation** | Keterlaksanaan sintaks *Station Rotation* satu ruangan lab (Zona A: Praktik Lab Mandiri 1:1; Zona B: Evaluasi Adaptif Mandiri via ponsel cerdas dan bimbingan guru bergerak). |
| **Kualitas Soal & Rubrik Penskoran** | Kejelasan rumusan butir soal *two-tier*, ketepatan kunci jawaban, berfungsinya distraktor, serta objektivitas rubrik pedoman penskoran kognitif bergradasi polikotomis (Skor 0, 1, 2). |

---

### Lampiran 3. Kuesioner System Usability Scale (SUS)

Petunjuk: Berilah tanda centang ($\checkmark$) pada kolom skala yang paling sesuai dengan persepsi Anda (Skala 1 = Sangat Tidak Setuju hingga 5 = Sangat Setuju).

| No | Butir Pernyataan Standar SUS (Brooke, 1996) | 1 (STS) | 2 (TS) | 3 (N) | 4 (S) | 5 (SS) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | Saya merasa ingin sering menggunakan sistem web LogiTrace ini dalam pembelajaran. | | | | | |
| 2 | Saya merasa sistem web LogiTrace ini terlalu rumit untuk digunakan. | | | | | |
| 3 | Saya merasa sistem web LogiTrace ini mudah digunakan. | | | | | |
| 4 | Saya membutuhkan bantuan dari orang teknis untuk dapat menggunakan sistem web ini. | | | | | |
| 5 | Saya merasa fitur-fitur pada sistem web LogiTrace ini terintegrasi dengan sangat baik. | | | | | |
| 6 | Saya merasa ada terlalu banyak hal yang tidak konsisten pada sistem web LogiTrace ini. | | | | | |
| 7 | Saya membayangkan bahwa kebanyakan orang akan dapat mempelajari sistem web ini dengan sangat cepat. | | | | | |
| 8 | Saya merasa sistem web LogiTrace ini sangat membingungkan saat digunakan. | | | | | |
| 9 | Saya merasa sangat percaya diri menggunakan sistem web LogiTrace ini. | | | | | |
| 10 | Saya perlu membiasakan diri terlebih dahulu sebelum saya dapat mengoperasikan sistem web ini dengan lancar. | | | | | |

---

### Lampiran 4. Kisi-kisi Instrumen Tes Kemampuan Logical Thinking Berbasis Penalaran Troubleshooting Jaringan

Paket instrumen paralel (Bentuk A dan Bentuk B) masing-masing memuat **36 butir soal pilihan ganda beralasan dua tingkat (*two-tier multiple choice*)**, terdiri atas 30 butir materi target (5 fase Jonassen × 6 butir) dan 6 butir kontrol NEDV:

| No | Fase Kognitif Troubleshooting (Jonassen, 2006) | Konteks Kasus Kejuruan Jaringan Kabel & Nirkabel (TKJ) | Alur Capaian Kurikulum | Bentuk Soal | Butir Bentuk A | Butir Bentuk B | Skor Maks |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| 1–6 | **1. Symptom Recognition** | Mengidentifikasi indikator LED adapter/switch, pesan galat ICMP DHU vs RTO, dan degradasi awal sinyal. | **TP 2.2** (Perawatan & Perbaikan) | *Two-Tier* | A01–A06 | B01–B06 | 12 |
| 7–12 | **2. Problem Space Construction** | Mengisolasi batas masalah (klien vs AP), verifikasi kecocokan SSID/WPA2, dan pemisahan variabel uji. | **TP 2.2** (Perawatan & Perbaikan) | *Two-Tier* | A07–A12 | B07–B12 | 12 |
| 13–18 | **3. Fault Hypothesis Generation** | Merumuskan dugaan kausalitas penurunan RSSI (-dBm) akibat kelipatan jarak dan koefisien serap material sekat. | **TP 2.1** (Instalasi Nirkabel) | *Two-Tier* | A13–A18 | B13–B18 | 12 |
| 19–24 | **4. Hypothesis Testing & Evaluation** | Menguji ambang batas roaming pemancar dan mengevaluasi probabilitas tabrakan paket (CSMA/CA) pada spektrum padat. | **TP 2.1 & 2.2** | *Two-Tier* | A19–A24 | B19–B24 | 12 |
| 25–30 | **5. Corrective Action & Verification** | Merancang alokasi kanal non-overlapping (1, 6, 11), skema topologi bebas interferensi, dan verifikasi throughput link. | **TP 2.1** (Instalasi Nirkabel) | *Two-Tier* | A25–A30 | B25–B30 | 12 |
| 31–32 | **Non-Equivalent Dependent Variable (NEDV - Kontrol)** | **Layanan Voice over IP (VoIP):** Menganalisis parameter codec audio (G.711 vs G.729), packet loss, dan latensi jitter pada komunikasi VoIP (2 butir kontrol efek tes, materi tidak diajarkan selama 4 sesi). | **TP 2.3** (Layanan VoIP) | *Two-Tier* | C01–C02 | C01–C02 | 4 |
| 33–36 | **Non-Equivalent Dependent Variable (NEDV - Kontrol)** | **Jaringan dan Perbaikan Fiber Optik:** Menganalisis redaman sambungan fusion splicer, pengukuran OTDR, bending radius, serta perbedaan kabel single-mode vs multi-mode (4 butir kontrol efek tes, materi tidak diajarkan selama 4 sesi). | **TP 2.4 & TP 2.5** (Fiber Optik) | *Two-Tier* | C03–C06 | C03–C06 | 8 |

*Pedoman Penskoran Polikotomis:*
* **Skor 2**: Jawaban *tier* 1 Benar dan Alasan *tier* 2 Benar (Penalaran Ilmiah Matang).
* **Skor 1**: Jawaban *tier* 1 Benar namun Alasan *tier* 2 Keliru (Hafalan Prosedural Semu), ATAU Jawaban *tier* 1 Keliru akibat salah perhitungan teknis minor namun Alasan *tier* 2 Benar (Pemahaman Parsial).
* **Skor 0**: Jawaban dan Alasan Keliru keduanya, atau tidak menjawab (Tidak Menguasai Konsep).  
*Skor Maksimal Total Tes Target (Butir 1–30) = 60 Poin (Skor per fase = 0 s.d. 12 poin).*  
*Skor Butir NEDV (Butir 31–36, skor 0–2 per butir) dianalisis terpisah murni sebagai variabel kontrol validitas internal.*

---

### Lampiran 5. Contoh Struktur Dokumen Knowledge Component (KC) dan DAG Prasyarat

```json
{
  "kc_id": "WLAN_ROAMING_PROB",
  "nama": "Analisis Keputusan Roaming Jalur Pemancar Nirkabel",
  "definisi": "Menganalisis probabilitas perangkat klien berpindah asosiasi sinyal dari Root Access Point ke WLAN Extender berdasarkan ambang batas kuat sinyal (roaming threshold) dan redaman udara.",
  "prasyarat": ["WLAN_FREQ_CHANNEL", "WLAN_SIGNAL_PROP", "WLAN_TOPOLOGY_BSS"],
  "indikator_menguasai": [
    "Menentukan titik perpindahan sinyal berdasarkan selisih threshold RSSI (misal -75 dBm)",
    "Memprediksi stabilitas koneksi saat berada di area overlap antar dua pemancar"
  ],
  "miskonsepsi_umum": [
    "Mengasumsikan perangkat selalu otomatis terhubung ke pemancar dengan jarak fisik terdekat tanpa memperhitungkan hysteresis threshold",
    "Mengira bahwa sinyal kuat selalu menjamin throughput data tinggi tanpa melihat interferensi kanal"
  ],
  "tingkat_tolt_dominan": ["probabilistic", "proportional"]
}
```
