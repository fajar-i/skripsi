# Audit Penuh — Naskah LogiTrace (SINTA 3) + Produk Perangkat Lunak

**Tanggal audit:** 17 November 2026
**Naskah yang diaudit:** `paper SLR/draf_artikel_logitrace_sinta3.md` (modifikasi terakhir 12 Nov 2026; versi dengan uji Playwright & Gambar 4–5)
**Produk yang diaudit:** `apps/logitrace/` (backend, data, evals, tests, frontend, docs) + `apps/benchmark_concurrency_*`
**Acuan:** `apps/review_draf_artikel_logitrace_sinta3.md` (review panel 5-seat, 16 Nov 2026)
**Sifat audit:** read-only. Tidak ada file naskah/kode yang diubah. Satu-satunya perintah yang mengubah keadaan adalah `pytest` (membuat cache).

---

## 0. Ringkasan Eksekutif

**Verdict: BELUM LAYAK SUBMIT — ada blocker integritas data, bukan hanya Major Revision.**

Review 16 Nov menilai naskah dari teksnya saja dan menyimpulkan *Major Revision*. Audit ini mencocokkan setiap klaim naskah dengan kode, data, dan log produk. Hasilnya lebih berat:

1. **Tabel 4 dan 5 (uji konkurensi "empiris") berasal dari mode simulasi skrip, bukan dari Ollama sungguhan.** Laporan skrip sendiri mencatat `Mode Eksekusi: Validated CPU Queuing Benchmark`, yaitu label yang hanya ditulis bila Ollama **tidak** terdeteksi. Rerata latensinya cocok dengan parameter `np.random.normal` di fungsi simulasi.
2. **Tabel 2 tidak bisa dilacak ke skrip mana pun.** Salah satu barisnya (pencarian `pgvector`) mengukur komponen yang tidak ada di kode.
3. **Bank soal bukan dua tingkat (two-tier).** Ke-180 butir hanya punya satu kunci jawaban, tanpa tingkat alasan. Aturan `r = 1` jika "kedua tingkat benar" (§2.3) tidak diimplementasikan.
4. **`pgvector`/embedding/indeks semantik L2 tidak ada.** Basis data bawaan adalah SQLite.
5. **Skrip E1–E6 dan `docs/05_HASIL_EVALUASI_EMPIRIS_E1_E6.md` berisi angka hasil RNG** (Aiken's V, kappa, ICC, SUS, N-Gain, "validasi oleh 5 pakar") yang disajikan sebagai hasil empiris. Naskah tidak mengutipnya, tetapi repositori yang dijanjikan terbuka memuatnya.
6. **Tidak ada satu pun keluaran LLM yang tercatat di log aplikasi.** Semua log T2 = `static_bank`, semua log T3 = `deterministic_t3_engine`. Kolom "Agen T2 Dinamis" di Tabel 7 tidak punya jejak sumber.
7. **Kunci API `.env` (berbentuk asli, 35 karakter) ikut ter-commit** di commit `5ddd3f5` pada repo dengan remote GitHub.

Kemungkinan penjelasan yang tidak disengaja tetap ada: skrip benchmark **diam-diam** beralih ke simulasi saat Ollama mati, dan skrip-skrip itu dibuat dengan bantuan AI (lihat `brief_development_logitrace_benchmarking.md`). Namun bila diterbitkan apa adanya, reviewer atau pembaca repositori dapat menganggapnya fabrikasi data. Bagian ini harus diselesaikan **sebelum** perbaikan lain dalam roadmap review.

Semua temuan review 16 Nov **masih terbuka**: naskah belum diubah sejak review (12 Nov < 16 Nov). Beberapa di antaranya diperkuat oleh bukti kode (lihat §4).

---

## 1. Lingkup & Metode

| Langkah | Yang dilakukan |
|---|---|
| Baca acuan | Review 5-seat (EIC, R1–R3, DA) + roadmap P0–P2 |
| Identifikasi versi naskah | Dua salinan: `apps/` (11 Nov, tanpa Playwright) dan `paper SLR/` (12 Nov). Yang diaudit adalah versi `paper SLR/`, yang juga dipakai review. |
| Baca kode | `backend/app/**` (engine, rag, routers, schemas, db), `data/**`, `evals/**`, `tests/**`, `frontend/student/app.js` |
| Jalankan | `pytest` (seluruh suite), hitung ulang Tabel 3 & pita ZPD dengan fungsi asli, uji `PIIScrubber` dengan variasi input, uji 36 petunjuk statis × 180 butir terhadap `AnswerLeakageGuard`, query `agent_logs` di `logitrace.db` & `logitrace_dev.db`, `git ls-files` |
| Tidak dilakukan | Menjalankan Ollama/9router (tidak tersedia), membuka repo GitHub yang disebut naskah, verifikasi ulang DOI (diambil dari review), melihat isi gambar PNG |

---

## 2. Blocker Integritas (wajib selesai sebelum apa pun)

### INT-1 [BLOCKER] Tabel 4 & 5 adalah keluaran simulasi, dilaporkan sebagai "uji konkurensi empiris"

**Klaim naskah:** §2.5 poin 2, §3.3, Tabel 4–5, abstrak ("Uji beban konkurensi pada CPU 8-thread lokal membuktikan…"), Kesimpulan ("Pengujian konkurensi empiris membuktikan…").

**Bukti:**
- `evals/benchmark_concurrency_ollama.py:523` menulis `Mode Eksekusi: 'Ollama Live Server' if is_live else 'Validated CPU Queuing Benchmark'`.
- `apps/BENCHMARK_CONCURRENCY_REPORT.md` (11 Nov 10:42:47) tertulis **`Mode Eksekusi: Validated CPU Queuing Benchmark`**, artinya `is_live == False`.
- `apps/benchmark_concurrency_results.json` ditulis pada run yang sama (10:42:47.758 vs .760).
- Fungsi `simulate_cpu_concurrency_latency()` (baris ~276–306) menghasilkan latensi = `normal(1.75, 0.18)` × faktor `{1; 1,45; 2,70; 4,90}`. Nilai harapan: 1,75 / 2,54 / 4,73 / 8,58 s. **Tabel 4:** 1,74 / 2,64 / 4,74 / 8,90 s. Cocok.
- Pada mode simulasi, "CPU" yang diukur adalah *busy-loop* `math.sqrt(random())` milik Python sendiri. "RAM" adalah `psutil.virtual_memory().used` **seluruh sistem**, bukan proses Ollama. Inilah penjelasan angka ~4,3 GB (M4 di review) dan ΔRAM yang tidak monoton.
- `response_length = random.randint(180, 260)`. Klaim "keluaran ~45–55 token" dan "laju ~28–32 token/detik" (Tabel 5) tidak ada dalam data apa pun.
- Fungsi simulasi menyebut "saturasi bandwidth memori DDR4" sebagai **asumsi parameter**. Naskah §3.3 menyajikannya sebagai **temuan** penyebab degradasi.

**Konsekuensi:** Tabel 4, Tabel 5, angka abstrak (1,74 s; 2,64 s; 83,3%; dst.), Tabel 6 baris Ollama, argumen "k = 2 optimal", dan seluruh analisis Poisson §3.3 kehilangan dasar empiris.

**Tindakan:** jalankan ulang dengan Ollama hidup. Ubah skrip agar **gagal keras** (bukan beralih diam-diam ke simulasi) bila Ollama mati, dan catat `is_live`, versi Ollama, model digest, `eval_count/eval_duration` per permintaan ke JSON. Sambil melakukannya, terapkan protokol M1–M3 review: ≥ 5 ulangan, ≥ 100 permintaan/kondisi, warm-up, k = 3, timeout 3,0 s sungguhan. Jika tidak sempat, **hapus** Tabel 4–5 dan semua klaim turunannya.

### INT-2 [BLOCKER] Tabel 2 tidak punya sumber yang dapat direproduksi

- Tidak ada skrip yang menjalankan "10.000 iterasi" (§2.5 poin 1). Grep `10000|10_000|0,18 ms|12,30` di seluruh repo: nihil.
- Satu-satunya pengukuran latensi L3 yang ada (`evals/e5_latency_usability.py`, 2.000 iterasi) mencatat **L3 p95 = 0,0008 ms dan fallback = 0,0009 ms** (`evaluation_report.json`). `docs/05` menulis 0,42 ms dan 3,8 ms. Tabel 2 menulis 0,18/0,42 ms dan 12,30/18,50 ms. Tiga sumber, tiga angka berbeda.
- Baris "L1/L2 Item Search — pencarian semantik 5 butir termirip 4,20 ms" mengukur fitur yang **tidak ada** (lihat INT-4).
- Fallback statis di kode hanyalah `dict.get()` (`hint_service.py:38-48`), mustahil memakan 12,3 ms kecuali termasuk panggilan HTTP yang gagal.

**Tindakan:** buat satu skrip benchmark L3 dan fallback yang dikomit, catat hasil mentah, dan isi Tabel 2 hanya dari skrip itu. Hapus baris pencarian semantik.

### INT-3 [BLOCKER] Klaim "180 butir soal dua tingkat (two-tier)" tidak sesuai produk

**Klaim naskah:** judul tabel, abstrak, §2.1, §2.3 ("r = 1 apabila jawaban teknis (Tingkat 1) dan alasan penalaran (Tingkat 2) keduanya benar"), Gambar 4 caption, Kesimpulan.

**Bukti:**
- `data/l2_item_bank/items_adaptive_180.json`: 180 butir, masing-masing tepat **4 opsi dan 1 `correct_answer`**. Tidak ada field tingkat alasan. Kunci yang ada: `id, sequence_id, primary_kc, secondary_kc, difficulty, tolt_dimension, is_calibration, prompt_text, options, correct_answer, explanation, jonassen_phase, jonassen_label, framework_source`.
- `schemas/quiz.py`: `SubmitAnswerRequest.choice` = satu huruf (`max_length=1`).
- `routers/student_quiz.py:306`: `is_correct = (req.choice == item.correct_answer)`.

**Konsekuensi:** temuan D4 review (hilangnya informasi dua-tier) ternyata lebih parah: tidak ada two-tier sama sekali. Field `jonassen_phase` / "Jonassen & Hung (2006)" di setiap butir juga tidak pernah disebut di naskah.

**Tindakan:** pilih salah satu. (a) Implementasikan tier-2 (data, skema, UI, aturan skor). (b) Ubah naskah menjadi "pilihan ganda empat opsi" di semua tempat dan hapus argumen dua-tier.

### INT-4 [BLOCKER] Lapisan 2 "Indeks Semantik `pgvector`" tidak ada

**Klaim naskah:** abstrak, Gambar 1, §2.1 poin 2, §2.5 ("PostgreSQL 16 (`pgvector` pada korpus N = 180)"), Tabel 2, Kesimpulan.

**Bukti:** grep `pgvector|embedding|vector|cosine|similarity` di `backend/`, `frontend/`, `evals/`, `tests/` hanya menemukan **satu komentar** di `db/database.py:3`. Tidak ada kolom vektor di `models.py`, tidak ada model embedding, dan tidak ada query kemiripan. `DATABASE_URL` bawaan dan di `.env` adalah **SQLite** (`aiosqlite`). `requirements.txt` tidak memuat `pgvector`.

**Tindakan:** hapus seluruh klaim pgvector/indeks semantik/PostgreSQL, atau implementasikan dan ukur. Konsekuensinya, "Arsitektur Tiga Lapis" perlu didefinisikan ulang karena L2 hanya berisi bank soal JSON.

### INT-5 [BLOCKER] Data evaluasi E1–E6 dan `docs/05` dihasilkan RNG tetapi disajikan sebagai empiris

- `e1_content_validity.py:90-109`: rating pakar = `np.random.choice([5,4,3], p=[0.88,…])`, label AI 92% cocok via `np.random.random()`.
- `e2_socratic_quality.py:116`: skor penilai = `np.random.choice([4.2,…,5.0])`.
- `e5_latency_usability.py:146-154`: **SUS 34 siswa dibangkitkan** ("Generates realistic positive responses").
- `e6_learning_impact.py:61-110`: pre/post-test, N-Gain, dosis, dan NEDV dibangkitkan dari distribusi normal/binomial.
- `e4_llm_reliability.py:51`: `mock_deterministic_llm` bila Ollama mati.
- `evaluation_report.json`: "ALL PASSED", SUS = 87,13, N-Gain = 0,4786, d_z = 4,89.
- `docs/05_HASIL_EVALUASI_EMPIRIS_E1_E6.md` menulis "**Validasi ahli oleh 5 pakar (3 dosen … dan 2 guru …)**", SUS = 82,4, Gain = 0,58, p = 0,0004. Angka ini bahkan berbeda dari `evaluation_report.json`.

Naskah tidak mengutip E1–E6, jadi teks naskah aman. Namun §Ketersediaan Data menjanjikan repositori publik, dan `docs/` disajikan oleh aplikasi di `/documentation`. Dokumen yang mengklaim validasi 5 pakar dan SUS 34 siswa, padahal penelitian ini menyatakan tidak melibatkan manusia, adalah risiko integritas serius. Grep juga menemukan angka sejenis di `proposal/proposal_skripsi_bab_1_2_3.md`, `proposal/rangkuman_skripsi_fajari_logitrace.md`, `PRD`, dan `desain-final`; periksa apakah itu ditulis sebagai rencana atau sebagai hasil.

**Tindakan:** hapus E1–E6 dan `docs/05` dari repositori publik, atau beri label jelas di judul file dan di setiap angka: "DATA SIMULASI — bukan hasil penelitian". Jangan pernah mengutipnya di skripsi/artikel sebagai hasil.

### INT-6 [MAJOR] Tidak ada jejak keluaran LLM; kolom dinamis Tabel 7 tanpa provenance

`agent_logs` di kedua DB: T2 = `static_bank` (2 dan 35 baris), T3 = `deterministic_t3_engine` (4 dan 42 baris), dan **0 baris** keluaran LLM. Teks dinamis Tabel 7 (mis. "link budget") tidak ditemukan di log mana pun. Gambar 5b ("Modal Ringkasan AI Agen T3") kemungkinan besar menampilkan narasi templat deterministik, bukan keluaran AI.

**Tindakan:** bangkitkan ulang contoh Tabel 7 melalui `HintService` dengan provider yang dicatat, simpan log mentah (model, waktu, prompt, keluaran), dan sebutkan model per baris (P4 review). Ubah caption Gambar 5b bila memang templat.

### INT-7 [MAJOR] Pernyataan penggunaan AI tidak akurat

Naskah menyatakan AI hanya dipakai untuk kerangka pytest, tata bahasa abstrak, dan format tabel. Namun `brief_development_logitrace_benchmarking.md` adalah brief kepada "sesi AI development" untuk **membuat skrip benchmark dan tabel siap salin ke Bab 3**. Laporan yang dihasilkan juga menulis analisis "untuk Naskah Jurnal". Perluas pernyataan tersebut sesuai kenyataan (pembuatan kode aplikasi, skrip evaluasi, draf analisis).

---

## 3. Klaim Naskah vs Implementasi (temuan baru dari kode)

| # | Klaim naskah (lokasi) | Kenyataan di kode | Sev. |
|---|---|---|---|
| C1 | Agen T1 = "Semantic Item Labeler", orkestrasi Tri-Agen (§1, §2.4, Tabel 9) | `labeling_service.py`: murni pencocokan kata kunci + aturan if/else. `llm_client` dibuat tetapi **tidak pernah dipanggil**. Bukan agen dan bukan semantik. | Major |
| C2 | Butir dengan keyakinan < 0,60 ditahan di *Teacher Review Queue* (§2.4) | `teacher_ambient.py` `/items/review-queue` hanya mengembalikan 10 butir terbaru dengan **confidence hard-coded 0,92/0,85**. Hasil `/items/label` tidak dimasukkan ke bank maupun antrean. Alur human-in-the-loop tidak tersambung. | Major |
| C3 | T3 memakai "algoritma *Bipartite Matching* berpelindung anti-self-pairing", memasangkan tutor dengan maksimal 2 mentee (§2.4, §3.6) | `summary_service.py:146-189`: greedy. Hanya untuk 3 KC terlemah, 1 tutor terbaik + ≤ 2 mentee per KC, sehingga **maksimal 3 pasangan untuk 34 siswa**. Tutor yang sama bisa muncul di beberapa KC. Bukan bipartite matching. | Major |
| C4 | Ambang tutor m ≥ 0,70, mentee ≤ 0,45 (§3.6); "0,65–0,70" (§2.4) | Kode: tutor **≥ 0,65**, mentee ≤ 0,45. | Minor |
| C5 | Peer-tutoring "terukur" | Mastery KC yang belum pernah diukur diisi **0,25 bawaan** atau **diwarisi rata-rata induk** (`calibration.estimate_unmeasured_kcs`, `student_quiz.py:367-390`). Akibatnya siswa yang **belum mengerjakan apa pun** (m = 0,25 ≤ 0,45) bisa direkomendasikan sebagai mentee, dan tutor bisa dipilih berdasarkan nilai warisan tanpa bukti. | Major |
| C6 | Narasi T3 = refleksi kelas | Templat fallback (`summary_service.py:286-297`) **selalu** menulis "pemahaman yang sangat kokoh… mayoritas siswa mencapai zona kemahiran mandiri" dan "Analisis galat menunjukkan adanya miskonsepsi", **apa pun datanya** (termasuk rerata 0,25). Templat ini menyesatkan guru. | Major |
| C7 | Payload T3 memuat kode siswa & identitas rombel sehingga butuh `PIIScrubber` (§2.4 Layer 1) | Prompt T3 (`summary_service.py:261-268`) hanya berisi judul sesi, rombel, statistik agregat, dan nama KC, **tanpa kode siswa**. Prompt T2 hanya berisi topik, deskripsi KC, level, dan teks soal. PII tidak masuk payload karena rancangan (mendukung P1 review). Klaim risiko di §2.4 keliru. | Minor |
| C8 | `AnswerLeakageGuard` memeriksa substring kunci **dan teks opsi** ≥ 4 karakter (§2.4 Layer 4) | `guardrails.py:33-71`: parameter `options` **diabaikan**. Hanya kunci benar yang dicek, dengan ambang **> 2** karakter. | Major |
| C9 | Fallback statis bebas bocor; "0% kebocoran" | Fallback tidak melewati guard dan selalu `is_safe=True` (`hint_service.py:91-93`). Uji 36 petunjuk × 180 butir dengan guard milik sendiri: **3 pasangan gagal** (mis. `ITEM_ICMP_CONNECTIVITY_1_01` level 1 & 3 menyebut "ping" = kunci; `ITEM_ICMP_TROUBLE_DHU_2_04` level 1 menyebut kunci "Destination Host Unreachable"). | Major |
| C10 | `PIIScrubber` menyensor nama (`Budi`) 100% (Tabel 8) | Tidak ada pola nama. `"Nama saya Budi Santoso"` lolos utuh. Tes tidak meng-assert "Budi". Lolos juga: `"SMKN 4 Bandung"`, NISN berspasi `"0061 2345 67"`, alamat. `"SMK Negeri 4 Kota Bandung"` → `[REDACTED_SCHOOL] Bandung` (bocor sebagian). | Major |
| C11 | Scrubber tidak merusak konten | False positive: angka teknis 10 digit (`1300000000 bps`) → `[REDACTED_NISN]`; `S11` → `[REDACTED_ID]`. Teks soal yang dikirim ke LLM bisa rusak. | Minor |
| C12 | Soket diputus tegas pada 3,0 s; "siswa tidak pernah menunggu lebih dari 3,05 detik" (§3.3) | `httpx.AsyncClient(timeout=3.0)` menetapkan 3 s **per fase** (connect, read, write, pool), bukan batas total. Waktu tunggu terburuk bisa > 3 s. Tidak ada `asyncio.wait_for`. Klaim 3,05 s tidak dijamin kode dan tidak pernah diukur (M1 review). | Major |
| C13 | Peluruhan Ebbinghaus *on-read* diterapkan (§2.3, Gambar 1, Tabel 8) | `apply_temporal_decay()` **tidak dipanggil di mana pun** selain tes. Fitur ini tidak aktif di aplikasi. | Major |
| C14 | "Simpul anak terkunci rapat selama induk < 0,60" (Tabel 8); pita ZPD [0,60; 0,85] wajib (§2.3) | `zpd_selector.py:96-99`: bila tak ada butir yang lolos prasyarat, gating **dilewati** (`eligible = unanswered`). Baris 120-130: bila pita ZPD kosong, butir di luar pita dipilih (*relaxation*). `student_quiz.py:204-209`: fallback ke butir apa saja. Pada m = 0,25, p̂ = 0,451/0,25/0,119, sehingga pita ZPD **selalu kosong** di awal dan yang berjalan adalah relaxation. Perilaku ini tidak dijelaskan di naskah (memperkuat D2 review). | Major |
| C15 | Kalibrasi 6 butir pada "simpul akar" (§2.3) | `dag_prerequisites.json` mencantumkan `roots` = 3 KC, tetapi `in_degrees` dan `edges` membuat **hanya WLAN_STANDARDS** yang akar (ada edge 01→02 dan 02→03). `kcs.json` menyatakan KC-02 dan KC-03 sebagai root tanpa prasyarat. Tiga sumber DAG saling bertentangan. | Major |
| C16 | Gambar 2 = DAG yang dipakai | Gambar 2 memuat **14 sisi**, kode memuat **13**. Edge KC-04→KC-07 (FREQ_CHANNEL→SIGNAL_PROP) ada di gambar tetapi tidak di kode. | Minor |
| C17 | Pewarisan estimasi klaster DAG (hanya disebut di Tabel 8) | Setiap submit menimpa mastery KC tak-terukur dengan rata-rata induk langsung (`confidence="low"`). Nilai ini memengaruhi p̂ butir anak, heatmap guru, dan peer-tutoring, tetapi tidak dijelaskan di Metode (D10 review). | Major |
| C18 | Tabel 1: satu dimensi TOLT per KC | Data: dimensi TOLT ditetapkan **per butir** dan bercampur di setiap KC. Contoh: WLAN_STANDARDS memuat kelima dimensi, padahal Tabel 1 menulis *Correlational*. Mesin L3 tidak memakai TOLT sama sekali. | Major |
| C19 | h = 0,5 bila siswa membuka petunjuk | `used_hint` dan `hint_level` dikirim **oleh klien** (`frontend/student/app.js:593-594`) dan tidak dicocokkan dengan log `/hint` di server. Siswa dapat memalsukan h = 1,0. | Minor |
| C20 | Prompt T2 hanya berisi nama KC, level, dan teks soal (§3.4) | Prompt juga memuat `Konsep L1: {kc_description}` (`secure_client.py:237`). Naskah merujuk "baris 236–241"; isi sebenarnya ada di 231–244. | Minor |
| C21 | `max_tokens = 120` (§2.4) / `MAX_TOKENS = 150` (§2.5) | Keduanya benar di tempat masing-masing: produksi 120, benchmark 150. Artinya benchmark tidak mengukur konfigurasi produksi. | Minor |
| C22 | 41 unit test lulus; rincian per modul di Tabel 8 | `pytest` hari ini: **44 passed** (29,97 s). Per modul: calibration **4** (naskah 3), item_bank **9** (naskah 8), backend_api **11** (naskah 10). Sisanya cocok. | Minor |
| C23 | 9 skenario uji otomatis Playwright; artefak Playwright ada di repo (§2.5 poin 4, §Ketersediaan Data) | Tidak ada skrip Playwright, `.spec`, atau konfigurasi di seluruh folder skripsi. Yang ada hanya 11 PNG di `apps/screenshots/`. Klaim "pengujian otomatis" dan "tanpa regresi visual" tidak dapat diverifikasi (memperkuat M10 review). | Major |
| C24 | Repositori `github.com/fajari-arkan/logitrace-core` | Remote git lokal adalah `github.com/fajar-i/skripsi` (repo skripsi gabungan). Pastikan URL di naskah benar-benar ada dan berisi kode ini. | Minor |
| C25 | PostgreSQL 16 + SQLAlchemy Async (§2.5) | SQLite di `.env`, `.env.example`, dan bawaan. Tidak ada bukti uji di PostgreSQL. | Minor |
| C26 | Tabel 2: fallback T3 < 10 ms | Fallback T3 baru berjalan **setelah** panggilan LLM gagal (hingga 5 s per fase). Latensi yang dirasakan guru = timeout + templat. | Minor |

---

## 4. Status Temuan Review 16 Nov

Naskah belum diubah setelah review, jadi **semua temuan berstatus terbuka**. Kolom terakhir menunjukkan efek bukti kode.

| ID review | Ringkas | Status | Catatan audit |
|---|---|---|---|
| EIC-1 | Klaim melampaui bukti | Terbuka | **Diperberat** INT-1…INT-4 |
| EIC-2..6 | DSR knowledge, judul, format, anonimitas, istilah Station Rotation | Terbuka | Placeholder pembimbing/email masih ada |
| M1 | Fallback tak dieksekusi; SLA pasca-ukur | Terbuka | **Diperberat**: bahkan Ollama tidak jalan (INT-1); C12 timeout per-fase |
| M2 | Statistik n kecil, p95, CI | Terbuka | Lebih mendasar: datanya simulasi |
| M3 | Konfigurasi Ollama tak dilaporkan | Terbuka | Tidak ada karena Ollama tidak berjalan |
| M4 | RAM/CPU ambigu | Terbuka | **Dijelaskan**: `virtual_memory().used` seluruh sistem + busy-loop Python |
| M5 | Latensi cloud tanpa metode | Terbuka | Tak ada pengukuran cloud di repo |
| M6 | Inkonsistensi parameter | Terbuka | + C4, C21, C22 |
| M7 | Poisson tak sahih | Terbuka | Juga bergantung pada data simulasi |
| M8 | Tak ada uji end-to-end beban | Terbuka | — |
| M9 | DSR 5 vs 6 tahap | Terbuka | — |
| M10 | Playwright ≠ visual regression | Terbuka | **Diperberat** C23: skrip Playwright tidak ada |
| M11 | Reprodusibilitas | Terbuka | + INT-2 |
| D1 | Validitas model kognitif tak diuji | Terbuka | `e3_predictive_accuracy.py` memakai siswa sintetis dari RNG dan estimasi = truth + noise, sehingga tidak bisa dipakai sebagai validasi |
| D2 | Tabel 3 salah (α₀ = 0,40 mandiri) & ZPD | Terbuka | **Dikonfirmasi** dengan fungsi asli: (1 butir, m = 0,670). Pita ZPD kosong pada m < 0,379 → relaxation (C14) |
| D3 | 2 jawaban benar → kandidat tutor | Terbuka | Di kode ambang 0,65 sehingga lebih longgar; + C5 |
| D4 | Info two-tier hilang | Terbuka | **Diperberat**: tidak ada two-tier (INT-3) |
| D5 | Peluruhan Ebbinghaus | Terbuka | **Diperberat**: fungsi tak dipanggil (C13) |
| D6 | KC–TOLT & DAG tak divalidasi | Terbuka | + C15, C16, C18 |
| D7 | Bank soal tanpa proses | Terbuka | Generator `generate_curated_bank.py` + blueprint menunjukkan butir dibuat dari templat skrip; dokumentasikan siapa penyusunnya |
| D8 | "RAG"/"Agen" berlebihan | Terbuka | **Diperberat**: tidak ada retrieval (INT-4), T1 tanpa LLM (C1) |
| D9 | Sitasi tak mendukung | Terbuka | DOI Komalasari & Nurbaeti (404) masih ada di naskah |
| D10 | Ambang tak seragam; kalibrasi | Terbuka | + C17 |
| P1 | Zero-PII ≠ patuh UU PDP | Terbuka | **Dikonfirmasi** C10 (nama lolos), C7 (payload memang minim PII) |
| P2 | 5 lapis campur keamanan/keandalan | Terbuka | `verify=True` tak berarti untuk `http://localhost` (9router, Ollama) |
| P3 | Kebocoran jawaban | Terbuka | **Dikonfirmasi** C8, C9 (3 pasangan bocor) |
| P4 | Evaluasi pedagogis tak ada | Terbuka | + INT-6 |
| P5 | Data Gambar 4–5 sintetis | Terbuka | DB berisi `std_01…`, 38/82 siswa seed; nyatakan sintetis |
| P6 | Kebergunaan tak dievaluasi | Terbuka | Jangan memakai SUS dari E5 (INT-5) |
| P7 | Representativitas perangkat | Terbuka | — |
| DA-1..3 | Nilai tambah LLM runtime; mesin kognitif; zero outage tautologis | Terbuka | DA-1 **diperkuat** INT-6: dalam praktik aplikasi selama ini 100% berjalan dengan petunjuk statis |

---

## 5. Keamanan Produk

Bagian ini relevan karena naskah mengklaim "siap diimplementasikan".

| # | Temuan | Bukti | Tindakan |
|---|---|---|---|
| S1 | **Kunci API ter-commit** | `apps/logitrace/.env` dilacak git sejak commit `5ddd3f5 init`. `NINEROUTER_API_KEY` panjang 35 karakter, bukan placeholder. Remote: GitHub. | **Rotasi kunci sekarang**, hapus `.env` dari indeks (`git rm --cached`), tambahkan `.gitignore`, dan bersihkan riwayat bila repo pernah/akan publik |
| S2 | Tanpa autentikasi | Semua endpoint guru terbuka: reset sesi, reset siswa, approve label, export audit log, ringkasan. `/api/quiz/submit` menerima `student_code` apa pun (mudah ditebak: `std_01`…). | Minimal token guru + PIN/sesi siswa sebelum uji lapangan |
| S3 | CORS `*` | `main.py:50-56` | Batasi ke origin LAN |
| S4 | DB dev ter-commit | `logitrace_dev.db` dilacak git | Pastikan tak ada data siswa nyata; keluarkan dari repo |
| S5 | Prompt injection | Hanya pemotongan 1.000 karakter | Sudah dicatat P2 |

---

## 6. Rekomendasi — Urutan Pengerjaan

**Tahap 0 — Integritas (tanpa ini, jangan submit)**
1. S1: rotasi kunci, keluarkan `.env` dari git.
2. INT-5: beri label "SIMULASI" atau hapus E1–E6, `evaluation_report.json`, dan `docs/05` dari repo publik. Cek proposal/rangkuman agar tidak ada angka E1–E6 yang ditulis sebagai hasil.
3. INT-1: jalankan benchmark dengan Ollama hidup (skrip gagal keras bila offline; catat `is_live`) atau hapus Tabel 4–5 dan semua klaim turunannya (abstrak, §3.3, Poisson, Tabel 6, Kesimpulan).
4. INT-2: buat skrip Tabel 2 yang dikomit; isi ulang tabel dari keluarannya.
5. INT-3, INT-4: putuskan "implementasikan" vs "hapus klaim" untuk two-tier dan pgvector. Untuk tenggat dekat, **hapus klaim** lebih realistis; judul dan arsitektur "tiga lapis/RAG-KT" ikut berubah (sejalan dengan D8 review).
6. INT-6, INT-7: log keluaran LLM nyata untuk Tabel 7 dan perbaiki pernyataan penggunaan AI.

**Tahap 1 — Selaraskan kode dan naskah** (pilih untuk setiap butir: perbaiki kode atau perbaiki teks)
7. C8, C9: guard memeriksa opsi (≥ 4 karakter) dan fallback statis ikut melewati guard; perbaiki 3 petunjuk yang bocor.
8. C10, C11: tambah pola NISN berspasi, "SMKN", dan nama (atau hapus klaim nama); kurangi false positive; buat korpus uji PII berlabel (P1 review).
9. C12: bungkus dengan `asyncio.wait_for(…, 3.0)` lalu ukur latensi fallback nyata.
10. C13: aktifkan peluruhan saat baca, atau hapus dari naskah.
11. C14–C17: dokumentasikan relaxation & bypass gating di §2.3 (atau ubah kode); satukan tiga sumber DAG; samakan Gambar 2 dengan kode; jelaskan pewarisan klaster.
12. C1–C6: ganti istilah "Agen T1" dan "Bipartite Matching"; perbaiki antrean review; kecualikan siswa yang belum mulai dan nilai low-confidence dari peer-tutoring; templat T3 harus berbasis data.
13. C18: tentukan TOLT per KC atau per butir dan samakan Tabel 1 dengan data.
14. C22, C23: perbarui jumlah tes (44) atau sebutkan commit hash tempat 41 diambil; tambahkan skrip Playwright beserta assertion-nya, atau ubah klaim menjadi "tangkapan layar alur manual".

**Tahap 2 — Roadmap review 16 Nov** (P0 #1, #2, #4–#7; P1; P2) tetap berlaku setelah Tahap 0–1.

**Arah reframing yang paling jujur dan masih bisa terbit:** "Rancangan dan studi kelayakan teknis sistem asesmen formatif adaptif berbasis aturan dengan petunjuk LLM opsional dan fallback statis." Klaimnya terbatas pada yang benar-benar diukur ulang. Tambahkan studi simulasi validitas L3 vs BKT/Elo (D1) yang **dilaporkan terbuka sebagai simulasi**.

---

## Lampiran A — Bukti Perintah

```text
pytest (apps/logitrace):        44 passed, 1 warning in 29.97s   (Python 3.13.14, pytest 9.2.0)
pytest --collect-only per file: backend_api 11, calibration 4, cognitive_engine 7,
                                guardrails 4, item_bank 9, secure_client 6, zpd_selector 3

BENCHMARK_CONCURRENCY_REPORT.md:  "Mode Eksekusi: Validated CPU Queuing Benchmark"  (= is_live False)
Expected sim means (1.75 × {1,1.45,2.70,4.90}): 1.75 / 2.54 / 4.73 / 8.58 s
Reported Tabel 4 means:                          1.74 / 2.64 / 4.74 / 8.90 s

Tabel 3 recompute (fungsi asli update_mastery, d=2, m0=0.25 → ≥0.60):
  α0  berbantuan(h=.5)   mandiri(h=1)
  0.1 (9, 0.610)         (5, 0.647)
  0.2 (5, 0.647)         (2, 0.611)
  0.3 (3, 0.630)         (2, 0.748)
  0.4 (2, 0.611)         (1, 0.670)   ← naskah: 2 butir, 0.855 (salah)
  0.5 (2, 0.683)         (1, 0.775)
p̂ pada m=0.25: d1=0.451, d2=0.250, d3=0.119 → tak ada butir di pita [0.60, 0.85]

agent_logs:  logitrace.db      T1 2, T1_REVIEW 2, T2 static_bank 2,  T3 deterministic 4
             logitrace_dev.db  T1 17, T1_REVIEW 17, T2 static_bank 35, T3 deterministic 42
             → 0 keluaran LLM

PIIScrubber:
  'Nama saya Budi Santoso'      -> tidak berubah
  'NISN: 0061 2345 67'          -> tidak berubah
  'SMKN 4 Bandung'              -> tidak berubah
  'SMK Negeri 4 Kota Bandung'   -> '[REDACTED_SCHOOL] Bandung'
  'Throughput 1300000000 bps'   -> 'Throughput [REDACTED_NISN] bps'   (false positive)

AnswerLeakageGuard pada 36 petunjuk statis × 180 butir: 3 pasangan ditolak guard
  ITEM_ICMP_CONNECTIVITY_1_01 L1, L3 ('ping'); ITEM_ICMP_TROUBLE_DHU_2_04 L1

git ls-files: apps/logitrace/.env, .env.example, logitrace_dev.db terlacak; .env sejak commit 5ddd3f5
```

## Lampiran B — Yang Tidak Diverifikasi

- Repositori `github.com/fajari-arkan/logitrace-core` (tidak dibuka).
- Perilaku 9router/Ollama/DeepSeek/Groq secara langsung (tidak tersedia di mesin audit).
- DOI referensi: mengikuti hasil Crossref di review 16 Nov (13/15 valid, 2 gagal 404).
- Isi visual 11 tangkapan layar.
- Apakah kunci di `.env` masih aktif.
