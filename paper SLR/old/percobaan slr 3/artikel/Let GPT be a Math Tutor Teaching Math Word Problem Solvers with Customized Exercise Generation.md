Berikut adalah rangkuman menyeluruh dari paper ini yang disajikan secara terstruktur dan mudah dipahami.

---

### 1. Masalah Utama yang Ingin Diselesaikan

* **LLM Raksasa Terlalu Boros:** Model AI besar seperti GPT-3 atau PaLM sangat jago menyelesaikan soal cerita matematika (*Math Word Problems* / MWP). Namun, ukurannya yang raksasa membuat biaya operasinya mahal, lambat, dan tidak hemat energi.


* **Cara Melatih AI Kecil yang Lama Kurang Efektif:** Metode distilasi biasa biasanya memaksa AI kecil meniru "langkah-langkah penjelasan" (*Chain-of-Thought*) dari AI besar. Masalahnya, AI kecil sering kali tidak mampu mencerna logika rumit tersebut, dan tidak ada umpan balik jika AI kecil mengalami kesulitan.



---

### 2. Solusi: Metode CEMAL (*Customized Exercise for MAth Learning*)

Peneliti membuat metode baru bernama **CEMAL** yang meniru hubungan **Guru dan Murid di dunia nyata**:

* **AI Guru (GPT-3.5):** Berukuran raksasa, tugasnya **bukan menjawab soal**, melainkan **membuat soal latihan** yang disesuaikan.


* **AI Murid (Model Kecil / RoBERTa + GTS):** Berukuran jauh lebih ringan (~377M parameter), tugasnya **belajar membaca cerita dan menjawab soal** tersebut hingga menghasilkan rumus matematika yang tepat.



---

### 3. Cara Kerja Sistem (Alur "Les Privat" AI)

```
[1. Buat Buku Latihan] ---> [2. AI Murid Diuji] ---> [3. Lacak Soal yang Salah]
                                                                  |
[5. AI Murid Makin Pintar] <-- [4. GPT Buat Soal Baru] <----------+

```

1. **Pembuatan Buku Latihan (*Exercise Book*):** Di awal, GPT-3.5 membuat ribuan variasi soal latihan untuk dijadikan lembar evaluasi.


2. **Ujian Diagnostik (*Knowledge Tracing*):** Di tengah masa pelatihan, AI Murid diminta mengerjakan *exercise book* tersebut.


3. **Mendeteksi Kelemahan:** Sistem secara otomatis memisahkan soal-soal yang gagal dijawab oleh AI Murid.


4. **Pembuatan Soal Khusus (*Personalized Learning*):** Soal yang salah tadi diserahkan ke GPT-3.5. GPT akan membuatkan **soal-soal latihan baru yang polanya mirip** (mengubah jalan cerita atau struktur angka) khusus untuk melatih area kelemahan AI Murid tersebut.


5. **Pelatihan Bertahap (*Progressive Learning*):** Soal-soal baru ini dimasukkan ke materi belajar AI Murid, sehingga kemampuan AI Murid meningkat secara bertahap.



---

### 4. Tingkat Kesulitan Soal

Soal yang dipelajari berada pada tingkat **Aritmatika & Aljabar Dasar (SD–SMP)**, seperti pada dataset MAWPS, ASDiv-a, dan SVAMP.

Tantangan utamanya bukan pada perhitungan angka yang rumit, melainkan pada **kemampuan bahasa alami**: AI Murid harus bisa memahami konteks cerita, mengabaikan informasi pengecoh, dan menerjemahkan kalimat menjadi rumus matematika yang tepat.

---

### 5. Hasil Akhir dan Keunggulan

* **Sangat Akurat:** AI Murid hasil metode CEMAL mencapai akurasi **76.4%–85.4%** pada dataset pengujian SVAMP. Angka ini jauh mengungguli metode pelatihan AI kecil biasa (47.3%).


* **Mengalahkan / Setara AI Raksasa:** AI Murid yang ukurannya ratusan kali lebih kecil ini bahkan sanggup mengimbangi atau melampaui akurasi model raksasa seperti GPT-3 + CoT (69.2%) dan PaLM + CoT (78.5%).


* **Sangat Ringan:** Hasil akhirnya adalah model AI pemecah soal matematika yang **seringkas kalkulator** (dibanding LLM raksasa), namun **paham logika bahasa cerita matematika dengan sangat akurat**.