PROPOSAL
RANCANG BANGUN GIM SIMULASI DEBUGGING DENGAN
SCAFFOLDING SINTAKS PROBLEM BASED LEARNING PADA
MATERI ARSITEKTUR KOMPUTER UNTUK PENGUATAN
COMPUTATIONAL THINKING
disusun untuk memenuhi salah satu syarat untuk mengambil mata kuliah skripsi
oleh:
Fajari Arkan Fadhlurrahman
2304794
PROGRAM STUDI PENDIDIKAN ILMU KOMPUTER
FAKULTAS PENDIDIKAN MATEMATIKA ILMU PENGETAHUAN ALAM
UNIVERSITAS PENDIDIKAN INDONESIA
2025

KATA PENGANTAR
Tiada kata yang mewakili perasaan saya saat ini kecuali rasa syukur. Untuk
itu, saya ucapkan terima kasih kepada Tuhan atas rahmat-Nya, sayang dapat
menyusun proposal ini dengan baik. Meski mendapatkan kendala, tapi saya bisa
melaluinya sehingga proposal berjudul "Rancang bangun gim simulasi debugging
dengan scaffolding sintaks problem based learning pada materi arsitektur komputer
untuk penguatan computational thinking" ini dapat terselesaikan tepat waktu.
Penulis sangat berharap semoga proposal ini dapat menambah pengetahuan
dan pengalaman bagi pembaca. Bahkan saya berharap lebih jauh lagi agar proposal
ini bisa pembaca praktikkan dalam kehidupan sehari-hari.
Bagi saya sebagai penyusun merasa bahwa masih banyak kekurangan dalam
penyusunan proposal ini karena keterbatasan pengetahuan dan pengalaman saya.
Untuk itu saya sangat mengharapkan kritik dan saran yang membangun dari
pembaca demi kesempurnaan proposal ini.
Bandung, 16 Desember 2025
Penulis
i

DAFTAR ISI
KATA PENGANTAR ............................................................................................. i
DAFTAR ISI ........................................................................................................... ii
BAB I PENDAHULUAN ....................................................................................... 1
1.1. Latar Belakang ........................................................................................ 1
1.2. Rumusan Masalah ................................................................................... 4
1.3. Tujuan Penelitian .................................................................................... 4
1.4. Manfaat/Signifikansi Penelitian .............................................................. 4
1.5. Struktur Organisasi Skripsi ..................................................................... 5
BAB II TINJAUAN PUSTAKA ............................................................................. 7
2.1. Peta Literatur ........................................................................................... 7
2.2. Kajian Teori ............................................................................................ 8
2.2.1. Gim Edukasi & Simulasi ................................................................. 8
2.2.2. Kerangka Teoretis Pembelajaran Berbasis Gim ............................. 9
2.2.3. Materi Arsitektur Komputer .......................................................... 11
2.2.4. Model Pembelajaran Problem Based Learning (PBL) ................. 13
2.2.5. Computational Thinking (Berpikir Komputasional) ..................... 16
2.3. Kajian Metodologis ............................................................................... 18
2.3.1. Model Pengembangan Sistem ....................................................... 18
2.3.2. Perangkat Pengembangan Sistem ................................................. 20
2.3.3. Instrumen Evaluasi Kualitas Media (Validitas & Usabilitas) ....... 21
2.3.4. Desain Penelitian Eksperimen....................................................... 22
2.3.5. Asesmen Computational Thinking (CT) ........................................ 23
2.3.6. Teknik Pengumpulan Data ............................................................ 25
2.3.7. Teknik Analisis Data Statistik ....................................................... 26
2.4. Penelitian yang Relevan (State of the Art) ............................................ 28
ii

2.5. Kerangka Berpikir ................................................................................. 29
2.5.1. Kondisi Awal (Masalah) ............................................................... 29
2.5.2. Analisis Kesenjangan (Gap Analysis) ........................................... 30
2.5.3. Solusi (Intervensi) ......................................................................... 30
BAB III METODOLOGI PENELITIAN.............................................................. 31
3.1. Jenis Penelitian ...................................................................................... 31
3.2. Prosedur Penelitian................................................................................ 31
3.3. Desain pengembangan media ................................................................ 32
3.3.1. Tahap Analisis (Analyze) .............................................................. 34
3.3.2. Tahap Desain (Design) .................................................................. 34
3.3.3. Tahap Pengembangan (Develop) .................................................. 35
3.3.4. Tahap Implementasi (Implement) ................................................. 35
3.3.5. Tahap Evaluasi (Evaluate) ............................................................ 36
3.4. Subjek dan Tempat Penelitian ............................................................... 36
3.5. Instrumen Pengumpulan Data ............................................................... 36
3.5.1. Instrumen Non-Tes........................................................................ 36
3.5.2. Instrumen Tes ................................................................................ 37
3.6. Teknik Analisis Data ............................................................................. 37
3.6.1. Analisis Data Kelayakan ............................................................... 37
3.6.2. Analisis Data Efektivitas ............................................................... 38
DAFTAR PUSTAKA ........................................................................................... 39
LAMPIRAN .......................................................................................................... 44
iii

BAB I
PENDAHULUAN
1.1. Latar Belakang
Informatika telah ditetapkan sebagai mata pelajaran wajib dalam Kurikulum
Merdeka mulai jenjang SD hingga SMA. Kebijakan ini menuntut perubahan
orientasi pembelajaran dari sekadar penguasaan aplikasi menuju penguatan logika
berpikir. Capaian Pembelajaran (CP) mata pelajaran Informatika elemen
Computational Thinking (CT) pada Fase E (Kelas X SMA) memiliki salah satu
tujuan yaitu "...memahami model dan menyimulasikan dinamika Input-Process-
Output dalam sebuah komputer Von Neumann...". Hal ini menegaskan bahwa
pembelajaran Arsitektur Komputer harus bergeser dari hafalan komponen menuju
pemahaman alur proses sistem (system flow) yang erat kaitannya dengan
kemampuan CT.
Secara konseptual, Arsitektur Von Neumann atau yang sering disebut
struktur Princeton merupakan fondasi utama komputer modern hingga saat ini.
Konsep intinya terletak pada prinsip stored-program, di mana instruksi program
dan data disimpan dalam memori yang sama serta diproses melalui jalur tunggal
(single bus) (Zhu Wei et al. dalam Xue, 2021). Arsitektur ini mensyaratkan lima
komponen utama yang saling terintegrasi, yaitu unit kontrol (controller), unit
aritmatika (arithmetic unit), memori, serta perangkat input dan output.
Kompleksitas arsitektur ini terletak pada mekanisme kerjanya yang menuntut
eksekusi sekuensial (sequential execution) berbasis sistem biner. Inilah yang
menjadikan Von Neumann sebagai "cetak biru" teknologi digital, namun sekaligus
menjadi materi yang menantang bagi siswa. Sesuai dengan referensi Chen Ruiwei
(dalam Xue, 2021), meskipun menjadi standar industri, keterbatasan alamiah
(nature limitations) dari struktur ini menuntut pemahaman logika alur data yang
kuat. Oleh karena itu, penguasaan terhadap dinamika kelima komponen tersebut
menjadi syarat mutlak bagi siswa informatika.
1

Urgensi pengembangan media berbasis teknologi muncul pada temuan
empiris terkait karakteristik dan preferensi belajar siswa. Studi yang dipublikasikan
dalam jurnal Putra et al. (2023) mengungkap fakta bahwa meskipun kepemilikan
smartphone di kalangan siswa mencapai 100%, penggunaannya didominasi untuk
media sosial, sementara pemanfaatan untuk pembelajaran sistem komputer masih
minim. Akibatnya, 75% siswa mengalami kesulitan memahami struktur dan fungsi
komputer karena keterbatasan sumber belajar visual dan metode penyampaian yang
monoton. Padahal, data yang sama menunjukkan adanya potensi besar di mana 90%
siswa memiliki motivasi tinggi untuk belajar menggunakan media, dan 100%
responden secara spesifik menginginkan penyajian materi sistem komputer dalam
bentuk aplikasi yang memuat teks, gambar, dan video. Selain itu, dari sisi
kurikulum, materi struktur Von Neumann memiliki alokasi waktu yang sangat
padat, yakni hanya sekitar 2 jam pelajaran untuk pembahasan struktur utama.
Waktu yang sangat tidak memadai untuk melakukan simulasi proses secara manual
di dalam kelas. Keterbatasan waktu tatap muka ini, dikombinasikan dengan
tingginya permintaan siswa terhadap media interaktif, menegaskan perlunya sebuah
gim edukatif yang dapat memvisualisasikan materi secara mandiri dan efisien.
Berbagai upaya pengembangan media pembelajaran sistem komputer telah
dilakukan, antara lain oleh Pryanka & Sukirman (2024) serta Hidayat dkk. (2024)
yang mengembangkan gim edukatif berbasis Android. Meskipun berhasil
memvisualisasikan materi, media-media tersebut cenderung berfokus pada
pengenalan komponen (drill-and-practice) dan masih dominan pada aspek kognitif
level rendah (C1-C2). Di sisi lain, implementasi gim dalam pembelajaran CT
memperlihatkan hasil empiris yang variatif. Peningkatan kemampuan CT melalui
media gim telah dilaporkan dalam beberapa studi (Ismail & Nurjanah, 2025).
Namun, terdapat temuan kontradiktif yang menunjukkan bahwa penggunaan gim
tanpa intervensi pedagogis spesifik hanya berdampak pada peningkatan rasa
percaya diri (self-efficacy), tanpa disertai peningkatan signifikan pada kompetensi
CT siswa (Pan et al., 2024). Fenomena ini mengindikasikan bahwa integrasi elemen
permainan semata tidaklah memadai, diperlukan kerangka pedagogis terstruktur
untuk mengarahkan proses kognitif siswa secara efektif.
2

Guna menjembatani kesenjangan tersebut, pendekatan Problem Based
Learning (PBL) diajukan sebagai kerangka pedagogis utama. Pemilihan integrasi
model PBL untuk penguatan CT didasarkan pada bukti empiris terkini yang
menunjukkan efektivitas model ini. Penelitian terbaru oleh Asrianti dan
Rakhmawati (2024) menegaskan bahwa terdapat pengaruh yang signifikan dari
penggunaan model PBL terhadap kemampuan berpikir komputasi siswa, khususnya
dalam konteks pemecahan masalah matematis yang terstruktur. Temuan ini
diperkuat oleh riset (Nurulaisyah et al., 2024) yang menyimpulkan bahwa model
PBL efektif dalam memberdayakan keterampilan berpikir komputasi siswa jenjang
sekolah menengah. Berdasarkan studi-studi mutakhir tersebut, pengembangan gim
edukatif dalam penelitian ini diposisikan sebagai media interaktif yang
memfasilitasi sintaks PBL, mengisi kebutuhan akan alat bantu ajar yang terbukti
valid secara ilmiah untuk meningkatkan CT.
Lebih lanjut, strategi implementasi gim ini dirancang secara kolaboratif
(collaborative play) guna memaksimalkan potensi PBL. Keputusan ini didasarkan
pada temuan Nurulaisyah et al. (2024) yang secara spesifik menemukan bahwa
selain meningkatkan CT, model PBL juga berpengaruh positif terhadap
keterampilan kolaborasi (collaboration skills). Hal ini sejalan dengan prinsip bahwa
kolaborasi adalah prasyarat pedagogis dalam memecahkan masalah yang
kompleks. Oleh karena itu, skenario permainan berkelompok (3 siswa 1 gim) dalam
penelitian ini bukan sekadar teknis pelaksanaan untuk mengatasi keterbatasan
perangkat, melainkan strategi yang sengaja dirancang agar proses scaffolding CT
dapat berjalan efektif melalui diskusi dan pertukaran gagasan antar siswa saat
menghadapi simulasi kerusakan komputer.
Merespons permasalahan dan peluang tersebut, penelitian ini mengusulkan
pengembangan media yang berbeda, yaitu gim simulasi dengan pendekatan
scaffolding sintaks PBL. Penelitian ini bertujuan menjembatani kesenjangan
tersebut melalui integrasi model PBL ke dalam media gim edukasi. Sinergi ini
diharapkan tidak hanya menstimulasi motivasi dan efikasi diri, tetapi juga secara
efektif meningkatkan kompetensi CT siswa pada materi Arsitektur Komputer,
menawarkan kebaruan solusi berupa simulasi debugging prosedural, aspek yang
belum dikaji secara komprehensif dalam penelitian-penelitian sebelumnya.
3

1.2. Rumusan Masalah
Berdasarkan batasan dan identifikasi masalah di atas, rumusan masalah
dalam penelitian ini adalah:
1. Bagaimana rancang bangun gim simulasi debugging dengan scaffolding
sintaks Problem Based Learning pada materi Arsitektur Komputer?
2. Bagaimana peningkatan kemampuan Computational Thinking siswa setelah
menggunakan gim simulasi, serta apakah terdapat perbedaan peningkatan
yang signifikan antar komponen CT (Dekomposisi, Pengenalan Pola,
Abstraksi, dan Berpikir Algoritma)?
3. Bagaimana respon siswa terhadap penggunaan gim simulasi dalam
pembelajaran Arsitektur Komputer?
1.3. Tujuan Penelitian
Berdasarkan rumusan masalah tersebut, tujuan penelitian ini adalah:
1. Menghasilkan produk gim simulasi debugging yang mengintegrasikan
sintaks Problem Based Learning untuk memvisualisasikan materi
Arsitektur Von Neumann yang teruji validitasnya.
2. Mengukur besaran peningkatan kemampuan Computational Thinking
siswa, sekaligus menganalisis profil peningkatan pada setiap komponen CT
untuk mengetahui aspek mana yang paling dominan berkembang.
3. Menganalisis respon siswa terhadap gim simulasi yang dikembangkan
ditinjau dari aspek kegunaan (usability) dan kepuasan pengguna.
1.4. Manfaat/Signifikansi Penelitian
Adapun manfaat dan kegunaan dari penelitian yang akan diharapkan adalah
sebagai berikut :
1. Bagi sekolah, agar hasil penelitian ini dapat memberikan alternatif
penggunaan media pembelajaran bagi guru/ pendidik terutama pada mata
pelajaran Informatika.
4

2. Bagi guru, agar hasil penelitian ini dapat menjadi bahan masukan untuk
memperkaya media pembelajaran menggunakan gim edukatif.
3. Bagi siswa, penggunaan media pembelajaran ini diharapkan dapat
meningkatkan kompetensi berpikir komputasi terutama pada mata pelajaran
Informatika.
4. Bagi pengelola lembaga pendidikan, agar hasil penelitian ini dapat dijadikan
inspirasi untuk mengambil kebijakan dalam memaksimalkan pengadaan
dan pemanfaatan fasilitas.
5. Bagi peneliti, agar hasil penelitian ini dapat menjadi sarana penerapan ilmu
kependidikan yang diperoleh selama perkuliahan di program studi
Pendidikan Ilmu Komputer fakultas pendidikan matematika dan ilmu
pengetahuan alam UPI dan menjadi masukan dalam pengembangan
penelitian selanjutnya.
1.5. Struktur Organisasi Skripsi
Sistematika penulisan skripsi ini disusun untuk memberikan gambaran
menyeluruh mengenai alur penelitian pengembangan yang dilakukan. Adapun
rincian muatan setiap bab adalah sebagai berikut:
BAB I Pendahuluan
Bab ini menguraikan latar belakang masalah mengenai urgensi media interaktif
pada materi Arsitektur Komputer, identifikasi masalah pembelajaran di kelas,
batasan masalah, serta rumusan masalah yang berfokus pada pengembangan gim
simulasi dan peningkatan Computational Thinking. Bab ini juga memuat tujuan
penelitian, manfaat penelitian bagi berbagai pihak, serta struktur organisasi skripsi.
BAB II Tinjauan Pustaka
Bab ini menyajikan landasan teori yang mendasari penelitian, meliputi: konsep
Serious Games dan simulasi dalam pendidikan, karakteristik materi Arsitektur Von
Neumann, sintaks model Problem Based Learning (PBL) sebagai strategi
scaffolding, serta kerangka kerja Computational Thinking (CT) menurut Csizmadia
et al. (2015). Selain itu, bab ini memaparkan kajian penelitian terdahulu yang
relevan dan kerangka berpikir pengembangan gim simulasi debugging.
5

BAB III Metodologi Penelitian
Bab ini menjelaskan desain penelitian Research and Development (R&D) yang
mengadopsi model pengembangan ADDIE (Analyze, Design, Develop, Implement,
Evaluate). Bagian ini merinci prosedur pengembangan produk, instrumen
pengumpulan data (validasi ahli, angket respon, dan tes CT), serta teknik analisis
data yang mencakup analisis kelayakan, analisis kepraktisan, dan uji statistik
ANOVA untuk mengukur perbedaan peningkatan antar komponen CT.
BAB IV Hasil Penelitian dan Pembahasan
Bab ini memaparkan hasil dari setiap tahapan pengembangan ADDIE, mulai dari
analisis kebutuhan hingga produk final. Data yang disajikan meliputi hasil validasi
ahli materi dan media, data respon siswa terhadap kegunaan gim, serta analisis data
pre-test dan post-test. Pembahasan berfokus pada interpretasi peningkatan skor N-
Gain pada setiap komponen CT (Dekomposisi, Pengenalan Pola, Abstraksi,
Algoritma) untuk membuktikan keseimbangan kualitas media dalam melatih logika
berpikir siswa.
BAB V Kesimpulan, Implikasi dan Rekomendasi
Bab ini memuat simpulan akhir mengenai keberhasilan rancang bangun gim
simulasi debugging, peta peningkatan kompetensi CT siswa, dan tingkat
penerimaan media. Bab ini diakhiri dengan implikasi pedagogis penggunaan gim
dalam pembelajaran Arsitektur Komputer serta rekomendasi untuk pengembangan
penelitian selanjutnya.
DAFTAR PUSTAKA
LAMPIRAN
6

BAB II
TINJAUAN PUSTAKA
2.1. Peta Literatur
Gambar 2.1.1 Peta Literatur
Peta literatur pada Gambar 2.1.1. memvisualisasikan integrasi lima pilar
teori utama dalam penelitian ini. Fokus utama terletak pada materi Arsitektur
Komputer (konsep Von Neumann) yang memiliki tingkat abstraksi tinggi. Materi
7

ini didekati menggunakan media gim Simulasi untuk memvisualisasikan proses
abstrak tersebut. Namun, agar tidak sekadar menjadi media hafalan, desain
permainan dikontrol oleh sintaks Problem Based Learning (PBL). Integrasi ketiga
elemen tersebut bermuara pada satu tujuan luaran, yaitu peningkatan kemampuan
Computational Thinking (CT) siswa, khususnya pada aspek dekomposisi dan
pengenalan pola kerusakan perangkat keras.
2.2. Kajian Teori
2.2.1. Gim Edukasi & Simulasi
Gim edukasi merupakan salah satu bentuk media pembelajaran yang
memanfaatkan elemen permainan untuk mencapai tujuan instruksional tertentu.
Gim edukasi dapat didefinisikan sebagai penggabungan antara konten pendidikan
yang serius dengan elemen permainan video yang menghibur, yang bertujuan untuk
memotivasi peserta didik agar belajar dengan cara yang menyenangkan (Mayer,
2019). Konsep ini sejalan dengan definisi Serious Games, yaitu permainan yang
mengintegrasikan prinsip-prinsip pedagogi ke dalam struktur permainan video, di
mana hiburan digunakan sebagai strategi untuk mencapai tujuan pendidikan yang
serius (Zhonggen, 2019).
Lebih lanjut dalam konteks pengembangan media, gim edukasi dipahami
sebagai salah satu bentuk multimedia interaktif yang mengemas materi pelajaran
dalam bentuk simulasi atau permainan, sehingga pengguna dapat berinteraksi
langsung dengan sistem untuk memecahkan masalah (Munir, 2012). Adanya
interaksi timbal balik ini memungkinkan siswa mendapatkan umpan balik
(feedback) secara instan atas tindakan yang dilakukan.
Salah satu genre yang dinilai efektif dalam pembelajaran berbasis komputer
adalah gim simulasi. Gim simulasi merupakan permainan yang mencoba
mereproduksi pengalaman dunia nyata secara akurat ke dalam sistem digital
(Schell, 2019). Dalam konteks pendidikan, simulasi sangat berguna untuk
mengajarkan prosedur atau fenomena yang berisiko tinggi, mahal, atau memakan
waktu lama jika dilakukan di dunia nyata (Chernikova et al., 2020). Melalui
simulasi, siswa dapat melakukan eksperimen dan melihat dampak dari keputusan
yang diambil dalam lingkungan yang aman (risk-free environment).
8

Selain simulasi, gim bergenre puzzle merupakan jenis permainan yang
menitikberatkan pada pemecahan teka-teki logis. Daya tarik utama gim puzzle
terletak pada tantangan intelektual, di mana logika dan penalaran harus digunakan
untuk menyelesaikan masalah yang diberikan. Hal ini menuntut kemampuan
analisis pemain dalam mengenali pola atau urutan tertentu untuk mencapai solusi
yang benar (Schell, 2019).
Berdasarkan paparan di atas, dapat disimpulkan bahwa gim edukasi adalah
aplikasi perangkat lunak multimedia yang menggabungkan materi pembelajaran
dengan mekanisme permainan interaktif untuk meningkatkan motivasi dan
pemahaman siswa. Gim simulasi diartikan sebagai tiruan aktivitas dunia nyata
dalam bentuk digital untuk melatih keterampilan prosedural tanpa risiko fisik,
sedangkan gim puzzle didefinisikan sebagai permainan yang menuntut logika,
ketelitian, dan strategi untuk memecahkan masalah guna mencapai tujuan
pembelajaran.
2.2.2. Kerangka Teoretis Pembelajaran Berbasis Gim
Efektivitas penggunaan gim dalam pendidikan tidak terlepas dari prinsip-
prinsip pemrosesan informasi dalam kognisi manusia. Pembelajaran melalui gim
komputer merupakan bentuk skenario pembelajaran multimedia, di mana materi
instruksional disajikan melalui kata-kata (teks atau narasi) dan gambar (grafis,
animasi, atau video) (Mayer, 2019). Oleh karena itu, kerangka kerja gim edukasi
dalam penelitian ini didasarkan pada Teori Kognitif Pembelajaran Multimedia
(Cognitive Theory of Multimedia Learning) yang dibangun di atas tiga prinsip
utama sains pembelajaran:
1. Prinsip Saluran Ganda (Dual Channels): Manusia memproses materi
visual/gambar dan materi verbal/kata-kata melalui saluran yang terpisah.
2. Prinsip Kapasitas Terbatas (Limited Capacity): Manusia hanya mampu
memproses sejumlah kecil informasi dalam setiap saluran pada satu waktu.
3. Prinsip Pemrosesan Aktif (Active Processing): Pembelajaran mendalam
(deep learning) terjadi ketika pembelajar terlibat dalam proses kognitif
aktif, meliputi: menyeleksi informasi yang relevan (selecting),
mengorganisasikannya menjadi model mental yang koheren (organizing),
dan mengintegrasikannya dengan pengetahuan awal (integrating).
9

Gambar 2.2.1 Model kognitif dari pembelajaran multimedia
Dalam konteks perancangan gim edukasi, Pemain mengalokasikan
kapasitas pemrosesan kognitif mereka yang terbatas ke dalam tiga jenis pemrosesan
(Mayer, 2019):
• Pemrosesan Ekstrane (Extraneous Processing): Proses kognitif yang
tidak mendukung tujuan pembelajaran, biasanya disebabkan oleh desain
instruksional yang buruk atau fitur gim yang mendistraksi.
• Pemrosesan Esensial (Essential Processing): Proses kognitif yang
diperlukan untuk merepresentasikan materi relevan secara mental. Hal ini
dipengaruhi oleh tingkat kompleksitas materi itu sendiri.
• Pemrosesan Generatif (Generative Processing): Proses kognitif yang
bertujuan untuk memahami materi secara mendalam, yang didorong oleh
motivasi pemain untuk mengerahkan usaha mental.
Berdasarkan kerangka tersebut, tujuan perancangan gim dalam penelitian
ini adalah untuk meminimalkan pemrosesan ekstrane (mengurangi distraksi
antarmuka), memandu pemrosesan esensial (membantu siswa memahami
kompleksitas arsitektur Von Neumann), dan mendorong pemrosesan generatif
(memotivasi siswa memecahkan masalah debugging).
Selain aspek kognitif, gim edukasi juga mengakomodasi aspek motivasi dan
metakognisi. Motivasi berfungsi sebagai inisiator yang mempertahankan perilaku
terarah pada tujuan. Gim memiliki kekuatan motivasional karena mampu membuat
siswa memilih untuk bermain, bertahan dalam permainan, dan mengerahkan usaha
untuk menguasainya (Mayer, 2019). Sementara itu, metakognisi dalam gim
mendorong siswa menjadi pembelajar mandiri yang bertanggung jawab memantau
dan mengontrol proses kognitif mereka sendiri selama permainan berlangsung.
10

2.2.3. Materi Arsitektur Komputer
a. Konsep Arsitektur Von Neumann
Dasar dari hampir semua komputer modern saat ini adalah arsitektur
yang dikenal sebagai mesin Von Neumann. Karakteristik paling
revolusioner dari arsitektur ini adalah konsep Stored Program (program
tersimpan). Berbeda dengan mesin komputasi terdahulu, konsep stored
program memungkinkan instruksi program dan data disimpan di dalam
memori utama yang sama secara elektronik. Konsep ini memungkinkan
komputer untuk bekerja secara fleksibel dan otomatis dengan mengambil
instruksi dari memori, menerjemahkannya, dan mengeksekusinya secara
berurutan atau sequential processing (Stallings, 2022). Secara struktural,
arsitektur Von Neumann terdiri dari subsistem utama yang saling terhubung
melalui jalur komunikasi (bus). Komponen-komponen tersebut dirincikan
sebagai berikut (Patterson & Hennessy, 2020):
• Central Processing Unit (CPU): Merupakan otak dari komputer yang
bertugas mengontrol operasi dan melakukan pemrosesan data. CPU
sendiri terdiri dari:
− Control Unit (CU): Mengatur aliran data dan interpretasi instruksi.
− Arithmetic Logic Unit (ALU): Melakukan operasi matematika
(tambah, kurang) dan logika (AND, OR).
• Memori Utama: Tempat penyimpanan sementara untuk instruksi
program dan data yang sedang diproses. Dalam arsitektur ini, tidak ada
pemisahan fisik antara memori data dan memori instruksi.
• Input/Output (I/O): Modul yang berfungsi sebagai jembatan
komunikasi antara komputer dengan lingkungan luar (pengguna atau
perangkat lain), seperti keyboard untuk input dan monitor untuk output.
Gambar 2.2.2 Arsitektur komputer Von Neumann
11

b. Mekanisme Kerja CPU: Siklus Instruksi dan Datapath
Gambar 2.2.3 Siklus Instruksi dan Datapath pada CPU
Agar sebuah komputer dapat menjalankan program, prosesor harus
melakukan serangkaian langkah sistematis yang berulang yang dikenal sebagai
Siklus Instruksi (Instruction Cycle). Fungsi dasar yang dilakukan oleh komputer
adalah eksekusi program, di mana CPU membaca instruksi dari memori satu
per satu dan mengeksekusinya (Stallings, 2022). Siklus dasar ini sering disebut
sebagai siklus Fetch-Decode-Execute, yang terdiri dari tahapan berikut:
1. Fetch (Pengambilan Instruksi): CPU membaca instruksi dari lokasi
memori yang ditunjuk oleh Program Counter (PC). Instruksi tersebut
kemudian dimuat ke dalam Instruction Register (IR).
2. Decode (Penerjemahan): Unit Kontrol (Control Unit) menerjemahkan
kode instruksi (opcode) yang ada di IR untuk menentukan jenis operasi
apa yang harus dilakukan dan operand mana yang diperlukan.
3. Execute (Eksekusi): CPU menjalankan operasi yang telah
diterjemahkan. Operasi ini bisa berupa pemindahan data antar memori,
operasi aritmatika oleh ALU, atau operasi I/O.
Setelah tahap eksekusi selesai, siklus akan berulang kembali ke
tahap Fetch untuk instruksi berikutnya, kecuali jika ada instruksi berhenti
(halt) atau interupsi.
12

c. Alur Data (Datapath)
Gambar 2.2.4 Ilustrasi alur data
Jika siklus instruksi menjelaskan "kapan" dan "apa" yang dilakukan,
maka Alur Data (Datapath) menjelaskan jalur fisik yang dilalui data di dalam
CPU selama proses tersebut. Datapath merupakan sekumpulan unit fungsional
seperti Arithmetic Logic Unit (ALU), register, dan jalur penghubung (bus) yang
saling terkoneksi untuk melakukan operasi pemrosesan data (Patterson &
Hennessy, 2020). Efisiensi sebuah prosesor sangat bergantung pada desain
datapath. Desain yang baik akan meminimalkan hambatan (bottleneck) aliran
data, sehingga setiap siklus instruksi dapat diselesaikan dalam waktu yang
sesingkat mungkin.
2.2.4. Model Pembelajaran Problem Based Learning (PBL)
a. Definisi Problem Based Learning
Model pembelajaran yang digunakan sebagai dasar perancangan
alur permainan dalam penelitian ini adalah Problem Based Learning (PBL).
PBL didefinisikan sebagai model pembelajaran yang menyuguhkan siswa
pada masalah otentik dan bermakna (authentic and meaningful problems)
yang berfungsi sebagai batu loncatan untuk investigasi dan penyelidikan
(Arends, 2015). Berbeda dengan pengajaran tradisional, dalam PBL guru
berperan sebagai fasilitator yang membimbing siswa untuk membangun
pengetahuan mereka sendiri melalui pemecahan masalah.
13

Tujuan utama dari model ini bukan hanya sekadar memahami materi
akademik, tetapi juga untuk membantu siswa mengembangkan
keterampilan berpikir kritis, kemampuan pemecahan masalah, dan
keterampilan sosial melalui kolaborasi. Pandangan ini menegaskan bahwa
PBL menantang siswa untuk membangun kebiasaan belajar mandiri, serta
bekerja sama dalam kelompok untuk mengonstruksi pengetahuan melalui
masalah dunia nyata yang relevan (Yew & Goh, 2016).
b. Sintaks Model Problem Based Learning
Pelaksanaan PBL terdiri dari lima fase utama yang dapat diadaptasi
ke dalam skenario gim edukasi (Arends, 2015):
1. Orientasi Siswa pada Masalah: Guru (atau sistem gim) menyajikan
masalah yang menarik dan memotivasi siswa untuk terlibat.
2. Mengorganisasi Siswa untuk Belajar: Membantu siswa
mendefinisikan dan mengorganisasikan tugas belajar yang berhubungan
dengan masalah tersebut.
3. Membimbing Penyelidikan Individu/Kelompok: Mendorong siswa
untuk mengumpulkan informasi yang sesuai dan melaksanakan
eksperimen untuk mendapatkan penjelasan dan pemecahan masalah.
4. Mengembangkan dan Menyajikan Hasil Karya: Membantu siswa
merencanakan dan menyiapkan karya yang sesuai.
5. Menganalisis dan Mengevaluasi Proses: Membantu siswa melakukan
refleksi atau evaluasi terhadap penyelidikan mereka dan proses-proses
yang mereka gunakan.
c. Integrasi PBL dalam Gim
Konsep penggabungan elemen permainan dengan pemecahan
masalah dikenal sebagai Problem-Based Serious Games. Penelitian terbaru
menunjukkan bahwa lingkungan permainan digital yang dirancang dengan
prinsip PBL mampu menempatkan pemain sebagai pemecah masalah aktif.
Integrasi ini tidak hanya meningkatkan pengalaman pengguna, tetapi juga
memberikan dampak signifikan terhadap peningkatan motivasi belajar
siswa melalui visualisasi masalah yang konkret (Moradi & Noor, 2022).
14

Tabel 1. Sintaks PBL sebagai scaffolding dalam gim edukasi
| Fase PBL  | Aktivitas  |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Implementasi dalam Fitur Gim
| (Arends, 2015)   | Kognitif Siswa  |      |                                          |            |     |       |      |            |
| ---------------- | --------------- | ---- | ---------------------------------------- | ---------- | --- | ----- | ---- | ---------- |
|                  | Memahami        |      | Briefing & Error Log: Pemain menerima    |            |     |       |      |            |
|                  | konteks         |      | laporan                                  | kerusakan  |     | dari  | NPC  | (Teknisi)  |
| Orientasi  pada  |                 |      |                                          |            |     |       |      |            |
|                  | kerusakan       | dan  | berupa keluhan pengguna atau kode error  |            |     |       |      |            |
Masalah
|     | tujuan      |     | (misal:                                 | "Hasil   | perhitungan  |              | ALU  | tidak   |
| --- | ----------- | --- | --------------------------------------- | -------- | ------------ | ------------ | ---- | ------- |
|     | perbaikan.  |     | sesuai")                                |          |              |              |      |         |
|     | Menentukan  |     | Diagnostic Menu & Specs: Tersedia menu  |          |              |              |      |         |
|     | strategi    |     | untuk                                   | melihat  |              | spesifikasi  |      | sistem  |
Mengorganisasi
|     | diagnostik  | dan  | (Arsitektur  | Von  | Neumann)  |     | dan  | memilih  |
| --- | ----------- | ---- | ------------ | ---- | --------- | --- | ---- | -------- |
Siswa
|     | alat bantu yang  |     | alat diagnosa untuk merencanakan strategi  |             |     |        |             |     |
| --- | ---------------- | --- | ------------------------------------------ | ----------- | --- | ------ | ----------- | --- |
|     | dibutuhkan.      |     | pelacakan bug.                             |             |     |        |             |     |
|     |                  |     | Cycle                                      | Simulation  |     | (Core  | Gameplay):  |     |
Melakukan
Pemain menjalankan simulasi siklus Fetch-
penelusuran
|               |                  |     | Decode-Execute  |            | langkah  |         | demi  | langkah.  |
| ------------- | ---------------- | --- | --------------- | ---------- | -------- | ------- | ----- | --------- |
| Membimbing    | masalah,         |     |                 |            |          |         |       |           |
|               |                  |     | Pemain          | mengamati  |          | aliran  | data  | di  Bus   |
| Penyelidikan  | eksperimen, dan  |     |                 |            |          |         |       |           |
Sistem untuk melokalisir di unit mana (CU,
mencari
|     |     |     | ALU,  | atau  | Memori)  | data  |     | mengalami  |
| --- | --- | --- | ----- | ----- | -------- | ----- | --- | ---------- |
penyebab error.
korupsi atau kemacetan.
|     |           |     | Debugging  | Console:    |     | Pemain   |     | melakukan  |
| --- | --------- | --- | ---------- | ----------- | --- | -------- | --- | ---------- |
|     | Menyusun  |     | tindakan   | perbaikan,  |     | seperti  |     | mengganti  |
Mengembangkan  solusi perbaikan  kode instruksi (Mnemonic), memperbaiki
Hasil Karya  dan  menguji  nilai pada Register, atau menyambungkan
|     | hipotesis.  |     | jalur  Bus  | yang  | terputus,  |     | lalu  | menekan  |
| --- | ----------- | --- | ----------- | ----- | ---------- | --- | ----- | -------- |
tombol "Run " untuk menguji solusi.
|     |     |     | System  | Feedback:  |     | Sistem  | menampilkan  |     |
| --- | --- | --- | ------- | ---------- | --- | ------- | ------------ | --- |
Merefleksikan
|     |     |     | animasi  | komputer  |     | bekerja  | normal  | (jika  |
| --- | --- | --- | -------- | --------- | --- | -------- | ------- | ------ |
proses
benar) atau meledak/hang (jika salah). Di
| Analisis  &  | penyelesaian  |      |        |         |         |             |     |       |
| ------------ | ------------- | ---- | ------ | ------- | ------- | ----------- | --- | ----- |
|              |               |      | akhir  | level,  | muncul  | Scoreboard  |     | yang  |
| Evaluasi     | masalah       | dan  |        |         |         |             |     |       |
memberikan umpan balik spesifik terkait
efektivitas
|     |     |     | efisiensi  | langkah  |     | debugging  |     | yang  |
| --- | --- | --- | ---------- | -------- | --- | ---------- | --- | ----- |
solusi.
dilakukan.
Dengan begitu, elemen interaktif dalam gim mampu memfasilitasi
fase penyelidikan PBL yang sulit dilakukan di kelas konvensional, yaitu
memberikan ruang bagi siswa untuk melakukan eksperimen berulang tanpa
risiko nyata. Keselarasan ini menciptakan siklus kognitif di mana pemain
15

menyelidiki lingkungan, membangun hipotesis strategi, dan mengevaluasi
hasil tindakan mereka secara mandiri.
Oleh karena itu, integrasi model PBL ke dalam media gim edukasi
dalam penelitian ini didasarkan pada validitas pedagogis tersebut. Penelitian
ini menerjemahkan sintaks PBL ke dalam mekanika permainan untuk
menciptakan lingkungan pemecahan masalah yang kompleks namun
menarik. Daftar konseptual untuk penerapannya dapat dilihat di tabel 1.
2.2.5. Computational Thinking (Berpikir Komputasional)
a. Definisi dan Konsep Dasar
Kemampuan pemecahan masalah dalam era digital saat ini sering
dirangkum dalam istilah Computational Thinking (CT). CT didefinisikan
sebagai kerangka kerja konseptual yang mencakup penyelesaian masalah,
perancangan sistem, dan pemahaman perilaku manusia dengan
menggambar pada konsep dasar ilmu komputer (Shute et al., 2017). CT
dipandang sebagai literasi abad ke-21 yang esensial bagi semua orang, tidak
terbatas pada ilmuwan komputer. Hal ini mencakup dekomposisi masalah,
abstraksi data, perancangan algoritma, serta debugging dan iterasi untuk
menghasilkan solusi yang efisien dan dapat dieksekusi (Shute et al., 2017).
b. Komponen Utama CT
Untuk mengukur kemampuan CT secara operasional, penelitian ini
mengadaptasi kerangka kerja pedagogis dari Computing at School
(Csizmadia et al., 2015). Secara teoretis, CT diuraikan ke dalam lima konsep
dasar: algorithmic thinking, decomposition, generalisation (patterns),
abstraction, dan evaluation. Namun, untuk kepentingan pengukuran proses
kognitif dalam gim simulasi debugging, penelitian ini memfokuskan pada
empat fondasi utama pemecahan masalah, yaitu:
• Dekomposisi (Decomposition): Merupakan proses memecah sistem
yang kompleks menjadi bagian-bagian komponen yang lebih kecil
(Csizmadia et al., 2015).
16

• Pengenalan Pola (Generalization): kemampuan mengidentifikasi
pola untuk memecahkan masalah baru berdasarkan pengalaman
sebelumnya (Csizmadia et al., 2015).
• Abstraksi (Abstraction): Proses membuat masalah atau sistem
lebih mudah dipikirkan dengan cara mengurangi detail yang tidak
perlu (Csizmadia et al., 2015).
• Berpikir Algoritma (Algorithmic Thinking): Kemampuan untuk
berpikir dalam urutan dan aturan yang jelas sebagai cara untuk
memecahkan masalah (Csizmadia et al., 2015).
c. Hubungan Arsitektur Komputer dan CT
Dalam Arsitektur Komputer, CT bermanifestasi dalam aktivitas
debugging. Aktivitas menemukan kesalahan (debugging) merupakan
penerapan praktis dari pemikiran logis dan algoritmik (Curzon & McOwan,
2017). Selain itu, CT juga bermanifestasi dalam perancangan sistem.
Melalui fitur gim yang memungkinkan siswa merancang 'node' pemrosesan
mereka sendiri, siswa diajak mensimulasikan model mental Arsitektur Von
Neumann. Aktivitas ini melatih siswa untuk memetakan bagaimana data
mentah (Input) diubah menjadi informasi (Output) melalui serangkaian
instruksi logis, dengan rincian sebagai berikut:
• Penerapan Dekomposisi: Siswa memecah sistem komputasi yang
kompleks menjadi modul-modul fungsional yang lebih kecil
berdasarkan prinsip Input-Proses-Output. Saat merancang 'node'
baru, siswa harus memisahkan mana bagian yang bertugas
menerima data (Input Unit), mana yang bertugas mengolah
logika/aritmatika (ALU/Process), dan mana yang bertugas
menampilkan hasil (Output Unit).
• Penerapan Abstraksi: Siswa belajar menyembunyikan kerumitan
detail sirkuit elektronik atau transistor menjadi sebuah model
representasi sederhana (Black Box). Saat siswa membuat sebuah
'node', mereka fokus pada fungsi logisnya tanpa perlu memikirkan
kompleksitas teknis di dalamnya. Mereka hanya fokus pada data apa
yang masuk dan apa yang harus keluar.
17

• Penerapan Pengenalan Pola: Dalam merancang sistem, siswa
mengidentifikasi pola aliran data (data flow) yang berulang.
Contohnya, siswa mengenali bahwa setiap operasi aritmatika selalu
memiliki pola arsitektur yang sama: mengambil data dari memori →
diproses di node prosesor → disimpan kembali ke memori/output.
Pola ini diadopsi siswa untuk merancang node-node fungsi lainnya.
• Penerapan Algoritma: Siswa menyusun urutan eksekusi logika di
dalam node rancangan mereka. Agar node berfungsi sesuai prinsip
Von Neumann, siswa harus menentukan langkah-langkah
pemrosesan data secara sekuensial (berurutan). Jika siswa salah
menyusun urutan, maka node tersebut akan gagal berfungsi. Ini
melatih logika prosedural yang presisi.
Dengan demikian, gim edukasi ini mentransformasi siswa dari
sekadar pengguna teknologi menjadi perancang sistem. Melalui simulasi
pembuatan node, siswa mempraktikkan inti dari Arsitektur Von Neumann
mulai dari integrasi unit-unit input, proses, hingga output secara konstruktif.
2.3. Kajian Metodologis
2.3.1. Model Pengembangan Sistem
Penelitian ini tergolong ke dalam jenis Penelitian dan Pengembangan atau
Research and Development (R&D). Penelitian pengembangan dalam bidang
pendidikan memerlukan tahapan-tahapan yang terorganisir dengan baik untuk
memastikan keberhasilannya, mulai dari identifikasi masalah hingga evaluasi
produk (Borg dan Gall, 1983). Secara metodologis, prosedur penelitian
pengembangan dikelompokkan ke dalam dua bagian, yaitu Tahapan Umum dan
Tahapan Khusus sesuai model yang dipilih (Judijanto et al., 2024). Penelitian ini
mengadopsi prosedur Tahapan Umum R&D yang terdiri dari enam langkah
sistematis sebagai kerangka besar penelitian, yaitu:
1. Identifikasi Masalah: Melakukan penelitian awal dan analisis mendalam
terkait isu pendidikan yang relevan.
2. Perancangan Rencana: Merumuskan tujuan, metodologi, dan sumber daya
penelitian.
18

3. Pengumpulan Data: Implementasi rencana termasuk observasi dan
pengumpulan informasi.
4. Analisis Data: Menganalisis pola atau tren relevan dari data yang terkumpul.
5. Interpretasi Hasil: Mengevaluasi temuan untuk menarik kesimpulan solusi.
6. Penulisan Laporan: Menyusun temuan dan rekomendasi secara sistematis.
Untuk mengoperasionalkan tahapan umum tersebut dalam pembuatan
produk media gim edukasi, penelitian ini menggunakan Tahapan Khusus dengan
model ADDIE. Model ini dipilih karena strukturnya yang sistematis dalam
merancang konsep dan konten produk (Branch, 2009). Model ADDIE terdiri dari
lima fase pengembangan yang selaras dengan prosedur umum R&D (Judijanto et
al., 2024), yaitu:
Gambar 2.3.1 Model pengembangan ADDIE
a. Analysis (Analisis)
Tahap ini selaras dengan langkah identifikasi masalah pada prosedur
umum. Kegiatan utamanya adalah menganalisis perlunya pengembangan
produk baru serta menganalisis kelayakan dan syarat-syarat pengembangannya.
Masalah dapat muncul karena produk pembelajaran yang ada saat ini sudah
tidak relevan dengan kebutuhan sasaran, karakteristik peserta didik, atau
teknologi .
b. Design (Desain)
Tahap desain merupakan proses sistematik yang dimulai dari merancang
konsep dan konten di dalam produk tersebut. Pada tahap ini, rancangan produk
masih bersifat konseptual (seperti peta materi, skenario gim, dan storyboard)
yang akan mendasari proses pengembangan di tahap berikutnya.
19

c. Development (Pengembangan)
Tahap ini berisi kegiatan realisasi rancangan produk yang sebelumnya
telah dibuat. Kerangka konseptual direalisasikan menjadi produk gim yang siap
diterapkan. Pada tahap ini juga dilakukan pembuatan instrumen untuk
mengukur kinerja produk, yang mencakup validasi oleh para ahli untuk
memastikan kelayakan media sebelum diuji coba.
d. Implementation (Implementasi)
Penerapan produk dimaksudkan untuk memperoleh umpan balik
terhadap produk yang dikembangkan. Umpan balik awal (early evaluation)
diperoleh dengan menerapkan gim sesuai rancangan yang telah dibuat dalam
situasi pembelajaran nyata untuk melihat respon pengguna.
e. Evaluation (Evaluasi)
Tahap evaluasi dilakukan untuk memberi umpan balik kepada pengguna
produk dan pengembang, sehingga revisi dapat dibuat sesuai kebutuhan yang
belum terpenuhi. Tujuan akhir dari tahap ini adalah mengukur ketercapaian
tujuan pengembangan, yaitu peningkatan kemampuan CT siswa.
2.3.2. Perangkat Pengembangan Sistem
Untuk mengimplementasikan rancangan gim edukasi menjadi produk
perangkat lunak yang fungsional, penelitian ini memanfaatkan serangkaian
perangkat pengembangan yang terintegrasi.
a. Godot sebagai Game Engine
Perangkat utama yang digunakan dalam penelitian ini adalah Godot
Engine. Godot didefinisikan sebagai mesin permainan lintas platform
(cross-platform) yang bersifat sumber terbuka (open source) di bawah
lisensi MIT (Godot Community, 2023). Arsitektur Godot tidak
menggunakan pola komponen tradisional, melainkan menggunakan sistem
Scene dan Node yang memungkinkan pengembang untuk mengorganisir
elemen gim secara modular (Wang, 2019). Pemilihan Godot didasarkan
pada overhead performa yang sangat rendah (lightweight) namun tetap
mampu melakukan rendering 3D dan 2D yang kompleks (Bradfield, 2018).
20

b. Bahasa Pemrograman: GDScript
Logika permainan diprogram menggunakan GDScript, yaitu bahasa
pemrograman tingkat tinggi yang didesain secara spesifik untuk Godot
(Manzur & Linietsky, 2014). Bahasa ini memiliki kemiripan struktur
dengan Python, dengan keunggulan utama pada integrasi ketat dengan
editor yang memungkinkan fitur hot-reloading dan debugging yang lebih
efisien (Hill, 2020).
c. Perangkat Lunak Pendukung
Pengembangan aset didukung oleh Blender untuk pemodelan 3D
dan Figma untuk desain antarmuka. Blender merupakan perangkat lunak
yang mendukung keseluruhan pipeline 3D mulai dari pemodelan hingga
rendering (Blender Foundation, 2023), sedangkan Figma adalah alat desain
berbasis vektor dan kolaborasi awan yang memungkinkan perancangan
antarmuka yang presisi (Putra, 2021).
2.3.3. Instrumen Evaluasi Kualitas Media (Validitas & Usabilitas)
Untuk memastikan kelayakan media gim edukasi sebelum diujicobakan,
diperlukan instrumen standar yang diakui secara akademis.
a. Learning Object Review Instrument (LORI)
Learning Object Review Instrument (LORI) adalah kerangka kerja
evaluasi yang dikembangkan untuk menilai kualitas objek pembelajaran
multimedia. LORI dirancang untuk menyeimbangkan penilaian antara
kualitas konten pedagogis dan kualitas desain antarmuka (Leacock dan
Nesbit, 2007). Instrumen ini mengukur sembilan dimensi, antara lain:
kualitas konten, keselarasan tujuan pembelajaran, umpan balik (feedback)
dan adaptasi, motivasi, presentasi desain, kemudahan penggunaan interaksi,
aksesibilitas, penggunaan kembali (reusability), dan kepatuhan standar.
Penggunaan LORI dalam penelitian ini bertujuan untuk mendapatkan data
validitas media yang komprehensif dari para ahli materi dan ahli media.
Rubrik penilaian yang digunakan adalah LORI 2.0 yang dimodifikasi agar
turut serta mengukur kesesuaian dengan komponen CT.
21

b. System Usability Scale (SUS)
Persepsi pengguna akhir (siswa) diukur menggunakan System
Usability Scale (SUS). Brooke (1996) mendefinisikan SUS sebagai "skala
cepat dan kotor" (quick and dirty) yang namun sangat tangguh (robust)
untuk mengukur kegunaan sistem. Keunggulan SUS adalah sifatnya yang
technology-agnostic (dapat digunakan untuk berbagai jenis perangkat
lunak) dan kemampuannya memberikan skor tunggal yang mudah
diinterpretasikan untuk menentukan tingkat penerimaan pengguna
(usability) dan kepuasan subjektif secara efisien (Bangor et al., 2008).
2.3.4. Desain Penelitian Eksperimen
a. Pre-Experimental: One-Group Pretest-Posttest Design
Desain ini dipilih ketika peneliti bertujuan untuk membandingkan
kondisi sebelum dan sesudah perlakuan pada satu kelompok subjek yang
sama tanpa adanya kelompok kontrol pembanding. Pola desain ini
digambarkan sebagai (𝑂 ×𝑂 ), di mana 𝑂 adalah nilai tes awal (pretest)
1 2 1
sebelum diberi perlakuan, 𝑋 adalah perlakuan (pembelajaran menggunakan
gim), dan 𝑂 adalah nilai tes akhir (posttest) (Sugiyono, 2019). Desain ini
2
relevan digunakan dalam penelitian pengembangan untuk mengetahui
besaran dampak intervensi produk terhadap kompetensi siswa secara
spesifik pada kelompok uji terbatas.
b. Teknik Sampling
Teknik pengambilan sampel merupakan strategi untuk menentukan
subjek penelitian yang representatif. Penelitian ini menggunakan teknik
Purposive Sampling, yaitu teknik penentuan sampel dengan pertimbangan
tertentu (Creswell, 2014). Pertimbangan ini didasarkan pada karakteristik
siswa yang belum pernah mendapatkan materi Arsitektur Komputer
sebelumnya dan memiliki akses ke perangkat laboratorium yang memadai,
sehingga data yang dihasilkan relevan dengan tujuan penelitian.
22

2.3.5. Asesmen Computational Thinking (CT)
Pengukuran konstruk kognitif yang abstrak seperti CT memerlukan
instrumen yang terstruktur.
a. Computational Thinking Test
Untuk mengukur peningkatan kompetensi CT siswa pada materi
Arsitektur Komputer, penelitian ini menggunakan instrumen tes diagnostik
kognitif. Butir soal dalam instrumen ini dirancang khusus berdasarkan
empat indikator utama CT yaitu: dekomposisi, pengenalan pola, abstraksi,
dan berpikir algoritma (Shute et al., 2017).
Setiap butir soal memiliki bobot yang memetakan kemampuan siswa
dalam menyelesaikan masalah dalam arsitektur komputer Von Neumann.
Untuk menjamin bahwa butir soal tersebut benar-benar mengukur aspek CT
dan bukan sekadar pengetahuan umum, instrumen ini wajib melalui proses
Validasi Isi (Content Validity). Validitas isi dilakukan oleh panel ahli
(expert judgment) untuk memastikan kesesuaian antara butir soal dengan
indikator materi dan indikator kognitif yang dituju (Sari et al., 2021).
b. Analisis Kualitas Instrumen (Teori Tes Klasik)
Analisis butir soal adalah proses sistematis yang bertujuan untuk
mengevaluasi kualitas tes berdasarkan kualitas setiap butir soal, kumpulan
soal, dan hubungan antar butir soal1. Mengacu pada Shofiah et al. (2023),
analisis kualitas instrumen dalam penelitian ini mencakup lima komponen
utama:
1. Validitas Empiris (Validity)
Validitas adalah tingkat ketepatan atau keabsahan suatu tes
dalam mengukur tujuan tertentu, baik terkait materi maupun
kemampuan siswa yang sesungguhnya. Validitas butir soal dihitung
menggunakan rumus korelasi Pearson Product Moment. Sebuah
soal dikatakan valid dan layak dipakai jika nilai koefisien korelasi
(𝑟 ) berada pada kategori sedang hingga sangat tinggi (0,40 <
𝑥𝑦
(𝑟 ) ≤ 1,00) dan nilai (𝑟 > 𝑟 ).
𝑥𝑦 𝑥𝑦 𝑡𝑎𝑏𝑒𝑙
23

2. Reliabilitas Tes (Reliability)
Reliabilitas menentukan keandalan instrumen, di mana
instrumen yang reliabel akan memberikan hasil yang hampir sama
setiap kali digunakan. Untuk tes objektif, reliabilitas dihitung
menggunakan rumus KR-21 sebagaimana diusulkan Slameto dalam
Shofiah et al. (2023). Kualitas instrumen ditentukan berdasarkan
indeks reliabilitas, di mana tes dengan koefisien 0,61 −
0,80 dikategorikan tinggi dan 0,81 − 1,00 sangat tinggi.
3. Tingkat Kesukaran (Difficulty Level)
Analisis ini bertujuan mengetahui persentase siswa yang
menjawab benar untuk melihat karakteristik soal. Tingkat kesukaran
(𝑇𝐾) dihitung dengan membagi jumlah siswa yang menjawab benar
dari kelompok atas dan bawah dengan jumlah seluruh peserta tes.
Berdasarkan klasifikasi Shofiah et al. (2023), proporsi tingkat
kesukaran dibagi menjadi:
− Sukar: 0,00 − 0,30
− Sedang: 0,31 − 0,70 (Soal yang dianggap baik)
− Mudah: 0,71 − 1,00.
4. Daya Pembeda (Discriminating Power)
Daya pembeda adalah kemampuan soal dalam
menggambarkan perbedaan antara siswa berkemampuan tinggi dan
rendah. Indeks Diskriminasi (𝐷𝑃) dihitung dari selisih siswa yang
menjawab benar di kelompok atas (𝑈) dan kelompok bawah (𝐿).
Kriteria soal yang baik menurut Shofiah et al. (2023) adalah:
− 0,41 – 0,70 (Baik): Soal dipakai.
− 0,71 – 1,00 (Sangat Baik): Soal dipakai.
− < 0,20 (Buruk): Soal dibuang.
5. Analisis Pengecoh (Distractor)
Pada tes pilihan ganda, analisis ini bertujuan mendeteksi opsi
jawaban salah yang tidak berfungsi. Pengecoh dikatakan berfungsi
baik apabila dipilih oleh setidaknya 5% dari peserta tes, serta lebih
banyak dipilih oleh kelompok siswa berkemampuan rendah.
24

2.3.6. Teknik Pengumpulan Data
Validitas data penelitian sangat bergantung pada kualitas instrumen dan
ketepatan teknik pengumpulan data yang digunakan. Dalam penelitian ini, teknik
yang digunakan merujuk pada pedoman penelitian R&D menurut Sugiyono (2019),
meliputi:
a. Observasi
Metode pengumpulan data ini dilakukan melalui pengamatan
langsung terhadap perilaku siswa dan interaksi mereka dengan media gim
selama proses pembelajaran berlangsung. Tujuannya adalah untuk mencatat
fenomena perilaku yang tidak terungkap melalui tes tertulis, seperti
antusiasme dan kesulitan teknis saat mengoperasikan gim.
b. Wawancara
Wawancara tidak terstruktur dilakukan kepada perwakilan siswa
dan guru untuk menggali informasi mendalam yang bersifat kualitatif.
Teknik ini digunakan untuk memvalidasi data angket dan mendapatkan
wawasan mengenai pengalaman pengguna serta kendala teknis yang
dialami selama penggunaan media.
c. Angket (Kuesioner)
Angket digunakan untuk memperoleh data kuantitatif mengenai
kelayakan media dari para ahli dan respon kepraktisan dari siswa.
Responden diberikan seperangkat pernyataan tertulis untuk dijawab
berdasarkan skala penilaian yang telah ditentukan.
d. Skala Pengukuran (Skala Likert)
Untuk mengukur variabel non-kognitif seperti validitas media dan
respon siswa, digunakan Skala Likert. Menurut Likert (1932), skala ini
adalah instrumen psikometrik yang digunakan untuk mengukur sikap,
pendapat, dan persepsi seseorang tentang fenomena sosial. Dalam penelitian
ini, skala Likert 4 poin (Sangat Setuju, Setuju, Tidak Setuju, Sangat Tidak
Setuju) digunakan untuk menghindari bias central tendency (jawaban
netral/ragu-ragu).
25

2.3.7. Teknik Analisis Data Statistik
Data kuantitatif yang diperoleh dianalisis menggunakan uji statistik yang
ketat untuk menarik kesimpulan yang valid.
a. Analisis Peningkatan Kemampuan (Normalized Gain)
Untuk mengukur besaran peningkatan kemampuan Computational
Thinking (CT) siswa sebelum dan sesudah penggunaan media, digunakan rumus
Normalized Gain (N-Gain) yang dikembangkan oleh Hake (1999):
𝑆 −𝑆
𝑝𝑜𝑠𝑡 𝑝𝑟𝑒
𝑔 =
𝑆 −𝑆
𝑚𝑎𝑘𝑠 𝑝𝑟𝑒
Keterangan:
• 𝑔 : Skor N-Gain
• 𝑆 : Skor Post-test
𝑝𝑜𝑠𝑡
• 𝑆 : Skor Pre-test
𝑝𝑟𝑒
• 𝑆 : Skor Maksimal Ideal
𝑚𝑎𝑘𝑠
Pengkategorian kelompok data dilakukan menggunakan teknik statistik
hipotetik (Mean Standar Deviasi) merujuk pada Azwar (2012).
b. Uji Prasyarat (Normalitas & Homogenitas)
Sebelum melakukan uji hipotesis, data N-Gain harus memenuhi asumsi
dasar statistik parametrik:
• Uji Normalitas: Menggunakan uji Shapiro-Wilk untuk mengetahui
apakah data N-Gain berdistribusi normal, mengingat sampel penelitian
berjumlah kecil (𝑁 < 50). Menurut Field (2018) dan Shapiro & Wilk
(1965), uji ini memiliki kekuatan (power) yang lebih baik untuk
mendeteksi deviasi normalitas pada sampel kecil dibandingkan uji
Kolmogorov-Smirnov.
• Uji Homogenitas: Menggunakan Levene’s Test untuk memastikan
bahwa varians data antar kelompok komponen adalah seragam.
Sebagaimana dijelaskan oleh Field (2018), uji ini tidak mensyaratkan
data harus terdistribusi normal secara sempurna agar tetap valid,
sehingga lebih tangguh (robust) dibandingkan uji Bartlett.
26

c. Pengelompokan Data Statistik (Grouping by Component)
Penelitian ini mengelompokkan data berdasarkan Komponen CT. Hal
ini dilakukan untuk menghindari bias diskriminatif terhadap subjek penelitian
dan memfokuskan evaluasi pada performa media dalam mengajarkan setiap
aspek materi. Data N-Gain dipetakan menjadi empat kelompok distribusi:
1. Kelompok data N-Gain aspek Dekomposisi.
2. Kelompok data N-Gain aspek Pengenalan Pola.
3. Kelompok data N-Gain aspek Abstraksi.
4. Kelompok data N-Gain aspek Berpikir Algoritma.
Pengelompokan ini bertujuan untuk memetakan profil efektivitas
media, apakah gim simulasi mampu meningkatkan keempat aspek tersebut
secara seimbang atau hanya dominan pada aspek tertentu.
d. Uji One-Way ANOVA (Analysis of Variance)
Penelitian ini menggunakan uji One-Way ANOVA untuk menguji
signifikansi perbedaan rata-rata peningkatan (mean N-Gain) antar keempat
komponen CT tersebut. Menurut Field (2018), ANOVA memungkinkan
peneliti untuk membandingkan varians rata-rata lebih dari dua kelompok data
secara simultan dengan meminimalkan kesalahan Tipe I. Dalam konteks
penelitian ini, uji ANOVA digunakan untuk menjawab hipotesis keseimbangan
kualitas produk:
• Jika nilai signifikansi (Sig.) > 0.05 (H 0 Diterima): Tidak terdapat
perbedaan peningkatan yang signifikan antar komponen. Hal ini
merupakan indikator positif yang menunjukkan bahwa gim simulasi
efektif secara holistik/seimbang dalam melatih seluruh aspek CT siswa.
• Jika nilai signifikansi (Sig.) < 0.05 (H 0 Ditolak): Terdapat perbedaan
signifikan, yang mengindikasikan bahwa gim simulasi memiliki kekuatan
yang menonjol pada aspek tertentu namun perlu perbaikan pada aspek
lainnya.
27

2.4. Penelitian yang Relevan (State of the Art)
3.  Tabel 2. Daftar penelitian yang relevan
| Peneliti & Judul      |     |                           | Metode & Hasil Utama  |     |     |
| --------------------- | --- | ------------------------- | --------------------- | --- | --- |
| Putra et al., (2023)  |     | Metode: R&D model ADDIE.  |                       |     |     |
| Pengembangan          |     | media                     |                       |     |     |
pembelajaran berbasis Android  Hasil: Media berbasis Android dinilai "Baik" pada uji
pada  mata  pelajaran  sistem  usability dan mendapatkan respon positif serta
| komputer di kelas X SMKN 1  |     | antusiasme tinggi dari siswa.  |     |     |     |
| --------------------------- | --- | ------------------------------ | --- | --- | --- |
Manggis.
Metode: Pengembangan sistem GDLC (Game
Hidayat et al. (2024)
Development Life Cycle).
Perancangan  Aplikasi  Game  Hasil: Terciptanya gim edukasi tebak gambar dan
| Edukasi Pengenalan Komputer  |     | kuis komponen komputer yang mampu  |     |     |     |
| ---------------------------- | --- | ---------------------------------- | --- | --- | --- |
Dasar Berbasis Android  menyederhanakan materi agar mudah dipahami.
Metode: Kualitatif, R&D model Waterfall (Android
Hidayad & Prasetya (2022)
Studio).
Perancangan  Aplikasi  Game  Hasil: Aplikasi gim edukasi yang menyediakan
Edukasi Pengenalan Komputer  informasi detail perangkat komputer dan fitur kuis
| Dasar Berbasis Android  |     | untuk melatih pengetahuan pengguna.  |     |     |     |
| ----------------------- | --- | ------------------------------------ | --- | --- | --- |
Metode: True Experimental (Post-test Only Control
Asrianti & Rakhmawati (2024)
Design).
The Effect of Problem Based
Hasil: Terdapat pengaruh signifikan penggunaan
Learning Model on Students’
model PBL terhadap kemampuan CT matematis
| Mathematical  | Computational  |     |     |     |     |
| ------------- | -------------- | --- | --- | --- | --- |
siswa (Sig. < 0,001).
Thinking Skills
| Nurulaisyah,  | Probosari,  | &   |     |     |     |
| ------------- | ----------- | --- | --- | --- | --- |
Metode: Kuasi Eksperimen (Quasi-Experimental).
Antrakusuma (2024)
Problem-based learning model
Hasil: Model PBL terbukti efektif memberdayakan
| on  the  collaboration  |     | and  |     |     |     |
| ----------------------- | --- | ---- | --- | --- | --- |
keterampilan kolaborasi dan CT siswa.
computational thinking skills
Wahyuni et al. (2025)  Metode: R&D (ADDIE) One Group Pretest-Posttest.
| Interactive  | Multimedia  |     |     |     |     |
| ------------ | ----------- | --- | --- | --- | --- |
Educational Games Based on
Hasil: Multimedia gim berbasis PBL valid, praktis,
| Problem-Based  | Learning  |               |               |                    |        |
| -------------- | --------- | ------------- | ------------- | ------------------ | ------ |
|                |           | dan  efektif  | meningkatkan  | motivasi  belajar  | siswa  |
(PBL) for Ecosystem Material
secara signifikan.
to Enhance Student Learning
Motivation.
|     |     | Metode:  | Eksperimen  | (Pre-test  | Post-test)  |
| --- | --- | -------- | ----------- | ---------- | ----------- |
Ismail & Nurjanah (2025)
menggunakan LightBot.
Educational  Game  for  Hasil:  Peningkatan  signifikan  pada  skor  CT  pada
| Computational Thinking  |     | kelompok yang menggunakan gim.  |                           |     |     |
| ----------------------- | --- | ------------------------------- | ------------------------- | --- | --- |
|                         |     | Metode: Implementasi            | Game-Based Learning pada  |     |     |
Pan et al. (2024)  siswa  sekolah  menengah  dengan  analisis  faktor
moderasi (gender, usia, pengalaman).
Hasil: Penggunaan gim terbukti meningkatkan efikasi
Enhancing  middle  school  diri  (self-efficacy)  siswa  terhadap  CT.  Namun,
students’  computational  penelitian ini mencatat bahwa intervensi gim tersebut
thinking  competency  through  tidak meningkatkan kompetensi CT secara signifikan.
game-based learning  Faktor  gender  ditemukan  berpengaruh  lebih  besar
dibandingkan usia.
28

Berdasarkan pemetaan matriks pada tabel 2, teridentifikasi adanya
kesenjangan yang nyata dalam pengembangan media pembelajaran Arsitektur
Komputer. Mayoritas penelitian terdahulu masih berfokus pada media berbasis
presentasi atau aplikasi evaluasi kognitif tingkat rendah (hafalan), serta belum
mengakomodasi pengembangan kognitif tingkat tinggi (Putra et al., 2023).
Di sisi lain, implementasi gim dalam pembelajaran CT memperlihatkan
hasil empiris yang variatif. Peningkatan kemampuan CT melalui media gim telah
dilaporkan dalam beberapa studi (Ismail & Nurjanah, 2025). Namun, terdapat
temuan kontradiktif yang menunjukkan bahwa penggunaan gim tanpa intervensi
pedagogis spesifik hanya berdampak pada peningkatan rasa percaya diri (self-
efficacy), tanpa disertai peningkatan signifikan pada kompetensi CT siswa (Pan et
al., 2024). Fenomena ini mengindikasikan bahwa integrasi elemen permainan
semata tidaklah memadai, diperlukan kerangka pedagogis terstruktur untuk
mengarahkan proses kognitif siswa secara efektif.
Oleh karena itu, penelitian ini bertujuan menjembatani kesenjangan tersebut
melalui integrasi model PBL ke dalam media gim edukasi. Sinergi ini diharapkan
tidak hanya menstimulasi motivasi dan efikasi diri, tetapi juga secara efektif
meningkatkan kompetensi CT siswa pada materi Arsitektur Komputer,
menawarkan kebaruan solusi berupa simulasi debugging prosedural, aspek yang
belum dikaji secara komprehensif dalam penelitian-penelitian sebelumnya.
2.5. Kerangka Berpikir
2.5.1. Kondisi Awal (Masalah)
Pembelajaran materi Arsitektur Komputer di tingkat pendidikan
menengah sering kali dinilai abstrak dan sulit dipahami oleh siswa. Berdasarkan
kajian literatur, media pembelajaran yang tersedia saat ini teridentifikasi masih
didominasi oleh salindia statis atau aplikasi permainan yang terbatas pada aspek
kognitif tingkat rendah seperti hafalan komponen (Hidayat et al., 2024).
Konsekuensinya, kemampuan pemecahan masalah dan CT siswa yang
mencakup elemen dekomposisi, pengenalan pola, abstraksi, dan algoritma
belum berkembang secara optimal.
29

2.5.2. Analisis Kesenjangan (Gap Analysis)
Model pembelajaran PBL telah terbukti efektif dalam meningkatkan
kemampuan berpikir komputasional, namun implementasinya yang terintegrasi
dengan media interaktif digital masih terbatas (Asrianti & Rakhmawati, 2024).
Di sisi lain, pendekatan Game-Based Learning terbukti mampu meningkatkan
motivasi dan efikasi diri siswa (Pan et al., 2024). Akan tetapi, temuan terbaru
mengindikasikan bahwa penggunaan gim tanpa didukung strategi pedagogis
yang terstruktur seringkali tidak memberikan dampak signifikan terhadap
peningkatan kompetensi teknis CT siswa.
2.5.3. Solusi (Intervensi)
Guna mengatasi permasalahan tersebut, diusulkan pengembangan
media gim edukasi yang mengintegrasikan sintaks PBL. Dalam pengembangan
ini, fungsi gim tidak sekadar sebagai sarana hiburan, melainkan dirancang
secara sistematis agar setiap level permainan merepresentasikan tahapan PBL,
mulai dari orientasi masalah, pengorganisasian belajar, penyelidikan, penyajian
hasil, hingga evaluasi. Sinergi ini ditujukan untuk menstimulasi siswa secara
aktif dalam mendayagunakan kemampuan berpikir komputasional guna
menyelesaikan tantangan dalam permainan.
Melalui intervensi ini, diharapkan dapat dihasilkan media pembelajaran
yang teruji validitas dan kepraktisannya. Lebih jauh, media ini diharapkan
mampu meningkatkan kompetensi CT siswa secara efektif pada materi
Arsitektur Komputer.
30

BAB III
METODOLOGI PENELITIAN
Metodologi penelitian
3.1. Jenis Penelitian
Penelitian ini menggunakan pendekatan Research and Development (R&D)
dengan mengadopsi model pengembangan ADDIE. Model ini dipilih karena
tahapan kerjanya yang sistematis dan relevan untuk menghasilkan produk gim
edukasi yang teruji validitas dan efektivitasnya. Penelitian ini bertujuan untuk
mengembangkan produk berupa gim edukatif berbasis PBL pada mata pelajaran
Arsitektur Komputer, serta menguji efektivitasnya dalam meningkatkan
kemampuan CT siswa.
3.2. Prosedur Penelitian
Gambar 3.2.1 Diagram prosedur penelitian
31

Penelitian pengembangan terdiri dari Tahapan Umum (langkah sistematis
penelitian ilmiah) dan Tahapan Khusus (model pengembangan produk). Untuk
menyelaraskan kedua aspek tersebut, prosedur penelitian ini disusun ke dalam tiga
alur utama:
1. Tahap Studi Pendahuluan (General Research Phase)
Tahap ini mengadopsi langkah "Identifikasi Masalah" dan
"Perancangan Rencana" dari tahapan umum R&D. Kegiatan ini meliputi studi
literatur terkait gap penelitian, observasi kondisi lapangan, dan merumuskan
rancangan penelitian. Luaran tahap ini adalah rumusan masalah yang melandasi
perlunya pengembangan media.
2. Tahap Pengembangan Sistem (Model ADDIE)
Tahap ini merupakan inti dari pengembangan produk yang mengadopsi
model ADDIE dimulai dari analysis, design, development, implementation,
hingga evaluation.
3. Tahap Akhir dan Pelaporan (Reporting Phase)
Tahap ini mengadopsi langkah "Analisis Data", "Interpretasi Hasil", dan
"Penulisan Laporan" dari tahapan umum R&D. Di sini peneliti mengolah data
statistik (Pretest-Posttest) menggunakan uji ANOVA, mengukur kualitas
instrumen menggunakan classical test theory, membahas temuan penelitian,
dan menyusun laporan skripsi sebagai bentuk diseminasi hasil penelitian dalam
lingkup akademik.
3.3. Desain pengembangan media
Seperti yang telah dijelaskan sebelumnya, pengembangan media pembelajaran
untuk penelitian ini mengadopsi model ADDIE. Model ini dipilih karena
strukturnya yang sistematis dalam merancang konsep dan konten produk serta
proses evaluasi yang iteratif di setiap tahapan memberikan kesempatan kepada
peneliti untuk mengembangkan produk secara berkala sambil menerima masukan
dari evaluasi formatif. Berikut ini rinciannya:
32

Gambar 3.3.1 Diagram pengembangan media dengan model ADDIE
33

3.3.1. Tahap Analisis (Analyze)
Tahap ini bertujuan untuk mengidentifikasi kemungkinan penyebab
kesenjangan kinerja (performance gap). Kegiatan yang dilakukan peneliti
meliputi:
a. Studi lapangan kondisi pembelajaran Informatika: Melakukan
wawancara dengan guru mata pelajaran untuk mengetahui kendala
pembelajaran Arsitektur Komputer yang selama ini berlangsung serta
mengidentifikasi karakteristik siswa kelas X, meliputi gaya belajar dan
kemampuan awal CT siswa untuk menentukan tingkat kesulitan gim.
b. Analisis kurikulum materi Arsitektur Von Neumann: Menganalisis
Capaian Pembelajaran (CP) dan Alur Tujuan Pembelajaran (ATP) pada
materi Arsitektur Komputer untuk memastikan konten gim relevan
dengan target kurikulum.
c. Analisis spesifikasi teknis lab komputer sekolah: Menganalisis
fasilitas yang bisa diakses siswa selama pembelajaran untuk
memastikan seluruh siswa dapat menggunakan media dengan maksimal.
3.3.2. Tahap Desain (Design)
Tahap ini bertujuan untuk memverifikasi performa yang diinginkan dan
metode pengujian yang tepat. Pada tahap ini, peneliti merancang integrasi
sintaks PBL ke dalam mekanika gim. Kegiatan yang dilakukan meliputi:
a. Penyusunan peta materi arsitektur komputer: Menentukan sub-
materi Arsitektur Komputer yang akan dimasukkan ke dalam level
permainan.
b. Perancangan gim dengan scaffolding sintaks PBL): Merancang alur
permainan (gameplay) yang disesuaikan dengan 5 sintaks PBL, yaitu:
orientasi masalah, organisasi belajar, penyelidikan, pengembangan
karya, hingga evaluasi. Rancangan sementara dapat dilihat pada tabel 1.
c. Pengayaan CT pada rancangan gim: menambahkan komponen CT
pada rancangan gim untuk penguatan CT siswa.
34

d. Perancangan instrumen kelayakan: Menyusun kisi-kisi lembar
validasi (mengadaptasi instrumen LORI 2.0) dan kisi-kisi soal tes CT.
e. Penyusunan game design document: Membuat storyboard, sketsa
visual antarmuka, alur navigasi gim dan lain lain.
3.3.3. Tahap Pengembangan (Develop)
Tahap ini bertujuan untuk menghasilkan dan memvalidasi sumber
belajar. Kegiatan yang dilakukan meliputi:
a. Produksi gim: Merealisasikan desain menjadi aplikasi gim nyata
menggunakan software Godot.
b. Validasi Ahli (Expert Judgment): Menggunakan instrumen adaptasi
LORI 2.0 untuk menilai aspek interaksi, desain visual, dan motivasi.
Selain itu, tahap ini juga menilai kesesuaian konsep Arsitektur
Komputer dan keterlaksanaan sintaks PBL di dalam gim.
c. Revisi Produk: Melakukan perbaikan gim berdasarkan masukan dan
saran dari para ahli validator.
3.3.4. Tahap Implementasi (Implement)
Tahap ini bertujuan untuk mempersiapkan lingkungan belajar dan
melibatkan siswa secara nyata.
a. Distribusi Pre-test & Seleksi Sampel: Peneliti mendistribusikan soal
pre-test ke beberapa kelas paralel populasi kelas X. Data hasil pre-test
dari berbagai kelas tersebut kemudian diuji Prasyarat (Normalitas dan
Homogenitas). Kelas yang terbukti memiliki varians data yang
homogen dan berdistribusi normal akan dipilih secara purposive sebagai
subjek penelitian utama (Sampel Eksperimen).
b. Treatment: Siswa menggunakan gim tersebut dalam kegiatan
pembelajaran kolaboratif berbasis kelompok kecil (small group
discussion) sesuai skenario pembelajaran yang telah dirancang..
c. Post-test: Peneliti menyebar soal Post-test dan angket respon siswa
untuk mengukur efektivitas dan kebergunaan media. Peneliti juga
melakukan observasi keterlaksanaan pembelajaran.
35

3.3.5. Tahap Evaluasi (Evaluate)
Tahap ini bertujuan untuk mengukur kualitas produk dan proses
pembelajaran. Evaluasi dilakukan dalam dua bentuk:
a. Evaluasi Formatif: Dilakukan sepanjang tahap analisis hingga
implementasi untuk perbaikan segera (misalnya perbaikan bug program
saat pengembangan).
b. Evaluasi Sumatif: seperti yang telah dijelaskan sebelumnya, peneliti
akan melakukan pengelompokkan (stratifikasi) data siswa berdasarkan
kemampuan akademik mereka. Lalu dianalisis menggunakan one-way
Anova untuk diukur pengaruh media pada siswa kelas bawah, tengah
dan atas. Peneliti juga akan mengukur kebergunaan media berdasarkan
angket yang telah disebar sebelumnya.
3.4. Subjek dan Tempat Penelitian
Penelitian ini dilaksanakan di jenjang SMA. Subjek penelitian adalah siswa
kelas 10 SMA tahun ajaran 2026/2027.
3.5.Instrumen Pengumpulan Data
3.5.1. Instrumen Non-Tes
• Lembar Validasi Ahli Media: Instrumen ini diadaptasi dari Learning
Object Review Instrument (LORI) v2.0 dengan penambahan indikator
khusus untuk memverifikasi fitur penunjang CT dalam gim. Kisi-kisi
instrumen terlampir pada Lampiran 1.
• Lembar Validasi Ahli Materi: Instrumen ini disusun untuk menilai
kebenaran konsep Arsitektur Komputer (Von Neumann) serta ketepatan
integrasi sintaks PBL dalam skenario permainan. instrumen terlampir
pada Lampiran 2.
• Angket Respon Siswa: Instrumen ini disusun untuk mengukur
kegunaan dan kepuasan pengguna. Butir pernyataan mengadopsi
instrumen SUS yang dimodifikasi menggunakan Skala Likert 4 poin
(Sangat Setuju, Setuju, Tidak Setuju, Sangat Tidak Setuju) untuk
menghindari bias jawaban netral (central tendency bias).
36

3.5.2. Instrumen Tes
Untuk mengukur kompetensi CT siswa pada materi arsitektur
komputer, digunakan butir soal yang menguji pemahaman siswa sekaligus
kemampuan CT siswa. Validitas butir soal dibuktikan melalui:
• Soal Tes CT: Instrumen utama untuk mengukur efektivitas berupa tes
objektif tipe Pilihan Ganda (Multiple Choice) yang diberikan pada tahap
pre-test dan post-test. Butir soal dikembangkan berdasarkan 4 indikator
CT (Dekomposisi, Pengenalan Pola, Abstraksi, Algoritma) yang
dikontekstualisasikan ke dalam kasus debugging arsitektur komputer.
• Kunci Jawaban dan Pedoman Penskoran: Dokumen ini berisi kunci
jawaban benar serta bobot penilaian untuk setiap butir soal guna
menjamin objektivitas pemeriksaan hasil belajar siswa. Pedoman ini
divalidasi terlebih dahulu oleh ahli materi sebelum digunakan.
• Analisis kualitas instrumen: Sebelum data hasil tes digunakan untuk
uji hipotesis, jawaban siswa dianalisis kualitasnya menggunakan
pendekatan Classical Test Theory (CTT). Parameter yang diuji meliputi
Validitas Empiris, Reliabilitas, Tingkat Kesukaran, Daya Beda, dan
Efektivitas Pengecoh (Distractor). Analisis ini dilaporkan pada Bab IV
untuk memastikan bahwa keputusan statistik didasarkan pada instrumen
yang memiliki karakteristik psikometrik yang layak.
3.6.Teknik Analisis Data
3.6.1. Analisis Data Kelayakan
Analisis ini menggunakan teknik deskriptif kuantitatif untuk mengolah
data non-tes:
1. Analisis Validitas Produk: Data skor dari Ahli Media dan Ahli Materi
dihitung rata-ratanya, kemudian dikonversi ke dalam kategori
kelayakan (Sangat Layak, Layak, Cukup, Kurang) untuk menentukan
apakah media siap diujicobakan.
2. Analisis Respon Siswa: Data angket respon dianalisis menggunakan
perhitungan persentase skor aktual terhadap skor ideal untuk
mengetahui tingkat kepraktisan dan penerimaan media oleh pengguna.
37

3.6.2. Analisis Data Efektivitas
Analisis statistik inferensial digunakan untuk menguji efektivitas media
terhadap peningkatan CT. Langkah-langkah analisis meliputi:
1. Perhitungan N-Gain per Komponen: Menghitung skor Normalized
Gain (N-Gain) untuk masing-masing dari 4 komponen CT
(Dekomposisi, Pengenalan Pola, Abstraksi, Algoritma) secara terpisah.
2. Uji Prasyarat: Melakukan uji Normalitas (Shapiro-Wilk) dan
Homogenitas (Levene’s Test) pada keempat kelompok data N-Gain
tersebut untuk memastikan data memenuhi asumsi dasar statistik
parametrik.
3. Pengelompokan Data (Grouping by Component): Alih-alih
mengelompokkan siswa berdasarkan kemampuan akademik (yang
berpotensi bias), data dikelompokkan berdasarkan aspek materi CT.
Tujuannya adalah membandingkan apakah gim simulasi berhasil
mengajarkan keempat aspek tersebut dengan kualitas yang setara.
• Kelompok 1: N-Gain Dekomposisi
• Kelompok 2: N-Gain Pengenalan Pola
• Kelompok 3: N-Gain Abstraksi
• Kelompok 4: N-Gain Algoritma
4. Uji Hipotesis (One-Way ANOVA): Menggunakan uji One-Way
ANOVA untuk mengetahui apakah terdapat perbedaan peningkatan
(mean N-Gain) yang signifikan antar keempat komponen tersebut.
• Jika nilai Sig. > 0.05 ( Diterima): Tidak terdapat perbedaan
signifikan antar komponen. Artinya, media terbukti efektif secara
holistik/seimbang dalam meningkatkan seluruh aspek CT. (Ini
adalah hasil yang diharapkan).
• Jika nilai Sig. < 0.05 ( Ditolak): Terdapat ketimpangan peningkatan
pada salah satu aspek, yang menjadi bahan evaluasi perbaikan fitur
gim.
38

DAFTAR PUSTAKA
Arends, R. (2015). Learning to teach (10th ed.). McGraw-Hill Companies.
Asrianti, M., & Rakhmawati, F. (2024). The effect of problem based learning model
on students’ mathematical computational thinking skills. Journal of
Mathematics Education, 9(1), 83–88.
Azwar, S. (2012). Penyusunan skala psikologi (Edisi ke-2). Pustaka Pelajar.
Bangor, A., Kortum, P. T., & Miller, J. A. (2008). An empirical evaluation of the
System Usability Scale. International Journal of Human-Computer
Interaction, 24(6), 574–594. https://doi.org/10.1080/10447310802205776
Blender Foundation. (2023). Blender 3.6 reference manual.
https://docs.blender.org/
Borg, W. R., & Gall, M. D. (1983). Educational research: An introduction (4th
ed.). Longman.
Bradfield, C. (2018). Godot engine game development in 24 hours, Sams teach
yourself: The official guide to Godot 3.0. Sams Publishing.
Branch, R. M. (2009). Instructional design: The ADDIE approach. Springer.
Brooke, J. (1996). SUS: A ‘quick and dirty’ usability scale. In P. W. Jordan, B.
Thomas, B. A. Weerdmeester, & A. L. McClelland (Eds.), Usability
evaluation in industry (pp. 189–194). Taylor & Francis.
Brookhart, S. M. (2013). How to create and use rubrics for formative assessment
and grading. ASCD.
Chen, R. (2017). Study on the practice of classroom teaching in the principles of
Feng Niman [Von Neumann]. Modern Basic Education Research, 28(4),
221–226.
Chernikova, O., Heitzmann, N., Stadler, M., Holzberger, D., Seidel, T., & Fischer,
F. (2020). Simulation-based learning in higher education: A meta-analysis.
Review of Educational Research, 90(4), 499–541.
39

Creswell, J. W. (2014). Research design: Qualitative, quantitative, and mixed
methods approaches (4th ed.). SAGE Publications.
Csizmadia, A., Curzon, P., Dorling, M., Humphreys, S., Ng, T., Selby, C., &
Woollard, J. (2015). Computational thinking: A guide for teachers.
Computing at School.
Curzon, P., & McOwan, P. W. (2017). The power of computational thinking:
Games, magic and puzzles to help you become a computational thinker.
World Scientific.
Field, A. (2018). Discovering statistics using IBM SPSS statistics (5th ed.). SAGE
Publications.
Fisher, R. A. (1925). Statistical methods for research workers. Oliver and Boyd.
Gee, J. P. (2005). Learning by design: Good video games as learning machines. E-
Learning and Digital Media, 2(1), 5–16.
Godot Community. (2023). Godot engine 4.1 documentation.
https://docs.godotengine.org/
Hake, R. R. (1998). Interactive-engagement versus traditional methods: A six-
thousand-student survey of mechanics test data for introductory physics
courses. American Journal of Physics, 66(1), 64-74.
Hidayad, M. A., & Prasetya, R. (2022). Perancangan aplikasi game edukasi
pengenalan komputer dasar berbasis Android. JRAMI (Jurnal Riset dan
Aplikasi Mahasiswa Informatika), 3(2), 205–212.
Hidayat, F. A., Asiska, L., Fitria, R., & Sari, S. I. (2024). Perancangan aplikasi
game edukasi pengenalan komputer dasar berbasis Android. Instink:
Inovasi Pendidikan, Teknologi Informasi dan Komputer, 3(1), 22–30.
Hill, C. (2020). Learning Godot 3.0: Create 2D and 3D games with Godot engine.
Packt Publishing.
40

Hwang, G. J., Wu, P. H., & Chen, C. C. (2012). An online game approach for
improving students’ learning performance in web-based problem-solving
activities. Computers & Education, 59(4), 1246–1256.
Ismail, A. M., & Nurjanah, D. (2025). Educational game for computational
thinking. Jurnal Locus Penelitian dan Pengabdian, 4(10), 9493–9501.
Judijanto, L., Muhammadiah, M. U., Utami, R. N., Suhirman, L., Laka, L., Boari,
Y., ... Yunus, M. (2024). Metodologi research and development: Teori dan
penerapan metodologi RnD. PT. Sonpedia Publishing Indonesia.
Kim, S. (2008). What is a puzzle. In T. Fullerton (Ed.), Game design workshop: A
playcentric approach to creating innovative games (pp. 35–39). Morgan
Kaufmann.
Leacock, T. L., & Nesbit, J. C. (2007). A framework for evaluating the quality of
multimedia learning resources. Educational Technology & Society, 10(2),
44–59.
Levene, H. (1960). Robust tests for equality of variances. In I. Olkin, S. G. Ghurye,
W. Hoeffding, W. G. Madow, & H. B. Mann (Eds.), Contributions to
probability and statistics: Essays in honor of Harold Hotelling (pp. 278–
292). Stanford University Press.
Likert, R. (1932). A technique for the measurement of attitudes. Archives of
Psychology, 140, 1–55.
Manzur, A., & Linietsky, J. (2014). Godot engine design philosophy. Godot Engine
Official Blog.
Mayer, R. E. (2019). Computer games in education. Annual Review of Psychology,
70, 531–549. https://doi.org/10.1146/annurev-psych-010418-102744
Moradi, M., & Noor, N. F. B. M. (2022). The impact of problem-based serious
games on learning motivation. IEEE Access, 10, 8339–8349.
https://doi.org/10.1109/ACCESS.2022.3140434
Munir. (2012). Multimedia konsep & aplikasi dalam pendidikan. Alfabeta.
41

Nurulaisyah, D., Probosari, R. M., & Antrakusuma, B. (2024). Problem-based
learning model on the collaboration and computational thinking skills.
Innovations in Science Education and Practice, 1(1), 36–46.
https://doi.org/10.20961/isep.v1i1.1757
Pan, Y., Adams, E. L., Ketterlin-Geller, L. R., Larson, E. C., & Clark, C. (2024).
Enhancing middle school students’ computational thinking competency
through game-based learning. Educational Technology Research and
Development, 72(6), 3391–3419.
Pasek, K. H., Zosh, J. M., Hadani, H. S., Golinkoff, R. M., Clark, K., Donohue, C.,
& Wartella, E. (2022). A whole new world: Education meets the metaverse
(Policy Brief). Center for Universal Education at Brookings.
Patterson, D. A., & Hennessy, J. L. (2020). Computer organization and design
RISC-V edition: The hardware software interface (2nd ed.). Morgan
Kaufmann.
Pryanka, M., & Sukirman, S. T. (2024). Pengembangan media pembelajaran untuk
simulasi fungsi sistem komputer [Doctoral dissertation, Universitas
Muhammadiyah Surakarta].
Putra, D. A. (2021). UI/UX design for mobile applications with Figma. Elex Media
Komputindo.
Putra, I. M. A. R., Kesiman, M. W. A., & Darmawiguna, I. G. M. (2023).
Pengembangan media pembelajaran berbasis Android pada mata pelajaran
sistem komputer di kelas X SMKN 1 Manggis. KARMAPATI (Kumpulan
Artikel Mahasiswa Pendidikan Teknik Informatika), 12(1), 17–25.
Sari, E. D. K., Rustam, A., & Yunita, L. (2021). Pengembangan instrumen
penelitian sosial. Kun Fayakun.
Schell, J. (2019). The art of game design: A book of lenses (3rd ed.). A K
Peters/CRC Press. https://doi.org/10.1201/b22101
Shapiro, S. S., & Wilk, M. B. (1965). An analysis of variance test for normality
(complete samples). Biometrika, 52(3/4), 591–611.
42

Shofiah, S., Bachtiar, E., Permatasari K. D., D., Syahropi, H., Zaman, N., Salam.,
... Hidayat, N. (2023). Dasar-dasar evaluasi pembelajaran. PT. Mifandi
Mandiri Digital.
Shute, V. J., Sun, C., & Asbell-Clarke, J. (2017). Demystifying computational
thinking. Educational Research Review, 22, 142–158.
Stallings, W. (2022). Computer organization and architecture: Designing for
performance. Pearson Education India.
Sugiyono. (2019). Metode penelitian kuantitatif, kualitatif, dan R&D. Alfabeta.
Wahyuni, K. A., Wibawa, I. M. C., & Rismawan, K. S. G. (2025). Interactive
multimedia educational games based on problem-based learning (PBL) for
ecosystem material to enhance student learning motivation. MIMBAR
PGSD Undiksha, 13(1), 200–209.
Wang, W. (2019). Godot engine game development projects. Packt Publishing.
Xue, S. (2021). Overview of computer architecture development direction breaking
through Von Neumann architecture. International Core Journal of
Engineering, 7(8), 330–334.
Yew, E. H. J., & Goh, K. (2016). Problem-based learning: An overview of its
process and impact on learning. Health Professions Education, 2(2), 75–79.
https://doi.org/10.1016/j.hpe.2016.01.004
Zhonggen, Y. (2019). A meta-analysis of use of serious games in education over a
decade. International Journal of Computer Games Technology, 2019, 1–8.
https://doi.org/10.1155/2019/4797032
Zhu, W., Fang, Y., & San, Y. (2013). Research on the limitation of Von Noyan
[Neumann] system computer. Journal of Science and Technology, 36, 67–
68.
43

LAMPIRAN
Lampiran 1. Rubrik kelayakan media
Aspek Penilaian
Indikator Penilaian
(LORI 2.0)
Kebenaran logika simulasi Input-Proses-Output pada arsitektur Von
Kualitas Konten Neumann (bebas dari kesalahan konsep alur data).
(Content Quality) Keseimbangan penyajian antara teks instruksi dan visualisasi aliran
data (data flow visualization).
Kesesuaian mekanika pembuatan 'node' dengan Capaian Pembelajaran
Keselarasan Tujuan
(CP) Fase E (Memahami model komputasi).
(Learning Goal
Kejelasan target kompetensi: siswa mampu merancang/memperbaiki
Alignment)
sistem, bukan sekadar menghafal nama komponen.
Ketepatan respon sistem: Munculnya visualisasi error (misal: data
macet/meledak) ketika siswa salah menyusun urutan node atau logika
Umpan Balik
instruksi.
(Feedback)
Scaffolding: Sistem memberikan petunjuk (hint) bertahap saat siswa
mengalami kebuntuan dalam merancang alur.
Kemampuan elemen tantangan menarik minat siswa untuk
Motivasi bereksperimen dengan berbagai desain arsitektur node.
(Motivation) Relevansi Skenario: Pergeseran peran dari "Teknisi" menjadi "Arsitek
Sistem" yang relevan dengan konsep Computational Thinking.
Kualitas estetika antarmuka (UI) node dan jalur bus data agar mudah
Desain Presentasi
dibedakan fungsinya.
(Presentation
Visualisasi pergerakan data (animasi) yang jelas dan mendukung
Design)
pemahaman abstrak.
Kemudahan fitur Drag-and-Drop saat menyusun atau menghubungkan
Kemudahan
node komponen.
Interaksi
Responsivitas tombol simulasi (Run/Stop/Step-by-step) untuk menguji
(Usability)
rancangan.
Gim dapat berjalan lancar (ringan) saat memproses simulasi logika
Aksesibilitas yang kompleks pada perangkat sekolah.
(Accessibility) Keterbacaan teks kode instruksi (mnemonic) dan angka biner/hex pada
layar.
Dekomposisi: Fitur yang memfasilitasi siswa memecah sistem besar
menjadi modul Input, Proses, dan Output terpisah.
Pengenalan Pola: Konsistensi visualisasi siklus instruksi (Fetch-
Decode-Execute) yang membantu siswa mengenali pola kerja CPU.
Kesesuaian Fitur Abstraksi: Penggunaan simbol/ikon node sederhana (Black Box) untuk
CT (CT Support) mewakili komponen rumit (misal: Node ALU hanya berupa kotak
"+").
Algoritma: Mekanisme permainan yang menuntut siswa menyusun
node secara sekuensial/berurutan agar data dapat diproses menjadi
output yang benar.
44

Lampiran 2. Rubrik kelayakan materi dalam gim
Aspek
Indikator Penilaian
Penilaian
Kebenaran Konsep Von Neumann: Akurasi representasi Stored-
Program Concept (Data dan Instruksi di memori yang sama).
Substansi Akurasi Alur Data (Datapath): Ketepatan logika perpindahan
Arsitektur data antar register, ALU, dan Memori dalam simulasi.
Komputer Logika Instruksi: Kesesuaian hasil eksekusi simulasi dengan
prinsip kerja komputer (Misal: Jika instruksi ADD, maka nilai
Akumulator bertambah).
Orientasi Masalah: Kasus yang disajikan berupa "Kegagalan
Sistem" atau "Output Salah" yang menuntut analisis logika
(bukan kerusakan fisik).
Penyelidikan Mandiri: Gim memfasilitasi siswa untuk
Integrasi PBL
melakukan eksperimen "Trial & Error" dalam
(Pedagogical)
merancang/memperbaiki node tanpa batasan kaku.
Evaluasi & Refleksi: Fitur Debug Console atau Log Report yang
membantu siswa mengevaluasi mengapa rancangan mereka
gagal atau berhasil.
Materi menuntut siswa melakukan Dekomposisi masalah
Konstruksi
(memecah error besar menjadi error per komponen).
CT dalam
Materi melatih Abstraksi dengan mengabaikan detail kelistrikan
Materi
dan fokus pada logika informasi.
45