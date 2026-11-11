Dokumen **Handoff Desain Arsitektur & Model DKT** ini ditujukan khusus untuk **AI/ML Engineer, Data Engineer, dan Backend Developer**. Dokumen ini mengatur spesifikasi teknis model, proses pemrosesan data, pelatihan (*training*), hingga *deployment* ke dalam lingkungan produksi (*production environment*).

---

# 🧠 HANDOFF DESAIN MODEL AI: DEEP KNOWLEDGE TRACING (DKT)

## 1. Arsitektur Model AI (Model Architecture Specification)

Sistem menggunakan arsitektur **DKT berbasis LSTM dengan Attention Mechanism (Attentive DKT / DKT-LSTM)** untuk menjaga keseimbangan antara performa akurasi ($AUC > 0{,}80$) dan latensi prediksi yang sangat rendah ($< 50\text{ ms}$).

```
[Input Vector x_t] ──► [Embedding Layer] ──► [LSTM Layer] ──► [Attention Layer] ──► [Dense / Sigmoid Layer] ──► [Output y_t]

```

### Spesifikasi Layer Networks:

| Layer | Tipe / Spesifikasi | Ukuran Output / Dimensi | Fungsi & Keterangan |
| --- | --- | --- | --- |
| **Input Layer** | One-Hot Vector $x_t = (q_t, r_t)$ | $2 \times \vert{}Q\vert{}$ | Penggabungan ID Soal/Konsep ($q_t$) dan Kebenaran ($r_t \in \{0, 1\}$). |
| **Embedding Layer** | Continuous Linear Embedding | Dimensi = $128$ | Memetakan sparse vector menjadi dense representation. |
| **Recurrent Layer** | Stacked LSTM (2 Layers) | Hidden units = $256$ | Mengingat pola sekuensial belajar dan efek keterlupaan siswa. |
| **Dropout Layer** | Dropout Rate = $0.3$ | Dimensi = $256$ | Mencegah *overfitting* pada dataset siswa yang kecil. |
| **Attention Layer** | Bahdanau / Dot-Product Attention | Dimensi = $256$ | Memberikan bobot lebih pada latihan masa lalu yang relevan dengan soal saat ini. |
| **Output Layer** | Dense + Activation Sigmoid | $\vert{}Q\vert{}$ (Jumlah Konsep) | Mengeluarkan probabilitas penguasaan ($y_t \in [0, 1]$) untuk tiap konsep. |

---

## 2. Formulasi Matematis & Pemrosesan Data (Data Pipeline)

### A. Vektor Input ($x_t$)

Jika terdapat $M$ jenis konsep/keterampilan (*Skill IDs*), vektor input $x_t$ pada langkah ke-$t$ direpresentasikan sebagai *one-hot vector* berukuran $2M$:


$$x_t = q_t + r_t \times M$$

* $q_t$: Index ID Konsep ($0 \le q_t < M$)
* $r_t$: Kebenaran Jawaban ($0$ jika Salah, $1$ jika Benar)

### B. Pembaruan State & Prediksi Output

$$\begin{aligned} h_t &= \text{LSTM}(e(x_t), h_{t-1}) \quad \text{dimana } e(\cdot) \text{ adalah Embedding Layer} \\ c_t &= \text{Attention}(h_t, H_{1:t-1}) \\ y_t &= \sigma(W_y \cdot [h_t; c_t] + b_y) \end{aligned}$$


Nilai $y_{t}[k]$ mewakili perkiraan probabilitas bahwa siswa akan menjawab **benar** jika diberikan soal yang berkaitan dengan Konsep $k$ pada interaksi berikutnya.

---

## 3. Strategi Pelatihan Model (Training Setup)

### A. Dataset & Pre-processing

* **Dataset Pre-training:** ASSISTments / EdNet / Data Histori Lokal Sekolah.
* **Sequence Padding:** Maksimum panjang sekuens interaksi dikunci pada $N = 100$ langkah terakhir (`max_len = 100`). Sekuens yang lebih pendek diberi *padding* $0$.
* **Train / Val / Test Split:** $80\% / 10\% / 10\%$ berdasarkan **Student ID Split** (bukan random row split untuk mencegah *data leakage* antar-siswa).

### B. Hyperparameters & Optimization

* **Loss Function:** *Binary Cross-Entropy Loss* (diukur hanya pada posisi konsep yang diuji di $t+1$):

$$\mathcal{L} = -\sum_t \left( r_{t+1} \log y_t^{q_{t+1}} + (1 - r_{t+1}) \log (1 - y_t^{q_{t+1}}) \right) + \lambda \mathcal{L}_{\text{smoothness}}$$


* **Optimizer:** Adam Optimizer ($\text{Learning Rate} = 0.001$, $\text{Weight Decay} = 1\text{e-}5$).
* **Batch Size:** $64$ (saat offline training).
* **Early Stopping:** Patience = 10 epochs berdasarkan *Validation Loss*.

---

## 4. Ambang Batas Logika Sistem (Threshold & Rulemaking)

Untuk menentukan aksi intervensi di antarmuka (UI), backend AI memetakan nilai $y_t$ menjadi *categorical state* sebagai berikut:

```python
# Rule Engine untuk Output DKT
def determine_adaptive_action(y_t_predicted, consecutive_failures):
    if consecutive_failures >= 3:
        return {
            "state": "STUCK",
            "action": "TRIGGER_REMEDIAL_VIDEO_AND_ALERT_TEACHER",
            "next_difficulty": "EASY"
        }
    
    if y_t_predicted >= 0.80:
        return {
            "state": "HIGH_MASTERY",
            "action": "SERVE_ADVANCED_QUESTION",
            "next_difficulty": "HARD"
        }
    elif 0.40 <= y_t_predicted < 0.80:
        return {
            "state": "MODERATE",
            "action": "SERVE_PRACTICE_QUESTION",
            "next_difficulty": "MEDIUM"
        }
    else:
        return {
            "state": "LOW_MASTERY",
            "action": "SERVE_SCAFFOLDING_AND_HINT",
            "next_difficulty": "EASY"
        }

```

---

## 5. Spesifikasi Infrastruktur & Deployment (MLOps)

```
[User Client] ──► [API Gateway (FastAPI)] ──► [Redis Cache (State h_t)] ──► [Triton / ONNX Runtime]
                                                                                   │
                                                                                   ▼
                                                                        [DKT Model Inference]

```

1. **Format Model Export:**
Model PyTorch yang telah selesai dilatih wajib di-export ke format **ONNX (Open Neural Network Exchange)** untuk memaksimalkan kecepatan prediksi pada CPU/GPU server.
2. **Manajemen Hidden State ($h_t$ Cache):**
* Agar tidak perlu menghitung ulang sekuens dari awal setiap kali siswa menjawab $1$ soal, simpan *Hidden State* ($h_t$) dan *Cell State* ($c_t$) terakhir siswa di dalam **Redis Cache** dengan TTL (Time-To-Live) $24$ jam.
* *Inference Latency Target:* $\le 30\text{ ms}$ per permintaan interaksi.


3. **Monitoring & Logging:**
* Simpan *log* histori `(student_id, question_id, correctness, y_t_predicted)` ke dalam database PostgreSQL / BigQuery secara *asynchronous* (menggunakan *Message Queue* seperti Celery / RabbitMQ) untuk bahan *retraining* model secara berkala.