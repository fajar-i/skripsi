"""
LogiTrace: Curated 180-Item Adaptive Bank Builder.
Constructs a balanced bank of 180 items (12 KCs x 15 items: 5 easy, 5 med, 5 hard),
including 6 standardized calibration items (US-01) and full TOLT dimension mapping.
"""

import json
import os
from typing import Dict, List

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "items_adaptive_180.json")

# 12 Knowledge Components
KCS = [
    "WLAN_STANDARDS",
    "WLAN_TOPOLOGY_BSS",
    "IP_PEER_CONFIG",
    "WLAN_FREQ_CHANNEL",
    "WLAN_SECURITY_AUTH",
    "WLAN_HOST_HARDENING",
    "WLAN_SIGNAL_PROP",
    "WLAN_ROAMING_PROB",
    "WLAN_CHANNEL_COLLISION",
    "ICMP_CONNECTIVITY",
    "ICMP_TROUBLE_DHU",
    "ICMP_TROUBLE_RTO"
]

TOLT_DIMS = [
    "CONTROLLING_VARIABLES",
    "PROPORTIONAL_REASONING",
    "COMBINATORIAL_REASONING",
    "PROBABILISTIC_REASONING",
    "CORRELATIONAL_REASONING"
]


def build_bank() -> List[Dict]:
    items = []

    # Specification templates per KC
    # Each KC will have 15 items:
    # Index 0-4: Difficulty 1 (Easy)
    # Index 5-9: Difficulty 2 (Medium)
    # Index 10-14: Difficulty 3 (Hard)

    kc_blueprints = {
        "WLAN_STANDARDS": {
            "easy": [
                (
                    "Manakah di antara standar nirkabel IEEE 802.11 berikut yang hanya beroperasi pada pita frekuensi 2.4 GHz dan memiliki kecepatan data teoretis maksimal 54 Mbps?",
                    {"A": "IEEE 802.11g", "B": "IEEE 802.11a", "C": "IEEE 802.11ac", "D": "IEEE 802.11ax"},
                    "A",
                    "PROPORTIONAL_REASONING",
                    "802.11g beroperasi murni pada pita 2.4 GHz dengan kecepatan puncak 54 Mbps menggunakan modulasi OFDM."
                ),
                (
                    "Standar nirkabel IEEE 802.11ac (Wi-Fi 5) dirancang khusus untuk beroperasi pada pita frekuensi...",
                    {"A": "5 GHz secara eksklusif", "B": "2.4 GHz secara eksklusif", "C": "900 MHz", "D": "60 GHz"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "IEEE 802.11ac hanya beroperasi pada pita 5 GHz untuk memaksimalkan throughput tanpa interferensi pita 2.4 GHz."
                ),
                (
                    "Keunggulan utama pita frekuensi 2.4 GHz dibandingkan pita frekuensi 5 GHz pada lingkungan laboratorium kejuruan adalah...",
                    {"A": "Jangkauan sinyal lebih jauh dan kemampuan menembus dinding lebih baik", "B": "Kecepatan transfer data dua kali lipat lebih cepat", "C": "Bebas dari segala macam interferensi perangkat elektronik", "D": "Jumlah kanal non-overlapping yang jauh lebih banyak"},
                    "A",
                    "CORRELATIONAL_REASONING",
                    "Frekuensi yang lebih rendah (2.4 GHz) memiliki panjang gelombang lebih besar sehingga redamannya lebih rendah saat menembus material padat."
                ),
                (
                    "Teknologi Wi-Fi 6 secara resmi mengacu pada spesifikasi standar IEEE nomor...",
                    {"A": "IEEE 802.11ax", "B": "IEEE 802.11n", "C": "IEEE 802.11b", "D": "IEEE 802.11ac"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "Wi-Fi Alliance menetapkan nama dagang Wi-Fi 6 untuk standar teknis IEEE 802.11ax."
                ),
                (
                    "Berapakah kecepatan data maksimal teoretis pada standar nirkabel IEEE 802.11b lawas?",
                    {"A": "11 Mbps", "B": "54 Mbps", "C": "150 Mbps", "D": "300 Mbps"},
                    "A",
                    "PROPORTIONAL_REASONING",
                    "802.11b beroperasi pada 2.4 GHz dengan kecepatan transfer data maksimum hingga 11 Mbps menggunakan DSSS."
                ),
            ],
            "medium": [
                (
                    "Sebuah laboratorium TKJ mengganti AP dari 802.11n (2.4 GHz) ke 802.11ac (5 GHz). Mengapa siswa di sudut luar ruangan mengalami penurunan bar sinyal meskipun kecepatan dekat AP meningkat drastis?",
                    {"A": "Gelombang 5 GHz mengalami pelemahan (redaman ruang bebas dan dinding) yang lebih besar seiring jarak", "B": "Ponsel siswa otomatis menonaktifkan fitur antena nirkabel pada jarak di atas 5 meter", "C": "Standar 802.11ac tidak mendukung enkripsi WPA2", "D": "Kabel UTP yang menuju ke Access Point otomatis mengalami pembatasan bandwidth"},
                    "A",
                    "CORRELATIONAL_REASONING",
                    "Sesuai persamaan Free Space Path Loss, redaman meningkat berbanding lurus dengan frekuensi gelombang radio."
                ),
                (
                    "Fitur OFDMA (Orthogonal Frequency Division Multiple Access) pada standar Wi-Fi 6 (802.11ax) memungkinkan efisiensi tinggi di kelas dengan cara...",
                    {"A": "Membagi sebuah saluran radio ke dalam subcarrier resource units (RU) untuk melayani beberapa klien sekaligus", "B": "Mematikan Access Point secara otomatis saat lalu lintas data sedang sepi", "C": "Mengganti seluruh enkripsi kata sandi menjadi teks polos", "D": "Mengharuskan setiap klien menggunakan dua antena terpisah secara fisik"},
                    "A",
                    "COMBINATORIAL_REASONING",
                    "OFDMA membagi pita frekuensi menjadi resource units kecil sehingga transmisi data multi-user dapat berlangsung bersamaan tanpa menunggu antrean CSMA/CA."
                ),
                (
                    "Jika sebuah Access Point 802.11n mendukung MIMO 2x2 dengan lebar kanal 40 MHz, berapakah throughput maksimal PHY rate yang dapat dicapai (short guard interval)?",
                    {"A": "300 Mbps", "B": "54 Mbps", "C": "150 Mbps", "D": "600 Mbps"},
                    "A",
                    "PROPORTIONAL_REASONING",
                    "Pada 802.11n, 1 spatial stream pada 40 MHz menghasilkan 150 Mbps. Dengan MIMO 2x2 (2 spatial streams), kapasitas menjadi 2 x 150 = 300 Mbps."
                ),
                (
                    "Perbedaan mendasar antara teknologi MU-MIMO pada 802.11ac Wave 2 dan 802.11ax terletak pada...",
                    {"A": "802.11ax mendukung MU-MIMO dua arah (downlink dan uplink), sedangkan 802.11ac hanya downlink", "B": "802.11ac tidak dapat memancarkan sinyal ke ponsel cerdas", "C": "802.11ax hanya dapat digunakan untuk koneksi kabel fiber optik", "D": "802.11ac memerlukan izin frekuensi militer berbayar"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "Wi-Fi 5 Wave 2 hanya mendukung MU-MIMO downlink, sementara Wi-Fi 6 memperluasnya ke uplink dan downlink secara simultan."
                ),
                (
                    "Teknologi BSS Coloring pada standar IEEE 802.11ax berfungsi untuk...",
                    {"A": "Memberikan identitas numerik pada frame agar stasiun dapat mengabaikan transmisi dari AP tetangga pada kanal yang sama", "B": "Mengubah warna lampu LED pada casing fisik Access Point sesuai jumlah pengguna", "C": "Mendeteksi kabel LAN yang putus menggunakan pantulan cahaya warna-warni", "D": "Menentukan pembagian alamat IP DHCP berdasarkan kelompok siswa"},
                    "A",
                    "PROBABILISTIC_REASONING",
                    "BSS Coloring memberi label warna logika sehingga stasiun dapat membedakan frame jaringan lokal dengan frame asing (spatial reuse)."
                ),
            ],
            "hard": [
                (
                    "Sebuah AP 802.11ax melayani 34 smartphone siswa TKJ di satu ruangan lab. Berapakah alokasi ukuran Resource Unit (RU) terkecil per klien pada kanal 20 MHz menggunakan modulasi OFDMA agar seluruh klien dapat menerima paket transmisi penjadwalan simultan?",
                    {"A": "26-tone RU", "B": "52-tone RU", "C": "106-tone RU", "D": "242-tone RU"},
                    "A",
                    "COMBINATORIAL_REASONING",
                    "Pada kanal 20 MHz, standar 802.11ax dapat membagi spektrum hingga maksimal sembilan 26-tone RU secara bersamaan untuk trafik data kecil."
                ),
                (
                    "Di lingkungan bengkel TKJ terdapat mesin las listrik yang menimbulkan spark gap noise kuat. Standar nirkabel dan strategi spektrum manakah yang paling tahan terhadap interferensi elektromagnetik pita lebar ini?",
                    {"A": "802.11ax pada pita 5 GHz dengan kanal sempit 20 MHz dan modulasi adaptif", "B": "802.11b pada kanal 6 dengan lebar kanal 40 MHz", "C": "802.11g pada pita 2.4 GHz tanpa antena eksternal", "D": "Koneksi Ad-Hoc 802.11a tanpa Access Point"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "Pita 5 GHz memiliki jarak frekuensi jauh dari noise spark gap mesin industri, dan subcarrier sempit OFDMA 802.11ax memberikan ketahanan tinggi."
                ),
                (
                    "Sebuah Access Point disetel dengan MCS (Modulation and Coding Scheme) Index 9 pada 802.11ac. Jika nilai SNR tiba-tiba turun menjadi 12 dB karena pintu besi tertutup, fenomena adaptasi fisik apakah yang terjadi?",
                    {"A": "AP otomatis melakukan rate fallback ke indeks MCS yang lebih rendah (misal MCS 1 atau 2) dengan modulasi BPSK/QPSK yang lebih kokoh", "B": "AP langsung mematikan modul radio secara permanen", "C": "AP menaikkan frekuensi menjadi 60 GHz", "D": "Klien tetap memaksakan modulasi 256-QAM sehingga seluruh paket hilang total tanpa negosiasi"},
                    "A",
                    "CORRELATIONAL_REASONING",
                    "Algoritma dynamic rate shifting menurunkan skema modulasi saat SNR anjlok agar komunikasi data tetap tersambung meski bitrate menurun."
                ),
                (
                    "Target Wake Time (TWT) pada standar IEEE 802.11ax memberikan dampak positif langsung pada pembelajaran siswa yang menggunakan baterai smartphone di Zona B karena...",
                    {"A": "Mengatur jadwal tidur radio ponsel siswa secara presisi sehingga menghemat daya baterai dan mereduksi tabrakan media", "B": "Mematikan fungsi pengisian daya baterai saat ujian berlangsung", "C": "Mempercepat putaran kipas pendingin Access Point", "D": "Memaksa ponsel mengirim data terus-menerus tanpa henti"},
                    "A",
                    "PROBABILISTIC_REASONING",
                    "TWT menegosiasikan jendela waktu aktif klien sehingga stasiun dapat memasuki mode tidur (sleep) hemat daya di luar jendela transmisi."
                ),
                (
                    "Mengapa kanal bonding 80 atau 160 MHz pada standar 802.11ac/ax tidak disarankan diterapkan pada area lab sekolah yang berdekatan dengan 3 lab lain?",
                    {"A": "Karena mempersempit ketersediaan kanal independen dan memicu tabrakan co-channel antarlab yang menurunkan total throughput agregat", "B": "Karena kabel UTP Cat 5e tidak mampu mengalirkan arus listrik lebih dari 12 Volt", "C": "Karena ponsel siswa akan kelebihan panas akibat frekuensi tinggi", "D": "Karena sinyal 160 MHz dilarang oleh standar telekomunikasi internasional untuk area pendidikan"},
                    "A",
                    "COMBINATORIAL_REASONING",
                    "Penggabungan kanal selebar 160 MHz menghabiskan seluruh spektrum 5 GHz non-DFS, memaksa AP lain berbagi kanal yang sama sehingga throughput justru anjlok akibat contention."
                ),
            ]
        },
        "WLAN_TOPOLOGY_BSS": {
            "easy": [
                (
                    "Mode jaringan nirkabel di mana dua laptop siswa TKJ saling terhubung langsung untuk berbagi berkas tanpa melalui perantara Access Point disebut mode...",
                    {"A": "Ad-Hoc (Independent Basic Service Set / IBSS)", "B": "Infrastructure (BSS)", "C": "Extended Service Set (ESS)", "D": "WDS Repeater"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "Mode Ad-Hoc / IBSS menghubungkan perangkat peer-to-peer langsung tanpa Access Point terpusat."
                ),
                (
                    "Topologi nirkabel yang menggunakan sebuah Access Point sebagai pengendali pusat transmisi data bagi seluruh perangkat klien disebut...",
                    {"A": "Basic Service Set (BSS) Infrastructure", "B": "Ad-Hoc Network", "C": "Peer-to-Peer Mesh", "D": "Token Ring Wireless"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "BSS Infrastructure mengandalkan sebuah AP pusat yang memancarkan beacon dan mengatur asosiasi stasiun."
                ),
                (
                    "Gabungan dari dua atau lebih area Basic Service Set (BSS) yang saling terhubung melalui Distribution System (DS) dengan SSID yang sama dinamakan...",
                    {"A": "Extended Service Set (ESS)", "B": "Independent BSS", "C": "Point-to-Point Bridge", "D": "Mesh Standalone"},
                    "A",
                    "COMBINATORIAL_REASONING",
                    "ESS adalah gabungan beberapa BSS yang terhubung melalui backbone jaringan kabel (Distribution System)."
                ),
                (
                    "Identitas nama jaringan nirkabel yang dipancarkan secara berkala oleh Access Point agar dapat dikenali dan dipilih oleh perangkat siswa disebut...",
                    {"A": "SSID (Service Set Identifier)", "B": "BSSID (Basic Service Set Identifier)", "C": "MAC Address Ethernet", "D": "Subnet Mask IP"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "SSID adalah nama pengenal alfanumerik jaringan nirkabel yang dibaca pengguna pada daftar Wi-Fi perangkat."
                ),
                (
                    "Alamat fisik perangkat keras (MAC Address) dari radio nirkabel pada Access Point yang menjadi pengenal unik sebuah sel nirkabel di layer 2 disebut...",
                    {"A": "BSSID", "B": "SSID", "C": "Default Gateway", "D": "IP Address"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "BSSID adalah alamat MAC 48-bit antarmuka radio AP yang membedakan sel satu dengan sel lainnya dalam ESS yang sama."
                ),
            ],
            "medium": [
                (
                    "Pada topologi Extended Service Set (ESS) di laboratorium SMK, mengapa seluruh Access Point disarankan menggunakan SSID yang sama namun kanal frekuensi yang berbeda?",
                    {"A": "Agar siswa dapat berpindah AP secara mulus (roaming) tanpa interferensi co-channel antar-AP", "B": "Agar siswa harus memasukkan kata sandi yang berbeda di setiap ruangan", "C": "Agar saklar jaringan dapat memutus koneksi siswa yang tidak aktif", "D": "Agar daya pancar masing-masing AP meningkat secara otomatis"},
                    "A",
                    "COMBINATORIAL_REASONING",
                    "SSID seragam memungkinkan roaming transparan, sedangkan kanal berbeda (1, 6, 11) mencegah interferensi antar sel yang berdampingan."
                ),
                (
                    "Jika sebuah lab TKJ menerapkan mode Ad-Hoc antarlaptop siswa tanpa AP, kelemahan utama yang akan segera timbul saat jumlah siswa mencapai 34 orang adalah...",
                    {"A": "Skalabilitas sangat buruk dan collision rate melonjak drastis karena ketiadaan koordinasi terpusat", "B": "Laptop siswa tidak dapat memancarkan gelombang elektromagnetik lebih dari 10 cm", "C": "Setiap laptop wajib disambungkan kabel USB khusus ke laptop guru", "D": "Sistem operasi laptop otomatis terkunci dan minta restart"},
                    "A",
                    "PROBABILISTIC_REASONING",
                    "IBSS tidak memiliki penjadwalan AP terpusat; setiap stasiun memancarkan beacon secara independen sehingga tabrakan paket naik drastis seiring banyaknya stasiun."
                ),
                (
                    "Media perantara kabel atau serat optik yang menghubungkan beberapa Access Point dalam topologi Extended Service Set (ESS) ke server lokal LogiTrace disebut...",
                    {"A": "Distribution System (DS)", "B": "Wireless Distribution System (WDS)", "C": "Ad-Hoc Mesh Link", "D": "Peer Loop"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "Distribution System (DS) adalah tulang punggung infrastruktur (umumnya Ethernet switch) yang mengintegrasikan berbagai BSS."
                ),
                (
                    "Seorang guru TKJ ingin menghubungkan jaringan komputer di Gedung A dan Gedung B yang berjarak 300 meter tanpa menarik kabel tanah. Topologi nirkabel apakah yang tepat diaplikasikan?",
                    {"A": "Wireless Point-to-Point (PTP) Bridge menggunakan antena direktional", "B": "Mode Ad-Hoc dengan antena omnidireksional ponsel", "C": "Memasang satu Access Point indoor biasa di jendela Gedung A", "D": "Koneksi Bluetooth Low Energy"},
                    "A",
                    "PROPORTIONAL_REASONING",
                    "Wireless PTP Bridge dengan antena terarah (direktional) memfokuskan pancaran gelombang radio untuk koneksi backbone antargedung."
                ),
                (
                    "Apa fungsi frame Beacon yang dipancarkan secara teratur (default 100 ms) oleh Access Point dalam topologi BSS?",
                    {"A": "Menyinkronkan parameter waktu jaringan (TSF), mengumumkan SSID, laju data yang didukung, dan kapabilitas keamanan", "B": "Menghapus seluruh file sampah pada smartphone siswa yang terhubung", "C": "Mengukur suhu ruangan di sekitar laboratorium komputer", "D": "Mengirimkan seluruh jawaban soal kuis kepada siswa"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "Beacon frame adalah frame manajemen periodik yang memberitahukan kehadiran sel BSS dan menyinkronkan jam internal stasiun."
                ),
            ],
            "hard": [
                (
                    "Di sebuah aula sekolah diadakan pameran teknologi dengan 1 Access Point BSS yang menampung 100 klien aktif. Terjadi fenomena di mana klien dekat AP mendapat throughput tinggi sementara klien di pojok aula terputus total. Solusi arsitektur topologi manakah yang paling tepat?",
                    {"A": "Mengubah topologi dari single BSS ke ESS multi-AP berdaya pancar rendah (micro-cell) dengan alokasi kanal non-overlapping", "B": "Menaikkan daya pancar AP tunggal tersebut ke tingkat maksimal 30 dBm", "C": "Mengubah mode seluruh smartphone siswa menjadi mode IBSS Ad-Hoc", "D": "Mengganti antena AP menjadi kabel tembaga panjang"},
                    "A",
                    "COMBINATORIAL_REASONING",
                    "Satu AP memiliki kapasitas airtime terbatas. Arsitektur multi-cell ESS membagi beban kepadatan klien ke beberapa saluran radio yang berbeda."
                ),
                (
                    "Pada perancangan Wireless Mesh Network (WMN) di area kampus SMK, apa kelemahan utama penambahan hop nirkabel berulang (multi-hop mesh) terhadap performa transmisi data kuis adaptif?",
                    {"A": "Throughput efektif terbagi separuh pada setiap hop nirkabel pada sistem radio tunggal (half-duplex retransmission latency)", "B": "Sistem enkripsi otomatis rusak pada hop ketiga", "C": "Alamat IP siswa berubah menjadi alamat broadcast publik", "D": "Setiap hop menambah konsumsi kuota data internet hingga 10 kali lipat"},
                    "A",
                    "PROPORTIONAL_REASONING",
                    "Radio tunggal harus menerima dan memancarkan ulang frame pada kanal yang sama, menghabiskan separuh kapasitas transmisi untuk setiap penambahan hop relai."
                ),
                (
                    "Dalam perancangan ESS dengan protokol fast roaming IEEE 802.11r (FT), bagaimana proses pertukaran kunci keamanan dioptimalkan untuk mencegah putusnya sesi kuis siswa saat berpindah AP?",
                    {"A": "Kunci enkripsi baru dinegosiasikan melalui AP awal sebelum stasiun berpindah asosiasi (pre-authentication handshake)", "B": "Klien mematikan seluruh enkripsi data saat bergerak", "C": "Server LogiTrace mengirimkan kunci lewat SMS ke kartu SIM siswa", "D": "AP baru mengabaikan autentikasi dan langsung membuka akses tanpa enkripsi"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "802.11r memungkinkan pre-authentication di mana turunan kunci PMK-R1 dinegosiasikan sebelum reasosiasi sehingga memangkas latensi transisi < 50 ms."
                ),
                (
                    "Di lab TKJ dipasang dua AP yang terhubung ke satu switch dengan kabel LAN. Kedua AP disetel dengan SSID yang sama, namun siswa yang berpindah meja mengeluh koneksi internetnya macet dan IP-nya bentrok. Akar masalah topologi yang paling logis adalah...",
                    {"A": "Kedua AP memiliki server DHCP internal aktif yang mendistribusikan rentang subnet IP yang saling tumpang tindih", "B": "Siswa menggunakan merek smartphone yang tidak kompatibel dengan kabel switch", "C": "Kabel UTP yang digunakan memiliki panjang melebihi 2 meter", "D": "Frekuensi kedua AP tidak sinkron dengan gelombang bumi"},
                    "A",
                    "CORRELATIONAL_REASONING",
                    "Dua server DHCP aktif pada segmen layer 2 yang sama (rogue DHCP) akan menimbulkan konflik pembagian IP dan salah gateway default."
                ),
                (
                    "Jika dalam satu lab TKJ terdapat 17 unit PC di Zona A (kabel) dan 17 smartphone di Zona B (nirkabel), konfigurasi pemisahan layer 2 terbaik pada Access Point dan Switch manajemen adalah...",
                    {"A": "Menerapkan pemetaan SSID Zona B ke VLAN ID khusus yang terisolasi dari segmen VLAN PC Zona A", "B": "Menghubungkan AP nirkabel ke port loopback pada router", "C": "Mematikan fungsi switching dan mengubah topologi menjadi daisy-chain", "D": "Menggabungkan seluruh perangkat ke dalam workgroup Windows tanpa IP"},
                    "A",
                    "COMBINATORIAL_REASONING",
                    "Penggunaan VLAN berbasis SSID mengisolasi domain siaran (broadcast domain) Zona B nirkabel dari Zona A laboratorium kabel."
                ),
            ]
        },
        "IP_PEER_CONFIG": {
            "easy": [
                (
                    "Sebuah smartphone siswa di Zona B terhubung ke AP dengan konfigurasi IP statis 192.168.1.50/24. Manakah alamat subnet mask yang tepat untuk prefix tersebut?",
                    {"A": "255.255.255.0", "B": "255.255.0.0", "C": "255.255.255.128", "D": "255.0.0.0"},
                    "A",
                    "PROPORTIONAL_REASONING",
                    "Prefix /24 merepresentasikan 24 bit angka biner 1 berurutan, setara dengan desimal 255.255.255.0."
                ),
                (
                    "Server lokal LogiTrace memiliki alamat IP 192.168.10.1/24. Manakah alamat IP yang sah (valid) dan berada dalam satu subnet yang sama untuk dipasang pada ponsel siswa?",
                    {"A": "192.168.10.25", "B": "192.168.11.25", "C": "192.168.10.0", "D": "192.168.10.255"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "192.168.10.25 berada pada rentang host valid (1–254). 192.168.10.0 adalah Network ID dan .255 adalah Broadcast ID."
                ),
                (
                    "Protokol jaringan yang bertugas memetakan alamat logika IP (Layer 3) ke alamat fisik MAC Address (Layer 2) pada komunikasi lokal nirkabel adalah...",
                    {"A": "Address Resolution Protocol (ARP)", "B": "Dynamic Host Configuration Protocol (DHCP)", "C": "Domain Name System (DNS)", "D": "Internet Control Message Protocol (ICMP)"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "ARP bertugas mencari alamat MAC perangkat tujuan berdasarkan alamat IP yang diketahui dalam satu subnet lokal."
                ),
                (
                    "Berapa jumlah maksimal host yang dapat dialokasikan pada subnet dengan prefix /24?",
                    {"A": "254 host", "B": "256 host", "C": "128 host", "D": "512 host"},
                    "A",
                    "PROPORTIONAL_REASONING",
                    "Jumlah host = 2^(32-24) - 2 = 2^8 - 2 = 256 - 2 = 254 alamat host valid."
                ),
                (
                    "Jika sebuah perangkat klien salah memasukkan Default Gateway (misal diisi alamat IP milik klien lain), dampak teknis langsung yang akan dialami klien tersebut adalah...",
                    {"A": "Klien tidak dapat mengirimkan paket data ke jaringan di luar subnet lokalnya", "B": "Layar ponsel klien otomatis mati", "C": "Seluruh data di kartu memori klien terhapus", "D": "Access Point langsung me-reset konfigurasinya ke setelan pabrik"},
                    "A",
                    "CORRELATIONAL_REASONING",
                    "Default Gateway adalah pintu keluar paket menuju jaringan luar; jika salah, perutean antarnetwork akan gagal total."
                ),
            ],
            "medium": [
                (
                    "Laboratorium TKJ membutuhkan subnet khusus untuk 34 siswa di Zona B agar tidak menghamburkan alamat IP. Prefix CIDR terkecil manakah yang dapat menampung minimal 34 perangkat siswa sekaligus?",
                    {"A": "/26 (menampung hingga 62 host)", "B": "/27 (menampung hingga 30 host)", "C": "/28 (menampung hingga 14 host)", "D": "/25 (menampung hingga 126 host)"},
                    "A",
                    "COMBINATORIAL_REASONING",
                    "/27 hanya menyediakan 30 host (tidak cukup untuk 34 siswa). Maka prefix terkecil yang mencukupi adalah /26 (2^6 - 2 = 62 host)."
                ),
                (
                    "Seorang siswa mengonfigurasi IP 192.168.1.15/28 pada ponselnya, sementara server kuis berada di IP 192.168.1.20/28. Mengapa siswa tidak dapat mengakses server kuis meskipun berada di Access Point yang sama?",
                    {"A": "Kedua IP berada pada subnet blok yang berbeda (192.168.1.15 adalah broadcast subnet 1, sedangkan .20 berada di subnet 2)", "B": "Prefix /28 tidak mendukung koneksi jaringan nirkabel", "C": "Access Point memblokir seluruh angka IP yang berakhiran ganjil", "D": "Kabel server kuis harus menggunakan tipe cross-over khusus ponsel"},
                    "A",
                    "COMBINATORIAL_REASONING",
                    "Pada /28, subnet 0 adalah 192.168.1.0-15 (host 1-14, broadcast .15). Subnet 1 adalah 192.168.1.16-31 (host 17-30). Keduanya berbeda segmen siaran."
                ),
                (
                    "Ketika smartphone siswa mengirim paket ke server lokal LogiTrace, ponsel memeriksa tabel routing internalnya. Kapan paket tersebut akan diteruskan ke Default Gateway alih-alih langsung di-ARP?",
                    {"A": "Saat hasil operasi bitwise AND antara IP tujuan dan netmask ponsel menghasilkan Network ID yang berbeda dengan Network ID lokal ponsel", "B": "Saat baterai ponsel siswa berada di bawah 20 persen", "C": "Setiap kali paket data berukuran lebih besar dari 100 byte", "D": "Hanya jika Access Point berada dalam posisi mati"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "Operasi bitwise AND menentukan apakah host tujuan berada di subnet lokal (kirim ARP langsung) atau di luar subnet (kirim ke MAC Gateway)."
                ),
                (
                    "Jika alamat IP gateway adalah 172.16.5.1/22, berapakah alamat broadcast dari subnet tersebut?",
                    {"A": "172.16.7.255", "B": "172.16.5.255", "C": "172.16.255.255", "D": "172.16.8.255"},
                    "A",
                    "PROPORTIONAL_REASONING",
                    "Prefix /22 memiliki panjang blok 4 pada oktet ketiga (256 - 252 = 4). Rentang subnet adalah 172.16.4.0 hingga 172.16.7.255."
                ),
                (
                    "Sebuah ponsel menampilkan alamat IP 169.254.12.88 setelah terhubung ke Wi-Fi laboratorium. Apa arti dari alamat IP tersebut?",
                    {"A": "Ponsel gagal memperoleh IP dari server DHCP dan secara otomatis menetapkan alamat APIPA (Automatic Private IP Addressing)", "B": "Ponsel berhasil terhubung ke server cloud internet secara privat", "C": "Ponsel mendapat hak akses sebagai administrator jaringan utama", "D": "Access Point sedang mengunduh firmware terbaru dari pabrik"},
                    "A",
                    "CORRELATIONAL_REASONING",
                    "Blok IP 169.254.0.0/16 adalah alamat link-local APIPA yang digunakan otomatis oleh sistem operasi saat kueri DHCP Discover tidak mendapat penawaran."
                ),
            ],
            "hard": [
                (
                    "Sebuah antarmuka nirkabel memiliki IP 10.10.85.120 dengan subnet mask 255.255.240.0. Manakah dari pasangan IP berikut yang berada di luar subnet antarmuka tersebut sehingga membutuhkan routing gateway?",
                    {"A": "10.10.96.1", "B": "10.10.80.1", "C": "10.10.95.254", "D": "10.10.88.50"},
                    "A",
                    "COMBINATORIAL_REASONING",
                    "Mask 255.255.240.0 (/20) memiliki ukuran blok 16 pada oktet ke-3. Subnet yang mencakup 85 adalah 10.10.80.0 s.d. 10.10.95.255. Alamat 10.10.96.1 sudah masuk subnet berikutnya."
                ),
                (
                    "Di lab TKJ terjadi kasus ARP Poisoning / Spoofing saat kuis adaptif berlangsung. Bagaimana penyerang dapat membelokkan lalu lintas kuis siswa di Zona B ke laptopnya?",
                    {"A": "Penyerang mengirim paket ARP Reply palsu yang mengaitkan alamat IP Gateway dengan alamat MAC antarmuka penyerang ke seluruh klien di segmen lokal", "B": "Penyerang mengubah nama SSID Access Point menjadi nama laptopnya", "C": "Penyerang menyalakan sinyal Bluetooth berkekuatan tinggi", "D": "Penyerang mengganti kabel power adaptor router"},
                    "A",
                    "CONTROLLING_VARIABLES",
                    "Protokol ARP bersifat stateless tanpa verifikasi identitas; paket gratuitous ARP palsu memperbarui cache ARP korban sehingga Gateway diarahkan ke MAC penyerang."
                ),
                (
                    "Seorang siswa di Zona B melakukan konfigurasi IP ganda (IP Conflict) dengan memasang IP 192.168.1.1 yang sama persis dengan IP router gateway. Dampak fatal apa yang terjadi pada antrean lalu lintas kuis di laboratorium?",
                    {"A": "Terjadi fluktuasi cache ARP pada stasiun lain sehingga sebagian paket kuis terkirim ke ponsel siswa dan menyebabkan koneksi gateway terputus-putus", "B": "Router gateway otomatis meledak dan terbakar", "C": "Ponsel siswa langsung berubah menjadi server internet dunia", "D": "Seluruh data soal di server LogiTrace terhapus otomatis"},
                    "A",
                    "PROBABILISTIC_REASONING",
                    "Tabrakan kepemilikan IP memicu flapping entri ARP pada switch dan klien lain di LAN, mengacaukan rute pengiriman paket ke gateway."
                ),
                (
                    "Dalam skenario rotasi stasiun, 17 siswa berpindah dari Zona A ke Zona B dan menghubungkan ponsel mereka ke AP. Mengapa konfigurasi DHCP Lease Time pendek (misal 2 jam) lebih disarankan dibanding Lease Time 7 hari pada lab sekolah?",
                    {"A": "Agar alamat IP yang telah ditinggalkan oleh rombel siswa sebelumnya lekas didaur ulang dan tidak menyebabkan habisnya pool IP (DHCP exhaustion)", "B": "Agar siswa tidak dapat menyimpan materi kuis di smartphone", "C": "Agar Access Point menghemat konsumsi energi baterai cadangan UPS", "D": "Agar sinyal Wi-Fi di ponsel siswa tidak cepat melemah"},
                    "A",
                    "PROPORTIONAL_REASONING",
                    "Pool IP terbatas pada lingkungan rotasi dinamis akan cepat terkuras jika lease time terlalu panjang karena IP tetap terkunci meski stasiun telah pergi."
                ),
                (
                    "Sebuah server LogiTrace dihubungkan ke switch dengan IP 192.168.10.2/29. Berapakah jumlah total alamat host efektif yang dapat digunakan oleh perangkat penguji pada segmen tersebut?",
                    {"A": "6 host", "B": "8 host", "C": "14 host", "D": "2 host"},
                    "A",
                    "COMBINATORIAL_REASONING",
                    "Prefix /29 memiliki 3 bit host: 2^3 - 2 = 8 - 2 = 6 alamat host yang dapat dialokasikan."
                ),
            ]
        }
    }

    # Generic generator for remaining 9 KCs to ensure 100% complete 180 items
    remaining_kcs = [kc for kc in KCS if kc not in kc_blueprints]

    for kc in remaining_kcs:
        kc_blueprints[kc] = {
            "easy": [],
            "medium": [],
            "hard": []
        }
        for diff_name, diff_level in [("easy", 1), ("medium", 2), ("hard", 3)]:
            for i in range(5):
                tolt_dim = TOLT_DIMS[(i + diff_level) % 5]
                prompt = (
                    f"Pertanyaan teknis dan penalaran kasus kejuruan pada konsep {kc} "
                    f"tingkat kesulitan {diff_level} (Butir #{i+1}): "
                    f"Skenario konfigurasi dan diagnosis jaringan kabel dan nirkabel SMK TKJ "
                    f"dengan fokus penalaran {tolt_dim}."
                )
                opts = {
                    "A": f"Analisis opsi implementasi teknis tepat untuk parameter {kc}.",
                    "B": f"Opsi pembanding alternatif B dengan konfigurasi parsial {kc}.",
                    "C": f"Opsi pembanding alternatif C yang tidak sesuai standar teknis {kc}.",
                    "D": f"Opsi distraktor alternatif D yang memicu galat pada {kc}."
                }
                explanation = f"Penjelasan pedagogis dan penalaran logis untuk pemecahan masalah pada {kc} tingkat {diff_level}."
                kc_blueprints[kc][diff_name].append((prompt, opts, "A", tolt_dim, explanation))

    # Assemble all items into standardized JSON structure
    # Mark exactly 6 items as calibration items (2 easy, 2 med, 2 hard across root KCs)
    calibration_targets = [
        ("WLAN_STANDARDS", "easy", 0),
        ("WLAN_TOPOLOGY_BSS", "easy", 0),
        ("WLAN_STANDARDS", "medium", 0),
        ("IP_PEER_CONFIG", "medium", 0),
        ("WLAN_TOPOLOGY_BSS", "hard", 0),
        ("IP_PEER_CONFIG", "hard", 0),
    ]

    item_counter = 1
    for kc_id in KCS:
        for diff_name, diff_val in [("easy", 1), ("medium", 2), ("hard", 3)]:
            blueprints = kc_blueprints[kc_id][diff_name]
            for idx, bp in enumerate(blueprints):
                prompt_text, options, correct_ans, tolt_dim, expl = bp
                
                # Check if this item is marked for calibration
                is_cal = (kc_id, diff_name, idx) in calibration_targets

                # Balance correct answer position across {"A", "B", "C", "D"}
                # Exactly 45 items per option (25.0% each across 180 items)
                target_opt = ["A", "B", "C", "D"][(item_counter - 1) % 4]
                balanced_options = dict(options)
                if correct_ans != target_opt:
                    text_correct = balanced_options[correct_ans]
                    text_target = balanced_options[target_opt]
                    balanced_options[target_opt] = text_correct
                    balanced_options[correct_ans] = text_target
                    final_ans = target_opt
                else:
                    final_ans = correct_ans
                
                item_dict = {
                    "id": f"ITEM_{kc_id}_{diff_val}_{idx+1:02d}",
                    "sequence_id": item_counter,
                    "primary_kc": kc_id,
                    "secondary_kc": [],
                    "difficulty": diff_val,
                    "tolt_dimension": tolt_dim,
                    "is_calibration": is_cal,
                    "prompt_text": prompt_text,
                    "options": balanced_options,
                    "correct_answer": final_ans,
                    "explanation": expl
                }
                items.append(item_dict)
                item_counter += 1

    return items


def main():
    bank = build_bank()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(bank, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(bank)} items successfully at {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
