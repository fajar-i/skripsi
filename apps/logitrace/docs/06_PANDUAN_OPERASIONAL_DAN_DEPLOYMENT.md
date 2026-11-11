# MODUL 06: PANDUAN OPERASIONAL & PENERAPAN (DEPLOYMENT GUIDE)
## Petunjuk Teknis Instalasi, Konfigurasi Lingkungan, dan Eksekusi di Laboratorium

---

### 1. Prasyarat Sistem (System Requirements)

#### A. Perangkat Keras (Hardware Minimal):
- **Server Guru / Laptop Penguji (Host LogiTrace):**
  - Processor: Minimal 4-Core / 8-Thread (e.g. AMD Ryzen 3 / Intel Core i3 gen 11+).
  - RAM: Minimal 8 GB DDR4.
  - Penyimpanan: Minimal 5 GB ruang kosong (SSD direkomendasikan).
  - Jaringan: Kartu Wi-Fi atau port LAN terhubung ke router laboratorium.
- **Perangkat Klien Siswa (Zona B):**
  - Smartphone Android atau iOS siswa yang memiliki peramban modern (Chrome, Safari, Firefox).
  - Terhubung ke SSID Wi-Fi lokal laboratorium TKJ.
- **Perangkat Roving Guru (Zona B):**
  - Tablet (iPad / Android Tablet) atau Laptop ringan untuk memantau Dasbor Ambient.

#### B. Perangkat Lunak (Software Stack):
- Sistem Operasi: Windows 10/11, Ubuntu 22.04 LTS, atau macOS.
- Python: Versi 3.11 s.d. 3.13.
- Basis Data: SQLite (bawaan dev/standalone) atau PostgreSQL dengan ekstensi pgvector.
- Browser: Google Chrome versi 110+ atau Safari versi 16+.

---

### 2. Langkah Instalasi Dependensi & Setup Backend

#### Langkah 1: Kloning Repositori & Buat Virtual Environment
Buka PowerShell atau Terminal pada direktori proyek:
```bash
cd c:\kuliah\semester_7\skripsi\apps\logitrace

# Buat virtual environment python
python -m venv venv

# Aktifkan virtual environment
# Pada Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Pada Linux / macOS:
source venv/bin/activate
```

#### Langkah 2: Instalasi Pustaka Python yang Dibutuhkan
```bash
pip install -r requirements.txt
```
*(Paket utama mencakup: `fastapi`, `uvicorn`, `sqlalchemy`, `aiosqlite`, `httpx`, `pydantic`, `numpy`, `psutil`, `pytest`).*

---

### 3. Konfigurasi Kredensial & Lingkungan (`.env`)

Salin file contoh konfigurasi:
```bash
cp .env.example .env
```

Buka file `.env` menggunakan teks editor dan sesuaikan pilihan provider AI Anda:

```env
# ==============================================================================
# LOGITRACE (RAG-KT) CONFIGURATION
# ==============================================================================

# Pilihan Provider LLM: '9router', 'deepseek', 'groq', 'openai', atau 'ollama'
LOGITRACE_LLM_PROVIDER=9router

# 1. Jika Menggunakan 9router Local Proxy (Default Rekomendasi):
NINEROUTER_API_URL=http://localhost:20128/v1/chat/completions
NINEROUTER_API_KEY=sk-your_9router_api_key_here
NINEROUTER_MODEL=ag/gemini-3.8-flash

# 2. Jika Menggunakan DeepSeek API Langsung (Hemat: ~$0.14 / 1M token):
# DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# LOGITRACE_LLM_MODEL=deepseek-chat

# 3. Jika Menggunakan Groq Cloud API (Free Tier Ultra Cepat):
# GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
# LOGITRACE_LLM_MODEL=llama-3.1-8b-instant

# 4. Jika Menggunakan Ollama Lokal (100% Offline Tanpa Internet):
# LOGITRACE_LLM_PROVIDER=ollama
# LOGITRACE_OLLAMA_URL=http://localhost:11434/api/generate
# LOGITRACE_LLM_MODEL=qwen2.5:3b

# Basis Data Transaksional Append-Only
LOGITRACE_DB_URL=sqlite+aiosqlite:///./logitrace_dev.db
ENVIRONMENT=production
```

> **Catatan Keamanan:** Jika komputer tidak memiliki koneksi internet dan API key dikosongkan, sistem secara otomatis beralih menggunakan **Curated Static Hint Bank (< 50 ms)** tanpa error.

---

### 4. Menjalankan Server Backend FastAPI

Jalankan perintah berikut untuk menyalakan server backend:
```bash
# Jalankan uvicorn server pada port 8000 (bind ke semua IP jaringan lab)
uvicorn logitrace.backend.app.main:app --host 0.0.0.0 --port 8000 --reload
```

Keluaran terminal yang menandakan server siap:
```text
INFO:     Started server process [12400]
INFO:     Waiting for application startup.
INFO:     Database tables verified (Append-Only interactions enabled).
INFO:     Seed items verified: 180 two-tier items loaded.
INFO:     Initialized SecureLLMClient [Provider: 9ROUTER, Model: ag/gemini-3.8-flash]
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

---

### 5. Mengakses Antarmuka Pengguna di Laboratorium

Cari tahu alamat IP lokal laptop server Anda (misal jalankan `ipconfig` di PowerShell, contoh IP: `192.168.1.100`):

1. **Antarmuka Siswa (Smartphone di Zona B):**
   - Siswa membuka browser smartphone dan mengetikkan:  
     `http://192.168.1.100:8000/student/`
   - Siswa memilih kode siswa (`std_01` s.d. `std_34`) untuk memulai kalibrasi dan kuis adaptif ZPD.
2. **Antarmuka Dasbor Ambient Guru (Tablet / Laptop di Zona B):**
   - Guru membuka:  
     `http://192.168.1.100:8000/teacher/`
   - Guru dapat memantau peta panas penguasaan kelas 12 KCs, kartu *Top-3 Stuck Students*, dan memicu *Session Summary Agen T3*.
3. **Dokumentasi API Interaktif (Swagger UI):**
   - Guru atau pengembang dapat memeriksa seluruh endpoint di:  
     `http://192.168.1.100:8000/docs`

---

### 6. SOP Penggunaan Guru Roving Saat Pembelajaran di Lab

1. **Persiapan (H-15 Menit):**
   - Nyalakan router Wi-Fi lab TKJ.
   - Buka server backend LogiTrace di laptop guru (`uvicorn`).
   - Buka halaman Dasbor Ambient di tablet guru.
   - Pastikan jobsheet praktik Zona A sudah diletakkan di meja 17 unit PC lab.
2. **Pelaksanaan Rotasi 1 (05:00 – 40:00):**
   - Kelompok A berada di Zona A (PC Lab), Kelompok B duduk di Zona B (meja kuis).
   - Guru memegang tablet sambil berkeliling di Zona B.
   - Bila muncul kartu merah/oranye *Top-3 Stuck Students*, dekati siswa tersebut dan berikan pertanyaan pemantik lisan (*guiding, not solving*).
3. **Transisi Pergantian Stasiun (40:00 – 42:00):**
   - Bunyikan sinyal bel rotasi.
   - Arahkan Kelompok A bertukar tempat ke Zona B, dan Kelompok B ke Zona A. Waktu jeda maksimal 2 menit.
4. **Pelaksanaan Rotasi 2 (42:00 – 77:00):**
   - Kelompok A mengerjakan kuis adaptif smartphone di Zona B, Kelompok B melakukan praktik PC di Zona A.
   - Guru mengulangi pemantauan roving dan bimbingan klinis.
5. **Pleno Refleksi Akhir Sesi (77:00 – 85:00):**
   - Seluruh 34 siswa berkumpul di area tengah kelas menghadap layar proyektor.
   - Guru menekan tombol **"Generate Summary & Peer Tutoring"** pada Dasbor Ambient.
   - Tampilkan temuan miskonsepsi kelas dan bacakan pasangan *Peer-Tutoring* untuk penugasan kolaboratif pada pertemuan minggu depan.
   - Tutup pembelajaran dengan doa dan apresiasi.
