# TABEL SPESIFIKASI SKENARIO USE CASE SISTEM LOGITRACE (RAG-KT)
## Model Pembelajaran Station Rotation — Konsentrasi Keahlian Teknik Komputer dan Jaringan (SMK TKJ)

---

**Informasi Dokumen:**
- **Sistem:** LogiTrace (Web Evaluasi Formatif Adaptif Berbasis Knowledge Tracing & RAG)
- **Model Pembelajaran:** Blended Learning — *Station Rotation* (80 Menit / 2 JP)
- **Target Sasaran:** Peserta Didik Kelas XI TKJ 1 (34 Siswa), SMK Negeri 4 Bandung
- **Mata Pelajaran:** Teknologi Jaringan Kabel dan Nirkabel (Fase F)
- **Standar Penulisan:** Standar Rekayasa Perangkat Lunak Formal (Alistair Cockburn Template / IEEE Std 830)

---

## 1. TABEL RINGKASAN DAFTAR USE CASE

| ID Use Case | Nama Use Case | Aktor Utama | Aktor Pendukung | Konteks Station Rotation |
|:---|:---|:---|:---|:---|
| **UC-01** | Autentikasi & Inisialisasi Sesi Siswa | Siswa | Guru, Datastore | Menit 05:00 (Kel. B) & Menit 42:00 (Kel. A) di Zona B |
| **UC-02** | Pengerjaan Butir Kalibrasi Cold-Start | Siswa | Engine L3, Datastore | 5–10 menit awal siswa duduk di Zona B (Butir 1–6) |
| **UC-03** | Pengerjaan Butir Evaluasi Adaptif ZPD | Siswa | Engine L3, Datastore | 25–30 menit pertengahan di Zona B (Butir 7–20) |
| **UC-04** | Permintaan Bantuan Sokratik Bertingkat | Siswa | Local LLM, Engine L3 | Terjadi di Zona B saat siswa mengalami keraguan/stuck |
| **UC-05** | Pemantauan Dasbor Ambient Real-Time | Guru | Engine L3, Datastore | Guru berkeliling membawa tablet memantau Zona B |
| **UC-06** | Pelaksanaan Intervensi Roving Tatap Muka | Guru | Siswa | Intervensi klinis personal bagi *Top-3 Stuck Students* |
| **UC-07** | Rotasi Stasiun & Transisi Ruangan | Guru, Siswa | - | Menit 40:00 – 42:00 (Pertukaran fisik Zona A & Zona B) |
| **UC-08** | Pembangkitan Refleksi Sesi & Peer-Tutoring | Guru | Local LLM, Siswa | Menit 77:00 – 85:00 (Sesi Pleno Refleksi Seluruh Kelas) |
| **UC-09** | Pelabelan Semantik & Kurasi Bank Soal | Guru | Local LLM, Datastore | Di luar jam tatap muka (Persiapan pembelajaran guru) |
| **UC-10** | Manajemen & Reset Sesi Kelas Formatif | Guru | Datastore, Engine L3 | Siklus berulang kelas formatif (Standar Reusable LMS) |
| **UC-11** | Audit Trail Interaksi Append-Only & Ekspor | Guru / Peneliti | Datastore | Analisis data skripsi, evaluasi E1–E6, & verifikasi log |

---

## 2. TABEL SKENARIO USE CASE TERINCI

---

### TABEL UC-01: Autentikasi & Inisialisasi Sesi Siswa

| Atribut Skenario | Keterangan Spesifikasi |
|:---|:---|
| **ID Use Case** | **UC-01** |
| **Nama Use Case** | **Autentikasi & Inisialisasi Sesi Siswa** |
| **Aktor Utama** | Siswa XI TKJ 1 |
| **Aktor Pendukung** | Guru Pengampu, Datastore (PostgreSQL / SQLite) |
| **Tingkat Kepentingan** | Vital (Tinggi) |
| **Konteks Pembelajaran** | Dilakukan oleh siswa saat pertama kali duduk di meja Zona B pada awal rotasinya. |
| **Pra-kondisi** | 1. Siswa telah menempati meja di Zona B.<br>2. Smartphone siswa terhubung ke jaringan Wi-Fi Lab TKJ.<br>3. Guru telah mengaktifkan sesi kelas aktif di LogiTrace. |
| **Pasca-kondisi Sukses** | 1. Siswa berhasil login dan terotentikasi ke sistem.<br>2. State kognitif awal siswa termuat ($m_{s,k} = 0.25$ untuk seluruh 12 KCs).<br>3. Antarmuka menyajikan layar instruksi kuis formatif. |
| **Pemicu (Trigger)** | Siswa membuka URL web LogiTrace pada peramban smartphone. |

#### Alur Normal (Main Flow) UC-01:
| Langkah | Aksi Aktor (Siswa) | Reaksi Sistem (LogiTrace) |
|:---:|:---|:---|
| 1 | Membuka browser smartphone dan mengakses URL LogiTrace. | Menampilkan antarmuka halaman login siswa. |
| 2 | Memasukkan kode siswa (misal: `S01` s.d. `S34`) atau nama lengkap. | Menerima input kredensial siswa. |
| 3 | Menekan tombol **"Mulai Evaluasi"**. | Memvalidasi keberadaan siswa pada daftar rombel aktif XI TKJ 1. |
| 4 | - | Memeriksa riwayat interaksi: jika siswa baru, inisialisasi state kognitif $m_{s,k} = 0.25$ untuk seluruh 12 KCs. Jika sesi lanjutan, memuat status terakhir. |
| 5 | - | Mengarahkan siswa ke halaman pengerjaan soal dan memunculkan petunjuk teknis. |

#### Alur Alternatif & Eksepsi UC-01:
| Kode Alur | Kondisi Pemicu | Langkah Penanganan Sistem & Aktor |
|:---:|:---|:---|
| **A1** | Kode siswa tidak ditemukan di database. | 1. Sistem menampilkan pesan: *"Kode siswa tidak terdaftar dalam rombel XI TKJ 1."*<br>2. Siswa memanggil Guru Roving yang sedang berkeliling di Zona B.<br>3. Guru memverifikasi nomor absen siswa dan memberikan kode identitas yang benar. |
| **E1** | Koneksi Wi-Fi lab terputus saat login. | 1. Sistem menampilkan peringatan kendala jaringan lokal.<br>2. Setelah Wi-Fi tersambung kembali, sistem mengulang proses autentikasi tanpa kehilangan data. |

---

### TABEL UC-02: Pengerjaan Butir Kalibrasi Cold-Start (Butir 1–6)

| Atribut Skenario | Keterangan Spesifikasi |
|:---|:---|
| **ID Use Case** | **UC-02** |
| **Nama Use Case** | **Pengerjaan Butir Kalibrasi Cold-Start (Butir 1–6)** |
| **Aktor Utama** | Siswa XI TKJ 1 |
| **Aktor Pendukung** | Deterministic Math Engine L3, Datastore Append-Only |
| **Tingkat Kepentingan** | Vital (Tinggi) |
| **Konteks Pembelajaran** | Dikerjakan pada 5–10 menit pertama pengerjaan di Zona B untuk mengatasi masalah *cold-start* profil kognitif. |
| **Pra-kondisi** | Siswa telah berhasil login (UC-01) dan belum menyelesaikan 6 butir kalibrasi. |
| **Pasca-kondisi Sukses** | 1. 6 butir kalibrasi berhasil dikerjakan oleh siswa.<br>2. Status penguasaan awal $m$ diperbarui secara deterministik sesuai jawaban benar/salah.<br>3. Data tersimpan permanen di tabel `interactions` dengan `is_calibration = TRUE`.<br>4. Sistem bertransisi otomatis ke Siklus Adaptif ZPD (UC-03). |
| **Pemicu (Trigger)** | Siswa menekan tombol konfirmasi siap mengerjakan soal kalibrasi. |

#### Alur Normal (Main Flow) UC-02:
| Langkah | Aksi Aktor (Siswa) | Reaksi Sistem (LogiTrace) |
|:---:|:---|:---|
| 1 | Mengonfirmasi siap memulai soal kalibrasi. | Mengambil 6 butir kalibrasi acak seimbang: 2 butir mudah ($d_1$), 2 butir sedang ($d_2$), 2 butir sulit ($d_3$) yang merepresentasikan 12 KCs. |
| 2 | - | Menyajikan butir soal kalibrasi pertama ke layar smartphone siswa dengan tombol hint dinonaktifkan (*disabled*). |
| 3 | Membaca narasi soal, gambar topologi/diagram teknis, dan opsi jawaban (A, B, C, D, E). | Menghitung waktu pengerjaan (*timer count up*). |
| 4 | Memilih salah satu opsi jawaban dan menekan tombol **"Kirim Jawaban"**. | Menerima opsi jawaban dan mencatat durasi respon siswa (*response time* dalam detik). |
| 5 | - | **Engine L3 Evaluasi:** Memeriksa kebenaran jawaban ($r = 1$ jika benar, $r = 0$ jika salah). |
| 6 | - | **Deterministic Update:** Menghitung perubahan mastery $m$ KC terkait:<br>• Jika $r=1$: $m \leftarrow m + \alpha_d (1 - m)$<br>• Jika $r=0$: $m \leftarrow m - \gamma_d m$ |
| 7 | - | Melakukan *strict clipping* $m \in [0.02, 0.98]$. |
| 8 | - | Melakukan `INSERT` append-only ke tabel `interactions` dengan flag `is_calibration = TRUE` dan `hint_used = FALSE`. |
| 9 | - | Mengulangi langkah 2–8 hingga butir ke-6 selesai. |
| 10 | - | Menampilkan pesan transisi: *"Kalibrasi awal selesai! Anda memasuki mode soal adaptif personal."* |

#### Alur Alternatif & Eksepsi UC-02:
| Kode Alur | Kondisi Pemicu | Langkah Penanganan Sistem & Aktor |
|:---:|:---|:---|
| **A1** | Siswa mencoba meminta petunjuk sokratik pada butir 1–6. | Sistem menjaga tombol hint tetap *disabled* dengan tooltip: *"Petunjuk belum tersedia pada tahap kalibrasi awal mandiri."* |
| **E1** | Siswa menutup browser secara tidak sengaja di tengah butir ke-3. | Saat siswa membuka kembali aplikasi, sistem langsung menyajikan butir ke-3 tanpa mengulang butir 1 dan 2 yang telah tersimpan di database. |

---

### TABEL UC-03: Pengerjaan Butir Evaluasi Adaptif ZPD (Butir 7–20)

| Atribut Skenario | Keterangan Spesifikasi |
|:---|:---|
| **ID Use Case** | **UC-03** |
| **Nama Use Case** | **Pengerjaan Butir Evaluasi Adaptif ZPD (Butir 7–20)** |
| **Aktor Utama** | Siswa XI TKJ 1 |
| **Aktor Pendukung** | Deterministic Math Engine L3, Datastore Append-Only |
| **Tingkat Kepentingan** | Vital (Tinggi) |
| **Konteks Pembelajaran** | Fase inti evaluasi formatif adaptif di Zona B selama 25–30 menit. |
| **Pra-kondisi** | Siswa telah menyelesaikan 6 butir kalibrasi awal (UC-02). |
| **Pasca-kondisi Sukses** | 1. Siswa menyelesaikan total 20 butir soal evaluasi formatif adaptif.<br>2. Setiap butir soal yang disajikan berada dalam Zone of Proximal Development ($\hat{p} \in [0.60, 0.85]$).<br>3. Seluruh interaksi tercatat pada tabel `interactions` (append-only).<br>4. Profil penguasaan kognitif personal 12 KCs ditampilkan di akhir sesi. |
| **Pemicu (Trigger)** | Butir kalibrasi ke-6 atau butir adaptif sebelumnya selesai disubmit. |

#### Alur Normal (Main Flow) UC-03:
| Langkah | Aksi Aktor (Siswa) | Reaksi Sistem (LogiTrace) |
|:---:|:---|:---|
| 1 | - | **Prioritas KC:** Mengidentifikasi Knowledge Component (KC) siswa yang memiliki nilai $m$ terendah atau paling membutuhkan penguatan. |
| 2 | - | **Kalkulasi Probabilitas L3:** Menghitung estimasi probabilitas sukses $\hat{p}(q)$ untuk butir yang belum dikerjakan:<br>$$\hat{p}(q) = \sigma(\text{logit}(m_{s,k_q}) + \theta_{d_q})$$ |
| 3 | - | **ZPD Filtering:** Menyaring butir soal yang masuk rentang optimal $[0.60, 0.85]$. |
| 4 | - | Menyajikan butir terpilih ke smartphone siswa beserta tombol aktif **"Minta Petunjuk"** (Agen T2). |
| 5 | Menganalisis soal dan opsi jawaban (atau meminta petunjuk sokratik via UC-04). | Memulai penghitungan waktu pengerjaan soal. |
| 6 | Memilih opsi jawaban dan menekan tombol **"Kirim Jawaban"**. | Menerima respon jawaban dan menghentikan pencatatan durasi waktu. |
| 7 | - | **Evaluasi & Update L3 Deterministik (< 1 ms):**<br>• Jika tanpa hint ($h=1.0$): update penguasaan penuh.<br>• Jika pakai hint ($h=0.5$): penalti $50\%$ pada perolehan penguasaan jika benar.<br>• Strict clipping: $m \in [0.02, 0.98]$. |
| 8 | - | Menyimpan log interaksi (`is_calibration = FALSE`) ke tabel `interactions` secara append-only. |
| 9 | - | Menyiarkan pembaruan metrik kognitif siswa via WebSocket ke Dasbor Ambient Guru (UC-05). |
| 10 | - | Mengulangi langkah 1–9 hingga butir ke-20 tuntas. |
| 11 | - | Menampilkan kartu capaian akhir formatif siswa dan visualisasi radar 12 KCs. |

#### Alur Alternatif & Eksepsi UC-03:
| Kode Alur | Kondisi Pemicu | Langkah Penanganan Sistem & Aktor |
|:---:|:---|:---|
| **A1** | Tidak ada butir tersisa yang persis masuk interval target $[0.60, 0.85]$. | Sistem memperlebar batas toleransi secara otomatis menjadi $[0.50, 0.90]$ dan memilih butir dengan jarak terdekat ke titik ideal ZPD ($0.725$). |
| **A2** | Siswa mengalami keraguan sebelum menjawab. | Siswa menekan tombol "Minta Petunjuk" (bercabang ke UC-04) sebelum melanjutkan langkah 6. |

---

### TABEL UC-04: Permintaan Bantuan Sokratik Bertingkat (Agen T2) & Fallback

| Atribut Skenario | Keterangan Spesifikasi |
|:---|:---|
| **ID Use Case** | **UC-04** |
| **Nama Use Case** | **Permintaan Bantuan Sokratik Bertingkat (Agen T2) & Fallback** |
| **Aktor Utama** | Siswa XI TKJ 1 |
| **Aktor Pendukung** | Local LLM (`Qwen2.5-3B-Instruct`), pgvector RAG, Deterministic Math Engine L3 |
| **Tingkat Kepentingan** | Tinggi (High) |
| **Konteks Pembelajaran** | Terjadi di Zona B ketika siswa ragu atau mengalami miskonsepsi saat mengerjakan butir adaptif 7–20. |
| **Pra-kondisi** | 1. Siswa sedang membuka butir soal adaptif (7–20).<br>2. Siswa belum menekan tombol submit jawaban.<br>3. Jumlah petunjuk yang digunakan pada butir tersebut belum mencapai batas maksimal (maks 3 kali). |
| **Pasca-kondisi Sukses** | 1. Siswa menerima petunjuk sokratik terpandu (< 60 kata) dengan prinsip *Guiding, Not Solving*.<br>2. Kunci jawaban terjamin tidak bocor ($100\%$ zero leakage).<br>3. Parameter penalti mastery diset $h = 0.5$ untuk butir tersebut.<br>4. Penggunaan petunjuk tercatat dalam audit trail. |
| **Pemicu (Trigger)** | Siswa mengklik tombol **"Minta Petunjuk"** pada layar pengerjaan soal. |

#### Alur Normal (Main Flow) UC-04:
| Langkah | Aksi Aktor (Siswa) | Reaksi Sistem (LogiTrace) |
|:---:|:---|:---|
| 1 | Mengklik tombol **"Minta Petunjuk"**. | Mengaktifkan indikator pemuatan dan memulai pencatatan timer latensi pemicuan Agen T2. |
| 2 | - | **RAG Retrieval:** Agen T2 mengambil teks soal, target KC, dan distractor yang sedang dibaca siswa, lalu melakukan semantic search di basis pengetahuan pgvector untuk SOP jaringan terkait. |
| 3 | - | **LLM Invocations:** Mengirim prompt sokratik ke LLM Lokal (`Qwen2.5-3B-Instruct` CPU) dengan instruksi ketat: batas 60 kata, mengajukan pertanyaan penuntun konseptual, dan dilarang menyebut kunci. |
| 4 | - | LLM menghasilkan draf teks petunjuk sokratik. |
| 5 | - | **Leakage Guard Check:** Sistem memindai teks respons menggunakan Regex Anti-Bocor untuk memastikan tidak ada token opsi jawaban benar atau frasa pembocor. |
| 6 | - | **Latency Check:** Sistem memverifikasi waktu pemrosesan $\le 3.0$ detik. |
| 7 | - | Menampilkan kartu petunjuk sokratik terpandu di layar smartphone siswa. |
| 8 | - | Menetapkan variabel pengali penguasaan $h = 0.5$ dan memperbarui flag `hint_used = TRUE`. |
| 9 | Membaca petunjuk sokratik, menyelaraskan kembali konsep berpikirnya, dan menutup dialog petunjuk. | Mengaktifkan kembali tombol pemilihan opsi jawaban kuis. |

#### Alur Alternatif & Eksepsi UC-04:
| Kode Alur | Kondisi Pemicu | Langkah Penanganan Sistem & Aktor |
|:---:|:---|:---|
| **A1** | Latensi inferensi LLM melebihi batas waktu (> 3.0 detik). | 1. Sistem segera membatalkan proses komputasi LLM.<br>2. Sistem melakukan **Instant Fallback (< 50 ms)** ke *Curated Static Hint Bank* yang telah diverifikasi guru.<br>3. Petunjuk statis terkurasi ditampilkan ke layar siswa.<br>4. Parameter $h = 0.5$ tetap diberlakukan. |
| **A2** | Teks petunjuk LLM terdeteksi mengandung token jawaban benar oleh Regex Guard. | 1. Sistem mendrop respons LLM secara instan.<br>2. Sistem langsung mengalihkan output ke *Curated Static Hint Bank* ($100\%$ zero leakage).<br>3. Sistem mencatat event leakage drop ke log audit internal untuk evaluasi keamanan E5. |
| **A3** | Siswa telah meminta 3 petunjuk pada butir yang sama. | Sistem menonaktifkan tombol hint dan memunculkan saran: *"Anda telah menggunakan batas maksimal 3 petunjuk. Silakan berkonsultasi langsung dengan Guru Roving."* |

---

### TABEL UC-05: Pemantauan Dasbor Ambient & Deteksi Top-3 Stuck Students

| Atribut Skenario | Keterangan Spesifikasi |
|:---|:---|
| **ID Use Case** | **UC-05** |
| **Nama Use Case** | **Pemantauan Dasbor Ambient & Deteksi Top-3 Stuck Students** |
| **Aktor Utama** | Guru Pengampu (Roving Teacher) |
| **Aktor Pendukung** | Deterministic Math Engine L3, Datastore, WebSocket Service |
| **Tingkat Kepentingan** | Tinggi (High) |
| **Konteks Pembelajaran** | Guru mengawasi dinamika kelas secara ambient melalui layar tablet sambil berkeliling di Zona B selama 35 menit rotasi aktif. |
| **Pra-kondisi** | 1. Guru telah login ke Dasbor Ambient LogiTrace di tablet/laptop guru.<br>2. Siswa di Zona B sedang aktif mengerjakan kuis formatif. |
| **Pasca-kondisi Sukses** | 1. Dasbor menampilkan radar diagram sebaran penguasaan 12 KCs kelas secara real-time.<br>2. Tiga siswa yang paling membutuhkan bantuan tatap muka (*Top-3 Stuck Students*) tersorot secara otomatis.<br>3. Guru memperoleh informasi diagnostik presisi untuk melakukan intervensi tatap muka (UC-06). |
| **Pemicu (Trigger)** | Data interaksi siswa yang mengalir melalui WebSocket secara berkelanjutan. |

#### Alur Normal (Main Flow) UC-05:
| Langkah | Aksi Aktor (Guru Pengampu) | Reaksi Sistem (LogiTrace) |
|:---:|:---|:---|
| 1 | Membuka dan mengamati tampilan Dasbor Ambient LogiTrace pada tablet. | Menampilkan widget status kelas, radar diagram 12 KCs, matriks siswa, dan panel notifikasi. |
| 2 | - | Menerima data evaluasi dan event pengerjaan dari seluruh siswa via WebSocket secara real-time (latensi $< 500$ ms). |
| 3 | - | **Algoritma Deteksi Stuck:** Mengevaluasi metrik komposit setiap siswa:<br>• Frekuensi hint $\ge 2$ pada butir yang sama.<br>• Durasi pengerjaan butir $> 120$ detik.<br>• Penurunan penguasaan berturut-turut pada KC yang sama ($\Delta m < 0$). |
| 4 | - | Memperbarui daftar **"Top-3 Stuck Students"** dengan kartu sorotan (nama siswa, KC bermasalah, durasi stuck, dan rekomendasi pertanyaan pemantik). |
| 5 | Mengamati indikator visual siswa yang masuk dalam daftar Top-3 Stuck. | Menjaga visualisasi data tetap responsif dan bersih dari noise kognitif. |
| 6 | Memilih salah satu siswa yang diprioritaskan untuk didatangi secara fisik di Zona B. | Menyediakan detail ringkas butir soal yang sedang dihadapi siswa tersebut. |

#### Alur Alternatif & Eksepsi UC-05:
| Kode Alur | Kondisi Pemicu | Langkah Penanganan Sistem & Aktor |
|:---:|:---|:---|
| **A1** | Seluruh siswa bekerja dalam ritme adaptif normal (tidak ada siswa berstatus stuck). | Panel Top-3 menampilkan status hijau: *"Seluruh siswa berada dalam Zona ZPD Ideal."* Guru dapat memperluas fokus pemantauan ke ketertiban lab Zona A. |
| **E1** | Koneksi WebSocket tablet guru terputus sesaat. | Sistem secara otomatis melakukan rekoneksi berkala (*auto-reconnect*) dan menyinkronkan status data terbaru dari database. |

---

### TABEL UC-06: Pelaksanaan Intervensi Klinis Tatap Muka (Roving Scaffolding)

| Atribut Skenario | Keterangan Spesifikasi |
|:---|:---|
| **ID Use Case** | **UC-06** |
| **Nama Use Case** | **Pelaksanaan Intervensi Klinis Tatap Muka (Roving Scaffolding)** |
| **Aktor Utama** | Guru Pengampu (Roving Teacher) |
| **Aktor Pendukung** | Siswa XI TKJ 1 |
| **Tingkat Kepentingan** | Tinggi (High) |
| **Konteks Pembelajaran** | Interaksi langsung tatap muka antara Guru Roving dan siswa yang teridentifikasi mengalami kebuntuan di Zona B. |
| **Pra-kondisi** | Siswa terdaftar pada panel *Top-3 Stuck Students* di Dasbor Ambient Guru (UC-05). |
| **Pasca-kondisi Sukses** | 1. Miskonsepsi berpikir siswa terurai tanpa guru membocorkan kunci jawaban.<br>2. Siswa mampu melanjutkan pengerjaan soal secara mandiri.<br>3. Status siswa keluar dari daftar *Top-3 Stuck Students*. |
| **Pemicu (Trigger)** | Guru memutuskan mendatangi meja siswa berdasarkan sorotan dasbor ambient. |

#### Alur Normal (Main Flow) UC-06:
| Langkah | Aksi Aktor (Guru Pengampu) | Aksi Aktor (Siswa) / Respon Sistem |
|:---:|:---|:---|
| 1 | Bergerak mendatangi meja siswa yang bersangkutan secara tenang di Zona B. | Siswa menyadari kehadiran guru pengampu. |
| 2 | Mengamati layar smartphone siswa untuk melihat konteks butir soal dan KC yang sedang dikerjakan. | Menunjukkan bagian soal yang membingungkan. |
| 3 | Mengajukan pertanyaan pemantik sokratik lisan (*Guiding, Not Solving*), mengaitkan teori dengan praktik yang telah/akan dilakukan di Zona A. | Mendengarkan pertanyaan guru dan merefleksikan kembali konsep jaringan yang dipelajari. |
| 4 | Membimbing penalaran teknis siswa langkah demi langkah. | Mengemukakan logika pemecahan masalah yang baru dipahaminya. |
| 5 | Mengonfirmasi pemahaman siswa dan memotivasi siswa untuk memilih opsi jawaban. | Memilih opsi jawaban di aplikasi LogiTrace dan menekan kirim jawaban. |
| 6 | Berpindah untuk melanjutkan pengawasan keliling (roving). | Sistem LogiTrace memperbarui metrik, dan nama siswa otomatis terhapus dari daftar Top-3 Stuck. |

#### Alur Alternatif & Eksepsi UC-06:
| Kode Alur | Kondisi Pemicu | Langkah Penanganan Sistem & Aktor |
|:---:|:---|:---|
| **A1** | Siswa mengalami defisit pemahaman konsep yang mendasar sehingga bimbingan singkat tidak cukup. | Guru menandai siswa tersebut untuk dipasangkan dengan Tutor Sebaya (*Peer-Tutoring*) berkemampuan tinggi pada sesi pleno akhir (UC-08). |

---

### TABEL UC-07: Rotasi Stasiun & Transisi Ruangan (Zona A ↔ Zona B)

| Atribut Skenario | Keterangan Spesifikasi |
|:---|:---|
| **ID Use Case** | **UC-07** |
| **Nama Use Case** | **Rotasi Stasiun & Transisi Ruangan (Zona A ↔ Zona B)** |
| **Aktor Utama** | Guru Pengampu, Siswa XI TKJ 1 (Kelompok A & Kelompok B) |
| **Aktor Pendukung** | - |
| **Tingkat Kepentingan** | Vital (Tinggi) |
| **Konteks Pembelajaran** | Terjadi tepat pada menit ke-40:00 hingga 42:00 (Durasi transisi maksimal 2 menit). |
| **Pra-kondisi** | Sesi Rotasi 1 (35 menit) telah selesai dilaksanakan. |
| **Pasca-kondisi Sukses** | 1. Kelompok A bertukar posisi fisik menempati meja Zona B.<br>2. Kelompok B bertukar posisi fisik menempati PC Lab Zona A.<br>3. Seluruh fasilitas siap pakai dan sesi Rotasi 2 dimulai tepat waktu. |
| **Pemicu (Trigger)** | Timer 35 menit Rotasi 1 berbunyi (alarm bel rotasi dari konsol guru). |

#### Alur Normal (Main Flow) UC-07:
| Langkah | Aksi Aktor (Guru Pengampu) | Aksi Aktor (Siswa Kelompok A & B) |
|:---:|:---|:---|
| 1 | Membunyikan sinyal bel rotasi dan mengumumkan: *"Waktu Rotasi 1 selesai, silakan bersiap bertukar stasiun."* | Menghentikan aktivitas pengerjaan masing-masing zona. |
| 2 | - | **Siswa Zona A (Kel. A):** Menyimpan file jobsheet di PC, merapikan kursi lab, dan bergerak tertib ke Zona B. |
| 3 | - | **Siswa Zona B (Kel. B):** Merapikan meja kuis, menyimpan smartphone, dan bergerak tertib ke PC Lab Zona A. |
| 4 | Berdiri di area lorong tengah untuk mengarahkan alur pergerakan fisik siswa agar tidak terjadi tabrakan/penumpukan. | Bergerak mengikuti jalur alur rotasi satu arah. |
| 5 | Mengonfirmasi kesiapan Kelompok B di Zona A dan Kelompok A di Zona B dalam waktu $\le 2$ menit. | Mengambil posisi duduk dan menyiapkan perlengkapan belajar masing-masing stasiun. |
| 6 | Mengumumkan dimulainya sesi Rotasi 2 (menit 42:00 s.d. 77:00). | Kelompok A login ke LogiTrace; Kelompok B menyalakan layar PC lab dan membuka jobsheet. |

#### Alur Alternatif & Eksepsi UC-07:
| Kode Alur | Kondisi Pemicu | Langkah Penanganan Sistem & Aktor |
|:---:|:---|:---|
| **A1** | Siswa di Zona B sedang membaca soal terakhir saat bel berbunyi. | Siswa diperbolehkan menekan submit butir terakhir tersebut (karena sistem menyimpan state secara aman per butir), lalu segera berpindah zona. |

---

### TABEL UC-08: Pembangkitan Refleksi Sesi & Rekomendasi Peer-Tutoring (Agen T3)

| Atribut Skenario | Keterangan Spesifikasi |
|:---|:---|
| **ID Use Case** | **UC-08** |
| **Nama Use Case** | **Pembangkitan Refleksi Sesi & Rekomendasi Peer-Tutoring (Agen T3)** |
| **Aktor Utama** | Guru Pengampu |
| **Aktor Pendukung** | Local LLM (`Qwen2.5-3B-Instruct`), Siswa XI TKJ 1, Datastore |
| **Tingkat Kepentingan** | Tinggi (High) |
| **Konteks Pembelajaran** | Dilaksanakan pada menit ke-77:00 hingga 85:00 dalam format sesi pleno bersama seluruh 34 siswa. |
| **Pra-kondisi** | Seluruh 34 siswa telah menyelesaikan kedua siklus rotasi (baik praktik di Zona A maupun evaluasi di Zona B). |
| **Pasca-kondisi Sukses** | 1. Narasi refleksi pedagogis kelas berhasil disintesis oleh Agen T3.<br>2. Matriks rekomendasi pasangan *Peer-Tutoring* yang adil dan seimbang terbentuk secara otomatis.<br>3. Siswa mengetahui kelebihan kognitif dan mitra tutor sebaya untuk tindak lanjut pembelajaran berikutnya. |
| **Pemicu (Trigger)** | Guru menekan tombol **"Generate Summary & Peer Tutoring"** pada Dasbor Ambient. |

#### Alur Normal (Main Flow) UC-08:
| Langkah | Aksi Aktor (Guru Pengampu) | Reaksi Sistem (LogiTrace) / Siswa |
|:---:|:---|:---|
| 1 | Mengumpulkan seluruh 34 siswa di area tengah menghadap layar proyektor utama. | Seluruh siswa berkumpul dengan tertib. |
| 2 | Menekan tombol **"Generate Summary & Peer Tutoring"** pada Dasbor Guru. | Menampilkan dialog status pemrosesan agregasi data sesi. |
| 3 | - | **Agregasi Data:** Menghitung rata-rata penguasaan 12 KCs seluruh siswa dan mengidentifikasi 3 KCs terlemah kelas. |
| 4 | - | **Algoritma Matching Peer-Tutoring:** Menjalankan algoritma pemadanan bipartite: memfilter *Tutor* ($m \ge 0.70$) dan *Mentee* ($m < 0.40$) pada KC yang sama. Menetapkan 1 tutor mendampingi maksimal 2 mentee (bebas *self-pairing*). |
| 5 | - | **Sintesis Narasi LLM (Agen T3):** Mengirim data agregasi ke LLM Qwen2.5-3B untuk menghasilkan rangkuman naratif reflektif (maksimal 3 paragraf). |
| 6 | - | Menampilkan modal ringkasan refleksi kelas dan tabel matriks tutor sebaya. |
| 7 | Memaparkan hasil refleksi kelas dan mengumumkan daftar pasangan tutor sebaya melalui proyektor. | Siswa menyimak pemaparan guru dan mencatat nama mitra belajar mereka. |
| 8 | Memberikan apresiasi atas kedisiplinan rotasi dan menutup sesi pembelajaran dengan doa bersama. | Siswa merapikan perangkat lab dan bersiap meninggalkan ruangan. |

#### Alur Alternatif & Eksepsi UC-08:
| Kode Alur | Kondisi Pemicu | Langkah Penanganan Sistem & Aktor |
|:---:|:---|:---|
| **A1** | Pada suatu KC tertentu tidak ada siswa yang mencapai kriteria tutor ($m \ge 0.70$). | Algoritma secara otomatis menugaskan *"Guru Pendamping (Zona B)"* sebagai tutor bagi siswa mentee pada KC tersebut. |
| **A2** | Guru ingin menyesuaikan pasangan tutor berdasarkan dinamika sosial kelas. | Guru dapat mengubah pasangan tutor langsung pada tabel antarmuka sebelum mengesahkannya. |

---

### TABEL UC-09: Pelabelan Semantik & Kurasi Bank Soal (Agen T1)

| Atribut Skenario | Keterangan Spesifikasi |
|:---|:---|
| **ID Use Case** | **UC-09** |
| **Nama Use Case** | **Pelabelan Semantik & Kurasi Bank Soal (Agen T1)** |
| **Aktor Utama** | Guru Pengampu / Tim Kurikulum TKJ |
| **Aktor Pendukung** | Local LLM (`Qwen2.5-3B`), pgvector, Datastore |
| **Tingkat Kepentingan** | Sedang (Medium) |
| **Konteks Pembelajaran** | Dilakukan di luar jam mengajar aktif untuk memperkaya dan mengurasi bank butir soal adaptif. |
| **Pra-kondisi** | Guru memiliki draf butir soal baru (soal pilihan ganda teknis) yang belum dilabeli KC dan kesulitan. |
| **Pasca-kondisi Sukses** | 1. Butir soal terpetakan secara semantik ke salah satu dari 12 KCs kurikulum TKJ.<br>2. Tingkat kesulitan $d \in \{1, 2, 3\}$ terestimasi secara objektif.<br>3. Butir soal terverifikasi oleh guru manusia (*Human-in-the-Loop*) dan tersimpan aktif di bank soal. |
| **Pemicu (Trigger)** | Guru memasukkan teks butir soal baru pada formulir review queue. |

#### Alur Normal (Main Flow) UC-09:
| Langkah | Aksi Aktor (Guru Pengampu) | Reaksi Sistem (LogiTrace) |
|:---:|:---|:---|
| 1 | Membuka portal guru pada menu **"Review Queue Butir Soal"**. | Menampilkan antarmuka kurasi bank soal. |
| 2 | Memasukkan teks soal, opsi jawaban (A, B, C, D, E), dan kunci jawaban yang benar. | Menerima draf konten soal. |
| 3 | Mengklik tombol **"Labeli Butir Otomatis (Agen T1)"**. | Memulai analisis semantik. |
| 4 | - | **Vector Semantic Matching:** Agen T1 menghitung cosine similarity soal terhadap deskriptor 12 KCs menggunakan embeddings pgvector. |
| 5 | - | **LLM Inference:** LLM menganalisis taksonomi Bloom soal dan menghasilkan estimasi kesulitan $d \in \{1, 2, 3\}$, rekomendasi KC, dan teks justifikasi pedagogis. |
| 6 | - | Menampilkan kartu pratinjau telaah (*review card*) beserta skor keyakinan (*confidence score*). |
| 7 | Memeriksa dan memvalidasi kesesuaian rekomendasi Agen T1. | Menyediakan opsi revisi label KC atau tingkat kesulitan jika diperlukan. |
| 8 | Mengklik tombol **"Setujui & Publikasikan"**. | Menyimpan butir soal baru ke tabel bank soal aktif dengan flag `is_active = TRUE`. |

#### Alur Alternatif & Eksepsi UC-09:
| Kode Alur | Kondisi Pemicu | Langkah Penanganan Sistem & Aktor |
|:---:|:---|:---|
| **A1** | Skor keyakinan Agen T1 di bawah ambang batas ($< 0.70$). | Sistem menampilkan penanda warna kuning (*flagged for manual review*) dan mewajibkan guru memilih KC secara manual dari daftar dropdown. |

---

### TABEL UC-10: Manajemen & Reset Sesi Kelas Formatif (Standar LMS)

| Atribut Skenario | Keterangan Spesifikasi |
|:---|:---|
| **ID Use Case** | **UC-10** |
| **Nama Use Case** | **Manajemen & Reset Sesi Kelas Formatif (Standar LMS)** |
| **Aktor Utama** | Guru Pengampu |
| **Aktor Pendukung** | Datastore, Deterministic Math Engine L3 |
| **Tingkat Kepentingan** | Sedang (Medium) |
| **Konteks Pembelajaran** | Pengelolaan siklus pembelajaran antar-pertemuan agar sistem dapat digunakan berulang kali (*reusable*) menyerupai Google Classroom. |
| **Pra-kondisi** | Guru memiliki hak akses otentikasi pengampu kelas XI TKJ 1. |
| **Pasca-kondisi Sukses** | 1. Sesi pembelajaran sebelumnya diarsipkan secara aman tanpa kehilangan data log.<br>2. Sesi kelas baru terbentuk dengan state kognitif kembali bersih (baseline $m = 0.25$).<br>3. Dasbor Ambient siap menerima aliran pengerjaan sesi baru. |
| **Pemicu (Trigger)** | Guru ingin memulai sesi rotasi baru untuk pertemuan minggu berikutnya. |

#### Alur Normal (Main Flow) UC-10:
| Langkah | Aksi Aktor (Guru Pengampu) | Reaksi Sistem (LogiTrace) |
|:---:|:---|:---|
| 1 | Membuka menu **"Manajemen Sesi LMS"** pada dasbor guru. | Menampilkan daftar sesi kelas aktif dan arsip historis. |
| 2 | Menekan tombol **"Reset Sesi Pembelajaran / Buat Sesi Baru"**. | Menampilkan dialog konfirmasi pengarsipan sesi. |
| 3 | Mengonfirmasi tindakan reset sesi. | Melakukan pengarsipan ID sesi berjalan. |
| 4 | - | Membuat token sesi pembelajaran baru untuk Rombel XI TKJ 1. |
| 5 | - | Mereset state kognitif cache siswa kembali ke nilai baseline $m = 0.25$ untuk seluruh 12 KCs. |
| 6 | - | Mengosongkan widget pemantauan real-time pada Dasbor Ambient dan menyiarkan sinyal sesi baru. |

#### Alur Alternatif & Eksepsi UC-10:
| Kode Alur | Kondisi Pemicu | Langkah Penanganan Sistem & Aktor |
|:---:|:---|:---|
| **A1** | Terjadi kendala teknis pada satu siswa tertentu (misal: smartphone restart). | Guru dapat memilih opsi *Reset Single Student* pada baris nama siswa terkait tanpa mereset 33 siswa lainnya. |

---

### TABEL UC-11: Audit Trail Interaksi Append-Only & Ekspor Log Pembelajaran

| Atribut Skenario | Keterangan Spesifikasi |
|:---|:---|
| **ID Use Case** | **UC-11** |
| **Nama Use Case** | **Audit Trail Interaksi Append-Only & Ekspor Log Pembelajaran** |
| **Aktor Utama** | Guru Pengampu / Peneliti Skripsi |
| **Aktor Pendukung** | Datastore Append-Only (PostgreSQL / SQLite) |
| **Tingkat Kepentingan** | Tinggi (High) |
| **Konteks Pembelajaran** | Keperluan pembuktian integritas data penelitian skripsi, evaluasi metrik empiris E1 s.d. E6, dan pelaporan nilai formatif. |
| **Pra-kondisi** | Tersedia rekaman data pada tabel `interactions` hasil pengerjaan kuis siswa. |
| **Pasca-kondisi Sukses** | File data log interaksi lengkap berhasil diekspor dalam format CSV/JSON terstruktur dengan timestamp milidetik presisi. |
| **Pemicu (Trigger)** | Pengguna menekan tombol "Ekspor Log Interaksi (CSV)" pada menu pelaporan. |

#### Alur Normal (Main Flow) UC-11:
| Langkah | Aksi Aktor (Guru / Peneliti) | Reaksi Sistem (LogiTrace) |
|:---:|:---|:---|
| 1 | Mengakses menu pelaporan dan audit pada portal guru LogiTrace. | Menampilkan filter sesi, rombel, dan rentang tanggal data. |
| 2 | Memilih sesi pembelajaran yang ingin dianalisis. | Menampilkan ringkasan jumlah baris transaksi interaksi yang tersedia. |
| 3 | Mengklik tombol **"Ekspor Data Interaksi (CSV)"**. | Mengekstrak seluruh baris data dari tabel `interactions` tanpa manipulasi. |
| 4 | - | Memverifikasi kepatuhan append-only (memastikan tidak ada data yang termutasi atau terhapus). |
| 5 | - | Menyusun file CSV yang mencakup: `id`, `student_id`, `item_id`, `kc_id`, `response`, `hint_used`, `response_time_ms`, `is_calibration`, `mastery_before`, `mastery_after`, dan `created_at`. |
| 6 | - | Mengunduh file CSV secara otomatis ke perangkat pengguna. |

#### Alur Alternatif & Eksepsi UC-11:
| Kode Alur | Kondisi Pemicu | Langkah Penanganan Sistem & Aktor |
|:---:|:---|:---|
| **A1** | Pengguna menginginkan pemisahan antara data kalibrasi dan data adaptif murni. | Sistem menyediakan opsi checkbox filter: *"Kecualikan Butir Kalibrasi Cold-Start (is_calibration = FALSE)"* untuk perhitungan metrik akurasi E3. |

---

*Tabel spesifikasi use case scenario ini dirancang sebagai acuan baku rekayasa perangkat lunak dan implementasi pengujian pada Skripsi Program Studi Pendidikan Ilmu Komputer / Teknik Komputer.*
