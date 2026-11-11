# MODUL 04: REKAYASA PERANGKAT LUNAK (DIAGRAM UML & USE CASE)
## Pemodelan Swimlane Activity Diagram, Use Case Diagram, & Spesifikasi Skenario

---

### 1. Ikhtisar Diagram Rekayasa Perangkat Lunak

Pemodelan sistem LogiTrace disusun mengacu pada standar baku UML 2.5 dan metodologi rekayasa perangkat lunak formal (Cockburn Template / IEEE Std 830).

Semua diagram telah digenerasikan dalam format Draw.io asli (`.drawio`), gambar editable biner beresolusi tinggi (`.drawio.png` dengan embedded XML dan perbaikan chunk IEND), grafis vektor scalable (`.svg`), serta pratinjau (`.png`).

| Diagram | Berkas Sumber (.drawio) | Versi Editable (.drawio.png) | Versi Vektor (.svg) | Pratinjau (.png) |
|:---|:---|:---|:---|:---|
| **Activity Diagram (Station Rotation)** | [`activity_diagram_station_rotation.drawio`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/docs/diagrams/activity_diagram_station_rotation.drawio) | [`activity_diagram_station_rotation.drawio.png`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/docs/diagrams/activity_diagram_station_rotation.drawio.png) | [`activity_diagram_station_rotation.svg`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/docs/diagrams/activity_diagram_station_rotation.svg) | [`activity_diagram_station_rotation.png`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/docs/diagrams/activity_diagram_station_rotation.png) |
| **Use Case Diagram (System Boundary)** | [`use_case_diagram_station_rotation.drawio`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/docs/diagrams/use_case_diagram_station_rotation.drawio) | [`use_case_diagram_station_rotation.drawio.png`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/docs/diagrams/use_case_diagram_station_rotation.drawio.png) | [`use_case_diagram_station_rotation.svg`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/docs/diagrams/use_case_diagram_station_rotation.svg) | [`use_case_diagram_station_rotation.png`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/docs/diagrams/use_case_diagram_station_rotation.png) |

---

### 2. Activity Diagram (Swimlane UML Model Station Rotation)

Diagram aktivitas membagi alur interaksi pembelajaran formatif adaptif ke dalam **3 jalur partisi vertikal (*Swimlanes*)**:
1. **Swimlane 1: Siswa (Kelompok A & Kelompok B / 34 Siswa):**
   - Menghadiri pembukaan & menuju zona awal.
   - [Zona A]: Menjalankan jobsheet praktik konfigurasi PC Lab 1:1.
   - [Zona B]: Membuka smartphone, login akun, mengerjakan 6 butir kalibrasi cold-start.
   - [Zona B]: Memasuki siklus butir adaptif ZPD (7–20). Meminta petunjuk sokratik (Agen T2) jika ragu. Menerima bimbingan tatap muka jika berstatus *stuck*.
   - [Transisi 2 Menit]: Bertukar posisi fisik antarstasiun secara tertib (Kelompok A $\leftrightarrow$ Kelompok B).
   - [Fase Pleno Refleksi]: Berkumpul bersama, menyimak evaluasi kelas, dan menerima mitra *Peer-Tutoring*.
2. **Swimlane 2: Guru Pengampu (Roving Teacher / Fasilitator):**
   - Membuka kelas, apersepsi TP 2.1 & 2.2, membagi rombel 34 siswa menjadi Kelompok A dan B.
   - Berkeliling (*roving*) di Zona B membawa tablet pemantau.
   - Mengamati *Ambient Console* real-time: sebaran radar 12 KCs kelas dan kartu *Top-3 Stuck Students*.
   - Melakukan intervensi klinis tatap muka (*clinical scaffolding*) dengan prinsip *guiding, not solving*.
   - Membunyikan sinyal bel rotasi pada menit ke-40.
   - Menekan tombol Agen T3 pada menit ke-77, memaparkan refleksi, mengumumkan kelompok tutor sebaya, dan menutup sesi.
3. **Swimlane 3: Sistem LogiTrace (Mesin L3 & RAG Orchestrator):**
   - Autentikasi dan inisialisasi state kognitif awal ($m_{s,k} = 0.25$).
   - Menyajikan 6 butir kalibrasi cold-start acak seimbang ($d_1-d_3$) dengan flag `is_calibration = TRUE`.
   - Menghitung $\hat{p}(q) = \sigma(\text{logit}(m) + \theta_d)$ dan memfilter butir pada ZPD $[0.60, 0.85]$.
   - Merespons permintaan petunjuk Agen T2 (pgvector RAG + prompt Sokratik LLM).
   - Memeriksa batas waktu $\le 3.0$s dan *Regex Answer Leakage Guard* (dengan fallback $< 50$ ms ke bank statis jika gagal).
   - Mengeksekusi pembaruan deterministik $m \in [0.02, 0.98]$ (< 1 ms), menyisipkan log append-only ke tabel `interactions`.
   - Menyiarkan pembaruan metrik kelas via WebSocket secara real-time ke dasbor guru.
   - Mengeksekusi agregasi data kelas dan algoritma bipartite matching tutor sebaya Agen T3.

---

### 3. Use Case Diagram & Relasi Sub-Fungsi

Batas sistem (*System Boundary*) LogiTrace mengintegrasikan interaksi antara Aktor Manusia (Siswa dan Guru Roving) dengan Aktor Sistem/AI (Deterministic Math Engine L3, LLM Lokal Qwen/Cloud API, dan Datastore Append-Only):

#### Daftar Relasi & Dependensi:
- **`<<include>>` Hitung Mastery L3 (< 1 ms):** Diikutsertakan secara wajib oleh UC-02 (Pengerjaan Kalibrasi) dan UC-03 (Pengerjaan Adaptif ZPD).
- **`<<include>>` Answer Leakage Guard & Fallback:** Diikutsertakan oleh UC-04 (Bantuan Sokratik Agen T2).
- **`<<include>>` Deteksi Otomatis Top-3 Stuck Students:** Diikutsertakan oleh UC-05 (Dasbor Ambient Guru).
- **`<<include>>` Algoritma Bipartite Matching Tutor-Mentee:** Diikutsertakan oleh UC-08 (Refleksi Akhir Sesi Agen T3).
- **`<<extend>>` Permintaan Bantuan Sokratik (UC-04):** Memperluas UC-03 secara opsional ketika siswa mengalami keraguan saat mengerjakan butir adaptif.

---

### 4. Matriks 11 Skenario Use Case Terinci

Dokumentasi lengkap 11 skenario Use Case terformat dalam tabel formal metodologi Alistair Cockburn tersedia pada berkas:  
📁 [**`logitrace/docs/TABEL_USE_CASE_SCENARIO.md`**](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/docs/TABEL_USE_CASE_SCENARIO.md) dan narasi detail pada [**`logitrace/docs/USE_CASE_SCENARIO_STATION_ROTATION.md`**](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/docs/USE_CASE_SCENARIO_STATION_ROTATION.md).

#### Ringkasan Daftar Skenario:
1. **UC-01: Autentikasi & Inisialisasi Sesi Siswa** (Validasi kredensial rombel XI TKJ 1, inisialisasi baseline $m=0.25$).
2. **UC-02: Pengerjaan Butir Kalibrasi Cold-Start (1–6)** (6 butir acak seimbang $d_1-d_3$, petunjuk nonaktif, flag `is_calibration = TRUE`).
3. **UC-03: Pengerjaan Butir Adaptif ZPD (7–20)** (Penyajian butir interval $\hat{p} \in [0.60, 0.85]$, update $m$, audit append-only).
4. **UC-04: Permintaan Bantuan Sokratik Bertingkat (Agen T2)** (Scaffolding < 60 kata, zero leakage, SLA 3.0s, fallback < 50ms, penalti $h=0.5$).
5. **UC-05: Pemantauan Dasbor Ambient Real-Time** (Visualisasi radar 12 KCs, websocket streaming, deteksi Top-3 Stuck Students).
6. **UC-06: Pelaksanaan Intervensi Roving Tatap Muka** (Guru mendatangi meja siswa stuck, scaffolding lisan *guiding not solving*).
7. **UC-07: Rotasi Stasiun & Transisi Ruangan (Zona A $\leftrightarrow$ Zona B)** (Sinyal bel rotasi menit ke-40, transisi fisik tertib $\le 2$ menit).
8. **UC-08: Pembangkitan Refleksi Sesi & Rekomendasi Peer-Tutoring (Agen T3)** (Agregasi 12 KCs kelas, bipartite matching tutor $m \ge 0.70$ dan mentee $m < 0.40$).
9. **UC-09: Pelabelan Semantik & Kurasi Bank Soal (Agen T1)** (Embeddings pgvector, estimasi kesulitan, telaah guru manusia *Human-in-the-Loop*).
10. **UC-10: Manajemen & Reset Sesi Kelas Formatif** (Siklus ulang kelas formatif berulang / Reusable LMS mirip Google Classroom).
11. **UC-11: Audit Trail Interaksi Append-Only & Ekspor Log** (Ekspor CSV data penelitian tanpa risiko manipulasi data).
