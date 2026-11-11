Dokumen **Handoff Desain** ini dirancang sebagai jembatan komunikasi antara **UI/UX Designer, AI Data Scientist, dan Software Engineer (Frontend/Backend)** untuk mengimplementasikan sistem *Deep Knowledge Tracing* (DKT) ke dalam media pembelajaran adaptif.

---

# 📑 MOCKUP HANDOFF DESAIN: SYSTEM DKT ADAPTIF

## 1. Arsitektur Data & Peta Komponen (Component Mapping)

| Elemen UI | Sumber Data / API Input | Trigger Action | Respon Sistem / AI |
| --- | --- | --- | --- |
| **Soal/Kuis Formatif** | `GET /api/v1/next-item` | Siswa submit jawaban (`0` atau `1`) | DKT menghitung $h_t$ & $y_{t+1}$ |
| **Progress Bar Mastery** | Probabilitas DKT ($y_t \in [0, 1]$) | Update otomatis per interaksi | Visualisasi nilai mastery ($0-100\%$) |
| **Pop-up Scaffolding** | Conditions: $y_t < 0.30$ | Auto-trigger saat salah beruntun | Menampilkan *Hint* / Rangkuman SOP |
| **Modal Intervensi Video** | Conditions: 3x Salah Beruntun | Auto-modal popup | Sesi kuis dipause $\rightarrow$ Wajib tonton video |
| **Alert Dasbor Guru** | Conditions: $y_t < 0.20$ & Status: *Stuck* | Push notification ke WebSocket | Guru menerima notifikasi "Siswa Butuh Bantuan" |

---

## 2. Alur Pengalaman Pengguna (UX Flow Logic)

```
[Siswa Jawab Soal (t)] ──► [Submit Jawaban] ──► [Kirim Payload Ke DKT]
                                                     │
                                                     ▼
                                       [Hitung Prediksi DKT (yt+1)]
                                                     │
          ┌──────────────────────────────────────────┼──────────────────────────────────────────┐
          ▼                                          ▼                                          ▼
   [yt+1 >= 0.80]                             [0.40 <= yt+1 < 0.80]                       [yt+1 < 0.40]
   Status: HIGH MASTERY                        Status: MODERATE                            Status: LOW / STUCK
          │                                          │                                          │
          ▼                                          ▼                                          ▼
Tampilkan Soal Lebih Sulit /               Tampilkan Soal Standar                      Beri Scaffolding (Hint/SOP)
Modul Pengayaan (Advanced)                 (Practice Mode)                             
                                                                                                │
                                                                                 [Jika 3x Salah Berturut-turut]
                                                                                                │
                                                                                                ▼
                                                                                   1. Tampilkan Video Remedi
                                                                                   2. Kirim Alert ke Dasbor Guru

```

---

## 3. Spesifikasi UI & Rule Logic (Desain Antarmuka Siswa)

### A. Indikator Penguasaan Materi (Mastery Progress Widget)

* **Karakteristik UI:** Bar/Gauge Chart dinamis di bagian atas layar kuis.
* **Logic Color State:**
* 🔴 **Merah (`#E53935`):** Mastery $0\% - 39\%$ (*Memerlukan Bantuan*)
* 🟡 **Kuning (`#FDD835`):** Mastery $40\% - 79\%$ (*Cukup / Berkembang*)
* 🟢 **Hijau (`#43A047`):** Mastery $80\% - 100\%$ (*Sangat Menguasai*)


* **Micro-copy Text:**
* Low: *"Mari ulangi konsep dasar sebentar!"*
* Moderate: *"Kerja bagus, teruskan latihan!"*
* High: *"Luar biasa! Kamu siap untuk tantangan berikutnya."*



### B. State Kartu Soal (Dynamic Question Card)

* **Tingkat Kesulitan Visual:**
* **Level Mudah:** Chip Hijau (`Tingkat: Dasar`)
* **Level Sedang:** Chip Biru (`Tingkat: Menengah`)
* **Level Sulit:** Chip Ungu (`Tingkat: Lanjutan / HOTS`)


* **Tombol Bantuan (Hint Button):**
* *Default:* Terkunci / Muted.
* *Active:* Menyala otomatis jika DKT memprediksi probabilitas siswa benar $< 40\%$.



### C. Modal Intervensi Remedi (Video/Materi Pop-up)

* **Trigger Condition:** Siswa mengalami **3x kesalahan berturut-turut** pada skill ID yang sama.
* **Behavior:**
* Layar kuis di-*freeze* (tidak bisa *submit* jawaban baru).
* Modal bermunculan: *"Sistem mendeteksi kamu mengalami kesulitan pada langkah ini. Yuk, tonton penjelasan 2 menit berikut!"*
* Tombol *"Lanjut Kuis"* baru aktif setelah video selesai diputar (*minimum 80% duration*).



---

## 4. Spesifikasi UI Dasbor Guru (Teacher Intervention Dashboard)

### A. Kartu Pantauan *Real-Time* Kelas (Live Monitoring Card)

* **Indikator Siswa *Stuck* (Critical Badge):**
* Badge Merah Kedap-Kedip: `[!] MEMBUTUHKAN BANTUAN TANGAN (STUCK)`
* Parameter Filter: Terpemicu jika $y_t < 0.20$ selama $> 10$ menit di kelas.


* **Aksi Cepat Guru (Quick Action Buttons):**
* `[Buka Detail Log]` $\rightarrow$ Melihat urutan histori soal yang dijawab salah oleh siswa.
* `[Tandai Sudah Dibantu]` $\rightarrow$ Mereset *alert* di dasbor setelah guru mendatangi meja siswa.



---

## 5. Contract API (Spesifikasi Integrasi Developer)

### A. Payload Input (Client $\rightarrow$ DKT Backend)

Sistem UI harus mengirimkan payload JSON ini setiap kali siswa menekan tombol **Submit**:

```json
{
  "student_id": "STD_10923",
  "session_id": "SES_8821",
  "timestamp": "2026-09-19T13:10:00Z",
  "interaction": {
    "question_id": "Q_TKJ_SUB_04",
    "concept_skill_id": "SKILL_SUBNETTING_VLSM",
    "correctness": 0,
    "response_time_seconds": 45,
    "hint_used": true
  }
}

```

### B. Response Payload (DKT Backend $\rightarrow$ Client UI)

Backend DKT akan mengembalikan data berikut untuk menentukan perubahan UI secara instan:

```json
{
  "student_id": "STD_10923",
  "updated_mastery_score": 0.32,
  "predicted_next_correctness": 0.35,
  "recommended_action": {
    "action_type": "TRIGGER_SCAFFOLDING",
    "next_question_id": "Q_TKJ_SUB_02_EASY",
    "interventions": {
      "show_hint": true,
      "force_remedial_video": true,
      "video_url": "https://cdn.school.id/remedial/vlsm-basic.mp4",
      "notify_teacher_stuck": true
    }
  }
}

```

---

## 6. Catatan Khusus untuk Developer (Edge Cases Handling)

1. **Kondisi Offline / Koneksi Terputus:**
Jika koneksi internet siswa terputus saat submit, UI harus menyimpan interaksi ke dalam **Local Storage / IndexedDB** dan menampilkan soal cadangan berstatus `MODERATE`. Sync data DKT dilakukan saat koneksi pulih.
2. **Cold-Start (Siswa Baru Tanpa Histori):**
Untuk 3 soal pertama, kuis diberikan dengan tingkat kesulitan standar (`MODERATE`) secara statis sambil DKT mengisi nilai *initial state* ($h_0$).