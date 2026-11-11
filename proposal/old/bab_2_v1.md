# BAB II
# TINJAUAN PUSTAKA

## 2.1 Evaluasi Formatif Adaptif dalam Pendidikan Kejuruan

### 2.1.1 Konsep dan Fungsi Evaluasi Formatif Diagnostik
Evaluasi pendidikan merupakan komponen integral dari sistem instruksional yang berfungsi memantau, mengukur, dan meningkatkan mutu proses belajar mengajar. Secara mendasar, literatur pedagogi membedakan dua fungsi utama evaluasi: evaluasi sumatif (*summative assessment*) dan evaluasi formatif (*formative assessment*) (Black & Wiliam, 1998; Shute, 2008). Evaluasi sumatif berorientasi pada pengukuran hasil akhir (*assessment of learning*) yang dilaksanakan pada ujung periode instruksional—seperti ujian akhir semester atau uji sertifikasi kompetensi—dengan tujuan utama memberikan vonis kelulusan atau akreditasi nilai capaian. Sebaliknya, evaluasi formatif merupakan evaluasi yang berorientasi pada perbaikan proses (*assessment for learning*) yang diselenggarakan secara berkelanjutan selama kegiatan pembelajaran berlangsung.

Dalam konteks pendidikan kejuruan di Sekolah Menengah Kejuruan (SMK), evaluasi formatif mengemban fungsi diagnostik yang krusial (Sudira, 2017). Evaluasi formatif diagnostik bertujuan mengidentifikasi kekuatan, kelemahan, serta miskonsepsi kognitif peserta didik sedini mungkin sebelum kelemahan tersebut terakumulasi menjadi kegagalan performa teknis. Evaluasi ini tidak semata-mata menghasilkan skor numerik, melainkan menyediakan informasi balikan (*feedback loop*) yang memetakan kesenjangan (*learning gap*) antara kondisi pemahaman aktual siswa dengan standar kompetensi yang ditargetkan (Sadler, 1989). Umpan balik diagnostik yang efektif memiliki tiga karakteristik utama:
1. **Feed Up:** Memperjelas tujuan pembelajaran dan kriteria keberhasilan yang harus diraih (*Where am I going?*);
2. **Feed Back:** Memberikan informasi objektif mengenai posisi capaian pemahaman saat ini (*How am I going?*); dan
3. **Feed Forward:** Menyajikan rekomendasi tindakan terarah atau strategi perbaikan untuk mencapai pemahaman optimal (*Where to next?*) (Hattie & Timperley, 2007).

Kendati signifikansi evaluasi formatif sangat tinggi, praktik evaluasi di SMK selama ini umumnya masih bersifat konvensional, seragam, dan statis (Robins et al., 2003; Wardani et al., 2022). Instrumen evaluasi formatif kerap direduksi menjadi sekadar kuis kertas (*paper-and-pencil test*) berkala atau tes daring statis (seperti lembar formulir daring) yang mendistribusikan rangkaian butir soal yang identik kepada seluruh peserta didik tanpa mempertimbangkan heterogenitas kecepatan belajar individu. Evaluasi konvensional semacam ini mengasumsikan bahwa seluruh siswa berada pada kesiapan kognitif yang homogen. Akibatnya, siswa yang memiliki pemahaman lambat (*slow learners*) akan mengalami frustrasi dan kegagalan berulang ketika dihadapkan pada butir soal tingkat tinggi tanpa bimbingan konsep prasyarat, sementara siswa berkemampuan tinggi (*fast learners*) mengalami kebosanan karena tidak tertantang secara optimal.

Lebih jauh lagi, ketiadaan evaluasi formatif diagnostik yang dinamis menyebabkan miskonsepsi logika teknis siswa tidak terdeteksi secara dini. Dalam bidang kejuruan teknologi informasi dan jaringan, kegagalan memahami keterhubungan antar-parameter konfigurasi tidak dapat diselesaikan hanya dengan memberikan kunci jawaban yang benar, melainkan memerlukan pelacakan akar penyebab kekeliruan bernalar. Oleh sebab itu, dibutuhkan transformasi paradigma asesmen menuju sistem evaluasi formatif yang responsif dan mampu beradaptasi secara otomatis terhadap dinamika pemahaman individu.

### 2.1.2 Personalisasi Pembelajaran dan Asesmen Adaptif
Heterogenitas karakteristik kognitif peserta didik melahirkan kebutuhan mendesak akan personalisasi pembelajaran (*personalized learning*). Personalisasi pembelajaran menempatkan siswa sebagai pusat instruksional dengan menyesuaikan laju belajar (*pacing*), strategi penyampaian materi, dan tingkat kesulitan tantangan instruksional sesuai dengan kebutuhan, minat, dan profil kompetensi masing-masing individu (Walkington & Bernacki, 2020). Landasan teoretis personalisasi ini berakar kuat pada teori perkembangan kognitif sosial Vygotsky (1978), khususnya konsep *Zone of Proximal Development* (ZPD). ZPD didefinisikan sebagai jarak antara tingkat perkembangan aktual yang ditentukan oleh pemecahan masalah secara mandiri dengan tingkat perkembangan potensial yang dicapai melalui bimbingan orang dewasa atau kolaborasi dengan teman sebaya yang lebih kompeten.

Agar proses belajar berlangsung optimal di dalam ZPD siswa, lingkungan instruksional harus menyediakan bantuan bertahap (*scaffolding*) yang terukur (Wood et al., 1976). *Scaffolding* berfungsi sebagai penyangga kognitif sementara yang diberikan saat siswa menghadapi kesulitan pemecahan masalah, dan secara perlahan dikurangi (*fading*) seiring dengan meningkatnya kemandirian dan penguasaan konsep siswa. Dalam sistem evaluasi formatif modern, mekanisme *scaffolding* dapat berupa pemberian petunjuk terarah (*hints*), penjelasan konsep prasyarat, analogi visual, maupun peringatan terhadap anomali alur logika.

Perkembangan teknologi komputasi melahirkan paradigma *Computerized Adaptive Testing* (CAT) sebagai wahana asesmen terpersonalisasi (Wainer, 2000). CAT tradisional bekerja dengan memilih butir soal berikutnya secara dinamis berdasarkan estimasi kemampuan peserta didik ($\theta$) yang dihitung menggunakan model *Item Response Theory* (IRT). Namun, pendekatan CAT konvensional berbasis IRT memiliki keterbatasan mendasar dalam konteks evaluasi formatif: IRT mengasumsikan parameter kemampuan siswa bersifat statis selama sesi tes berlangsung, serta hanya mengestimasi kemampuan berdimensi tunggal (*unidimensional ability*) tanpa mampu memetakan dinamika pertumbuhan pengetahuan multi-konsep secara sekuensial (van der Linden & Hambleton, 1997).

Integrasi kecerdasan buatan (*Artificial Intelligence in Education* / AIEd) mentransformasikan keterbatasan CAT statis menjadi sistem asesmen formatif adaptif cerdas (Holmes et al., 2019; Luckin et al., 2016). Asesmen formatif adaptif berbasis AI tidak hanya mengukur skor performa, melainkan secara aktif memodelkan kondisi pengetahuan laten siswa (*latent knowledge state*) secara temporal langkah-demi-langkah. Ketika siswa menunjukkan indikasi kebuntuan (*stuck*) atau miskonsepsi, sistem asesmen cerdas dapat mengintervensi dengan menyajikan butir soal diagnostik turunan atau *scaffolding* terpersonalisasi secara otomatis. Dengan demikian, evaluasi formatif adaptif tidak sekadar berfungsi sebagai alat ukur pasif, melainkan bertindak sebagai mitra dialogis kognitif yang memandu siswa melintasi ZPD mereka menuju penguasaan konsep formal yang kokoh.

---

## 2.2 Pemodelan Kognitif Berbasis Deep Knowledge Tracing (DKT)

### 2.2.1 Konsep Knowledge Tracing: Dari BKT Menuju DKT
*Knowledge Tracing* (KT) adalah bidang penelitian fundamental dalam pemodelan kognitif dan *Intelligent Tutoring Systems* (ITS) yang bertujuan memodelkan dan melacak status penguasaan konsep (*knowledge state*) peserta didik secara kontinu berdasarkan riwayat interaksi respons mereka terhadap butir-butir latihan (Corbett & Anderson, 1994; Abdelrahman et al., 2023). Secara formal, persoalan *Knowledge Tracing* dirumuskan sebagai berikut: diberikan sekuens interaksi belajar siswa masa lalu $X = (x_1, x_2, \dots, x_t)$, di mana setiap interaksi $x_t$ mencakup butir soal atau konsep yang dikerjakan serta ketepatan respons siswa, sistem ditugaskan memprediksi probabilitas siswa menjawab dengan benar pada interaksi berikutnya $x_{t+1} = (q_{t+1}, r_{t+1})$ untuk konsep yang relevan.

Selama lebih dari dua dekade, pendekatan dominan dalam *Knowledge Tracing* adalah *Bayesian Knowledge Tracing* (BKT) yang diperkenalkan oleh Corbett dan Anderson (1994). BKT memodelkan penguasaan setiap konsep atau keterampilan (*skill*) sebagai variabel acak biner tersembunyi (apakah konsep sudah dikuasai atau belum dikuasai) menggunakan kerangka *Hidden Markov Model* (HMM). BKT memperbarui probabilitas penguasaan pengetahuan $P(L_t)$ menggunakan aturan inferensi Bayes melalui empat parameter probabilitas tetap:
1. $P(L_0)$: Probabilitas awal penguasaan konsep sebelum latihan (*initial knowledge*);
2. $P(T)$: Probabilitas transisi dari status belum menguasai menjadi menguasai setelah latihan (*probability of learning*);
3. $P(G)$: Probabilitas menebak benar padahal konsep belum dikuasai (*guess*); dan
4. $P(S)$: Probabilitas salah menjawab padahal konsep sudah dikuasai (*slip*).

Kendati BKT memiliki keunggulan berupa kemudahan interpretasi parameter secara probabilistik, model ini memiliki kelemahan struktural yang signifikan:
* **Asumsi Independensi Keterampilan:** BKT memodelkan setiap konsep (*knowledge component*) secara terisolasi dan independen satu sama lain, sehingga gagal menangkap relasi prasyarat hirarkis, asosiasi transfer belajar, atau efek interferensi antar-keterampilan yang kompleks (Abdelrahman et al., 2023).
* **Ketergantungan pada Graf Pakar:** BKT membutuhkan pelabelan dan dekomposisi graf konsep manual (*expert-defined cognitive model*) yang sangat melelahkan, rentan bias subjektif pakar, dan tidak fleksibel terhadap domain pembelajaran yang luas.
* **Kapasitas Representasi Biner yang Sempit:** Asumsi bahwa status pengetahuan hanya bernilai biner (paham vs belum paham) tidak mampu menangkap nuansa pemahaman bertahap atau dinamika degradasi memori (*forgetting effect*).

Untuk mengatasi keterbatasan mendasar BKT, Piech et al. (2015) memperkenalkan paradigma *Deep Knowledge Tracing* (DKT). DKT memanfaatkan jaringan saraf tiruan berulang (*Recurrent Neural Network* / RNN), khususnya unit memori *Long Short-Term Memory* (LSTM), untuk memproyeksikan seluruh riwayat sekuensial interaksi siswa ke dalam vektor ruang tersembunyi (*hidden state vector*) berdimensi tinggi yang kontinu. DKT tidak memerlukan pemetaan graf manual oleh pakar karena model secara otomatis mempelajari keterhubungan laten antar-konsep dari pola data interaksi empiris. Abdelrahman et al. (2023) dalam survei komprehensifnya menegaskan bahwa DKT secara konsisten mengungguli model psikometrik klasik dan BKT dalam akurasi prediksi luaran belajar (AUC meningkat signifikan dari rata-rata 0,67 pada BKT menjadi di atas 0,82 pada DKT).

### 2.2.2 Arsitektur Recurrent Neural Network (RNN) dan LSTM pada DKT
Struktur dasar DKT dibangun di atas kemampuan jaringan saraf tiruan berulang untuk memproses data sekuensial temporal. Pada RNN standar, informasi dari langkah waktu sebelumnya dialirkan ke langkah waktu saat ini melalui sambungan *recurrent*. Namun, RNN standar rentan terhadap permasalahan gradien yang lenyap (*vanishing gradient problem*) atau gradien yang meledak (*exploding gradient problem*) saat memproses sekuens interaksi belajar yang panjang (Hochreiter & Schmidhuber, 1997). Oleh karena itu, arsitektur DKT modern secara luas mengadopsi unit *Long Short-Term Memory* (LSTM) atau unit berpagar (*Gated Recurrent Unit* / GRU).

Arsitektur LSTM mengatasi hambatan gradien dengan memperkenalkan struktur sel memori internal ($c_t$) yang dikontrol oleh tiga gerbang (*gates*) komputasi:
1. **Forget Gate ($f_t$):** Menentukan proporsi informasi dari *cell state* sebelumnya ($c_{t-1}$) yang harus dilupakan atau dibuang, yang secara pedagogis merefleksikan efek keterlupaan konsep oleh siswa seiring berjalannya waktu:
   $$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
2. **Input Gate ($i_t$):** Menentukan informasi baru dari interaksi terkini yang akan disimpan ke dalam *cell state*:
   $$i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$$
   $$\tilde{c}_t = \tanh(W_c \cdot [h_{t-1}, x_t] + b_c)$$
3. **Pembaruan Cell State ($c_t$):** Mengombinasikan memori lama yang dipertahankan dengan kandidat memori baru:
   $$c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t$$
4. **Output Gate ($o_t$):** Mengatur bagian dari memori sel yang akan diteruskan menjadi status kognitif tersembunyi (*hidden state*) $h_t$:
   $$o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$$
   $$h_t = o_t \odot \tanh(c_t)$$

Di mana $\sigma(\cdot)$ adalah fungsi aktivasi sigmoid logistik, $\odot$ menyatakan operasi perkalian elemen-demi-elemen (*Hadamard product*), $W$ mewakili matriks bobot bobot jaringan, dan $b$ mewakili vektor bias. Melalui gerbang-gerbang adaptif ini, vektor tersembunyi $h_t \in \mathbb{R}^d$ berfungsi sebagai representasi matematis komprehensif dari status kognitif laten (*latent knowledge state*) peserta didik pada langkah interaksi ke-$t$.

Dalam penelitian ini, untuk memperkuat presisi estimasi penguasaan materi pada tugas penalaran logis berdimensi jamak, arsitektur DKT dikembangkan dengan mengintegrasikan mekanisme atensi (*Attention Mechanism*) atau model Attentive DKT (Pandey & Karypis, 2019). Mekanisme atensi memberikan bobot relevansi temporal yang dinamis terhadap interaksi-interaksi masa lalu yang memiliki keterkaitan konsep langsung dengan butir soal yang sedang dihadapi siswa saat ini, sehingga mereduksi derau (*noise*) dari latihan materi yang tidak relevan.

### 2.2.3 Formulasi Matematis Pembaruan State dan Probabilitas Penguasaan
Formulasi komputasi DKT mencakup alur transformasi data dari representasi masukan interaksi, pembaruan status tersembunyi, hingga penghitungan fungsi objektif pelatihan (*loss function*):

#### A. Representasi Vektor Masukan ($x_t$)
Misalkan terdapat $M$ butir *Knowledge Components* (KC) atau konsep penalaran yang didefinisikan dalam domain pembelajaran ($k \in \{1, 2, \dots, M\}$). Setiap interaksi siswa pada langkah waktu $t$ direpresentasikan sebagai pasangan tuple $(q_t, r_t)$, di mana $q_t \in \{1, \dots, M\}$ merupakan indeks konsep yang diujikan, dan $r_t \in \{0, 1\}$ adalah biner respons siswa ($0$ jika jawaban salah, $1$ jika jawaban benar). 

Untuk diumpankan ke dalam jaringan saraf, pasangan $(q_t, r_t)$ dikonversikan menjadi representasi vektor *one-hot* $x_t \in \{0, 1\}^{2M}$ dengan dimensi berukuran $2M$:
$$x_t = \begin{cases} e_{q_t}, & \text{jika } r_t = 0 \text{ (salah)} \\ e_{q_t + M}, & \text{jika } r_t = 1 \text{ (benar)} \end{cases}$$
Di mana $e_i$ adalah vektor satuan kanonikal standar dengan nilai 1 pada posisi ke-$i$ dan 0 pada posisi lainnya. Untuk menghindari disparitas dimensi pada ruang input yang renggang (*sparse*), vektor $x_t$ diproyeksikan melalui lapisan penyematan linier (*embedding layer*) $E \in \mathbb{R}^{d_e \times 2M}$:
$$e_t = E \cdot x_t$$

#### B. Propagasi Maju dan Estimasi Probabilitas ($y_t$)
Vektor penyematan $e_t$ diteruskan ke lapisan LSTM bertumpuk (*stacked LSTM*) untuk memperbarui vektor tersembunyi $h_t$:
$$h_t = \text{LSTM}(e_t, h_{t-1})$$
Status tersembunyi $h_t$ kemudian dipetakan ke lapisan keluaran penuh (*dense layer*) menggunakan fungsi aktivasi sigmoid untuk menghasilkan vektor probabilitas penguasaan $y_t \in (0, 1)^M$:
$$y_t = \sigma(W_y h_t + b_y)$$
Elemen ke-$k$ dari vektor luaran, dinotasikan sebagai $y_t[k]$, merepresentasikan estimasi probabilitas bahwa siswa akan berhasil menjawab dengan benar apabila disajikan butir soal yang menguji konsep $k$ pada langkah waktu berikutnya $t+1$.

#### C. Fungsi Kerugian Pelatihan (*Objective Loss Function*)
Pelatihan parameter model DKT dilakukan secara terarah (*supervised learning*) dengan meminimalkan fungsi kerugian entropi silang biner (*binary cross-entropy loss*). Karena pada langkah waktu $t+1$ hanya ada satu konsep aktual $q_{t+1}$ yang dijawab oleh siswa dengan nilai kebenaran $r_{t+1}$, maka fungsi kerugian dihitung secara selektif hanya pada posisi konsep yang diujikan tersebut:
$$\mathcal{L} = -\sum_{t=1}^{T-1} \left[ r_{t+1} \log y_t^{q_{t+1}} + (1 - r_{t+1}) \log (1 - y_t^{q_{t+1}}) \right]$$
Di mana $y_t^{q_{t+1}}$ adalah probabilitas prediksi model untuk konsep $q_{t+1}$ yang dikeluarkan pada langkah waktu $t$. Untuk menjaga stabilitas model dan mencegah fluktuasi probabilitas penguasaan yang tidak realistis antarlangkah yang berdekatan, ditambahkan suku regulasi kehalusan (*wave/smoothness regularization penalty*) (Yeung & Yeung, 2018):
$$\mathcal{L}_{\text{total}} = \mathcal{L} + \lambda_1 \sum_{t} \left\| y_{t+1} - y_t \right\|_2^2$$
Optimasi parameter bobot $\Theta = \{W_f, W_i, W_c, W_o, W_y, E, b\}$ dilakukan melalui propagasi balik melintasi waktu (*Backpropagation Through Time* / BPTT) menggunakan algoritma pengoptimalan Adam (Kingma & Ba, 2014).

### 2.2.4 Pemetaan Komponen Pengetahuan (Knowledge Components / KC)
Algoritma DKT tidak dapat beroperasi secara optimal tanpa adanya taksonomi terstruktur mengenai materi pembelajaran. Dalam pemodelan kognitif, unit atomik dari pengetahuan atau keterampilan yang dipelajari dan diuji disebut sebagai *Knowledge Component* (KC) (Koedinger et al., 2012). Sebuah KC merepresentasikan unit penalaran, konsep teoritis, atau operasi prosedural yang diaktifkan oleh siswa saat menyelesaikan suatu butir tugas.

Dalam penelitian ini, butir-butir soal evaluasi formatif tidak diorganisasikan secara acak, melainkan dipetakan secara ketat ke dalam matriks relasi Q (*Q-matrix*) yang menghubungkan setiap butir soal ($J$) dengan satu atau lebih KC yang relevan ($K$):
$$Q \in \{0, 1\}^{J \times K}$$
Di mana $q_{jk} = 1$ menunjukkan bahwa butir soal ke-$j$ menguji komponen pengetahuan ke-$k$. Dalam domain perencanaan dan konfigurasi jaringan SMK kelas XI, KC dikonstruksikan dengan memadukan elemen silabus kompetensi teknis jaringan dengan indikator penalaran logis formal. Pemetaan KC ini memungkinkan mesin inferensi DKT membedakan secara presisi: apakah kegagalan siswa saat mengonfigurasi jaringan disebabkan oleh ketidakmampuan berhitung proporsi biner, kegagalan mengisolasi variabel galat, atau disorientasi pemahaman tabel perutean.

---

## 2.3 Model Pembelajaran Blended Learning Tipe Station Rotation

### 2.3.1 Konsep Dasar Blended Learning dan Taksonomi Horn & Staker
*Blended learning* secara umum didefinisikan sebagai model desain pendidikan yang memadukan secara harmonis antara pembelajaran tatap muka tradisional di ruang kelas (*face-to-face classroom instruction*) dengan pembelajaran berbantuan teknologi digital berbasis komputer/internet (*online learning*) yang memberikan kendali kepada siswa atas waktu, tempat, jalur, dan kecepatan belajarnya (Graham, 2006). Menurut Horn dan Staker (2014) dari *Christensen Institute*, *blended learning* bukan sekadar melengkapi kelas fisik dengan perangkat gawai digital, melainkan merestrukturisasi modalitas interaksi kelas agar menghasilkan pengalaman belajar yang terintegrasi dan terpersonalisasi.

Horn dan Staker (2014) mengklasifikasikan taksonomi *blended learning* ke dalam empat model arsitektur utama:
1. **Model Rotasi (*Rotation Model*):** Model di mana peserta didik berotasi secara berkala sesuai jadwal tetap atau petunjuk guru di antara berbagai stasiun pembelajaran, dengan sedikitnya satu stasiun berupa pembelajaran daring terstruktur. Varian model ini meliputi: *Station Rotation*, *Lab Rotation*, *Flipped Classroom*, dan *Individual Rotation*.
2. **Model Fleksibel (*Flex Model*):** Pembelajaran daring menjadi tulang punggung kurikulum, sementara guru berada di lokasi untuk memberikan fasilitasi tatap muka secara fleksibel sesuai kebutuhan individual.
3. **Model Campuran Mandiri (*A La Carte Model*):** Siswa mengambil satu mata pelajaran penuh secara daring sembari tetap mengikuti mata pelajaran lainnya di sekolah fisik.
4. **Model Virtual Terkaya (*Enriched Virtual Model*):** Siswa membagi waktu antara sesi tatap muka wajib di kampus sekolah dan penyelesaian sisa materi di luar sekolah secara daring.

Di antara varian model di atas, model *Station Rotation* merupakan model yang paling adaptif dan realistis untuk diimplementasikan di jenjang SMK. Model ini mempertahankan struktur pendampingan guru dan ketersediaan ruang fisik sekolah sembari menyuntikkan efisiensi komputasional teknologi digital ke dalam dinamika kelas harian (Truitt & Ku, 2018).

### 2.3.2 Sintaks Pembelajaran Station Rotation 3 Stasiun
Model *Station Rotation* mengorganisasikan satu ruang kelas/laboratorium menjadi serangkaian stasiun belajar terpisah yang memiliki fokus instruksional berbeda. Peserta didik dibagi ke dalam kelompok-kelompok kecil yang berpindah (*rotate*) dari satu stasiun ke stasiun berikutnya dalam interval waktu yang ditentukan secara presisi. Dalam penelitian pengembangan ini, sintaks pembelajaran dirancang ke dalam **tiga stasiun belajar terpadu** yang diilustrasikan pada Tabel 2.1.

**Tabel 2.1** Sintaks dan Karakteristik 3 Stasiun Pembelajaran *Station Rotation*

| Nama Stasiun | Lingkungan Fisik & Media | Peran Peserta Didik | Peran Pendidik / Sistem |
| :--- | :--- | :--- | :--- |
| **1. Online Adaptive Station** *(Stasiun Evaluasi Digital)* | Ruang kelas teori / Meja reguler; Media: *Smartphone* pribadi masing-masing siswa terhubung ke Web DKT. | Mengerjakan kuis formatif penalaran logis adaptif, menerima umpan balik seketika, dan mengeksplorasi modul bantuan (*scaffolding*) mandiri. | Sistem DKT memetakan status kognitif laten ($h_t$), mengestimasi probabilitas penguasaan ($y_t$), dan menyajikan butir adaptif secara otonom. |
| **2. Teacher-Led Station** *(Stasiun Bimbingan Guru)* | Meja bundar instruktur / Area bimbingan kelompok kecil. | Mendiskusikan miskonsepsi penalaran, mengklarifikasi logika teknis yang rumit, dan menerima penjelasan remediasi. | Guru memanfaatkan dasbor analitik DKT *real-time* untuk memberikan intervensi terarah (*targeted scaffolding*) berbasis titik lemah siswa. |
| **3. Collaborative Hands-on Station** *(Stasiun Praktik Lab)* | Laboratorium Komputer; Media: PC Lab (1 unit PC untuk 1 siswa) & simulator/perangkat jaringan. | Mempraktikkan konfigurasi jaringan nyata (Cisco Packet Tracer / Router Fisik), menguji logika pengalamatan, dan memverifikasi rute. | Guru memantau penerapan unjuk kerja; siswa menguji coba hipotesis penalaran logika yang telah dipelajari di stasiun sebelumnya. |

Sintaks pelaksanaan pembelajaran per pertemuan (alokasi waktu standar 90 menit) diatur ke dalam alur kronologis:
1. **Fase Pembuka & Diagnostik Awal (10 Menit):** Seluruh siswa di kelas secara serentak mengakses Web DKT melalui *smartphone* untuk mengerjakan kuis formatif awal (3–5 butir soal logika). Mesin DKT menginisialisasi vektor status pemahaman awal kelas.
2. **Fase Rotasi Stasiun (2 x 35 Menit = 70 Menit):** Kelas dibagi menjadi dua kelompok besar yang bergerak melintasi stasiun secara bergantian:
   * *Putaran 1 (35 Menit):* Kelompok A berada di Stasiun Praktik Lab (PC Lab 1:1), sementara Kelompok B dibagi antara Stasiun Evaluasi DKT Mandiri dan Stasiun Bimbingan Guru (*Teacher-Led*).
   * *Putaran 2 (35 Menit):* Kelompok bertukar peran secara resiprokal (*crossover*). Kelompok B memasuki Stasiun Praktik Lab, sedangkan Kelompok A mengikuti sesi Evaluasi DKT dan Bimbingan Guru.
3. **Fase Refleksi & Penutup (10 Menit):** Seluruh siswa kembali berkumpul untuk mengerjakan kuis refleksi formatif akhir via Web DKT, di mana sistem memperbarui grafik trajektori pemahaman dan guru merangkum intisari penalaran hari tersebut.

### 2.3.3 Strategi Device-Purpose Split untuk Mengatasi Rasio Lab (1 PC : 2 Siswa)
Hambatan fisik sarana prasarana merupakan realitas umum di mayoritas SMK Indonesia, di mana rasio ketersediaan unit komputer di laboratorium kejuruan kerap tidak sebanding dengan jumlah siswa dalam satu rombongan belajar (sering kali berada pada rasio 1 unit PC untuk 2 orang siswa). Situasi ini memicu dilema pedagogis:
* Terjadinya fenomena pasangan dominan-pasif (*dominant-passive pair*), di mana satu siswa yang lebih vokal/percaya diri mendominasi papan ketik dan tetikus, sedangkan pasangannya menjadi penonton pasif;
* Penilaian formatif di komputer lab menjadi bias karena guru sulit memisahkan antara kemampuan kognitif orisinal individu dengan hasil mencontek konfigurasi teman sebangku (*collusion noise*); dan
* Terdistorsinya proses praktikum menjadi sekadar menyalin skrip konfigurasi tanpa pemahaman konsep (*task completion* mekanis).

Sebagai terobosan instruksional, penelitian ini merumuskan strategi **Device-Purpose Split** (Pemisahan Perangkat Berbasis Peran Instruksional) yang dipadukan ke dalam sintaks *Station Rotation*. Rasionalisasi strategi ini bertumpu pada pemilahan fungsi gawai:
1. **Smartphone Pribadi Siswa $\rightarrow$ Dialokasikan Khusus untuk Aktivitas Kognitif-Formatif Individual:** Hampir seluruh siswa SMK saat ini memiliki *smartphone* pribadi dengan akses internet. Perangkat ini dialokasikan di *Online Adaptive Station* untuk mengerjakan asesmen formatif DKT. Karena dikerjakan di layar genggam masing-masing secara individual, integritas data interaksi respons siswa terjamin 100% murni (*pure individual cognitive trace*), bebas dari campur tangan teman.
2. **PC Laboratorium Komputer $\rightarrow$ Dialokasikan Khusus untuk Aktivitas Unjuk Kerja Psikomotorik Mandiri:** Dengan membagi rombel menjadi rotasi 50% siswa di stasiun teori/evaluasi dan 50% siswa di stasiun laboratorium, kapasitas lab yang semula 1 PC untuk 2 siswa secara matematis tereduksi menjadi **1 PC untuk 1 Siswa (rasio ideal 1:1)**. Setiap siswa memperoleh hak istimewa untuk mengonfigurasi router, memasukkan perintah CLI, dan melacak galat secara mandiri tanpa harus berebut giliran perangkat dengan rekan sekelas.

Integrasi strategi *Device-Purpose Split* membuktikan bahwa keterbatasan fasilitas fisik sekolah kejuruan tidak lagi menjadi penghalang bagi tercapainya mutu pembelajaran berstandar tinggi, asalkan dikelola melalui rekayasa pedagogis dan arsitektur asesmen yang adaptif.

---

## 2.4 Kemampuan Logical Thinking dalam Bidang Jaringan Komputer

### 2.4.1 Hakikat Logical Thinking dan Perkembangan Kognitif Formal
Berpikir logis (*logical thinking*) merupakan kemampuan mental operasional untuk menghubungkan premis-premis, menganalisis hubungan sebab-akibat, menarik kesimpulan yang valid berdasarkan kaidah inferensi yang konsisten, serta menyusun strategi sistematis dalam memecahkan permasalahan yang kompleks (Tobin & Capie, 1981; Piaget, 1972). Dalam teori perkembangan intelektual Jean Piaget, perkembangan kognitif manusia bergerak melalui empat tahapan utama: sensori motorik, pra-operasional, operasional konkret (usia 7–11 tahun), dan operasional formal (usia 11 tahun hingga dewasa) (Inhelder & Piaget, 1958).

Pada tahap operasional konkret, individu hanya mampu memecahkan masalah yang terikat langsung pada objek-objek fisik yang tampak di hadapannya. Sebaliknya, tahap operasional formal ditandai oleh kemampuan berpikir abstrak, hipotesis-deduktif, dan reflektif. Individu pada tahap formal mampu:
1. Memikirkan kemungkinan-kemungkinan hipotesis di luar kenyataan faktual sesaat (*hypothetico-deductive reasoning*);
2. Mengisolasi faktor-faktor penentu dalam sebuah sistem multi-variabel; serta
3. Menggunakan representasi simbolik, logika proporsional, dan penalaran kombinatorik untuk memprediksi konsekuensi logis dari suatu tindakan.

Peserta didik SMK kelas XI (rentang usia 16–17 tahun) secara kronologis seharusnya telah memantapkan operasi berpikir formal. Namun, berbagai studi empiris menunjukkan bahwa sebagian besar remaja dan bahkan orang dewasa belum sepenuhnya mencapai kematangan berpikir formal dalam domain spesifik sains dan rekayasa komputer tanpa adanya stimulus instruksional yang eksplisit (Lawson, 1985; Valanides, 1999). Ketika dihadapkan pada abstraksi arsitektur jaringan komputer—seperti representasi bit biner, topologi virtual, dan aliran paket protokol—banyak siswa mengalami regresi kognitif dan terjebak pada mode berpikir konkret mekanis: mereka hanya mengandalkan hafalan posisi tombol menu antarmuka perangkat lunak tanpa memahami logika komputasional yang mendasarinya.

### 2.4.2 Kerangka Kerja Test of Logical Thinking (TOLT) Tobin & Capie (1981)
Untuk mengukur tingkat penguasaan operasi berpikir formal secara objektif, valid, dan reliabel tanpa memerlukan wawancara klinis Piagetian individual yang rumit, Tobin dan Capie (1981) mengembangkan instrumen standar yang dikenal sebagai **Test of Logical Thinking (TOLT)**. Kerangka kerja TOLT memetakan kemampuan berpikir logis formal ke dalam **lima dimensi penalaran esensial**:

1. **Controlling Variables (Mengontrol dan Mengisolasi Variabel):**  
   Kemampuan merancang penyelidikan yang valid dengan mengidentifikasi variabel bebas, variabel terikat, dan mengontrol variabel kontrol secara konstan. Individu mampu menguji satu faktor independen pada satu waktu untuk memastikan bahwa perubahan yang terjadi pada sistem murni diakibatkan oleh faktor yang diuji tersebut.
2. **Proportional Reasoning (Penalaran Proporsional):**  
   Kemampuan memahami dan mengkalkulasi hubungan matematis rasio, fraksi, dan skala proporsional ($A/B = C/D$), serta mengenali hubungan kovariansi non-linier antara dua kuantitas yang saling bergantung.
3. **Combinatorial Reasoning (Penalaran Kombinatorik):**  
   Kemampuan membangkitkan secara sistematis seluruh kombinasi atau permutasi yang mungkin dari serangkaian variabel atau kondisi tanpa ada alternatif yang terlewatkan atau terulang.
4. **Probabilistic Reasoning (Penalaran Probabilistik):**  
   Kemampuan memperhitungkan peluang terjadinya suatu peristiwa di bawah kondisi ketidakpastian, mengenali fluktuasi acak versus hukum deterministik, serta membuat keputusan optimal berbasis ekspektasi probabilitas kejadian.
5. **Correlational Reasoning (Penalaran Korelasional):**  
   Kemampuan mengevaluasi ada atau tidaknya hubungan asosiatif timbal-balik antara dua variabel atau kejadian, dengan membandingkan data konfirmasi ($A$ terjadi bersama $B$) terhadap data diskonfirmasi, serta membedakan hubungan korelasional dari hubungan kausalitas semu.

Validitas konstruk TOLT telah teruji secara ekstensif lintas dekade dalam memprediksi keberhasilan akademik siswa pada bidang sains, teknologi, rekayasa, dan matematika (STEM) (Tobin & Capie, 1981; Valanides, 1999).

### 2.4.3 Kontekstualisasi 5 Dimensi TOLT pada Materi TKJ
Dalam penelitian ini, kelima dimensi penalaran logis formal TOLT didekontekstualisasikan dari domain laboratorium sains murni dan direkontekstualisasikan secara mendalam ke dalam aktivitas kompetensi kejuruan Teknik Komputer dan Jaringan (TKJ), khususnya pada materi perencanaan pengalamatan, konfigurasi rute, dan pelacakan galat sistem jaringan. Tabel 2.2 merinci matrik operasionalisasi 5 dimensi TOLT ke dalam domain spesifik TKJ.

**Tabel 2.2** Operasionalisasi dan Kontekstualisasi 5 Dimensi TOLT dalam Domain TKJ

| Dimensi TOLT (Tobin & Capie, 1981) | Definisi Kognitif Umum | Manifestasi Keterampilan pada Domain Jaringan Komputer (TKJ) | Indikator Perilaku Siswa yang Terukur |
| :--- | :--- | :--- | :--- |
| **1. Controlling Variables** | Mengisolasi variabel independen saat menguji sistem multi-faktor. | **Troubleshooting Koneksi & Isolasi Lapangan Gangguan:** Menguji tumpukan protokol TCP/IP lapis demi lapis secara sekuensial (misal: uji loopback `127.0.0.1` $\rightarrow$ uji gateway lokal $\rightarrow$ uji DNS) tanpa mengubah setting IP router secara acak. | Siswa mampu menentukan titik anomali koneksi dengan mengubah hanya 1 parameter uji pada satu waktu tanpa merusak parameter yang sudah berfungsi. |
| **2. Proportional Reasoning** | Menghitung rasio matematis dan relasi skala kuantitatif. | **Kalkulasi Prefix CIDR vs Kapasitas Host (Subnetting):** Memahami hubungan eksponensial invers ($2^{32-n} - 2$) antara panjang bit prefix ($/n$) dengan jumlah alokasi IP host valid dan kapasitas pemborosan alamat. | Siswa mampu menentukan prefix paling proporsional untuk link point-to-point (`/30`) vs segmen LAN (`/26`) secara efisien tanpa mubazir IP. |
| **3. Combinatorial Reasoning** | Menyusun permutasi dan kombinasi partisi sistem secara tuntas. | **Desain Partisi Subnet VLSM Non-Overlapping:** Membagi satu blok alamat global (`/24`) ke dalam partisi-partisi variabel dengan memprioritaskan blok host terbesar ke terkecil tanpa ada blok yang tumpang tindih. | Siswa mampu menyusun skema alokasi rentang alamat jaringan untuk 3 atau lebih segmen ruang secara lengkap dan bebas tabrakan IP. |
| **4. Probabilistic Reasoning** | Memprediksi probabilitas keterjadian di bawah parameter seleksi. | **Analisis Pemilihan Rute Terbaik (*Best Path*) & Metrik:** Menilai kemungkinan router memilih rute data berdasarkan hierarki *Administrative Distance* (AD), metrik hop/bandwidth, dan risiko *packet loss*. | Siswa mampu memprediksi jalur pengiriman paket yang pasti dilalui router saat terdapat rute statis utama (AD=1) dan rute cadangan (AD=5). |
| **5. Correlational Reasoning** | Menganalisis korelasi timbal-balik antar-gejala dan kode status. | **Interpretasi Korelasi Pesan Galat Jaringan (ICMP):** Mengorelasikan jenis respons protokol ICMP (*Request Timed Out* vs *Destination Host Unreachable*) terhadap letak kegagalan lapisan jaringan. | Siswa mampu mengorelasikan bahwa pesan DHU berkaitan dengan kegagalan resolusi ARP lokal, sedangkan RTO berkaitan dengan rute/firewall remote. |

Melalui operasionalisasi ini, *Logical Thinking* tidak lagi diperlakukan sebagai konsep psikologi abstrak, melainkan diukur secara presisi melalui butir-butir evaluasi kejuruan yang mencerminkan pemecahan masalah teknis nyata.

---

## 2.5 Materi Perencanaan dan Konfigurasi Jaringan sebagai Domain Pengetahuan

### 2.5.1 Perencanaan Pengalamatan Jaringan (Subnetting, CIDR, VLSM)
Pengalamatan *Internet Protocol* versi 4 (IPv4) merupakan fondasi logika paling fundamental dalam arsitektur jaringan komputer. Alamat IPv4 terdiri atas 32 bit biner yang dibagi menjadi 4 oktet desimal bertitik (*dotted-decimal notation*). Alamat IP secara logis terbagi menjadi dua porsi: *Network ID* (identitas segmen jaringan) dan *Host ID* (identitas perangkat fisik di dalam segmen tersebut), yang dibatasi oleh sebuah *Subnet Mask* (Lammle, 2020; Odom, 2020).

Dalam silabus Kurikulum Merdeka Konsentrasi Keahlian TKJ kelas XI, materi perencanaan pengalamatan mencakup tiga tahapan penalaran matematis-logis:
1. **Classless Inter-Domain Routing (CIDR):** Notasi prefiks garis miring (misal: `/24`, `/27`) yang merepresentasikan jumlah bit biner 1 berurutan pada subnet mask, menggantikan sistem kelas IPv4 tradisional (*Classful*) yang kaku.
2. **Fixed-Length Subnet Masking (FLSM):** Pembagian blok jaringan menjadi beberapa subnet yang memiliki ukuran kapasitas host identik.
3. **Variable-Length Subnet Masking (VLSM):** Teknik partisi subnetting tingkat lanjut di mana setiap subnet dialokasikan masker dengan panjang prefiks yang bervariasi sesuai dengan kebutuhan riil masing-masing segmen (Kurose & Ross, 2021). VLSM menuntut kemampuan berpikir kombinatorik tingkat tinggi: perancang jaringan harus mengurutkan segmen berdasarkan kebutuhan host terbesar, mengalokasikan blok bit perpangkatan dua terdekat ($2^h - 2 \ge \text{kebutuhan}$), menentukan alamat *Network*, rentang *Host Valid*, dan alamat *Broadcast*, sebelum melanjutkan partisi ke segmen berikutnya. Kesalahan alur pada satu segmen akan mengakibatkan tabrakan alamat (*overlapping network*) yang melumpuhkan rute perutean.

### 2.5.2 Konfigurasi Perangkat Jaringan (Routing Statis dan Routing Table)
Perutean (*routing*) adalah proses logika di mana perangkat router meneruskan paket data melintasi interkoneksi jaringan komputer dari jaringan asal (*source*) menuju jaringan tujuan (*destination*) pada Lapisan Jaringan (*Network Layer* / Layer 3 model OSI) (Tanenbaum et al., 2021). Keputusan perutean dieksekusi berdasarkan informasi yang tersimpan di dalam tabel perutean (*routing table*).

Pada konfigurasi perutean statis (*static routing*), administrator jaringan memasukkan entri rute secara manual ke dalam router. Struktur entri perutean statis memerlukan pemahaman logika relasional antara empat parameter utama:
* **Network Destination:** Alamat subnet tujuan yang hendak dijangkau;
* **Subnet Mask / Prefix:** Batasan ukuran segmen tujuan;
* **Next-Hop IP Address:** Alamat IP antarmuka router tetangga berikutnya yang menjadi pintu gerbang perlintasan paket; serta
* **Outgoing Interface:** Port fisik atau logis lokal tempat paket dikeluarkan (misal: `ether1`, `GigabitEthernet0/0`).

Siswa kerap mengalami kebuntuan bernalar saat membedakan antara konsep *Default Gateway* pada PC klien dengan *Next-Hop* pada router. *Default Gateway* adalah alamat IP router lokal yang berfungsi sebagai pintu keluar pertama bagi host klien menuju dunia luar, sedangkan *Next-Hop* adalah alamat hop berikutnya di sepanjang rantai antar-router. Kegagalan menalar arah aliran rute ini mengakibatkan terjadinya lingkaran perutean (*routing loop*) atau paket terbuang (*black hole*).

### 2.5.3 Analisis Troubleshooting Koneksi Jaringan (ICMP, RTO, DHU)
Pelacakan gangguan (*troubleshooting*) merupakan wujud tertinggi dari integrasi kemampuan kognitif dan keterampilan teknis kejuruan. Ketika konektivitas antar-perangkat gagal, teknisi menguji ketercapaian host (*reachability*) menggunakan utilitas diagnostik berbasis protokol *Internet Control Message Protocol* (ICMP), seperti perintah `ping` (*Packet Internet Groper*) dan `traceroute` (Odom, 2020).

Dua kode status galat ICMP yang paling sering disalahpahami oleh siswa adalah:
1. **Destination Host Unreachable (DHU):**  
   Pesan galat yang diinisiasi oleh router lokal atau perangkat pengirim itu sendiri ketika sistem gagal menemukan rute logis menuju jaringan tujuan (ketiadaan entri pada *routing table*) atau ketika protokol *Address Resolution Protocol* (ARP) gagal memetakan alamat IP tujuan ke alamat fisik (*MAC address*) pada jaringan lokal yang sama. Pesan ini mencerminkan kegagalan pada ranah logika lokal atau keterhubungan segmen Layer 2 / Layer 3 langsung.
2. **Request Timed Out (RTO):**  
   Pesan galat yang terjadi ketika paket permintaan gema ICMP (*echo request*) berhasil dikirimkan ke luar jaringan lokal, namun perangkat pengirim tidak menerima paket balasan (*echo reply*) hingga batas ambang waktu tunggu kedaluwarsa. Kondisi ini berkorelasi dengan pemutusan jalur transmisi di router tengah, kesalahan konfigurasi rute balik (*return routing*), atau blokade oleh dinding api (*firewall/access list*) pada perangkat tujuan.

Analisis pemecahan masalah ini menuntut siswa menggunakan penalaran mengontrol variabel dan penalaran korelasional secara simultan guna mengisolasi letak anomali konfigurasi perangkat.

---

## 2.6 Kajian Penelitian Terdahulu yang Relevan (Matriks Sintesis Literatur)

Untuk meletakkan posisi kebaruan (*novelty*) dan orisinalitas penelitian ini di dalam peta riset internasional, dilakukan penelaahan kritis terhadap literatur-literatur bereputasi terkini (rentang 2020–2025) yang mengkaji pemodelan *Deep Knowledge Tracing*, evaluasi adaptif, serta model *Station Rotation*. Matriks sintesis kajian penelitian terdahulu disajikan pada Tabel 2.3.

**Tabel 2.3** Matriks Komparasi dan Sintesis Penelitian Terdahulu yang Relevan

| Peneliti & Tahun | Judul Penelitian | Metode & Model AI | Temuan Utama | Persamaan dengan Penelitian Ini | Keterbatasan / Kesenjangan (*Gap*) yang Diisi Skripsi Ini |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Abdelrahman et al. (2023)** | *Knowledge Tracing: A Survey* (ACM Computing Surveys) | Survei komprehensif algoritma BKT, DKT, DKVMN, dan Graph KT. | DKT berbasis deep learning secara konsisten mengungguli model probabilistik klasik dalam menangkap representasi pengetahuan laten non-linier siswa. | Menjadikan algoritma DKT sebagai landasan komputasional pelacakan status kognitif siswa. | Bersifat kajian teoritis pustaka; tidak mengembangkan platform perangkat lunak terapan maupun menguji efektivitas pada kelas fisik kejuruan. |
| **Holstein et al. (2019)** | *Co-Designing a Real-Time Classroom Orchestration Tool for Teachers* (JLA) | *Learning Analytics Dashboard* (Lumilo) berbasis kacamata pintar di kelas tutor cerdas. | Dasbor analitik *real-time* meningkatkan efektivitas guru dalam memberikan bantuan kognitif yang merata kepada siswa yang mengalami kebuntuan (*stuck*). | Menggunakan konsep orkestrasi dasbor guru *real-time* untuk memandu bimbingan kelompok kecil (*Teacher-Led*). | Sistem dirancang untuk kelas tutor komputer penuh (1 siswa 1 PC canggih); tidak mengintegrasikan sintaks rotasi fisik untuk mengatasi kendala rasio lab sekolah berkembang. |
| **Vesin et al. (2021)** | *Intelligent Techniques in E-Learning: A Literature Review* (AI Review) | Reviu implementasi AI, machine learning, dan sistem adaptif dalam platform e-learning. | Personalisasi materi dan tes adaptif meningkatkan retensi pengetahuan siswa, namun mayoritas sistem terisolasi pada lingkungan belajar daring mandiri (*desktop silo*). | Mengembangkan sistem web asesmen formatif adaptif dengan penyajian konten berbasis status pemahaman. | Mengabaikan dimensi unjuk kerja praktik fisik; penelitian skripsi ini mengisi celah dengan menghubungkan evaluasi adaptif ke unjuk kerja lab via *Station Rotation*. |
| **Truitt & Ku (2018)** | *A Case Study of Students' Perceptions of the Station Rotation Blended Learning Model* (ETR&D) | Studi kualitatif & kuantitatif implementasi *Station Rotation* di sekolah dasar/menengah. | Siswa menunjukkan motivasi, keterlibatan aktif, dan kepuasan belajar yang sangat tinggi pada lingkungan rotasi kelompok kecil dibanding pembelajaran klasikal. | Menerapkan sintaks *Station Rotation* 3 stasiun untuk mengelola dinamika kelas secara aktif. | Evaluasi pada stasiun digital masih menggunakan materi statis seragam tanpa AI adaptif; serta tidak mengukur kemampuan penalaran tingkat tinggi (*Logical Thinking*). |
| **Wang et al. (2022)** | *Attentive Knowledge Tracing: Modeling Dynamic Student Knowledge with Attention Mechanisms* (IEEE TLT) | Arsitektur Attentive DKT (Akt/LSTM) pada dataset asesmen pemrograman berskala besar. | Penggabungan mekanisme atensi pada model DKT meningkatkan nilai AUC hingga 0,83 dan memberikan bobot relevansi latihan masa lalu secara interpretabel. | Mengadopsi prinsip DKT dengan mekanisme atensi untuk memprediksi luaran kebenaran konsep sekuensial. | Diterapkan pada latihan sintaks coding daring murni; belum pernah dikontekstualisasikan untuk melacak 5 dimensi penalaran TOLT pada konfigurasi jaringan SMK. |

Berdasarkan telaah sintesis pada Tabel 2.3, **kebaruan ilmiah (*novelty*) dari penelitian ini** terletak pada konvergensi unik tiga elemen yang belum pernah disatukan dalam penelitian sebelumnya:
1. **Domain Kognitif Spesifik:** Mengontekstualisasikan algoritma DKT untuk melacak dan memprediksi 5 dimensi penalaran logis formal berbasis kerangka *Test of Logical Thinking* (TOLT Tobin & Capie, 1981) pada materi perencanaan dan konfigurasi jaringan komputer;
2. **Desain Orkestrasi Instruksional:** Menanamkan sistem web DKT langsung ke dalam sintaks rotasi fisik kelas kejuruan (*Station Rotation*); serta
3. **Solusi Manajerial Fasilitas:** Memperkenalkan strategi *Device-Purpose Split* yang memanfaatkan komputasi cerdas di *smartphone* pribadi siswa untuk membebaskan ruang laboratorium komputer, sehingga mampu memecahkan masalah rasio sarana 1 PC : 2 Siswa menjadi 1 PC : 1 Siswa secara elegan.

---

## 2.7 Kerangka Berpikir (Conceptual Framework)

Kerangka berpikir dalam penelitian pengembangan ini dibangun atas premis bahwa rendahnya kemampuan berpikir logis (*Logical Thinking*) siswa SMK kelas XI TKJ merupakan akibat dari dua faktor yang saling berkelindan:
1. Praktik evaluasi formatif yang masih bersifat konvensional, seragam, dan statis sehingga gagal mendeteksi miskonsepsi penalaran logika secara dini; serta
2. Keterbatasan sarana laboratorium komputer (rasio 1 PC : 2 Siswa) yang memicu fenomena pasangan dominan-pasif, menurunkan kemandirian asesmen, dan mendistorsi pembelajaran praktik menjadi sekadar penyelesaian tugas fisik mekanis (*task completion*).

Sebagai solusi konseptual terpadu, dirancang suatu intervensi komputasional dan instruksional berupa **Pengembangan Web Evaluasi Formatif Adaptif Berbasis Deep Knowledge Tracing (DKT) yang diintegrasikan ke dalam Model Blended Learning Tipe Station Rotation**. 

Alur logika kerangka berpikir penelitian ini digambarkan secara skematis pada Gambar 2.1 dan dinarasikan sebagai berikut:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                     KONDISI AWAL                                       │
│ • Pembelajaran praktik kejuruan terjebak pada procedural rigidity & task completion.   │
│ • Evaluasi formatif bersifat statis, seragam, dan tidak diagnostik.                    │
│ • Keterbatasan lab (1 PC : 2 Siswa) memicu fenomena dominant-passive pair.             │
│ • Kemampuan Logical Thinking siswa rendah (kesulitan VLSM, routing, & troubleshooting).│
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              TINDAKAN / PENGEMBANGAN (R&D)                             │
│ 1. Pengembangan Web Evaluasi Adaptif DKT:                                              │
│    - Pemodelan kognitif sekuensial RNN/LSTM + Attention Mechanism.                     │
│    - Dekomposisi 5 Dimensi TOLT ke dalam Knowledge Components (KC) Jaringan.           │
│    - Inferensi probabilitas penguasaan (yt) & pemberian scaffolding adaptif.           │
│ 2. Desain Pembelajaran Station Rotation dengan Strategi Device-Purpose Split:          │
│    - Stasiun 1: Evaluasi Adaptif Mandiri via Smartphone Pribadi Siswa.                 │
│    - Stasiun 2: Bimbingan Diagnostik Guru Berbasis Dasbor Analitik DKT Real-Time.      │
│    - Stasiun 3: Praktik Konfigurasi Mandiri di PC Lab dengan Rasio Optimal (1 PC:1 Siswa).│
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               KONDISI AKHIR YANG DIHARAPKAN                            │
│ • Terwujudnya sistem web evaluasi formatif DKT yang valid, praktis, dan akurat.        │
│ • Peningkatan signifikan kemampuan Logical Thinking siswa (N-Gain kategori sedang-tinggi).│
│ • Terpetakannya trajektori penguasaan 5 dimensi penalaran TOLT tiap siswa via DKT.    │
│ • Terselesaikannya kendala rasio lab komputer melalui orkestrasi kelas yang efisien.   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
**Gambar 2.1** Bagan Alur Kerangka Berpikir Pengembangan Sistem Web DKT dalam *Station Rotation*

Melalui integrasi ini, siswa memperoleh latihan penalaran individual yang adaptif di layar telepon pintar mereka, guru memperoleh wawasan analitik seketika untuk membimbing siswa yang mengalami kesulitan (*stuck*), dan setiap siswa memperoleh hak penuh untuk mengoperasikan komputer laboratorium secara mandiri. Sinergi antara keunggulan komputasional kecerdasan buatan (*AI in Education*) dan keunggulan pedagogis pembelajaran rotasi (*Station Rotation*) diharapkan secara efektif memutus rantai berpikir kaku prosedural dan mengantarkan peserta didik menjadi teknisi jaringan yang berkarakter pakar adaptif (*adaptive experts*).

---

## DAFTAR PUSTAKA

Abdelrahman, G., Wang, Q., & Nunes, B. (2023). Knowledge tracing: A survey. *ACM Computing Surveys*, 55(11), Article 224, 1–37. https://doi.org/10.1145/3569576

Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice*, 5(1), 7–74. https://doi.org/10.1080/0969595980050102

Corbett, A. T., & Anderson, J. R. (1994). Knowledge tracing: Modeling the acquisition of procedural knowledge. *User Modeling and User-Adapted Interaction*, 4(4), 253–278. https://doi.org/10.1007/BF01099821

Graham, C. R. (2006). Blended learning systems: Definition, current trends, and future directions. Dalam C. J. Bonk & C. R. Graham (Ed.), *The handbook of blended learning: Global perspectives, local designs* (hlm. 3–21). Pfeiffer Publishing.

Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research*, 77(1), 81–112. https://doi.org/10.3102/003465430298487

Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. *Neural Computation*, 9(8), 1735–1780. https://doi.org/10.1162/neco.1997.9.8.1735

Holmes, W., Bialik, M., & Fadel, C. (2019). *Artificial intelligence in education: Promises and implications for teaching and learning*. Center for Curriculum Redesign.

Horn, M. B., & Staker, H. (2014). *Blended: Using disruptive innovation to improve schools*. Jossey-Bass.

Inhelder, B., & Piaget, J. (1958). *The growth of logical thinking from childhood to adolescence*. Basic Books.

Kingma, D. P., & Ba, J. (2014). Adam: A method for stochastic optimization. *arXiv preprint arXiv:1412.6980*. https://doi.org/10.48550/arXiv.1412.6980

Koedinger, K. R., Corbett, A. T., & Perfetti, C. (2012). The Knowledge-Learning-Instruction (KLI) framework: Bridging the science-practice chasm to enhance robust student learning. *Cognitive Science*, 36(5), 757–798. https://doi.org/10.1111/j.1551-6709.2012.01245.x

Kurose, J. F., & Ross, K. W. (2021). *Computer networking: A top-down approach* (Edisi ke-8). Pearson.

Lammle, T. (2020). *Cisco Certified Network Associate (CCNA) study guide: Exam 200-301*. Sybex / Wiley.

Lawson, A. E. (1985). A review of research on formal reasoning and science teaching. *Journal of Research in Science Teaching*, 22(7), 569–617. https://doi.org/10.1002/tea.3660220702

Luckin, R., Holmes, W., Griffiths, M., & Forcier, L. B. (2016). *Intelligence unleashed: An argument for AI in education*. Pearson Education.

Odom, W. (2020). *CCNA 200-301 official cert guide, Volume 1 & 2*. Cisco Press.

Pandey, S., & Karypis, G. (2019). A self-attentive model for knowledge tracing. *Proceedings of the 12th International Conference on Educational Data Mining (EDM 2019)*, 384–389.

Piaget, J. (1972). Intellectual evolution from adolescence to adulthood. *Human Development*, 15(1), 1–12. https://doi.org/10.1159/000271225

Piech, C., Bassen, J., Huang, J., Ganguli, S., Sahami, M., Guibas, L. J., & Sohl-Dickstein, J. (2015). Deep knowledge tracing. *Advances in Neural Information Processing Systems (NeurIPS 2015)*, 28, 505–513.

Robins, A., Rountree, J., & Rountree, N. (2003). Learning and teaching programming: A review and discussion. *Computer Science Education*, 13(2), 137–172. https://doi.org/10.1076/csed.13.2.137.14200

Sadler, D. R. (1989). Formative assessment and the design of instructional systems. *Instructional Science*, 18(2), 119–144. https://doi.org/10.1007/BF00117714

Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research*, 78(1), 153–189. https://doi.org/10.3102/0034654307313795

Sudira, P. (2017). *TVET holistik: Pendekatan, model, dan praksis pendidikan kejuruan*. UNY Press.

Tanenbaum, A. S., Feamster, N., & Wetherall, D. (2021). *Computer networks* (Edisi ke-6). Pearson.

Tobin, K. G., & Capie, W. (1981). The development and validation of a group test of logical thinking. *Educational and Psychological Measurement*, 41(2), 413–423. https://doi.org/10.1177/001316448104100220

Truitt, A. A., & Ku, H. Y. (2018). A case study of third grade students' perceptions of the station rotation blended learning model. *Educational Technology Research and Development*, 66(5), 1227–1249. https://doi.org/10.1007/s11423-018-9608-3

Valanides, N. (1999). Formal reasoning abilities and school success in selected science subjects of normal track and technical track Cypriot students. *School Science and Mathematics*, 99(8), 415–424. https://doi.org/10.1111/j.1949-8594.1999.tb17502.x

van der Linden, W. J., & Hambleton, R. K. (Ed.). (1997). *Handbook of modern item response theory*. Springer. https://doi.org/10.1007/978-1-4757-2691-6

Vesin, B., Mangaroska, K., & Giannakos, M. (2021). Intelligent techniques in e-learning: A literature review. *Artificial Intelligence Review*, 54(7), 5295–5345. https://doi.org/10.1007/s10462-021-09998-w

Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.

Wainer, H. (Ed.). (2000). *Computerized adaptive testing: A primer* (Edisi ke-2). Lawrence Erlbaum Associates.

Walkington, C., & Bernacki, M. L. (2020). Appraising research on personalized learning: Definitions, theoretical perspectives, cues, and interventions. *Computers in Human Behavior*, 107, Article 105822. https://doi.org/10.1016/j.chb.2018.10.049

Wang, Q., Abdelrahman, G., & Nunes, B. (2022). Attentive knowledge tracing: Modeling dynamic student knowledge with attention mechanisms. *IEEE Transactions on Learning Technologies*, 15(4), 488–501. https://doi.org/10.1109/TLT.2022.3188988

Wardani, R., Harun, H., & Wibawa, A. P. (2022). Vocational education in the industrial revolution 4.0: A systematic literature review. *International Journal of Information and Education Technology*, 12(9), 920–928. https://doi.org/10.18178/ijiet.2022.12.9.1706

Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry*, 17(2), 89–100. https://doi.org/10.1111/j.1469-7610.1976.tb00381.x

Yeung, C. K., & Yeung, D. Y. (2018). Addressing two problems in deep knowledge tracing via monotonicity and smoothness regularization. *Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*, 1009–1017. https://doi.org/10.1145/3219819.3219904
