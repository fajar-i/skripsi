# To-Do Lanjutan LogiTrace (per 17 Nov 2026)

Kolom **Siapa**: *Anda* = keputusan atau tindakan Anda; *Pakar* = dosen/guru/validator; *Claude* = bisa saya kerjakan setelah ada keputusan.
Urutan di dalam tiap bagian adalah urutan yang disarankan.

## A. Keputusan yang memblokir pekerjaan lain

| # | Tugas | Siapa | Membuka |
|---|---|---|---|
| A1 | Pastikan kunci 9router lama sudah dicabut. Kalau repo pernah/akan publik, bersihkan `.env` dari riwayat git (commit `5ddd3f5`, mis. dengan `git filter-repo`) | Anda | Keamanan repo |
| A2 | Pilih strategi petunjuk: **petunjuk per butir dibangkitkan di muka** (disarankan) atau LLM real-time dengan batas ±8 s | Anda | B5, D1, D2 |
| A3 | Pastikan penggunaan 9router/akun Antigravity boleh untuk penelitian sekolah, dan catat ke mana data diproses (Google, luar negeri) | Anda | D3 (bagian UU PDP) |
| A4 | Putuskan soal two-tier untuk bank adaptif: sebagian (36–60 butir), penuh (180), atau tidak sama sekali | Anda + dosen | C6 |

## B. Bank soal: kualitas dan kisi-kisi

| # | Tugas | Siapa |
|---|---|---|
| B1 | Telaah draf `apps/logitrace/docs/kisi_kisi_bank_soal.xlsx`: indikator, level C1–C5, fase Jonassen | Anda |
| B2 | Selesaikan 37 catatan telaah: 12 butir kemungkinan di luar cakupan Fase F (ganti), 6 butir salah KC, 19 butir dengan fase Jonassen yang meragukan | Anda (+ Claude untuk draf butir pengganti) |
| B3 | Tambah atau pindahkan butir untuk 6 indikator yang hanya punya 1–2 butir (IND-01.2, 03.1, 04.3, 11.3, 12.1, 12.3) | Anda (+ Claude) |
| B4 | Buat **lembar telaah pakar** (materi, konstruksi, bahasa) dan **skrip Aiken's V + Cohen's κ** dari isian pakar | Claude |
| B5 | Telaah dan validasi isi oleh 2–5 pakar | Pakar |
| B6 | Rencana uji coba empiris di kelas non-sampel: pembagian paket + butir jangkar | Anda + Claude |
| B7 | **Skrip analisis butir**: tingkat kesukaran p, daya pembeda D/point-biserial, efektivitas pengecoh, KR-20 per KC, korelasi butir-total, daftar butir yang harus direvisi | Claude |
| B8 | Laksanakan uji coba, revisi butir, lalu tetapkan tingkat kesulitan `d` dari hasil empiris | Anda |
| B9 | Jalur yang sama (B4–B8) untuk instrumen pre/post-test troubleshooting Form A/B, ditambah uji kesetaraan kedua form | Anda + Claude |
| B10 | Ubah `label_status` butir menjadi `divalidasi_pakar` setelah lolos, lalu ekspor ulang kisi-kisi | Claude |

## C. Produk (aplikasi)

| # | Tugas | Siapa | Syarat |
|---|---|---|---|
| C1 | Skrip pembangkitan 540 petunjuk per butir lewat 9router (opsi dan kunci tidak dikirim, dicek guard, bisa dilanjutkan bila terputus, mencatat model dan tanggal) | Claude | A2 |
| C2 | Urutan sumber petunjuk saat runtime: butir yang sudah disetujui guru → butir yang belum ditinjau (ditandai) → statis per KC; LLM real-time dimatikan secara bawaan | Claude | A2 |
| C3 | Lembar tinjau petunjuk untuk guru (CSV/Excel + rubrik); hasilnya sekaligus menjadi data evaluasi mutu petunjuk | Claude | C1 |
| C4 | Autentikasi guru (token/PIN) dan siswa (PIN sesi) sebelum uji lapangan | Claude | — |
| C5 | Perbarui `docs/03` dan `docs/06` (masih menyebut Ollama), lalu ambil ulang tangkapan layar | Claude (+ Anda untuk tangkapan layar) | C2 |
| C6 | Dukungan two-tier: skema `reasons`, UI dua langkah, skor, dan miskonsepsi di dasbor | Claude | A4 + konten dari Anda |
| C7 | (Opsional) Petunjuk per pengecoh, untuk scaffolding berbasis jawaban salah | Claude | C1, B2 |

## D. Evaluasi dan naskah artikel

| # | Tugas | Siapa | Syarat |
|---|---|---|---|
| D1 | Kalau memilih petunjuk dibangkitkan di muka: hapus Tabel 5 (konkurensi) dan ganti dengan evaluasi mutu petunjuk (rubrik, ≥ 2 penilai, ICC/κ, tingkat kebocoran) | Claude + Pakar | A2, C3 |
| D2 | Kalau tetap real-time: jalankan ulang benchmark 9router dengan batas waktu baru (3 ulangan) dan isi Tabel 5 | Claude | A2 |
| D3 | Lengkapi isian ⟦…⟧ di naskah v2: penjelasan 9router dan penyedia hulu, sitasi pengganti 2 rujukan Indonesia, URL repo + commit hash, pasal UU PDP, CRediT, nama pembimbing | Anda | A3 |
| D4 | Cek DOI: Jung et al. (2025), Jonassen & Hung (2006), Treagust (1988) bila dipakai | Claude | — |
| D5 | Studi simulasi validitas L3 vs BKT, Elo, dan baseline RM 3, dengan siswa sintetis yang penguasaan sebenarnya diketahui (dilaporkan terbuka sebagai simulasi) | Claude | — |
| D6 | Masukkan hasil telaah pakar (B5) dan uji coba (B8) ke naskah setelah tersedia | Claude | B5, B8 |

## E. Skripsi dan administrasi

| # | Tugas | Siapa |
|---|---|---|
| E1 | Selaraskan proposal Bab 1–3: TOLT dihapus, 9router menggantikan Ollama, petunjuk dibangkitkan di muka, rencana E1–E6 dengan data nyata (bukan simulasi) | Anda + Claude |
| E2 | Izin sekolah, persetujuan orang tua/wali, dan protokol data siswa untuk uji lapangan | Anda |
| E3 | Perbarui deskripsi PR #2 (belum menyebut kisi-kisi dan `old/`), lalu tinjau dan merge PR #1 dan #2 | Claude (deskripsi) + Anda (merge) |
