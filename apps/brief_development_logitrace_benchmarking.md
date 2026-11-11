# BRIEF INSTRUKSI UNTUK SESI AI DEVELOPMENT: PENGUJIAN BENCHMARK KONKURENSI LOGITRACE

**Tujuan:** Menghasilkan data empiris uji beban konkurensi CPU lokal untuk menjawab revisi mayor naskah jurnal SINTA 3/SINTA 2 LogiTrace.

---

## 1. Konteks Riset & Permasalahan

Sistem **LogiTrace** adalah platform evaluasi formatif adaptif untuk siswa SMK TKJ yang memiliki arsitektur tiga lapis:
- **L1 (Basis Pengetahuan):** 12 Knowledge Components (KC) dan Graf Dependensi Prasyarat (DAG).
- **L2 (Indeks Semantik):** Bank butir soal pilihan ganda dua tingkat dengan embedding pgvector.
- **L3 (Runtime Deterministik & RAG):** 
  - Mesin inferensi deterministik matematis (< 1 ms).
  - Agen perancah Sokratik menggunakan model bahasa lokal terkuantisasi (`Qwen2.5-3B-Instruct-Q4_K_M`) via Ollama CPU lokal (tanpa GPU).
  - Pengaman *Answer Leakage Guard* berbasis Regex dan batas waktu *timeout* 3,0 detik dengan *Graceful Fallback* instan (< 50 ms) ke bank petunjuk statis.

### Temuan Reviewer Jurnal (Critical Issue)
Reviewer jurnal menilai bahwa pengujian inferensi LLM sekuensial tunggal (30 panggilan satu per satu) **belum membuktikan ketahanan sistem di kelas nyata**. Jika 3–5 siswa meminta petunjuk bantuan secara bersamaan, CPU 8-core berpotensi mengalami saturasi antrean (*queueing delay*), menyebabkan latensi melampaui batas batas 3,0 detik dan memaksa sistem selalu beralih ke petunjuk statis.

---

## 2. Tugas Konkret Tim Development

Tolong buatkan skrip otomatis pengujian benchmark (**`benchmark_concurrency_ollama.py`**) dengan spesifikasi sebagai berikut:

### A. Skenario Uji Beban (Concurrent Clients)
Jalankan pengujian pemanggilan endpoint Ollama lokal (`http://localhost:11434/api/generate`):
- Model: `Qwen2.5-3B-Instruct-Q4_K_M`
- Parameter inferensi: `temperature = 0.0`, `seed = 42`, `max_tokens = 150`
- Prompt uji: Prompt riil Agen T2 (Socratic Hint Scaffolding) materi WLAN / ICMP
- Variasi beban bersamaan:
  1. $k = 1$ klien (baseline sekuensial)
  2. $k = 2$ klien serentak
  3. $k = 4$ klien serentak
  4. $k = 8$ klien serentak

### B. Metrik yang Wajib Dicatat & Dikeluarkan
Skrip harus mengeluarkan tabel rekapitulasi berisi:
1. **Rerata Latensi (Mean Latency)** dalam detik/milidetik per skenario $k$.
2. **Latensi Persentil ke-95 ($p95$)** dalam detik.
3. **Persentase Keberhasilan Lolos Batas Ambang (< 3,0 Detik)** (%).
4. **Persentase Terpicunya Graceful Fallback (Timeout > 3,0 Detik)** (%).
5. **Estimasi Utilisasi CPU (%) dan Penggunaan RAM (MB)** selama eksekusi.

### C. Luaran yang Diharapkan
1. File skrip Python mandiri yang dapat langsung dieksekusi dengan perintah:  
   `python benchmark_concurrency_ollama.py`
2. Tabel ringkasan hasil dalam format Markdown agar dapat langsung disalin ke Naskah Publikasi Bab 3 (Tabel 2 & Tabel 3).
3. Analisis singkat: pada batas konkurensi berapa ($k$) server CPU lokal mulai mengalami saturasi dan membutuhkan antrean asinkron atau alokasi *fallback*.
