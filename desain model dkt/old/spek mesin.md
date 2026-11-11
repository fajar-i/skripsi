Spesifikasi mesin/server yang dibutuhkan untuk mengembangkan dan menjalankan model **Custom DKT (LSTM/Transformer)** terbagi menjadi 2 kebutuhan: **Kebutuhan Pengembangan/Pelatihan (*Training*)** dan **Kebutuhan Server Produksi/Inference (*Deployment*)**.

Kabar baiknya, karena DKT bekerja pada data sekuens numerik/vektor (bukan data gambar besar atau video), **kebutuhan spesifikasinya sangat efisien dan jauh lebih ringan** dibandingkan melatih model LLM atau Vision.

---

## 1. Spesifikasi untuk Pelatihan Model (*Training Specs*)

Dibutuhkan saat Anda melatih model DKT dari nol menggunakan dataset (seperti ASSISTments, EdNet, atau data lokal).

| Komponen | Spesifikasi Minimal (Cukup) | Spesifikasi Rekomendasi (Ideal) |
| --- | --- | --- |
| **GPU** | **NVIDIA GTX 1650 / RTX 3050** (4 GB VRAM) atau **Google Colab Free Tier (T4 GPU)** | **NVIDIA RTX 3060 / 4060** (8–12 GB VRAM) |
| **CPU** | 4 Cores (Intel i5 / AMD Ryzen 5) | 8 Cores (Intel i7 / AMD Ryzen 7) |
| **RAM** | 8 GB DDR4 | 16 GB – 32 GB DDR4/DDR5 |
| **Storage** | 100 GB SSD (NVMe disarankan) | 250 GB NVMe SSD |

> 💡 **Tips Hemat:** Anda **tidak wajib membeli laptop/PC GPU mahal**. Anda bisa memanfaatkan **Google Colab (Gratis)** atau **Kaggle Notebooks (Gratis)** yang menyediakan akses GPU NVIDIA T4 secara cuma-cuma. Proses latihan DKT untuk ~50.000 data interaksi biasanya selesai dalam waktu **15–30 menit saja** di Colab.

---

## 2. Spesifikasi Server Produksi (*Deployment / Live Server Specs*)

Dibutuhkan saat model DKT yang sudah dilatih di-export ke format **ONNX** dan dihubungkan ke aplikasi web/LMS sekolah untuk diuji ke siswa.

### Skala 1: Pengujian Sekolah / Uji Eksperimen (100–500 Siswa Aktif)

* **Hosting:** Cloud VPS Murah (DigitalOcean, Biznet Gio, Linode, atau AWS EC2 t3.medium)
* **CPU:** 2 vCPU
* **RAM:** 4 GB
* **Storage:** 20–40 GB SSD
* **GPU:** **TIDAK BUTUH GPU** (Model ONNX/PyTorch DKT sangat ringan, CPU biasa mampu memproses prediksi $< 20\text{ ms}$).
* **Estimasi Biaya Server:** Rp 150.000 – Rp 300.000 / bulan (atau gunakan PC lokal di sekolah sebagai server).

### Skala 2: Produksi Skala Luas (5.000+ Siswa Aktif Bersamaan)

* **CPU:** 4–8 vCPU
* **RAM:** 8–16 GB
* **Infrastruktur TAMBAHAN:**
* **Redis Server (RAM 2–4 GB):** Khusus untuk menyimpan *Hidden State* ($h_t$) interaksi siswa secara *real-time*.


* **Estimasi Biaya Server:** Rp 600.000 – Rp 1.200.000 / bulan.

---

## 3. Komposisi Software/Stack Lingkungan Kerja

Untuk memastikan spesifikasi di atas berjalan optimal, gunakan lingkungan eksekusi (*tech stack*) berikut:

* **OS:** Ubuntu 22.04 LTS (disarankan untuk server) atau Windows 11 / macOS (untuk laptop dev).
* **Python Version:** Python 3.10 / 3.11
* **ML Framework:** PyTorch 2.x + ONNX Runtime (ONNX Runtime membuat prediksi CPU 3x lebih cepat dibanding PyTorch standar).
* **Inference Server:** FastAPI + Uvicorn + Redis.

---

## Ringkasan Kebutuhan

1. **Untuk Bikin & Latih Model:** Pakai **Google Colab Gratis** (0 Rupiah).
2. **Untuk Server Aplikasi ke Siswa:** Cukup sewa **VPS CPU 2 vCPU / 4 GB RAM** (± Rp 150 rb/bln) atau manfaatkan komputer server/laptop sekolah biasa.