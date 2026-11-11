Berikut adalah **Handoff Document (Dokumen Serah Terima Konsep)** yang dapat Anda simpan dan jadikan panduan utama untuk menyusun proposal skripsi, mengembangkan media web DKT, maupun saat berdiskusi dengan dosen pembimbing.

---

# **HANDOFF DOCUMENT: RENCANA SKRIPSI R&D**

### **1. RINGKASAN PROJEK SKRIPSI**

* **Jenis Penelitian:** *Research and Development* (R&D) — Model ADDIE / 4D.
* **Topik Utama:** Pengembangan Web Evaluasi Formatif Adaptif Berbasis *Deep Knowledge Tracing* (DKT) untuk Meningkatkan *Logical Thinking* Siswa.
* **Masalah Utama Lapangan:** Keterbatasan fasilitas laboratorium komputer sekolah (rasio 1 PC untuk 2 siswa).
* **Solusi Inovatif:** Pemisahan media berbasis peran (*Device-Purpose Split*) menggunakan model **Station Rotation**.

---

### **2. ARCHITECTURE & WORKFLOW PEMBELAJARAN**

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │                    SESI 1: EVALUASI AWAL (10 Menit)                    │
 │  • Media: HP Pribadi Masing-Masing                                    │
 │  • Aktivitas: Seluruh siswa mengerjakan kuis formatif DKT awal         │
 │  • Output: DKT memetakan Knowledge State & Logika Dasar awal individu  │
 └───────────────────────────────────┬────────────────────────────────────┘
                                     │
                    ┌────────────────┴────────────────┐
                    ▼                                 ▼
 ┌──────────────────────────────────────┐ ┌──────────────────────────────┐
 │          STASIUN 1: PRAKTIK          │ │      STASIUN 2: TEORI        │
 │  • Tempat: Lab Komputer              │ │  • Tempat: Meja Kelas        │
 │  • Media: PC Lab (1 PC 1 Siswa)      │ │  • Media: LKS / Paper-Based  │
 │  • Akses: 50% Siswa (Kelompok A)     │ │  • Akses: 50% Siswa (Kel. B) │
 │  • Aktivitas: Praktik/Simulasi       │ │  • Aktivitas: Analisis Kasus │
 └──────────────────┬───────────────────┘ └──────────────┬───────────────┘
                    │                                    │
                    └─────────────────┬──────────────────┘
                                      │
                         [ ROTASI STASIUN - 25 Menit ]
                                      │
 ┌────────────────────────────────────▼───────────────────────────────────┐
 │                   SESI 3: EVALUASI AKHIR (10 Menit)                    │
 │  • Media: HP Pribadi Masing-Masing                                    │
 │  • Aktivitas: Seluruh siswa mengerjakan Kuis Refleksi DKT              │
 │  • Output: DKT memperbarui matriks penguasaan & skor Logical Thinking │
 └────────────────────────────────────────────────────────────────────────┘

```

---

### **3. METODOLOGI PENELITIAN (BAB 3)**

* **Bentuk Desain Uji Coba:** *Quasi-Experimental / Pre-Experimental* dengan pendekatan ***One-Group Counterbalanced Crossover Design***.
* **Subjek:** 1 Kelas Eksperimen (Tanpa Kelas Kontrol Luar). Subjek bertindak sebagai kontrol atas dirinya sendiri (*self-control*).
* **Metode Analisis Data Keefektifan:**
1. **N-Gain Score ($g$):** Membuktikan persentase peningkatan skor *Logical Thinking* (*Pre-Test* vs *Post-Test*).
2. **Paired Sample t-Test / Uji Wilcoxon:** Membuktikan signifikansi perubahan kemampuan siswa sebelum dan sesudah intervensi.
3. **Visualisasi Tracing DKT:** Menampilkan grafik temporal perubahan probabilitas penguasaan materi (*knowledge state*) yang dihasilkan oleh model DKT.



---

### **4. SPESIFIKASI TEKNIS MEDIA WEB DKT**

* **Target Device:** *Smartphone / Mobile-Friendly* (Fully Responsive UI/UX).
* **Fokus Soal DKT:** Ranah kognitif *Logical Thinking* berbasis penalaran (*Tracing Algorithm, Pattern Recognition, Debugging Logic, Analisis Sebab-Akibat*).
* **Algoritma DKT:** Menggunakan model *Probabilistic Neural Network* (RNN/LSTM atau Transformer) yang menerima input sekuensial respons jawaban ($x_t = \{q_t, a_t\}$) untuk memprediksi performa jawaban pada soal berikutnya ($q_{t+1}$).

---

### **5. KEUNGGULAN DESAIN UNTUK SIDANG SKRIPSI (RATIONALE)**

1. **Integritas Data DKT 100% Personal:** Data *log* DKT murni berasal dari pengerjaan individu via HP pribadi (bebas *noise*).
2. **Menjawab Keterbatasan Fasilitas:** Menjadi contoh solusi konkret (*best practice*) bagi sekolah yang kekurangan fasilitas PC tanpa mengorbankan kualitas pembelajaran individual.
3. **Validitas Metodologis:** Desain *Counterbalanced* berhasil mengontrol variabel pengganggu berupa efek urutan (*order effect*) tanpa perlu melanggar hak kesetaraan belajar siswa melalui pembentukan kelas kontrol pasif.

---

### **6. CHECKLIST LANGKAH SELANJUTNYA**

* [ ] Memilih mata pelajaran & materi spesifik (Informatika/Matematika/Sains).
* [ ] Menyusun kisi-kisi *Knowledge Components* (KC) dan bank soal *Logical Thinking*.
* [ ] Mengembangkan arsitektur web/model DKT (R&D Stage: *Design & Development*).
* [ ] Menyusun Modul Ajar / RPP berbasis *Station Rotation*.
* [ ] Membuat draf Bab 1–3 proposal skripsi.