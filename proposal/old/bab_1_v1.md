# BAB I
# PENDAHULUAN

## 1.1 Latar Belakang Masalah

Perkembangan teknologi kecerdasan buatan (*Artificial Intelligence*) dan transformasi digital pada era Industri 4.0 dan Society 5.0 telah mendisrupsi berbagai sektor kehidupan, termasuk lanskap pendidikan vokasi dan tuntutan kualifikasi tenaga kerja global. Ekosistem industri modern kini menuntut sumber daya manusia yang tidak hanya menguasai keterampilan teknis prosedural, melainkan memiliki kecakapan kognitif tingkat tinggi, khususnya kemampuan berpikir logis (*logical thinking*) dalam menganalisis dan memecahkan permasalahan sistem yang kompleks [BUTUH KUTIPAN 2021–2026: Tuntutan keterampilan berpikir logis dan pemecahan masalah adaptif di era Industri 4.0/5.0]. Sejalan dengan pergeseran tersebut, pemanfaatan teknologi cerdas di bidang pendidikan (*Artificial Intelligence in Education*) berkembang pesat, terutama dalam menghadirkan sistem asesmen formatif adaptif yang mampu mempersonalisasi proses belajar sesuai dengan dinamika pemahaman masing-masing peserta didik.

Secara ideal, pendidikan kejuruan berfungsi menyiapkan peserta didik agar memiliki kompetensi kerja yang relevan, mandiri, dan berdaya adaptasi tinggi terhadap dinamika industri, sebagaimana diamanatkan dalam Undang-Undang Nomor 20 Tahun 2003 tentang Sistem Pendidikan Nasional (Republik Indonesia, 2003). Untuk mencapai standar mutu tersebut, proses pembelajaran idealnya ditopang oleh evaluasi formatif yang bersifat diagnostik dan berkelanjutan. Evaluasi formatif yang efektif berfungsi memetakan lintasan pemahaman konsep peserta didik secara berkala, memberikan umpan balik tepat waktu, serta melatih daya nalar logis agar siswa mampu memahami relasi sebab-akibat dari setiap tindakan operasional teknis (Bohle Carbonell et al., 2014; Wardani et al., 2022). Dengan pemahaman logika yang matang, peserta didik diharapkan bertransformasi menjadi praktisi yang adaptif (*adaptive expert*) dan mampu menyelesaikan permasalahan teknis secara sistematis.

Kendati demikian, kenyataan di lapangan menunjukkan adanya kesenjangan yang signifikan dari kondisi ideal tersebut. Praktik evaluasi formatif pada pembelajaran kejuruan di Sekolah Menengah Kejuruan (SMK) selama ini umumnya masih bersifat konvensional, seragam, dan statis (Robins et al., 2003). Asesmen formatif kerap direduksi menjadi sekadar tes berkala yang memberikan butir soal serupa kepada seluruh siswa tanpa mempertimbangkan keberagaman tingkat pemahaman individu. Di sisi lain, proses pembelajaran praktik kejuruan cenderung terdistorsi pada pencapaian tugas fisik semata (*task completion* mekanis), di mana siswa sekadar meniru panduan operasional tanpa menginternalisasi landasan logika di balik instruksi kerja yang dilakukan (Sudira, 2017) [BUTUH KUTIPAN 2021–2026: Fenomena distorsi pembelajaran praktik kejuruan yang berorientasi sebatas task completion/procedural rigidity]. Berdasarkan studi pendahuluan yang dilakukan di [MASUKKAN HASIL STUDI PENDAHULUAN: Nama SMK Mitra], hasil tes diagnostik awal menunjukkan bahwa sebanyak [MASUKKAN HASIL STUDI PENDAHULUAN: Persentase kegagalan siswa, misal: 68,5%] siswa mengalami kesulitan dalam menalar alur logika teknis dan mengisolasi akar permasalahan saat terjadi gangguan sistem. Kondisi ini diperberat oleh keterbatasan fasilitas laboratorium komputer sekolah, dengan rasio rata-rata [MASUKKAN HASIL STUDI PENDAHULUAN: Rasio komputer, misal: 1 unit PC digunakan bersama oleh 2 siswa], yang memicu ketergantungan antar-siswa dan menyulitkan guru dalam mengukur capaian kognitif individu secara mandiri [BUTUH KUTIPAN 2021–2026: Kendala keterbatasan fasilitas laboratorium dan dampaknya terhadap kemandirian asesmen siswa kejuruan].

Kesenjangan antara tuntutan kompetensi logis dan realitas pembelajaran mekanistik ini menimbulkan persoalan serius terhadap kualitas lulusan kejuruan. Ketiadaan evaluasi formatif adaptif menyebabkan miskonsepsi logika siswa tidak terdeteksi secara dini oleh pendidik. Siswa yang terbiasa berpikir kaku pada panduan manual (*procedural rigidity*) berisiko tinggi mengambil keputusan operasional berbasis spekulasi saat menghadapi anomali teknis baru di lingkungan kerja. Kegagalan dalam menganalisis hubungan sebab-akibat ini dapat memicu kesalahan berantai (*domino error effect*) yang merugikan produktivitas industri. Jika permasalahan ini dibiarkan tanpa intervensi instruksional yang terukur, kesenjangan antara kompetensi lulusan SMK dan kebutuhan kualifikasi tenaga kerja industri akan semakin melebar.

Sejumlah penelitian terdahulu berupaya menjawab tantangan personalisasi pembelajaran melalui pengembangan pemodelan kognitif berbasis data. Salah satu pendekatan yang terbukti efektif adalah algoritma *Deep Knowledge Tracing* (DKT), yang memanfaatkan jaringan saraf tiruan berulang (*Recurrent Neural Network*) untuk memetakan dan memprediksi status penguasaan materi (*knowledge state*) peserta didik secara kontinu (Piech et al., 2015; Abdelrahman et al., 2023). DKT memiliki keunggulan dalam melacak perkembangan pengetahuan laten siswa secara dinamis tanpa memerlukan pemetaan graf konsep manual oleh pakar. Di sisi lain, pada ranah pengelolaan kelas kejuruan, model *blended learning* tipe *Station Rotation* terbukti efektif meningkatkan kemandirian belajar dan mengatasi keterbatasan perangkat fisik melalui pembagian stasiun belajar rotasi (Horn & Staker, 2014; Truitt & Ku, 2018). Namun demikian, terdapat kesenjangan penelitian (*research gap*) yang nyata di mana mayoritas implementasi DKT selama ini masih terisolasi pada platform pembelajaran daring penuh (*fully online learning*) atau sistem tutor cerdas mandiri di perguruan tinggi (Holstein et al., 2019; Vesin et al., 2021). Sangat jarang penelitian yang secara khusus mengintegrasikan algoritma adaptif DKT ke dalam sintaks pembelajaran rotasi tatap muka di ruang kelas kejuruan. Ketiadaan integrasi ini menyebabkan potensi komputasional DKT belum teraktualisasi dalam mendukung orkestrasi pembelajaran aktif dan interaksi langsung di laboratorium sekolah.

Melihat urgensi permasalahan tersebut, diperlukan solusi terpadu melalui perancangan media web evaluasi formatif adaptif berbasis DKT yang disisipkan ke dalam sintaks model *Station Rotation*. Melalui model ini, evaluasi kognitif adaptif difasilitasi melalui perangkat ponsel cerdas (*smartphone*) pribadi siswa di stasiun digital, sementara bimbingan guru dan unjuk kerja praktik berlangsung secara bergantian di laboratorium sekolah dengan rasio komputer yang optimal (*Device-Purpose Split*). Pendekatan ini sangat mendesak dan bernilai strategis karena tidak hanya mengatasi keterbatasan sarana laboratorium fisik, tetapi juga menyediakan dasbor analitik kognitif seketika (*real-time*) bagi pendidik untuk memberikan bimbingan diagnostik yang tepat sasaran demi memperkuat kemampuan berpikir logis siswa kejuruan.

Berdasarkan latar belakang permasalahan, urgensi inovasi asesmen, serta kesenjangan penelitian yang telah dipaparkan, maka penelitian pengembangan (*Research and Development*) ini diarahkan pada rancang bangun sistem dan desain instruksional yang terintegrasi. Sebagai penegasan dari arah dan fokus penelitian yang akan dilaksanakan, maka penelitian ini berjudul:

> **"Pengembangan Web Evaluasi Formatif Adaptif Berbasis Deep Knowledge Tracing (DKT) dalam Pembelajaran Station Rotation untuk Meningkatkan Logical Thinking Siswa SMK"**

---

## 1.2 Rumusan Masalah

Berdasarkan latar belakang masalah dan identifikasi kesenjangan di atas, rumusan masalah dalam penelitian ini adalah:
1. Bagaimana rancang bangun web evaluasi formatif adaptif berbasis algoritma *Deep Knowledge Tracing* (DKT) yang terintegrasi dengan sintaks model pembelajaran *Station Rotation* untuk materi perencanaan dan konfigurasi jaringan?
2. Bagaimana kelayakan (validitas dan kepraktisan) web evaluasi formatif adaptif berbasis DKT yang dikembangkan berdasarkan penilaian ahli materi, ahli media, serta guru praktisi?
3. Bagaimana peningkatan kemampuan *Logical Thinking* siswa setelah menggunakan web evaluasi formatif adaptif berbasis DKT dalam pembelajaran *Station Rotation*, serta bagaimana profil trajektori penguasaan konsep penalaran logis siswa?
4. Bagaimana respons siswa terhadap penggunaan web evaluasi formatif adaptif berbasis DKT dalam model pembelajaran *Station Rotation* ditinjau dari aspek kegunaan (*usability*) dan kepuasan pengguna?

---

## 1.3 Tujuan Penelitian

Berdasarkan rumusan masalah tersebut, tujuan yang hendak dicapai dalam penelitian ini adalah:
1. Menghasilkan produk web evaluasi formatif adaptif berbasis algoritma *Deep Knowledge Tracing* (DKT) yang terintegrasi secara harmonis ke dalam sintaks model pembelajaran *Station Rotation* pada materi perencanaan dan konfigurasi jaringan.
2. Menguji kelayakan produk web evaluasi formatif adaptif berbasis DKT ditinjau dari aspek validitas oleh ahli materi dan ahli media serta kepraktisan penggunaannya dalam pembelajaran di kelas.
3. Mengukur besaran peningkatan kemampuan *Logical Thinking* siswa setelah implementasi web evaluasi formatif adaptif berbasis DKT dalam pembelajaran *Station Rotation*, sekaligus menganalisis pola pertumbuhan pengetahuan (*knowledge growth*) siswa melalui pemodelan DKT.
4. Menganalisis respons siswa terhadap pemanfaatan web evaluasi formatif adaptif berbasis DKT ditinjau dari aspek kegunaan (*usability*) dan kepuasan pengalaman pengguna.

---

## 1.4 Manfaat Penelitian

Adapun manfaat dan signifikansi yang diharapkan dari hasil penelitian pengembangan ini adalah sebagai berikut:
1. **Bagi Sekolah:** Memberikan alternatif solusi instruksional dan model tata kelola kelas inovatif (*Device-Purpose Split*) dalam mengoptimalkan pemanfaatan fasilitas laboratorium komputer yang terbatas, sehingga kualitas pembelajaran kejuruan tetap berjalan efektif tanpa kendala rasio perangkat.
2. **Bagi Guru:** Memberikan instrumen evaluasi formatif cerdas yang dilengkapi dasbor analitik kognitif seketika (*real-time*), sehingga memudahkan guru dalam memetakan miskonsepsi siswa secara objektif dan memberikan intervensi bimbingan diagnostik terarah pada kelompok kecil.
3. **Bagi Siswa:** Membantu siswa melatih kemampuan berpikir logis secara mandiri melalui kuis adaptif dan bantuan bertahap (*scaffolding*) yang terpersonalisasi, serta memberikan kesempatan praktikum mandiri dengan rasio optimal (1 siswa 1 PC) saat beraktivitas di laboratorium komputer.
4. **Bagi Pengelola Lembaga Pendidikan / Pembuat Kebijakan:** Memberikan rujukan empiris mengenai efektivitas integrasi kecerdasan buatan (*Artificial Intelligence in Education*) dan pembelajaran *blended learning* dalam meningkatkan efisiensi sarana prasarana serta mutu pembelajaran vokasi.
5. **Bagi Peneliti:** Menjadi sarana penerapan integrasi ilmu kependidikan, rekayasa perangkat lunak, dan kecerdasan buatan yang diperoleh selama perkuliahan di Program Studi Pendidikan Ilmu Komputer, Fakultas Pendidikan Matematika dan Ilmu Pengetahuan Alam, Universitas Pendidikan Indonesia (FPMIPA UPI), serta menjadi pijakan bagi pengembangan riset AIEd kejuruan selanjutnya.

---

## 1.5 Struktur Organisasi Skripsi

Sistematika penulisan skripsi ini disusun untuk memberikan gambaran menyeluruh mengenai alur penelitian pengembangan yang dilakukan. Adapun rincian muatan setiap bab adalah sebagai berikut:

* **BAB I Pendahuluan:**  
  Bab ini menguraikan latar belakang masalah mengenai urgensi transformasi asesmen formatif adaptif dan penguatan kemampuan berpikir logis (*Logical Thinking*) di SMK, fenomena kesenjangan evaluasi di lapangan, kendala rasio sarana laboratorium komputer, serta *research gap* integrasi AI ke dalam kelas fisik. Bab ini juga memuat rumusan masalah, tujuan penelitian, manfaat penelitian bagi berbagai pihak, serta struktur organisasi skripsi.

* **BAB II Tinjauan Pustaka:**  
  Bab ini menyajikan landasan teoretis yang mendasari penelitian, meliputi: konsep evaluasi formatif adaptif, arsitektur dan pemodelan matematis algoritma *Deep Knowledge Tracing* (DKT), sintaks model pembelajaran *Station Rotation* dengan strategi *Device-Purpose Split*, hakikat kemampuan *Logical Thinking* berbasis kerangka kerja *Test of Logical Thinking* (TOLT) menurut Tobin dan Capie (1981), serta dekomposisi komponen pengetahuan (*Knowledge Components*) pada materi perencanaan dan konfigurasi jaringan. Selain itu, bab ini memaparkan kajian penelitian terdahulu yang relevan dan kerangka berpikir pengembangan sistem.

* **BAB III Metodologi Penelitian:**  
  Bab ini menjelaskan desain penelitian *Research and Development* (R&D) yang mengadopsi model pengembangan ADDIE (*Analyze, Design, Develop, Implement, Evaluate*). Bagian ini merinci prosedur pengembangan sistem web DKT, desain uji coba pembelajaran menggunakan pendekatan *within-subjects repeated measures* (satu kelompok subjek dengan pengukuran pre-test dan post-test), subjek penelitian, instrumen pengumpulan data (lembar validasi ahli, tes kemampuan *Logical Thinking*, dan angket *usability*), serta teknik analisis data yang mencakup analisis kelayakan produk, analisis peningkatan skor *N-Gain*, uji signifikansi statistik (*paired sample t-test* / Wilcoxon), dan visualisasi kurva *knowledge state tracing*.

* **BAB IV Hasil Penelitian dan Pembahasan:**  
  Bab ini memaparkan hasil dari setiap tahapan pengembangan ADDIE, mulai dari temuan analisis kebutuhan awal, rancang bangun antarmuka dan arsitektur model DKT, hasil validasi ahli materi dan media, data kepraktisan dan respons siswa terhadap sistem, hingga analisis hasil *pre-test* dan *post-test*. Pembahasan berfokus pada interpretasi capaian peningkatan kemampuan *Logical Thinking* dan analisis pola perkembangan pengetahuan siswa berbasis DKT guna membuktikan efektivitas media dan model pembelajaran yang dikembangkan.

* **BAB V Kesimpulan, Implikasi, dan Rekomendasi:**  
  Bab ini memuat simpulan akhir mengenai ketercapaian tujuan penelitian yang meliputi keberhasilan rancang bangun sistem web adaptif berbasis DKT, kelayakan produk, efektivitas model *Station Rotation* dalam meningkatkan *Logical Thinking* siswa, serta tingkat penerimaan pengguna. Bab ini diakhiri dengan paparan implikasi pedagogis dan teknologis serta rekomendasi untuk pemanfaatan praktis dan pengembangan penelitian lanjutan.

---

## DAFTAR PUSTAKA

Abdelrahman, G., Wang, Q., & Nunes, B. (2023). Knowledge tracing: A survey. *ACM Computing Surveys*, 55(11), Article 224, 1–37. https://doi.org/10.1145/3569576

Bohle Carbonell, K., Stalmeijer, R. E., Könings, K. D., O'Reilly, R., & van Merriënboer, J. J. (2014). How experts deal with novel situations: A review of adaptive expertise. *Educational Research Review*, 12, 14–29. https://doi.org/10.1016/j.edurev.2014.05.001

Holstein, K., McLaren, B. M., & Aleven, V. (2019). Co-designing a real-time classroom orchestration tool for teachers. *Journal of Learning Analytics*, 6(2), 27–44. https://doi.org/10.18608/jla.2019.62.3

Horn, M. B., & Staker, H. (2014). *Blended: Using disruptive innovation to improve schools*. Jossey-Bass.

Piech, C., Bassen, J., Huang, J., Ganguli, S., Sahami, M., Guibas, L. J., & Sohl-Dickstein, J. (2015). Deep knowledge tracing. *Advances in Neural Information Processing Systems (NeurIPS 2015)*, 28, 505–513.

Republik Indonesia. (2003). *Undang-Undang Republik Indonesia Nomor 20 Tahun 2003 tentang Sistem Pendidikan Nasional*. Lembaran Negara RI Tahun 2003, No. 78. Sekretariat Negara.

Robins, A., Rountree, J., & Rountree, N. (2003). Learning and teaching programming: A review and discussion. *Computer Science Education*, 13(2), 137–172. https://doi.org/10.1076/csed.13.2.137.14200

Sudira, P. (2017). *TVET holistik: Pendekatan, model, dan praksis pendidikan kejuruan*. UNY Press.

Tobin, K. G., & Capie, W. (1981). The development and validation of a group test of logical thinking. *Educational and Psychological Measurement*, 41(2), 413–423. https://doi.org/10.1177/001316448104100220

Truitt, A. A., & Ku, H. Y. (2018). A case study of third grade students' perceptions of the station rotation blended learning model. *Educational Technology Research and Development*, 66(5), 1227–1249. https://doi.org/10.1007/s11423-018-9608-3

Vesin, B., Mangaroska, K., & Giannakos, M. (2021). Intelligent techniques in e-learning: A literature review. *Artificial Intelligence Review*, 54(7), 5295–5345. https://doi.org/10.1007/s10462-021-09998-w

Wardani, R., Harun, H., & Wibawa, A. P. (2022). Vocational education in the industrial revolution 4.0: A systematic literature review. *International Journal of Information and Education Technology*, 12(9), 920–928. https://doi.org/10.18178/ijiet.2022.12.9.1706
