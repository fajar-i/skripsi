# Rancang Bangun Arsitektur Tiga Lapis (RAG-KT) Multi-Provider dengan Pengujian Konkurensi dan Proteksi Zero-PII untuk Evaluasi Formatif Adaptif pada Sekolah Menengah Kejuruan

**Design, Concurrency Benchmarking, and Zero-PII Hardening of a Multi-Provider Three-Tier RAG-KT Architecture for Adaptive Formative Assessment in Vocational High Schools**

Fajari Arkan Fadhlurrahman¹*, [Nama Dosen Pembimbing 1]¹, [Nama Dosen Pembimbing 2]¹  
¹ Program Studi Pendidikan Ilmu Komputer, Fakultas Pendidikan Matematika dan Ilmu Pengetahuan Alam, Universitas Pendidikan Indonesia, Bandung, Indonesia  
* Penulis Korespondensi: [email@upi.edu]

---

## Abstrak

Evaluasi formatif adaptif pada Sekolah Menengah Kejuruan (SMK) menghadapi tantangan ganda: model *Deep Knowledge Tracing* (DKT) konvensional mensyaratkan korpus data interaksi masif yang tidak tersedia pada skala kelas (*small data regime*), sementara keterbatasan perangkat keras laboratorium dan risiko privasi data menghambat adopsi model bahasa komputasi awan secara langsung. Penelitian rekayasa sistem (*Design Science Research*) ini bertujuan merancang, menguji ketahanan konkurensi, serta memvalidasi keamanan arsitektur evaluasi formatif adaptif bernama **LogiTrace**. Sistem dibangun melalui arsitektur tiga lapis: Lapisan 1 (*Basis Pengetahuan*) memformalisasi 12 *Knowledge Components* (KC) Kurikulum Merdeka Fase F Teknik Komputer dan Jaringan beserta Graf Dependensi Prasyarat (DAG) dan 5 dimensi *Test of Logical Thinking* (TOLT); Lapisan 2 (*Indeks Semantik*) mengelola 180 butir soal dua tingkat (*two-tier*) berbasis `pgvector`; dan Lapisan 3 (*Runtime Deterministik & Orkestrasi Tri-Agen RAG*) mengeksekusi estimasi penguasaan kognitif secara instan tanpa pelatihan jaringan saraf tiruan, dipadukan dengan klien inferensi multi-provider (`SecureLLMClient`) yang mendukung proxy lokal `9router` (`ag/gemini-3.8-flash`), API awan berlatensi rendah (`DeepSeek-V3`, `Groq Llama-3.1`), serta mesin CPU lokal (`Ollama Qwen2.5-3B-Instruct-Q4_K_M`) berpelindung keamanan lima lapis (*Defense-in-Depth*). Pengujian laboratorium (*in-silico benchmarking*) membuktikan bahwa mesin deterministik L3 mengeksekusi pembaruan kognitif dan seleksi butir ZPD dalam rerata 0,18 ms ($p95 = 0{,}42$ ms). Uji beban konkurensi pada CPU 8-thread lokal membuktikan operasi optimal pada $k = 1$ klien (rerata 1,74 s, $p95 = 2{,}13$ s, kelolosan SLA 100%) dan $k = 2$ klien (rerata 2,64 s, $p95 = 3{,}06$ s, kelolosan 83,3%). Pada lonjakan beban $k \ge 4$ klien maupun gangguan jaringan, mekanisme *timeout* 3,0 detik secara otomatis mengalihkan respons ke bank petunjuk statis terkurasi (< 50 ms) dengan tingkat kegagalan layanan nol (*zero service outage*). Verifikasi 41 skenario pengujian unit otomatis (`pytest`) dan pengujian antarmuka menyeluruh (*end-to-end*) berbasis Playwright mengonfirmasi bahwa modul *Pre-Flight Zero-PII Sanitizer*, *Token Masking*, dan *Answer Leakage Guard* berhasil menyaring 100% identitas pribadi siswa serta mencegah kebocoran kunci jawaban, sementara antarmuka adaptif siswa dan dasbor guru beroperasi mulus tanpa regresi visual. Hasil ini membuktikan bahwa arsitektur LogiTrace layak secara komputasi, tangguh terhadap konkurensi, patuh privasi, dan siap diimplementasikan pada pembelajaran *Station Rotation*.

**Kata Kunci:** *evaluasi formatif adaptif; knowledge tracing; retrieval-augmented generation; multi-provider llm; benchmark konkurensi; zero-pii; sekolah menengah kejuruan*

---

## Abstract

Adaptive formative assessment in vocational high schools faces a dual challenge: conventional Deep Knowledge Tracing (DKT) models require massive interaction logs unavailable in classroom-scale environments (the small data regime), while laboratory hardware constraints and data privacy risks hinder unmediated cloud language model deployments. This Design Science Research study designs, stress-tests, and validates a three-tier adaptive assessment architecture named LogiTrace. The system decouples computational responsibilities into three distinct layers: Layer 1 (Knowledge Base) formalizes 12 Knowledge Components (KCs) from the Indonesian Merdeka Curriculum for computer networking, mapped to a Prerequisite Directed Acyclic Graph (DAG) and five Test of Logical Thinking (TOLT) dimensions; Layer 2 (Semantic Index) indexes 180 two-tier items via pgvector cosine similarity; and Layer 3 (Deterministic Runtime & Tri-Agent RAG Orchestration) calculates cognitive mastery deterministically without neural network training, coupled with a multi-provider inference client (`SecureLLMClient`) supporting a local OpenAI-compatible proxy (`9router` running `ag/gemini-3.8-flash`), low-latency cloud APIs (`DeepSeek-V3`, `Groq Llama-3.1`), and a local CPU engine (`Ollama Qwen2.5-3B-Instruct-Q4_K_M`) fortified by a five-layer defense-in-depth security scheme. In-silico technical benchmarking reveals that the Layer 3 rule engine executes cognitive state updates and ZPD item selection in an average of 0.18 ms ($p95 = 0.42$ ms). Empirical multi-user concurrency testing on an 8-thread CPU confirms robust local operation at $k = 1$ client (mean 1.74 s, $p95 = 2.13$ s, 100% SLA pass rate) and $k = 2$ clients (mean 2.64 s, $p95 = 3.06$ s, 83.3% pass rate). Under concurrent bursts ($k \ge 4$ clients) or network disruptions, the 3.0-second timeout guard seamlessly diverts requests to a curated static hint repository (< 50 ms), maintaining zero service outages. Automated verification across 41 unit test scenarios (`pytest`) and Playwright end-to-end interface testing confirms 100% effectiveness in pre-flight Zero-PII redaction, credential masking, and answer leakage prevention, alongside responsive, regression-free UI workflows across mobile and desktop viewports. These findings establish that LogiTrace is computationally viable, concurrency-resilient, privacy-preserving, and ready for field trials in Station Rotation classrooms.

**Keywords:** *adaptive formative assessment; knowledge tracing; retrieval-augmented generation; multi-provider llm; concurrency benchmarking; zero-pii; vocational high school*

---

## 1. Pendahuluan

Evaluasi formatif adaptif memegang peranan krusial dalam memfasilitasi pembelajaran tuntas (*mastery learning*), khususnya pada pendidikan kejuruan rumpun Teknik Komputer dan Jaringan (TKJ). Pada materi konfigurasi dan penelusuran kesalahan (*troubleshooting*) jaringan kabel dan nirkabel Kurikulum Merdeka Fase F, peserta didik tidak hanya dituntut menguasai prosedur sintaks mekanis, melainkan wajib membangun penalaran logis formal untuk menghubungkan parameter konfigurasi (seperti pengalamatan IP, interferensi kanal frekuensi, dan tabel *routing*) dengan gejala konektivitas sistem (Tobin & Capie, 1981; Wing, 2006). Kendati demikian, pembelajaran di laboratorium SMK di Indonesia masih menghadapi hambatan ganda: keterbatasan rasio perangkat keras laboratorium (rata-rata 1 komputer untuk 2 siswa) serta instrumen evaluasi formatif konvensional yang bersifat statis, tidak adaptif, dan lambat dalam mendiagnosis miskonsepsi penalaran teknis peserta didik (Komalasari et al., 2023; Nurbaeti et al., 2024).

Dalam ranah sistem pembelajaran adaptif dan tutor cerdas (*Intelligent Tutoring Systems* / ITS), pemodelan pelacakan pengetahuan (*Knowledge Tracing* / KT) telah lama dimanfaatkan untuk memprakirakan status penguasaan konsep pembelajar berdasarkan riwayat interaksinya (Corbett & Anderson, 1995; Shen et al., 2024). Munculnya *Deep Knowledge Tracing* (DKT) berbasis jaringan saraf berulang (Piech et al., 2015) beserta arsitektur atensi dan transformernya memang menghasilkan akurasi prediksi yang tinggi pada repositori data masif seperti ASSISTments dan EdNet (Abdelrahman et al., 2023; Huang et al., 2024). Namun demikian, DKT konvensional mensyaratkan korpus interaksi masif ($\ge 100.000$ baris data) yang mustahil tersedia pada skala satu rombongan belajar SMK yang hanya beranggotakan 30 hingga 36 siswa (*small data regime*), serta mengalami kegagalan inferensi parah pada kondisi data awal kosong (*cold-start*) (Jung et al., 2025; Nkambou et al., 2023). Selain itu, sifat kotak hitam (*black-box*) pada model neural menyulitkan guru untuk mengaudit secara transparan alasan di balik rekomendasi kognitif yang diberikan sistem.

Sebaliknya, literatur psikometri komputasional telah lama membuktikan bahwa pada data terbatas, model psikometri klasik terstruktur seperti *Bayesian Knowledge Tracing* (BKT) dengan parameter apriori (Corbett & Anderson, 1995) maupun sistem rating dinamis berbasis Teori Respons Butir (*Item Response Theory* / IRT) seperti *Elo Rating System* (Pelánek, 2016) mampu memberikan estimasi kemampuan yang stabil tanpa memerlukan komputasi gradien yang intensif. Temuan mutakhir (Nkambou et al., 2023; Tato & Nkambou, 2022) menegaskan bahwa penggabungan struktur pakar (seperti graf dependensi kurikulum dan pemodelan relasi prasyarat) jauh lebih efektif dalam melacak penalaran inferensial dibandingkan melatih jaringan neural dari nol pada sampel kecil. Pendekatan berbasis Graf Asiklik Terarah (*Directed Acyclic Graph* / DAG) terbukti memberikan batas kognitif yang kokoh (*guardrailed boundaries*) agar pembelajar tidak melompat ke konsep rumit sebelum konsep fondasi dikuasai secara tuntas (Jadhav et al., 2023; Xia et al., 2026).

Di sisi lain, integrasi Model Bahasa Skala Besar (*Large Language Models* / LLM) membuka era baru dalam penyusunan perancah Sokratik (*Socratic scaffolding*) yang memandu pemecahan masalah tanpa membocorkan kunci jawaban secara langsung (*guiding, not solving*) (Wang et al., 2026; Zhao et al., 2026). Namun, implementasi tutor LLM di lingkungan sekolah kejuruan Indonesia menghadapkan pengembang pada dilema infrastruktur dan regulasi privasi. Ketergantungan tunggal pada *cloud API* komersial tanpa pelindung rentan terhadap fluktuasi koneksi internet laboratorium serta berisiko melanggar Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP) apabila identitas siswa (seperti NISN, nama lengkap, atau profil sekolah) ikut terkirim dalam *payload* permintaan teks ke peladen eksternal. Sebaliknya, menjalankan model bahasa secara murni pada CPU lokal sekolah (misalnya via Ollama tanpa akselerator GPU diskret) memberikan kedaulatan penuh secara luring (*air-gapped*), namun membutuhkan alokasi memori RAM besar (~4,5 GB) dan rentan mengalami saturasi antrean komputasi CPU ketika beberapa siswa meminta petunjuk secara serentak (*concurrent burst*).

Menjawab kesenjangan metodologis dan komputasi tersebut, penelitian ini bertujuan merancang, menguji ketahanan konkurensi, serta memvalidasi keamanan arsitektur sistem evaluasi formatif adaptif bernama **LogiTrace**. Berbeda dari penelitian DKT konvensional maupun tutor LLM berkanal tunggal, penelitian ini mengajukan tiga kontribusi rekayasa utama:
1. **Mesin Kognitif Deterministik Bebas-Pelatihan (< 1 ms):** Mengintegrasikan estimasi probabilitas logistik 1-parameter, pembaruan penguasaan asimetris berbobot bantuan ($h$), seleksi butir Zona Perkembangan Proksimal (ZPD), serta prasyarat DAG pada 12 KC jaringan komputer yang dipetakan ke 5 dimensi penalaran formal TOLT;
2. **Orkestrasi Tri-Agen RAG & Klien Multi-Provider (`SecureLLMClient`):** Mengelola tiga agen fungsional—Agen T1 (*Semantic Item Labeler*), Agen T2 (*3-Level Socratic Hint Scaffolding*), dan Agen T3 (*Session Narrative Reflection & Bipartite Peer-Tutoring*)—yang dapat beralih secara mulus antara proxy lokal `9router`, API awan hemat biaya (`DeepSeek`/`Groq`), dan mesin CPU lokal (`Ollama`);
3. **Pertahanan Keamanan Lima Lapis (*Defense-in-Depth*) & Proteksi *Zero-PII*:** Menjamin sanitasi identitas pribadi pra-transmisi (`PIIScrubber`), penyensoran kredensial (`mask_secret`), pembatasan waktu tunggu ketat 3,0 detik, pencegahan kebocoran kunci jawaban berbasis ekspresi reguler (`AnswerLeakageGuard`), serta pengalihan instan (< 50 ms) ke bank petunjuk statis terkurasi.

---

## 2. Metode Penelitian

### 2.1 Metodologi Design Science Research (DSR) & Arsitektur Tiga Lapis

Pengembangan sistem LogiTrace mengadopsi metodologi *Design Science Research* (DSR) dalam sistem informasi (Peffers et al., 2007) yang dilaksanakan melalui lima tahapan sistematis: (1) *Identifikasi Masalah & Motivasi* (keterbatasan data kelas kecil SMK, kendala perangkat keras rasio 1:2, dan risiko privasi UU PDP); (2) *Definisi Tujuan Solusi* (target latensi mesin kognitif $< 1\text{ ms}$, batas waktu layanan perancah Sokratik $\le 3{,}0\text{ detik}$, dan 0% kebocoran PII/kunci jawaban); (3) *Perancangan & Pengembangan Artefak* (arsitektur tiga lapis L1–L3 dan modul `SecureLLMClient`); (4) *Demonstrasi Teknis* (simulasi numerik parameter kognitif dan integrasi orkestrasi Tri-Agen); serta (5) *Evaluasi* (uji beban konkurensi CPU $k \in \{1, 2, 4, 8\}$, verifikasi 41 skenario pengujian unit otomatis, serta pengujian antarmuka pengguna menyeluruh *end-to-end* berbasis Playwright).

Secara struktural, artefak perangkat lunak LogiTrace memisahkan tanggung jawab komputasi ke dalam tiga lapisan fungsional (*separation of concerns*) sebagaimana diilustrasikan pada Gambar 1.

```text
┌─────────────────────────────────────────────────────────────────────────────────┐
│                       LAPISAN 1: BASIS PENGETAHUAN (L1)                         │
│  ┌─────────────────────────┐  ┌───────────────────────┐  ┌───────────────────┐  │
│  │ 12 Knowledge Components │  │ Prerequisite Directed │  │ 5 Dimensi TOLT    │  │
│  │ (Kurikulum Fase F TKJ)  │  │ Acyclic Graph (DAG)   │  │ Penalaran Jaringan│  │
│  └─────────────────────────┘  └───────────────────────┘  └───────────────────┘  │
└────────────────────────────────────────┬────────────────────────────────────────┘
                                         │
┌────────────────────────────────────────▼────────────────────────────────────────┐
│                     LAPISAN 2: INDEKS BUTIR SEMANTIK (L2)                       │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │ Bank Soal Dua Tingkat (180 Butir Terkurasi) + pgvector Cosine Similarity  │  │
│  │ Agen T1 (Semantic Item Labeler): Klasifikasi KC, TOLT, & Kesulitan (d)    │  │
│  └───────────────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────┬────────────────────────────────────────┘
                                         │
┌────────────────────────────────────────▼────────────────────────────────────────┐
│          LAPISAN 3: RUNTIME DETERMINISTIK (L3) & ORKESTRASI TRI-AGEN RAG        │
│  ┌───────────────────────────────┐     ┌─────────────────────────────────────┐  │
│  │ Mesin Inferensi Kognitif      │     │ SecureLLMClient (Multi-Provider)    │  │
│  │ • Kalibrasi Cold-Start (m0)   │     │ • Agen T2: Socratic Hint (Level 1-3)│  │
│  │ • Estimasi Peluang p_hat      │     │ • Agen T3: Refleksi & Peer-Tutoring │  │
│  │ • Pembaruan Mastery (m) & ZPD │     │ • Pre-Flight Zero-PII & Masking     │  │
│  │ • Dasbor Ambient Guru (Top-3) │     │ • 9router / DeepSeek / Groq / Ollama│  │
│  │ • Peluruhan Ebbinghaus (tau)  │     │ • Leakage Guard & Fallback < 50 ms  │  │
│  └───────────────────────────────┘     └─────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────┘
```
*Gambar 1. Diagram arsitektur tiga lapis sistem LogiTrace dengan orkestrasi Tri-Agen dan pengaman Defense-in-Depth.*

1. **Lapisan 1 (L1 - Basis Pengetahuan):** Memuat ontologi kurikulum formal berupa 12 Komponen Pengetahuan (*Knowledge Components* / KC) materi Teknologi Jaringan Kabel dan Nirkabel (Fase F TKJ), Graf Dependensi Prasyarat (DAG), dan 5 dimensi operasionalisasi *Test of Logical Thinking* (TOLT).
2. **Lapisan 2 (L2 - Indeks Butir Semantik & Agen T1):** Mengelola repositori 180 butir soal pilihan ganda beralasan dua tingkat (*two-tier diagnostic items*) beserta representasi vektor semantik melalui PostgreSQL `pgvector` dan layanan kurasi otomatis **Agen T1 (`LabelingService`)**.
3. **Lapisan 3 (L3 - Runtime Deterministik & Orkestrasi Agen T2/T3):** Menggabungkan mesin pembaruan status kognitif matematis instan (< 1 ms), penyeleksi butir ZPD, telemetri dasbor guru berbasis WebSocket, serta orkestrasi **Agen T2 (`HintService`)** dan **Agen T3 (`SummaryService`)** yang dilindungi oleh modul keamanan lima lapis `SecureLLMClient`.

---

### 2.2 Formalisasi 12 KC, Relasi DAG, dan Justifikasi Dimensi TOLT (L1)

Capaian Pembelajaran (CP) Elemen 2 Fase F TKJ (Tujuan Pembelajaran TP 2.1 & TP 2.2) didekomposisi secara granular ke dalam 12 KC. Berbeda dari kategorisasi subjektif, pemetaan setiap KC ke dalam lima dimensi penalaran formal *Test of Logical Thinking* (TOLT) mengacu pada kerangka operasionalisasi penalaran ilmiah Tobin & Capie (1981), sebagaimana dijabarkan pada Tabel 1.

*Tabel 1. Taksonomi 12 Knowledge Components (KC), relasi prasyarat DAG, dan justifikasi dimensi TOLT.*

| Kode KC | Nama Komponen Pengetahuan | Konsep & Tugas Kognitif Jaringan | Dimensi TOLT | Justifikasi Teoretis Operasional (Tobin & Capie, 1981) |
|:---|:---|:---|:---|:---|
| `KC-01` | `WLAN_STANDARDS` | Karakteristik IEEE 802.11 b/g/n/ac/ax, frekuensi (2,4 vs 5 GHz), dan modulasi sinyal. | *Correlational* | Menganalisis korelasi terbalik antara frekuensi gelombang dengan daya tembus material fisik (*path loss*). |
| `KC-02` | `WLAN_TOPOLOGY_BSS` | Mode Ad-Hoc (IBSS), Infrastructure (BSS/ESS), dan fungsi Distribution System. | *Combinatorial* | Mengkombinasikan berbagai simpul klien dan titik akses untuk membentuk cakupan jaringan terintegrasi. |
| `KC-03` | `IP_PEER_CONFIG` | Pengalamatan IPv4 statis, subnet mask (/24 s.d. /30), dan penentuan Network/Host ID. | *Controlling Variables* | Mengisolasi variabel alamat host pada segmen subnet yang sama untuk memastikan komunikasi peer-to-peer berhasil. |
| `KC-04` | `WLAN_FREQ_CHANNEL` | Alokasi kanal non-overlapping (1, 6, 11) dan mitigasi interferensi kanal bersama (*co-channel*). | *Combinatorial* | Menentukan permutasi alokasi kanal optimal tanpa tumpang-tindih pada denah multi-AP berdekatan. |
| `KC-05` | `WLAN_SECURITY_AUTH` | Enkripsi identitas WPA2-PSK (AES) vs WPA3-SAE dan kelemahan protokol jabat tangan WEP. | *Correlational* | Mengkorelasikan jenis protokol autentikasi dengan kerentanan serangan penangkapan paket (*handshake capture*). |
| `KC-06` | `WLAN_HOST_HARDENING` | Pengamanan klien melalui penyaringan alamat fisik (*MAC Filtering*) dan dinding api AP. | *Controlling Variables* | Menjaga variabel hak akses konstan dengan hanya memanipulasi parameter daftar izin alamat fisik (*whitelist*). |
| `KC-07` | `WLAN_SIGNAL_PROP` | Pelemahan propagasi radio, redaman dinding beton/kaca, dan batas ambang RSSI (-dBm). | *Probabilistic* | Mengestimasi probabilitas fluktuasi penurunan laju data (*throughput drop*) akibat redaman dinamis material. |
| `KC-08` | `WLAN_ROAMING_PROB` | Ambang batas perpindahan sinyal klien (*roaming threshold*) dan histeresis penguat sinyal. | *Probabilistic* | Menghitung peluang keputusan perpindahan asosiasi BSS klien berdasarkan fluktuasi margin deviasi RSSI. |
| `KC-09` | `WLAN_CHANNEL_COLLISION` | Tabrakan domain paket, *hidden node problem*, dan mekanisme koordinasi CSMA/CA. | *Proportional* | Menghitung rasio proporsi penundaan transmisi (*backoff time*) terhadap peningkatan volume kepadatan trafik paket. |
| `KC-10` | `ICMP_CONNECTIVITY` | Pengujian ketercapaian host melalui protokol ICMP (`ping`) dan evaluasi *Round-Trip Time* (RTT). | *Controlling Variables* | Mengontrol parameter ukuran paket (*packet size*) dan TTL untuk mengisolasi latensi fisik media transmisi. |
| `KC-11` | `ICMP_TROUBLE_DHU` | Diagnosis galat *Destination Host Unreachable* (DHU) akibat kesalahan *gateway*, ARP, atau rute. | *Correlational* | Menghubungkan gejala pesan galat layer 3 dengan korelasi ketiadaan entri tabel rute pengalihan paket. |
| `KC-12` | `ICMP_TROUBLE_RTO` | Pelacakan galat *Request Timed Out* (RTO) akibat blokade *firewall*, putus kabel, atau redaman. | *Correlational* | Mengkorelasikan ketiadaan paket balasan (*echo reply*) dengan keberadaan aturan pemfilteran paket masuk. |

Ketergantungan kurikuler antar-KC diformalkan ke dalam Graf Asiklik Terarah (*Directed Acyclic Graph* / DAG) $G = (V, E)$ (Gambar 2). Aturan pembatasan prasyarat (*prerequisite gating*) menetapkan bahwa butir soal pada simpul anak (*child KC*) hanya dapat disajikan apabila seluruh simpul induk langsungnya (*direct parents*) telah mencapai ambang ketuntasan prasyarat $m \ge 0{,}60$, sedangkan kemahiran mandiri penuh (*mastered* untuk kandidat tutor sebaya) ditetapkan pada $m \ge 0{,}70$ (Xia et al., 2026).

```text
[KC-01: WLAN_STANDARDS] ──────► [KC-04: WLAN_FREQ_CHANNEL] ──────► [KC-09: WLAN_CHANNEL_COLLISION]
          │                                  │
          ▼                                  ▼
[KC-02: WLAN_TOPOLOGY_BSS] ───► [KC-07: WLAN_SIGNAL_PROP] ───────► [KC-08: WLAN_ROAMING_PROB]
          │                                  │
          ▼                                  ▼
[KC-03: IP_PEER_CONFIG] ──────► [KC-10: ICMP_CONNECTIVITY] ───┬──► [KC-11: ICMP_TROUBLE_DHU]
          │                                                    └──► [KC-12: ICMP_TROUBLE_RTO]
          ▼                                                                 ▲
[KC-05: WLAN_SECURITY_AUTH] ──► [KC-06: WLAN_HOST_HARDENING] ───────────────┘
```
*Gambar 2. Graf Dependensi Prasyarat (Prerequisite DAG) 12 Knowledge Components.*

---

### 2.3 Formulasi Matematika Mesin Deterministik (L3)

Mengatasi kelemahan DKT yang membutuhkan data masif (Piech et al., 2015), mesin L3 LogiTrace (`cognitive.py` & `calibration.py`) menggunakan persamaan deterministik berbasis fungsi logistik 1-parameter dan aturan pembaruan penguasaan adaptif. Status penguasaan kognitif siswa $s$ pada komponen $k$ direpresentasikan sebagai nilai kontinu $m_{s,k} \in [0{,}02;\ 0{,}98]$. Untuk mengatasi masalah *cold-start* pada awal sesi, seluruh KC diinisialisasi pada nilai apriori $m_0 = 0{,}25$, diikuti oleh 6 butir soal kalibrasi terstandar (`is_calibration = TRUE`) pada simpul akar sebelum memasuki fase seleksi adaptif ZPD (butir ke-7 s.d. ke-20).

#### 1. Estimasi Probabilitas Respons Benar ($\hat{p}$)
Peluang seorang siswa dengan penguasaan $m_{s,k_q}$ menjawab benar butir soal $q$ dengan tingkat kesulitan apriori $d_q \in \{1, 2, 3\}$ dirumuskan melalui fungsi logistik:

$$\hat{p}(q) = \sigma\big(\mathrm{logit}(m_{s, k_q}) + \theta_{d_q}\big) = \frac{1}{1 + \exp\left(-\left(\ln\left(\frac{m_{s,k_q}}{1 - m_{s,k_q}}\right) + \theta_{d_q}\right)\right)}$$

dengan parameter offset kesulitan: $\theta_1 = +0{,}90$ (mudah), $\theta_2 = 0{,}00$ (sedang), dan $\theta_3 = -0{,}90$ (sulit).

#### 2. Aturan Pembaruan Status Penguasaan ($m$) dan Peluruhan Memori
Pada instrumen pilihan ganda beralasan dua tingkat (*two-tier*), respons siswa dikodekan secara ketat sebagai $r = 1$ apabila jawaban teknis (Tingkat 1) dan alasan penalaran logis (Tingkat 2) keduanya benar, atau $r = 0$ jika salah satu tingkat keliru. Pembaruan status kognitif pasca-respons dihitung secara seketika (< 1 ms):

$$m_{t} \leftarrow \begin{cases} 
m_{t-1} + \alpha_d (1 - m_{t-1}) h, & \text{jika respons benar } (r = 1) \\ 
m_{t-1} - \gamma_d m_{t-1}, & \text{jika respons salah } (r = 0) 
\end{cases}$$

dengan laju penyesuaian adaptif berbobot tingkat kesulitan:

$$\alpha_d = \alpha_0 \big(1 + \beta(d - 1)\big), \qquad \gamma_d = \gamma_0 \big(1 + \beta(3 - d)\big)$$

Konstanta dasar ditetapkan sebesar $\alpha_0 = 0{,}30$, $\gamma_0 = 0{,}25$, dan faktor penskalaan kesulitan $\beta = 0{,}40$. Faktor bobot kemandirian bernilai $h = 1{,}0$ jika siswa menjawab benar secara mandiri, dan dikenai faktor diskon $h = 0{,}5$ jika jawaban benar dicapai setelah membuka petunjuk Sokratik. Nilai $m$ dipotong secara ketat (*clipped*) pada batas $[0{,}02;\ 0{,}98]$ guna mencegah singularitas pembagian nol pada fungsi logit. Selain itu, untuk sesi lintas-minggu, diterapkan peluruhan retensi memori Ebbinghaus saat pembacaan status (*on-read decay*): $m_k(t) = m_k(t_{\text{last}}) \cdot \exp(-\Delta t_{\text{hari}} / \tau_k)$ dengan konstanta waktu $\tau_k = 60\text{ hari}$.

#### 3. Seleksi Butir Adaptif pada Zona Perkembangan Proksimal (ZPD)
Algoritma penyeleksi (`zpd_selector.py`) memilih soal berikutnya $q^*$ yang meminimalkan fungsi penalti deviasi terhadap sasaran probabilitas ideal $\hat{p}_{\text{target}} = 0{,}72$:

$$q^* = \arg\min_{q \in Q_{\text{kandidat}}} \left( |\hat{p}(q) - 0{,}72| - 0{,}05 \cdot \mathbb{I}_{\text{KC baru}}(q) + 0{,}10 \cdot \mathbb{I}_{\text{KC berurutan}}(q) \right)$$

dengan syarat: butir belum dikerjakan pada sesi bersangkutan, berada dalam pita ZPD $0{,}60 \le \hat{p}(q) \le 0{,}85$, dan seluruh simpul prasyarat langsung pada DAG telah mencapai $m \ge 0{,}60$.

---

### 2.4 Orkestrasi Tri-Agen RAG, Arsitektur Multi-Provider `9router`, & Pertahanan *Zero-PII*

Berbeda dari integrasi LLM naif yang hanya memanggil satu jenis model secara langsung, LogiTrace mengimplementasikan pola **Orkestrasi Tri-Agen (*Tri-Agent Specialization*)** yang beroperasi di atas klien komunikasi terproteksi `SecureLLMClient` (`secure_client.py`):
1. **Agen T1 (`LabelingService` — Kurasi Bank Soal Pra-Pembelajaran):** Mengevaluasi teks butir soal baru secara leksikal-semantik terhadap kata kunci 12 KC dan indikator 5 dimensi TOLT, mengestimasi tingkat kesulitan nominal ($d \in \{1, 2, 3\}$), serta menghitung skor keyakinan (*confidence score*). Butir dengan tingkat keyakinan $< 0{,}60$ secara otomatis ditahan pada *Teacher Review Queue* untuk diverifikasi oleh guru manusia (*human-in-the-loop*).
2. **Agen T2 (`HintService` — Perancah Sokratik 3-Tingkat Waktu-Nyata):** Ketika siswa mengalami kesulitan pada fase adaptif di Zona B, Agen T2 menyusun petunjuk Sokratik berjenjang (*Level 1: Directing Attention* / mengarahkan perhatian ke parameter kunci; *Level 2: Intermediate Step* / mengingatkan aturan atau rumus antara; *Level 3: Conceptual Framework* / memberikan kerangka penelusuran masalah) dengan batasan ketat $\le 60\text{ kata}$ (`max_tokens = 120`, `temperature = 0.0`).
3. **Agen T3 (`SummaryService` — Refleksi Naratif Sesi & Matriks *Peer-Tutoring*):** Pada fase penutup pembelajaran (menit ke-80), Agen T3 mengagregasi capaian 34 siswa pada 12 KC, memasangkan siswa kemahiran tinggi (**Tutor Sebaya**, $m \ge 0{,}65\text{--}0{,}70$) dengan maksimal 2 rekan yang mengalami kesulitan (**Mentee**, $m \le 0{,}40\text{--}0{,}45$) melalui algoritma *Bipartite Matching* berpelindung *anti-self-pairing*, serta menyintesis narasi evaluasi kelas 3 paragraf untuk ditampilkan di proyektor kelas.

Guna menjamin fleksibilitas operasional di berbagai kondisi infrastruktur sekolah sekaligus mematuhi UU PDP, `SecureLLMClient` mendukung **empat mode penyedia inferensi (*Multi-Provider Backend*)** yang dikawal oleh lima lapisan keamanan (*Defense-in-Depth*) (Gambar 3).

```mermaid
flowchart TD
    subgraph EdgeLayer ["1. Perangkat Siswa / Guru & Backend FastAPI Lokal"]
        REQ["Pemicu Agen T2 (Petunjuk Sokratik Level 1-3)<br/>atau Agen T3 (Refleksi Sesi Kelas)"] --> SCRUB["Layer 1: Pre-Flight Zero-PII Sanitizer (PIIScrubber)<br/>(Sensor NISN, NIK, No HP, Email, ID S01, & Nama Sekolah)"]
        SCRUB --> MASK["Layer 2: Credential Masking & Transport Security<br/>(Masking sk-****cdef, stream=False, & TLS Verification)"]
    end

    subgraph MultiProvider ["2. Multi-Backend Inference Router (SecureLLMClient - SLA 3,0s)"]
        MASK --> ROUTER{"Pilih Mode Provider<br/>(.env Auto-Detect)"}
        ROUTER -- "Mode 1 (Default Proxy)" --> NINEROUTER["9router Local Proxy<br/>(localhost:20128 | ag/gemini-3.8-flash)"]
        ROUTER -- "Mode 2 (Direct Cloud)" --> CLOUD["Cloud Inference API<br/>(DeepSeek-V3 / Groq Llama-3.1)"]
        ROUTER -- "Mode 3 (100% Offline CPU)" --> OLLAMA["Ollama Local CPU Engine<br/>(Qwen2.5-3B-Instruct Q4_K_M | k <= 2)"]
    end

    subgraph PostFlight ["3. Guardrail Pasca-Inferensi & Graceful Fallback"]
        NINEROUTER --> GUARD{"Layer 3 & 4: Latensi <= 3,0s &<br/>Lolos AnswerLeakageGuard?"}
        CLOUD --> GUARD
        OLLAMA --> GUARD
        GUARD -- "Lolos (<= 60 Kata & Zero Leakage)" --> XSS["Layer 4b: Anti-XSS Sanitizer<br/>(Strip Code Fences & html.escape)"]
        GUARD -- "Timeout > 3,0s / HTTP 429 / Bocor" --> FALLBACK["Layer 5: Instant Deterministic Fallback (< 50 ms)<br/>(static_hints.json / Template Naratif T3)"]
    end

    XSS --> UI["Tampil di Smartphone Siswa / Dasbor Guru"]
    FALLBACK --> UI
```
*Gambar 3. Diagram alir arsitektur Multi-Provider SecureLLMClient dan lima lapisan pengamanan Defense-in-Depth.*

Lima lapisan pengamanan teknis yang diterapkan pada `secure_client.py` dan `guardrails.py` meliputi:
1. **Layer 1 (`PIIScrubber` — Pre-Flight Zero-PII Sanitizer):** Mengingat `SecureLLMClient` melayani baik permintaan petunjuk individu (Agen T2) maupun sintesis agregasi kelas yang memuat kode siswa dan identitas rombongan belajar (Agen T3), terdapat risiko terselipnya atribut identitas dalam *payload* teks sebelum dikirim ke proxy `9router` atau API awan. Modul `PIIScrubber` menerapkan ekspresi reguler berbatas kata (`\b`) untuk memindai dan menyensor: NISN 10-digit (`[REDACTED_NISN]`), NIK 16-digit (`[REDACTED_NIK]`), nomor telepon `+62`/`08xx` (`[REDACTED_PHONE]`), alamat email (`[REDACTED_EMAIL]`), kode identitas siswa seperti `Siswa S07` atau `S01` (`[REDACTED_STUDENT_ID]` / `[REDACTED_ID]`), serta nama institusi sekolah seperti `SMK Negeri 4 Bandung` (`[REDACTED_SCHOOL]`), ditambah pemotongan panjang *prompt* maksimal 1.000 karakter untuk menangkal *prompt bloat/injection*.
2. **Layer 2 (Credential Masking, Stream Control, & Transport Hardening):** Kredensial (`NINEROUTER_API_KEY`, `DEEPSEEK_API_KEY`, `GROQ_API_KEY`) diisolasi di sisi peladen (`.env`) dan disamarkan melalui fungsi `mask_secret()` menjadi format `sk-d****cdef` pada seluruh log sistem. Parameter `"stream": False` dipaksakan secara eksplisit pada *payload* JSON guna mencegah terpecahnya respons menjadi *Server-Sent Events* (SSE) pada proxy `9router`, disertai verifikasi sertifikat TLS (`verify=True`).
3. **Layer 3 (Strict SLA Timeout):** Batas waktu tunggu klien HTTP asinkron (`httpx.AsyncClient`) dikunci pada **3,0 detik** untuk Agen T2 (dan 5,0 detik untuk sintesis akhir sesi Agen T3) guna mencegah penumpukan antrean pada peramban siswa.
4. **Layer 4 (`AnswerLeakageGuard` & Anti-XSS Sanitizer):** Memeriksa apakah keluaran LLM mematuhi batas $\le 60\text{ kata}$, bebas dari frasa pembocor eksplisit (`"jawabannya adalah"`, `"pilihan yang benar"`, `"kunci jawaban"`), serta tidak mengandung pencocokan substring terhadap teks kunci jawaban benar maupun teks opsi pilihan ganda ($\ge 4\text{ karakter}$). Keluaran yang lolos dibersihkan dari pagar kode *markdown* (` ``` `) dan di-*escape* menggunakan `html.escape()` untuk mencegah injeksi *Cross-Site Scripting* (XSS).
5. **Layer 5 (Instant Graceful Fallback < 50 ms):** Apabila terjadi *timeout* $> 3{,}0\text{ detik}$, ketiadaan kunci API/koneksi luring, pembatasan kuota (`HTTP 429`), atau terdeteksi kebocoran jawaban, `HintService` dan `SummaryService` secara otomatis beralih ke repositori lokal terkurasi (`static_hints.json` yang memuat 36 petunjuk bertingkat Level 1–3 untuk 12 KC, atau templat refleksi deterministik T3) dalam waktu $< 50\text{ ms}$.

---

### 2.5 Protokol Pengujian Komputasi & Uji Beban Konkurensi (*In-Silico Setup*)

Evaluasi teknis prototipe dieksekusi pada peladen uji coba representatif laboratorium sekolah:
- **Spesifikasi Perangkat Keras Host:** Prosesor AMD Ryzen 7 5700U (8 Physical Cores, 16 Logical Threads @ 1,80 GHz base clock, up to 4,30 GHz boost), Memori RAM 16 GB DDR4, Penyimpanan NVMe SSD 512 GB, tanpa akselerator GPU diskret.
- **Lingkungan Perangkat Lunak:** Windows 11 / Linux WSL2, Python 3.13.14, FastAPI, SQLAlchemy Async, PostgreSQL 16 (`pgvector` pada korpus $N = 180$ butir soal dua tingkat), proxy lokal `9router` (`localhost:20128`, model `ag/gemini-3.8-flash`), serta Ollama (`localhost:11434`, model terkuantisasi 4-bit `Qwen2.5-3B-Instruct-Q4_K_M` dengan ukuran memori ~4,3 GB).
- **Prosedur Pengujian:**
  1. *Pengujian Deterministik L3:* 10.000 iterasi kalkulasi matematis $\hat{p}$, pembaruan penguasaan $m$, peluruhan memori Ebbinghaus, dan seleksi butir ZPD + verifikasi prasyarat DAG;
  2. *Uji Beban Konkurensi Multi-Klien pada CPU Lokal ($k \in \{1, 2, 4, 8\}$):* Skrip otomatis (`benchmark_concurrency_ollama.py`) mengeksekusi permintaan petunjuk Sokratik Agen T2 (`MAX_TOKENS = 150`, `temperature = 0.0`, `seed = 42`, panjang rata-rata *prompt* ~115 token dan keluaran ~45–55 token Bahasa Indonesia) secara simultan menggunakan `asyncio.gather` ($10\text{ permintaan}$ pada $k=1$; $6\times 2 = 12$ pada $k=2$; $4\times 4 = 16$ pada $k=4$; dan $2\times 8 = 16$ pada $k=8$) dengan perekaman telemetri perangkat keras (`psutil`) setiap 100 ms. Untuk memetakan kurva degradasi penuh perangkat keras CPU tanpa terpotong prematur, batas *timeout* soket pada skrip *benchmark* dibuka hingga 30,0 detik sementara status kelolosan SLA dievaluasi secara pasca-ukur terhadap ambang ketat $\le 3{,}0\text{ detik}$ (`passed_sla = lat <= 3.0`);
  3. *Uji Verifikasi Fungsional & Keamanan Terautomasi:* Eksekusi 41 skenario pengujian unit dan integrasi (`pytest` 9.2.0) pada 7 modul uji (`test_backend_api.py`, `test_calibration.py`, `test_cognitive_engine.py`, `test_guardrails.py`, `test_item_bank.py`, `test_secure_client.py`, dan `test_zpd_selector.py`);
  4. *Pengujian Antarmuka Pengguna Menyeluruh (End-to-End UI Testing):* Validasi alur pengguna dieksekusi secara terprogram menggunakan kerangka kerja otomasi peramban Playwright (Chromium) pada dua konfigurasi layar representatif: antarmuka bergerak siswa (viewport ponsel cerdas 390×844 px) dan antarmuka orkestrasi guru (layar desktop 1440×900 px). Pengujian memverifikasi 9 skenario alur kerja kritis: navigasi halaman landing (`01_landing.png`), otentikasi siswa (`02_student_login.png`), pemilihan ruang rotasi stasiun (`03_student_classroom.png`), interaksi butir kuis dua tingkat dengan perancah Sokratik Level 1 (`04_student_quiz.png`), umpan balik salah dan penjelasan konsep (`05_student_feedback_wrong.png`), umpan balik benar dan kenaikan penguasaan kognitif (`05b_student_feedback_correct.png`), layar selebrasi ketuntasan kuis (`06_student_celebration.png`), dasbor telemetri waktu-nyata guru (`07_teacher_dashboard.png`), modal ringkasan AI pasca-sesi Agen T3 (`08_teacher_summary_modal.png`), serta modal manajemen rotasi dan kurasi bank butir soal Agen T1 (`09_teacher_manage_modal.png`).

---

## 3. Hasil dan Pembahasan

### 3.1 Kinerja Komputasi Mesin Deterministik (L3)

Hasil pengujian membuktikan bahwa seluruh operasi kognitif deterministik pada Lapisan 3 bekerja dalam skala sub-milidetik, sebagaimana dirangkum pada Tabel 2.

*Tabel 2. Hasil benchmark latensi pemrosesan komponen deterministik dan fallback LogiTrace.*

| Komponen Arsitektur | Operasi Komputasi yang Diuji | Nilai Rerata (Mean) | Persentil ke-95 ($p95$) | Target Ambang Batas | Status Kinerja |
|:---|:---|:---:|:---:|:---:|:---:|
| **L3 Math Engine** | Kalkulasi $\hat{p}(q)$, aturan $m$, & peluruhan $\tau$ | $0{,}04$ ms | $0{,}09$ ms | $< 1{,}0$ ms | Memenuhi |
| **L3 ZPD Selector** | Evaluasi fungsi penalti ZPD + *gating* DAG (12 KC) | $0{,}18$ ms | $0{,}42$ ms | $< 10{,}0$ ms | Memenuhi |
| **L1/L2 Item Search** | Pencarian semantik 5 butir termirip ($N=180$ butir) | $4{,}20$ ms | $7{,}80$ ms | $< 50{,}0$ ms | Memenuhi |
| **T2 Static Fallback** | Pengalihan instan ke `static_hints.json` (12 KC $\times$ 3 Level) | $12{,}30$ ms | $18{,}50$ ms | $< 50{,}0$ ms | Memenuhi |
| **T3 Summary Fallback** | Sintesis naratif deterministik + *Bipartite Matching* | $6{,}40$ ms | $9{,}80$ ms | $< 10{,}0$ ms | Memenuhi |

Waktu eksekusi seleksi butir adaptif L3 yang hanya sebesar $0{,}18$ ms ($p95 = 0{,}42$ ms) menjamin bahwa perpindahan antar-soal pada antarmuka telepon pintar peserta didik berlangsung seketika tanpa beban tunda (*zero perceived latency*).

---

### 3.2 Analisis Sensitivitas Numerik Parameter L3

Untuk memvalidasi pemilihan konstanta laju dasar $\alpha_0 = 0{,}30$ (bersama $\gamma_0 = 0{,}25$ dan $\beta = 0{,}40$), dilakukan simulasi numerik menggunakan persamaan rekurensi eksak pada Subbab 2.3 terhadap siswa berkemampuan awal rendah ($m_0 = 0{,}25$) yang mengerjakan butir soal tingkat kesulitan sedang ($d = 2$, sehingga $\alpha_2 = \alpha_0(1 + 0{,}40(2-1)) = 1{,}4\alpha_0$) untuk mencapai ambang batas pembukaan prasyarat DAG ($m \ge 0{,}60$). Tabel 3 membandingkan lintasan konvergensi antara kondisi **berbantuan petunjuk Sokratik ($h = 0{,}5$, laju efektif $\alpha_2 h = 0{,}7\alpha_0$)** dan kondisi **mandiri tanpa bantuan ($h = 1{,}0$, laju efektif $\alpha_2 = 1{,}4\alpha_0$)**.

*Tabel 3. Analisis sensitivitas parameter laju penguasaan $\alpha_0$ terhadap konvergensi ketuntasan prasyarat ($m_0 = 0{,}25 \to m \ge 0{,}60$ pada $d=2, \beta=0{,}40$).*

| Nilai Laju $\alpha_0$ | Laju Efektif Berbantuan ($\alpha_2 h, h=0{,}5$) | Jumlah Butir Menuju $m \ge 0{,}60$ ($h=0{,}5$ Berbantuan) | Rerata $\Delta m$ per Butir ($h=0{,}5$) | Jumlah Butir Menuju $m \ge 0{,}60$ ($h=1{,}0$ Mandiri) | Karakteristik Perilaku Psikometrik | Status Pemilihan |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| **$0{,}10$** | $0{,}070$ | 9 butir ($m_9 = 0{,}610$) | $+0{,}040$ | 5 butir ($m_5 = 0{,}647$) | Terlalu lambat (*sluggish*); memicu kelelahan pengerjaan (*fatigue*). | Ditolak |
| **$0{,}20$** | $0{,}140$ | 5 butir ($m_5 = 0{,}647$) | $+0{,}079$ | 2 butir ($m_2 = 0{,}611$) | Lambat pada mode berbantuan; durasi per KC terlalu panjang. | Ditolak |
| **$0{,}30$** | **$0{,}210$** | **3 butir ($m_3 = 0{,}630$)** | **$+0{,}127$** | **2 butir ($m_2 = 0{,}748$)** | **Optimal: 2 butir jika mandiri penuh, 3 butir jika dibantu petunjuk.** | **Dipilih (Baseline)** |
| **$0{,}40$** | $0{,}280$ | 2 butir ($m_2 = 0{,}611$) | $+0{,}181$ | 2 butir ($m_2 = 0{,}855$) | Terlalu agresif; tidak membedakan jumlah butir mandiri vs. berbantuan. | Ditolak |
| **$0{,}50$** | $0{,}350$ | 2 butir ($m_2 = 0{,}683$) | $+0{,}217$ | 1 butir ($m_1 = 0{,}775$) | Tidak stabil; 1 tebakan beruntung langsung membuka simpul DAG. | Ditolak |

Hasil perhitungan eksak pada Tabel 3 memperlihatkan keunggulan struktural penetapan $\alpha_0 = 0{,}30$:
1. Siswa yang menjawab benar **secara mandiri ($h = 1{,}0, \alpha_2 = 0{,}42$)** membuktikan penguasaan dalam **2 butir soal** ($m_0 = 0{,}25 \to m_1 = 0{,}565 \to m_2 = 0{,}748$), sekaligus langsung melampaui ambang kandidat **Tutor Sebaya ($m \ge 0{,}70$)**;
2. Sebaliknya, siswa yang menjawab benar **dengan bantuan petunjuk Sokratik ($h = 0{,}5, \alpha_2 h = 0{,}21$)** memerlukan **3 butir soal** berturut-turut ($m_0 = 0{,}25 \to m_1 = 0{,}408 \to m_2 = 0{,}532 \to m_3 = 0{,}630 \ge 0{,}60$, dengan kenaikan rata-rata $\Delta m = +0{,}127\text{/butir}$) untuk membuka simpul prasyarat DAG berikutnya. Diferensiasi 2 butir (mandiri) versus 3 butir (berbantuan) ini tidak dapat dicapai pada $\alpha_0 = 0{,}40$ (keduanya selesai dalam 2 butir) maupun $\alpha_0 = 0{,}20$ (membutuhkan 5 butir saat berbantuan, yang akan menghabiskan kuota 14 soal adaptif hanya pada 2–3 KC).

---

### 3.3 Hasil Pengujian Beban Konkurensi CPU Multi-Pengguna & Analisis Trafik Kelas

Uji konkurensi empiris mode CPU lokal (`Ollama Qwen2.5-3B-Instruct-Q4_K_M`) pada prosesor AMD Ryzen 7 5700U menghasilkan profil kinerja yang dipaparkan pada Tabel 4 dan Tabel 5.

*Tabel 4. Profil latensi penyelesaian penuh dan keandalan SLA pemanggilan petunjuk Sokratik pada variasi konkurensi klien CPU lokal.*

| Beban Klien ($k$) | Total Uji ($N$) | Rerata Latensi Penuh (s) | Mediana Latensi (s) | Latensi $p95$ (s) | Lolos SLA ($\le 3{,}0$ s) (%) | Terpicu Fallback Statis (%) | Status Ketahanan Layanan |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **$k = 1$ klien** | 10 | $1{,}74 \pm 0{,}30$ | $1{,}73$ | **$2{,}13$** | **$100{,}0\%$** | $0{,}0\%$ | Stabil Sempurna |
| **$k = 2$ klien** | 12 | $2{,}64 \pm 0{,}26$ | $2{,}61$ | **$3{,}06$** | **$83{,}3\%$** | $16{,}7\%$ | Batas Kapasitas Optimal CPU |
| **$k = 4$ klien** | 16 | $4{,}74 \pm 0{,}64$ | $4{,}58$ | **$5{,}85$** | **$0{,}0\%$** | $100{,}0\%$ | Degradasi Anggun (*Fallback Active*) |
| **$k = 8$ klien** | 16 | $8{,}90 \pm 1{,}24$ | $9{,}18$ | **$10{,}16$** | **$0{,}0\%$** | $100{,}0\%$ | Degradasi Anggun (*Fallback Active*) |

*Tabel 5. Pemanfaatan sumber daya komputasi peladen CPU host selama pengujian beban.*

| Beban Klien ($k$) | Rerata Utilisasi CPU (%) | Puncak CPU (%) | RAM Awal (MB) | Puncak RAM (MB) | Selisih RAM (MB) | Implikasi Operasional Peladen |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **$k = 1$ klien** | $19{,}0\%$ | $79{,}0\%$ | $4.314{,}4$ | $4.341{,}9$ | $+27{,}5$ | Alokasi memori linear, laju ~28–32 token/detik, jauh di bawah SLA. |
| **$k = 2$ klien** | $27{,}1\%$ | $77{,}2\%$ | $4.308{,}5$ | $4.417{,}8$ | $+109{,}3$ | Throughput optimal CPU 8-core, pembagian lebar pita memori DDR4. |
| **$k = 4$ klien** | $24{,}7\%$ | $72{,}9\%$ | $4.339{,}1$ | $4.471{,}8$ | $+132{,}7$ | Kontensi antrean *thread*; di produksi langsung dipotong pada 3,0 s. |
| **$k = 8$ klien** | $28{,}4\%$ | $98{,}5\%$ | $4.460{,}7$ | $4.488{,}1$ | $+27{,}4$ | Saturasi *thread* 98,5%; aplikasi tetap responsif via *Static Fallback*. |

Data pada Tabel 4 dan Tabel 5 menunjukkan bahwa **kapasitas konkurensi optimal inferensi CPU lokal murni berada pada $k = 2$ klien simultan**. Ketika beban dinaikkan menjadi $k = 4$ dan $k = 8$ klien yang menembakkan permintaan pada milidetik yang sama, waktu penyelesaian penuh di sisi *worker* Ollama meningkat menjadi $4{,}74$ detik dan $8{,}90$ detik akibat pembagian siklus *thread* dan saturasi jalur memori DDR4. Namun, pada implementasi produksi `SecureLLMClient`, soket HTTP diputus secara tegas pada batas `timeout_seconds = 3.0` detik dan dialihkan ke `static_hints.json` dalam $12{,}30$ ms, sehingga siswa tidak pernah menunggu lebih dari 3,05 detik (*zero service outage*).

Lebih lanjut, jika dikaitkan dengan ekologi ruang kelas *Station Rotation* di mana **Zona B dihuni oleh 17 siswa serentak** (separuh dari 34 siswa satu kelas), kapasitas $k = 2$ pada jendela 3 detik sebenarnya telah mencukupi sebagian besar trafik alami kelas. Berdasarkan pemodelan kedatangan *Poisson*, dengan durasi pengerjaan 14 butir adaptif selama 15 menit (900 detik) dan asumsi setiap siswa membutuhkan bantuan Sokratik rata-rata pada 2 butir soal sulit, total permintaan dari 17 siswa adalah $17 \times 2 = 34\text{ permintaan}$ dalam 900 detik, atau laju kedatangan rata-rata $\lambda = 34 / 900 \approx 0{,}0378\text{ permintaan/detik}$. Dalam jendela layanan $\Delta t = 2{,}6\text{ detik}$, nilai harapan jumlah permintaan simultan hanyalah $\mu = \lambda \cdot \Delta t \approx 0{,}098$ klien, sehingga peluang terjadinya tumpukan $\ge 3$ permintaan secara bersamaan berdasarkan distribusi Poisson $P(X \ge 3) = 1 - \sum_{x=0}^{2} \frac{\mu^x e^{-\mu}}{x!}$ adalah **kurang dari $0{,}02\%$ ($< 0{,}0002$)**.

Selain itu, untuk laboratorium sekolah yang memiliki koneksi internet dan menginginkan beban RAM lokal mendekati nol (< 50 MB), dukungan multi-provider pada `SecureLLMClient` memungkinkan pengalihan ke proxy lokal `9router` maupun API awan (`DeepSeek-V3` / `Groq`), sebagaimana dirangkum pada Tabel 6.

*Tabel 6. Matriks perbandingan karakteristik operasional empat mode provider pada `SecureLLMClient`.*

| Mode Provider | Endpoint & Model Default | Latensi Tipikal | Jejak Memori RAM Host | Kebutuhan Konfigurasi & Biaya | Skenario Penggunaan Rekomendasi di SMK |
|:---|:---|:---:|:---:|:---|:---|
| **Mode 1: `9router` (Local Proxy)** | `localhost:20128/v1`<br/>(`ag/gemini-3.8-flash`) | $1{,}2\text{--}2{,}8$ s | Sangat Ringan ($< 50$ MB) | Proxy lokal dengan `stream=False`; tanpa beban GPU/CPU. | **Default Pengembangan & Uji Kelas Terkoneksi** pada laptop guru standar. |
| **Mode 2: `DeepSeek` (Cloud API)** | `api.deepseek.com`<br/>(`deepseek-chat`) | $0{,}6\text{--}0{,}9$ s | Nol di Host ($0$ MB) | API Key berbayar sangat hemat (~$\$0{,}14$/1M token). | **Produksi Kelas Skala Besar** dengan internet sekolah stabil. |
| **Mode 3: `Groq` (LPU Cloud)** | `api.groq.com/openai/v1`<br/>(`llama-3.1-8b-instant`) | $0{,}3\text{--}0{,}5$ s | Nol di Host ($0$ MB) | Tersedia *Free Tier* berkecepatan ultra-tinggi. | **Uji Responsivitas Instan** (< 0,5 s) pada jaringan terkoneksi. |
| **Mode 4: `Ollama` (Local CPU)** | `localhost:11434/api`<br/>(`Qwen2.5-3B-Q4_K_M`) | $1{,}7\text{--}2{,}6$ s ($k \le 2$) | Berat (~$4{,}3\text{--}4{,}5$ GB) | 100% Gratis & Mandiri tanpa koneksi internet. | **Mode Luring Penuh (*Air-Gapped*)** saat internet laboratorium mati. |

---

### 3.4 Evaluasi Kualitas Pedagogis Petunjuk Sokratik & Keamanan *Zero-PII* (41/41 Unit Tests)

Menjawab pertanyaan krusial mengenai kualitas pedagogis keluaran model bahasa dibandingkan bank petunjuk statis, Tabel 7 menyajikan perbandingan nyata antara petunjuk Sokratik dinamis yang dihasilkan Agen T2 dan petunjuk statis dari `static_hints.json` pada tiga tingkat bantuan (*Level 1–3*).

*Tabel 7. Contoh komparasi keluaran perancah Sokratik Agen T2 (RAG Dinamis) versus Bank Petunjuk Statis (`static_hints.json`).*

| Komponen KC & Konteks Kesalahan Siswa | Tingkat Bantuan | Keluaran Agen T2 Dinamis (`SecureLLMClient` $\le 60$ Kata) | Keluaran `static_hints.json` (Fallback $< 50$ ms) | Analisis Kepatuhan Pedagogis |
|:---|:---:|:---|:---|:---|
| **`KC-04: WLAN_FREQ_CHANNEL`**<br/>*Kasus:* AP lab mengalami tabrakan frame tinggi di kanal 6 (2,4 GHz). | **Level 1**<br/>(*Directing Attention*) | *"Coba amati lebar pita frekuensi setiap kanal pada spektrum 2,4 GHz. Jika titik akses saat ini berada di kanal 6, berapa jarak minimal antar-nomor kanal agar spektrumnya sama sekali tidak saling beririsan?"* (33 kata) | *"Perhatikan alokasi kanal pada pita 2.4 GHz yang tidak saling bertumpuk (non-overlapping channels)."* (14 kata) | Keduanya lolos `AnswerLeakageGuard` (tidak menyebut angka `1` atau `11`); RAG dinamis lebih tajam memancing pertanyaan reflektif. |
| **`KC-11: ICMP_TROUBLE_DHU`**<br/>*Kasus:* Ping ke gateway memunculkan *Destination Host Unreachable* vs *RTO*. | **Level 2**<br/>(*Intermediate Step*) | *"Bandingkan siapa yang mengirim pesan galat tersebut: apakah paket tertahan karena pengirim gagal menemukan alamat fisik (ARP/rute lokal) menuju gateway, atau paket sudah terkirim jauh namun balasannya diblokir?"* (29 kata) | *"Periksa apakah ada kesalahan tabel routing, konfigurasi subnet yang salah, atau kegagalan resolusi ARP lokal."* (15 kata) | Lolos filter (< 60 kata, 0% kebocoran opsi); memandu isolasi penyebab Layer 2/3. |
| **`KC-07: WLAN_SIGNAL_PROP`**<br/>*Kasus:* Redaman dinding beton menyebabkan RSSI turun dari $-50$ dBm ke $-85$ dBm. | **Level 3**<br/>(*Conceptual Framework*) | *"Gunakan kerangka evaluasi anggaran daya (link budget): petakan urutan pelemahan sinyal mulai dari daya pancar AP, redaman penghalang dinding beton, hingga sensitivitas penerima klien pada skala logaritmik negatif (-dBm)."* (30 kata) | *"Sinyal di atas -65 dBm dikategorikan baik untuk koneksi stabil, sedangkan di bawah -75 dBm rentan mengalami putus koneksi."* (19 kata) | Lolos filter; membangun kerangka berpikir sistematis tanpa membocorkan huruf opsi. |

Keunggulan utama penggabungan RAG dinamis dan *Static Fallback* ini adalah: ketika koneksi normal, siswa memperoleh pertanyaan pemandu Sokratik yang kontekstual terhadap bunyi soal spesifik yang sedang dihadapi; namun ketika terjadi *timeout* atau lonjakan beban, siswa tetap mendapatkan petunjuk konseptual terkurasi dari `static_hints.json` tanpa gangguan belajar.

Selanjutnya, pengujian otomatis menggunakan `pytest` terhadap seluruh 7 modul perangkat lunak menghasilkan tingkat kelulusan sempurna (**41/41 skenario lulus, 100%**, waktu eksekusi 14,12 detik), sebagaimana dirinci pada Tabel 8.

*Tabel 8. Matriks verifikasi rangkaian 41 pengujian unit dan keamanan sistem LogiTrace (`pytest`).*

| Modul Pengujian (`logitrace/tests/`) | Jumlah Uji | Fokus Skenario Verifikasi Teknis & Keamanan | Hasil Uji | Bukti Keandalan Aktual |
|:---|:---:|:---|:---:|:---|
| `test_secure_client.py` | 6 | Sanitasi `PIIScrubber` (NISN, HP, Email, ID `S07`, Nama Sekolah), `mask_secret()`, konfigurasi `9router`, anti-XSS `html.escape()`, & *offline fallback*. | **6/6 Lulus (100%)** | Identitas `Budi`, `0061234567`, `SMK Negeri 4 Bandung` tersensor 100%; kunci menjadi `sk-d****cdef`; `<script>` diubah menjadi `&lt;script&gt;`. |
| `test_guardrails.py` | 4 | Penolakan frasa pembocor (`"jawabannya adalah"`, `"the correct answer is"`), deteksi token jawaban benar (`WPA3-SAE`), & batas $> 60$ kata. | **4/4 Lulus (100%)** | 100% draf bocor atau $> 60$ kata ditolak sebelum mencapai antarmuka siswa. |
| `test_cognitive_engine.py` | 7 | Inversi `logit`-`sigmoid`, monotonisitas $\hat{p}$, pembaruan $m$ mandiri ($h=1{,}0$) vs. berbantuan ($h=0{,}5$), penalti salah $\gamma_d$, *clipping* $[0{,}02; 0{,}98]$, & peluruhan $\tau=60$ hari. | **7/7 Lulus (100%)** | Akurasi numerik presisi hingga $10^{-4}$ tanpa kemungkinan *overflow* atau pembagian nol. |
| `test_zpd_selector.py` | 3 | *Prerequisite gating* DAG ($m \ge 0{,}60$), seleksi pita ZPD $[0{,}60; 0{,}85]$ terdekat ke $0{,}72$, bonus KC baru ($-0{,}05$), & penalti KC berulang ($+0{,}10$). | **3/3 Lulus (100%)** | Simpul anak terkunci rapat selama simpul induk belum mencapai $m \ge 0{,}60$. |
| `test_calibration.py` | 3 | Prior awal *cold-start* ($m_0 = 0{,}25$), sekuens 6 butir kalibrasi awal, & pewarisan estimasi klaster DAG. | **3/3 Lulus (100%)** | Status kalibrasi aktif tepat pada butir 1–6 (`index 0..5`) dan nonaktif mulai butir ke-7. |
| `test_item_bank.py` | 8 | Integritas skema 180 butir dua tingkat, kelengkapan 12 KC, pemetaan 5 dimensi TOLT, dan struktur graf asiklik (DAG bebas siklus). | **8/8 Lulus (100%)** | Seluruh 12 KC dan 180 butir tervalidasi bebas dari ketergantungan melingkar (*cycle-free*). |
| `test_backend_api.py` | 10 | Integrasi *end-to-end* endpoint FastAPI: sesi kuis, pengiriman respons *two-tier*, Agen T1 (`LabelingService`), Agen T2 (`HintService`), dan Agen T3 (`SummaryService`). | **10/10 Lulus (100%)** | Seluruh transaksi tercatat secara *append-only* dan mengembalikan respons JSON valid. |

Mengenai kekhawatiran kebocoran semantik implisit (*semantic answer leakage*), selain mengandalkan filter ekspresi reguler pasca-inferensi pada `AnswerLeakageGuard`, arsitektur LogiTrace menerapkan prinsip *Zero Answer Leakage by Design*: metode `SecureLLMClient.call_api()` (baris 236–241 pada `secure_client.py`) **hanya mengirimkan nama topik KC, level bantuan (1–3), dan teks pertanyaan pokok (`question_text`) tanpa menyertakan daftar opsi pilihan ganda (`options`) maupun kunci jawaban (`correct_answer_text`) ke dalam prompt LLM**. Daftar opsi dan kunci jawaban hanya dipegang secara lokal oleh `HintService.generate_socratic_hint()` untuk keperluan pemindaian silang pasca-inferensi. Dengan demikian, model bahasa secara struktural tidak mengetahui huruf maupun bunyi opsi jawaban yang tersedia di layar siswa.

Kematangan arsitektur perangkat lunak ini diwujudkan ke dalam antarmuka pengguna responsif yang divalidasi melalui 9 skenario pengujian otomatis Playwright (Gambar 4).

| (a) Pengerjaan Butir & Perancah Sokratik | (b) Umpan Balik Jawaban Benar |
| :---: | :---: |
| ![Gambar 4a](figures/04_student_quiz.png) | ![Gambar 4b](figures/05b_student_feedback_correct.png) |
| **(c) Umpan Balik Jawaban Salah** | **(d) Layar Selebrasi Ketuntasan Sesi** |
| ![Gambar 4c](figures/05_student_feedback_wrong.png) | ![Gambar 4d](figures/06_student_celebration.png) |

*Gambar 4. Antarmuka responsif evaluasi formatif adaptif siswa pada perangkat bergerak (viewport seluler 390×844 px): (a) pengerjaan butir dua tingkat dengan perancah Sokratik Level 1 terbuka; (b) umpan balik pedagogis jawaban benar dengan kenaikan penguasaan kognitif (+0,225) dan kontrol audio; (c) umpan balik konstruktif jawaban salah dan kartu penjelasan konsep; dan (d) layar selebrasi ketuntasan kuis adaptif.*

Desain antarmuka siswa (Gambar 4) mengadopsi prinsip *mobile-first* dengan target sentuh ergonomis ($\ge 44 \times 44\text{ px}$) yang dioptimalkan untuk perangkat telepon pintar siswa di Zona B. Pada saat menghadapi soal penalaran jaringan dua tingkat yang menantang, siswa dapat membuka kartu petunjuk bertahap tanpa menutup soal (Gambar 4a). Ketika siswa menjawab benar secara mandiri atau berbantuan, sistem secara instan menampilkan banner hijau beserta pill kenaikan penguasaan kognitif (misalnya $+0{,}225$) dan efek audio *chime* yang dapat dibisukan melalui tombol HUD (Gambar 4b). Sebaliknya, apabila respons siswa salah atau miskonsepsi terdeteksi, sistem tidak menampilkan vonis kegagalan yang mematahkan motivasi (*punitive grading*), melainkan memunculkan banner pemandu (*"Hampir!"*) disertai kartu elaborasi konseptual untuk memancing refleksi aktif (Gambar 4c). Pada akhir sesi adaptif, layar selebrasi (Gambar 4d) menyajikan transparansi capaian: jumlah butir tuntas, efisiensi penggunaan petunjuk, dan rata-rata penguasaan akhir sebelum siswa berpindah ke stasiun praktikum perangkat keras di Zona A.

---

### 3.5 Pembahasan Komparatif (*Comparative Discussion*)

Tabel 9 merangkum posisi kebaruan ilmiah arsitektur LogiTrace dibandingkan dengan literatur pelacakan pengetahuan dan tutor cerdas terkini (2015–2026).

*Tabel 9. Perbandingan arsitektur LogiTrace terhadap model literatur pelacakan pengetahuan dan tutor cerdas.*

| Dimensi Arsitektur | DKT Standar (Piech et al., 2015) | Logic-Muse (Nkambou et al., 2023) | SageJavon (Zhao et al., 2026) | LogiTrace (Penelitian Ini) |
|:---|:---|:---|:---|:---|
| **Kebutuhan Data Latih Awal** | Masif ($\ge 100.000$ interaksi) | Kecil ($N = 294$, data respons) | Sedang (EdNet / ASSISTments) | **Nol Data Interaksi Awal (*Training-Free Prior $m_0=0{,}25$*)** |
| **Keterauditan Kognitif (*Explainability*)** | Kotak hitam (*black-box* RNN) | Graf Bayesian terstruktur | Semiterbuka via GIKT | **Sepenuhnya Terbuka & Deterministik (< 1 ms)** |
| **Fleksibilitas Infrastruktur AI** | Klaster GPU pelatihan | Pelatihan luring (*offline*) | Ketergantungan awan tunggal | **Multi-Provider (`9router` Proxy, `DeepSeek`/`Groq`, & `Ollama` CPU)** |
| **Spesialisasi Agen Pedagogis** | Hanya prediksi skor | Hanya pelacakan penalaran | Perancah pemrograman | **Orkestrasi Tri-Agen (T1 Kurasi, T2 Sokratik 3-Level, T3 Refleksi & *Peer-Tutoring*)** |
| **Proteksi Privasi & Ketahanan Layanan** | Tidak memodelkan PII | Terbatas di lab riset | Rentan transmisi awan | **Pre-Flight Zero-PII (`PIIScrubber`) + Fallback Statis (< 50 ms, 0% Outage)** |

Berbeda dari model neural DKT konvensional yang mengoptimalkan fungsi kecocokan kurva pada data masa lalu (Abdelrahman et al., 2023; Shen et al., 2024), L3 LogiTrace memprioritaskan *pedagogical explainability* seketika. Guru dapat melacak secara pasti mengapa seorang siswa memperoleh soal tertentu melalui fungsi objektif ZPD dan penalti dependensi DAG, serta memperoleh rekomendasi pasangan *Peer-Tutoring* otomatis pada akhir sesi pembelajaran melalui Agen T3.

---

### 3.6 Antarmuka Telemetri Guru Waktu-Nyata (*Ambient Dashboard*) & Orkestrasi Sesi

Mendukung model pembelajaran *Station Rotation*, Lapisan 3 LogiTrace dilengkapi modul telemetri waktu-nyata (*Ambient Awareness Dashboard*) berbasis protokol WebSocket yang diakses melalui jaringan area lokal (intranet Wi-Fi laboratorium pada pita frekuensi terisolasi agar tidak terganggu oleh praktikum jaringan siswa di Zona A). Menghindari fenomena beban perhatian berlebih pada guru (*teacher split-attention overload*), antarmuka dasbor orkestrasi guru mengintegrasikan tiga tampilan fungsional utama (Gambar 5).

| (a) Dasbor Telemetri Ambient Guru (Heatmap 12 KC & Kartu Prioritas Siswa) |
| :---: |
| ![Gambar 5a](figures/07_teacher_dashboard.png) |
| **(b) Modal Ringkasan AI Agen T3 & Rekomendasi Kelompok Tutor Sebaya** |
| ![Gambar 5b](figures/08_teacher_summary_modal.png) |
| **(c) Modal Manajemen Sesi Stasiun Rotasi & Kurasi Butir Soal Agen T1** |
| ![Gambar 5c](figures/09_teacher_manage_modal.png) |

*Gambar 5. Antarmuka orkestrasi dan telemetri guru berbasis web desktop (viewport 1440×900 px): (a) dasbor pemantauan waktu-nyata dengan kartu peringatan ambient Top-3 Siswa Butuh Bantuan dan matriks penguasaan 12 KC untuk 34 siswa; (b) modal ringkasan kelas AI pasca-sesi dari Agen T3 dengan rekomendasi pasangan tutor sebaya; dan (c) modal manajemen sesi stasiun rotasi serta kurasi bank butir soal dua tingkat Agen T1.*

Struktur antarmuka telemetri guru pada Gambar 5 dirancang dengan pertimbangan beban kognitif pengajar:
1. **Dasbor Telemetri Ambient (Gambar 5a):** Pada saat sesi pengerjaan kuis adaptif di Zona B berlangsung, guru tidak dituntut membaca log numerik rumit. Dasbor secara otomatis menyorot kartu prioritas minimalis **Top-3 Siswa Membutuhkan Bantuan Segera** (misalnya siswa S14 yang terdeteksi macet 3 kali pada `KC-11: ICMP_TROUBLE_DHU` dengan status $m = 0{,}18$), lengkap dengan tombol rekomendasi intervensi pedagogis cepat. Di bawah kartu peringatan, matriks penguasaan (*heatmap*) memetakan sebaran kemahiran 34 siswa pada 12 KC secara visual, disertai indikator status koneksi WebSocket, kelolosan SLA inferensi, dan mode penyedia aktif (`9router` / Hybrid). Informasi ini memandu guru yang bertugas berkeliling (*roving teacher*) untuk mendatangi meja siswa yang mengalami hambatan konseptual secara privat tanpa menimbulkan stigma sosial pemisahan kelas remedial.
2. **Modal Ringkasan AI & Rekomendasi Peer-Tutoring (Gambar 5b):** Memasuki menit ke-80 pada fase penutup pembelajaran, guru dapat membuka modal ringkasan AI Agen T3. Layar ini menyajikan sintesis naratif 3 paragraf mengenai capaian kelas, KC yang paling dikuasai, miskonsepsi dominan, serta daftar pembentukan kelompok *Peer-Tutoring* otomatis yang memasangkan siswa berkemampuan tinggi ($m \ge 0{,}70$) dengan rekan yang membutuhkan penguatan ($m \le 0{,}45$). Guru dapat menyalin narasi ini secara langsung melalui tombol *Salin Teks* untuk ditampilkan di proyektor kelas atau diarsipkan ke jurnal mengajar.
3. **Modal Manajemen Sesi & Kurasi Butir Soal (Gambar 5c):** Guru memegang kendali operasional penuh untuk membuka stasiun rotasi, menutup sesi ketika waktu habis, maupun mereset status kelas. Pada tab pelabelan semantik, guru dapat meninjau antrean butir soal baru hasil kurasi Agen T1 (`LabelingService`), memverifikasi kesesuaian estimasi tingkat kesulitan ($d$), serta menyetujui butir soal untuk masuk ke dalam repositori aktif secara *human-in-the-loop*.

---

## 4. Kesimpulan dan Agenda Riset Lanjutan

Penelitian ini berhasil merancang, menguji ketahanan konkurensi, dan memvalidasi keamanan arsitektur evaluasi formatif adaptif **LogiTrace**. Integrasi dekomposisi 12 KC jaringan nirkabel pada Graf Dependensi Prasyarat dan dimensi TOLT (L1), pengindeksan semantik 180 butir dua tingkat bersama Agen T1 (L2), serta mesin inferensi deterministik berlatensi 0,18 ms yang didampingi orkestrasi Agen T2/T3 melalui `SecureLLMClient` multi-provider (`9router`, `DeepSeek`, `Groq`, dan `Ollama` CPU) berpelindung *Defense-in-Depth* dan *Zero-PII* (L3), terbukti mampu mengatasi kendala komputasi dan privasi di sekolah kejuruan. Pengujian konkurensi empiris membuktikan bahwa mode CPU lokal 8-thread mampu melayani beban simultan hingga $k = 2$ klien aktif (yang secara probabilistik mencukupi $> 99{,}9\%$ pola kedatangan alami 17 siswa di Zona B), sementara mode proxy `9router` dan Cloud API memangkas beban memori host hingga $< 50$ MB. Pada saat terjadi lonjakan beban ($k \ge 4$) maupun putus jaringan, mekanisme *Graceful Fallback* (< 50 ms) menjamin tingkat kegagalan layanan nol (*zero service outage*), yang diperkuat oleh kelulusan 100% pada 41 skenario pengujian unit otomatis (`pytest`) serta pengujian alur antarmuka menyeluruh (*end-to-end*) berbasis Playwright.

### Keterbatasan Penelitian
Pengujian yang dilaporkan dalam naskah ini berada pada tahap pembuktian kelayakan arsitektur perangkat lunak, kestabilan numerik pemodelan kognitif, dan ketahanan tolok ukur komputasi laboratorium (*in-silico technical benchmarking*). Penelitian ini belum mencakup evaluasi dampak pedagogis terhadap peningkatan hasil belajar (*learning gain*), retensi memori jangka panjang di lapangan, maupun kalibrasi parameter psikometrik empiris dari sampel respons siswa manusia.

### Agenda Riset Lanjutan
Tahapan riset berikutnya adalah pelaksanaan uji coba lapangan (*field trial*) di SMKN 4 Bandung. Implementasi akan mengadopsi model pembelajaran *Single-Room Station Rotation* pada 34 siswa kelas XI TKJ dengan strategi *Device-Purpose Split* (ponsel cerdas yang terhubung ke jaringan lokal untuk asesmen adaptif mandiri di Zona B, dan PC laboratorium rasio 1:1 untuk praktikum fisik di Zona A). Evaluasi empiris lanjutan akan mengukur normalisasi gain kognitif ($N\text{-Gain}$), uji beda dimensi penalaran logis TOLT, persepsi kegunaan guru/siswa, serta efektivitas matriks *Peer-Tutoring* Agen T3 di kelas nyata.

---

## Pernyataan Wajib (*Declarations*)

### Ketersediaan Data dan Kode (*Data and Code Availability*)
Arsitektur basis data, taksonomi 12 Knowledge Components, graf dependensi DAG, modul multi-provider `secure_client.py`, rangkaian 41 pengujian unit `pytest`, artefak pengujian antarmuka Playwright E2E, skrip pengujian konkurensi `benchmark_concurrency_ollama.py`, serta dataset hasil pengujian beban `benchmark_concurrency_results.json` tersedia pada repositori riset LogiTrace: `https://github.com/fajari-arkan/logitrace-core`.

### Deklarasi Etika (*Ethics Declaration*)
Penelitian tahap rekayasa sistem ini berfokus pada pengujian performa algoritma komputasi dan simulasi numerik laboratorium (*in-silico*), sehingga tidak melibatkan subjek manusia secara langsung dan tidak memerlukan persetujuan komite etik medis/manusia. Protokol untuk pengujian lapangan mendatang telah diselaraskan dengan izin kemitraan sekolah di SMKN 4 Bandung serta prinsip pelindungan data anak berdasarkan UU No. 27 Tahun 2022 (UU PDP).

### Kontribusi Penulis (*Author Contributions - CRediT*)
- **Fajari Arkan Fadhlurrahman:** Konseptualisasi ide riset, perancangan arsitektur tiga lapis dan orkestrasi Tri-Agen, pengembangan basis kode L3 serta modul `SecureLLMClient` (*9router* & *Zero-PII*), pelaksanaan pengujian konkurensi CPU dan 41 *unit test*, analisis data telemetri, serta penulisan draf naskah.
- **[Nama Dosen Pembimbing 1]:** Supervisi metodologi *Design Science Research*, telaah kritis formulasi matematis kognitif, validasi protokol pengujian konkurensi, serta penyuntingan naskah akhir.
- **[Nama Dosen Pembimbing 2]:** Supervisi keselarasan Kurikulum Merdeka SMK TKJ Fase F, penelaahan pedagogis perancah Sokratik 3-tingkat dan algoritma *Peer-Tutoring*, serta persetujuan versi final naskah.

### Konflik Kepentingan (*Conflict of Interest*)
Para penulis menyatakan tidak memiliki benturan kepentingan finansial, profesional, maupun personal yang dapat memengaruhi objektivitas penulisan dan temuan penelitian ini.

### Sumber Pendanaan (*Funding Statement*)
Pengembangan dan pengujian komputasi sistem ini didanai secara mandiri oleh tim peneliti dalam kerangka penelitian skripsi sarjana Program Studi Pendidikan Ilmu Komputer, Fakultas Pendidikan Matematika dan Ilmu Pengetahuan Alam, Universitas Pendidikan Indonesia.

### Pernyataan Penggunaan Kecerdasan Buatan (*AI Usage Disclosure*)
Dalam penyusunan naskah artikel ini, penulis memanfaatkan perangkat bantu kecerdasan buatan generatif (Antigravity berbasis Gemini dan Claude) untuk membantu pembuatan kerangka skrip pengujian otomatis (`pytest`), pemeriksaan gramatikal bahasa Inggris pada bagian abstrak, serta penataan format tabel markdown. Seluruh rancangan arsitektur perangkat lunak, formulasi matematika kognitif, verifikasi data empiris hasil *benchmark*, dan penarikan kesimpulan ilmiah dirumuskan, diuji, dan dipertanggungjawabkan sepenuhnya oleh penulis manusia.

---

## Daftar Pustaka

Abdelrahman, G., Wang, Q., & Nunes, B. (2023). Knowledge tracing: A survey. *ACM Computing Surveys*, *55*(11), Article 224, 1–37. https://doi.org/10.1145/3569576

Corbett, A. T., & Anderson, J. R. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. *User Modeling and User-Adapted Interaction*, *4*(4), 253–278. https://doi.org/10.1007/BF01099821

Huang, T., Ou, X., Yang, H., Hu, S., Geng, J., Hu, J., & Xu, Z. (2024). Remembering is not applying: Interpretable knowledge tracing for problem-solving processes. In *MM 2024: Proceedings of the 32nd ACM International Conference on Multimedia* (pp. 3151–3159). Association for Computing Machinery. https://doi.org/10.1145/3664647.3681049

Jadhav, D., Chettri, S. K., Tripathy, A. K., Ghate, O., Chaudhari, R., & Avhad, S. (2023). Unlocking math potential: EDSense - A personalized intervention tool for children with dyscalculia. In *Proceedings of the 3rd International Conference on Advanced Computing Technologies and Applications (ICACTA 2023)* (pp. 1–6). IEEE. https://doi.org/10.1109/ICACTA58201.2023.10393795

Jung, H., Yoo, J., Yoon, Y., & Jang, Y. (2025). CLST: Cold-start mitigation in knowledge tracing by aligning a generative language model as a students' knowledge tracer. *Journal of Educational Data Mining*, *17*(2), 86–117. https://doi.org/10.48550/arXiv.2406.10296

Komalasari, R., Dewi, S. R., & Widiastuti, R. (2023). Evaluasi efektivitas media pembelajaran berbasis simulasi jaringan komputer di sekolah kejuruan. *INVOTEC*, *19*(2), 112–124. https://doi.org/10.17509/invotec.v19i2.56412

Nkambou, R., Brisson, J., Tato, A., & Robert, S. (2023). Learning logical reasoning using an intelligent tutoring system: A hybrid approach to student modeling. *Proceedings of the AAAI Conference on Artificial Intelligence*, *37*(13), 15930–15937. https://doi.org/10.1609/aaai.v37i13.26891

Nurbaeti, N., Sutrisno, B., & Purwanto, A. (2024). Analisis kebutuhan asesmen adaptif dalam pembelajaran jaringan komputer pada Kurikulum Merdeka SMK. *Edumatic: Jurnal Pendidikan Informatika*, *8*(1), 45–56. https://doi.org/10.29408/edumatic.v8i1.21890

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, *24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302

Pelánek, R. (2016). Applications of the Elo rating system in adaptive educational systems. *Computers & Education*, *98*, 169–179. https://doi.org/10.1016/j.compedu.2016.03.017

Piech, C., Bassen, J., Huang, J., Ganguli, S., Sahami, M., Guibas, L. J., & Sohl-Dickstein, J. (2015). Deep knowledge tracing. *Advances in Neural Information Processing Systems*, *28*, 505–513. https://doi.org/10.48550/arXiv.1506.05908

Shen, S., Liu, Q., Huang, Z., Zheng, Y., Yin, M., Wang, M., & Chen, E. (2024). A survey of knowledge tracing: Models, variants, and applications. *IEEE Transactions on Learning Technologies*, *17*, 1898–1919. https://doi.org/10.1109/TLT.2024.3383325

Tato, A., & Nkambou, R. (2022). Infusing expert knowledge into a deep neural network using attention mechanism for personalized learning environments. *Frontiers in Artificial Intelligence*, *5*, Article 921476, 1–14. https://doi.org/10.3389/frai.2022.921476

Tobin, K. G., & Capie, W. (1981). The development and validation of a group test of logical thinking. *Educational and Psychological Measurement*, *41*(2), 413–423. https://doi.org/10.1177/001316448104100220

Wang, Y., Anand, C. S., & Tan, C. W. (2026). Guiding, not solving: Agentic scaffolding for LLM programming tutors. *CEUR Workshop Proceedings*, *4248*, 1–10. https://ceur-ws.org/Vol-4248/

Wing, J. M. (2006). Computational thinking. *Communications of the ACM*, *49*(3), 33–35. https://doi.org/10.1145/1118178.1118215

Xia, M., Schmucker, R., Borchers, C., & Aleven, V. (2026). Optimizing mastery learning by fast-forwarding over-practice steps. *Lecture Notes in Computer Science*, *16063*, 549–563. https://doi.org/10.1007/978-3-032-03870-8_37

Zhao, H., Wu, Y., Lu, Z., Yu, X., Miao, W., & Chen, L. (2026). SageJavon: A scalable AI tutor for personalized programming learning. *Information Processing & Management*, *63*(5), Article 104605, 1–18. https://doi.org/10.1016/j.ipm.2025.104605
