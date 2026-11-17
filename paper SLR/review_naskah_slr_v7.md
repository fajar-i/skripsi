# Laporan Review Sejawat Simulasi — `naskah_slr_lengkap(7).md`

**Mode:** full · **Bahasa laporan:** Indonesia (istilah teknis tetap Inggris) · **Rujukan lokasi:** nomor baris pada berkas naskah (mis. "b.101").

## 0. Catatan provenans dan batas laporan (baca dulu)

- Kelima kursi (Journal-Fit Reviewer, R1, R2, R3, Devil's Advocate) dan sintesis dijalankan **berurutan oleh satu model (Claude Sonnet 5.5) dalam satu konteks**. Pemisahan adalah pemisahan **peran**, bukan pemeriksaan independen. Keluaran sesama kursi terlihat satu sama lain, sehingga kesepakatan antarkursi tidak boleh dibaca sebagai bukti bebas.
- Tidak dijalankan: kontrak sprint dua-panggilan, skrip validasi (`check_phase_conformance`, `check_panel_synthesis`), jalur cross-model, dan lampiran cek akronim/referensi/klaim. Status kalibrasi: `NOT_CALIBRATED`. Tidak ada skor numerik.
- Manuskrip **tidak diubah** (read-only). Pencarian Scopus, PDF sumber, dan matriks ekstraksi **tidak diperiksa ulang**; semua temuan berasal dari teks naskah dan konsistensi internalnya.
- Pengecekan aritmetika internal (distribusi tahun, domain, penerbit, jenis dokumen, Springer/IEEE di Lampiran A, jumlah K1–K5 Lampiran B, dan selisih pada Tabel 5/Park/Wang) hasilnya **cocok**, kecuali yang tercatat di Lampiran 1 laporan ini.

---

## 1. Fase 0 — Analisis bidang dan kartu konfigurasi reviewer

| Item | Hasil |
|:--|:--|
| Disiplin utama / sekunder | Teknologi pendidikan–AIED / educational data mining; pendidikan ilmu komputer |
| Jenis naskah | Tinjauan sistematis (PRISMA 2020), sintesis naratif tematik, 1 basis data (Scopus) |
| Kematangan | Draf lanjut dengan banyak placeholder (nama penulis, alat AI, konfirmasi tanggal) |
| Target jurnal (asumsi, tidak tertulis di naskah) | Jurnal informatika/teknologi pendidikan berbahasa Indonesia tingkat SINTA 1–2; bila diterjemahkan, jurnal internasional Q2–Q3 bidang AIED. Ambang review dikalibrasi ke sini. |

| Kursi | Profil yang dikonfigurasi |
|:--|:--|
| Journal-Fit Reviewer (`EIC`) | Editor pelaksana jurnal teknologi pendidikan/AIED; menilai kecocokan, orisinalitas, kejelasan kontribusi |
| R1 Metodologi | Metodolog tinjauan sistematis dan sintesis bukti (PRISMA, SWiM, penilaian mutu studi ML/pendidikan) |
| R2 Domain | Peneliti knowledge tracing / EDM (arsitektur DKT, graf, LLM-KT, dataset ASSISTments/EdNet) |
| R3 Perspektif | Peneliti pendidikan komputasi dan computational thinking; sudut praktik sekolah/kampus Indonesia |
| Devil's Advocate | Kursi tetap; menantang argumen inti |

---

## 2. Ringkasan naskah

Naskah memetakan 21 artikel Scopus (2021–2026) tentang knowledge tracing untuk tugas penalaran/pemecahan masalah/pemrograman. Temuan utamanya: LLM mulai dipakai (8 artikel), afek jarang dimodelkan (1), ASSISTments dominan, bukti intervensi kecil dan jangka pendek, logika formal hanya 2 artikel dari satu kelompok, dan computational thinking (CT) tidak didefinisikan oleh artikel mana pun. Kekuatan yang nyata: kejujuran pelaporan keterbatasan, hitungan ulang selisih metrik yang transparan, dan kehati-hatian klaim di Bagian 4.1 dan 5.1.

---

## 3. Laporan Journal-Fit Reviewer (`EIC`)

**Rekomendasi sinyal:** Major Revision.

**Kecocokan dan signifikansi.** Topik relevan dan tepat waktu. Namun judul menjanjikan "Deep Knowledge Tracing untuk pemodelan penalaran logis dan berpikir komputasional", sedangkan hasil menunjukkan: CT nol artikel (b.207), logika formal dua artikel dari satu kelompok (b.201), dan lima dari 21 artikel bukan studi KT empiris (lihat R1). Penulis sendiri mengakui di b.257 bahwa judul "lebih tepat dibaca" sebagai pemetaan KT untuk pemecahan masalah dan pemrograman. Judul harus mengikuti temuan, bukan sebaliknya.

**Kontribusi.** Tiga kontribusi di b.53 (taksonomi, pemetaan RQ2, pemetaan dataset/metrik/bukti) belum cukup berbeda dari survei KT yang sudah ada; kebaruannya ada pada lensa "bagaimana penalaran direpresentasikan" dan pada **peta celah bukti** (gap map). Kontribusi paling kuat sebenarnya adalah audit kritis atas klaim (mis. Park 2026, Huang 2026, Li 2026, Shukla 2026), dan ini kurang diangkat.

**Klaim kebaruan lemah.** b.41: "belum kami temukan" tinjauan serupa, dengan pengakuan bahwa pencarian tidak dirancang untuk mencari tinjauan. Klaim kebaruan perlu pencarian khusus.

**Kekuatan.** (1) Pelaporan keterbatasan jujur (b.279). (2) Pemisahan bukti per dataset di Tabel 4. (3) Pelacakan inkonsistensi internal artikel yang ditinjau (Li 2026, Huang 2026, Shukla 2026).

**Kesiapan.** Belum siap: placeholder tersisa, catatan penulis di daftar pustaka, dan masalah metodologis (R1).

---

## 4. Laporan R1 — Metodologi

**M1 [Critical] Kriteria kelayakan tidak dipatuhi.** Eksklusi (b) di b.80 menyingkirkan "studi tanpa komponen pemodelan atau algoritma pelacakan", namun 21/21 laporan lolos tanpa eksklusi (b.86, Gambar 1). Padahal b.143 menyatakan Liang 2023, Shukla 2026, Wang 2024 **tidak memuat modul KT**, Samonte 2024 hanya rancangan konseptual, dan Shen 2024 adalah survei. Itu 5 dari 21 (24%) yang oleh kriteria penulis sendiri seharusnya tereksklusi atau diperlakukan sebagai konteks. Akibatnya: judul, abstrak, "taksonomi 21 studi" (b.53), dan hitungan seperti "delapan artikel LLM" memakai penyebut yang salah. Penjelasan di b.279 ("string terlalu luas") adalah diagnosis, bukan perbaikan. Selain itu, nol eksklusi di dua tahap pada 34 rekaman, dengan seleksi oleh satu penelaah berbantuan AI tanpa validasi, adalah tanda bahaya sensitivitas/spesifisitas, bukan bukti keberhasilan pencarian.

**M2 [Critical] Retrieval 38%.** 13/34 laporan tidak diperoleh (b.86). Pada tinjauan sistematis standar, laporan tak-terambil biasanya sebagian kecil. Di sini ia menyentuh langsung pertanyaan pusat: 3 dari 13 bertopik penalaran logis, 1 neural-simbolik (b.279). Upaya yang tidak tercatat dan layak dicoba: permintaan ke penulis, interlibrary loan/akses institusi, pracetak, repositori institusi. Li et al. (2025) bertanda akses terbuka di Scopus tetapi dilaporkan "tautan rusak" (b.86) dan dapat dicoba lewat DOI. Menjadikan "teks lengkap dapat diperoleh" sebagai **kriteria inklusi/eksklusi** (b.78, b.80) mencampur akses dengan kelayakan; PRISMA 2020 memperlakukan "reports not retrieved" sebagai kotak aliran tersendiri, bukan kriteria eksklusi. Karena 13 laporan itu tidak pernah dinilai kelayakannya, klaim "tidak ada eksklusi pada tahap kelayakan" hanya berlaku untuk 21 yang terambil.

**M3 [Critical] Satu penelaah + AI tanpa validasi.** Seleksi: satu penelaah + alat AI yang belum disebut ([nama alat dan versi], b.101). Ekstraksi: satu agen AI, diperiksa AI, lalu manusia pada 72/74 butir; **6 butir salah (~8%)** (b.101). Tingkat galat ini menunjukkan ekstraksi AI tidak dapat dipercaya tanpa verifikasi menyeluruh, padahal pemeriksaan manusia hanya mencakup butir log; detail di luar log tidak diperiksa (diakui di b.101, b.279). Dengan n = 34 rekaman dan 21 artikel, penyaringan ganda manusia dan ekstraksi independen oleh penelaah kedua adalah pekerjaan kecil dan membuka kritik terbesar. Cek-silang AI-oleh-AI (pencocokan string) tidak independen secara bermakna, seperti diakui sendiri oleh penulis ("hanya memastikan string muncul di suatu tempat", b.101).

**M4 [Major] Strategi pencarian.** (a) Satu basis data. KT dikelola luas di IEEE Xplore, ACM DL, ERIC, WoS, dan prosiding EDM/LAK/AIED. (b) Konsep ketiga menggabungkan konstruk target ("Logical Reasoning", "Computational Thinking") dengan "Problem Solving" yang sangat luas; keseluruhan string menghasilkan hanya 34 rekaman untuk 5 tahun KT, artinya sampel sempit, bukan "literatur KT 2021–2026". (c) Tidak ada sinonim: "student/learner modeling", "programming", "code", "mastery", "exercise"; kata "programming" dipakai sebagai domain inklusi (b.78) tetapi tidak ada di string. (d) `"ITS"` pada `TITLE-ABS-KEY` dapat bertabrakan dengan kata ganti *its* bergantung pengolahan stop-word Scopus; **perlu diverifikasi** dan, bila terbukti, konsep kedua praktis tak membatasi apa pun. (e) Tidak dilaporkan jumlah rekaman per konsep/istilah, sehingga pembaca tak bisa menilai mengapa CT menghasilkan nol artikel. (f) Protokol tidak didaftarkan/pra-ditetapkan; RQ tampak disusun bersama string; PRISMA-S tidak dipakai. Tanggal penelusuran masih placeholder (b.65).

**M5 [Major] Penilaian mutu.** Lembar K1–K5 buatan sendiri, dinilai satu penelaah berbantuan AI. Konstruknya terlalu dangkal untuk studi ML: tidak ada butir kebocoran data, pembagian per siswa vs per interaksi, penyetelan hiperparameter, pembanding direproduksi vs disalin, ketersediaan kode/data. Selain itu ada **inkonsistensi pengkodean**: Wang 2021 diberi K4 = Ya dan disebut di b.147 sebagai salah satu dari empat artikel dengan dukungan statistik lengkap, padahal b.166 menyatakan keunggulannya terhadap DKT, DKVMN, dan pembanding tensor terkuat **tidak signifikan**. K4 menilai apakah uji "mendukung klaim keunggulan"; di sini tidak mendukung. Zhao 2026 juga K4 = Ya padahal Tabel 5 memuat puluhan uji tanpa koreksi, beberapa pada p = 0,045–0,049. Sementara itu uji non-independen vs independen pada Shukla dicatat secara kritis di b.245. Standar kritik tidak konsisten.

**M6 [Major] Sintesis.** Narative thematic tanpa pelaporan SWiM, tanpa penilaian kepastian bukti (certainty) per temuan, dan tanpa tabel yang memetakan modalitas input × artikel, padahal "pergeseran sumber informasi" (b.185) dan "pola yang menghubungkan banyak artikel" (b.253) adalah klaim hasil utama yang tidak ditabulasi. Tato & Nkambou 2022 dan Nkambou 2023 memakai data yang sama dan angka yang identik (b.201) tetapi dihitung sebagai dua studi dalam Tabel 2 dan hitungan RQ; laporan terkait seharusnya disatukan sebagai satu klaster studi.

**M7 [Minor] Reproduksibilitas.** Pernyataan ketersediaan data masih placeholder (b.309). Ekspor 34 rekaman (disertakan/tidak), matriks ekstraksi, log verifikasi 74 butir, prompt AI, dan skrip pencocokan sebaiknya dideposit (OSF/Zenodo).

**M8 [Minor] Bagian 2.5** adalah satu paragraf ±450 kata yang mencampur metode, hasil verifikasi, dan riwayat koreksi ("telah diperbarui", b.101). Pindahkan riwayat koreksi ke berkas suplemen; sisakan prosedur, tingkat galat, dan batasannya.

---

## 5. Laporan R2 — Domain (knowledge tracing)

**D1 [Major] Konsep "Deep" KT tidak konsisten dengan korpus.** Judul dan RQ1 membingkai "DKT"; Tabel 2 memasukkan 5 artikel psikometrik/faktorisasi/BKT dan 3+ tanpa modul KT. RQ1 "bagaimana arsitektur berkembang dari sekuensial, ke graf/hipergraf, ke LLM" mengandung praanggapan perkembangan linear yang oleh Bagian 4.2 sendiri ditolak ("tidak mendukung narasi bahwa satu arus menggantikan arus lain"). Rumuskan ulang RQ1 tanpa praanggapan (mis. "Informasi apa yang dimasukkan ke model dan oleh arsitektur apa?").

**D2 [Major] Klasifikasi LLM tidak konsisten.** Tabel 2 menghitung 8 artikel "terintegrasi LLM", tetapi Zhang et al. (2025) memakai GPT-4o untuk augmentasi (b.136, b.166) dan ditempatkan di kelompok psikometrik; dengan kriteria "memakai LLM" jumlahnya 9 (8 dari 9 terbit 2025–2026). Dua dari 8 (Liang, Shukla) tanpa modul KT, sehingga klaim abstrak "delapan artikel memakai LLM" berlaku untuk lingkup yang berbeda dari "model KT". Tetapkan satu kriteria klasifikasi (arsitektur inti vs penggunaan komponen) dan pakai konsisten. "Taksonomi" (b.53) lebih tepat disebut pengelompokan karena tak hierarkis dan tidak saling lepas (b.151).

**D3 [Major] Dataset penalaran logika.** Abstrak b.13: dua artikel "dari satu kelompok dan satu dataset"; Tabel 1 (b.119) menunjukkan Tato & Nkambou 2022 memakai **dua** dataset, dan MorALERT adalah klasifikasi teks penalaran sosio-moral, bukan KT dan bukan logika formal (b.193). Jadi bukti KT logika formal sebenarnya satu dataset (Logic-Muse), satu kelompok, dan **satu klaster studi** (bukan dua). Itu justru temuan yang lebih kuat; tulis dengan tepat.

**D4 [Major] Kualitas data dan perbandingan.** Tabel 4 membandingkan AUC lintas studi pada ASSIST09/12/17 walau pembagian, praproses, dan versi data berbeda; teks (b.228) mencatat sebagian, tetapi tabelnya sendiri tidak membawa peringatan. Literatur KT telah mendokumentasikan masalah kualitas pada ASSIST09 (mis. rekaman duplikat) yang menggembungkan AUC bila tidak dibersihkan (**perlu diverifikasi sumbernya sebelum dikutip**). Hal ini relevan terhadap Li 2026 (AUC 0,901 pada subset 1.000 siswa dengan pembagian tak dirinci, vs 0,8289 pada Huang 2026): tanyakan versi data apa, apakah ada kebocoran pembagian. Tambahkan kolom "versi data, subset, pembagian" di Tabel 4 atau hapus tabel itu sebagai pembanding.

**D5 [Major] Afek.** Huang 2026 memakai label afek dari *sensor-free affect detector* pada ASSIST12/17 (b.205): afek di sini adalah **prediksi model**, bukan observasi. Pernyataan "satu-satunya yang memodelkan afek secara eksplisit" perlu disertai catatan validitas detektor. Definisi operasional "dimensi afektif" belum ada di Metode (apakah beban kognitif/NASA-TLX pada Shukla, kecepatan pada Jadhav termasuk?).

**D6 [Minor] Atribusi F1.** b.37 mengaitkan F1 = 0,0 dan 0,47–0,80 dengan Nkambou 2023; b.201 mengaitkan F1 per keterampilan MPP/MTT dengan Tato & Nkambou 2022. Karena kedua artikel berbagi angka, pastikan atribusi sama di semua tempat.

**D7 [Minor] Klaim tanpa dukungan.** b.31: "kesalahan estimasi pada soal penalaran berdampak lebih besar daripada pada hafalan" tak bersumber. b.33: "Kurikulum saat ini menekankan…" hanya dirujuk ke Wing (2006).

**Kekuatan.** Hitungan ulang kritis (Jung 2025 24,52% vs 11,9%; Park 2026 kenaikan per model; Shao 2026 binarisasi di 0,5), dan penolakan terhadap perbandingan AUC lintas protokol, adalah nilai tambah nyata bagi bidang.

---

## 6. Laporan R3 — Perspektif lintas disiplin dan praktik

**P1 [Major] Konstruk CT dan penalaran tidak dioperasionalkan di Metode.** Naskah menyimpulkan "CT tidak didefinisikan" tanpa menyatakan apa yang dihitung sebagai definisi (dekomposisi, abstraksi, dll., b.207) di Bagian 2. Rujukan CT tunggal (Wing 2006) tidak cukup; literatur pendidikan CT (kerangka operasional untuk K-12/perguruan tinggi, asesmen CT) perlu dipakai untuk menurunkan kode ekstraksi. Tanpa itu "nol artikel" tidak dapat diaudit. Sebaliknya, wajar bahwa CT tidak muncul dalam KT: asesmen CT umumnya bukan butir benar/salah. Itu seharusnya dibahas sebagai temuan konseptual (ketidaksesuaian konstruk–metode), bukan hanya "celah".

**P2 [Major] Konteks Indonesia hampir hilang.** Judul/abstrak berbahasa Indonesia tetapi motivasi tidak menyentuh pendidikan Indonesia: tak ada rujukan kurikulum (mis. mata pelajaran informatika), tak ada data penerapan ITS setempat, tak ada pertimbangan bahasa (semua dataset berbahasa Inggris/Prancis/Cina?). Kalimat tentang server kampus Indonesia (b.271) berdiri sendiri. Entah dikaitkan dengan serius atau dilepas.

**P3 [Major] Implikasi praktis melampaui bukti.** b.275: "memakai LLM untuk membimbing, bukan menjawab (Wang 2026)" didasarkan pada benchmark siswa-simulasi dan pilot 42 siswa tanpa kontrol yang oleh Bagian 3.4 sendiri dinilai lemah. Rekomendasi 7 di b.303 (hibrida simbolik–neural) bersandar pada satu klaster studi tanpa uji signifikansi. Turunkan ke "hipotesis yang layak diuji", atau tambahkan tingkat kepastian.

**P4 [Minor] Pembaca guru/praktisi.** Tabel ringkas "apa yang bisa dipakai praktisi sekarang vs belum" (bukti kuat/lemah per kebutuhan: memprediksi, memberi petunjuk, memilih soal) akan menaikkan manfaat bagi pembaca non-peneliti KT. Biaya komputasi dan privasi (b.271, b.275) layak dijadikan baris di tabel itu.

**P5 [Minor] Etika dan privasi.** Dua kalimat tentang sinyal fisiologis cukup baik; tambahkan satu paragraf tentang risiko memakai LLM pihak ketiga pada log siswa (kebocoran data siswa).

---

## 7. Laporan Devil's Advocate

**Kontra-argumen terkuat (±250 kata).** Kesimpulan utama naskah, yaitu bahwa bukti penalaran logis tipis dan CT tidak ada, bukan temuan tentang literatur; itu **artefak desain tinjauan**. String penelusuran menempatkan "Problem Solving" di samping konstruk target, hanya memakai Scopus, tanpa sinonim, dan 38% laporan tak terambil, termasuk tiga yang berfokus pada penalaran logis. Dengan korpus yang dipenuhi studi matematika ASSISTments yang masuk karena frasa "problem solving", dan lima artikel yang bukan studi KT, "21 studi" menyembunyikan bahwa inti tema (logika formal) bertumpu pada satu klaster studi dan nol uji signifikansi. Lalu seleksi dan ekstraksi dikerjakan satu orang dengan AI, dengan galat 8% pada butir kunci yang terdeteksi: kita tidak tahu galat pada butir yang tidak dicek. Sintesis kemudian menyusun narasi ("pergeseran sumber informasi", "pola yang menghubungkan banyak artikel") dari matriks yang sama, lalu memakai "keterbatasan Bagian 1.2" yang disusun dari studi yang sama sebagai motivasi: sirkular. Hasil bersihnya adalah laporan yang jujur tetapi hanya ringkasan deskriptif dari sampel bergantung-akses, yang disajikan dengan bahasa sistematis.

**Isu**

| # | Tingkat | Isu | Lokasi |
|:-:|:--|:--|:--|
| DA1 | **CRITICAL** | Kesimpulan "celah" (logika formal tipis, CT nol) tak dapat dibedakan dari artefak pencarian/akses; klaim ketiadaan butuh pencarian yang dirancang untuk menemukannya | b.13, b.201, b.207, b.293 |
| DA2 | **CRITICAL** | Kriteria inklusi tidak diterapkan; 24% korpus bukan studi KT; penyebut semua hitungan salah | b.80, b.86, b.143 |
| DA3 | **CRITICAL** | Rantai verifikasi AI-oleh-AI; galat ~8% pada butir yang dicek; nol validasi seleksi | b.101, b.279 |
| DA4 | MAJOR | Sirkularitas: motivasi 1.2 dan "pola" 4.1 disusun dari studi yang sama | b.37, b.253–255 |
| DA5 | MAJOR | Hitungan "satu klaster studi" dianggap dua; "paling konsisten" tanpa tabel | b.185, b.201 |
| DA6 | MAJOR | Perbandingan lintas dataset yang dilarang Bagian 2.5 dilakukan sendiri di 4.3 (AUC 0,574–0,689 vs 0,80–0,90) | b.103 vs b.267 |
| DA7 | MAJOR | Rekomendasi (hibrida simbolik–neural, LLM membimbing) bersandar pada bukti yang dinilai lemah | b.275, b.303 |
| DA8 | MINOR | Peran Liang 2023 (LLM mengajar *solver*, bukan siswa) kabur sebagai bukti untuk pembelajaran | b.191 |

**Alternatif yang diabaikan.** (i) Tinjauan pemetaan (*scoping*/*evidence gap map*) lebih cocok dengan desain dan tujuan daripada tinjauan sistematis penuh dengan klaim kelayakan. (ii) Penelusuran terpisah per konstruk (logika formal; CT; pemrograman) dengan string sendiri. (iii) KT berbasis non-*deep* (BKT/IRT/DAS3H) untuk domain data-kecil dipinggirkan walau relevan untuk logika formal.

**Pemangku kepentingan yang tak terwakili.** Guru/dosen (apakah keluaran KT dipakai?), pengembang ITS lokal, dan pembelajar (privasi data log/biosensor).

**Uji "so what?".** Bagi pembaca KT: tak ada sintesis kuantitatif atau pedoman pelaporan yang bisa dipakai. Bagi praktisi Indonesia: tak ada rekomendasi yang bisa diterapkan dengan bukti memadai. Nilai tersisa adalah peta celah dan audit klaim; angkat itu secara eksplisit.

**Pengamatan non-cacat.** Pelaporan keterbatasan, penghitungan ulang selisih, dan pengungkapan penggunaan AI sudah di atas rata-rata.

---

## 8. Surat Keputusan Editorial

**Keputusan: MAJOR REVISION.**

### 8.1 Konsensus (lintas kursi; ingat satu-model, bukan independen)

1. Judul/RQ melebihi bukti (EIC, R2-D1, R3-P1, DA1).
2. Kriteria kelayakan tak diterapkan; 5/21 artikel bukan studi KT (R1-M1, R2-D2, DA2).
3. Verifikasi dan seleksi tidak independen; galat ekstraksi ~8% (R1-M3, DA3).
4. Strategi pencarian sempit dan retrieval 38% memengaruhi inti temuan (R1-M2, M4, DA1).
5. Hitungan dan klasifikasi internal perlu direkonsiliasi (R1-M6, R2-D2, D3, Lampiran 1).

### 8.2 Perbedaan dan arbitrasi

- **Tinjauan sistematis vs pemetaan.** EIC/R1 menuntut perbaikan prosedur sistematis; DA menyarankan turun ke scoping/evidence gap map. **Arbitrasi:** kedua jalur sah. Jalur A (perbaiki dan perluas): tambah basis data, penyaringan ganda, ambil ulang laporan. Jalur B (reposisi): ubah judul/klaim menjadi pemetaan celah, jujur tentang sampel Scopus; tetap wajib ada penyaringan ganda untuk 34 rekaman dan eksklusi sesuai kriteria. Disarankan A minimal + B untuk judul dan klaim.
- **Tingkat keparahan K4 Wang 2021/Zhao.** R1 menilai inkonsistensi pengkodean (Major); EIC menganggap koreksi mudah. Disepakati: wajib dikoreksi, bukan penentu keputusan.

### 8.3 Adjudikasi Devil's Advocate CRITICAL

| DA | Putusan | Alasan |
|:-:|:--|:--|
| DA1 | **Divalidasi** | Konsisten dengan M2/M4; klaim ketiadaan butuh desain pencarian yang sesuai atau pelunakan bahasa |
| DA2 | **Divalidasi** | Terbukti dari teks sendiri (b.80, b.143, b.86) |
| DA3 | **Divalidasi sebagian** | Pengungkapan jujur dan 72/74 butir diperiksa manusia memitigasi; tetapi seleksi tanpa validasi dan butir di luar log tak terverifikasi |

Ketiganya divalidasi; kondisi ini menutup jalur **Accept** dan mendukung **Major Revision** (bukan Reject, karena semuanya dapat diperbaiki).

### 8.4 Ringkasan penilaian (kategori, `NOT_CALIBRATED`)

| Dimensi | Penilaian |
|:--|:--|
| Relevansi topik | MEETS |
| Kesesuaian judul/RQ dengan bukti | DOES_NOT_MEET |
| Ketepatan pencarian & seleksi | DOES_NOT_MEET |
| Ekstraksi & penilaian mutu | PARTLY_MEETS |
| Validitas sintesis dan klaim | PARTLY_MEETS |
| Transparansi dan kehati-hatian klaim | MEETS (dengan catatan konsistensi) |
| Kesiapan naskah (placeholder, format) | DOES_NOT_MEET |

---

## 9. Peta Jalan Revisi (Revision Roadmap)

Daftar ini adalah **saran**; urutan kerja dan keputusan lingkup tetap milik penulis. `[W]` = wajib untuk menjawab keputusan; `[S]` = disarankan.

### Prioritas 1 — struktural

| ID | Tindakan | Sumber |
|:-:|:--|:-:|
| R1 `[W]` | **Selaraskan lingkup.** Pilih: (a) ubah judul/abstrak/RQ jadi "KT untuk pemecahan masalah dan pemrograman…", lalu perlakukan logika formal dan CT sebagai pernyataan celah; atau (b) rancang ulang string untuk konstruk target. Hapus praanggapan perkembangan di RQ1. | M1, D1, EIC |
| R2 `[W]` | **Terapkan kriteria.** Keluarkan atau pindahkan ke "konteks" Liang 2023, Shukla 2026, Wang 2024, Samonte 2024, Shen 2024 (atau ubah kriteria secara terbuka); perbarui PRISMA dengan alasan eksklusi dan seluruh hitungan (abstrak, Tabel 2, RQ). | M1 |
| R3 `[W]` | **Pulihkan laporan.** Upayakan 13 teks lengkap (penulis, ILL, akses institusi, pracetak; Li 2025 lewat DOI); ubah "teks lengkap" dari kriteria eksklusi menjadi kotak "reports not retrieved"; laporkan hasil upaya. Bila tetap tak terambil, nilai dari abstrak dan tandai sebagai "belum disintesis". | M2 |
| R4 `[W]` | **Verifikasi manusia.** Penyaringan ganda independen atas 34 rekaman (laporkan kappa); ekstraksi independen oleh penelaah kedua untuk nilai di Tabel 1, 4, 5 (laporkan tingkat galat dan cakupan); sebut alat AI, versi, prompt. | M3 |
| R5 `[W]` | **Perluas dan laporkan pencarian.** Tambah ≥2 basis data dan sinonim (student/learner modeling, programming, code); verifikasi masalah "ITS"; laporkan hitungan per konsep; patuhi PRISMA-S; daftarkan protokol (OSF) dengan keterangan penyimpangan; isi tanggal penelusuran. | M4 |
| R6 `[W]` | **Perbaiki penilaian mutu.** Tambah butir khas ML (kebocoran/pembagian per siswa, penyetelan, pembanding direproduksi, kode/data); koreksi K4 Wang 2021 dan tinjau K4 Zhao; penilaian ganda. | M5 |

### Prioritas 2 — sintesis dan klaim

| ID | Tindakan | Sumber |
|:-:|:--|:-:|
| R7 `[W]` | Rekonsiliasi hitungan: LLM 8 vs 9 (Zhang 2025), "enam belas" vs 17 (b.143), "satu dataset" vs MorALERT (b.13/b.119), "25–294" vs isi Tabel 5 (b.245), "hampir separuh" untuk 11/21 (b.111), "Dua hal… Ketiga" (b.245), duplikasi "Huang et al. (2024), sebaliknya, Huang et al. (2024)" (b.164). | D2, D3, Lamp. 1 |
| R8 `[W]` | Gabungkan Tato & Nkambou 2022 dan Nkambou 2023 sebagai satu klaster studi dalam hitungan dan klaim logika formal. | M6, D3 |
| R9 `[S]` | Tambah tabel modalitas input × artikel dan pandangan temporal untuk menopang "pergeseran sumber informasi" dan 4.1; ganti "taksonomi" menjadi "pengelompokan". | M6, D2 |
| R10 `[S]` | Tambah penilaian kepastian bukti per temuan RQ (kriteria sederhana tertulis) dan acu SWiM. | M6 |
| R11 `[W]` | Lunakkan klaim ketiadaan menjadi "dalam korpus ini"; hapus/relabel perbandingan lintas dataset di b.267; turunkan rekomendasi 4.4 dan 5.2-7 ke hipotesis atau beri tingkat kepastian. | DA1, DA6, DA7, P3 |
| R12 `[S]` | Perbaiki Tabel 4: kolom versi data/subset/pembagian atau hapus sebagai pembanding; periksa isu kualitas ASSIST09 (verifikasi sumber). | D4 |
| R13 `[S]` | Beri definisi operasional "afektif" dan catatan bahwa label afek Huang 2026 berasal dari detektor. | D5 |
| R14 `[S]` | Operasionalkan CT/penalaran logis di Bagian 2 dengan kerangka dari literatur pendidikan CT; bahas ketidaksesuaian konstruk–metode. | P1 |
| R15 `[S]` | Lakukan pencarian tinjauan terdahulu (KT di pemrograman, LLM-KT) dan perjelas kebaruan. | EIC |
| R16 `[S]` | Kaitkan ke konteks Indonesia secara substantif (kurikulum, bahasa, infrastruktur) atau hapus klaim lokal; beri sumber untuk b.31 dan b.33. | P2, D7 |

### Prioritas 3 — penyajian

| ID | Tindakan | Sumber |
|:-:|:--|:-:|
| R17 `[W]` | Hapus semua placeholder dan "Catatan untuk penulis" (daftar di Lampiran 1). | EIC |
| R18 `[S]` | Ringkas Bagian 2.5; pindahkan riwayat koreksi dan log ke suplemen; deposit matriks, log verifikasi, ekspor 34 rekaman, prompt. | M7, M8 |
| R19 `[S]` | Gunakan templat diagram alir PRISMA 2020 resmi; pisahkan "reports not retrieved". | M2 |
| R20 `[S]` | Rapikan referensi: bedakan Zhang et al. 2025a/b, periksa tahun "Zhou et al. (2027)" terhadap rentang 2021–2026, verifikasi identitas model "Gemini Flash 3.8" dan DOI, dan putuskan apakah laporan tak-terambil boleh dikutip dari judul saja. | Lamp. 1 |

**Urutan kerja yang disarankan:** R1 → R2 → R5 → R3 → R4 → R6 → R7–R8 → sisanya. R1 dan R2 menentukan lingkup; mengerjakannya lebih dulu mencegah pengerjaan ulang.

---

## Lampiran 1 — Daftar placeholder dan inkonsistensi angka

**Placeholder/catatan yang harus dihapus atau diisi:** nama penulis, afiliasi, email (b.5–7); tanggal penelusuran (b.65); "[konfirmasi]" (b.86); "[nama alat dan versi]", "[isi bila penulis memeriksa sendiri]", "[konfirmasi: penulis memeriksa penilaian]" (b.101); data availability (b.309); CRediT, konflik, pendanaan (b.313–317); nama alat seleksi (b.319); catatan penulis di daftar pustaka (b.325).

**Inkonsistensi/butir untuk dicek:**

| Lokasi | Butir |
|:--|:--|
| b.111 | "Hampir separuh" untuk 11/21 (52%) |
| b.143 | 21 − 3 − 1 = 17, bukan 16, kecuali survei Shen 2024 juga tak dihitung; nyatakan |
| b.13 vs b.119 | "satu dataset" vs Logic-Muse + MorALERT |
| b.147 vs b.166 | Wang 2021 K4 = Ya vs keunggulan tak signifikan |
| b.164 | Duplikasi sitasi "Huang et al. (2024), sebaliknya, Huang et al. (2024)" |
| b.136 vs Tabel 2 | Zhang 2025 memakai GPT-4o tetapi tidak dihitung "terintegrasi LLM" |
| b.245 | "Dua hal perlu dicatat" diikuti tiga butir; rentang sampel "25–294" melibatkan 294 yang tidak ada di Tabel 5 |
| b.37 vs b.201 | Atribusi F1 ke Nkambou 2023 vs Tato & Nkambou 2022 |
| b.267 vs b.103 | Perbandingan lintas dataset padahal ada aturan hanya dalam dataset yang sama |
| b.409 | "Zhou et al. (2027)" di luar rentang 2021–2026 |
| b.141 | Catatan Tabel 1: "Tahun mengikuti ekspor Scopus" — periksa terhadap tahun terbit sebenarnya untuk artikel 2026 yang mungkin early access |
