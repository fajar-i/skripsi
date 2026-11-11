**Catatan penting:** Dokumen ini adalah **paper survei** (*survey paper*), bukan paper yang mengembangkan satu model DKT baru dan melakukan eksperimen tunggal. Karena itu, tidak ada satu arsitektur utama yang “dikembangkan” dan tidak ada skor AUC/ACC/RMSE/F1/N-Gain yang dilaporkan.

---

## 1. IDENTITAS PAPER
- **Judul Lengkap:** *A Survey of Knowledge Tracing: Models, Variants, and Applications*
- **Penulis Utama & Tahun:**  
  - Penulis pertama: **Shuanghong Shen**  
  - Penulis lain: Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, Enhong Chen  
  - **Tahun:** Tidak tercantum eksplisit di teks yang diberikan; referensi terbaru yang muncul adalah **2024**.  
- **Nama Jurnal / Konferensi:** Tidak disebutkan eksplisit pada header/teks yang diekstrak. Dokumen berformat IEEE, tetapi nama jurnal/konferensi tidak terlihat.

---

## 2. METODE & ARSITEKTUR MODEL AI / DKT
- **Nama Arsitektur/Model utama yang dikembangkan:**  
  **Tidak ada model baru.** Paper ini adalah survei yang mengusulkan taksonomi KT. Model yang direview:
  - **Bayesian models:** BKT, Dynamic Bayesian Knowledge Tracing (DBKT)
  - **Logistic models:** Learning Factor Analysis (LFA), Performance Factor Analysis (PFA), Knowledge Tracing Machines (KTM)
  - **Deep learning models:**
    - Deep Knowledge Tracing (DKT) berbasis RNN/LSTM
    - Memory-aware KT: DKVMN, SKVMN
    - Attentive KT: SAKT, SAINT, SAINT+, AKT
    - Graph-based KT: GKT, SKT, AGKT
  - **Varian:** individualization before learning, engagement during learning, forgetting after learning, side information across learning

- **Detail Komponen Teknis:**
  - **BKT:** Hidden Markov Model dua-state; parameter \(P(L_0)\), \(P(T)\), \(P(G)\), \(P(S)\). DBKT menggunakan Dynamic Bayesian Network untuk dependensi antar-KC.
  - **Logistic:** LFA/PFA memakai regresi logistik; KTM memakai factorization machines untuk side information.
  - **DKT:** RNN/LSTM dengan hidden state; input one-hot/embedding; output probabilitas jawaban benar.
  - **DKVMN:** key matrix statis + value matrix dinamis; operasi read/write dengan mekanisme erase-followed-by-add.
  - **Attentive KT:** self-attention; SAINT memakai encoder-decoder terpisah untuk exercise dan answer; SAINT+ menambah fitur temporal; AKT memakai embedding Rasch model, monotonic attention, dan exponential decay.
  - **Graph-based KT:** GKT memodelkan KC sebagai graph \(G=(V,E)\); modul aggregate, update, predict; memakai GNN/GRU.

- **Cara Memproses Sekuel Respons Siswa (Input & Output):**
  - Input: \(\mathbf{X} = \{(e_1,k_{e_1},a_1,r_1), \dots, (e_t,k_{e_t},a_t,r_t), \dots\}\)  
    \(e_t\): exercise, \(k_{e_t}\): knowledge concept, \(a_t\): benar/salah, \(r_t\): side information.
  - Output: estimasi **knowledge state** siswa dan/atau **probabilitas jawaban benar pada exercise berikutnya**.

---

## 3. DOMAIN KOGNITIF & KNOWLEDGE COMPONENTS (KC)
- **Domain Kognitif Spesifik:** **Umum / multi-domain**  
  Survei mencakup matematika, engineering, English, dan programming.
- **Definisi/Pemetaan KC:**
  - Setiap exercise terkait dengan KC tertentu.
  - Di ASSISTments, KC disebut *skill*.
  - Contoh KC pada Fig. 1: *equality, inequality, plane vector, probability*.
  - KC dapat bersifat independen (Bayesian), pre-defined, atau ditemukan otomatis oleh model deep learning.
  - Pada GKT, hubungan antar-KC dimodelkan sebagai edge dalam graph.
  - Pada CodeWorkout, setiap exercise memiliki KC unik.

---

## 4. DATASET & EKSPERIMEN
Paper survei ini **tidak melakukan eksperimen baru**. Ia merangkum dataset yang tersedia untuk evaluasi KT pada **Table II**.

| Dataset | Siswa | Exercise | KC | Learning Records |
|---|---:|---:|---:|---:|
| ASSISTments2009 | 4.163 | 17.751 | 123 | 346.860 |
| ASSISTments2012 | 46.674 | 179.999 | 265 | 6.123.270 |
| ASSISTments2015 | 19.917 | tidak dicantumkan | 100 | 708.631 |
| ASSISTments2017 | 1.709 | 3.162 | 102 | 942.816 |
| Junyi | 247.606 | 722 | 41 | 25.925.922 |
| Eedi2020 | 118.971 | 27.613 | 388 | 15.867.850 |
| Statics2011 | 335 | 1.224 | 80 | 361.092 |
| EdNet-KT1 | 784.309 | 13.169 | 188 | 95.293.926 |
| EdNet-KT2 | 297.444 | 13.169 | 188 | 56.360.602 |
| EdNet-KT3 | 297.915 | 13.169 | 293 | 89.270.654 |
| EdNet-KT4 | 297.915 | 13.169 | 293 | 131.441.538 |
| CodeWorkout | 819 | 50 | 50 | >130.000 |

---

## 5. METRIK PERFORMA KUANTITATIF
- **AUC:** Tidak dilaporkan.
- **Accuracy / RMSE / F1-Score:** Tidak dilaporkan.
- **Dampak Kognitif / N-Gain:** Tidak ada uji coba ke siswa yang dilaporkan.
- Alasan: Penulis secara eksplisit menyatakan **tidak membandingkan performa model KT** karena setting eksperimen tiap studi berbeda, dataset berbeda, dan tidak ada satu model KT yang selalu terbaik.

---

## 6. TEMUAN UTAMA & RESEARCH GAP
- **Temuan Utama:**
  - KT dikelompokkan menjadi tiga model fundamental: **Bayesian, Logistic, Deep Learning**.
  - Varian KT dikelompokkan menjadi empat: **individualization, engagement, forgetting, side information**.
  - Deep learning unggul dalam prediksi performa, tetapi **interpretabilitas dan explainability** masih rendah.
  - Tidak ada model KT tunggal yang selalu terbaik di semua konteks.
  - Penulis merilis dua library: **EduData** dan **EduKTM**.

- **Keterbatasan / Research Gap yang Diakui:**
  - Interpretabilitas model KT, terutama deep learning, masih sulit.
  - Data sparsity / sedikit interaksi belajar.
  - Exercise subjektif dan jawaban open-ended belum banyak ditangani.
  - Umpan balik siswa (*students’ feedback*) belum banyak dimanfaatkan.
  - Peluang untuk **general user modeling** dan integrasi **Large Language Models (LLM)**.
  - Keterbatasan survei: mungkin ada karya representatif yang terlewat; kompleksitas model dapat menurunkan aplikabilitas.