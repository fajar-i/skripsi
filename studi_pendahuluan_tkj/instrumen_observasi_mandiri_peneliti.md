# LOGBOOK & PANDUAN OBSERVASI MANDIRI PENELITI
*(Dokumen Pegangan Pribadi Peneliti — Tidak Perlu Diberikan ke Guru/Siswa)*

> **Fungsi Dokumen Ini:**  
> Berisi data empiris kunjungan sekolah mitra, rekaman hasil wawancara mendalam dengan guru kejuruan TKJ, panduan observasi lab, tabel rekapitulasi data Google Form siswa (konteks materi Jaringan Nirkabel/WLAN & 5 fase penalaran troubleshooting Jonassen 2006), serta draf paragraf Bab I yang siap disalin ke naskah skripsi.

---

## 📌 DATA IDENTITAS KUNJUNGAN SEKOLAH MITRA

* **Nama Sekolah / SMK Mitra:** SMKN 4 Bandung
* **Alamat / Lokasi Sekolah:** Jl. Kliningan No. 6, Turangga, Kecamatan Lengkong, Kota Bandung, Jawa Barat 40264
* **Hari / Tanggal Wawancara Awal:** Senin, 12 Oktober 2026
* **Waktu / Jam Kunjungan:** Pukul 14.00 s.d. 15.00 WIB
* **Jadwal Observasi & Pengambilan Data Siswa:** Pertengahan November 2026
* **Nama Guru Kejuruan:** Yofi Fikri Islami Anshary, S.Pd.
* **Kelas Sasaran Penelitian:** Kelas XI TKJ 1
* **Karakteristik Khusus Kelas:** Berdasarkan catatan guru, kelas XI TKJ 1 memiliki proporsi siswa remedial yang paling tinggi pada tes formatif sementara dibandingkan kelas lainnya.
* **Jumlah Siswa Terdaftar di Kelas:** 39 Siswa (Laki-laki: 35 orang / Perempuan: 4 orang)
* **Elemen Mata Pelajaran:** Teknologi Jaringan Kabel dan Nirkabel (Konsentrasi Keahlian TKJ Fase F)
* **Fokus Materi Pokok yang Sedang Dipelajari:** Jaringan Nirkabel (*WLAN / Wireless Network*), mencakup:
  - Teori dasar nirkabel (sejarah, kriteria, kategori, dan regulasi frekuensi).
  - Topologi jaringan nirkabel: Mode *Ad-Hoc* (*peer-to-peer*) vs Mode *Infrastruktur* (terpusat via *Access Point*).
  - Konfigurasi perangkat: Setup SSID, autentikasi keamanan (*password* WPA/WPA2), dan mode *Access Point*.
  - Implementasi perangkat perluasan jangkauan: *WLAN Extender* (Ubiquiti/TP-Link) untuk keterhubungan dasar nirkabel.
  - Pengujian konektivitas (*Challenge*): Pengujian transfer data dan utilitas diagnostik ICMP (`ping`) secara *peer-to-peer*.

---

## BAGIAN 1: OBSERVASI MANDIRI FISIK LAB & INTERAKSI SISWA
*(Diisi saat jadwal observasi kelas di pertengahan November 2026)*

### A. Inventaris Komputer & Perhitungan Rasio
1. **Jumlah Komputer (PC) di Ruang Lab TKJ SMKN 4 Bandung:**
   * Total PC di meja lab: ________ Unit
   * Jumlah PC yang berfungsi normal/menyala: ________ Unit
   * Jumlah PC yang rusak/mati: ________ Unit
2. **Kalkulasi Rasio Komputer terhadap Siswa:**
   $$\text{Rasio PC} = \frac{\text{Jumlah Siswa Hadir}}{\text{Jumlah PC Berfungsi}} = \frac{\dots\dots}{\dots\dots} \approx 1\text{ PC untuk }\dots\dots\text{ Siswa}$$
   * Jumlah siswa hadir hari ini: ________ dari ________ terdaftar *(logbook mencatat 39; proposal/sistem memakai 34 — pastikan angka yang benar)*
   * [x] **1 PC : 2 Siswa (Berpasangan)** *(Terkonfirmasi awal dari wawancara guru)*
   * [ ] **1 PC : 1 Siswa (Mandiri)**
   * [ ] **1 PC : 3+ Siswa (Berkelompok)**

### B. Pengamatan Dinamika Kerja Berpasangan (*Dominant-Passive Pair*)
*Pengamatan terhadap 39 siswa yang dibagi duduk berpasangan secara acak:*
* [ ] **Terjadi Dominasi Nyata:** Hanya 1 siswa di tiap meja yang aktif mengoperasikan keyboard/mouse dan konfigurasi perangkat nirkabel, sedangkan pasangannya pasif hanya menonton/mencatat.
* [ ] **Bekerja Bergantian:** Siswa saling bertukar peran secara seimbang saat praktikum.
* **Catatan Khusus Peneliti:**  
  _________________________________________________________________________________________________  
  _________________________________________________________________________________________________

### C. Respon Siswa Ketika Praktikum Eror / Tidak Terhubung
*Pengamatan reaksi siswa saat koneksi nirkabel / ping ICMP peer-to-peer gagal:*
* [ ] Siswa mencontek setelan konfigurasi SSID/IP dari meja teman sebelahnya.
* [ ] Siswa mengubah setelan IP/password secara acak (*trial and error*) tanpa menelusuri secara runut.
* [ ] Siswa langsung memanggil guru/laboran sebelum mencoba memeriksa konfigurasi mandiri.
* [ ] Siswa memeriksa status adapter Wi-Fi dan menelusuri tabel konfigurasi secara sistematis.
* **Catatan Khusus Peneliti:**  
  _________________________________________________________________________________________________  
  _________________________________________________________________________________________________

### D. Ekosistem Smartphone & Jaringan Sekolah
* [ ] Seluruh siswa membawa smartphone pribadi ke sekolah.
* [ ] Jangkauan sinyal Access Point / Wi-Fi sekolah di area lab: [ ] Lancar [ ] Cukup [ ] Lemah

---

## BAGIAN 2: REKAMAN HASIL WAWANCARA DENGAN GURU KEJURUAN
*(Wawancara dengan Bapak Yofi Fikri Islami Anshary, S.Pd. pada 12 Oktober 2026)*

### 1. Materi Tersulit yang Sering Menjadi Kendala Siswa:
* **Pertanyaan:** *"Pak, selama mengajarkan materi jaringan kabel dan nirkabel dari dasar kelas X sampai kelas XI ini, materi apa yang anak-anak paling sering macet atau gagal paham?"*
* **Transkrip Jawaban Guru:**  
  *"Mungkin di Host hardening. Kalau di materi nirkabel, anak-anak sering kesulitan saat menghubungkan konsep topologi dengan pengujian komunikasi antar-perangkat (ICMP peer-to-peer), terutama saat mencari letak masalah kenapa perangkat tidak saling terhubung padahal SSID sudah sama."*
* **Analisis Peneliti:** Siswa mengalami kesulitan bukan pada aktivitas fisik menyalakan alat, melainkan pada penalaran logika abstrak saat terjadi kendala pengalamatan logis dan keamanan sistem.

### 2. Daya Nalar Logis vs Hafalan Prosedural:
* **Pertanyaan:** *"Kalau pas praktikum konfigurasi atau troubleshooting, anak-anak biasanya kalau eror bisa menelusuri secara runut atau cenderung bingung dan nebak-nebak, Pak?"*
* **Transkrip Jawaban Guru:**  
  *"Disuruh coba sendiri dulu, baru kalau masih tidak bisa baru dibantu."*
* **Analisis Peneliti:** Guru sudah menerapkan prinsip kemandirian belajar, namun tanpa adanya sistem pemandu bertahap (*scaffolding* cerdas), siswa yang memiliki kemampuan penalaran rendah berisiko terjebak pada kebuntuan (*stuck*) atau menghafal urutan menu tanpa menguasai alur logika sebab-akibat.

### 3. Dampak Rasio Lab dan Penilaian Individu:
* **Pertanyaan:** *"Di lab sini biasanya 1 anak pegang 1 PC atau harus berdua ya, Pak? Kalau berdua, biasanya bagaimana pembagiannya dan kendalanya apa bagi penilaian individu?"*
* **Transkrip Jawaban Guru:**  
  *"1 PC berdua, dibagikan secara acak. Penilaian kadang kelompok, kadang sendiri-sendiri."*
* **Analisis Peneliti:** Kondisi riil di SMKN 4 Bandung mengonfirmasi rasio **1 PC : 2 Siswa**. Pembagian acak berpotensi memperparah fenomena *dominant-passive pair*. Penilaian yang bersifat campur aduk (kadang kelompok, kadang mandiri) membuktikan bahwa guru kesulitan mengukur capaian kognitif murni tiap individu siswa saat fasilitas lab terbatas.

### 4. Pelaksanaan Evaluasi Formatif & Umpan Balik:
* **Pertanyaan:** *"Selama ini kalau kuis formatif harian bentuknya seperti apa ya Pak? Apakah sempat memetakan kelemahan tiap anak secara bertahap, atau waktunya terbatas?"*
* **Transkrip Jawaban Guru:**  
  *"Sampai sebelum UTS ada formatif: teoritik kuis, LKPD, praktikum. Akhir semester ada UAS sumatif teori. Ada uji kompetensi dari pemerintah untuk kelas 3 saja.*  
  *Penilaian formatif biasanya buat lihat umpan balik dari peserta didik. Kalau ada siswa yang gak bisa, dikasih treatment khusus. Kalau sumatif itu untuk akhir saja. Kalau teori kuis buat formatif.*  
  *Kalau praktikum pakai scaffolding: gak boleh maju kalau belum selesai. Soal formatif kebanyakan disusun bapak, disamain semua. Perlakuan khusus ada di pematerian dan remedial saja, tergantung kemampuan."*
* **Analisis Peneliti:** Asesmen formatif yang berjalan saat ini **masih seragam dan statis** (*"disamain semua"*). Guru sebenarnya sangat sadar pentingnya *scaffolding* dan *treatment khusus*, namun intervensi individual saat ini baru bisa dilakukan secara manual saat jam remedial di ujung pembelajaran. Hal ini membuktikan urgensi sistem evaluasi formatif cerdas (berbasis DKT) yang mampu memberikan umpan balik adaptif otomatis secara *real-time* di setiap sesi kelas.

---

## BAGIAN 3: REKAPITULASI DATA HASIL GOOGLE FORM SISWA
*(Diisi setelah survei disebarkan ke siswa kelas XI TKJ 1. Instrumen: `instrumen_studi_pendahuluan_v4_gform.md`; nomor soal di bawah mengacu ke v4.)*

* **Jumlah Responden yang Bersedia ($N$):** ______ dari ______ siswa terdaftar (Kelas XI TKJ 1 SMKN 4 Bandung)

### A. Data Fasilitas & Kebiasaan Belajar Siswa
| No | Indikator Kuantitatif Temuan | Frekuensi ($f$) | Persentase (%) | Makna Bukti untuk Bab I Skripsi |
|:---:|:---|:---:|:---:|---|
| 1 | No. 4 — Siswa berbagi PC (1 PC : 2 siswa atau lebih) | ...... | ...... % | Memvalidasi temuan wawancara guru tentang rasio lab. |
| 2 | No. 5 — Siswa lebih banyak melihat/mencatat (teman mendominasi) | ...... | ...... % | Indikasi fenomena *dominant-passive pair*. |
| 3 | No. 6 — Siswa membawa smartphone hampir setiap hari | ...... | ...... % | Kelayakan asesmen lewat ponsel di Zona B. |
| 4 | No. 9 — Pertama kali saat eror: bertanya teman / mengubah setelan acak | ...... | ...... % | Pola menghadapi kebuntuan. |
| 5 | No. 10a — Setuju/Sangat setuju "semua siswa mengerjakan soal yang sama" | ...... | ...... % | Gambaran keseragaman kuis formatif. |
| 6 | No. 10b — Tidak setuju/Sangat tidak setuju "tahu bagian konsep yang masih salah" | ...... | ...... % | Kebutuhan umpan balik diagnostik. |
| 7 | No. 10c — Tidak setuju/Sangat tidak setuju "tersedia petunjuk saat kesulitan" | ...... | ...... % | Kebutuhan *scaffolding*. |
| 8 | No. 11 — Menunggu bantuan guru > 5 menit atau tidak sempat dibantu | ...... | ...... % | Beban bantuan guru saat praktikum. |

### B. Pemetaan Spektrum Kesulitan Materi Kejuruan TKJ
| Pilihan Aspek Pembelajaran Jaringan | Frekuensi ($f$) | Persentase (%) | Ranking |
|:---|:---:|:---:|:---:|
| **Pengalamatan IP & Subnetting** *(IP, gateway, subnet mask)* | ...... | ...... % | ...... |
| **Konfigurasi & Topologi Nirkabel** *(Ad-Hoc vs Infrastruktur, AP, extender)* | ...... | ...... % | ...... |
| **Pengujian Koneksi & Troubleshooting (ICMP)** *(ping, analisis pesan eror)* | ...... | ...... % | ...... |
| **Keamanan Nirkabel (Host & Device Hardening)** *(WPA2/WPA3, kata sandi, pembatasan akses)* | ...... | ...... % | ...... |
| **Media & Perangkat Keras Jaringan** *(pemasangan fisik, antena, alat ukur)* | ...... | ...... % | ...... |
*(Sesuai pilihan No. 8 v4; responden boleh memilih maksimal 2, sehingga total persentase bisa > 100%.)*

### C. Hasil 5 Kasus Troubleshooting (Jonassen & Hung, 2006) — Konteks Nirkabel
*Kategori dari kombinasi pilihan × skor alasan (0–2, dinilai 2 penilai): **Paham** = benar & alasan 2; **Menebak/hafal** = benar & alasan 0–1; **Keliru menerapkan** = salah & alasan 1–2; **Miskonsepsi** = salah & alasan 0.*

| Kasus (No.) | Fase | Paham | Menebak/hafal | Keliru menerapkan | Miskonsepsi | Pengecoh terbanyak |
|:---:|:---|:-:|:-:|:-:|:-:|:-:|
| 1 (12–13) | Konstruksi ruang masalah — mengisolasi masalah ke laptop sendiri | ...% | ...% | ...% | ...% | ... |
| 2 (14–15) | Perumusan hipotesis — jarak/redaman → kualitas link | ...% | ...% | ...% | ...% | ... |
| 3 (16–17) | Tindakan korektif & verifikasi — Ad-Hoc → Infrastruktur + uji ping | ...% | ...% | ...% | ...% | ... |
| 4 (18–19) | Pengujian hipotesis — memeriksa AP yang sedang dipakai | ...% | ...% | ...% | ...% | ... |
| 5 (20–21) | Pengenalan gejala — membedakan DHU dan RTO | ...% | ...% | ...% | ...% | ... |

*Catatan: satu kasus per fase hanya memberi gambaran awal; jangan menyimpulkan kemampuan per fase tiap siswa dari data ini.*

---:|:---|:---:|:---|:---|
| **Kasus 1** | **Problem Space Construction**<br>*(Isolasi Masalah Adapter Wi-Fi Lokal vs AP)* | ...... | ...... % | Siswa berspekulasi tanpa menguji variabel internal terlebih dahulu. |
| **Kasus 2** | **Fault Hypothesis Generation**<br>*(Kausalitas Redaman Jarak/Sinyal RSSI terhadap Kualitas Link)* | ...... | ...... % | Siswa gagal menalar hubungan kausalitas non-linear sinyal nirkabel. |
| **Kasus 3** | **Corrective Action & Verification**<br>*(Perancangan Topologi Ad-Hoc vs Infrastruktur)* | ...... | ...... % | Siswa keliru membedakan kombinasi arsitektur jaringan nirkabel. |
| **Kasus 4** | **Hypothesis Testing & Evaluation**<br>*(Evaluasi Probabilitas Roaming & Ambang Sinyal)* | ...... | ...... % | Siswa mengabaikan probabilitas interferensi dan mekanisme roaming. |
| **Kasus 5** | **Symptom Recognition**<br>*(Identifikasi Gejala Galat ICMP pada Link Nirkabel)* | ...... | ...... % | Siswa menyamaratakan penyebab galat `RTO` dan `Host Unreachable`. |

---

## 📝 TEMPLATE PARAGRAF LATAR BELAKANG BAB I (TINGGAL SALIN HASIL AKHIR)

> ⚠️ **Draf lama — tulis ulang setelah data masuk.** Paragraf di bawah sudah memuat kesimpulan (mis. "defisit kemampuan berpikir logis yang nyata") sebelum ada data, dan masih menyebut DKT/RAG. Biarkan kesimpulan mengikuti angka yang benar-benar diperoleh, dan sesuaikan nama pendekatan dengan rancangan terbaru (mesin penguasaan berbasis aturan + petunjuk bertahap terkurasi).

Draf narasi lama (rujukan struktur saja):

> *"Berdasarkan studi pendahuluan yang dilaksanakan pada tanggal 12 Oktober 2026 hingga pertengahan November 2026 di SMKN 4 Bandung pada kelas XI Konsentrasi Keahlian TKJ 1 dengan melibatkan 39 orang siswa dan guru mata pelajaran kejuruan (Bapak Yofi Fikri Islami Anshary, S.Pd.), ditemukan sejumlah permasalahan empiris mendasar dalam pembelajaran dan evaluasi:*
> 
> *Pertama, dari aspek sarana prasarana, hasil wawancara dan observasi laboratorium mengonfirmasi bahwa ketersediaan unit komputer berada pada rasio 1 unit PC digunakan bersama oleh 2 orang siswa yang dibagikan secara acak. Keterbatasan ini memicu fenomena pasangan dominan-pasif, di mana sebanyak `[... %]` siswa mengaku lebih banyak menjadi pengamat pasif saat praktikum berlangsung karena perangkat didominasi oleh rekan sebangku. Kondisi ini menyulitkan guru dalam melakukan evaluasi kognitif individual yang objektif karena penilaian praktikum kerap bercampur dengan hasil kerja kelompok.*
> 
> *Kedua, dari aspek kognitif, tes diagnostik berbasis kerangka kerja penalaran pemecahan masalah teknis (Cognitive Troubleshooting Jonassen & Hung, 2006) pada materi jaringan nirkabel dan pengujian koneksi menunjukkan defisit kemampuan berpikir logis yang nyata pada kelima fase kognitifnya. Sebanyak `[... %]` siswa gagal pada fase problem space construction dalam mengisolasi variabel gangguan nirkabel, `[... %]` siswa gagal pada fase fault hypothesis generation dalam menalar kausalitas redaman jarak dan stabilitas sinyal, `[... %]` siswa gagal pada fase corrective action & verification dalam merancang topologi ad-hoc vs infrastruktur, `[... %]` siswa gagal pada fase hypothesis testing & evaluation dalam memperhitungkan ambang batas roaming jalur data, serta `[... %]` siswa gagal pada fase symptom recognition dalam mengidentifikasi gejala pesan galat ICMP. Guru mengonfirmasi bahwa kelas XI TKJ 1 merupakan kelas dengan tingkat remedial tertinggi pada evaluasi formatif sementara, yang mengindikasikan kuatnya distorsi pembelajaran mekanistik di mana siswa cenderung sekadar mengikuti petunjuk tanpa menguasai alur penalaran logika di balik konfigurasi.*
> 
> *Ketiga, hasil wawancara mengonfirmasi bahwa sistem evaluasi formatif harian yang berjalan selama ini masih bersifat seragam (*disamakan semua*) dan konvensional. Meskipun guru telah berupaya memberikan bantuan bertahap (*scaffolding*), perlakuan khusus baru dapat diberikan secara manual saat sesi remedial di akhir materi karena keterbatasan alokasi waktu mengajar. Kondisi ini menegaskan urgensi pengembangan media web evaluasi formatif adaptif (LogiTrace) berbasis Knowledge Tracing dan Retrieval-Augmented Generation (RAG) yang diintegrasikan ke dalam model pembelajaran Station Rotation dengan strategi Device-Purpose Split guna memecahkan kendala rasio komputer lab sekaligus melatih kemandirian berpikir logis siswa secara terpersonalisasi..."*

---
*Dokumen ini merupakan catatan resmi kegiatan studi pendahuluan peneliti di SMKN 4 Bandung.*
