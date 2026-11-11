# MODUL 01: KONTEKS RISET & PEDAGOGI MODEL STATION ROTATION
## Evaluasi Formatif Adaptif Berbasis Knowledge Tracing & RAG (LogiTrace)

---

### 1. Profil Sasaran & Masalah Pendidikan
- **Satuan Pendidikan:** Sekolah Menengah Kejuruan (SMK) Negeri 4 Bandung
- **Program Keahlian:** Teknik Komputer dan Informatika
- **Konsentrasi Keahlian:** Teknik Komputer dan Jaringan (TKJ) — Fase F (Kelas XI)
- **Rombongan Belajar:** Kelas XI TKJ 1 (Jumlah: 34 Peserta Didik)
- **Mata Pelajaran:** Teknologi Jaringan Kabel dan Nirkabel
- **Elemen Pembelajaran (Kepmenristekdikti / BSKAP No. 033/H/KR/2022):**
  - **TP 2.1:** Menerapkan instalasi jaringan kabel dan nirkabel (perencanaan pengkabelan, crimping, splicing FO, konfigurasi Access Point, SSID, kanal non-overlapping, standar IEEE 802.11a/b/g/n/ac/ax).
  - **TP 2.2:** Menerapkan perawatan dan perbaikan jaringan kabel dan nirkabel (pengukuran Optical Power Meter, Optical Time-Domain Reflectometer, analisis tabrakan kanal, troubleshooting konektivitas IP/ICMP, subnetting VLSM).

#### Permasalahan Pembelajaran Riil di SMK:
1. **Kesenjangan Kemampuan Penalaran Abstraksi (Abstract Reasoning Gap):** Siswa SMK sering kali terampil secara motorik saat mencolok kabel atau memasang perangkat, namun lemah ketika dihadapkan pada penalaran konseptual (misal: menghitung subnetting VLSM, menganalisis interferensi ko-kanal frekuensi 2.4 GHz, atau menafsirkan kode galat ICMP *Destination Host Unreachable* vs *Request Timed Out*).
2. **Keterbatasan Ruang dan Rasio PC Laboratorium:** Ruang laboratorium jaringan memiliki keterbatasan unit PC berkemampuan tinggi (17 unit PC mumpuni untuk 34 siswa), sehingga pembelajaran harus dibagi menjadi dua shift atau kelompok.
3. **Beban Kognitif Guru dalam Memantau Siswa:** Guru pengampu kesulitan mendeteksi secara dini siswa mana yang mengalami miskonsepsi saat praktikum berlangsung secara individual.

---

### 2. Desain Model Pembelajaran Station Rotation (1 Ruang Lab)

Model *Station Rotation* diterapkan secara terintegrasi dalam **satu ruang laboratorium komputer berukuran 12 m × 8 m** dengan membagi ruangan menjadi dua stasiun fisik berdampingan:

```text
+-----------------------------------------------------------------------------------+
|               LABORATORIUM JARINGAN KOMPUTER (SMK NEGERI 4 BANDUNG)               |
+-----------------------------------------+-----------------------------------------+
|                ZONA A                   |                 ZONA B                  |
|    (Stasiun Praktik Komputer / 1:1)     |   (Stasiun Evaluasi Adaptif Smartphone) |
|                                         |                                         |
|  - 17 Unit PC Desktop Workstation       |  - Meja Kolaboratif Siswa (Bentuk U/O)  |
|  - Switch Manageable, Routerboard       |  - Siswa Mengakses Web LogiTrace via HP |
|  - Patch Panel, Crimping Tool, Tester   |  - Guru Pengampu Berkeliling (Roving)   |
|  - Fusion Splicer & OPM Fiber Optic     |  - Tablet Konsol Dasbor Ambient Guru    |
|                                         |                                         |
| [Kelompok A: Rotasi 1 | Kel. B: Rotasi 2]| [Kelompok B: Rotasi 1 | Kel. A: Rotasi 2]|
+-----------------------------------------+-----------------------------------------+
|          Papan Tulis, Smart TV Layar Refleksi Bersama, & Akses Pintu Keluar       |
+-----------------------------------------------------------------------------------+
```

#### Karakteristik Kedua Zona:
1. **Zona A (Hands-on Lab Practice):**
   - Berisi 17 unit PC desktop terhubung ke switch manageable dan routerboard.
   - Siswa mengerjakan lembar kerja praktikum (*jobsheet*) konfigurasi perangkat, penarikan kabel, dan simulasi topologi jaringan pada Cisco Packet Tracer / MikroTik RouterOS.
2. **Zona B (Adaptive Formative Evaluation & Clinical Roving):**
   - Siswa duduk di meja kolaboratif membawa smartphone masing-masing yang terhubung ke jaringan Wi-Fi lokal Lab TKJ.
   - Siswa mengakses antarmuka kuis adaptif **LogiTrace** yang menyajikan butir soal pilihan ganda dua tingkat (*two-tier*) pada Zone of Proximal Development (ZPD) masing-masing.
   - Guru pengampu bertindak sebagai **Roving Teacher** yang memantau konsol ambient di tablet untuk mendeteksi siswa yang *stuck* dan memberikan bimbingan klinis tatap muka (*clinical scaffolding*).

---

### 3. Sintaks Alur Pembelajaran 80 Menit (2 Jam Pelajaran)

| Fase | Alokasi Waktu | Durasi | Aktivitas Kelompok A | Aktivitas Kelompok B | Peran Guru Pengampu |
|:---:|:---:|:---:|:---|:---|:---|
| **Fase 1** | 00:00 – 05:00 | 5 Mnt | Mengikuti apersepsi kelas dan pembagian zona | Mengikuti apersepsi kelas dan pembagian zona | Membuka kelas, menjelaskan tujuan TP 2.1 & 2.2, membagi rombel 34 siswa menjadi Kelompok A (17 siswa) dan Kelompok B (17 siswa). |
| **Fase 2 (Rotasi 1)** | 05:00 – 40:00 | 35 Mnt | **Di Zona A (Lab PC):**<br>Praktik konfigurasi jaringan kabel & nirkabel sesuai jobsheet. | **Di Zona B (Meja Kuis):**<br>Mengerjakan evaluasi formatif adaptif di smartphone (6 butir kalibrasi + 14 butir ZPD). | Melakukan *roving* aktif di Zona B membawa tablet, memantau *Top-3 Stuck Students*, dan memberikan scaffolding tatap muka. |
| **Fase 3 (Transisi)** | 40:00 – 42:00 | 2 Mnt | Merapikan PC Lab, bergerak tertib menuju Zona B. | Merapikan meja kuis, bergerak tertib menuju PC Lab Zona A. | Membunyikan sinyal bel rotasi, memandu alur pergerakan siswa di lorong tengah agar tidak bertabrakan. |
| **Fase 4 (Rotasi 2)** | 42:00 – 77:00 | 35 Mnt | **Di Zona B (Meja Kuis):**<br>Mengerjakan evaluasi formatif adaptif di smartphone. | **Di Zona A (Lab PC):**<br>Praktik konfigurasi jaringan sesuai jobsheet. | Melanjutkan pemantauan ambient console di Zona B dan supervisi keselamatan lab di Zona A. |
| **Fase 5 (Refleksi)** | 77:00 – 85:00 | 8 Mnt | Berkumpul kembali di area tengah untuk pleno refleksi bersama seluruh 34 siswa. | Berkumpul kembali di area tengah untuk pleno refleksi bersama seluruh 34 siswa. | Menekan tombol Agen T3 untuk memicu *Session Summary*, memaparkan miskonsepsi umum kelas, mengumumkan pasangan *Peer-Tutoring*, dan menutup kelas. |

---

### 4. Peran Pedagogis Roving Teacher (Clinical Scaffolding)
Guru pengampu tidak lagi mengajar secara ceramah satu arah (*teacher-centered*), melainkan bertransformasi menjadi **fasilitator klinis presisi**:
- **Bukan Membocorkan Jawaban (*Guiding, Not Solving*):** Guru mendekati siswa yang teridentifikasi mengalami kebuntuan (*stuck*) dan mengajukan pertanyaan pemicu sokratik lisan.
- **Menghubungkan Teori dan Praktik:** Guru mengaitkan kesulitan konseptual siswa di Zona B dengan fenomena fisik yang dialami di Zona A (misal: *"Mengapa tadi saat crimping kabel straight urutan pin 1, 2, 3, dan 6 sangat krusial untuk sinyal data Ethernet?"*).
- **Efisiensi Intervensi Berbasis Data:** Guru tidak perlu mendatangi seluruh 17 siswa secara acak, melainkan langsung menuju 3 siswa prioritas tertinggi yang disorot oleh Dasbor Ambient LogiTrace.
