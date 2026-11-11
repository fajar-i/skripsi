# Panduan Penyusunan SLR Valid & Kokoh untuk Skripsi Rancang Bangun Media Pembelajaran PBO

Dokumen ini disusun untuk membantu Anda sebagai **penulis tunggal (solo writer)** dalam merancang *Systematic Literature Review* (SLR) yang valid, bereputasi, dan bebas dari cacat metodologis. Panduan ini merefleksikan seluruh pembelajaran kritis dari proses revisi naskah yang baru saja kita lalui.

---

## 1. PETA JALAN METODOLOGI (SLR FRAMEWORK)

Topik skripsi Anda adalah **Rancang Bangun (RnD) Media Pembelajaran PBO** dengan mengukur **Kompetensi Berpikir Siswa (Logical/Critical/Computational Thinking)**. SLR Anda harus diarahkan untuk menjawab celah penelitian (*research gap*) di area tersebut.

### A. Perumusan Questions (Research Questions - RQ)
Gunakan kerangka **PICOC** (Population, Intervention, Comparison, Outcome, Context) untuk merancang RQ:
*   **RQ1 (Metodologis):** Model pembelajaran dan media interaktif apa saja yang sudah divalidasi dalam literatur untuk mengajarkan konsep PBO (misal: enkapsulasi, pewarisan, polimorfisme)?
*   **RQ2 (Teknologis):** Fitur teknis dan arsitektur media pembelajaran (seperti *game-based learning*, *visual programming*, atau *automated grading*) apa yang paling efektif dalam meminimalkan kesulitan belajar mahasiswa/siswa?
*   **RQ3 (Pedagogis):** Bagaimana literatur mengukur peningkatan kemampuan berpikir kritis, logis, atau *computational thinking* siswa dalam konteks PBO?
*   **RQ4 (Research Gap):** Apa celah metodologis dan praktis dalam rancang bangun media PBO yang masih belum diteliti secara komprehensif di Indonesia?

### B. Rumus Pembobotan Relevansi (Relevance Score - $S$)
Hindari pengali linear yang redundan (belajar dari revisi Rumus $S$ sebelumnya). Buat formula pembobotan relevansi yang sederhana, transparan, dan dapat direplikasi:

$$S = S_{\text{domain}} + S_{\text{method}} + S_{\text{outcome}}$$

Skala maksimal $S = 10,0$:
1.  **Skor Domain ($S_{\text{domain}}$ - Maks 4,0):** Kemunculan kata kunci PBO/OOP (+2,0) dan Media Pembelajaran/RnD (+2,0) pada judul/abstrak.
2.  **Skor Metode ($S_{\text{method}}$ - Maks 3,0):** Menyebutkan secara eksplisit model pembelajaran (seperti PjBL, PBL, Discovery) (+1,5) dan desain evaluasi empiris (+1,5).
3.  **Skor Kompetensi ($S_{\text{outcome}}$ - Maks 3,0):** Menyebutkan pengukuran salah satu kemampuan berpikir (Critical/Logical/Computational Thinking) (+3,0).

---

## 2. TRAPS TO AVOID (JEBAKAN METODOLOGIS PENULIS TUNGGAL)

Sebagai *solo writer*, Anda tidak memiliki *second screener* (penilai kedua) untuk melakukan verifikasi seleksi naskah. Hal ini adalah titik paling rentan yang sering diserang oleh penguji skripsi atau reviewer jurnal.

| # | Jebakan Metodologis (Trap) | Mengapa Berbahaya? | Solusi & Strategi Penyelamatan (Refleksi Revisi Kita) |
|---|---|---|---|
| **1** | **Paywall Attrition vs. Sampling Bias** | Membatasi pencarian hanya pada *Gold Open Access* (karena gratis) akan mengeksklusi jurnal pendidikan komputer terbaik dunia (seperti *Computers & Education*, *IEEE Transactions on Education*, *ACM TOCE*) yang sebagian besar hibrida/berbayar. | Jika kampus Anda tidak memiliki langganan, Anda harus **secara eksplisit** membatasi judul dan keterbatasan penelitian Anda. Gunakan judul: *"Tinjauan Literatur Sistematis Akses Terbuka..."* dan akui *selection bias* ini secara transparan di bab keterbatasan. |
| **2** | **"False Consensus" Screening** | Melakukan screening kelayakan sendirian tanpa adanya pengukuran keandalan penilai (*inter-rater reliability*). Penguji akan menganggap seleksi Anda sangat subjektif. | **Gunakan Metode AI-Assisted Co-Screener (Akurasi Terlacak):**<br>Lakukan screening manual pada 10% sampel artikel. Gunakan AI (Gemini/Claude) sebagai screener kedua menggunakan prompt kriteria inklusi yang ketat. Hitung nilai *Cohen's Kappa* (indeks kesepakatan) antara Anda dan AI. Jika Kappa > 0.80, Anda memiliki justifikasi objektif bahwa proses screening Anda konsisten dan dapat direproduksi. |
| **3** | **Inkonsistensi Kuota Korpus ("Top-N")** | Menyatakan aturan mengambil "Top-3" per domain, namun jumlah artikel aktual di tabel akhir tidak seimbang (seperti kasus 4, 4, 3, 3, 1 kita sebelumnya). | Jika terjadi nilai relevansi yang kembar (*tie scores*) pada peringkat batas akhir, buat aturan tertulis di metodologi: *"Jika ada nilai Relevance Score kembar di peringkat ke-3, kedua naskah diinklusi."* Jika ada domain yang kekurangan naskah, jelaskan batas pencarian riilnya. |
| **4** | **Subjektivitas Penilaian Kualitas (JBI Appraisal)** | Mengubah instrumen standar (JBI Critical Appraisal) menjadi skala angka (0-2) tanpa definisi operasional dan justifikasi ilmiah. | Tuliskan **definisi operasional rubrik** secara kuantitatif. Rujuk metodologi konversi skala yang valid (sitir *Barker et al., 2023*) untuk membenarkan penggunaan skala ordinal 0, 1, dan 2 dalam pemeringkatan kualitas naskah Anda. |
| **5** | **Overclaiming Model TAM / Jalur Konseptual** | Menggambar kerangka media pembelajaran baru namun menyajikan alur hubungan tanpa membedakan mana yang merupakan temuan empiris literatur dan mana yang teoretis/usulan Anda sendiri. | Pada diagram model konseptual Anda, bedakan secara visual: gunakan **garis tegas** untuk hubungan yang sudah terbukti empiris dalam korpus, dan **garis putus-putus** untuk hipotesis/usulan RnD media Anda sendiri. |
| **6** | **Positive Outcome Bias (Bias Sukses)** | Korpus penelitian media pembelajaran hampir 99% melaporkan keberhasilan peningkatan kompetensi siswa. Literatur jarang menerbitkan media pembelajaran yang gagal. | Di bagian Diskusi, tambahkan analisis kritis: ingatkan pembaca bahwa realitas implementasi di kelas sering kali berbeda karena faktor luar (kesiapan guru, spesifikasi gawai siswa, atau stabilitas internet) yang sering disembunyikan oleh bias hasil positif di jurnal ilmiah. |
| **7** | **Abstraksi Konseptual Tanpa Lokalisasi** | Menganalisis model pembelajaran global tanpa mengaitkannya dengan kondisi nyata di sekolah Indonesia. | Lokalisasikan diskusi Anda dengan kurikulum nasional (**Kurikulum Merdeka**), infrastruktur sekolah di Indonesia (keterbatasan laboratorium komputer), dan karakteristik literasi digital siswa lokal (penggunaan smartphone vs laptop untuk praktik PBO). |
| **8** | **Diagram Mermaid Non-Printable** | Menyajikan diagram alir PRISMA atau model TAM menggunakan kode Mermaid di dalam naskah final skripsi. | Sistem kompilasi skripsi/jurnal tidak mendukung rendering Mermaid otomatis. Selalu ekspor diagram Mermaid Anda menjadi file gambar statis PNG beresolusi minimal 300 DPI dengan label gambar standar. |

---

## 3. RENCANA TINDAKAN (ACTION PLAN) UNTUK SKRIPSI ANDA

Berikut adalah langkah konkret yang harus Anda lakukan dalam 4 minggu pertama:

### Minggu 1: Konstruksi Protokol & String Pencarian
*   Rancang kueri Boolean terstruktur untuk Scopus/Google Scholar. Contoh:
    `("OOP" OR "Object-Oriented Programming" OR "Pemrograman Berorientasi Objek") AND ("learning media" OR "media pembelajaran" OR "educational game") AND ("computational thinking" OR "critical thinking" OR "logis")`
*   Tulis protokol inklusi/eksklusi di dokumen draf Anda sebelum mulai mengunduh artikel (*a priori pre-registration*).

### Minggu 2: Penapisan & Pengukuran Reliabilitas
*   Unduh metadata pencarian (.csv/.bib).
*   Lakukan deduplikasi naskah.
*   Lakukan screening manual (Judul & Abstrak). Gunakan metode AI-Assisted Co-Screener untuk menghitung nilai kesepakatan Kappa guna mengamankan validitas screening Anda.
*   Catat alasan eksklusi untuk setiap naskah yang ditolak dan simpan dalam file CSV terpisah (seperti berkas `all_screened_articles_refined.csv` kita) sebagai bukti transparansi data skripsi.

### Minggu 3: Relevance Scoring & Quality Appraisal
*   Hitung Relevance Score ($S$) untuk artikel yang lolos kelayakan teks lengkap menggunakan formula penjumlahan yang sederhana.
*   Terapkan instrumen JBI Critical Appraisal yang diadaptasi (skala 0-2) dengan definisi operasional yang jelas per tipe penelitian (studi eksperimen kelas vs studi rancang bangun *software* pembelajaran).

### Minggu 4: Sintesis Tematik & Peta Celah Penelitian (Gap Analysis)
*   Petakan artikel final ke dalam domain (misal: Media Berbasis Game, Web-Simulation, LKPD Digital, dll.).
*   Gunakan peta celah tersebut untuk menjustifikasi urgensi rancang bangun media pembelajaran yang akan Anda buat di bab 3 skripsi Anda:
    > *"Berdasarkan SLR terhadap N artikel, pengukuran computational thinking pada topik PBO masih sangat terbatas pada media berbasis desktop. Riset RnD ini mengisi celah tersebut dengan mengembangkan media berbasis mobile web yang patuh terhadap keterbatasan infrastruktur sekolah lokal."*

Dengan mengikuti peta jalan ini dan menghindari 8 jebakan di atas, bab metodologi SLR skripsi Anda akan menjadi sangat kokoh, objektif, dan sulit didebat oleh dosen penguji.
