# MODUL 02: ARSITEKTUR TIGA LAPIS SISTEM LOGITRACE (L1, L2, L3)
## Fondasi Basis Pengetahuan, Indeks Semantik, dan Mesin Kognitif Deterministik

---

### 1. Ikhtisar Arsitektur Tiga Lapis

Sistem LogiTrace dirancang menggunakan pemisahan tanggung jawab (*Separation of Concerns*) yang ketat ke dalam 3 lapisan arsitektural:

```text
+-----------------------------------------------------------------------------------+
|               ARSITEKTUR TIGA LAPIS LOGITRACE (RAG-KT ENGINE)                     |
+-----------------------------------------------------------------------------------+
|  L1: BASIS PENGETAHUAN (Knowledge Base & Prerequisite DAG)                       |
|      - 12 Knowledge Components (KCs) materi TP 2.1 & TP 2.2 TKJ                  |
|      - Taksonomi TOLT (Test of Logical Thinking) 5 Dimensi                       |
|      - Graf Berarah Bebas Siklus (DAG) Keterkaitan Prasyarat Belajar             |
+-----------------------------------------------------------------------------------+
|  L2: BANK BUTIR & INDEKS SEMANTIK (Semantic Index & Seed Bank)                   |
|      - 180 Butir Pilihan Ganda Dua Tingkat (Two-Tier Items: Tier 1 & Tier 2)      |
|      - Pemetaan Tingkat Kesulitan Objektif: d1 (Mudah), d2 (Sedang), d3 (Sulit)  |
|      - Curated Static Hint Bank (Petunjuk Statis Cadangan Bebas Halusinasi)      |
|      - Vektor Embeddings Semantik (pgvector) untuk Pengambilan Konteks           |
+-----------------------------------------------------------------------------------+
|  L3: RUNTIME DETERMINISTIK (Deterministic Cognitive Math Engine)                 |
|      - Algoritma Pelacakan Penguasaan: m <- m + alpha_d * (1 - m) * h (r=1)      |
|      - Estimasi Keberhasilan: p_hat(q) = sigma(logit(m) + theta_d)               |
|      - Strict Boundary Clipping: m in [0.02, 0.98]                               |
|      - Zone of Proximal Development (ZPD) Selection: p_hat in [0.60, 0.85]       |
|      - Transaksional Append-Only Logging pada Tabel `interactions` (Zero Update) |
+-----------------------------------------------------------------------------------+
```

---

### 2. Lapisan L1: Basis Pengetahuan & Taksonomi TOLT

L1 merepresentasikan ontologi materi kejuruan Teknik Komputer dan Jaringan yang diturunkan dari Capaian Pembelajaran Fase F:

#### A. Dua Belas Knowledge Components (12 KCs):
| Kode KC | Nama Knowledge Component | Deskripsi Ringkas Kompetensi | Prasyarat (DAG) |
|:---|:---|:---|:---|
| `KC01` | Prinsip Dasar Transmisi & Redaman Kabel | Memahami karakteristik kabel UTP/STP, redaman dB, dan standar kategori kabel Cat5e/Cat6. | - |
| `KC02` | Pengkabelan Twisted Pair (T568A/B & Crimping) | Menerapkan standar pinout T568A dan T568B, straight-through vs cross-over, serta uji kontinuitas LAN tester. | `KC01` |
| `KC03` | Arsitektur Fiber Optik (Core, Cladding, Single/Multi) | Memahami struktur fisik serat optik, mode transmisi cahaya, perbedaan Single-Mode vs Multi-Mode. | `KC01` |
| `KC04` | Alat Kerja & Penyambungan Fiber Optik (Splicer, Cleaver) | Menerapkan fungsi alat stripper, cleaver, fusion splicer, dan prosedur proteksi sambungan sleeve. | `KC03` |
| `KC05` | Pengukuran & Troubleshooting Fiber Optik (OPM & VFL) | Melakukan uji redaman optik menggunakan OPM, deteksi kebocoran core menggunakan Visual Fault Locator (VFL). | `KC04` |
| `KC06` | Standar Jaringan Nirkabel (IEEE 802.11a/b/g/n/ac/ax) | Menganalisis evolusi standar WiFi, pita frekuensi 2.4 GHz, 5 GHz, hingga 6 GHz, serta modulasi OFDMA. | - |
| `KC07` | Alokasi Frekuensi & Mitigasi Tabrakan Kanal WiFi | Menganalisis kanal non-overlapping frekuensi 2.4 GHz (1, 6, 11) dan mekanisme mitigasi interferensi ko-kanal. | `KC06` |
| `KC08` | Mode Operasi Jaringan Nirkabel (AP, Client, Bridge, WDS) | Mengkonfigurasi topologi nirkabel Infrastructure BSS, Ad-Hoc IBSS, Wireless Distribution System (WDS). | `KC06` |
| `KC09` | Parameter Kualitas Sinyal Nirkabel (RSSI, SNR, Noise) | Mendiagnosis degradasi sinyal berdasarkan nilai RSSI (dBm), rasio sinyal terhadap derau (SNR), dan noise floor. | `KC07` |
| `KC10` | Keamanan Jaringan Nirkabel (WPA2/WPA3, Enterprise) | Menerapkan enkripsi nirkabel PSK vs 802.1X EAP/RADIUS, proteksi PMF, dan pencegahan rogue AP. | `KC08` |
| `KC11` | Pengalamatan Logis IPv4 & Subnetting VLSM | Menghitung CIDR prefix, netmask, network address, broadcast, dan alokasi host menggunakan teknik VLSM. | - |
| `KC12` | Analisis Troubleshooting Jaringan (ICMP, ARP, Gateway) | Menganalisis galat Destination Host Unreachable, Request Timed Out, duplikasi IP, kegagalan default gateway. | `KC11` |

#### B. Lima Dimensi Penalaran Logis (TOLT - Test of Logical Thinking):
1. **CV (Controlling Variables):** Mengontrol variabel teknis (misal: menjaga panjang kabel tetap konstan saat menguji redaman jenis kabel berbeda).
2. **PR (Proportional Reasoning):** Penalaran proporsional (misal: menghitung rasio redaman optik per kilometer terhadap total daya transmisi SFP).
3. **CL (Combinatorial Logic):** Logika kombinatorial (misal: menentukan permutasi kanal nirkabel multi-AP tanpa saling bertabrakan).
4. **PL (Probabilistic Logic):** Penalaran probabilitas (misal: memperhitungkan peluang frame collision pada protokol CSMA/CA saat kepadatan trafik tinggi).
5. **CR (Correlational Reasoning):** Penalaran korelasional (misal: mengkorelasikan penurunan nilai SNR dengan lonjakan packet loss pada link nirkabel).

---

### 3. Lapisan L2: Bank Butir Soal & Indeks Semantik

- **Total Butir:** 180 butir soal pilihan ganda dua tingkat (*Two-Tier Multiple Choice*):
  - **Tier 1 (Factual / Procedural Choice):** Pilihan jawaban operasional (opsi A s.d. E).
  - **Tier 2 (Reasoning / Justification Choice):** Pilihan justifikasi alasan teknis mendasari pilihan Tier 1. Menghilangkan faktor tebakan (*guessing factor*).
- **Distribusi Kesulitan Butir ($d \in \{1, 2, 3\}$):**
  - $d_1$ (Mudah / Tingkat Aplikasi Dasar): 60 butir ($\theta_{d_1} = +0.90$)
  - $d_2$ (Sedang / Analisis Kasus Lab): 60 butir ($\theta_{d_2} = 0.00$)
  - $d_3$ (Sulit / Evaluasi dan Desain Troubleshooting): 60 butir ($\theta_{d_3} = -0.90$)
- **Penyimpanan:** Disimpan dalam [`logitrace/data/seed_items_180.json`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/data/seed_items_180.json).
- **Bank Petunjuk Statis Terkurasi (Curated Static Hint Bank):**
  - Disimpan dalam [`logitrace/data/fallback_hints/static_hints.json`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/data/fallback_hints/static_hints.json).
  - Terdiri dari 3 tingkat petunjuk per KC (Level 1: Konsep Inti, Level 2: Langkah Antara, Level 3: Kerangka Berpikir).
  - Menjadi fondasi *Graceful Fallback* instan (< 50 ms) yang dijamin $100\%$ bebas halusinasi dan kebocoran kunci.

---

### 4. Lapisan L3: Deterministic Cognitive Math Engine

Lapisan L3 adalah jantung komputasi sistem LogiTrace. Kode runtime L3 diimplementasikan murni menggunakan algoritma numerik matematis tanpa pemanggilan LLM pada berkas:
- [`logitrace/backend/app/engine/cognitive.py`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/backend/app/engine/cognitive.py)
- [`logitrace/backend/app/engine/zpd_selector.py`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/backend/app/engine/zpd_selector.py)
- [`logitrace/backend/app/engine/calibration.py`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/backend/app/engine/calibration.py)

#### A. Formula Estimasi Probabilitas Sukses Siswa ($\hat{p}$):
Untuk mengukur estimasi probabilitas siswa $s$ dapat menjawab butir soal $q$ dengan tingkat kesulitan $d_q$ pada KC $k_q$:
$$\hat{p}(q) = \sigma\Big(\mathrm{logit}(m_{s, k_q}) + \theta_{d_q}\Big)$$

Di mana:
- $\mathrm{logit}(m) = \ln\left(\frac{m}{1 - m}\right)$
- $\sigma(z) = \frac{1}{1 + e^{-z}}$
- Bobot kesulitan butir: $\theta_1 = +0.90$ (Mudah), $\theta_2 = 0.00$ (Sedang), $\theta_3 = -0.90$ (Sulit).

#### B. Formula Pembaruan Penguasaan Kognitif Siswa ($m$):
Setelah siswa menjawab butir soal ($r = 1$ jika benar, $r = 0$ jika salah):
$$m \leftarrow \begin{cases} 
m + \alpha_d (1 - m) h, & \text{jika } r = 1 \\ 
m - \gamma_d m, & \text{jika } r = 0 
\end{cases}$$

Di mana:
- **Laju Belajar Adaptif:** $\alpha_d = \alpha_0 \cdot \big(1 + \beta (d - 1)\big)$, dengan $\alpha_0 = 0.30, \ \beta = 0.40$.
- **Laju Lupa / Penalti Salah:** $\gamma_d = \gamma_0 \cdot \big(1 + \beta (3 - d)\big)$, dengan $\gamma_0 = 0.25$.
- **Faktor Pengali Petunjuk ($h$):**
  - $h = 1.0$ jika siswa menjawab mandiri tanpa bantuan petunjuk.
  - $h = 0.5$ jika siswa menggunakan petunjuk sokratik (penalti $50\%$ pada perolehan penguasaan).
- **Strict Boundary Clipping:** Nilai $m$ wajib dijepit (*strictly clamped*) pada interval matematis tertutup:
  $$m \in [0.02, \ 0.98]$$
  Mencegah singularitas $\pm \infty$ pada fungsi logit serta menghindari anggapan bahwa penguasaan siswa pernah mencapai mutlak $0\%$ atau mutlak $100\%$.

#### C. Algoritma Pemilihan Butir Adaptif Zone of Proximal Development (ZPD):
1. Sistem mengidentifikasi Knowledge Component (KC) siswa yang memiliki nilai $m$ terendah.
2. Sistem menyaring seluruh butir soal yang belum pernah dikerjakan oleh siswa pada KC tersebut.
3. Sistem menghitung $\hat{p}(q)$ untuk seluruh kandidat butir.
4. Butir soal yang dipilih wajib memenuhi kriteria batas ZPD:
   $$\hat{p}(q) \in [0.60, \ 0.85]$$
   *(Butir tidak terlalu mudah sehingga tidak memicu kebosanan, dan tidak terlalu sulit sehingga tidak memicu frustrasi).*
5. Jika tidak ada butir yang memenuhi interval ketat tersebut, toleransi diperlebar menjadi $[0.50, 0.90]$ dengan memilih butir terdekat ke titik ideal ZPD ($0.725$).

#### D. Protokol Kalibrasi Awal Cold-Start (Butir 1–6):
- Untuk butir 1 hingga 6, sistem menyajikan 6 butir acak seimbang: 2 butir $d_1$, 2 butir $d_2$, dan 2 butir $d_3$ yang mencakup spektrum 12 KCs.
- Seluruh 6 butir kalibrasi ditandai dengan flag `is_calibration = TRUE` pada database.
- Tombol petunjuk dinonaktifkan pada tahap kalibrasi untuk mengukur murni penguasaan awal (*prior knowledge*).
- Data kalibrasi ini dikecualikan dari perhitungan metrik akurasi prediksi adaptif E3.

#### E. Integritas Data Append-Only:
Tabel `interactions` dirancang secara *append-only*:
- Setiap jawaban siswa disisipkan sebagai baris baru (`INSERT`).
- Operasi `UPDATE` dan `DELETE` dilarang keras di tingkat model dan query database.
- Menjamin audit trail yang tak dapat dimanipulasi untuk sidang skripsi dan analisis penelitian ilmiah.
