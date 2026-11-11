# BAB III
# METODOLOGI PENELITIAN

## 3.1 Model Pengembangan Penelitian (Model ADDIE)

Penelitian ini merupakan penelitian pengembangan atau *Research and Development* (R&D). Mengacu pada Borg dan Gall (1983) serta Richey dan Klein (2007), penelitian R&D dalam bidang pendidikan bertujuan meneliti, merancang, memproduksi, serta memvalidasi produk atau intervensi instruksional baru guna memecahkan permasalahan pembelajaran nyata di lapangan. Produk yang dikembangkan dalam penelitian ini adalah **Media Web Evaluasi Formatif Adaptif Berbasis Deep Knowledge Tracing (DKT) yang diintegrasikan ke dalam Model Blended Learning Tipe Station Rotation** untuk meningkatkan kemampuan *Logical Thinking* siswa SMK pada kompetensi kejuruan Teknik Komputer dan Jaringan (TKJ).

Dalam operasionalisasinya, penelitian pengembangan ini mengadopsi model instruksional **ADDIE** yang dikembangkan oleh Branch (2009). Model ADDIE dipilih karena memiliki alur sistemik yang berkesinambungan dan menyediakan siklus evaluasi formatif yang melekat pada setiap tahapannya, sehingga menjamin kualitas pengembangan produk teknologi pembelajaran maupun rancangan sintaks pedagogis. Model ADDIE terdiri atas lima fase utama:
1. **Analysis (Analisis):** Mengidentifikasi kesenjangan kinerja, hambatan fasilitas laboratorium, profil penalaran logis awal siswa, serta memetakan materi kurikulum ke dalam komponen pengetahuan (*Knowledge Components*).
2. **Design (Perancangan):** Merumuskan cetak biru (*blueprint*) arsitektur sistem perangkat lunak web, spesifikasi model kecerdasan buatan DKT, instrumen bank soal berbasis 5 dimensi TOLT, serta modul ajar model *Station Rotation*.
3. **Development (Pengembangan):** Merealisasikan rancangan menjadi produk perangkat lunak fungsional (pengkodean antarmuka pengguna, basis data, *engine* inferensi DKT, dasbor pemantauan guru), serta melaksanakan uji validasi ahli (*expert judgment*).
4. **Implementation (Implementasi):** Menerapkan sistem web evaluasi adaptif dan model pembelajaran *Station Rotation* secara nyata dalam kegiatan belajar mengajar di kelas kejuruan SMK mitra.
5. **Evaluation (Evaluasi):** Mengukur efektivitas produk terhadap peningkatan kemampuan berpikir logis siswa melalui analisis skor perolehan (*N-Gain*), menguji akurasi model AI DKT, serta mengevaluasi respons penerimaan pengguna (*usability*).

Hubungan interaktif dan siklis antarfase dalam model pengembangan ADDIE yang diadaptasi dalam penelitian ini digambarkan pada Gambar 3.1.

```
                  ┌──────────────────────────────┐
                  │       1. ANALYSIS            │
                  │ • Analisis Masalah Lab 1:2   │
                  │ • Analisis TOLT & Defisit    │
                  │ • Dekomposisi Materi ke KC   │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │       2. DESIGN              │
                  │ • Arsitektur Web & DB Schema │
                  │ • Desain LSTM-Attention DKT  │
                  │ • RPP & Sintaks 3 Stasiun    │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │       3. DEVELOPMENT         │
                  │ • Coding Frontend & Backend  │
                  │ • Integrasi Engine ONNX DKT  │
                  │ • Validasi Ahli Materi/Media │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │       4. IMPLEMENTATION      │
                  │ • Pre-test TOLT Jaringan     │
                  │ • Pembelajaran Station Rot.  │
                  │ • Post-test TOLT & Angket    │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │       5. EVALUATION          │
                  │ • Uji Efektivitas N-Gain     │
                  │ • Uji Hipotesis Statistik    │
                  │ • Evaluasi AUC/RMSE DKT      │
                  │ • Evaluasi Usability SUS     │
                  └──────────────────────────────┘
```
**Gambar 3.1** Alur Prosedural Pengembangan Model ADDIE dalam Penelitian Skripsi

---

## 3.2 Prosedur Pengembangan Sistem dan Pembelajaran

Prosedur pengembangan dijabarkan secara rinci pada setiap tahapan siklus ADDIE sebagai berikut:

### 3.2.1 Tahap Analisis (Analysis)
Tahap analisis bertujuan mendiagnosis akar permasalahan instruksional dan menetapkan spesifikasi kebutuhan sistem. Langkah-langkah pada tahap ini meliputi:
1. **Analisis Kebutuhan Lapangan (*Needs Assessment*):**
   * Mengolah temuan studi pendahuluan yang dilakukan di SMK mitra melalui observasi laboratorium komputer dan wawancara guru kejuruan.
   * Mengonfirmasi fenomena keterbatasan sarana laboratorium komputer, di mana rasio ketersediaan perangkat adalah 1 unit PC untuk 2 orang siswa. Kondisi ini memicu fenomena pasangan dominan-pasif (*dominant-passive pair*) dan menyulitkan guru dalam melakukan evaluasi kognitif individu secara mandiri.
   * Mengidentifikasi ketersediaan telepon pintar (*smartphone*) pribadi siswa dan kesiapan infrastruktur Wi-Fi sekolah sebagai basis pelaksanaan strategi *Device-Purpose Split*.
2. **Analisis Kurikulum dan Materi Pembelajaran:**
   * Menelaah Capaian Pembelajaran (CP) dan Tujuan Pembelajaran (TP) pada Kurikulum Merdeka Konsentrasi Keahlian TKJ kelas XI, khususnya elemen Perencanaan dan Pengalamatan Jaringan serta Pemasangan dan Konfigurasi Perangkat Jaringan.
   * Mendekomposisi materi pokok (konversi bilangan biner, perhitungan FLSM dan VLSM, penentuan subnet mask/CIDR, penentuan default gateway, entri tabel perutean statis, serta troubleshooting ICMP) ke dalam 12 butir *Knowledge Components* (KC) atomik.
3. **Analisis Karakteristik dan Profil Kognitif Siswa:**
   * Menganalisis profil awal siswa berdasarkan hasil tes diagnostik pendahuluan.
   * Mengidentifikasi bahwa sebagian besar siswa mengalami hambatan berpikir operasional formal, khususnya pada dimensi penalaran kombinatorik (pembagian blok VLSM non-overlapping) dan penalaran korelasional (analisis korelasi pesan galat RTO vs DHU terhadap tumpukan protokol TCP/IP).

### 3.2.2 Tahap Perancangan (Design)
Tahap perancangan menerjemahkan hasil analisis ke dalam cetak biru konseptual dan teknis yang mencakup rancangan sistem perangkat lunak, arsitektur model AI, dan desain instruksional:
1. **Perancangan Arsitektur Sistem Web Evaluasi Adaptif:**
   * *Frontend:* Antarmuka web responsif berbasis *mobile-first* menggunakan framework modern (Vue.js / React didukung Tailwind CSS) agar nyaman diakses melalui peramban ponsel pintar siswa.
   * *Backend API:* Menggunakan arsitektur RESTful berbasis FastAPI (Python) yang memiliki performa konkurensi asinkron tinggi untuk melayani kueri inferensi cerdas dan transaksi data kuis.
   * *Basis Data:* PostgreSQL untuk menyimpan relasi entitas terstruktur (profil pengguna, bank butir soal, pemetaan KC, riwayat interaksi) dan Redis Cache untuk menyimpan status kognitif tersembunyi (*hidden state* $h_t$ dan *cell state* $c_t$) setiap siswa dengan latensi akses sangat rendah ($\le 30\text{ ms}$).
   * *Dasbor Guru:* Antarmuka pemantauan kelas seketika (*real-time classroom orchestration*) berbasis protokol WebSocket untuk menampilkan visualisasi *heatmap* penguasaan kelas serta memberikan sinyal waspada (*alert*) otomatis ketika ada siswa yang mengalami kebuntuan belajar (*stuck*).
2. **Perancangan Arsitektur Model Deep Knowledge Tracing (DKT):**
   * *Struktur Jaringan:* Model *Attentive DKT* berbasis *Stacked Long Short-Term Memory* (2 lapisan LSTM, 256 unit tersembunyi) yang dipadukan dengan *Dot-Product Attention Layer* (256 dimensi) dan lapisan *Dropout* (tingkat 0,3) untuk mencegah *overfitting*.
   * *Representasi Input:* Vektor masukan *one-hot* berukuran $2M$ ($M = \text{jumlah KC}$), yang diproyeksikan melalui *Embedding Layer* berdimensi 128.
   * *Engine Aturan Adaptif:* Menentukan logika aksi antarmuka berdasarkan luaran probabilitas DKT ($y_t$):
     * $y_t \ge 0{,}80 \rightarrow$ Kategori Penguasaan Tinggi (*High Mastery*): Sistem menyajikan butir soal tantangan pengayaan (*Advanced/HOTS*);
     * $0{,}40 \le y_t < 0{,}80 \rightarrow$ Kategori Penguasaan Sedang (*Moderate*): Sistem menyajikan butir soal latihan pemantapan standar;
     * $y_t < 0{,}40 \rightarrow$ Kategori Penguasaan Rendah (*Low Mastery*): Sistem menyajikan butir soal bergradasi mudah disertai bantuan petunjuk konsep (*scaffolding hint*);
     * Siswa salah 3 kali berturut-turut pada konsep yang sama $\rightarrow$ Status *Stuck*: Sistem mengunci sementara pengerjaan soal, memunculkan modal video remedi mikro (durasi 2 menit), dan mengirimkan notifikasi intervensi ke dasbor guru.
3. **Perancangan Desain Instruksional (Modul Ajar Station Rotation):**
   * Menyusun Rencana Pelaksanaan Pembelajaran (RPP) / Modul Ajar model *Station Rotation* 3 stasiun yang menerapkan strategi *Device-Purpose Split*.
   * Menetapkan durasi dan alur rotasi: 10 menit kuis diagnostik awal mandiri via ponsel, $2 \times 35$ menit rotasi resiprokal kelompok (Stasiun Praktik Lab 1:1 dan Stasiun Bimbingan Guru berbasis dasbor DKT), serta 10 menit kuis refleksi akhir.

### 3.2.3 Tahap Pengembangan (Development)
Tahap pengembangan adalah fase realisasi konstruksi produk fisik dan digital, instrumen evaluasi, serta pengujian validitas kelayakan:
1. **Pengkodean Perangkat Lunak (*Software Engineering*):**
   * Mengembangkan antarmuka pengguna responsif sesuai rancangan tata letak (*wireframe*).
   * Membangun basis data dan mengimplementasikan titik akhir (*endpoints*) API untuk alur autentikasi, penyajian butir soal, pencatatan log waktu respons, dan kalkulasi skor.
   * Mengekspor model DKT terlatih dari format PyTorch ke dalam format *Open Neural Network Exchange* (ONNX) guna mempercepat proses komputasi inferensi (*inference engine*) pada CPU/GPU server.
2. **Penyusunan Bank Butir Soal Evaluasi Formatif:**
   * Menyusun bank butir soal kuis adaptif pada domain pengalamatan dan konfigurasi jaringan.
   * Setiap butir soal diberi anotasi metadata yang mencakup: ID Butir, ID Komponen Pengetahuan (KC), Dimensi Penalaran TOLT (1 dari 5 dimensi), serta tingkat kesulitan estimasi awal.
3. **Validasi Ahli (*Expert Judgment*):**
   * Melakukan uji validitas isi dan konstruk oleh para ahli sebelum produk diujicobakan ke lapangan:
     * *Ahli Materi:* Dosen ahli pendidikan ilmu komputer dan guru pengampu kejuruan TKJ senior untuk memvalidasi kebenaran konsep jaringan, ketepatan pemetaan KC, dan keselarasan butir soal dengan dimensi TOLT.
     * *Ahli Media Pembelajaran:* Dosen ahli rekayasa perangkat lunak dan teknologi media pembelajaran untuk memvalidasi aspek rekayasa perangkat lunak, fungsionalitas UI/UX, stabilitas responsivitas, dan alur adaptivitas DKT.
   * Melakukan revisi produk berdasarkan catatan dan masukan perbaikan dari para validator hingga mencapai kriteria "Sangat Layak".

### 3.2.4 Tahap Implementasi (Implementation)
Tahap implementasi adalah penerapan produk sistem web DKT dan model pembelajaran *Station Rotation* secara nyata di kelas kejuruan:
1. **Sesi Orientasi dan Pre-Test:**
   * Melakukan sosialisasi prosedur teknis pengoperasian Web DKT kepada siswa dan guru.
   * Memberikan *Pre-test* Kemampuan *Logical Thinking* (TOLT Jaringan) kepada seluruh siswa untuk mengukur kemampuan awal sebelum perlakuan (*baseline measurement*).
2. **Pelaksanaan Sesi Pembelajaran Intervensi:**
   * Melaksanakan unit pembelajaran materi perencanaan pengalamatan dan konfigurasi jaringan selama serangkaian pertemuan terjadwal.
   * Pada setiap pertemuan, siswa mengikuti sintaks *Station Rotation* 3 stasiun: mengerjakan kuis formatif adaptif di ponsel pribadi (*Online Adaptive Station*), menerima bimbingan remedial kelompok terarah (*Teacher-Led Station*), dan mempraktikkan konfigurasi pada PC lab secara mandiri 1:1 (*Hands-on Lab Station*).
3. **Sesi Post-Test dan Pengisian Angket Usability:**
   * Di akhir rangkaian unit pembelajaran, seluruh siswa mengerjakan *Post-test* Kemampuan *Logical Thinking* dengan format dan tingkat kesulitan yang ekuivalen dengan *pre-test*.
   * Siswa mengisi kuesioner *System Usability Scale* (SUS) untuk mengevaluasi aspek kegunaan dan kepuasan antarmuka Web DKT.

### 3.2.5 Tahap Evaluasi (Evaluation)
Tahap evaluasi mengintegrasikan evaluasi formatif dan sumatif:
* **Evaluasi Formatif:** Berlangsung di setiap fase ADDIE (umpan balik tim ahli pada tahap desain, telaah instrumen pada tahap pengembangan, dan pemantauan kendala jaringan selama implementasi) sebagai dasar iterasi penyempurnaan media.
* **Evaluasi Sumatif:** Dilakukan pasca-implementasi untuk menilai ketercapaian tujuan penelitian secara menyeluruh, mencakup:
  1. Pengukuran peningkatan kemampuan *Logical Thinking* melalui perhitungan skor *N-Gain* dan uji beda statistik (*paired sample t-test* / Wilcoxon);
  2. Evaluasi kinerja prediksi model DKT menggunakan metrik AUC (*Area Under ROC Curve*) dan RMSE (*Root Mean Squared Error*), serta analisis grafik trajektori pertumbuhan pengetahuan (*knowledge growth curve*); dan
  3. Evaluasi kepraktisan sistem web berdasarkan skor rata-rata SUS dari persepsi siswa.

---

## 3.3 Desain Uji Coba Produk dan Pembelajaran

### 3.3.1 Desain Uji Coba Lapangan (Within-Subjects Repeated Measures Design)
Untuk membuktikan efektivitas sistem web evaluasi formatif adaptif berbasis DKT dalam model *Station Rotation*, penelitian ini menerapkan desain eksperimen **Within-Subjects Repeated Measures Design** (Desain Pengukuran Berulang Satu Kelompok Subjek) (Creswell & Creswell, 2018; Shadish et al., 2002).

Rasionalisasi pemilihan desain ini didasarkan pada pertimbangan metodologis dan etika pendidikan:
1. **Karakteristik Penelitian R&D di SMK:** Pada konteks sekolah kejuruan, jumlah rombongan belajar pada satu konsentrasi keahlian sering kali terbatas (hanya 1 atau 2 kelas per angkatan). Membagi kelas menjadi kelompok eksperimen dan kelompok kontrol konvensional berpotensi menimbulkan bias karakteristik awal yang tinggi karena keterbatasan jumlah rombel.
2. **Keadilan Akses Pembelajaran (*Educational Equity*):** Pembentukan kelas kontrol pasif yang sengaja tidak diberikan intervensi inovasi teknologi adaptif berpotensi merugikan hak kesetaraan siswa dalam memperoleh pembelajaran bermutu. Dalam desain *within-subjects*, seluruh siswa memperoleh hak perlakuan yang sama.
3. **Sensitivitas Statistik yang Lebih Tinggi (*Self-Control*):** Dalam desain pengukuran berulang, setiap subjek bertindak sebagai kontrol bagi dirinya sendiri (*participants serve as their own controls*). Pendekatan ini secara drastis mereduksi variansi kesalahan antarsubjek (*inter-subject error variance*) yang disebabkan oleh perbedaan kecerdasan bawaan, latar belakang sosial-ekonomi, atau motivasi belajar, sehingga pengujian efek perlakuan menjadi jauh lebih peka dan bertenaga (*high statistical power*).

Struktur formal desain penelitian digambarkan sebagai berikut:

$$\begin{array}{ccccc}
O_1 & \longrightarrow & X & \longrightarrow & O_2
\end{array}$$

**Tabel 3.1** Notasi dan Operasionalisasi Desain Penelitian *Within-Subjects*

| Simbol | Komponen Prosedur | Operasionalisasi Kegiatan |
| :---: | :--- | :--- |
| **$O_1$** | *Pre-test* Kemampuan *Logical Thinking* | Pengukuran awal kemampuan berpikir logis formal siswa pada domain perencanaan dan konfigurasi jaringan menggunakan instrumen TOLT Jaringan sebelum perlakuan dimulai. |
| **$X$** | Perlakuan (*Intervensi Instruksional*) | Implementasi Web Evaluasi Formatif Adaptif berbasis DKT yang diintegrasikan ke dalam sintaks model *Station Rotation* dengan strategi *Device-Purpose Split* selama 4 sesi pembelajaran tatap muka. |
| **$O_2$** | *Post-test* Kemampuan *Logical Thinking* | Pengukuran akhir kemampuan berpikir logis formal siswa menggunakan instrumen TOLT Jaringan yang ekuivalen setelah seluruh rangkaian perlakuan selesai diselenggarakan. |

Untuk menjamin validitas internal (*internal validity*) desain meskipun tanpa kelas kontrol pembanding luar, penelitian ini menerapkan kontrol ketat melalui:
* Standarisasi instrumen *pre-test* dan *post-test* yang memiliki ekuivalensi kisi-kisi dan tingkat kesukaran paralel;
* Perhitungan *Normalized Gain* ($N\text{-Gain}$) untuk menormalkan efek skor awal; serta
* Pengujian signifikansi statistik berpasangan guna memastikan bahwa peningkatan skor yang terjadi bukan disebabkan oleh faktor kebetulan (*chance event*).

### 3.3.2 Subjek dan Tempat Penelitian
* **Tempat Penelitian:** Penelitian ini dilaksanakan di Sekolah Menengah Kejuruan mitra, yaitu salah satu SMK Negeri di wilayah Provinsi Jawa Barat yang memiliki Program Keahlian Teknik Jaringan Komputer dan Telekomunikasi dengan Konsentrasi Keahlian Teknik Komputer dan Jaringan (TKJ).
* **Subjek Penelitian:** Subjek penelitian adalah siswa kelas XI TKJ pada semester ganjil tahun ajaran 2026/2027. Jumlah subjek dalam satu rombongan belajar sasaran adalah sebanyak **34 orang siswa**. Seluruh siswa dalam kelas tersebut dilibatkan secara penuh dalam seluruh tahapan uji coba intervensi.

---

## 3.4 Instrumen Pengumpulan Data

Untuk menghimpun data penelitian yang komprehensif, valid, dan reliabel, digunakan empat instrumen pengumpulan data:

### 3.4.1 Instrumen Validasi Ahli (Materi dan Media)
Lembar validasi ahli dirancang untuk menguji kelayakan isi, konstruk, dan fungsionalitas produk sebelum diimplementasikan. Instrumen menggunakan skala Likert 4 tingkat (1 = Sangat Kurang / Tidak Layak, 2 = Kurang Layak, 3 = Layak, 4 = Sangat Layak) guna menghindari kecenderungan responden memilih opsi ragu-ragu di tengah:
1. **Lembar Validasi Ahli Materi:** Menilai aspek relevansi kurikulum, kebenaran konsep materi jaringan, ketepatan taksonomi *Knowledge Components* (KC), keselarasan butir soal dengan indikator 5 dimensi TOLT, serta ketepatan materi video remedi.
2. **Lembar Validasi Ahli Media:** Menilai aspek rekayasa perangkat lunak, efisiensi arsitektur data, keterbacaan antarmuka (*UI/UX mobile*), ketepatan logika adaptif DKT, performa dasbor orkestrasi guru, serta keandalan sistem (*system reliability*).

### 3.4.2 Instrumen Tes Kemampuan Logical Thinking (Pre-test & Post-test TOLT)
Instrumen tes digunakan untuk mengukur capaian kemampuan berpikir logis siswa sebelum dan sesudah intervensi. Tes dikembangkan dengan mengadaptasi kerangka kerja baku **Test of Logical Thinking (TOLT) oleh Tobin dan Capie (1981)** yang direkontekstualisasikan ke dalam domain permasalahan konfigurasi dan rekayasa jaringan komputer. 

Instrumen terdiri atas 10 butir soal berbentuk pilihan ganda beralasan (*two-tier multiple-choice*) atau studi kasus teknis aplikatif yang mencakup 5 dimensi penalaran TOLT:
* Butir 1 & 2: Dimensi *Controlling Variables* (Isolasi anomali koneksi jaringan & penentuan variabel gangguan);
* Butir 3 & 4: Dimensi *Proportional Reasoning* (Kalkulasi proporsi prefix CIDR terhadap kapasitas host valid dan efisiensi alamat);
* Butir 5 & 6: Dimensi *Combinatorial Reasoning* (Perancangan partisi blok subnet VLSM bertingkat non-overlapping);
* Butir 7 & 8: Dimensi *Probabilistic Reasoning* (Analisis keputusan pemilihan rute terbaik berbasis AD dan probabilitas *packet loss*); serta
* Butir 9 & 10: Dimensi *Correlational Reasoning* (Korelasi pesan galat ICMP RTO/DHU terhadap status protokol tumpukan TCP/IP).

Setiap butir dinilai dengan skor dikotomis (1 jika jawaban benar beserta penalaran logis tepat, dan 0 jika salah atau penalaran tidak logis), sehingga rentang skor total tes berkisar antara 0 hingga 10.

### 3.4.3 Instrumen Angket Kepraktisan dan Usability (SUS)
Evaluasi terhadap respons kepraktisan dan kegunaan antarmuka web evaluasi DKT oleh siswa diukur menggunakan instrumen baku terstandarisasi **System Usability Scale (SUS)** yang dikembangkan oleh John Brooke (1996). Kuesioner SUS terdiri atas 10 butir pernyataan dengan skala Likert 5 poin (1 = Sangat Tidak Setuju hingga 5 = Sangat Setuju), yang disajikan secara bergantian antara pernyataan bernada positif (butir ganjil: 1, 3, 5, 7, 9) dan pernyataan bernada negatif (butir genap: 2, 4, 6, 8, 10) untuk meminimalkan bias respons siswa. Butir-butir pernyataan SUS diadaptasi ke dalam Bahasa Indonesia baku tanpa mengubah maksud psikometrik aslinya.

### 3.4.4 Log Data Interaksi DKT
Sistem web evaluasi adaptif secara otomatis merekam data transaksi sekuensial interaksi siswa ke dalam basis data PostgreSQL. Data log yang dihimpun mencakup:
* Identitas siswa (`student_id`);
* Pengenal sesi belajar (`session_id`);
* Waktu stempel interaksi (`timestamp`);
* Identitas butir soal yang disajikan (`question_id`);
* Komponen pengetahuan dan dimensi TOLT yang diuji (`concept_kc_id`);
* Kebenaran jawaban siswa ($r_t \in \{0, 1\}$);
* Durasi waktu yang dibutuhkan siswa untuk merespons dalam satuan detik (`response_time`);
* Riwayat penggunaan fitur bantuan petunjuk (`hint_used`); serta
* Nilai estimasi probabilitas penguasaan konsep hasil kalkulasi mesin DKT ($y_t$).

Data log ini berfungsi sebagai bahan evaluasi komputasional untuk mengukur akurasi prediksi model AI serta memetakan kurva pertumbuhan pengetahuan (*knowledge growth curve*) siswa secara temporal.

---

## 3.5 Teknik Analisis Data

Data yang dihimpun dalam penelitian ini dianalisis menggunakan teknik analisis kuantitatif deskriptif dan inferensial sebagai berikut:

### 3.5.1 Analisis Kelayakan dan Validitas Produk
Data hasil penilaian validator ahli materi dan ahli media dianalisis menggunakan teknik persentase kelayakan (Arikunto, 2013). Rumus persentase kelayakan dirumuskan sebagai:

$$P = \frac{\sum x}{\sum x_{\text{maks}}} \times 100\%$$

Di mana:
* $P$ = Persentase kelayakan produk (%);
* $\sum x$ = Jumlah total skor empiris yang diberikan oleh validator; dan
* $\sum x_{\text{maks}}$ = Jumlah total skor maksimum yang ideal.

Hasil persentase yang diperoleh kemudian diinterpretasikan berdasarkan kriteria kelayakan produk pada Tabel 3.2.

**Tabel 3.2** Kriteria Kelayakan Validitas Produk Pengembangan

| Rentang Persentase Kelayakan | Kategori Kevalidan / Kelayakan | Tindak Lanjut |
| :---: | :---: | :--- |
| $81\% \le P \le 100\%$ | **Sangat Layak** | Produk dapat diimplementasikan tanpa revisi besar. |
| $61\% \le P < 81\%$ | **Layak** | Produk dapat diimplementasikan setelah revisi kecil. |
| $41\% \le P < 61\%$ | **Cukup Layak** | Produk membutuhkan revisi substansial. |
| $21\% \le P < 41\%$ | **Kurang Layak** | Produk ditolak / memerlukan desain ulang mendasar. |
| $0\% \le P < 21\%$ | **Sangat Tidak Layak** | Produk tidak dapat digunakan. |

Produk Web DKT dinyatakan memenuhi kriteria kelayakan validitas untuk diuji coba ke lapangan apabila mencapai skor minimal dalam kategori **"Layak"** ($P \ge 61\%$).

### 3.5.2 Analisis Peningkatan Kemampuan Logical Thinking (N-Gain Score)
Besarnya peningkatan kemampuan *Logical Thinking* siswa antara sebelum ($O_1$) dan sesudah ($O_2$) pembelajaran dihitung menggunakan rumus faktor perolehan ternormalisasi (*Normalized Gain* / $N\text{-Gain}$) yang dirumuskan oleh Hake (1999):

$$g = \frac{S_{\text{post}} - S_{\text{pre}}}{S_{\text{maks}} - S_{\text{pre}}}$$

Di mana:
* $g$ = Nilai perolehan ternormalisasi (*N-Gain score*);
* $S_{\text{post}}$ = Skor capaian *post-test* siswa;
* $S_{\text{pre}}$ = Skor capaian *pre-test* siswa; dan
* $S_{\text{maks}}$ = Skor maksimum ideal yang mungkin diperoleh siswa ($S_{\text{maks}} = 10$).

Kategori perolehan skor $N\text{-Gain}$ diinterpretasikan mengacu pada klasifikasi Hake (1999) yang disajikan pada Tabel 3.3.

**Tabel 3.3** Kategori Perolehan *N-Gain Score*

| Nilai Perolehan ($g$) | Kategori Efektivitas Peningkatan |
| :---: | :---: |
| $g \ge 0{,}70$ | **Tinggi** |
| $0{,}30 \le g < 0{,}70$ | **Sedang** |
| $g < 0{,}30$ | **Rendah** |

Penerapan Web DKT dalam *Station Rotation* dinyatakan efektif meningkatkan kemampuan berpikir logis siswa apabila nilai rata-rata perolehan $N\text{-Gain}$ kelas berada minimal pada kategori **"Sedang"** ($g \ge 0{,}30$).

### 3.5.3 Analisis Uji Statistik Signifikansi
Untuk menguji apakah peningkatan skor *pre-test* ke *post-test* bersifat signifikan secara statistik atau sekadar terjadi karena faktor kebetulan, dilakukan pengujian hipotesis statistik komparatif dua sampel berpasangan (*paired samples*):

#### A. Uji Prasyarat: Uji Normalitas Distribusi Data
Karena ukuran sampel dalam penelitian ini adalah satu rombel kelas ($N = 34 \le 50$), uji normalitas distribusi terhadap data selisih skor perolehan ($D = S_{\text{post}} - S_{\text{pre}}$) dilakukan menggunakan uji **Shapiro-Wilk** (Razali & Wah, 2011). 
* Kriteria Uji: Jika nilai signifikansi $p\text{-value} > 0{,}05$, maka data berdistribusi normal; sebaliknya jika $p \le 0{,}05$, data tidak berdistribusi normal.

#### B. Uji Hipotesis Parametrik: Paired Sample t-Test
Apabila data memenuhi asumsi berdistribusi normal, pengujian hipotesis dilakukan menggunakan uji statistik parametrik **Paired Sample t-Test**. Rumus statistik uji $t$ berpasangan dinyatakan sebagai:

$$t = \frac{\bar{D}}{\frac{s_D}{\sqrt{n}}}$$

Di mana:
* $\bar{D}$ = Rata-rata selisih perbedaan antara skor *post-test* dan *pre-test* ($\bar{D} = \frac{1}{n}\sum D_i$);
* $s_D$ = Standar deviasi dari selisih perbedaan skor; dan
* $n$ = Jumlah total subjek siswa ($n = 34$).

Hipotesis statistik yang diuji:
* $H_0: \mu_D = 0$ (Tidak terdapat perbedaan yang signifikan pada kemampuan *Logical Thinking* siswa antara sebelum dan sesudah intervensi pembelajaran).
* $H_1: \mu_D > 0$ (Terdapat peningkatan yang signifikan pada kemampuan *Logical Thinking* siswa setelah intervensi pembelajaran).
* Kriteria Keputusan: Hipotesis nol ($H_0$) ditolak jika nilai signifikansi probabilitas $p\text{-value} < 0{,}05$ (pada taraf signifikansi $\alpha = 0{,}05$).

#### C. Uji Hipotesis Non-Parametrik: Wilcoxon Signed-Rank Test
Apabila data selisih skor terbukti tidak berdistribusi normal, pengujian hipotesis dialihkan menggunakan uji komparasi non-parametrik **Wilcoxon Signed-Rank Test** dengan membandingkan nilai jenjang peringkat positif dan negatif (Siegel, 1956). Kriteria penolakan $H_0$ tetap mengacu pada nilai $p\text{-value} < 0{,}05$.

### 3.5.4 Analisis Kinerja Model DKT (Akurasi Prediksi & Kurva Tracing)
Kinerja komputasional model AI *Deep Knowledge Tracing* dievaluasi secara kuantitatif melalui dua metrik evaluasi baku pembelajaran mesin (*machine learning*):

1. **Area Under the Receiver Operating Characteristic Curve (AUC):**  
   AUC mengukur kemampuan diskriminatif model DKT dalam membedakan antara siswa yang akan menjawab benar ($r=1$) dengan siswa yang akan menjawab salah ($r=0$) pada interaksi berikutnya. Nilai AUC berkisar antara 0,5 (tebakan acak) hingga 1,0 (klasifikasi sempurna). Model DKT dikategorikan memiliki performa prediktif yang baik apabila mencapai nilai $\text{AUC} \ge 0{,}75$, dan sangat unggul jika $\text{AUC} \ge 0{,}80$ (Abdelrahman et al., 2023).
2. **Root Mean Squared Error (RMSE):**  
   RMSE mengukur deviasi rata-rata antara probabilitas penguasaan kontinu yang diprediksi model ($y_t \in [0, 1]$) terhadap respons biner aktual siswa ($r_t \in \{0, 1\}$):
   $$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (r_i - y_i)^2}$$
   Nilai RMSE yang semakin kecil (mendekati 0) mengindikasikan bahwa estimasi tingkat penguasaan DKT semakin presisi terhadap performa nyata siswa.
3. **Analisis Visualisasi Kurva Pertumbuhan Pengetahuan (*Knowledge Growth Curve*):**  
   Selain metrik global, data probabilitas keluaran DKT dianalisis secara longitudinal untuk memplot grafik trajektori penguasaan konsep 5 dimensi TOLT tiap siswa dari waktu ke waktu ($t_1 \rightarrow t_n$), sehingga dinamika penguasaan dan pelenyapan miskonsepsi kognitif dapat dibuktikan secara empiris visual.

### 3.5.5 Analisis Respons Kepraktisan dan Usability Pengguna
Data respons siswa yang dihimpun melalui kuesioner *System Usability Scale* (SUS) dianalisis menggunakan prosedur penilaian standar Brooke (1996):
1. Setiap butir pernyataan bernomor $1$ sampai $10$ memiliki skor kontribusi $0$ sampai $4$:
   * Untuk pernyataan bernomor **ganjil** (butir 1, 3, 5, 7, 9): skor kontribusi adalah skor skala dikurangi 1 ($x_i - 1$);
   * Untuk pernyataan bernomor **genap** (butir 2, 4, 6, 8, 10): skor kontribusi adalah 5 dikurangi skor skala ($5 - x_i$).
2. Jumlahkan seluruh skor kontribusi dari kesepuluh butir pernyataan, kemudian kalikan jumlah tersebut dengan faktor pengali $2{,}5$ untuk menghasilkan skor akhir SUS berskala $0$ hingga $100$:
   $$\text{Skor SUS} = \left( \sum_{i \in \text{ganjil}} (x_i - 1) + \sum_{j \in \text{genap}} (5 - x_j) \right) \times 2{,}5$$
3. Hitung rata-rata skor SUS seluruh siswa responden:
   $$\overline{\text{SUS}} = \frac{1}{n} \sum_{k=1}^{n} \text{Skor SUS}_k$$

Skor rata-rata SUS kemudian dipetakan ke dalam kriteria penafsiran kegunaan menurut Bangor et al. (2008, 2009) yang merangkum tiga perspektif: *Acceptability Ranges*, *Grade Scale*, dan *Adjective Ratings*, sebagaimana dirangkum pada Tabel 3.4.

**Tabel 3.4** Matriks Penafsiran Skor *System Usability Scale* (SUS)

| Rentang Skor SUS | Rentang Penerimaan (*Acceptability*) | Skala Huruf (*Grade Scale*) | Penilaian Kualitatif (*Adjective Rating*) |
| :---: | :---: | :---: | :---: |
| $> 80{,}3$ | *Acceptable* | **A** | *Excellent / Best Imaginable* |
| $68{,}0 - 80{,}3$ | *Acceptable* | **B / C** | *Good* |
| $51{,}0 - 67{,}9$ | *Marginal (High/Low)* | **D** | *OK / Fair* |
| $< 51{,}0$ | *Not Acceptable* | **F** | *Poor / Worst Imaginable* |

Sistem Web Evaluasi Formatif DKT ditetapkan memenuhi standar kepraktisan dan akseptabilitas pengguna yang baik apabila memperoleh rata-rata skor SUS di atas ambang batas standar kelayakan industri ($\overline{\text{SUS}} \ge 68{,}0$) yang bersesuaian dengan kategori predikat kualitatif minimal **"Good"**.

---

## DAFTAR PUSTAKA

Abdelrahman, G., Wang, Q., & Nunes, B. (2023). Knowledge tracing: A survey. *ACM Computing Surveys*, 55(11), Article 224, 1–37. https://doi.org/10.1145/3569576

Arikunto, S. (2013). *Prosedur penelitian: Suatu pendekatan praktik*. Rineka Cipta.

Bangor, A., Kortum, P. T., & Miller, J. T. (2008). An empirical evaluation of the System Usability Scale. *International Journal of Human-Computer Interaction*, 24(6), 574–594. https://doi.org/10.1080/10447310802205776

Bangor, A., Kortum, P., & Miller, J. (2009). Determining what individual SUS scores mean: Adding an adjective rating scale. *Journal of Usability Studies*, 4(3), 114–123.

Borg, W. R., & Gall, M. D. (1983). *Educational research: An introduction* (Edisi ke-4). Longman.

Branch, R. M. (2009). *Approach, instructional design: The ADDIE approach*. Springer. https://doi.org/10.1007/978-0-387-09506-6

Brooke, J. (1996). SUS: A 'quick and dirty' usability scale. Dalam P. W. Jordan, B. Thomas, B. A. Weerdmeester, & I. L. McClelland (Ed.), *Usability evaluation in industry* (hlm. 189–194). Taylor & Francis.

Creswell, J. W., & Creswell, J. D. (2018). *Research design: Qualitative, quantitative, and mixed methods approaches* (Edisi ke-5). SAGE Publications.

Hake, R. R. (1999). Analyzing change/gain scores. *American Educational Research Association's Division D, Newsletter*, 1–4.

Kingma, D. P., & Ba, J. (2014). Adam: A method for stochastic optimization. *arXiv preprint arXiv:1412.6980*. https://doi.org/10.48550/arXiv.1412.6980

Pandey, S., & Karypis, G. (2019). A self-attentive model for knowledge tracing. *Proceedings of the 12th International Conference on Educational Data Mining (EDM 2019)*, 384–389.

Piech, C., Bassen, J., Huang, J., Ganguli, S., Sahami, M., Guibas, L. J., & Sohl-Dickstein, J. (2015). Deep knowledge tracing. *Advances in Neural Information Processing Systems (NeurIPS 2015)*, 28, 505–513.

Razali, N. M., & Wah, Y. B. (2011). Power comparisons of Shapiro-Wilk, Kolmogorov-Smirnov, Lilliefors and Anderson-Darling tests. *Journal of Statistical Modeling and Analytics*, 2(1), 21–33.

Richey, R. C., & Klein, J. D. (2007). *Design and development research: Methods, strategies, and issues*. Lawrence Erlbaum Associates.

Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and quasi-experimental designs for generalized causal inference*. Houghton Mifflin.

Siegel, S. (1956). *Nonparametric statistics for the behavioral sciences*. McGraw-Hill.

Tobin, K. G., & Capie, W. (1981). The development and validation of a group test of logical thinking. *Educational and Psychological Measurement*, 41(2), 413–423. https://doi.org/10.1177/001316448104100220
