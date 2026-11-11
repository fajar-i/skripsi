Berikut penjelasan **tiap model** yang dibahas dalam paper survei tersebut dengan bahasa yang sederhana dan tidak terlalu teknis.

---

## Model Bayesian

### 1. Bayesian Knowledge Tracing (BKT)
Bayangkan siswa hanya punya dua status untuk setiap konsep: **sudah paham** atau **belum paham**.  
BKT memperhitungkan:
- Peluang siswa menebak benar walaupun belum paham (*guess*).
- Peluang siswa salah walaupun sebenarnya sudah paham (*slip*).
- Peluang siswa berubah dari belum paham menjadi paham setelah belajar (*transition*).

BKT tidak mempertimbangkan lupa. Model ini sederhana, mudah dijelaskan, dan menjadi dasar banyak model KT.

### 2. Dynamic Bayesian Knowledge Tracing (DBKT)
DBKT adalah pengembangan BKT. Kalau BKT menganggap setiap konsep berdiri sendiri, DBKT menganggap konsep-konsep itu **saling berhubungan**.  
Misalnya, untuk menguasai konsep C, siswa harus menguasai konsep A dan B terlebih dahulu. Jadi DBKT memperhitungkan hubungan prasyarat antar konsep.

---

## Model Logistik

### 3. Learning Factor Analysis (LFA)
LFA memprediksi peluang siswa menjawab benar dengan rumus logistik. Faktor yang diperhitungkan:
- Kemampuan awal siswa.
- Tingkat kemudahan konsep.
- Kecepatan belajar konsep.

Semakin sering siswa berlatih, semakin besar peluang menjawab benar.

### 4. Performance Factor Analysis (PFA)
PFA mirip LFA, tetapi lebih fokus pada **riwayat benar/salah** siswa pada konsep tertentu.  
Jumlah keberhasilan dan kegagalan sebelumnya dipakai untuk memprediksi jawaban berikutnya. PFA lebih sensitif terhadap performa nyata siswa.

### 5. Knowledge Tracing Machines (KTM)
KTM memakai teknik *factorization machines*. Model ini bisa memasukkan banyak informasi tambahan: data siswa, exercise, konsep, dan informasi lain.  
KTM mencari pola hubungan antar fitur tersebut. Karena fleksibel, KTM sering dipakai untuk menggabungkan berbagai jenis data.

---

## Model Deep Learning

### 6. Deep Knowledge Tracing (DKT)
DKT adalah model pertama yang memakai **jaringan saraf berulang (RNN/LSTM)** untuk KT.  
Cara kerjanya seperti membaca cerita dari awal sampai akhir: model mengingat urutan jawaban siswa, lalu memperkirakan jawaban berikutnya.  
DKT kuat dalam prediksi, tetapi sulit dijelaskan karena keputusannya tersembunyi di dalam jaringan.

### 7. Memory-aware Knowledge Tracing
Model ini menambahkan **memori eksternal** agar lebih mudah dijelaskan.
- **DKVMN (Dynamic Key-Value Memory Networks):**  
  Ada dua memori: satu untuk menyimpan daftar konsep (*key*), satu untuk menyimpan tingkat penguasaan siswa (*value*).  
  Setiap kali siswa menjawab, memori dibaca dan diperbarui. Konsep yang salah bisa “dilupakan” sedikit, yang benar bisa “diperkuat”.
- **SKVMN (Sequential Key-Value Memory Network):**  
  Menggabungkan kekuatan DKT dan DKVMN. SKVMN bisa mengingat hubungan jangka panjang antar interaksi belajar.

### 8. Attentive Knowledge Tracing
Model ini memakai **mekanisme attention**, seperti pada Transformer. Intinya, model melihat kembali interaksi masa lalu yang paling relevan untuk memprediksi jawaban sekarang.
- **SAKT:** Menerapkan Transformer langsung ke KT.
- **SAINT:** Memisahkan proses belajar exercise dan jawaban, lalu menyusunnya berlapis-lapis.
- **SAINT+:** Menambahkan informasi waktu, seperti lama menjawab dan jeda antar soal.
- **AKT (Context-aware Attentive Knowledge Tracing):** Menggabungkan attention dengan model psikometri Rasch. AKT juga memperhitungkan peluruhan pengetahuan seiring waktu. Model ini lebih kontekstual dan lebih mudah diinterpretasi.

### 9. Graph-based Knowledge Tracing
Model ini menganggap konsep-konsep pengetahuan sebagai **graph** (jaringan): titik adalah konsep, garis adalah hubungan antar konsep.
- **GKT (Graph-based Knowledge Tracing):**  
  Pengetahuan siswa diperbarui berdasarkan konsep itu sendiri dan konsep-konsep tetangganya di graph.
- **SKT (Structure-based Knowledge Tracing):**  
  Mempertimbangkan **transfer pengetahuan** antar konsep. Jadi saat siswa belajar satu konsep, konsep lain yang berhubungan juga ikut terpengaruh.
- **AGKT (Automatic Graph-based Knowledge Tracing):**  
  Sama seperti GKT, tetapi graph-nya dibangun otomatis tanpa perlu anotasi manual.

---

## Varian Model KT (Tambahan)
Paper ini juga membahas pengembangan dari model-model di atas:
- **Individualization:** Menyesuaikan model dengan karakter tiap siswa (kemampuan awal, kecepatan belajar).
- **Engagement:** Memasukkan tingkat keterlibatan siswa, misalnya dari perilaku menonton video atau menjawab soal.
- **Forgetting:** Memperhitungkan bahwa siswa bisa lupa seiring waktu.
- **Side Information:** Memanfaatkan informasi tambahan seperti waktu respons, bantuan tutor, atau teks soal.

---

## Kesimpulan Sederhana
- **Bayesian & Logistik:** Lebih sederhana, mudah dijelaskan, tetapi kemampuan prediksinya terbatas.
- **Deep Learning:** Prediksinya lebih akurat, tetapi sering dianggap “kotak hitam” dan sulit diinterpretasi.
- **Tidak ada satu model terbaik mutlak.** Model yang tepat bergantung pada data, konteks, dan kebutuhan aplikasi.