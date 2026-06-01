# 🎓 Hybrid DSS — Beasiswa Studi Luar Negeri

Dashboard Streamlit untuk **Hybrid Decision Support System** rekomendasi peserta beasiswa studi luar negeri menggunakan metode **Random Forest** (ML) dan **TOPSIS** (MCDM).

---

## 📋 Informasi Tugas

| Item | Detail |
|------|--------|
| **Nama / NIM** | Novi Maharani Br Surbakti / 235150400111011 |
| **Kelas** | SPK SI-D |
| **Studi Kasus** | Rekomendasi Peserta Beasiswa Studi Luar Negeri |
| **Dataset** | Students Performance (800 siswa) |
| **Metode ML** | Random Forest Classifier |
| **Metode MCDM** | TOPSIS |

---

## 🚀 Cara Deploy ke Streamlit Community Cloud

### 1. Fork / Upload ke GitHub
Upload file `app.py` dan `requirements.txt` ke repository GitHub baru.

### 2. Deploy di Streamlit Cloud
1. Buka [share.streamlit.io](https://share.streamlit.io)
2. Klik **New app**
3. Pilih repository GitHub kamu
4. Set **Main file path** → `app.py`
5. Klik **Deploy!**

---

## 🖥️ Jalankan Lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📱 Fitur Dashboard

| Halaman | Deskripsi |
|---------|-----------|
| 🏠 Dashboard | KPI utama, ringkasan sistem, top 5 kandidat |
| 📊 Eksplorasi Data | Statistik deskriptif, distribusi, korelasi |
| 🤖 Model ML | Confusion matrix, ROC curve, feature importance |
| 🏆 Ranking TOPSIS | Ranking lengkap 7 kriteria berbobot |
| ⚡ Hybrid & Hasil | Scatter, distribusi, kandidat utama & cadangan |
| 🔍 Cek Siswa | Input manual + radar chart profil siswa |

---

## ⚙️ Konfigurasi Sidebar

- **Kuota Beasiswa** (5–30 siswa) — dapat diubah dinamis
- **Bobot TOPSIS vs ML** — slider real-time (otomatis total = 1.0)

---

## 🏗️ Arsitektur Sistem

```
Dataset (800 siswa)
    ↓
EDA + Feature Engineering
    ↓
┌─────────────────────────────┐
│   Random Forest Classifier  │  → Probabilitas Kelayakan
└─────────────────────────────┘
            +
┌─────────────────────────────┐
│   TOPSIS (7 kriteria)       │  → Skor & Ranking MCDM
└─────────────────────────────┘
            ↓
   Skor Hybrid = 0.6×TOPSIS + 0.4×ML
            ↓
   Rekomendasi Akhir (4 kategori)
```

---

## 📦 Dependensi

```
streamlit, pandas, numpy, scikit-learn, imbalanced-learn, plotly
```

---

## 📊 Kategori Rekomendasi

| Kategori | Kondisi |
|----------|---------|
| ✅ Direkomendasikan | Top-N hybrid **AND** ML = Layak |
| ⚠️ Perlu Ditinjau | Top-N hybrid **BUT** ML = Tidak Layak |
| 💡 Kandidat Potensial | Bukan Top-N **BUT** ML = Layak |
| ❌ Tidak Direkomendasikan | Bukan Top-N **AND** ML = Tidak Layak |
