"""
LogiTrace: Builder for 36-Item Parallel Troubleshooting Instruments (Form A Pretest & Form B Posttest).
Framework: David H. Jonassen & Woei Hung (2006) Cognitive Troubleshooting in Computer Networks.
Structure per Form:
- 30 Target Two-Tier Items (5 Phases x 6 Items)
- 6 NEDV Control Two-Tier Items (2 VoIP + 4 Fiber Optic)
Total: 36 Items in Form A & 36 Items in Form B (Polytomous scoring 0, 1, 2).
"""

import json
import os

OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "troubleshooting_test_parallel.json")


def build_parallel_troubleshooting_bank():
    # 5 Jonassen (2006) Cognitive Troubleshooting Phases
    # 1. SYMPTOM_RECOGNITION (6 items)
    # 2. PROBLEM_SPACE_CONSTRUCTION (6 items)
    # 3. FAULT_HYPOTHESIS_GENERATION (6 items)
    # 4. HYPOTHESIS_TESTING_EVALUATION (6 items)
    # 5. CORRECTIVE_ACTION_VERIFICATION (6 items)
    # NEDV: 6 items (2 VoIP, 4 Fiber Optic)

    form_a_items = [
        # --- FASE 1: SYMPTOM_RECOGNITION (A01 - A06) ---
        {
            "id": "TB_A_SR_01",
            "phase": "SYMPTOM_RECOGNITION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Seorang teknisi memasang kabel UTP baru dari switch ke komputer klien di lab TKJ. Setelah kabel ditancapkan, lampu indikator LED Link/Act pada port switch sama sekali tidak menyala (mati total). Gejala fisik ini mengindikasikan bahwa...",
            "options": {
                "A": "Terjadi tabrakan alamat IP statis (IP conflict) pada komputer klien.",
                "B": "Tidak terbentuk koneksi elektrik sinyal pada Lapisan Fisik (Layer 1 OSI).",
                "C": "Firewall sistem operasi klien memblokir paket pengujian ICMP.",
                "D": "Konfigurasi subnet mask komputer klien berbeda segmen dengan switch."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Karena lampu LED port switch mendeteksi integritas pulsa fisik (link pulse) pada pasangan pin kabel tembaga sebelum protokol layer atas berjalan.",
                "2": "Karena switch otomatis mematikan lampu port jika klien belum melakukan login autentikasi pengguna.",
                "3": "Karena lampu link hanya akan menyala jika komputer klien berhasil melakukan ping ke gateway internet."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_SR_02",
            "phase": "SYMPTOM_RECOGNITION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Saat melakukan uji konektivitas dari Laptop A ke Laptop B menggunakan perintah 'ping 192.168.10.5', terminal menampilkan pesan galat berulang: 'Destination Host Unreachable'. Gejala galat ini mengindikasikan bahwa...",
            "options": {
                "A": "Paket data berhasil sampai ke tujuan namun diblokir oleh software firewall.",
                "B": "Pengirim tidak berhasil menemukan rute fisik atau pemetaan alamat MAC target pada subnet lokal.",
                "C": "Waktu tempuh paket melampaui batas Time-To-Live (TTL = 0) di router.",
                "D": "Antarmuka kartu jaringan Laptop A mengalami kerusakan sirkuit nirkabel."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Pesan DHU menandakan protokol ARP lokal gagal memperoleh respons MAC Address tujuan atau gateway tidak memiliki rute ke subnet target.",
                "2": "Pesan DHU selalu berarti kabel jaringan putus tepat di tengah-tengah bentangan.",
                "3": "Pesan DHU merupakan respons resmi saat server web menolak koneksi port HTTP 80."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_SR_03",
            "phase": "SYMPTOM_RECOGNITION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Laptop siswa telah berhasil terhubung ke SSID Wi-Fi lab dan memperoleh IP 192.168.1.15. Namun saat melakukan ping ke komputer guru (192.168.1.1), terminal menampilkan 'Request Timed Out' (RTO). Gejala ini paling tepat menunjukkan bahwa...",
            "options": {
                "A": "Paket Echo Request terkirim namun paket Echo Reply tidak diterima kembali sebelum batas waktu habis.",
                "B": "Kartu Wi-Fi laptop siswa tidak mendukung standar enkripsi WPA2.",
                "C": "Access Point mengalami kegagalan modulasi frekuensi radio 2.4 GHz.",
                "D": "Kabel serat optik uplink mengalami tekukan tajam (macro-bending)."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "RTO terjadi karena paket dibuang di tengah jalan, di-drop oleh firewall host tujuan, atau rute balik ke pengirim terputus.",
                "2": "RTO hanya terjadi jika kabel patch cord switch dilepas secara sengaja oleh pengguna.",
                "3": "RTO menandakan bahwa komputer tujuan otomatis mati seketika saat menerima paket ICMP."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_SR_04",
            "phase": "SYMPTOM_RECOGNITION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Seorang siswa duduk di sudut ruangan lab TKJ dan mendapati bar sinyal Wi-Fi di ponselnya hanya 1 bar (-86 dBm). Saat melakukan penjelajahan web, kecepatan terasa sangat lambat dan sering putus. Gejala penurunan sinyal ini menandakan...",
            "options": {
                "A": "Ponsel siswa otomatis menurunkan resolusi layar saat sinyal lemah.",
                "B": "Nilai Received Signal Strength Indicator (RSSI) mendekati ambang batas sensitivitas penerima (noise floor).",
                "C": "Access Point kehabisan alamat IP DHCP pool untuk ponsel siswa.",
                "D": "Kanal frekuensi 5 GHz otomatis berpindah ke frekuensi radio gelombang pendek."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Nilai RSSI di bawah -80 dBm menghasilkan Signal-to-Noise Ratio (SNR) yang sangat rendah sehingga modulasi data beralih ke skema paling rendah (BPSK) dengan retransmisi tinggi.",
                "2": "Karena nilai dBm yang semakin negatif menunjukkan sinyal semakin kuat dan cepat.",
                "3": "Karena sinyal radio Wi-Fi tidak dapat merambat jika di dalam ruangan terdapat udara lembap."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_SR_05",
            "phase": "SYMPTOM_RECOGNITION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Pada taskbar sistem operasi laptop siswa muncul ikon jaringan dengan tanda seru kuning ('No Internet, Secured'). Saat diperiksa via command prompt, IP yang tertera adalah 169.254.45.12. Gejala ini secara spesifik menunjukkan bahwa...",
            "options": {
                "A": "Laptop terinfeksi malware yang memblokir kartu jaringan.",
                "B": "Laptop gagal memperoleh sewa konfigurasi dari DHCP Server sehingga mengaktifkan APIPA.",
                "C": "Access Point mengalami overheat dan mematikan fungsi radio Wi-Fi.",
                "D": "Subnet mask yang dimasukkan guru salah format bit."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Rentang IP 169.254.0.0/16 adalah Automatic Private IP Addressing (APIPA) yang dialokasikan otomatis oleh OS ketika permintaan DHCP Discover/Request tidak dijawab oleh server.",
                "2": "IP 169.254.x.x adalah alamat IP publik resmi dari penyedia layanan internet (ISP).",
                "3": "Tanda seru kuning menandakan bahwa laptop sedang mengunduh pembaruan firmware kartu nirkabel."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_SR_06",
            "phase": "SYMPTOM_RECOGNITION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Ketika seorang teknisi mencoba menyambungkan perangkat laptop baru ke Access Point dengan keamanan WPA2-Personal, muncul pesan galat 'Authentication problem' atau 'Can't connect to this network' secara berulang. Gejala awal ini paling sering disebabkan oleh...",
            "options": {
                "A": "Ketidakcocokan pre-shared key (password Wi-Fi) antara klien dan Access Point.",
                "B": "Tabel routing dinamis OSPF pada router mengalami kegagalan konvergensi.",
                "C": "Kabel UTP yang menghubungkan AP ke switch menggunakan standar crossover.",
                "D": "Suhu ruangan laboratorium melebihi batas operasional perangkat."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Kegagalan pada tahap 4-Way Handshake WPA2 terjadi jika Message Integrity Code (MIC) tidak cocok akibat salah input kata sandi pra-bagi (PSK).",
                "2": "Karena WPA2-Personal hanya mengizinkan maksimal 5 perangkat yang terhubung dalam satu hari.",
                "3": "Karena perangkat laptop baru selalu ditolak oleh protokol CSMA/CA."
            },
            "correct_reasoning": "1"
        },

        # --- FASE 2: PROBLEM_SPACE_CONSTRUCTION (A07 - A12) ---
        {
            "id": "TB_A_PC_01",
            "phase": "PROBLEM_SPACE_CONSTRUCTION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Seorang teknisi jaringan ingin menguji apakah antena eksternal dengan gain 9 dBi dapat meningkatkan jangkauan sinyal di area laboratorium terbuka dibanding antena bawaan 3 dBi. Variabel manakah yang harus dijaga konstan selama pengujian agar kesimpulan yang diambil valid?",
            "options": {
                "A": "Daya transmisi Access Point (Tx Power), posisi letak AP, dan orientasi sudut antena.",
                "B": "Tipe perangkat klien penerima, jarak pengujian, dan merek antena eksternal.",
                "C": "Kanal frekuensi yang digunakan dan jumlah pengguna yang melakukan streaming video.",
                "D": "Tingkat sensitivitas penerima klien dan perubahan cuaca luar ruangan."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Karena variabel bebas yang diuji adalah gain antena, maka seluruh parameter pemancar lain (daya Tx, lokasi, orientasi) dan lingkungan uji wajib dikendalikan tetap.",
                "2": "Karena antena dengan dBi tinggi selalu otomatis melipatgandakan jangkauan sinyal tanpa terpengaruh parameter lainnya.",
                "3": "Karena jarak pengujian harus bervariasi secara bebas bersamaan dengan penggantian daya pancar Access Point."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_PC_02",
            "phase": "PROBLEM_SPACE_CONSTRUCTION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Dalam eksperimen perbandingan redaman sinyal Wi-Fi 5 GHz terhadap dua partisi dinding (partisi gypsum vs kaca tebal), variabel manakah yang harus diubah (variabel manipulasi) sementara variabel lainnya dikontrol?",
            "options": {
                "A": "Jarak antara Access Point ke dinding.",
                "B": "Jenis material partisi penghalang.",
                "C": "Frekuensi kerja Access Point.",
                "D": "Daya pancar pemancar Wi-Fi."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Untuk mengisolasi efek daya serap material, hanya jenis partisi yang boleh diganti, sedangkan ketebalan, jarak, frekuensi, dan daya pancar wajib konstan.",
                "2": "Karena dinding kaca selalu memantulkan gelombang sedangkan gypsum selalu menyerapnya secara sempurna.",
                "3": "Karena frekuensi 5 GHz lebih mudah menembus dinding jika daya pancar diubah-ubah bersamaan."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_PC_03",
            "phase": "PROBLEM_SPACE_CONSTRUCTION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Sebuah PC di ruang bengkel TKJ tidak dapat mengakses server lokal. Untuk memetakan ruang masalah secara metodis (bottom-up), langkah uji pertama yang harus dilakukan teknisi sebelum menyalahkan router utama adalah...",
            "options": {
                "A": "Merestart router gateway dan modem internet ISP.",
                "B": "Melakukan uji ping ke alamat loopback lokal (127.0.0.1) dan memeriksa status link adapter.",
                "C": "Menginstal ulang sistem operasi pada PC bengkel.",
                "D": "Mengganti seluruh kabel instalasi di dalam dinding pipa konduit."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Uji loopback 127.0.0.1 memvalidasi integritas stack protokol TCP/IP internal pada PC lokal sebelum melangkah ke pengujian media fisik dan gateway jaringan.",
                "2": "Karena merestart router adalah satu-satunya cara mendeteksi kerusakan pada kartu jaringan komputer klien.",
                "3": "Karena alamat 127.0.0.1 menguji kecepatan transmisi kabel UTP hingga ke switch utama."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_PC_04",
            "phase": "PROBLEM_SPACE_CONSTRUCTION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Seorang siswa membuat kabel jaringan UTP sepanjang 20 meter. Sebelum dihubungkan ke komputer server, kabel diuji menggunakan kabel LAN tester. Pengujian ini bertujuan untuk mengisolasi batas masalah pada...",
            "options": {
                "A": "Kesesuaian alamat IP dan subnetting pada komputer server.",
                "B": "Kontinuitas elektrik dan ketepatan pemetaan urutan 8 pin kabel (pinout T568A/T568B).",
                "C": "Kecepatan transfer data riil pada protokol HTTP dan FTP.",
                "D": "Kemampuan kabel menahan serangan injeksi paket dari internet."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "LAN tester secara sekuensial memverifikasi apakah ada kabel yang putus (open), terhubung singkat (short), atau urutan pin tertukar (miswire) pada layer 1 fisik.",
                "2": "LAN tester berfungsi memberikan alamat IP otomatis pada konektor RJ45.",
                "3": "LAN tester digunakan untuk menguji kekuatan sinyal radio Wi-Fi di dalam jaket kabel tembaga."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_PC_05",
            "phase": "PROBLEM_SPACE_CONSTRUCTION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Di sebuah ruang kelas, seorang siswa mengeluh koneksi Wi-Fi laptopnya sering terputus. Sedangkan 30 siswa lain di ruangan yang sama menggunakan laptop masing-masing dan terhubung lancar tanpa kendala. Bagaimana teknisi mengisolasi ruang masalah ini?",
            "options": {
                "A": "Fokus memeriksa pengaturan, driver, dan kartu Wi-Fi pada laptop siswa yang bermasalah.",
                "B": "Segera mereset konfigurasi pabrik (factory reset) pada Access Point utama kelas.",
                "C": "Mengganti kabel uplink dari switch ke Access Point dengan kabel fiber optik.",
                "D": "Meminta provider internet menaikkan kapasitas bandwidth langganan sekolah."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Karena 30 perangkat lain berfungsi normal, maka subsistem Access Point dan jaringan sekolah terbukti sehat; masalah terlokalisir secara eksklusif pada sisi perangkat klien.",
                "2": "Karena Access Point selalu mematikan koneksi secara acak kepada siswa yang duduk di baris depan.",
                "3": "Mereset AP adalah tindakan wajib setiap kali ada satu pengguna yang mengalami masalah koneksi."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_PC_06",
            "phase": "PROBLEM_SPACE_CONSTRUCTION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Koneksi jaringan nirkabel di laboratorium tiba-tiba mengalami lonjakan packet loss hanya pada jam istirahat saat kantin sekolah mulai menghangatkan makanan menggunakan oven microwave. Untuk mengonfirmasi batas masalah ini, teknisi harus mengontrol variabel dengan cara...",
            "options": {
                "A": "Mengamati kestabilan sinyal saat microwave dinyalakan dan dimatikan secara terkontrol pada pita 2.4 GHz vs 5 GHz.",
                "B": "Mengganti seluruh konektor RJ45 pada kabel UTP di ruang server.",
                "C": "Mematikan server database utama sekolah.",
                "D": "Mengubah alamat IP gateway dari statis ke DHCP."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Oven microwave memancarkan radiasi elektromagnetik pada spektrum 2.45 GHz yang menginterferensi pita Wi-Fi 2.4 GHz; menguji operasi on/off mengisolasi variabel penyebab secara pasti.",
                "2": "Karena gelombang mikro microwave merusak kabel serat optik di bawah tanah.",
                "3": "Karena microwave menyerap daya listrik router hingga tegangan drop 0 Volt."
            },
            "correct_reasoning": "1"
        },

        # --- FASE 3: FAULT_HYPOTHESIS_GENERATION (A13 - A18) ---
        {
            "id": "TB_A_FH_01",
            "phase": "FAULT_HYPOTHESIS_GENERATION",
            "curriculum_element": "TP 2.1 - Instalasi Jaringan Nirkabel",
            "prompt": "Sebuah Access Point nirkabel beroperasi pada lebar kanal 20 MHz dan menghasilkan throughput riil rata-rata 60 Mbps. Jika lebar kanal dinaikkan menjadi 40 MHz pada kondisi modulasi dan rasio sinyal terhadap derau (SNR) yang setara, berapakah estimasi throughput baru yang diharapkan?",
            "options": {
                "A": "Mencapai 240 Mbps (meningkat empat kali lipat).",
                "B": "Tetap 60 Mbps karena frekuensi dasarnya tidak berubah.",
                "C": "Mendekati 120 Mbps (meningkat sebanding secara proporsional).",
                "D": "Turun menjadi 30 Mbps karena adanya pelebaran spektrum frekuensi."
            },
            "correct_option": "C",
            "reasoning_options": {
                "1": "Kapasitas saluran nirkabel (Teorema Shannon-Hartley) berbanding lurus secara proporsional dengan lebar pita (bandwidth) saluran saat SNR konstan.",
                "2": "Kecepatan selalu berbanding kuadrat terhadap lebar frekuensi saluran radio.",
                "3": "Lebar kanal yang lebih besar otomatis membagi kecepatan data menjadi dua kali lebih lambat pada masing-masing subcarrier."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_FH_02",
            "phase": "FAULT_HYPOTHESIS_GENERATION",
            "curriculum_element": "TP 2.1 - Instalasi Jaringan Nirkabel",
            "prompt": "Berdasarkan prinsip Free Space Path Loss (FSPL), pelemahan daya sinyal berbanding terbalik dengan kuadrat jarak. Jika seorang siswa bergerak menjauhi Access Point dari jarak 5 meter ke jarak 10 meter (2 kali lipat jarak awal), bagaimanakah kerapatan daya sinyal yang diterima antena ponselnya?",
            "options": {
                "A": "Tetap sama karena ponsel memiliki sirkuit Automatic Gain Control.",
                "B": "Berkurang menjadi 1/2 (setengah) dari daya awal.",
                "C": "Berkurang menjadi 1/8 (seperdelapan) dari daya awal.",
                "D": "Berkurang menjadi 1/4 (seperempat) dari daya awal."
            },
            "correct_option": "D",
            "reasoning_options": {
                "1": "Sesuai hukum kuadrat terbalik (inverse-square law), melipatgandakan jarak (r -> 2r) menyebabkan kerapatan daya sinyal turun menjadi 1/(2^2) = 1/4 dari nilai semula.",
                "2": "Penurunan sinyal selalu sebanding linier dengan bertambahnya jarak meter per meter.",
                "3": "Gelombang elektromagnetik di udara terbuka tidak mengalami pelemahan jika tidak ada penghalang fisik."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_FH_03",
            "phase": "FAULT_HYPOTHESIS_GENERATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Sebuah kabel patch cord serat optik yang rapi diikat erat menggunakan cable tie plastik tiba-tiba mengalami lonjakan nilai redaman (optical loss) drastis dari 0.3 dB menjadi 8.5 dB. Hipotesis penyebab kerusakan fisik yang paling logis adalah...",
            "options": {
                "A": "Terjadi induksi medan magnet dari kabel listrik yang berdekatan.",
                "B": "Terjadi macro-bending akibat ikatan yang terlalu kencang melampaui batas minimum bending radius.",
                "C": "Inti kaca (core) serat optik kehabisan elektron konduksi.",
                "D": "Panjang gelombang cahaya laser otomatis memendek akibat tekanan fisik."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Tekukan tajam (macro-bending) mengubah sudut datang cahaya di batas core-cladding melebihi sudut kritis, sehingga pulsa cahaya bocor keluar dari inti serat kaca.",
                "2": "Kabel serat optik sangat rentan terhadap radiasi magnetik dari kabel listrik AC.",
                "3": "Cable tie plastik bereaksi kimia melarutkan lapisan kaca fiber optik."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_FH_04",
            "phase": "FAULT_HYPOTHESIS_GENERATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Sebuah bentangan kabel UTP Cat5e dipasang menghubungkan lab lantai 1 ke pos satpam sejauh 145 meter. Koneksi sering putus, negosiasi kecepatan mentok di 10 Mbps, dan packet loss mencapai 35%. Hipotesis kausal yang tepat adalah...",
            "options": {
                "A": "Panjang kabel melebihi batas standar transmisi tembaga Ethernet (100 meter) sehingga sinyal mengalami atenuasi dan distorsi propagasi tinggi.",
                "B": "Komputer di pos satpam menggunakan sistem operasi yang terlalu baru.",
                "C": "Kabel UTP otomatis mematikan fungsi pengiriman data jika terkena angin kencang.",
                "D": "Tegangan listrik di pos satpam membuat kabel tembaga memuai secara permanen."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Standar IEEE 802.3 100BASE-TX menetapkan batas maksimum kabel twisted pair adalah 100 meter (90m horizontal + 10m patch); melampaui batas ini memicu atenuasi dan pelanggaran batas deteksi tabrakan CSMA/CD.",
                "2": "Kabel UTP sebenarnya mampu menjangkau 500 meter asalkan menggunakan konektor RJ45 emas.",
                "3": "Atenuasi kabel tembaga tidak dipengaruhi oleh panjang bentangan melainkan warna kulit isolatornya."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_FH_05",
            "phase": "FAULT_HYPOTHESIS_GENERATION",
            "curriculum_element": "TP 2.1 - Instalasi Jaringan Nirkabel",
            "prompt": "Access Point di lab TKJ memancarkan sinyal dual-band (2.4 GHz dan 5 GHz). Di ruangan kelas sebelah yang terpisah dinding beton bertulang 15 cm, sinyal 2.4 GHz masih terbaca 3 bar, namun sinyal 5 GHz hilang total. Hipotesis ilmiah atas fenomena ini adalah...",
            "options": {
                "A": "Frekuensi 5 GHz memiliki panjang gelombang lebih pendek sehingga mengalami penyerapan (absorpsi) dan redaman material yang jauh lebih tinggi pada medium padat.",
                "B": "Frekuensi 5 GHz sengaja diprogram pabrik untuk tidak boleh keluar ruangan.",
                "C": "Dinding beton bertulang memantulkan 2.4 GHz tetapi meneruskan 5 GHz ke angkasa.",
                "D": "Ponsel siswa memblokir frekuensi 5 GHz jika berada di balik tembok."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Semakin tinggi frekuensi, panjang gelombangnya semakin pendek (lambda = c/f), menyebabkan energi foton gelombang lebih mudah diserap oleh molekul air dan partikel padat dinding beton.",
                "2": "Karena gelombang 2.4 GHz memiliki daya listrik lebih kuat dibanding 5 GHz.",
                "3": "Karena standar IEEE 802.11 melarang gelombang 5 GHz menembus material semen."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_FH_06",
            "phase": "FAULT_HYPOTHESIS_GENERATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Hasil pemantauan koneksi VoIP antar-ruangan menunjukkan lonjakan jitter dari 3 ms menjadi 65 ms dan packet loss 12% setiap kali siswa kelas animasi melakukan upload file video 4K ke cloud. Hipotesis hubungan sebab-akibat yang paling valid adalah...",
            "options": {
                "A": "Saturasi kapasitas uplink memicu bufferbloat pada router sehingga antrean paket data VoIP tertunda secara bervariasi.",
                "B": "File video 4K mengubah frekuensi pembawa kabel UTP menjadi tidak stabil.",
                "C": "Server VoIP otomatis memotong panggilan jika mendeteksi ada file video di jaringan.",
                "D": "Kamera video animasi memancarkan interferensi elektromagnetik ke kabel telepon."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Ketika bandwidth uplink penuh (100% utilitas) tanpa penerapan Quality of Service (QoS / traffic shaping), paket UDP real-time VoIP terhambat di antrean buffer router, menyebabkan fluktuasi latensi (jitter) tinggi.",
                "2": "Protokol VoIP membutuhkan kabel tembaga murni tanpa campuran timbal agar bebas jitter.",
                "3": "Upload video menghabiskan seluruh daya listrik switch hub di laboratorium."
            },
            "correct_reasoning": "1"
        },

        # --- FASE 4: HYPOTHESIS_TESTING_EVALUATION (A19 - A24) ---
        {
            "id": "TB_A_TE_01",
            "phase": "HYPOTHESIS_TESTING_EVALUATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Di laboratorium TKJ terpasang AP Utama (Sinyal A) dan WLAN Extender (Sinyal B). Ambang batas roaming (roaming threshold) pada adapter laptop siswa disetel pada -75 dBm. Jika siswa bergerak menjauh hingga Sinyal A terbaca -78 dBm sementara Sinyal B terbaca -62 dBm, bagaimanakah probabilitas keputusan perangkat?",
            "options": {
                "A": "Laptop memiliki probabilitas sangat tinggi untuk memicu proses disasosiasi dari AP Utama dan berpindah (roaming) ke WLAN Extender.",
                "B": "Laptop dipastikan tetap bertahan pada AP Utama hingga sinyal mencapai 0 dBm.",
                "C": "Laptop akan mematikan kartu nirkabelnya karena bingung memilih pemancar.",
                "D": "Laptop akan terhubung ke kedua AP secara simultan untuk menggabungkan kecepatan."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Karena sinyal AP asal (-78 dBm) telah melewati batas ambang roaming (-75 dBm) dan sinyal AP baru (-62 dBm) melampaui selisih margin histeresis yang disyaratkan algoritma handover.",
                "2": "Karena perangkat Wi-Fi selalu otomatis berganti koneksi setiap 3 menit terlepas dari kekuatan sinyal.",
                "3": "Karena WLAN Extender selalu memiliki prioritas koneksi lebih tinggi daripada AP Utama."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_TE_02",
            "phase": "HYPOTHESIS_TESTING_EVALUATION",
            "curriculum_element": "TP 2.1 - Instalasi Jaringan Nirkabel",
            "prompt": "Dalam ruangan tertutup terdapat 30 siswa yang sedang mengakses video pembelajaran secara bersamaan pada 1 Access Point kanal 6 (lebar 20 MHz). Jika mekanisme CSMA/CA digunakan, bagaimanakah probabilitas terjadinya tabrakan data (collision) dan latensi rata-rata?",
            "options": {
                "A": "Peluang tabrakan menurun drastis dan latensi mendekati 0 milidetik.",
                "B": "Peluang tabrakan meningkat signifikan dan waktu tunda (backoff time) bertambah akibat perebutan media transmisi bersama (shared medium).",
                "C": "Kecepatan transfer data seluruh siswa tetap stabil pada 54 Mbps tanpa terpengaruh jumlah pengguna.",
                "D": "Access Point otomatis mengubah frekuensi menjadi gelombang inframerah."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "CSMA/CA bekerja secara half-duplex; semakin banyak klien yang bersaing dalam satu contention domain, semakin sering terjadi tabrakan transmisi simultan yang memicu backoff acak eksponensial.",
                "2": "Karena 1 Access Point mampu melayani 1000 koneksi bersamaan tanpa penurunan performa sedikit pun.",
                "3": "Karena kabel jaringan di dalam AP memiliki kapasitas tidak terbatas."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_TE_03",
            "phase": "HYPOTHESIS_TESTING_EVALUATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Teknisi menguji kabel serat optik single-mode sepanjang 3 km menggunakan Optical Power Meter (OPM). Nilai daya laser pemancar (Tx) adalah +3 dBm dan daya yang terbaca di penerima (Rx) adalah -27 dBm (Total Redaman Link = 30 dB). Hasil evaluasi diagnostik teknis ini menunjukkan bahwa...",
            "options": {
                "A": "Link serat optik dalam kondisi prima dan siap digunakan untuk koneksi 10 Gbps.",
                "B": "Terjadi anomali redaman sangat berat (abnormal loss) yang melampaui batas toleransi link budget serat optik standar.",
                "C": "Kabel serat optik membutuhkan pemanasan menggunakan oven splicing.",
                "D": "Nilai redaman 30 dB adalah standar mutlak dari ITU-T untuk kabel dalam kota."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Atenuasi standar single-mode pada panjang gelombang 1310/1550 nm hanya sekitar 0.35–0.4 dB/km (total wajar link 3 km ~ 1.5–2.5 dB termasuk konektor); redaman 30 dB mengindikasikan konektor kotor, patahan micro-crack, atau kesalahan splicing parah.",
                "2": "Karena serat optik single-mode selalu memiliki redaman minimal 10 dB setiap kilometer.",
                "3": "Karena OPM hanya dapat membaca daya jika kabel optik dialiri arus listrik 220 Volt."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_TE_04",
            "phase": "HYPOTHESIS_TESTING_EVALUATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Hasil pemindaian aplikasi Wi-Fi Analyzer memperlihatkan AP Lab TKJ disetel pada Kanal 3 pita 2.4 GHz, sementara AP Lab RPL di sebelahnya berada pada Kanal 1 dan AP Ruang Guru pada Kanal 6. Evaluasi teknis terhadap pengujian spektrum ini adalah...",
            "options": {
                "A": "Setelan kanal 3 adalah pilihan paling ideal karena membagi frekuensi secara rata di tengah.",
                "B": "Terjadi Adjacent-Channel Interference parah karena spektrum kanal 3 bertumpuk (overlap) dengan kanal 1 sekaligus kanal 6.",
                "C": "Kanal 3 otomatis mematikan interferensi dari kanal 1 dan 6 secara elektronik.",
                "D": "Access Point pada kanal 3 akan mendapatkan jangkauan dua kali lebih jauh."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Lebar spektrum 802.11b/g/n adalah 20–22 MHz; kanal 3 berpusat di 2422 MHz sehingga sayap frekuensinya merusak dan menginterferensi kanal 1 (2412 MHz) dan kanal 6 (2437 MHz) secara simultan.",
                "2": "Pita 2.4 GHz memiliki 14 kanal yang seluruhnya tidak saling bertumpuk.",
                "3": "Kanal 3 hanya boleh digunakan jika seluruh ruangan dipasangi peredam suara busa."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_TE_05",
            "phase": "HYPOTHESIS_TESTING_EVALUATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Pada switch manageable Cisco, log konsol menampilkan pesan berkala: 'LINK-3-UPDOWN: Interface GigabitEthernet0/5, changed state to down / changed state to up' (port flapping) setiap beberapa detik. Pengujian fisik langsung yang paling tepat untuk memverifikasi penyebabnya adalah...",
            "options": {
                "A": "Memeriksa kekencangan klip konektor RJ45 dan menguji pin kabel menggunakan cable tester.",
                "B": "Mengganti password enable pada konfigurasi privilege switch.",
                "C": "Menambah kapasitas RAM pada switch manageable.",
                "D": "Mengubah hostname switch dari CLI."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Port flapping intermiten sering dipicu oleh kontak fisik konektor RJ45 yang longgar, crimping pin tembaga tidak menancap sempurna, atau kabel tembaga yang retak di dekat boot konektor.",
                "2": "Karena port flapping adalah tanda switch sedang merayakan ulang tahun operasional.",
                "3": "Karena pesan UP/DOWN menandakan kabel jaringan berhasil mendeteksi koneksi satelit."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_TE_06",
            "phase": "HYPOTHESIS_TESTING_EVALUATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Seorang teknisi menguji throughput link nirkabel menggunakan tool iPerf. Hasil uji UDP throughput mencapai 85 Mbps dengan packet loss 0.2%. Namun saat diuji menggunakan TCP, throughput hanya mencapai 18 Mbps. Evaluasi kausal terhadap hasil pengujian ini adalah...",
            "options": {
                "A": "Kartu jaringan laptop tidak mendukung protokol TCP.",
                "B": "Terdapat fluktuasi latensi (jitter) atau paket drop minor yang memicu mekanisme congestion control TCP (sliding window collapse) memperkecil laju pengiriman.",
                "C": "Protokol UDP selalu empat kali lebih aman daripada protokol TCP.",
                "D": "Access Point secara otomatis memblokir seluruh paket data TCP yang lewat."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "TCP mensyaratkan konfirmasi ACK; adanya delay atau drop acak pada media nirkabel diartikan sebagai kongesti jaringan, memicu algoritma penanganan TCP memotong ukuran jendela transmisi.",
                "2": "Karena protokol UDP tidak menggunakan frekuensi gelombang radio dalam perambatannya.",
                "3": "Throughput TCP dan UDP tidak memiliki perbedaan dalam implementasi jaringan nyata."
            },
            "correct_reasoning": "1"
        },

        # --- FASE 5: CORRECTIVE_ACTION_VERIFICATION (A25 - A30) ---
        {
            "id": "TB_A_CA_01",
            "phase": "CORRECTIVE_ACTION_VERIFICATION",
            "curriculum_element": "TP 2.1 - Instalasi Jaringan Nirkabel",
            "prompt": "Pada pita frekuensi 2.4 GHz standar Indonesia/ETSI (kanal 1 hingga 13), teknisi ditugaskan menata frekuensi untuk 3 Access Point di satu gedung agar bebas interferensi. Berapa banyakkah pola kombinasi 3 kanal non-overlapping independen yang dapat dipilih?",
            "options": {
                "A": "Hanya 1 kombinasi standar utama (kanal 1, 6, dan 11).",
                "B": "Terdapat setidaknya 3 susunan kombinasi non-overlapping independen (misal: 1-6-11, 2-7-12, atau 3-8-13).",
                "C": "Terdapat 13 kombinasi karena setiap kanal bebas dipasangkan tanpa syarat.",
                "D": "Tidak ada kombinasi yang memungkinkan karena pita 2.4 GHz seluruhnya saling bertumpuk."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Syarat non-overlapping membutuhkan jarak pisah frekuensi minimal 25 MHz (selisih 5 nomor kanal), sehingga pola triplet (k, k+5, k+10) dapat dibentuk untuk k=1, 2, dan 3.",
                "2": "Perangkat keras Access Point pabrikan hanya dapat diprogram pada kanal bernomor ganjil saja.",
                "3": "Seluruh kanal pada 2.4 GHz dapat digunakan bersamaan tanpa interferensi asalkan SSID berbeda."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_CA_02",
            "phase": "CORRECTIVE_ACTION_VERIFICATION",
            "curriculum_element": "TP 2.1 - Instalasi Jaringan Nirkabel",
            "prompt": "Sebuah lab TKJ memiliki alokasi blok IP 192.168.10.0/24. Teknisi diminta membagi jaringan menjadi 4 subnet mandiri yang masing-masing mampu menampung 50 komputer siswa. Tindakan korektif alokasi subnet mask yang paling efisien dan tepat adalah...",
            "options": {
                "A": "Menggunakan prefix /25 (255.255.255.128) menghasilkan 2 subnet.",
                "B": "Menggunakan prefix /26 (255.255.255.192) menghasilkan 4 subnet dengan 62 host valid per subnet.",
                "C": "Menggunakan prefix /27 (255.255.255.224) menghasilkan 8 subnet dengan 30 host valid per subnet.",
                "D": "Menggunakan prefix /28 (255.255.255.240) menghasilkan 16 subnet dengan 14 host valid per subnet."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Prefix /26 meminjam 2 bit host (2^2 = 4 subnet) dan menyisakan 6 bit host (2^6 - 2 = 62 host), sangat mencukupi kebutuhan 50 PC tanpa pemborosan alamat IP.",
                "2": "Prefix /27 dipilih karena 30 host lebih mudah dikelola daripada 62 host.",
                "3": "Subnet mask tidak berpengaruh terhadap kapasitas tampung jumlah komputer di lab."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_CA_03",
            "phase": "CORRECTIVE_ACTION_VERIFICATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Kabel UTP yang menghubungkan PC klien ke switch menunjukkan lampu indikator LAN tester nomor 1, 2, 3, dan 6 menyala hijau berurutan, namun lampu 4, 5, 7, dan 8 mati total. Tindakan perbaikan yang harus diambil adalah...",
            "options": {
                "A": "Memotong kedua ujung konektor RJ45 dan melakukan crimping ulang sesuai standar EIA/TIA-568B dengan memastikan seluruh 8 kawat tembaga tertekan pin pisau konektor.",
                "B": "Membiarkan kabel karena jaringan Ethernet 100BASE-TX hanya membutuhkan pin 1, 2, 3, dan 6 untuk beroperasi normal.",
                "C": "Mengganti kartu jaringan komputer klien dengan kartu nirkabel.",
                "D": "Menyolder ujung konektor RJ45 ke port motherboard komputer."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Meskipun 10/100 Mbps hanya menggunakan pin 1,2,3,6, kabel 8-pin standar wajib terhubung sempurna untuk menjamin kompatibilitas Gigabit Ethernet (1000BASE-T) dan PoE.",
                "2": "Karena kabel UTP standar hanya boleh memiliki 4 helai tembaga di dalamnya.",
                "3": "Pin 4, 5, 7, dan 8 hanya digunakan untuk menyalurkan sinyal audio radio FM."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_CA_04",
            "phase": "CORRECTIVE_ACTION_VERIFICATION",
            "curriculum_element": "TP 2.1 - Instalasi Jaringan Nirkabel",
            "prompt": "Access Point di lab komputer mengalami interferensi ko-kanal parah karena AP lab sebelah juga menggunakan kanal 6 pada pita 2.4 GHz. Tindakan korektif konfigurasi nirkabel yang paling permanen dan efektif adalah...",
            "options": {
                "A": "Mengubah frekuensi salah satu AP ke kanal 1 atau 11 yang kosong, atau mengalihkan klien ke pita 5 GHz.",
                "B": "Menaikkan daya pancar (Tx power) kedua AP ke tingkat maksimum 1000 mW.",
                "C": "Menyembunyikan SSID (hide SSID) pada kedua Access Point.",
                "D": "Mengganti antena kedua AP dengan antena kabel tembaga tipis."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Memindahkan frekuensi ke kanal non-overlapping (1, 6, atau 11) atau migrasi ke pita 5 GHz yang memiliki lebih banyak kanal independen mengeliminasi interferensi ko-kanal dan tabrakan CSMA/CA.",
                "2": "Menaikkan daya pancar pemancar justru memperluas area interferensi dan memperparah tabrakan paket data.",
                "3": "Hide SSID hanya menyembunyikan siaran nama jaringan beacon frame, namun transmisi radio tetap bertabrakan di udara."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_CA_05",
            "phase": "CORRECTIVE_ACTION_VERIFICATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Hasil pengukuran titik sambungan serat optik menunjukkan redaman sambungan (splice loss) sebesar 3.2 dB (batas wajar standar telko < 0.1 dB). Tindakan perbaikan yang wajib dilakukan teknisi di lapangan adalah...",
            "options": {
                "A": "Membersihkan pelindung luar kabel dengan alkohol tanpa membuka sambungan.",
                "B": "Memotong sleeve pelindung, mengupas ulang serat kaca, memotong dengan fiber cleaver presisi, dan melakukan fusion splicing ulang.",
                "C": "Mengelem kedua ujung serat optik menggunakan lem tembak plastik.",
                "D": "Menambah penguat sinyal elektrik di titik sambungan kabel."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Redaman tinggi pada sambungan peleburan menandakan sudut potongan serat miring (bad cleave), gelembung udara, atau kotoran di inti; penyambungan ulang (re-splicing) adalah satu-satunya solusi standar.",
                "2": "Lem tembak plastik dapat menggantikan fungsi elektroda busur api mesin fusion splicer.",
                "3": "Kabel serat optik single-mode dapat mentransmisikan data normal meskipun redaman mencapai 50 dB per sambungan."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_CA_06",
            "phase": "CORRECTIVE_ACTION_VERIFICATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Setelah mengganti kartu Wi-Fi pada laptop yang bermasalah, langkah verifikasi akhir yang wajib dilakukan teknisi untuk membuktikan bahwa masalah jaringan telah terselesaikan secara tuntas adalah...",
            "options": {
                "A": "Menutup laptop dan langsung menyerahkannya ke guru tanpa pengujian.",
                "B": "Melakukan asosiasi ke SSID target, memeriksa perolehan IP via DHCP, melakukan uji ping gateway & internet kontinu (0% loss), serta menguji transfer data.",
                "C": "Cukup melihat apakah lampu indikator laptop menyala saat ditekan tombol power.",
                "D": "Memformat ulang harddisk laptop ke pengaturan pabrik."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Verifikasi komprehensif menguji keberhasilan seluruh lapisan jaringan: L1/L2 (asosiasi Wi-Fi), L3 (pengalamatan IP & ping), dan L7 (transfer aplikasi nyata) tanpa packet loss.",
                "2": "Karena pengujian ping tidak dapat membuktikan apakah kabel dan kartu jaringan berfungsi normal.",
                "3": "Langkah verifikasi hanya diperlukan jika perangkat yang diperbaiki adalah komputer mainframe bank."
            },
            "correct_reasoning": "1"
        },

        # --- NON-EQUIVALENT DEPENDENT VARIABLE (NEDV - KONTROL) (A31 - A36) ---
        {
            "id": "TB_A_NEDV_01",
            "phase": "NEDV_CONTROL",
            "curriculum_element": "TP 2.3 - Layanan Voice over IP",
            "prompt": "Dalam arsitektur komunikasi Voice over IP (VoIP), protokol yang bertugas menangani pembentukan panggilan (call setup), negosiasi parameter sesi, dan pemutusan hubungan panggilan telepon adalah...",
            "options": {
                "A": "Session Initiation Protocol (SIP)",
                "B": "Real-time Transport Protocol (RTP)",
                "C": "Dynamic Host Configuration Protocol (DHCP)",
                "D": "Simple Network Management Protocol (SNMP)"
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "SIP adalah protokol pensinyalan (signaling) layer aplikasi yang bertugas menginisiasi, memodifikasi, dan mengakhiri sesi komunikasi multimedia, sedangkan transmisi media audio riil ditangani oleh RTP.",
                "2": "SIP bertugas mengonversi suara analog manusia menjadi pulsa tegangan listrik AC.",
                "3": "DHCP dan SNMP adalah protokol utama yang memproses transmisi audio suara telepon secara langsung."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_NEDV_02",
            "phase": "NEDV_CONTROL",
            "curriculum_element": "TP 2.3 - Layanan Voice over IP",
            "prompt": "Sebuah kantor cabang memiliki kapasitas bandwidth internet yang terbatas (hanya 128 kbps) namun harus melayani 10 panggilan suara VoIP simultan. Codec kompresi audio manakah yang paling efisien menghemat bandwidth dengan bitrate sekitar 8 kbps per kanal?",
            "options": {
                "A": "G.711u (PCM 64 kbps)",
                "B": "G.729 (CS-ACELP 8 kbps)",
                "C": "G.711a (PCM 64 kbps)",
                "D": "Linear PCM Uncompressed (128 kbps)"
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Codec G.729 menggunakan algoritma kompresi CS-ACELP yang mampu mereduksi bitrate suara hingga 8 kbps per panggilan, sehingga 10 panggilan hanya membutuhkan ~80 kbps bandwidth.",
                "2": "Codec G.711 menghasilkan penghematan bandwidth sepuluh kali lebih tinggi dibanding G.729.",
                "3": "Kompresi audio pada VoIP tidak berpengaruh terhadap kebutuhan kapasitas bandwidth saluran internet."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_NEDV_03",
            "phase": "NEDV_CONTROL",
            "curriculum_element": "TP 2.4 - Instalasi Fiber Optik",
            "prompt": "Untuk instalasi transmisi data antarkampus dengan jarak jangkauan lebih dari 20 kilometer tanpa repeater optik, jenis kabel fiber optik yang paling tepat digunakan adalah...",
            "options": {
                "A": "Multi-Mode Fiber (MMF) OM1 dengan diameter inti 62.5 mikrometer.",
                "B": "Multi-Mode Fiber (MMF) OM3 dengan diameter inti 50 mikrometer.",
                "C": "Single-Mode Fiber (SMF) OS2 dengan diameter inti sekitar 9 mikrometer.",
                "D": "Kabel serat plastik (Plastic Optical Fiber) diameter 1 milimeter."
            },
            "correct_option": "C",
            "reasoning_options": {
                "1": "Single-Mode Fiber memiliki ukuran core yang sangat kecil (±9 um) sehingga cahaya merambat hanya melalui satu mode lurus, menghilangkan dispersi modal (modal dispersion) dan memungkinkan jangkauan hingga puluhan kilometer.",
                "2": "Multi-Mode Fiber memiliki inti lebih besar sehingga cahaya dapat melompat lebih cepat dan menjangkau jarak ratusan kilometer.",
                "3": "Kabel serat plastik POF dirancang khusus untuk kabel bawah laut antarpulau."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_NEDV_04",
            "phase": "NEDV_CONTROL",
            "curriculum_element": "TP 2.4 - Instalasi Fiber Optik",
            "prompt": "Prinsip dasar fisika optik yang memungkinkan pulsa cahaya merambat di dalam inti kabel serat optik sejauh puluhan kilometer tanpa bocor keluar ke lapisan selubung adalah...",
            "options": {
                "A": "Pembiasan ganda (birefringence) pada lapisan pelindung baja.",
                "B": "Pemantulan internal total (Total Internal Reflection) karena indeks bias core lebih besar dari indeks bias cladding.",
                "C": "Efek fotolistrik yang mengubah cahaya laser menjadi gelombang elektromagnetik radio.",
                "D": "Penyerapan foton secara sempurna oleh lapisan cladding berwarna hitam."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Total Internal Reflection terjadi jika cahaya merambat dari medium lebih rapat (core, n1) menuju medium kurang rapat (cladding, n2) dengan sudut datang melampaui sudut kritis pantulan.",
                "2": "Cahaya merambat di dalam serat optik karena ditarik oleh medan gravitasi bumi.",
                "3": "Lapisan cladding serat optik terbuat dari cermin perak yang memantulkan seluruh jenis radiasi panas."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_NEDV_05",
            "phase": "NEDV_CONTROL",
            "curriculum_element": "TP 2.5 - Perbaikan Fiber Optik",
            "prompt": "Sebelum dua ujung serat optik disambungkan menggunakan mesin pelebur fusion splicer, teknisi wajib memotong ujung serat menggunakan alat khusus bernama Fiber Cleaver. Mengapa proses pemotongan ini tidak boleh menggunakan gunting atau tang potong biasa?",
            "options": {
                "A": "Karena tang potong biasa akan merusak lapisan cat luar kabel saja.",
                "B": "Fiber Cleaver menghasilkan penampang potongan kaca yang tegak lurus sempurna (sudut potong < 1 derajat) dan rata tanpa gerigi micro-crack.",
                "C": "Karena mata pisau Fiber Cleaver dialiri arus listrik pemanas 500 derajat Celcius.",
                "D": "Penggunaan tang potong dilarang hanya karena alasan keamanan bahaya terkena serpihan kaca."
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "Mesin fusion splicer mensyaratkan sudut kemiringan ujung serat kaca mendekati 90 derajat sempurna; potongan tidak rata memicu redaman sambungan (splice loss) tinggi atau kegagalan fusi busur elektroda.",
                "2": "Gunting biasa membuat serat optik berubah menjadi kabel tembaga.",
                "3": "Fiber Cleaver berfungsi merekatkan konektor SC secara instan tanpa perlu lem perekat."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_NEDV_06",
            "phase": "NEDV_CONTROL",
            "curriculum_element": "TP 2.5 - Perbaikan Fiber Optik",
            "prompt": "Alat ukur canggih pada jaringan serat optik yang mampu menampilkan grafik jarak terhadap tingkat redaman, serta melokalisir secara presisi letak titik putus kabel (fiber break) atau tekukan tajam adalah...",
            "options": {
                "A": "Visual Fault Locator (VFL / Laser Pen Senter)",
                "B": "Optical Time-Domain Reflectometer (OTDR)",
                "C": "Optical Power Meter (OPM)",
                "D": "Digital Multimeter Clamp Ampere"
            },
            "correct_option": "B",
            "reasoning_options": {
                "1": "OTDR menginjeksikan pulsa cahaya dan menganalisis pantulan hamburan balik (Rayleigh backscattering dan Fresnel reflection) berdasarkan jeda waktu tempuh untuk memetakan kondisi fisik serat sepanjang jarak kabel.",
                "2": "OPM menampilkan peta grafik titik patahan kabel optik secara tiga dimensi.",
                "3": "VFL adalah perangkat komputer yang mampu memperbaiki kabel optik secara nirkabel dari jarak jauh."
            },
            "correct_reasoning": "1"
        }
    ]

    # FORM B (ISOMORPHIC PARALLEL FORM) - Setara secara psikometri, indikator, dan tingkat kesulitan
    form_b_items = [
        # --- FASE 1: SYMPTOM_RECOGNITION (B01 - B06) ---
        {
            "id": "TB_B_SR_01",
            "phase": "SYMPTOM_RECOGNITION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Access Point outdoor dihubungkan ke switch PoE melalui kabel UTP Cat5e sepanjang 130 meter. Perangkat AP sama sekali tidak menyala dan lampu port PoE pada switch berkedip cepat (fault status). Gejala fisik ini mengindikasikan bahwa...",
            "options": {
                "A": "Terjadi penurunan tegangan listrik (voltage drop) dan resistansi kabel berlebih pada Layer 1 fisik.",
                "B": "Access Point mengalami kegagalan proses booting sistem operasi Linux internal.",
                "C": "Server RADIUS sekolah menolak sertifikat keamanan perangkat AP.",
                "D": "Kabel UTP yang digunakan menggunakan susunan warna crossover T568A."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Standar PoE (IEEE 802.3af/at) mensyaratkan batas panjang kabel tembaga maksimal 100 meter; bentangan 130m memicu voltage drop drastis sehingga daya DC tidak mencukupi untuk menyalakan sirkuit AP.",
                "2": "Port PoE switch akan memutus daya jika nama SSID Access Point mengandung spasi.",
                "3": "Kabel UTP tidak dapat menghantarkan arus listrik DC pada suhu udara di atas 25 derajat Celcius."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_SR_02",
            "phase": "SYMPTOM_RECOGNITION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Saat menguji koneksi ke server dari terminal command prompt, muncul pesan balasan berulang: 'TTL Expired in Transit'. Gejala pesan ICMP ini secara spesifik menandakan bahwa...",
            "options": {
                "A": "Paket data berputar tanpa henti (routing loop) antar-router hingga nilai Time-To-Live habis menjadi nol.",
                "B": "Server tujuan sedang mengalami restart sistem operasi.",
                "C": "Kabel patch cord pada switch klien mengalami korsleting arus pendek.",
                "D": "Kecepatan internet provider sedang mengalami penurunan drastis."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Setiap router yang meneruskan paket mendikremen nilai header TTL sebesar 1; jika terjadi loop konfigurasi tabel rute, TTL akan menyentuh 0 dan router membuang paket sambil mengirim ICMP Type 11.",
                "2": "Pesan TTL Expired menandakan bahwa waktu sewa IP address DHCP telah kedaluwarsa.",
                "3": "Pesan ini selalu muncul jika kartu Wi-Fi laptop tidak memiliki antena internal."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_SR_03",
            "phase": "SYMPTOM_RECOGNITION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Seorang teknisi melakukan ping dari komputer klien ber-IP 192.168.1.50 ke server 10.0.0.1 tanpa mengisi konfigurasi Default Gateway. Terminal langsung merespons dengan pesan 'Network Unreachable'. Gejala ini menunjukkan bahwa...",
            "options": {
                "A": "Komputer pengirim tidak memiliki entri rute logis untuk meneruskan paket di luar subnet lokalnya.",
                "B": "Server tujuan mematikan fitur penerimaan paket data dari jaringan lokal.",
                "C": "Kabel serat optik ISP terputus oleh ekskavator proyek jalan.",
                "D": "Switch hub di laboratorium mengalami tabrakan frame CSMA/CD."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Jika IP tujuan berada di luar segmen jaringan lokal dan tidak ada Default Gateway yang ditentukan pada tabel routing lokal, stack TCP/IP lokal seketika menolak mengirim paket.",
                "2": "Pesan Network Unreachable adalah indikasi bahwa kartu jaringan komputer telah terbakar fisiknya.",
                "3": "Pesan ini menandakan bahwa nama domain server belum didaftarkan di DNS server."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_SR_04",
            "phase": "SYMPTOM_RECOGNITION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Aplikasi Wi-Fi analyzer pada laptop siswa menunjukkan kekuatan sinyal kuat (-58 dBm), namun throughput sangat rendah dan paket loss mencapai 25%. Di layar tertera nilai Signal-to-Noise Ratio (SNR) hanya 6 dB. Gejala ini mengindikasikan bahwa...",
            "options": {
                "A": "Sinyal pemancar mengalami gangguan noise lantai (noise floor) yang sangat tinggi di lingkungan sekitar.",
                "B": "Laptop siswa kehabisan kuota data internet bulanan.",
                "C": "Access Point beroperasi pada mode hemat daya malam hari.",
                "D": "Frekuensi Wi-Fi berubah otomatis menjadi frekuensi radio FM komersial."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Meskipun sinyal (RSSI) kuat (-58 dBm), jika derau (noise floor) tinggi (-64 dBm), maka SNR menjadi sangat kecil (6 dB), memicu modulasi turun ke MCS rendah dan bit error rate meningkat tajam.",
                "2": "Nilai SNR yang semakin kecil selalu menjamin koneksi internet semakin stabil dan cepat.",
                "3": "Noise floor Wi-Fi hanya dipengaruhi oleh suara bising manusia di dalam ruangan lab."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_SR_05",
            "phase": "SYMPTOM_RECOGNITION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Dua siswa TKJ menghubungkan laptop secara nirkabel mode Ad-Hoc. Tiba-tiba di layar muncul notifikasi sistem operasi: 'Windows has detected an IP address conflict'. Gejala ini secara spesifik menandakan bahwa...",
            "options": {
                "A": "Kedua laptop dikonfigurasi dengan alamat IP statis yang sama persis pada segmen jaringan yang sama.",
                "B": "Kabel UTP yang digunakan tertekuk melebihi batas kelengkungan kabel.",
                "C": "Kartu jaringan nirkabel pada salah satu laptop tidak memiliki alamat MAC fisik.",
                "D": "Nama Workgroup komputer pada kedua laptop belum disamakan."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Sistem operasi mendeteksi konflik melalui paket Gratuitous ARP; jika ada respons dari IP yang sama, OS langsung menonaktifkan konfigurasi IP ganda tersebut untuk mencegah disorientasi paket.",
                "2": "Konflik IP hanya terjadi jika ada virus komputer yang menghapus file registry kartu jaringan.",
                "3": "Konflik IP adalah tanda bahwa sinyal Wi-Fi kedua laptop memiliki password WPA2 berbeda."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_SR_06",
            "phase": "SYMPTOM_RECOGNITION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Pada Access Point terbaru dengan keamanan WPA3-Personal (SAE), sebuah laptop lawas gagal terhubung sama sekali dan selalu kembali ke status 'Disconnected' tanpa meminta kata sandi. Gejala ini paling tepat menunjukkan bahwa...",
            "options": {
                "A": "Hardware kartu jaringan atau driver laptop lawas tidak mendukung protokol autentikasi Simultaneous Authentication of Equals (SAE).",
                "B": "Access Point mengalami kerusakan antena transmisi pada polarisasi vertikal.",
                "C": "Kabel UTP uplink ke router menggunakan pinout T568A.",
                "D": "Daya listrik laptop lawas tidak mencukupi untuk memancarkan sinyal WPA3."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "WPA3 mensyaratkan dukungan cipher PMF (Protected Management Frames) dan algoritma kriptografi SAE; perangkat warisan (legacy) yang hanya mendukung WPA2-PSK tidak dapat memproses frame asosiasi WPA3 murni.",
                "2": "Access Point WPA3 hanya dapat terhubung ke perangkat yang memiliki sistem operasi buatan tahun 2026 ke atas.",
                "3": "Karena protokol WPA3 mengharuskan pengguna melakukan scan sidik jari pada laptop."
            },
            "correct_reasoning": "1"
        },

        # --- FASE 2: PROBLEM_SPACE_CONSTRUCTION (B07 - B12) ---
        {
            "id": "TB_B_PC_01",
            "phase": "PROBLEM_SPACE_CONSTRUCTION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Seorang teknisi ingin meneliti perbandingan jangkauan sinyal Wi-Fi antara frekuensi 2.4 GHz dan frekuensi 5 GHz di lorong sekolah terbuka. Agar pengujian adil dan valid secara ilmiah, variabel manakah yang wajib dikendalikan konstan?",
            "options": {
                "A": "Daya pancar pemancar (Tx Power), lokasi letak AP, ketinggian tiang, dan perangkat penerima yang digunakan.",
                "B": "Panjang gelombang radio dan frekuensi osilator kristal Access Point.",
                "C": "Kondisi cuaca dan jumlah siswa yang lalu-lalang di lorong secara bebas.",
                "D": "Merek smartphone yang berganti-ganti di setiap titik pengukuran."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Untuk mengisolasi pengaruh frekuensi sebagai variabel bebas, semua faktor lain yang memengaruhi kuat sinyal (daya Tx, tinggi antena, sensitivitas Rx klien, dan geometri lokasi) wajib dijaga tetap.",
                "2": "Frekuensi 2.4 GHz dan 5 GHz harus diuji dengan daya pancar yang berbeda sepuluh kali lipat.",
                "3": "Variabel lingkungan tidak perlu dikontrol karena gelombang radio kebal terhadap kondisi fisik."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_PC_02",
            "phase": "PROBLEM_SPACE_CONSTRUCTION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Dalam eksperimen untuk menguji ketahanan kabel terhadap induksi medan elektromagnetik (EMI) dari mesin dinamo di bengkel TKJ, variabel manipulasi (variabel bebas) yang harus diubah oleh siswa adalah...",
            "options": {
                "A": "Jenis pelindung kabel (kabel UTP unshielded vs kabel STP/FTP berpelindung aluminium foil).",
                "B": "Jarak bentangan kabel dari motor dinamo.",
                "C": "Tegangan listrik motor dinamo.",
                "D": "Sistem operasi komputer yang melakukan ping."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Tujuan pengujian adalah mengevaluasi efektivitas pelindung kabel terhadap derau listrik, maka jenis kabel (UTP vs STP) adalah satu-satunya variabel yang dimanipulasi pada jarak dan medan EMI yang sama.",
                "2": "Karena kabel UTP selalu kebal terhadap medan magnet dinamo tanpa memerlukan pelindung.",
                "3": "Untuk menguji kabel, tegangan listrik PLN harus dimatikan secara total selama pengujian."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_PC_03",
            "phase": "PROBLEM_SPACE_CONSTRUCTION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Sebuah komputer di lab TKJ tidak dapat mencetak dokumen ke printer jaringan. Untuk mengisolasi ruang masalah sebelum membongkar hardware printer, langkah penelusuran awal yang paling sistematis adalah...",
            "options": {
                "A": "Melakukan uji ping ke IP address printer jaringan dari komputer klien untuk memverifikasi ketercapaian layer 3.",
                "B": "Membongkar cartridge tinta dan roller kertas printer.",
                "C": "Menghubungi teknisi servis printer resmi untuk klaim garansi.",
                "D": "Mengganti kabel listrik PLN yang memberi daya pada printer."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Uji ping memvalidasi konektivitas logis jaringan; jika ping berhasil (0% loss), masalah terisolasi pada driver atau port antrean spooler printer, bukan pada kabel jaringan.",
                "2": "Karena kegagalan mencetak selalu disebabkan oleh kerusakan mekanis motor printer.",
                "3": "Printer jaringan tidak menggunakan protokol IP dalam pengiriman data dokumen."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_PC_04",
            "phase": "PROBLEM_SPACE_CONSTRUCTION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Link transmisi serat optik antar-gedung tiba-tiba terputus. Sebelum teknisi memutuskan untuk menggali pipa saluran kabel di tanah, langkah isolasi subsistem terdekat yang paling logis adalah...",
            "options": {
                "A": "Memeriksa status transceiver SFP pada switch dan membersihkan ujung konektor patch cord di rak server OTB.",
                "B": "Langsung menyewa alat berat untuk membongkar aspal jalur pipa kabel.",
                "C": "Mengganti switch hub dengan switch unmanaged.",
                "D": "Mematikan aliran listrik AC di seluruh gedung sekolah."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Sebagian besar gangguan serat optik terjadi di titik terminasi (konektor kotor, patch cord tertekuk, atau modul optik SFP rusak); memeriksa komponen yang mudah diakses menghemat waktu dan biaya.",
                "2": "Konektor serat optik tidak pernah kotor karena berada di dalam ruangan tertutup.",
                "3": "Modul SFP otomatis memperbaiki kabel optik yang putus di dalam tanah."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_PC_05",
            "phase": "PROBLEM_SPACE_CONSTRUCTION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Semua komputer di laboratorium TKJ dapat mengakses server lokal sekolah dengan sangat cepat, namun seluruhnya gagal membuka situs web di internet. Bagaimana teknisi membatasi ruang masalah?",
            "options": {
                "A": "Masalah terisolasi pada router gateway penghubung ke ISP atau link modem eksternal, bukan pada switch atau kabel lokal lab.",
                "B": "Masalah terjadi karena seluruh kartu jaringan di komputer lab rusak secara serentak.",
                "C": "Masalah terletak pada kabel UTP yang menghubungkan komputer siswa ke meja praktikum.",
                "D": "Masalah terjadi karena server lokal menyerap seluruh kuota internet secara diam-diam."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Karena komunikasi internal (LAN) berjalan lancar, infrastruktur lokal Layer 1/2/3 terbukti normal; kegagalan terpusat pada jalur transmisi WAN (uplink modem, routing NAT gateway, atau DNS publik).",
                "2": "Koneksi LAN dan koneksi internet selalu menggunakan sirkuit perangkat keras yang terpisah pada PC.",
                "3": "Router gateway tidak memiliki peran dalam meneruskan paket data ke jaringan internet."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_PC_06",
            "phase": "PROBLEM_SPACE_CONSTRUCTION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Pada instalasi antena Wi-Fi Point-to-Point (PtP) jarak 2 km, koneksi sering putus saat angin kencang bertiup kencang di sore hari. Untuk mengisolasi variabel penyebab gangguan, teknisi harus menguji apakah...",
            "options": {
                "A": "Tiang antena mengalami goyangan fisik sehingga titik fokus beamforming antena parabola bergeser keluar dari alignment.",
                "B": "Angin kencang meniup gelombang radio hingga berbelok ke arah berlawanan.",
                "C": "Suhu udara sore hari membuat frekuensi radio 5 GHz membeku di udara.",
                "D": "Kabel UTP di dalam tiang tertiup angin sehingga data terlempar keluar."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Antena directional gain tinggi memiliki sudut pancar (beamwidth) yang sangat sempit (3-5 derajat); defleksi tiang akibat angin menggeser line-of-sight antena dan memicu drop sinyal drastis.",
                "2": "Gelombang elektromagnetik dapat tertiup angin jika kecepatan angin melebihi 20 km/jam.",
                "3": "Antena PtP harus dipasang bebas tanpa pengunci tiang agar dapat mengikuti arah angin."
            },
            "correct_reasoning": "1"
        },

        # --- FASE 3: FAULT_HYPOTHESIS_GENERATION (B13 - B18) ---
        {
            "id": "TB_B_FH_01",
            "phase": "FAULT_HYPOTHESIS_GENERATION",
            "curriculum_element": "TP 2.1 - Instalasi Jaringan Nirkabel",
            "prompt": "Sebuah Access Point standar Wi-Fi 6 mengaktifkan teknologi Multiple-Input Multiple-Output (MIMO) spasial. Jika sistem ditingkatkan dari konfigurasi 2x2 MIMO menjadi 4x4 MIMO pada lebar kanal dan modulasi MCS yang sama, bagaimanakah estimasi kapasitas throughput teoritisnya?",
            "options": {
                "A": "Meningkat menjadi dua kali lipat secara proporsional.",
                "B": "Tetap sama karena jumlah frekuensi radio tidak bertambah.",
                "C": "Menurun menjadi setengahnya karena antena saling bertabrakan.",
                "D": "Meningkat enam belas kali lipat secara eksponensial."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Kapasitas multiplexing spasial berbanding lurus dengan jumlah aliran data independen (spatial streams); menggandakan antena stream dari 2 menjadi 4 melipatgandakan data rate teoritis.",
                "2": "Antena MIMO hanya berfungsi memperluas jangkauan jarak, bukan meningkatkan throughput data.",
                "3": "Penambahan antena selalu menurunkan performa kecepatan pada teknologi nirkabel."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_FH_02",
            "phase": "FAULT_HYPOTHESIS_GENERATION",
            "curriculum_element": "TP 2.1 - Instalasi Jaringan Nirkabel",
            "prompt": "Sesuai hukum pelemahan ruang bebas (Free Space Path Loss), jika jarak antara smartphone siswa ke Access Point bertambah dari 3 meter menjadi 9 meter (3 kali lipat lebih jauh), bagaimanakah kerapatan daya sinyal yang diterima antena smartphone?",
            "options": {
                "A": "Berkurang menjadi 1/9 (sepersembilan) dari daya awal.",
                "B": "Berkurang menjadi 1/3 (sepertiga) dari daya awal.",
                "C": "Berkurang menjadi 1/6 (seperenam) dari daya awal.",
                "D": "Tetap sama karena smartphone memiliki fitur penguat sinyal otomatis."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Berdasarkan prinsip hukum kuadrat terbalik (1/r^2), pertambahan jarak sebesar 3 kali lipat (r -> 3r) mengakibatkan pelemahan kerapatan daya sinyal menjadi 1/(3^2) = 1/9 dari nilai semula.",
                "2": "Pelemahan sinyal selalu proporsional linier 1/r terhadap pertambahan jarak.",
                "3": "Daya sinyal radio di udara bebas meningkat seiring bertambahnya jarak transmisi."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_A_FH_03",
            "phase": "FAULT_HYPOTHESIS_GENERATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Dua serat optik disambung dengan mesin fusion splicer, namun hasil uji OPM menunjukkan redaman abnormal sebesar 2.8 dB. Di layar mikroskop splicer terlihat sambungan memiliki gelembung udara dan garis hitam melintang. Hipotesis penyebab kerusakan fisik ini adalah...",
            "options": {
                "A": "Hasil pemotongan serat kaca miring (cleave angle buruk) atau permukaan kaca kotor saat dilebur oleh elektroda.",
                "B": "Daya laser OPM terlalu kuat sehingga membakar inti kaca.",
                "C": "Kabel serat optik dipasang terbalik antara pengirim dan penerima.",
                "D": "Suhu ruangan terlalu dingin sehingga kaca serat optik membeku."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Garis hitam dan gelembung fusi disebabkan oleh kontaminasi debu atau sudut potongan cleaver > 1 derajat, menyebabkan ketidaksempurnaan rekatan kaca dan hamburan cahaya besar.",
                "2": "Kabel serat optik single-mode harus disambung menggunakan lem alteco agar bebas gelembung.",
                "3": "Sambungan serat optik normal memang selalu memiliki garis hitam pekat di titik sambungan."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_FH_04",
            "phase": "FAULT_HYPOTHESIS_GENERATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Seorang siswa mengupas lilitan kabel UTP sepanjang 6 cm dari ujung konektor RJ45 saat melakukan crimping. Saat kabel dihubungkan pada switch Gigabit, jaringan mengalami bit error rate sangat tinggi dan koneksi sering terputus. Hipotesis kausal yang tepat adalah...",
            "options": {
                "A": "Membuka lilitan kabel terlalu panjang menghilangkan efek pembatalan induksi elektromagnetik antar-pasangan, memicu Near-End Crosstalk (NEXT) parah.",
                "B": "Kabel tembaga kehilangan kelenturan fisik jika lilitannya dilepas.",
                "C": "Konektor RJ45 tidak dapat mengalirkan data jika kabel tidak dipilin di dalam pin.",
                "D": "Panjang kabel 6 cm menyebabkan daya listrik DC bocor keluar jaket kabel."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Prinsip kabel twisted pair mengandalkan lilitan berlawanan fase untuk membatalkan interferensi derau antar-kawat; membuka pilinan > 1.3 cm (0.5 inci) merusak keseimbangan impedansi dan memicu crosstalk.",
                "2": "Lilitan kabel tembaga hanya berfungsi estetika agar kabel terlihat rapi di dalam pipa.",
                "3": "Kabel UTP kategori 6 harus diluruskan tanpa lilitan sama sekali agar kecepatan mencapai 10 Gbps."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_FH_05",
            "phase": "FAULT_HYPOTHESIS_GENERATION",
            "curriculum_element": "TP 2.1 - Instalasi Jaringan Nirkabel",
            "prompt": "Di sebuah ruangan kelas yang dipadati 36 siswa pengguna smartphone, sinyal Wi-Fi 2.4 GHz terbaca penuh (4 bar), namun browsing terasa sangat lambat dan sering macet. Hipotesis kausal yang paling logis atas masalah ini adalah...",
            "options": {
                "A": "Terjadi kepadatan spektrum kanal (channel saturation) dan tabrakan frame CSMA/CA akibat terlalu banyak perangkat yang berebut satu media bersama.",
                "B": "Smartphone siswa secara otomatis mematikan antena jika bar sinyal terlalu penuh.",
                "C": "Pita frekuensi 2.4 GHz mengalami kelelahan frekuensi akibat dipakai terus menerus.",
                "D": "Sinyal 4 bar menunjukkan bahwa Access Point sedang kehabisan gelombang radio."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Kekuatan sinyal radio (RSSI) yang tinggi tidak menjamin ketersediaan bandwidth udara (airtime); pada kanal bersama yang padat, waktu tunggu transmisi (contention overhead) melonjak drastis.",
                "2": "Karena sinyal 4 bar menandakan daya transmisi AP terlalu kuat hingga merusak chip Wi-Fi smartphone.",
                "3": "Siswa di dalam ruangan harus mematikan Bluetooth agar gelombang 2.4 GHz tidak terhisap."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_FH_06",
            "phase": "FAULT_HYPOTHESIS_GENERATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Uji transfer file besar via FTP melalui jaringan kabel menunjukkan kecepatan anjlok dari 95 MB/s ke 2 MB/s saat nilai RTT ping melonjak dari 1 ms ke 120 ms akibat kabel UTP terhimpit pintu besi. Hipotesis relasi kausal yang tepat adalah...",
            "options": {
                "A": "Himpitan fisik merusak impedansi kabel tembaga, menyebabkan paket data rusak dan memicu retransmisi TCP secara masif yang meruntuhkan congestion window.",
                "B": "Kabel tembaga yang terhimpit menyempitkan jalur fisik elektron sehingga elektron mengantre berdesakan.",
                "C": "Pintu besi menyerap kode biner file FTP sehingga server harus mengirim ulang kode biner baru.",
                "D": "Protokol FTP otomatis membatasi kecepatan jika suhu pintu besi berada di bawah 20 derajat Celcius."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Deformasi fisik kabel tembaga mengubah nilai impedansi karakteristik (100 Ohm) yang memicu pantulan sinyal (return loss) dan frame check sequence (FCS) error, memaksa TCP melakukan retransmisi terus-menerus.",
                "2": "Kabel UTP memiliki cairan konduktor di dalamnya yang akan tersumbat jika kabel terhimpit pintu.",
                "3": "Protokol TCP tidak terpengaruh oleh kondisi fisik kabel tembaga di lapangan."
            },
            "correct_reasoning": "1"
        },

        # --- FASE 4: HYPOTHESIS_TESTING_EVALUATION (B19 - B24) ---
        {
            "id": "TB_B_TE_01",
            "phase": "HYPOTHESIS_TESTING_EVALUATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Pada sistem jaringan nirkabel kampus dengan banyak Access Point terpusat (WLAN Controller), parameter roaming disetel dengan margin histeresis 6 dB. Jika laptop siswa sedang terhubung ke AP-1 dengan RSSI -72 dBm, pada kekuatan sinyal berapakah dari AP-2 proses handover roaming baru akan dipicu?",
            "options": {
                "A": "Sinyal AP-2 harus mencapai minimal -66 dBm atau lebih kuat (selisih minimal 6 dB lebih baik).",
                "B": "Sinyal AP-2 cukup bernilai -71 dBm (selisih 1 dB lebih baik).",
                "C": "Sinyal AP-2 harus mencapai 0 dBm tepat.",
                "D": "Handover tidak akan pernah terjadi jika AP-1 masih memancarkan sinyal."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Margin histeresis mencegah efek ping-pong roaming; perangkat baru akan berpindah AP jika sinyal kandidat baru melampaui sinyal AP lama ditambah nilai ambang histeresis (-72 + 6 = -66 dBm).",
                "2": "Karena perangkat nirkabel selalu berpindah ke AP mana pun yang memiliki nomor MAC address lebih besar.",
                "3": "Margin histeresis adalah setelan untuk mengatur kecerahan layar laptop saat roaming."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_TE_02",
            "phase": "HYPOTHESIS_TESTING_EVALUATION",
            "curriculum_element": "TP 2.1 - Instalasi Jaringan Nirkabel",
            "prompt": "Dalam skenario uji di mana dua laptop klien terhalang oleh partisi lemari besi sehingga tidak saling mendengar (Hidden Node Problem), pengujian throughput menunjukkan peningkatan stabilitas saat fitur RTS/CTS diaktifkan pada Access Point. Evaluasi hasil uji ini menunjukkan bahwa...",
            "options": {
                "A": "Frame Request-to-Send / Clear-to-Send berhasil mereservasi media transmisi nirkabel dan mencegah tabrakan tabrakan data antar-klien tersembunyi.",
                "B": "RTS/CTS melipatgandakan daya pancar antena laptop melewati lemari besi.",
                "C": "Lemari besi menyerap frame RTS/CTS sehingga interferensi berhenti seketika.",
                "D": "Fitur RTS/CTS mengubah koneksi Wi-Fi menjadi koneksi kabel virtual."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Mekanisme handshake RTS/CTS memverifikasi bahwa medium nirkabel bebas sebelum data besar dikirim, secara efektif mengatasi inefisiensi tabrakan yang dipicu oleh node tersembunyi (hidden station).",
                "2": "RTS/CTS berfungsi mendinginkan suhu Access Point saat menangani banyak klien.",
                "3": "Frame RTS/CTS bekerja dengan cara mematikan koneksi salah satu laptop secara permanen."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_TE_03",
            "phase": "HYPOTHESIS_TESTING_EVALUATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Teknisi melakukan pengetesan kabel serat optik menggunakan OTDR. Pada layar grafik (trace), pada titik jarak 420 meter terlihat lonjakan pantulan Fresnel refleksi tajam diikuti garis grafik yang jatuh tegak lurus ke dasar (noise floor). Evaluasi hasil pengukuran ini membuktikan bahwa...",
            "options": {
                "A": "Kabel serat optik mengalami putus total (fiber break / open end) di titik 420 meter.",
                "B": "Kabel serat optik dalam kondisi sempurna tanpa ada sambungan.",
                "C": "Terdapat konektor sambungan fusion splicer berkualitas tinggi di titik 420 meter.",
                "D": "OTDR kehabisan daya baterai tepat pada jarak 420 meter."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Lonjakan Fresnel tajam yang diikuti jatuhnya grafik ke dasar noise floor adalah karakteristik pemantulan kaca ke udara (glass-to-air interface) yang mengonfirmasi kabel terputus total di titik tersebut.",
                "2": "Grafik jatuh ke dasar menandakan kabel serat optik berhasil menembus dasar bumi.",
                "3": "Kabel serat optik yang putus tidak dapat terdeteksi oleh perangkat OTDR."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_TE_04",
            "phase": "HYPOTHESIS_TESTING_EVALUATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Dua Access Point diletakkan bersebelahan di lorong kelas dan keduanya disetel pada frekuensi kanal yang sama yaitu Kanal 6 pita 2.4 GHz. Pengujian throughput menunjukkan penurunan kecepatan hingga 50% pada kedua AP. Evaluasi teknis atas hasil pengujian ini adalah...",
            "options": {
                "A": "Terjadi interferensi kanal bersama (Co-Channel Interference / CCI) di mana kedua AP dan seluruh kliennya berbagi domain tabrakan contention yang sama.",
                "B": "Kedua AP otomatis saling bertukar bandwidth internet secara seimbang.",
                "C": "Kanal 6 adalah kanal khusus yang hanya boleh digunakan oleh satu sekolah dalam satu kota.",
                "D": "Kabel listrik kedua AP mengalami korsleting arus bolak-balik."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Ketika dua BSS beroperasi pada frekuensi yang sama dalam jarak jangkauan yang saling mendengar, mekanisme CSMA/CA memaksa kedua sel antrean mengantre bersamaan, membagi kapasitas airtime menjadi dua.",
                "2": "Karena kanal 6 memiliki panjang gelombang paling pendek pada pita frekuensi 2.4 GHz.",
                "3": "Interferensi ko-kanal hanya terjadi jika kedua AP memiliki merek pabrikan yang berbeda."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_TE_05",
            "phase": "HYPOTHESIS_TESTING_EVALUATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Pada port switch dihubungkan kabel UTP ke komputer server. Port switch tersetting 100 Mbps Full-Duplex, sedangkan kartu jaringan komputer tersetting Auto-Negotiation dan gagal bernegosiasi sehingga fallback ke Half-Duplex. Hasil uji transfer data menunjukkan lonjakan frame galat Late Collision. Evaluasi diagnostik yang tepat adalah...",
            "options": {
                "A": "Terjadi duplex mismatch yang menyebabkan tabrakan data karena switch mengirim data tanpa memedulikan status jalur yang sedang dipakai server.",
                "B": "Kabel UTP yang digunakan terlalu pendek sehingga elektron memantul kembali.",
                "C": "Server menolak koneksi karena switch menggunakan sistem operasi berbeda.",
                "D": "Late collision adalah tanda bahwa kartu jaringan server telah berhasil di-overclock."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Dalam kondisi duplex mismatch, sisi Full-Duplex mentransmisikan data setiap saat, sementara sisi Half-Duplex mendeteksi transmisi tersebut sebagai tabrakan setelah jendela slot time 64 byte terlampaui (late collision).",
                "2": "Half-Duplex dan Full-Duplex dapat bekerja bersamaan secara sempurna tanpa ada penurunan performa.",
                "3": "Switch manageable tidak dapat membedakan antara mode Full-Duplex dan Half-Duplex."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_TE_06",
            "phase": "HYPOTHESIS_TESTING_EVALUATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Teknisi melakukan pengujian stabilitas link kabel UTP dengan mengirimkan 1000 paket ICMP ukuran besar (1400 byte). Hasil menunjukkan round-trip time rata-rata stabil 1 ms, namun terdapat 2 paket yang hilang (0.2% loss). Evaluasi teknis atas hasil uji ini menunjukkan bahwa...",
            "options": {
                "A": "Link fisik kabel UTP berada dalam kondisi sangat sehat dan memenuhi standar kualitas transmisi data jaringan lokal.",
                "B": "Seluruh instalasi kabel UTP harus dibongkar dan diganti baru seketika.",
                "C": "Toleransi packet loss pada jaringan kabel tembaga harus bernilai tepat 10%.",
                "D": "Komputer pengirim harus di-restart agar packet loss mencapai angka nol mutlak."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Tingkat packet loss di bawah 1% pada pengujian beban paket besar mengindikasikan bahwa integritas fisik media kabel sangat baik dan latensi 1 ms mengonfirmasi ketiadaan kongesti antrean.",
                "2": "Kehilangan 2 paket dari 1000 paket membuktikan bahwa kabel tembaga mengalami patah di bagian tengah.",
                "3": "Pengujian 1000 paket ICMP hanya berlaku untuk jaringan satelit internasional."
            },
            "correct_reasoning": "1"
        },

        # --- FASE 5: CORRECTIVE_ACTION_VERIFICATION (B25 - B30) ---
        {
            "id": "TB_B_CA_01",
            "phase": "CORRECTIVE_ACTION_VERIFICATION",
            "curriculum_element": "TP 2.1 - Instalasi Jaringan Nirkabel",
            "prompt": "Teknisi diminta merancang alokasi frekuensi untuk 4 Access Point di satu lantai gedung menggunakan pita frekuensi 5 GHz (lebar kanal 20 MHz). Kombinasi kanal UNII-1 non-overlapping manakah yang harus dipilih agar seluruh AP beroperasi tanpa saling menginterferensi?",
            "options": {
                "A": "Kanal 36, 40, 44, dan 48.",
                "B": "Kanal 1, 6, 11, dan 14.",
                "C": "Kanal 36, 37, 38, dan 39.",
                "D": "Kanal 50, 60, 70, dan 80."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Pada pita 5 GHz UNII-1 (lebar 20 MHz), kanal 36 (5180 MHz), 40 (5200 MHz), 44 (5220 MHz), dan 48 (5240 MHz) memiliki jarak pisah frekuensi 20 MHz sehingga seluruhnya non-overlapping secara sempurna.",
                "2": "Kanal 1, 6, dan 11 adalah kanal pada pita frekuensi 5 GHz.",
                "3": "Pita frekuensi 5 GHz hanya memiliki 1 kanal yang dapat digunakan di dalam ruangan."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_CA_02",
            "phase": "CORRECTIVE_ACTION_VERIFICATION",
            "curriculum_element": "TP 2.1 - Instalasi Jaringan Nirkabel",
            "prompt": "Dua switch hub lawas yang belum mendukung fitur Auto-MDI/MDIX akan dihubungkan satu sama lain menggunakan kabel UTP. Tindakan pembuatan kabel yang benar agar kedua switch dapat saling bertukar data adalah...",
            "options": {
                "A": "Membuat kabel dengan skema Crossover (satu ujung standar T568A dan ujung lainnya T568B).",
                "B": "Membuat kabel dengan skema Straight-Through (kedua ujung sama-sama T568B).",
                "C": "Membuat kabel dengan menghubungkan pin 1 ke pin 1 dan pin 2 ke pin 2 saja.",
                "D": "Memotong kabel menjadi dua bagian dan menyambungnya kembali dengan isolasi hitam."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Koneksi antar-perangkat sejenis (switch ke switch tanpa Auto-MDIX) membutuhkan pembalikan pasangan pin kirim (Tx) dan terima (Rx) pada pin 1-3 dan 2-6 melalui skema crossover T568A/T568B.",
                "2": "Kabel Straight-Through hanya digunakan jika switch dihubungkan ke komputer server mainframe.",
                "3": "Perangkat sejenis selalu dapat terhubung dengan kabel jenis apa pun secara otomatis."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_CA_03",
            "phase": "CORRECTIVE_ACTION_VERIFICATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Kabel patch cord serat optik di rak server mengalami tekukan tajam dengan radius kelengkungan hanya 10 mm sehingga link down. Tindakan perbaikan yang harus dilakukan teknisi adalah...",
            "options": {
                "A": "Melepaskan ikatan kabel, merapikan jalur kabel pada tray pemandu dengan radius kelengkungan minimal 30 mm, dan memeriksa kembali status link.",
                "B": "Menarik kabel serat optik sekencang mungkin agar posisinya lurus tegang.",
                "C": "Mengganti inti kaca kabel dengan kawat tembaga solder.",
                "D": "Menambahkan cairan pelumas minyak di ujung konektor optik."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Mempertahankan radius kelengkungan (bending radius) di atas batas spesifikasi pabrikan (umumnya minimal 30 mm untuk kabel standar) memulihkan kondisi pemantulan internal total di dalam core kaca.",
                "2": "Kabel serat optik harus ditarik dengan beban minimal 50 kg agar pulsa cahaya stabil.",
                "3": "Minyak pelumas dapat membantu mempercepat laju rambat cahaya di dalam kabel kaca."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_CA_04",
            "phase": "CORRECTIVE_ACTION_VERIFICATION",
            "curriculum_element": "TP 2.1 - Instalasi Jaringan Nirkabel",
            "prompt": "Sebuah Access Point dual-band di lab mengalami kepadatan berlebih di pita 2.4 GHz, sementara pita 5 GHz nyaris kosong karena klien lama enggan berpindah. Tindakan konfigurasi korektif pada AP yang paling tepat adalah...",
            "options": {
                "A": "Mengaktifkan fitur Band Steering pada Access Point untuk mengarahkan klien dual-band agar memprioritaskan koneksi ke pita 5 GHz.",
                "B": "Mematikan pita frekuensi 5 GHz secara permanen dari menu pengaturan.",
                "C": "Menaikkan batas daya listrik Access Point menjadi 380 Volt tiga fase.",
                "D": "Mengganti nama SSID pada pita 5 GHz menjadi karakter tersembunyi."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Fitur Band Steering mendeteksi perangkat klien yang berkemampuan dual-band dan menunda respons probe request di 2.4 GHz sehingga klien terdorong berasosiasi pada pita 5 GHz yang lebih lengang dan cepat.",
                "2": "Mematikan frekuensi 5 GHz akan melipatgandakan kecepatan internet di pita 2.4 GHz.",
                "3": "Pita 2.4 GHz dan 5 GHz tidak dapat dipancarkan bersamaan oleh satu Access Point."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_CA_05",
            "phase": "CORRECTIVE_ACTION_VERIFICATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Kabel patch cord UTP yang menghubungkan komputer guru ke wallplate port jaringan memiliki klip pengunci konektor RJ45 yang patah dan sering terlepas sendiri saat meja tersenggol. Tindakan korektif yang tepat adalah...",
            "options": {
                "A": "Mengganti patch cord tersebut dengan patch cord pabrikan baru yang memiliki klip pengunci utuh dan boot pelindung konektor.",
                "B": "Menempelkan selotip lakban hitam di sekeliling konektor RJ45.",
                "C": "Mengganjal port jaringan dengan kertas koran basah.",
                "D": "Membiarkan konektor longgar karena sinyal listrik tetap dapat melompat melalui udara."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Klip pengunci yang patah memicu kontak fisik pin tembaga tidak stabil (loose connection), menghasilkan resistansi kontak tinggi dan port flapping; penggantian kabel menjamin keandalan mekanis dan elektrik.",
                "2": "Klip konektor RJ45 hanya berfungsi sebagai aksesoris hiasan tanpa fungsi penahan fisik.",
                "3": "Selotip lakban dapat mengalirkan data jaringan secara mandiri tanpa pin tembaga."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_CA_06",
            "phase": "CORRECTIVE_ACTION_VERIFICATION",
            "curriculum_element": "TP 2.2 - Perawatan dan Perbaikan",
            "prompt": "Setelah teknisi selesai mengganti switch hub yang rusak di laboratorium TKJ, prosedur verifikasi operasional akhir yang membuktikan bahwa seluruh jaringan lab telah kembali normal adalah...",
            "options": {
                "A": "Melakukan uji konektivitas ping dan pengujian transfer file secara acak pada sampel komputer di setiap baris meja lab dan memastikan status port switch normal.",
                "B": "Melihat apakah lampu indikator power switch menyala hijau lalu langsung pulang.",
                "C": "Mematikan server utama untuk melihat apakah komputer siswa ikut mati.",
                "D": "Meminta siswa membersihkan debu di keyboard komputer masing-masing."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Verifikasi menyeluruh melibatkan pengujian fungsional Layer 1 (lampu port switch), Layer 3 (ping reachability), dan throughput beban nyata untuk memastikan tidak ada segmen lab yang terisolasi.",
                "2": "Karena menyalanya lampu power switch otomatis membuktikan bahwa seluruh komputer lab pasti terhubung internet.",
                "3": "Uji transfer file hanya boleh dilakukan oleh teknisi bersertifikat internasional."
            },
            "correct_reasoning": "1"
        },

        # --- NON-EQUIVALENT DEPENDENT VARIABLE (NEDV - KONTROL) (B31 - B36) ---
        {
            "id": "TB_B_NEDV_01",
            "phase": "NEDV_CONTROL",
            "curriculum_element": "TP 2.3 - Layanan Voice over IP",
            "prompt": "Dalam sistem komunikasi telepon VoIP, protokol layer transport manakah yang digunakan untuk mengalirkan payload media suara secara langsung secara real-time dengan latensi terendah?",
            "options": {
                "A": "Real-time Transport Protocol (RTP) di atas protokol UDP.",
                "B": "Transmission Control Protocol (TCP) dengan Three-Way Handshake.",
                "C": "File Transfer Protocol (FTP) dengan enkripsi TLS.",
                "D": "Post Office Protocol 3 (POP3) pada port 110."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "RTP berjalan di atas UDP untuk meminimalkan overhead latensi transmisi suara; retransmisi TCP tidak diinginkan pada suara real-time karena paket terlambat tidak lagi bernilai bagi pendengar.",
                "2": "Paket suara VoIP selalu menggunakan TCP agar setiap suku kata dapat dikonfirmasi ulang jika hilang.",
                "3": "Protokol UDP tidak dapat digunakan untuk mentransmisikan data audio nirkabel."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_NEDV_02",
            "phase": "NEDV_CONTROL",
            "curriculum_element": "TP 2.3 - Layanan Voice over IP",
            "prompt": "Jika kualitas suara panggilan VoIP terdengar jernih tanpa kompresi dengan konsumsi bandwidth 64 kbps per panggilan, codec standar ITU-T yang sedang aktif digunakan pada perangkat IP Phone adalah...",
            "options": {
                "A": "Codec G.711 (Pulse Code Modulation / PCM)",
                "B": "Codec G.729 (CS-ACELP)",
                "C": "Codec MP3 pada bitrate 320 kbps",
                "D": "Codec H.264 Video Coding"
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "G.711 mengodekan sinyal audio analog menjadi sampel digital 8-bit pada frekuensi sampling 8 kHz (8 x 8000 = 64 kbps), memberikan kualitas suara toll-quality tanpa beban kompresi algoritma.",
                "2": "G.711 adalah codec kompresi video untuk kamera pengawas CCTV.",
                "3": "Codec G.729 mengonsumsi bandwidth 64 kbps per saluran panggilan."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_NEDV_03",
            "phase": "NEDV_CONTROL",
            "curriculum_element": "TP 2.4 - Instalasi Fiber Optik",
            "prompt": "Kabel serat optik Multi-Mode (MMF) dengan diameter core 50 atau 62.5 mikrometer umumnya digunakan untuk instalasi jarak pendek (di dalam gedung atau antarrack data center < 500 meter) karena...",
            "options": {
                "A": "Mengalami dispersi modal (modal dispersion) yang menyebabkan pulsa cahaya melebar dan saling bertumpuk pada jarak jauh.",
                "B": "Kabel Multi-Mode tidak tahan terhadap suhu udara ruangan di atas 10 derajat Celcius.",
                "C": "Inti serat Multi-Mode terbuat dari tembaga berlapis perak.",
                "D": "Kabel Multi-Mode dilarang oleh regulasi internasional untuk dipasang di luar ruangan."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Diameter core yang besar memungkinkan banyak mode berkas cahaya merambat dengan lintasan berbeda; selisih waktu tiba masing-masing mode memicu pelebaran pulsa (modal dispersion) yang membatasi jarak transmisi.",
                "2": "Multi-Mode hanya dapat mentransmisikan cahaya dengan kecepatan 10 bit per detik.",
                "3": "Serat optik Multi-Mode memiliki redaman lebih rendah daripada Single-Mode pada jarak 100 km."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_NEDV_04",
            "phase": "NEDV_CONTROL",
            "curriculum_element": "TP 2.4 - Instalasi Fiber Optik",
            "prompt": "Dalam struktur kabel serat optik, lapisan pelindung pertama yang mengelilingi inti kaca (core) dan memiliki indeks bias yang sengaja dirancang lebih kecil daripada inti kaca disebut...",
            "options": {
                "A": "Cladding",
                "B": "Coating / Buffer",
                "C": "Strength Member (Kevlar)",
                "D": "Outer Jacket (Kulit Luar)"
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Cladding berfungsi sebagai batas optik medium rapat ke renggang (n_core > n_cladding) yang menghasilkan fenomena pantulan internal total agar cahaya tetap terkurung di dalam core kaca.",
                "2": "Kevlar adalah lapisan yang memantulkan pulsa laser menggunakan medan magnet.",
                "3": "Outer jacket terbuat dari bahan kaca silika murni tanpa campuran polimer."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_NEDV_05",
            "phase": "NEDV_CONTROL",
            "curriculum_element": "TP 2.5 - Perbaikan Fiber Optik",
            "prompt": "Setelah serat optik dikupas menggunakan Miller stripper dan dibersihkan dengan alkohol isopropil 95%, pisau pemotong Fiber Cleaver digunakan. Mengapa permukaan ujung serat optik hasil potongan tidak boleh disentuh jari sebelum dimasukkan ke mesin splicer?",
            "options": {
                "A": "Karena minyak dan keringat dari jari tangan akan mengotori permukaan kaca dan menyebabkan gelembung fusi yang memicu redaman tinggi.",
                "B": "Karena jari tangan dapat menghantarkan sengatan listrik laser berkekuatan 1000 Watt.",
                "C": "Karena kaca serat optik akan seketika mencair saat terkena suhu tubuh manusia.",
                "D": "Menyentuh ujung serat optik dilarang hanya untuk menjaga agar sidik jari tidak tertinggal."
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "Minyak alami kulit, garam keringat, dan partikel debu mikro yang menempel pada ujung serat akan terbakar menjadi jelaga karbon saat elektroda splicer menyala, merusak transparansi titik sambungan kaca.",
                "2": "Kabel serat optik mengandung racun kimia arsenik yang dapat meresap ke pori-pori kulit.",
                "3": "Menyentuh kaca serat optik akan mengubah frekuensi cahaya laser dari inframerah menjadi ultraviolet."
            },
            "correct_reasoning": "1"
        },
        {
            "id": "TB_B_NEDV_06",
            "phase": "NEDV_CONTROL",
            "curriculum_element": "TP 2.5 - Perbaikan Fiber Optik",
            "prompt": "Seorang teknisi ingin melakukan pelacakan cepat kontinuitas serat optik sepanjang 50 meter di dalam lab untuk mendeteksi apakah core kaca putus atau tertukar. Alat penguji visual portabel paling praktis yang memancarkan sinar laser merah tampak (panjang gelombang ~650 nm) adalah...",
            "options": {
                "A": "Visual Fault Locator (VFL / Laser Pen)",
                "B": "Optical Time-Domain Reflectometer (OTDR)",
                "C": "Fusion Splicer Elektroda",
                "D": "Spectrum Analyzer Radio Frekuensi"
            },
            "correct_option": "A",
            "reasoning_options": {
                "1": "VFL memancarkan sinar laser merah kasat mata (visible red light); jika ada retakan (micro-bending) atau kabel patah di dekat patch cord/tray, cahaya merah akan berpendar keluar menembus selubung kabel.",
                "2": "VFL digunakan untuk mengukur bandwidth throughput jaringan internet kabel.",
                "3": "OTDR adalah alat berupa senter saku kecil tanpa layar grafik digital."
            },
            "correct_reasoning": "1"
        }
    ]

    data = {
        "title": "Instrumen Tes Kemampuan Logical Thinking Berbasis Penalaran Troubleshooting Jaringan Komputer TKJ",
        "theoretical_framework": "David H. Jonassen & Woei Hung (2006) - Cognitive Troubleshooting Architecture",
        "scoring_guide": {
            "scale": "Polikotomis Tiga Tingkat (0, 1, 2)",
            "rules": {
                "2": "Opsi tindakan teknis Tier 1 Benar DAN opsi alasan kausal ilmiah Tier 2 Benar (Penalaran Ilmiah Matang)",
                "1": "Opsi tindakan teknis Tier 1 Benar TETAPI opsi alasan Tier 2 Keliru (Hafalan Prosedural Semu), ATAU Opsi Tier 1 Keliru akibat salah perhitungan teknis minor namun Alasan Tier 2 Benar (Penguasaan Parsial / Miskonsepsi)",
                "0": "Opsi Tier 1 dan Tier 2 Keliru keduanya, atau tidak menjawab (Tidak Menguasai Konsep)"
            },
            "score_ranges": {
                "target_test_items": "30 Butir (Skor Maksimal = 60 Poin, 12 Poin per Fase Kognitif)",
                "nedv_control_items": "6 Butir (Skor Maksimal = 12 Poin, Dianalisis Terpisah untuk Validitas Internal)",
                "total_items_per_form": 36
            }
        },
        "phases_legend": {
            "SYMPTOM_RECOGNITION": "Fase 1: Pengenalan Gejala & Anomali Sistem (6 Butir)",
            "PROBLEM_SPACE_CONSTRUCTION": "Fase 2: Konstruksi Ruang Masalah & Isolasi Variabel (6 Butir)",
            "FAULT_HYPOTHESIS_GENERATION": "Fase 3: Perumusan Hipotesis Gangguan Kausalitas Fisik (6 Butir)",
            "HYPOTHESIS_TESTING_EVALUATION": "Fase 4: Pengujian & Evaluasi Hipotesis Diagnostik (6 Butir)",
            "CORRECTIVE_ACTION_VERIFICATION": "Fase 5: Tindakan Korektif & Verifikasi Link (6 Butir)",
            "NEDV_CONTROL": "Variabel Kontrol Non-Equivalent (TP 2.3 VoIP 2 Butir + TP 2.4/2.5 Fiber Optik 4 Butir)"
        },
        "form_a": form_a_items,
        "form_b": form_b_items
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated 36-item parallel instruments (Form A & Form B) at:\n{OUTPUT_FILE}")
    print(f"Form A: {len(form_a_items)} items (30 target + 6 NEDV)")
    print(f"Form B: {len(form_b_items)} items (30 target + 6 NEDV)")


if __name__ == "__main__":
    build_parallel_troubleshooting_bank()
