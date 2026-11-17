# HANDOFF DOCUMENT: PANDUAN ANALISIS DATA STUDI PENDAHULUAN & PENULISAN BAB I
**Proyek Skripsi R&D — Program Studi Pendidikan Ilmu Komputer, FPMIPA UPI**

> **Tujuan Dokumen Ini:**  
> Memberikan konteks lengkap, instruksi operasional, skema rubrik penilaian, dan formula penulisan laporan ilmiah bagi sesi asisten AI berikutnya yang bertugas **menganalisis data mentah survei/observasi** dan **menyusun narasi Bab I (Latar Belakang Masalah)**.

---

## 1. KONTEKS & IDENTITAS PENELITIAN

* **Judul Penelitian Skripsi:**  
  *"Pengembangan Web Evaluasi Formatif Adaptif Berbasis Deep Knowledge Tracing (DKT) dalam Pembelajaran Station Rotation untuk Meningkatkan Logical Thinking Siswa SMK"*
* **Model Pengembangan:** Research and Development (R&D) Model ADDIE (*Analysis, Design, Development, Implementation, Evaluation*).
* **Fase Saat Ini:** **Fase 1 (Analysis / Analisis Kebutuhan & Studi Pendahuluan)**.
* **Lokus / Sekolah Mitra:** **SMKN 4 Bandung** (Jl. Kliningan No. 6, Turangga, Kec. Lengkong, Kota Bandung, Jawa Barat 40264).
* **Populasi & Sampel Sasaran:** Siswa Kelas **XI TKJ 1** (Total **39 Siswa**: 35 Laki-laki / 4 Perempuan).  
  *Catatan Khusus:* Kelas XI TKJ 1 dipilih berdasarkan rekomendasi guru karena memiliki tingkat remedial formatif paling tinggi.
* **Guru Mitra Narasumber:** Bapak **Yofi Fikri Islami Anshary, S.Pd.** (Wawancara awal: 12 Oktober 2026; jadwal observasi & survei siswa: pertengahan November 2026).
* **Materi Pembelajaran Lapangan:** **Teknologi Jaringan Nirkabel (WLAN)**, mencakup:
  - Topologi nirkabel: Mode *Ad-Hoc* (*peer-to-peer*) vs Mode *Infrastruktur* (terpusat via *Access Point*).
  - Konfigurasi perangkat: Setup SSID, autentikasi keamanan (WPA2/WPA3 password), dan mode AP.
  - Perluasan jangkauan: *WLAN Extender* (Ubiquiti/TP-Link).
  - Pengujian konektivitas (*Challenge*): Pengujian transfer data dan utilitas diagnostik ICMP (`ping`) secara *peer-to-peer*.
* **Kerangka Teoretis Kognitif:** Kerangka kerja penalaran pemecahan masalah teknis (*Cognitive Troubleshooting*) menurut David H. Jonassen & Woei Hung (2006) yang mengoperasionalkan kemampuan *Logical Thinking* ke dalam 5 fase kognitif pemecahan masalah pada jaringan nirkabel.
* **Solusi yang Diusulkan:** Integrasi komputasional AI (*Attentive Deep Knowledge Tracing*) dan desain instruksional *Station Rotation* dengan strategi pemisahan media (*Device-Purpose Split*).

---

## 2. FILE ARTIFAK & LOKASI DOKUMEN RELEVAN

Semua berkas terkait tersimpan di dalam direktori kerja:
1. `c:\kuliah\semester_7\skripsi\studi_pendahuluan_tkj\instrumen_studi_pendahuluan_v3_gform.md`  
   *(Naskah instrumen yang disebarkan ke 39 siswa SMKN 4 Bandung melalui Google Forms).*
2. `c:\kuliah\semester_7\skripsi\studi_pendahuluan_tkj\instrumen_observasi_mandiri_peneliti.md`  
   *(Logbook catatan lapangan peneliti: rasio PC lab, rekaman wawancara Pak Yofi, dan template rekap).*
3. `c:\kuliah\semester_7\skripsi\bab_1_v1.md`  
   *(Draf Bab I skripsi yang saat ini masih memuat placeholder data studi pendahuluan).*

---

## 3. INSTRUMEN PENGUMPULAN DATA & SUMBER INPUT

Sesi AI baru akan menerima data mentah dari **tiga sumber utama**:

### A. Data Mentah Kuesioner Siswa (Ekspor CSV / XLSX dari Google Forms)
Google Form terdiri atas 4 bagian:
1. **Identitas Siswa:** Nama/Inisial, Kelas (XI TKJ 1), Jenis Kelamin.
2. **Kondisi Lab & Gawai (Q4–Q7):** Rasio PC riil, dinamika pasangan (siapa yang dominan/pasif), kepemilikan smartphone, dan akses kuota/Wi-Fi.
3. **Pemetaan Kesulitan Materi & Pola Belajar (Q8–Q10):**
   * Q8: Pilihan maksimal 2 topik tersulit dari 5 spektrum kejuruan TJKT (fokus nirkabel & pengalamatan).
   * Q9: Respon pertama siswa saat praktikum eror (*troubleshooting habit*).
   * Q10: Karakteristik kuis formatif yang dialami selama ini.
4. **Tes Diagnostik Penalaran Logis Berbasis 5 Fase Troubleshooting Jonassen (2006) (Q11–Q20):**
   * 5 kasus *Two-Tier* pada konteks jaringan nirkabel (Tingkat 1: Pilihan Ganda Tindakan Teknis, Tingkat 2: Alasan Logika Tertulis Bebas).

### B. Catatan Observasi Fisik Peneliti (Dari Logbook Mandiri)
* Jumlah PC di lab SMKN 4 Bandung yang menyala vs 39 siswa hadir $\rightarrow$ Rasio empiris riil (konfirmasi awal: 1 PC untuk 2 siswa berpasangan acak).
* Pengamatan perilaku berpasangan (*dominant-passive pair*).

### C. Catatan Wawancara Guru Kejuruan (Dari Logbook Mandiri)
* Transkrip wawancara Pak Yofi Fikri Islami Anshary, S.Pd.: kuis formatif seragam ("disamain semua"), scaffolding manual hanya di remedial, 1 PC berdua dibagi acak, penilaian campur kelompok/individu, siswa disuruh coba sendiri dulu saat eror.

---

## 4. PANDUAN & RUBRIK PENILAIAN ANALISIS DATA KOGNITIF (TROUBLESHOOTING JONASSEN 2006 PADA JARINGAN NIRKABEL)

Untuk menganalisis respon siswa pada **Bagian 4 (Kasus 1 s.d. Kasus 5)**, gunakan aturan evaluasi dua-tingkat (*Two-Tier Scoring Rubric*) berikut:

> ⚠️ **ATURAN MUTLAK PENILAIAN TWO-TIER:**  
> Seorang siswa dinyatakan **BERHASIL/PAHAM (Skor 1)** jika dan hanya jika **Pilihan Ganda BENAR DAN Alasan Tertulis VALID secara logika**.  
> Jika pilihan ganda benar tetapi alasan salah/menebak ("*firasat*", "*nebak aja*", "*karena mudah*"), siswa dikategorikan **GAGAL BERNALAR / SPEKULATIF (Skor 0)**.

### Rincian Kunci & Rubrik per Kasus (Konteks Nirkabel Berbasis 5 Fase Jonassen):

#### Kasus 1: Fase *Problem Space Construction* (Isolasi Batas Masalah Adapter Lokal vs AP)
* **Kunci Pilihan:** **B** (Memeriksa adapter Wi-Fi lokal laptop sendiri, SSID, dan ketepatan password sebelum mengubah AP/router).
* **Indikator Alasan Valid:** Siswa memahami prinsip isolasi batas subsistem masalah secara mandiri (mengontrol dan menguji perangkat sendiri sebelum menyalahkan atau mereset perangkat luar/AP jaringan bersama).
* **Klasifikasi Gagal:** Memilih A (mereset AP), C, atau D; atau memilih B tanpa dasar isolasi masalah lokal.

#### Kasus 2: Fase *Fault Hypothesis Generation* (Perumusan Hipotesis Kausalitas Redaman Jarak & Sinyal)
* **Kunci Pilihan:** **A** (Koneksi Siswa A jauh lebih stabil/cepat; sinyal melemah secara kuadratik akibat redaman jarak & dinding sehingga kecepatan Siswa B turun dan packet loss naik).
* **Indikator Alasan Valid:** Siswa memahami hubungan kausalitas sebab-akibat antara jarak fisik/rintangan material terhadap penurunan daya sinyal (dBm / RSSI) dan kestabilan transmisi data.
* **Klasifikasi Gagal:** Memilih B (mengira kecepatan sama karena AP sama) atau C (miskonsepsi sinyal mantul makin kuat).

#### Kasus 3: Fase *Corrective Action & Verification* (Tindakan Solusi & Perancangan Topologi Nirkabel)
* **Kunci Pilihan:** **A** (Skenario 1 mode Ad-Hoc peer-to-peer langsung; Skenario 2 mode Infrastruktur terpusat via Access Point).
* **Indikator Alasan Valid:** Siswa mampu merencanakan kombinasi arsitektur topologi yang tepat: tanpa perantara untuk 2 node mandiri vs terpusat via AP untuk banyak node berskala besar.
* **Klasifikasi Gagal:** Memilih B, C, atau D.

#### Kasus 4: Fase *Hypothesis Testing & Evaluation* (Pengujian Probabilitas Roaming & Ambang Sinyal)
* **Kunci Pilihan:** **B** (Belum tentu langsung pindah; laptop cenderung mempertahankan koneksi lama ke AP Utama selama belum melewati roaming threshold).
* **Indikator Alasan Valid:** Siswa memahami bahwa sistem nirkabel bekerja berdasarkan hukum ambang batas (*threshold/probabilitas*) deterministik perangkat dan margin histeresis, bukan insting alami yang otomatis berpindah seketika.
* **Klasifikasi Gagal:** Memilih A (antropomorfisme mesin: menganggap laptop punya insting otomatis) atau C.

#### Kasus 5: Fase *Symptom Recognition* (Pengenalan Gejala & Respons Galat Protokol ICMP)
* **Kunci Pilihan:** **B** (Berbeda; `DHU` berkorelasi dengan kegagalan menemukan rute/IP di lokal, sedangkan `RTO` berkorelasi dengan sinyal terhubung tapi tidak ada balasan dari tujuan/terhalang firewall).
* **Indikator Alasan Valid:** Siswa mampu mengenali dan membedakan gejala galat ICMP berdasarkan letak anomali logis pada konfigurasi jaringan nirkabel.
* **Klasifikasi Gagal:** Memilih A (menyamaratakan semua eror artinya laptop terbakar) atau C.

---

## 5. TUGAS & OUTPUT YANG HARUS DIKERJAKAN SESI AI BERIKUTNYA

Ketika pengguna mengunggah data hasil survei (berupa teks ekspor, tabel ringkasan, atau file CSV/Excel dari 39 siswa XI TKJ 1 SMKN 4 Bandung):

### Langkah 1: Tabulasi & Kalkulasi Statistik Deskriptif
1. Konfirmasi total responden ($N = 39$).
2. Hitung persentase keterbatasan fasilitas lab:
   * Rasio PC riil (persentase siswa yang berbagi 1 PC berdua).
   * Persentase siswa yang mengalami peran pasif (*dominant-passive pair*).
   * Persentase kepemilikan smartphone dan akses internet.
3. Hitung distribusi peringkat materi tersulit (Pertanyaan No. 8) dari 5 spektrum kejuruan.
4. Hitung persentase kebiasaan praktikum saat eror (contek teman vs spekulasi acak vs analisis mandiri).
5. Hitung skor Two-Tier untuk **kelima fase kognitif troubleshooting Jonassen (2006)**:
   * Persentase siswa yang Lulus/Paham vs Persentase Siswa yang Gagal Bernalar pada masing-masing fase (Kasus 1 s.d. 5).
   * Ekstraksi kutipan alasan verbal siswa yang paling representatif untuk menunjukkan miskonsepsi kognitif.

### Langkah 2: Penyusunan Laporan Sintesis Hasil Studi Pendahuluan
Buat tabel rekapitulasi komprehensif yang memuat:
* Indikator temuan, frekuensi ($f$), persentase ($\%$), dan makna pedagogisnya.
* Kutipan kualitatif alasan siswa (menunjukkan bukti autentik cara berpikir siswa).

### Langkah 3: Integrasi Data ke Naskah BAB I Skripsi
Buka dan mutakhirkan naskah `c:\kuliah\semester_7\skripsi\proposal\proposal_skripsi_bab_1_2_3.md` (khususnya Subbab 1.1 Latar Belakang Masalah):
* Gantikan seluruh teks penanda placeholder dengan fakta empiris riil SMKN 4 Bandung:
  * `[MASUKKAN HASIL STUDI PENDAHULUAN: Nama SMK Mitra]` $\rightarrow$ **SMKN 4 Bandung**.
  * Masukkan data kuantitatif riil hasil tes diagnostik 5 fase troubleshooting Jonassen.
  * Masukkan temuan wawancara Pak Yofi Fikri Islami Anshary, S.Pd. (rasio 1:2 acak, kuis seragam, perlunya scaffolding mandiri).
* Narasi harus disusun dengan gaya bahasa akademik formal, mengalir, dan secara runtut menghubungkan 3 pilar masalah ke solusi:
  1. Keterbatasan rasio lab fisik (1:2) $\rightarrow$ pasangan dominan-pasif & nilai campur aduk.
  2. Kesenjangan daya nalar logis formal (bukti 5 fase troubleshooting Jonassen nirkabel) $\rightarrow$ siswa mekanistik & tingkat remedial formatif tinggi.
  3. Ketiadaan evaluasi formatif adaptif $\rightarrow$ guru terkendala waktu mendiagnosis kelemahan per individu secara real-time.
  4. Sintesis solusi: **Web LogiTrace dalam Pembelajaran Station Rotation (Device-Purpose Split)**.

---
*Dokumen ini menjamin kontinuitas analisis data pada sesi AI berikutnya tanpa kehilangan konteks lapangan.*
