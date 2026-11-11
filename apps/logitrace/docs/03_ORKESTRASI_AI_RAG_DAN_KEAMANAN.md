# MODUL 03: ORKESTRASI AGEN AI (RAG) & ARSITEKTUR KEAMANAN
## Tri-Agent Specialization, Privacy-Preserving Zero-PII Cloud Call, & Defense-in-Depth

---

### 1. Arsitektur Tri-Agent LogiTrace

Sistem LogiTrace menerapkan spesialisasi tiga agen AI cerdas (*Tri-Agent Pattern*) yang beroperasi pada konteks pedagogis yang berbeda:

```text
+-----------------------------------------------------------------------------------+
|                        ORKESTRASI TRI-AGEN LOGITRACE (RAG-KT)                     |
+-----------------------------------------------------------------------------------+
|  AGEN T1: Semantic Item Labeler (Kurasi Bank Butir Soal Baru)                    |
|  - Waktu Aktif: Pra-pembelajaran (Di luar jam tatap muka oleh guru/kurikulum)     |
|  - Tugas: Analisis semantik teks soal baru -> Klasifikasi 12 KCs, estimasi d(1-3) |
|  - Fitur: Review Queue dengan persetujuan manusia (Human-in-the-Loop Approval)   |
+-----------------------------------------------------------------------------------+
|  AGEN T2: Socratic Hint Scaffolding (Bantuan Belajar Real-Time Siswa)             |
|  - Waktu Aktif: Saat pengerjaan butir adaptif 7-20 di Zona B                      |
|  - Tugas: Membimbing penalaran teknis siswa tanpa membocorkan kunci jawaban       |
|  - Batasan: Maksimal 60 kata, 'Guiding, Not Solving', penalti mastery h = 0.5    |
|  - Pengaman: Pre-flight Zero-PII, Regex Answer Leakage Guard, Fallback < 50 ms   |
+-----------------------------------------------------------------------------------+
|  AGEN T3: Session Narrative Reflection & Peer-Tutoring Pairing Matrix             |
|  - Waktu Aktif: Fase 5 (Menit 77-85 / Sesi Pleno Refleksi Akhir Kelas)            |
|  - Tugas: Agregasi data 34 siswa -> Sintesis narasi refleksi capaian 12 KCs       |
|  - Algoritma: Bipartite Matching Tutor Sebaya (Tutor m >= 0.65 <-> Mentee <= 0.45)|
+-----------------------------------------------------------------------------------+
```

---

### 2. Agen T1: Semantic Item Labeler (Kurasi Bank Soal)
- **Implementasi:** [`logitrace/backend/app/rag/labeling_service.py`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/backend/app/rag/labeling_service.py)
- **Cara Kerja:**
  1. Guru mengunggah teks butir soal baru pada antarmuka *Review Queue*.
  2. Agen T1 menghitung representasi semantik soal dan mencocokkannya dengan taksonomi 12 KCs.
  3. Sistem mengevaluasi taksonomi kognitif butir untuk menentukan estimasi tingkat kesulitan ($d \in \{1, 2, 3\}$), dimensi TOLT, dan teks penalaran pendukung.
  4. Sistem menyajikan kartu telaah (*review card*) kepada guru.
  5. Butir baru dapat dipublikasikan setelah disetujui (*approved*) oleh guru manusia (*Human-in-the-Loop*). Butir dengan keyakinan $< 0.60$ wajib ditinjau secara manual.

---

### 3. Agen T2: Socratic Hint Scaffolding (Guiding, Not Solving)
- **Implementasi:** [`logitrace/backend/app/rag/hint_service.py`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/backend/app/rag/hint_service.py) & [`logitrace/backend/app/rag/secure_client.py`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/backend/app/rag/secure_client.py)
- **Prinsip Utama Pedagogis:**
  - **Panjang Teks Maksimal 60 Kata:** Menghindari beban kognitif berlebih (*cognitive overload*) pada siswa SMK.
  - **Pertanyaan Penuntun (Socratic Questioning):** Memberikan pertanyaan pemicu atau analogi kejuruan daripada penjelasan teoretis panjang.
  - **Tiga Tingkat Bantuan Bertingkat (Levels 1–3):**
    - *Level 1 (Directing Attention):* Mengarahkan fokus perhatian pada kata kunci soal (misal: frekuensi, netmask, konektor).
    - *Level 2 (Intermediate Step):* Mengingatkan formula atau tahapan antara (misal: jumlah bit subnet, urutan pinout).
    - *Level 3 (Conceptual Framework):* Memberikan analogi konsep atau kerangka kerja troubleshooting terstruktur.
  - **Penalti Perolehan Penguasaan ($h = 0.5$):** Jika siswa menggunakan petunjuk dan berhasil menjawab benar, penambahan masterynya hanya sebesar $50\%$ dibanding siswa yang menjawab mandiri.

---

### 4. Agen T3: Refleksi Sesi & Rekomendasi Peer-Tutoring
- **Implementasi:** [`logitrace/backend/app/rag/summary_service.py`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/backend/app/rag/summary_service.py)
- **Cara Kerja:**
  1. Pada akhir pembelajaran, guru menekan tombol **"Generate Summary & Peer Tutoring"** di Dasbor Ambient.
  2. Sistem mengagregasi nilai mastery $m$ dari 34 siswa pada seluruh 12 KCs dan mengidentifikasi miskonsepsi umum.
  3. **Algoritma Bipartite Matching Peer-Tutoring:**
     - Siswa dengan $m \ge 0.65$ pada KC tertentu diklasifikasikan sebagai kandidat **Tutor Sebaya**.
     - Siswa dengan $m \le 0.45$ diklasifikasikan sebagai **Mentee**.
     - Algoritma memasangkan mereka dengan aturan: 1 Tutor mendampingi maksimal 2 Mentee.
     - Proteksi *Anti-Self-Pairing:* Siswa tidak pernah dipasangkan dengan dirinya sendiri.
     - Jika seluruh siswa berada pada baseline tanpa tutor yang memenuhi syarat, sistem secara otomatis menugaskan *"Guru Pendamping (Zona B)"* sebagai tutor.
  4. LLM menghasilkan narasi refleksi kelas 3 paragraf dalam Bahasa Indonesia formal untuk dipaparkan di proyektor kelas.

---

### 5. Arsitektur Keamanan Bertingkat (Defense-in-Depth & Zero-PII)

Untuk memastikan sistem dapat beroperasi secara cepat, murah, dan aman dari pelanggaran data pribadi siswa (UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi / UU PDP):

#### A. Layer 1: Pre-Flight Zero-PII Sanitization (`PIIScrubber`)
Sebelum teks apapun dikirim ke API internet (DeepSeek / Groq), modul `PIIScrubber` memindai dan menyensor secara ketat:
- **NISN (10 digit) & NIK (16 digit):** Disensor menjadi `[REDACTED_NISN]`
- **Nomor Telepon (+62 / 08xx):** Disensor menjadi `[REDACTED_PHONE]`
- **Alamat Email:** Disensor menjadi `[REDACTED_EMAIL]`
- **Identitas Siswa (`std_01`, `S01`, `Siswa S12`):** Disensor menjadi `[REDACTED_ID]`
- **Nama Sekolah:** Disensor menjadi `[REDACTED_SCHOOL]`
- **Hasil:** AI di Cloud hanya menerima teks butir soal teknis tanpa pernah mengetahui identitas siswa. Identitas asli siswa tetap 100% tersimpan aman di database lokal laptop penguji.

#### B. Layer 2: Credential & Transport Security
- Token API (`DEEPSEEK_API_KEY`, `GROQ_API_KEY`) hanya disimpan pada file `.env` di server backend. Token tidak pernah dikirim ke browser siswa.
- Token otomatis disensor (*masked*) pada log sistem (`sk-d****cdef`).
- Wajib HTTPS dengan verifikasi sertifikat SSL TLS 1.2+.

#### C. Layer 3: Strict SLA Timeout (3.0 Detik)
- Batas waktu tunggu panggilan API cloud ditetapkan secara tegas maksimal **3,0 detik**.
- Mencegah siswa menunggu terlalu lama saat jaringan internet sekolah mengalami fluktuasi.

#### D. Layer 4: Post-Flight Leakage Guard & Anti-XSS Sanitizer
- **Regex Answer Leakage Guard:** Memindai respons AI terhadap frasa pembocor (*"jawabannya adalah"*, *"pilihlah opsi A"*) dan kemunculan teks jawaban yang benar.
- **Anti-XSS Sanitizer:** Menyaring karakter khusus HTML (`<`, `>`, `&`, `"`) menggunakan `html.escape()` untuk mencegah serangan injeksi skrip di peramban siswa.

#### E. Layer 5: Instant Graceful Fallback (< 50 ms)
- Jika panggilan API gagal akibat: (1) Internet putus, (2) Batas waktu 3,0 detik terlampaui, (3) Rate limit HTTP 429, atau (4) Teks petunjuk mengandung indikasi kebocoran kunci;
- Sistem **secara instan (< 50 milidetik)** mengalihkan output ke *Curated Static Hint Bank*.
- Tingkat kegagalan layanan (*service outage*) terjamin **0%**.

---

### 6. Dukungan Provider Multi-Backend & Integrasi 9router

Untuk memberikan fleksibilitas operasional optimal di laboratorium sekolah tanpa membebani laptop penguji dengan spesifikasi terbatas (misal RAM 8 GB tanpa GPU diskrit), modul [`SecureLLMClient`](file:///c:/kuliah/semester_7/skripsi/apps/logitrace/backend/app/rag/secure_client.py) mendukung 4 mode inferensi yang dapat dipilih secara transparan:

```text
+-------------------------------------------------------------------------------------------------+
|                                 LOGITRACE SECURE LLM CLIENT ARCHITECTURE                        |
+-------------------------------------------------------------------------------------------------+
|                                  [PIIScrubber: Redact PII]                                      |
|                                             |                                                   |
|             +-------------------------------+-------------------------------+                   |
|             |                               |                               |                   |
|             v                               v                               v                   |
|     [Mode 1: 9router]             [Mode 2: Direct Cloud]            [Mode 3: Ollama CPU]        |
|  - Local OpenAI Proxy           - DeepSeek / Groq API             - Local CPU (Qwen2.5-3B)      |
|  - Port: localhost:20128        - HTTPS Endpoint TLS 1.2+         - Port: localhost:11434       |
|  - Model: ag/gemini-3.8-flash   - Latensi: 0.5 - 0.8s             - Latensi: 1.5 - 4.5s         |
|  - Zero Setup GPU Lokal         - Biaya: ~$0.14/1M token          - Bebas Kuota / 100% Offline  |
|             |                               |                               |                   |
|             +-------------------------------+-------------------------------+                   |
|                                             |                                                   |
|                             [AnswerLeakageGuard & Anti-XSS]                                     |
|                                             |                                                   |
|                       +---------------------+---------------------+                             |
|                       | (Valid & Safe)                            | (Timeout / Leaked / Error)  |
|                       v                                           v                             |
|               [Socratic Hint Out]                     [Curated Static Fallback Bank]            |
+-------------------------------------------------------------------------------------------------+
```

#### Spesifikasi Integrasi 9router:
- **Protokol:** OpenAI Chat Completions API (`POST /v1/chat/completions`)
- **Default Endpoint:** `http://localhost:20128/v1/chat/completions`
- **Model Aktif:** `ag/gemini-3.8-flash` (atau model kompatibel yang dikonfigurasi pada 9router)
- **Parameter Khusus:** Parameter `"stream": False` wajib diatur eksplisit pada payload untuk mencegah respons terpecah menjadi Server-Sent Events (SSE).
- **Proteksi Data:** Data prompt tetap melewati `PIIScrubber` sebelum diteruskan ke 9router, menjamin tidak ada PII siswa yang terekam pada router proxy.

#### Matriks Perbandingan Provider di Lingkungan Uji:

| Provider | Endpoint | Latensi Tipikal | Kebutuhan RAM | Biaya / Akses | Rekomendasi Penggunaan |
|:---|:---|:---|:---|:---|:---|
| **9router (Local Proxy)** | `http://localhost:20128/v1` | ~3.0 – 6.0 s | Ringan (< 50 MB) | Fleksibel via proxy | **Default Pengembangan & Uji Terkoneksi** |
| **DeepSeek Cloud** | `https://api.deepseek.com/v1` | ~0.6 – 0.9 s | Nol (Cloud) | Sangat hemat (~$0.14/1M) | Produksi Sekolah Terkoneksi Internet Cepat |
| **Groq Cloud** | `https://api.groq.com/openai/v1` | ~0.3 – 0.5 s | Nol (Cloud) | Free Tier tersedia | Uji Kecepatan Tinggi & Latensi Minimum |
| **Ollama Local CPU** | `http://localhost:11434/api` | ~1.8 – 5.2 s | Berat (~4.5 GB) | 100% Gratis & Mandiri | Kelas Tertutup / Lab Tanpa Akses Internet |

