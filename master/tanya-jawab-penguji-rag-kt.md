# Bank Tanya–Jawab Penguji
## Pendamping untuk: *Desain Sistem RAG-KT "LogiTrace"*

**Cara pakai:** hafalkan **angka** dan **satu kalimat pembuka** tiap jawaban. Sisanya cukup dipahami — penguji menilai apakah Anda tahu batas penelitian Anda, bukan apakah Anda hafal naskah.

---

## 0. Lima aturan menjawab

1. **Jawab dulu, jelaskan kemudian.** Satu kalimat jawaban, baru alasan. Jangan membuka dengan latar belakang.
2. **Sebut angka.** "34 siswa", "180 butir", "476 prediksi", "κ ≥ 0,60". Angka membuat jawaban terasa dikerjakan, bukan dikarang.
3. **Akui batas lebih dulu.** Setiap kali ada celah, sebutkan sebelum ditanyakan. Penguji berhenti menekan ketika Anda sudah menyebutnya.
4. **Jangan berdebat tentang istilah.** Jika penguji memakai istilah berbeda, terima dan jelaskan maksud Anda.
5. **Bila tidak tahu, katakan tidak tahu** — lalu sebutkan bagaimana Anda akan mengetahuinya. Itu jawaban yang dihargai; mengarang tidak.

### Tiga kalimat yang jangan pernah diucapkan

- ❌ *"Model saya akurat 80%."* → Anda tidak punya angka itu.
- ❌ *"Hasilnya bisa digeneralisasi ke seluruh SMK di Indonesia."* → tidak bisa dibela.
- ❌ *"Ini sama seperti ChatGPT."* → menghancurkan seluruh argumen Anda sendiri.

---

# A. Kebaruan dan posisi

**Q1. "Apa novelty penelitian Anda?"**

> **Jawab:** Tiga hal. Pertama, **adaptasi tanpa pelatihan**: kebutuhan data bergeser dari korpus perilaku siswa ke korpus konten kurikulum, sehingga domain vokasi yang tidak punya dataset publik menjadi mungkin. Kedua, **pelabelan ganda KC × dimensi TOLT**, sehingga status pengetahuan dapat dilaporkan pada tingkat dimensi penalaran, bukan hanya konsep. Ketiga, **pengukuran batas**: saya melaporkan di mana pendekatan ini gagal, bukan hanya bahwa ia berjalan.

**Q2. "Apa bedanya dengan CLST yang juga mengatasi cold start?"**

> **Jawab:** CLST tetap **melatih** model — Mistral-7B dengan LoRA pada korpus siswa lain. Saya menghapus tahap pelatihan itu seluruhnya. Perbedaan konsekuensinya: CLST hanya bisa masuk domain yang punya korpus; pendekatan saya masuk domain yang tidak punya. Saya juga tidak mengklaim mengalahkan CLST — CLST sendiri hanya mencapai AUC 0,635–0,689 pada 8 siswa.

**Q3. "Bukankah ini cuma chatbot dengan RAG?"**

> **Jawab:** Chatbot menjawab pertanyaan; sistem ini punya tiga hal yang tidak dimiliki chatbot. (1) **Status penguasaan eksplisit** per KC yang diperbarui dengan aturan yang dapat diaudit. (2) **Pemilih butir** yang menargetkan peluang benar 0,60–0,85. (3) **Agen terbatas** — hanya tiga pemicu tetap, keluarannya divalidasi skema, dan setiap panggilan tercatat.

**Q4. "Bukankah ini cuma prompt engineering? LLM-nya bukan Anda yang buat."**

> **Jawab:** Betul, LLM-nya bukan kontribusi saya — sama seperti LSTM pada DKT 2015 bukan kontribusi penulisnya. Yang saya bangun adalah pemetaan butir ke KC dan dimensi TOLT yang divalidasi pakar, aturan penguasaan yang dapat diaudit, dan pengukuran batas pendekatan tanpa-latih. Ketiganya tidak ada di CLST.

**Q5. "Kenapa tidak memakai DKT saja, kan sudah terbukti?"**

> **Jawab:** Karena DKT membutuhkan korpus. Dengan 34 siswa dan 12 KC, melatih DKT berarti ±440 parameter per interaksi — model akan menghafal siswa, bukan konsep. Dan tidak ada dataset publik untuk 12 KC jaringan versi kurikulum SMK. Saya tidak mengklaim mengalahkan DKT; saya mengklaim dapat dijalankan pada kondisi di mana DKT tidak dapat dijalankan.

---

# B. Metode dan sampling

**Q6. "Sampel Anda mewakili populasi apa?"**

> **Jawab:** Populasi targetnya siswa kelas XI TKJ pada SMK dengan keterbatasan laboratorium komputer. Populasi terjangkaunya seluruh siswa kelas XI TKJ di SMK A tahun ajaran 2026/2027 — 34 orang — dan **seluruhnya diteliti**. Jadi pada tingkat itu ini **sensus**, bukan sampel: keterwakilannya penuh, yang terbatas adalah cakupannya. Terhadap populasi yang lebih luas saya tidak mengklaim generalisasi statistik, melainkan transferabilitas bersyarat.

**Q7. "Kenapa memilih sekolah A dan bukan sekolah lain?"**

> **Jawab:** Pemilihan purposive dengan lima kriteria: SMKN konsentrasi TKJ, kelas XI semester ganjil, rasio PC 1:2, Wi-Fi tersedia, dan kesediaan guru. Kriteria penentu bukan yang memudahkan penelitian, melainkan yang membuat **fenomena ada** — rasio 1:2 itulah yang menimbulkan *dominant-passive pair*. Sekolah ber-PC 1:1 justru akan membuat produk terlihat lebih berhasil, dan saya tidak memilihnya.

**Q8. "34 siswa itu cukup?"**

> **Jawab:** Untuk **sensus** ya — tidak ada sampling error yang perlu diklaim. Untuk **daya uji**, saya sudah menghitung: dengan $n=34$ dan daya 80%, efek terkecil yang dapat dideteksi adalah $d_z \approx 0{,}48$ atau sekitar 1,2 poin dari skala 10. Saya menyebutkan angka itu agar pembaca tahu batasnya, dan saya tidak mengklaim efek kecil.

**Q9. "Purposive atau convenience?"**

> **Jawab:** Purposive pada tingkat lokasi, **sensus** pada tingkat kelas. Keterjangkauan saya akui sebagai pertimbangan operasional dan saya cantumkan di keterbatasan — bukan sebagai dasar pemilihan.

**Q10. "Kenapa hanya satu sekolah?"**

> **Jawab:** Tiga alasan: unit analisisnya kelas dengan fenomena spesifik; penelitian pengembangan mengejar kedalaman produk, bukan luas sebaran; dan menambah sekolah tanpa menambah variasi konteks tidak menambah kekuatan klaim, hanya menambah beban.

**Q11. "Berapa lama penelitiannya?"**

> **Jawab:** Empat sesi tatap muka, masing-masing 90 menit, ditambah uji coba kelompok kecil dua sesi sebelumnya. Total 14 minggu termasuk pengembangan produk.

---

# C. Model dan validitas

**Q12. "Model Anda tidak dilatih. Dari mana Anda tahu ia benar?"**

> **Jawab:** Dari empat jalur yang tidak membutuhkan pelatihan. (1) **Akurasi pemetaan** label LLM versus dua pakar pada 180 butir — target κ ≥ 0,60. (2) **Mutu petunjuk** dinilai tiga pakar — target ICC ≥ 0,70. (3) **Akurasi prediksi pasca-kalibrasi**: 476 prediksi, dibandingkan tiga pembanding tanpa-latih. (4) **Reliabilitas**: antar-run, antar-prompt, antar-model.

**Q13. "Mana angka akurasinya?"**

> **Jawab:** Sekitar 476 prediksi — 34 siswa × 14 butir setelah kalibrasi. Saya membandingkannya dengan tiga pembanding yang juga tidak butuh pelatihan: base rate kelas, rata-rata jawaban siswa sejauh ini, dan model kesulitan-saja. Klaim saya bukan angka absolut, melainkan **selisih di atas pembanding terbaik**, diuji dengan McNemar dan bootstrap.

**Q14. "Kenapa tidak melaporkan AUC saja seperti penelitian lain?"**

> **Jawab:** AUC tetap dilaporkan, tapi sebagai metrik sekunder. Dengan 476 prediksi yang mengelompok per siswa, interval kepercayaan AUC cukup lebar untuk membuat perbandingan tidak bermakna. Akurasi dan Brier lebih stabil pada ukuran ini, dan lebih langsung terkait keputusan yang diambil sistem.

**Q15. "Bagaimana cold start-nya?"**

> **Jawab:** Enam butir kalibrasi — dua mudah, dua sedang, dua sulit — yang mencakup minimal empat KC dan memuat akar DAG. Penguasaan awal 0,25, diperbarui dengan aturan yang sama. KC yang tidak terukur diberi nilai dari klaster prasyarat terdekat dan **ditandai berkeyakinan rendah** di dasbor. Tidak ada pelatihan, tidak ada riwayat yang dibutuhkan.

**Q16. "Kalau LLM salah memberi label KC?"**

> **Jawab:** Ada tiga lapis penjaga. Butir dengan keyakinan di bawah 0,6 masuk antrean tinjauan guru dan tidak dipakai sebelum diputuskan. Semua perubahan label tercatat dengan versi dan pelakunya. Dan dampaknya terbatas: label hanya menentukan KC mana yang diperbarui — kesalahan pada satu butir menggeser satu nilai, tidak merusak model, karena tidak ada model yang dilatih.

**Q17. "Bagaimana kalau petunjuknya membocorkan jawaban?"**

> **Jawab:** Ada pemeriksa kebocoran di kode: petunjuk ditolak bila memuat string jawaban akhir atau frasa "jawabannya adalah", lalu diganti petunjuk statis. Selain itu mutu petunjuk diuji pada E2 oleh tiga pakar dengan rubrik yang salah satu dimensinya justru "tidak membocorkan jawaban".

**Q18. "Bagaimana reliabilitas LLM-nya? Bukankah keluarannya berubah-ubah?"**

> **Jawab:** Saya mengunci tiga hal: `temperature = 0`, versi model dipatok dan dicatat di setiap log, dan prompt diberi versi. Lalu saya uji: tiga kali jalan harus ≥95% identik; dua variasi redaksi prompt untuk melihat sensitivitas; dan perbandingan 3B versus 7B. Kalau ternyata tidak stabil, itu **temuan**, dan saya laporkan sebagai temuan.

**Q19. "Dari mana angka 0,30 dan 0,25 pada aturan penguasaan?"**

> **Jawab:** Nilai awal yang wajar, bukan hasil optimasi. Karena itu saya menjalankan analisis sensitivitas: $\alpha_0 \in \{0{,}20;\ 0{,}30;\ 0{,}40\}$ dan $\tau \in \{30, 60, 120\}$ hari. Jika akurasi stabil terhadap perubahan itu, hasilnya tidak bergantung pada penyetelan halus — dan itu justru lebih kuat daripada satu angka hasil pencarian.

**Q20. "Aturan penguasaan itu bisa disebut model?"**

> **Jawab:** Bisa, dan saya menyebutnya model heuristik yang transparan. Setiap parameter punya arti: laju belajar per tingkat kesulitan, laju penurunan, dan waktu paruh lupa. Bedanya dengan DKT: seluruh riwayat dapat direkonstruksi dari log tanpa membuka bobot jaringan.

---

# D. Instrumen

**Q21. "TOLT itu instrumen baku. Anda mengadaptasinya — masih valid?"**

> **Jawab:** Saya menyebutnya **TOLT-Jaringan**, bukan TOLT. Adaptasi membatalkan norma aslinya, dan itu saya nyatakan. Yang saya lakukan: validasi isi oleh pakar, uji coba dengan KR-20, dan daya beda per butir. Kalau KR-20 di bawah 0,60, saya menambah butir atau membuang butir yang lemah.

**Q22. "Kenapa hanya 10 butir?"**

> **Jawab:** Mengikuti struktur asli TOLT — dua butir per dimensi. Konsekuensinya resolusi skor kasar: setiap butir 10%. Karena itu saya memakai **dua bentuk paralel** dan melaporkan gain mentah serta $d_z$ di samping N-Gain. Batas ini saya tulis di keterbatasan.

**Q23. "Bagaimana penskorannya?"**

> **Jawab:** Dikotomis dua tingkat: skor 1 hanya bila jawaban **dan** alasannya benar. Ini membuat instrumen mengukur penalaran, bukan tebakan.

**Q24. "Berapa KR-20-nya?"**

> **Jawab:** [isi hasil uji coba Anda]. Target minimal 0,60 untuk tes 10 butir dua tingkat. Jika lebih rendah, saya menambah butir pada dimensi yang daya bedanya lemah.

**Q25. "SUS cukup untuk mengukur kepraktisan?"**

> **Jawab:** Untuk persepsi pengguna, ya — instrumennya baku dan dapat dibandingkan dengan ambang 68. Untuk kepraktisan guru saya menambahkan wawancara singkat tiga guru, karena SUS tidak menangkap beban kerja guru.

---

# E. Desain dan kausalitas

**Q26. "Kenapa tidak ada kelas kontrol?"**

> **Jawab:** Dua alasan: jumlah rombel pada satu konsentrasi keahlian terbatas, dan pertimbangan ekuitas — membentuk kelas yang sengaja tidak diberi inovasi berisiko merugikan siswa. Sebagai gantinya saya memakai **NEDV** (butir topik yang tidak diajarkan), **dua bentuk paralel** untuk mengendalikan efek tes, dan rotasi stasiun terimbang. Saya juga tidak menyebut desain ini eksperimen — ini pra-eksperimen satu kelompok, dan batas klaimnya saya tulis.

**Q27. "N-Gain saja cukup?"**

> **Jawab:** Tidak, karena N-Gain bergantung pada skor awal dan resolusi tes. Saya melaporkan gain mentah, $d_z$, dan interval kepercayaan 95% bersama N-Gain.

**Q28. "Bagaimana Anda tahu peningkatan bukan efek tes?"**

> **Jawab:** Tiga pengendalian: butir NEDV yang seharusnya tidak berubah, dua bentuk paralel yang dibagikan bersilang, dan pembandingan dengan dimensi TOLT yang tidak disentuh materi. Jika NEDV ikut naik sebesar TOLT, saya harus menyimpulkan bahwa peningkatan sebagian berasal dari efek tes — dan itu akan saya laporkan.

**Q29. "Efek Hawthorne? Siswa tahu sedang diteliti."**

> **Jawab:** Tidak dapat dihilangkan sepenuhnya, dan saya tidak mengklaim menghilangkannya. Yang bisa saya lakukan: menyembunyikan hipotesis dari siswa, memakai instrumen yang sama di pre dan post, dan menyebutkannya di keterbatasan.

**Q30. "Empat sesi cukup untuk mengubah kemampuan bernalar?"**

> **Jawab:** Tidak untuk mengubah disposisi bernalar secara umum — dan saya tidak mengklaim itu. Yang diukur adalah penalaran **spesifik domain** pada materi yang diajarkan. Empat sesi cukup untuk mengubah performa pada tugas penalaran dalam konteks jaringan, bukan kecerdasan logis secara umum.

**Q31. "Kenapa tidak diacak?"**

> **Jawab:** Unitnya kelas utuh; mengacak siswa ke kondisi berarti memecah rombel yang sudah ada, dan itu tidak diizinkan sekolah. Randomisasi terjadi pada **urutan stasiun** dan **bentuk tes**, bukan pada perlakuan.

---

# F. Teknis dan produk

**Q32. "Berapa latensinya?"**

> **Jawab:** Aturan penguasaan dan pemilihan butir di bawah 10 ms. Panggilan agen 1–3 detik dan hanya terjadi pada tiga pemicu, tidak pada setiap jawaban. Target saya p95 di bawah 3 detik untuk keseluruhan permintaan.

**Q33. "Berapa biayanya?"**

> **Jawab:** Nol biaya API untuk data siswa, karena model berjalan lokal. Biaya sebenarnya adalah pelabelan offline 180 butir sekali jalan dan pelatihan tim — bukan biaya operasional per siswa. Itu justru keunggulan desain ini untuk sekolah.

**Q34. "Kalau internet mati atau server down?"**

> **Jawab:** Web menyimpan jawaban di penyimpanan lokal peramban lalu menyinkronkan saat koneksi kembali. Bila perangkat gagal total, tersedia prosedur kertas untuk satu sesi. Data yang hilang dicatat, bukan ditebak.

**Q35. "Bagaimana privasi siswa?"**

> **Jawab:** Model lokal, data tidak keluar dari server sekolah. Analisis memakai kode anonim. Dasbor guru hanya menampilkan penguasaan dan bukti, bukan label sifat. Persetujuan orang tua dikumpulkan untuk seluruh 34 siswa.

**Q36. "Kalau guru tidak membuka dasbor?"**

> **Jawab:** Maka nilai tambah sistem menurun, dan itu akan terlihat pada data kesetiaan perlakuan. Saya mencatat jumlah pembukaan dasbor dan waktu respons guru terhadap alert. Jika rendah, saya laporkan sebagai temuan implementasi — bukan menyembunyikannya.

**Q37. "Bisa dipakai 10 sekolah sekaligus?"**

> **Jawab:** Secara arsitektur ya, dan itulah intinya: tiap sekolah memakai basis pengetahuannya sendiri tanpa melatih ulang apa pun. Yang perlu disiapkan per sekolah adalah dokumen KC dan pelabelan butir — pekerjaan guru, bukan pekerjaan machine learning.

---

# G. Lapangan

**Q38. "Siswa bisa saling mencontek?"**

> **Jawab:** Butir yang disajikan berbeda antar siswa karena adaptif, sehingga mencontek tidak memberi jawaban yang berguna. Saya juga mencatat waktu respons dan menandai jawaban yang benar dengan durasi tidak wajar.

**Q39. "Kalau ada siswa tanpa ponsel?"**

> **Jawab:** Sekolah menyediakan perangkat pinjaman atau siswa berpasangan. Jika berpasangan, data dicatat sebagai satu sesi bersama dan **dikeluarkan** dari analisis individual — jumlahnya dilaporkan.

**Q40. "Guru sudah sibuk; ini menambah beban?"**

> **Jawab:** Beban utama ada di fase pengembangan, bukan operasional. Saat berjalan, guru hanya melihat satu layar: heatmap KC, daftar siswa macet, saran kelompok. Tidak ada input manual per siswa.

**Q41. "Bagaimana kalau listrik atau Wi-Fi mati di tengah sesi?"**

> **Jawab:** Mode lokal pada peramban menyimpan progres; sesi dapat dilanjutkan. Kejadian dicatat dengan timestamp agar durasi respons yang terdistorsi dapat dikeluarkan dari analisis.

---

# H. Kontribusi dan batas

**Q42. "Apa kontribusi teoretisnya, bukan hanya produk?"**

> **Jawab:** Dua. Pertama, bukti bahwa pelacakan pengetahuan dapat berjalan pada rezim **tanpa korpus perilaku** jika pengetahuan domain dinyatakan sebagai konten yang dapat dibaca mesin. Kedua, operasionalisasi penalaran logis sebagai label ganda KC × TOLT — sesuatu yang dalam tinjauan saya belum pernah didefinisikan secara terukur untuk knowledge tracing.

**Q43. "Apa yang bisa direplikasi sekolah lain?"**

> **Jawab:** Template dokumen KC, prosedur pelabelan butir, aturan penguasaan, dan tiga pemicu agen — semuanya dapat disalin dan disesuaikan. Yang tidak dapat disalin adalah isi materinya, dan itu memang seharusnya disusun tiap sekolah.

**Q44. "Saran penelitian lanjutan?"**

> **Jawab:** Empat. (1) Uji multisitus dengan kelompok kontrol. (2) Pengukuran retensi jangka panjang, bukan hanya post-test dua minggu. (3) Perbandingan langsung dengan DKT yang dilatih, pada domain yang akhirnya punya cukup data. (4) Pengukuran beban kognitif guru saat memakai dasbor.

---

# I. Pertanyaan yang paling menekan

**Q45. "Apa bagian terlemah dari penelitian Anda?"**

> **Jawab:** Tiga. Tidak ada kelompok kontrol, sehingga klaim efek hanya indikasi. Satu sekolah, sehingga generalisasi terbatas. Dan basis pengetahuan ditulis peneliti sendiri, sehingga ada kemungkinan bias penulis — yang saya mitigasi lewat tinjauan pakar, tetapi tidak menghilangkannya. Saya menyebut ketiganya di Bab 3, bukan menunggu ditanyakan.

**Q46. "Kalau hasilnya negatif, apa kontribusinya?"**

> **Jawab:** Tetap ada, dan justru lebih jujur. Hasil negatif pada E3 akan menunjukkan batas konkret pendekatan tanpa-latih: berapa banyak akurasi yang hilang ketika model tidak dilatih. Itu informasi yang dibutuhkan sekolah sebelum memilih pendekatan — dan belum ada yang melaporkannya untuk domain vokasi.

**Q47. "Kalau kampus melarang penggunaan LLM?"**

> **Jawab:** Desainnya tetap berjalan. LLM hanya dipakai di dua tempat: pelabelan butir dan penyusunan petunjuk. Keduanya punya jalur pengganti — pelabelan manual oleh guru, dan petunjuk statis berjenjang yang ditulis per KC. Sistem intinya, yaitu aturan penguasaan dan pemilih butir, tidak bergantung pada LLM sama sekali.

**Q48. "Anda menulis tiga stasiun di Bab 3, tapi dua stasiun di proposal. Mana yang benar?"**

> **Jawab:** Tiga stasiun, dan Bab 3 yang berlaku. Versi dua stasiun adalah draf awal sebelum stasiun bimbingan guru ditambahkan; saya sudah menyelaraskan seluruh dokumen dan menghapus versi lama.

**Q49. "Kalau mengulang penelitian ini, apa yang Anda ubah?"**

> **Jawab:** Tiga. Memulai uji coba kelompok kecil lebih awal agar basis data latih dan penyetelan parameter tidak bertumpuk dengan uji lapangan. Menyiapkan 240 butir, bukan 180, agar variasi lebih longgar. Dan mengajak satu kelas pembanding sejak awal, meski hanya untuk mengukur ekuivalensi awal.

**Q50. "Kenapa penelitian ini layak dipertahankan sebagai skripsi?"**

> **Jawab:** Karena ia menjawab masalah nyata di sekolah dengan sumber daya yang benar-benar tersedia, dan karena setiap klaimnya punya bukti yang saya rencanakan — bukan diasumsikan. Saya tidak mengklaim menemukan model terbaik; saya mengklaim menunjukkan bahwa pelacakan pengetahuan dapat dijalankan pada domain yang tidak pernah punya data, beserta harga dan batasnya.

---

## Lampiran: angka yang harus Anda hafal

| Angka | Arti |
|:--|:--|
| 12 | Jumlah KC |
| 5 | Dimensi TOLT |
| 180 | Butir soal minimum (12 × 3 tingkat × 5) |
| 34 | Siswa (sensus) |
| 4 | Sesi × 90 menit |
| 6 | Butir kalibrasi |
| ±2.720 | Total interaksi |
| 476 | Prediksi untuk E3 (34 × 14) |
| 0,60–0,85 | Pita peluang benar untuk pemilihan butir |
| κ ≥ 0,60 | Target kesepakatan label LLM vs pakar |
| ICC ≥ 0,70 | Target kesepakatan penilaian petunjuk |
| 0,48 | Efek terkecil yang dapat dideteksi ($d_z$, n=34, daya 80%) |
| 3 | Pemicu agen (T1, T2, T3) |
| 3B | Ukuran model lokal |
