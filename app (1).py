"""
HYBRID DECISION SUPPORT SYSTEM
Rekomendasi Peserta Beasiswa Studi Luar Negeri
Author: Novi Maharani Br Surbakti / 235150400111011
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings("ignore")

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Hybrid DSS – Beasiswa Luar Negeri",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Hide default streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main background */
.stApp {
    background: #0f1117;
    color: #e2e8f0;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #161b27;
    border-right: 1px solid #1e2536;
}
section[data-testid="stSidebar"] .stMarkdown h2 {
    color: #60a5fa;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 700;
}

/* Metric cards */
div[data-testid="metric-container"] {
    background: #161b27;
    border: 1px solid #1e2536;
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
div[data-testid="metric-container"] label {
    color: #94a3b8 !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    letter-spacing: 0.05em;
}
div[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #60a5fa !important;
    font-size: 28px !important;
    font-weight: 800 !important;
}

/* Cards */
.card {
    background: #161b27;
    border: 1px solid #1e2536;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 16px;
}
.card-title {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #60a5fa;
    margin-bottom: 12px;
}

/* Badges */
.badge-rec   { background: #14532d; color: #4ade80; border: 1px solid #16a34a; padding: 3px 10px; border-radius: 999px; font-size: 11px; font-weight: 700; }
.badge-rev   { background: #451a03; color: #fb923c; border: 1px solid #ea580c; padding: 3px 10px; border-radius: 999px; font-size: 11px; font-weight: 700; }
.badge-pot   { background: #172554; color: #60a5fa; border: 1px solid #2563eb; padding: 3px 10px; border-radius: 999px; font-size: 11px; font-weight: 700; }
.badge-no    { background: #1e1e2e; color: #94a3b8; border: 1px solid #334155; padding: 3px 10px; border-radius: 999px; font-size: 11px; font-weight: 700; }

/* Section headers */
.section-header {
    font-size: 22px;
    font-weight: 800;
    color: #f1f5f9;
    margin: 28px 0 16px 0;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-header::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #1e2536;
    margin-left: 12px;
}

/* Top banner */
.top-banner {
    background: linear-gradient(135deg, #1e3a5f 0%, #1a1f35 40%, #0f1117 100%);
    border: 1px solid #1e3a5f;
    border-radius: 16px;
    padding: 28px 36px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
}
.top-banner::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(96,165,250,0.12) 0%, transparent 70%);
    border-radius: 50%;
}
.top-banner h1 {
    font-size: 28px;
    font-weight: 800;
    color: #f1f5f9;
    margin: 0 0 6px 0;
}
.top-banner p {
    font-size: 14px;
    color: #94a3b8;
    margin: 0;
}
.top-banner .tag {
    display: inline-block;
    background: rgba(96,165,250,0.15);
    border: 1px solid rgba(96,165,250,0.3);
    color: #60a5fa;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 999px;
    margin-right: 6px;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* Dataframe styling */
.stDataFrame { border-radius: 10px; overflow: hidden; }

/* Tab styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: #161b27;
    border-radius: 10px;
    padding: 4px;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px;
    color: #94a3b8;
    font-weight: 600;
    font-size: 13px;
}
.stTabs [aria-selected="true"] {
    background: #1e3a5f !important;
    color: #60a5fa !important;
}

/* Button */
.stButton>button {
    background: linear-gradient(135deg, #1e3a5f, #1a4080);
    color: #60a5fa;
    border: 1px solid #2563eb;
    border-radius: 8px;
    font-weight: 600;
    font-size: 13px;
    transition: all 0.2s;
}
.stButton>button:hover {
    background: #1e3a5f;
    border-color: #60a5fa;
    transform: translateY(-1px);
}

/* Slider */
.stSlider [data-baseweb="slider"] { }

/* Info boxes */
.info-box {
    background: rgba(96,165,250,0.05);
    border-left: 3px solid #60a5fa;
    border-radius: 0 8px 8px 0;
    padding: 12px 16px;
    font-size: 13px;
    color: #94a3b8;
    margin: 8px 0;
}

/* Rank badge */
.rank-1  { color: #fbbf24; font-weight: 800; font-size: 16px; }
.rank-top { color: #4ade80; font-weight: 700; }
.rank-mid { color: #60a5fa; font-weight: 600; }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# DATA LOADING & PROCESSING
# ═══════════════════════════════════════════════════════════════

@st.cache_data(show_spinner=False)
def load_and_process():
    """Load dataset and run full hybrid pipeline."""
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.metrics import (accuracy_score, roc_auc_score,
                                  classification_report, confusion_matrix)
    from imblearn.over_sampling import SMOTE

    # ── Load dataset ────────────────────────────────────────────
    file_id = "1XskDxGhAjG3Uqd2SrPCbvgHKk_86iq8J"
    url = f"https://drive.google.com/uc?id={file_id}"
    df_raw = pd.read_csv(url)

    # ── Encoding ────────────────────────────────────────────────
    df = df_raw.copy()
    df['Kefasihan Bahasa Inggris'] = df['Kefasihan Bahasa Inggris'].map(
        {'Dasar': 1, 'Menengah': 2, 'Lanjut': 3})
    df['Pengalaman Magang'] = df['Pengalaman Magang'].map({'Tidak': 0, 'Ya': 1})

    # ── Derived features ────────────────────────────────────────
    df['Skor_Akademik'] = (
        (df['IPK'] / 4.0) * 0.6 +
        (df['Persentase Kehadiran Kelas'] / 100) * 0.4
    ).round(4)
    df['Skor_Ekonomi'] = (
        1 - (df['Penghasilan Orang Tua'] / df['Penghasilan Orang Tua'].max())
    ).round(4)
    df['Skor_Kompetensi'] = (
        (df['Jumlah Prestasi'] / df['Jumlah Prestasi'].max()) * 0.4 +
        df['Pengalaman Magang'] * 0.3 +
        (df['Kefasihan Bahasa Inggris'] / 3) * 0.3
    ).round(4)

    # ── Label ────────────────────────────────────────────────────
    def buat_label(row):
        return 1 if (
            row['IPK'] >= 3.00 and
            row['Persentase Kehadiran Kelas'] >= 75 and
            row['Jumlah Prestasi'] >= 1 and
            row['Kefasihan Bahasa Inggris'] >= 2 and
            row['Penghasilan Orang Tua'] < 7_000_000
        ) else 0
    df['layak_beasiswa'] = df.apply(buat_label, axis=1)

    # ── Preprocessing ────────────────────────────────────────────
    FITUR = ['IPK', 'Kefasihan Bahasa Inggris', 'Jumlah Prestasi',
             'Persentase Kehadiran Kelas', 'Pengalaman Magang',
             'Penghasilan Orang Tua', 'Semester',
             'Skor_Akademik', 'Skor_Ekonomi', 'Skor_Kompetensi']

    X = df[FITUR]
    y = df['layak_beasiswa']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)

    scaler = MinMaxScaler()
    X_train_s = pd.DataFrame(scaler.fit_transform(X_train), columns=FITUR)
    X_test_s  = pd.DataFrame(scaler.transform(X_test), columns=FITUR)

    ratio = max(y_train.sum(), (y_train == 0).sum()) / \
            min(y_train.sum(), (y_train == 0).sum())
    if ratio > 1.5:
        smote = SMOTE(random_state=42)
        X_tr, y_tr = smote.fit_resample(X_train_s, y_train)
    else:
        X_tr, y_tr = X_train_s, y_train

    # ── Random Forest ────────────────────────────────────────────
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_tr, y_tr)
    y_pred = rf.predict(X_test_s)
    y_prob = rf.predict_proba(X_test_s)[:, 1]

    ml_metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'roc_auc' : roc_auc_score(y_test, y_prob),
        'report'  : classification_report(y_test, y_pred,
                        target_names=['Tidak Layak', 'Layak'], output_dict=True),
        'cm'      : confusion_matrix(y_test, y_pred).tolist(),
        'fpr'     : None, 'tpr': None,
        'importances': pd.Series(rf.feature_importances_, index=FITUR)
                        .sort_values(ascending=False),
    }
    from sklearn.metrics import roc_curve
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    ml_metrics['fpr'] = fpr.tolist()
    ml_metrics['tpr'] = tpr.tolist()

    # Predict all
    df['prediksi_ML']    = rf.predict(scaler.transform(df[FITUR]))
    df['probabilitas_ML'] = rf.predict_proba(scaler.transform(df[FITUR]))[:, 1]

    # ── TOPSIS ───────────────────────────────────────────────────
    KRITERIA = {
        'C1': {'kolom': 'IPK',                        'jenis': 'benefit', 'bobot': 0.25},
        'C2': {'kolom': 'Kefasihan Bahasa Inggris',   'jenis': 'benefit', 'bobot': 0.20},
        'C3': {'kolom': 'Jumlah Prestasi',            'jenis': 'benefit', 'bobot': 0.20},
        'C4': {'kolom': 'Persentase Kehadiran Kelas', 'jenis': 'benefit', 'bobot': 0.15},
        'C5': {'kolom': 'Pengalaman Magang',          'jenis': 'benefit', 'bobot': 0.10},
        'C6': {'kolom': 'Penghasilan Orang Tua',      'jenis': 'cost',    'bobot': 0.07},
        'C7': {'kolom': 'Semester',                   'jenis': 'cost',    'bobot': 0.03},
    }
    KODE  = list(KRITERIA.keys())
    KOLOM = [v['kolom'] for v in KRITERIA.values()]
    BOBOT = np.array([v['bobot'] for v in KRITERIA.values()])
    JENIS = [v['jenis'] for v in KRITERIA.values()]

    X_t  = df[KOLOM].values.astype(float)
    denom = np.sqrt((X_t ** 2).sum(axis=0))
    R    = X_t / denom
    V    = R * BOBOT

    A_pos = np.zeros(len(KODE))
    A_neg = np.zeros(len(KODE))
    for j, jenis in enumerate(JENIS):
        if jenis == 'benefit':
            A_pos[j] = V[:, j].max(); A_neg[j] = V[:, j].min()
        else:
            A_pos[j] = V[:, j].min(); A_neg[j] = V[:, j].max()

    D_pos = np.sqrt(((V - A_pos) ** 2).sum(axis=1))
    D_neg = np.sqrt(((V - A_neg) ** 2).sum(axis=1))
    C_    = D_neg / (D_pos + D_neg)

    df_topsis = df[['ID Siswa'] + KOLOM].copy()
    df_topsis.columns = ['ID Siswa'] + KODE
    df_topsis['D+']             = np.round(D_pos, 6)
    df_topsis['D-']             = np.round(D_neg, 6)
    df_topsis['Skor_TOPSIS']    = np.round(C_, 6)
    df_topsis['prediksi_ML']    = df['prediksi_ML'].values
    df_topsis['probabilitas_ML'] = df['probabilitas_ML'].values
    df_topsis['Ranking_TOPSIS'] = df_topsis['Skor_TOPSIS'].rank(
        ascending=False, method='min').astype(int)
    df_topsis = df_topsis.sort_values('Ranking_TOPSIS').reset_index(drop=True)

    # ── Hybrid ───────────────────────────────────────────────────
    W_TOPSIS, W_ML = 0.6, 0.4
    df_hybrid = df_topsis.copy()
    df_hybrid['Skor_Hybrid'] = (
        W_TOPSIS * df_hybrid['Skor_TOPSIS'].clip(0,1) +
        W_ML     * df_hybrid['probabilitas_ML'].clip(0,1)
    ).round(6)
    df_hybrid['Ranking_Hybrid'] = df_hybrid['Skor_Hybrid'].rank(
        ascending=False, method='min').astype(int)
    df_hybrid = df_hybrid.sort_values('Ranking_Hybrid').reset_index(drop=True)

    def kategorikan(row, n):
        hybrid_top = row['Ranking_Hybrid'] <= n
        ml_layak   = row['prediksi_ML'] == 1
        if hybrid_top and ml_layak:    return 'Direkomendasikan'
        if hybrid_top and not ml_layak: return 'Perlu Ditinjau'
        if not hybrid_top and ml_layak: return 'Kandidat Potensial'
        return 'Tidak Direkomendasikan'

    N_BEASISWA = 10
    df_hybrid['Rekomendasi'] = df_hybrid.apply(
        lambda r: kategorikan(r, N_BEASISWA), axis=1)

    # Merge back readable criteria names for display
    nama_map = {v: k for k, v in {'C1':'IPK','C2':'Kefasihan Bahasa Inggris',
        'C3':'Jumlah Prestasi','C4':'Persentase Kehadiran Kelas',
        'C5':'Pengalaman Magang','C6':'Penghasilan Orang Tua','C7':'Semester'}.items()}

    return {
        'df_raw'    : df_raw,
        'df'        : df,
        'df_hybrid' : df_hybrid,
        'ml_metrics': ml_metrics,
        'scaler'    : scaler,
        'rf_model'  : rf,
        'FITUR'     : FITUR,
        'KRITERIA'  : KRITERIA,
        'N_BEASISWA': N_BEASISWA,
        'W_TOPSIS'  : W_TOPSIS,
        'W_ML'      : W_ML,
        'BOBOT'     : BOBOT,
        'KODE'      : KODE,
        'KOLOM'     : KOLOM,
    }


# ═══════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown("## 🎓 Hybrid DSS")
    st.markdown("---")
    st.markdown("## NAVIGASI")
    page = st.radio(
        "",
        ["🏠 Dashboard", "📊 Eksplorasi Data", "🤖 Model ML",
         "🏆 Ranking TOPSIS", "⚡ Hybrid & Hasil", "🔍 Cek Siswa"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.markdown("## PENGATURAN")
    n_beasiswa = st.slider("Kuota Beasiswa", 5, 30, 10)
    w_topsis   = st.slider("Bobot TOPSIS", 0.1, 0.9, 0.6, 0.05)
    w_ml       = round(1.0 - w_topsis, 2)
    st.markdown(f"""
    <div class="info-box">
    TOPSIS : <strong style="color:#60a5fa">{w_topsis}</strong><br>
    ML Prob : <strong style="color:#4ade80">{w_ml}</strong><br>
    Total   : <strong>1.00 ✓</strong>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <div style="font-size:11px; color:#475569; line-height:1.6;">
    <strong style="color:#64748b">Dataset</strong><br>
    Students Performance · 800 siswa<br><br>
    <strong style="color:#64748b">Metode</strong><br>
    Random Forest + TOPSIS<br><br>
    <strong style="color:#64748b">Mahasiswa</strong><br>
    Novi Maharani Br Surbakti<br>
    235150400111011 · SPK SI-D
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# LOAD DATA
# ═══════════════════════════════════════════════════════════════

with st.spinner("Memuat dan memproses data..."):
    try:
        data = load_and_process()
    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
        st.stop()

df_raw    = data['df_raw']
df        = data['df']
df_hybrid = data['df_hybrid'].copy()
ml        = data['ml_metrics']
KRITERIA  = data['KRITERIA']
KODE      = data['KODE']
KOLOM     = data['KOLOM']
FITUR     = data['FITUR']
N         = n_beasiswa

# Re-compute hybrid skor with sidebar weights
df_hybrid['Skor_Hybrid'] = (
    w_topsis * df_hybrid['Skor_TOPSIS'].clip(0,1) +
    w_ml     * df_hybrid['probabilitas_ML'].clip(0,1)
).round(6)
df_hybrid['Ranking_Hybrid'] = df_hybrid['Skor_Hybrid'].rank(
    ascending=False, method='min').astype(int)
df_hybrid = df_hybrid.sort_values('Ranking_Hybrid').reset_index(drop=True)

def kategorikan(row):
    t = row['Ranking_Hybrid'] <= N
    m = row['prediksi_ML'] == 1
    if t and m:     return 'Direkomendasikan'
    if t and not m: return 'Perlu Ditinjau'
    if not t and m: return 'Kandidat Potensial'
    return 'Tidak Direkomendasikan'

df_hybrid['Rekomendasi'] = df_hybrid.apply(kategorikan, axis=1)

WARNA = {
    'Direkomendasikan'     : '#4ade80',
    'Perlu Ditinjau'       : '#fb923c',
    'Kandidat Potensial'   : '#60a5fa',
    'Tidak Direkomendasikan': '#475569',
}

def badge(kat):
    cls = {'Direkomendasikan':'badge-rec','Perlu Ditinjau':'badge-rev',
           'Kandidat Potensial':'badge-pot','Tidak Direkomendasikan':'badge-no'}
    return f'<span class="{cls.get(kat,"badge-no")}">{kat}</span>'


# ═══════════════════════════════════════════════════════════════
# PAGE: DASHBOARD
# ═══════════════════════════════════════════════════════════════

if page == "🏠 Dashboard":
    st.markdown("""
    <div class="top-banner">
        <h1>🎓 Hybrid Decision Support System</h1>
        <p>Rekomendasi Peserta Beasiswa Studi Luar Negeri · SPK SI-D · 2024</p>
        <br>
        <span class="tag">Random Forest</span>
        <span class="tag">TOPSIS MCDM</span>
        <span class="tag">800 Siswa</span>
        <span class="tag">Hybrid Model</span>
    </div>
    """, unsafe_allow_html=True)

    # ── KPI row ──────────────────────────────────────────────────
    n_layak = int(df['layak_beasiswa'].sum())
    n_total = len(df)
    n_rec   = int((df_hybrid['Rekomendasi'] == 'Direkomendasikan').sum())
    acc     = ml['accuracy']
    auc     = ml['roc_auc']

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Siswa", f"{n_total:,}")
    c2.metric("Layak Beasiswa", f"{n_layak}", f"{n_layak/n_total*100:.1f}%")
    c3.metric("Kuota Beasiswa", f"{N}")
    c4.metric("Akurasi RF", f"{acc*100:.2f}%")
    c5.metric("ROC-AUC", f"{auc:.4f}")

    st.markdown('<div class="section-header">Ringkasan Sistem</div>', unsafe_allow_html=True)

    col_l, col_r = st.columns([3, 2])

    with col_l:
        # Pie kategori rekomendasi
        kat_counts = df_hybrid['Rekomendasi'].value_counts().reset_index()
        kat_counts.columns = ['Kategori', 'Jumlah']
        fig_pie = px.pie(
            kat_counts, names='Kategori', values='Jumlah',
            color='Kategori',
            color_discrete_map=WARNA,
            hole=0.5,
            title="Distribusi Kategori Rekomendasi"
        )
        fig_pie.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#94a3b8', title_font_color='#e2e8f0',
            legend=dict(orientation='v', font_size=11),
            margin=dict(t=40, b=10, l=10, r=10)
        )
        fig_pie.update_traces(textfont_color='#e2e8f0')
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_r:
        st.markdown('<div class="card"><div class="card-title">Alur Sistem Hybrid</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="font-size:13px; line-height:2; color:#94a3b8;">
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
            <div style="background:#1e3a5f;border:1px solid #2563eb;border-radius:8px;padding:6px 12px;color:#60a5fa;font-weight:700;font-size:11px;">1. DATA</div>
            <span>800 siswa · 7 fitur asli</span>
        </div>
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
            <div style="background:#1e3a5f;border:1px solid #2563eb;border-radius:8px;padding:6px 12px;color:#60a5fa;font-weight:700;font-size:11px;">2. EDA</div>
            <span>Statistik · outlier · korelasi</span>
        </div>
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
            <div style="background:#1e3a5f;border:1px solid #2563eb;border-radius:8px;padding:6px 12px;color:#60a5fa;font-weight:700;font-size:11px;">3. ML</div>
            <span>Random Forest → probabilitas kelayakan</span>
        </div>
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
            <div style="background:#1e3a5f;border:1px solid #2563eb;border-radius:8px;padding:6px 12px;color:#60a5fa;font-weight:700;font-size:11px;">4. TOPSIS</div>
            <span>7 kriteria berbobot → skor & ranking</span>
        </div>
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
            <div style="background:#14532d;border:1px solid #16a34a;border-radius:8px;padding:6px 12px;color:#4ade80;font-weight:700;font-size:11px;">5. HYBRID</div>
            <span>60% TOPSIS + 40% ML → Rekomendasi</span>
        </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Top 5 kandidat
    st.markdown('<div class="section-header">Top 5 Kandidat Utama</div>', unsafe_allow_html=True)
    top5 = df_hybrid.head(5)[['Ranking_Hybrid', 'ID Siswa', 'C1', 'Skor_TOPSIS',
                                'probabilitas_ML', 'Skor_Hybrid', 'Rekomendasi']]
    top5 = top5.rename(columns={'C1': 'IPK', 'probabilitas_ML': 'Prob ML'})
    top5['Skor_Hybrid'] = top5['Skor_Hybrid'].round(4)
    top5['Prob ML']     = top5['Prob ML'].round(4)
    top5['Skor_TOPSIS'] = top5['Skor_TOPSIS'].round(4)
    st.dataframe(
        top5.set_index('Ranking_Hybrid'),
        use_container_width=True,
        height=220
    )


# ═══════════════════════════════════════════════════════════════
# PAGE: EKSPLORASI DATA
# ═══════════════════════════════════════════════════════════════

elif page == "📊 Eksplorasi Data":
    st.markdown('<div class="top-banner"><h1>📊 Eksplorasi Data</h1><p>Analisis statistik dan distribusi dataset students performance</p></div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Statistik Dasar", "Distribusi Fitur", "Korelasi & Label"])

    with tab1:
        col1, col2, col3 = st.columns(3)
        col1.metric("Jumlah Baris", f"{df_raw.shape[0]}")
        col2.metric("Jumlah Kolom", f"{df_raw.shape[1]}")
        col3.metric("Missing Values", "0")

        st.markdown("#### Preview Data")
        st.dataframe(df_raw.head(20), use_container_width=True, height=380)

        st.markdown("#### Statistik Deskriptif")
        num_cols = ['IPK', 'Jumlah Prestasi', 'Persentase Kehadiran Kelas',
                    'Penghasilan Orang Tua', 'Semester']
        st.dataframe(df_raw[num_cols].describe().round(3), use_container_width=True)

    with tab2:
        num_cols = ['IPK', 'Jumlah Prestasi', 'Persentase Kehadiran Kelas',
                    'Penghasilan Orang Tua', 'Semester']

        fig_dist = make_subplots(
            rows=2, cols=5,
            subplot_titles=[f"Hist: {c}" for c in num_cols] +
                           [f"Box: {c}" for c in num_cols]
        )
        colors = ['#60a5fa', '#4ade80', '#fb923c', '#f472b6', '#a78bfa']
        for i, (col, clr) in enumerate(zip(num_cols, colors)):
            # histogram row 1
            fig_dist.add_trace(go.Histogram(
                x=df_raw[col], name=col, showlegend=False,
                marker_color=clr, opacity=0.8, nbinsx=20
            ), row=1, col=i+1)
            # boxplot row 2
            fig_dist.add_trace(go.Box(
                y=df_raw[col], name=col, showlegend=False,
                marker_color=clr, line_color=clr
            ), row=2, col=i+1)

        fig_dist.update_layout(
            height=600, paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)', font_color='#94a3b8',
            title_text="Distribusi & Outlier Fitur Numerik",
            title_font_color='#e2e8f0',
        )
        fig_dist.update_xaxes(showgrid=False, gridcolor='#1e2536')
        fig_dist.update_yaxes(showgrid=True, gridcolor='#1e2536')
        st.plotly_chart(fig_dist, use_container_width=True)

        # Kategorik
        col_a, col_b = st.columns(2)
        with col_a:
            vc = df_raw['Kefasihan Bahasa Inggris'].value_counts().reset_index()
            fig_cat1 = px.bar(vc, x='Kefasihan Bahasa Inggris', y='count',
                              title='Kefasihan Bahasa Inggris',
                              color='Kefasihan Bahasa Inggris',
                              color_discrete_sequence=['#60a5fa', '#4ade80', '#fb923c'])
            fig_cat1.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)', font_color='#94a3b8',
                title_font_color='#e2e8f0', showlegend=False)
            st.plotly_chart(fig_cat1, use_container_width=True)
        with col_b:
            vc2 = df_raw['Pengalaman Magang'].value_counts().reset_index()
            fig_cat2 = px.pie(vc2, names='Pengalaman Magang', values='count',
                              title='Pengalaman Magang', hole=0.4,
                              color_discrete_sequence=['#4ade80', '#f87171'])
            fig_cat2.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)', font_color='#94a3b8',
                title_font_color='#e2e8f0')
            st.plotly_chart(fig_cat2, use_container_width=True)

    with tab3:
        col_l, col_r = st.columns(2)
        with col_l:
            num_cols2 = ['IPK', 'Jumlah Prestasi', 'Persentase Kehadiran Kelas',
                         'Penghasilan Orang Tua', 'Semester']
            corr = df_raw[num_cols2].corr()
            fig_hm = px.imshow(
                corr, text_auto='.2f', color_continuous_scale='RdBu_r',
                title="Heatmap Korelasi Fitur Numerik",
                aspect='auto', zmin=-1, zmax=1
            )
            fig_hm.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)', font_color='#94a3b8',
                title_font_color='#e2e8f0')
            st.plotly_chart(fig_hm, use_container_width=True)
        with col_r:
            vc3 = df['layak_beasiswa'].value_counts().reset_index()
            vc3['label'] = vc3['layak_beasiswa'].map({1:'Layak (1)', 0:'Tidak Layak (0)'})
            fig_label = px.bar(vc3, x='label', y='count',
                               color='label',
                               color_discrete_sequence=['#f87171','#4ade80'],
                               title='Distribusi Label Target')
            fig_label.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)', font_color='#94a3b8',
                title_font_color='#e2e8f0', showlegend=False)
            st.plotly_chart(fig_label, use_container_width=True)


# ═══════════════════════════════════════════════════════════════
# PAGE: MODEL ML
# ═══════════════════════════════════════════════════════════════

elif page == "🤖 Model ML":
    st.markdown('<div class="top-banner"><h1>🤖 Model Machine Learning</h1><p>Evaluasi Random Forest Classifier untuk prediksi kelayakan beasiswa</p></div>', unsafe_allow_html=True)

    acc = ml['accuracy']; auc = ml['roc_auc']
    rep = ml['report']

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Accuracy",  f"{acc*100:.2f}%")
    c2.metric("ROC-AUC",   f"{auc:.4f}")
    c3.metric("Precision (Layak)", f"{rep['Layak']['precision']:.4f}")
    c4.metric("Recall (Layak)",    f"{rep['Layak']['recall']:.4f}")

    tab1, tab2, tab3 = st.tabs(["Confusion Matrix & ROC", "Feature Importance", "Classification Report"])

    with tab1:
        col_l, col_r = st.columns(2)
        with col_l:
            cm = ml['cm']
            fig_cm = go.Figure(go.Heatmap(
                z=cm, x=['Pred: Tidak Layak', 'Pred: Layak'],
                y=['Aktual: Tidak Layak', 'Aktual: Layak'],
                colorscale='Blues',
                text=[[str(v) for v in row] for row in cm],
                texttemplate='<b>%{text}</b>',
                textfont_size=20,
                showscale=False
            ))
            fig_cm.update_layout(
                title='Confusion Matrix', paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)', font_color='#94a3b8',
                title_font_color='#e2e8f0', height=350
            )
            st.plotly_chart(fig_cm, use_container_width=True)

        with col_r:
            fpr, tpr = ml['fpr'], ml['tpr']
            fig_roc = go.Figure()
            fig_roc.add_trace(go.Scatter(
                x=fpr, y=tpr, mode='lines',
                line=dict(color='#f87171', width=2),
                fill='tozeroy', fillcolor='rgba(248,113,113,0.1)',
                name=f'ROC (AUC = {auc:.4f})'
            ))
            fig_roc.add_trace(go.Scatter(
                x=[0,1], y=[0,1], mode='lines',
                line=dict(color='#475569', width=1, dash='dash'),
                name='Random', showlegend=False
            ))
            fig_roc.update_layout(
                title='ROC Curve — Random Forest',
                xaxis_title='False Positive Rate',
                yaxis_title='True Positive Rate',
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font_color='#94a3b8', title_font_color='#e2e8f0',
                legend=dict(x=0.55, y=0.1, font_size=11),
                height=350
            )
            fig_roc.update_xaxes(gridcolor='#1e2536')
            fig_roc.update_yaxes(gridcolor='#1e2536')
            st.plotly_chart(fig_roc, use_container_width=True)

    with tab2:
        imp = ml['importances'].reset_index()
        imp.columns = ['Fitur', 'Importance']
        fig_imp = px.bar(
            imp, x='Importance', y='Fitur',
            orientation='h',
            color='Importance',
            color_continuous_scale='Blues',
            title='Feature Importance — Random Forest'
        )
        fig_imp.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#94a3b8', title_font_color='#e2e8f0',
            yaxis={'categoryorder':'total ascending'},
            height=420, showlegend=False, coloraxis_showscale=False
        )
        fig_imp.update_xaxes(gridcolor='#1e2536')
        st.plotly_chart(fig_imp, use_container_width=True)

    with tab3:
        rep_df = pd.DataFrame(rep).T
        rep_df = rep_df.drop(['accuracy'], errors='ignore')
        st.dataframe(rep_df.round(4), use_container_width=True)


# ═══════════════════════════════════════════════════════════════
# PAGE: RANKING TOPSIS
# ═══════════════════════════════════════════════════════════════

elif page == "🏆 Ranking TOPSIS":
    st.markdown('<div class="top-banner"><h1>🏆 Ranking TOPSIS</h1><p>Multi-Criteria Decision Making — 7 kriteria berbobot</p></div>', unsafe_allow_html=True)

    # Tabel bobot kriteria
    st.markdown("#### Konfigurasi Kriteria & Bobot")
    cfg_data = {
        'Kode'    : list(KRITERIA.keys()),
        'Kriteria': [v['kolom'] for v in KRITERIA.values()],
        'Jenis'   : [v['jenis'] for v in KRITERIA.values()],
        'Bobot'   : [f"{v['bobot']*100:.0f}%" for v in KRITERIA.values()],
    }
    st.dataframe(pd.DataFrame(cfg_data), use_container_width=True, hide_index=True)

    tab1, tab2 = st.tabs(["Visualisasi Ranking", "Tabel Lengkap"])

    with tab1:
        top20 = df_hybrid.head(20).copy()
        top20['Warna'] = top20['Ranking_Hybrid'].apply(
            lambda r: '#4ade80' if r <= N else '#60a5fa')
        fig_rank = go.Figure()
        fig_rank.add_trace(go.Bar(
            x=top20['Skor_TOPSIS'],
            y=top20['ID Siswa'],
            orientation='h',
            marker_color=top20['Warna'],
            text=top20['Skor_TOPSIS'].round(4),
            textposition='outside',
            textfont=dict(size=10, color='#94a3b8')
        ))
        fig_rank.update_layout(
            title=f'Top 20 Kandidat — Skor TOPSIS (Hijau = Top {N})',
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#94a3b8', title_font_color='#e2e8f0',
            yaxis=dict(autorange='reversed'),
            xaxis_title='Skor TOPSIS', height=600,
            margin=dict(l=80, r=120)
        )
        fig_rank.update_xaxes(gridcolor='#1e2536')
        st.plotly_chart(fig_rank, use_container_width=True)

    with tab2:
        display_cols = ['Ranking_TOPSIS', 'ID Siswa'] + KODE + \
                       ['D+', 'D-', 'Skor_TOPSIS']
        st.dataframe(
            df_hybrid[display_cols].rename(columns=dict(zip(KODE, KOLOM))),
            use_container_width=True, height=500
        )


# ═══════════════════════════════════════════════════════════════
# PAGE: HYBRID & HASIL
# ═══════════════════════════════════════════════════════════════

elif page == "⚡ Hybrid & Hasil":
    st.markdown('<div class="top-banner"><h1>⚡ Hasil Hybrid DSS</h1><p>Integrasi Random Forest + TOPSIS dengan bobot yang dapat dikonfigurasi</p></div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-box">
    <strong>Formula:</strong> Skor_Hybrid = <strong style="color:#fb923c">{w_topsis}</strong> × Skor_TOPSIS
    + <strong style="color:#4ade80">{w_ml}</strong> × Probabilitas_ML
    &nbsp;·&nbsp; Kuota: <strong style="color:#60a5fa">{N} siswa</strong>
    </div>
    """, unsafe_allow_html=True)

    # Stats row
    n_rec  = (df_hybrid['Rekomendasi'] == 'Direkomendasikan').sum()
    n_rev  = (df_hybrid['Rekomendasi'] == 'Perlu Ditinjau').sum()
    n_pot  = (df_hybrid['Rekomendasi'] == 'Kandidat Potensial').sum()
    n_no   = (df_hybrid['Rekomendasi'] == 'Tidak Direkomendasikan').sum()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("✅ Direkomendasikan",       n_rec)
    c2.metric("⚠️ Perlu Ditinjau",         n_rev)
    c3.metric("💡 Kandidat Potensial",      n_pot)
    c4.metric("❌ Tidak Direkomendasikan",  n_no)

    tab1, tab2, tab3 = st.tabs(["Scatter & Distribusi", "Kandidat Utama", "Kandidat Cadangan"])

    with tab1:
        col_l, col_r = st.columns(2)
        with col_l:
            fig_sc = px.scatter(
                df_hybrid, x='Skor_TOPSIS', y='probabilitas_ML',
                color='Rekomendasi',
                color_discrete_map=WARNA,
                opacity=0.7, size_max=8,
                title='Scatter: Skor TOPSIS vs Probabilitas ML',
                labels={'probabilitas_ML': 'Prob ML', 'Skor_TOPSIS': 'Skor TOPSIS'}
            )
            fig_sc.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font_color='#94a3b8', title_font_color='#e2e8f0', height=380
            )
            fig_sc.update_xaxes(gridcolor='#1e2536')
            fig_sc.update_yaxes(gridcolor='#1e2536')
            st.plotly_chart(fig_sc, use_container_width=True)

        with col_r:
            kat_c = df_hybrid['Rekomendasi'].value_counts().reset_index()
            kat_c.columns = ['Kategori', 'Jumlah']
            fig_pie2 = px.pie(
                kat_c, names='Kategori', values='Jumlah',
                color='Kategori', color_discrete_map=WARNA,
                hole=0.45, title='Proporsi Kategori Rekomendasi'
            )
            fig_pie2.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font_color='#94a3b8', title_font_color='#e2e8f0', height=380
            )
            st.plotly_chart(fig_pie2, use_container_width=True)

        # Histogram skor hybrid
        fig_hist = px.histogram(
            df_hybrid, x='Skor_Hybrid', color='Rekomendasi',
            color_discrete_map=WARNA, nbins=40,
            title='Distribusi Skor Hybrid', opacity=0.8
        )
        fig_hist.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font_color='#94a3b8', title_font_color='#e2e8f0', height=300,
            barmode='overlay'
        )
        fig_hist.update_xaxes(gridcolor='#1e2536')
        fig_hist.update_yaxes(gridcolor='#1e2536')
        st.plotly_chart(fig_hist, use_container_width=True)

    with tab2:
        utama = df_hybrid[df_hybrid['Ranking_Hybrid'] <= N].copy()
        cols = ['Ranking_Hybrid', 'ID Siswa', 'C1', 'C2', 'C3',
                'Skor_TOPSIS', 'probabilitas_ML', 'Skor_Hybrid', 'Rekomendasi']
        st.markdown(f"**{len(utama)} Kandidat Utama** (Rank 1 – {N})")
        st.dataframe(
            utama[cols].rename(columns={
                'Ranking_Hybrid':'Rank', 'C1':'IPK', 'C2':'Kefasihan',
                'C3':'Prestasi', 'probabilitas_ML':'Prob ML'}),
            use_container_width=True, hide_index=True, height=400
        )

    with tab3:
        cadangan = df_hybrid[
            (df_hybrid['Ranking_Hybrid'] > N) &
            (df_hybrid['Ranking_Hybrid'] <= N * 2)
        ].copy()
        st.markdown(f"**{len(cadangan)} Kandidat Cadangan** (Rank {N+1} – {N*2})")
        st.dataframe(
            cadangan[cols].rename(columns={
                'Ranking_Hybrid':'Rank', 'C1':'IPK', 'C2':'Kefasihan',
                'C3':'Prestasi', 'probabilitas_ML':'Prob ML'}),
            use_container_width=True, hide_index=True, height=400
        )


# ═══════════════════════════════════════════════════════════════
# PAGE: CEK SISWA
# ═══════════════════════════════════════════════════════════════

elif page == "🔍 Cek Siswa":
    st.markdown('<div class="top-banner"><h1>🔍 Cek Kelayakan Siswa</h1><p>Masukkan data siswa untuk mendapatkan prediksi dan skor hybrid</p></div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Input Manual", "Cari ID Siswa"])

    with tab1:
        st.markdown("#### Input Data Siswa Baru")
        col1, col2 = st.columns(2)

        with col1:
            ipk       = st.slider("IPK (0.0 – 4.0)", 0.0, 4.0, 3.2, 0.01)
            kehadiran = st.slider("Persentase Kehadiran (%)", 0, 100, 85)
            prestasi  = st.slider("Jumlah Prestasi", 0, 20, 3)
            semester  = st.slider("Semester", 1, 8, 5)

        with col2:
            kefasihan_raw = st.selectbox("Kefasihan Bahasa Inggris",
                                          ['Dasar', 'Menengah', 'Lanjut'])
            magang_raw    = st.selectbox("Pengalaman Magang", ['Tidak', 'Ya'])
            penghasilan   = st.number_input("Penghasilan Orang Tua (Rp)",
                                             0, 50_000_000, 5_000_000, 500_000,
                                             format="%d")

        kefasihan = {'Dasar':1, 'Menengah':2, 'Lanjut':3}[kefasihan_raw]
        magang    = {'Tidak':0, 'Ya':1}[magang_raw]

        if st.button("⚡ Prediksi Kelayakan", use_container_width=True):
            # Derived features
            skor_akademik   = round((ipk/4.0)*0.6 + (kehadiran/100)*0.4, 4)
            max_penghasilan = df_raw['Penghasilan Orang Tua'].max()
            skor_ekonomi    = round(1 - penghasilan/max_penghasilan, 4)
            max_prestasi    = df_raw['Jumlah Prestasi'].max()
            skor_kompetensi = round(
                (prestasi/max_prestasi)*0.4 + magang*0.3 + (kefasihan/3)*0.3, 4)

            row_fitur = np.array([[ipk, kefasihan, prestasi, kehadiran, magang,
                                    penghasilan, semester,
                                    skor_akademik, skor_ekonomi, skor_kompetensi]])

            X_scaled     = data['scaler'].transform(row_fitur)
            pred_ml      = data['rf_model'].predict(X_scaled)[0]
            prob_ml      = data['rf_model'].predict_proba(X_scaled)[0][1]
            skor_hybrid_est = round(w_topsis * 0.5 + w_ml * prob_ml, 4)

            # Rule-based label
            rule_layak = (ipk >= 3.0 and kehadiran >= 75 and
                          prestasi >= 1 and kefasihan >= 2 and
                          penghasilan < 7_000_000)

            st.markdown("---")
            c1, c2, c3 = st.columns(3)
            c1.metric("Prediksi ML", "✅ LAYAK" if pred_ml == 1 else "❌ Tidak Layak")
            c2.metric("Probabilitas Kelayakan", f"{prob_ml*100:.2f}%")
            c3.metric("Rule-Based Label", "✅ LAYAK" if rule_layak else "❌ Tidak Layak")

            st.markdown(f"""
            <div class="card" style="margin-top:16px;">
            <div class="card-title">Detail Skor</div>
            <table style="width:100%; font-size:13px; color:#94a3b8; border-collapse:collapse;">
            <tr><td style="padding:6px 0; border-bottom:1px solid #1e2536;">Skor Akademik</td>
                <td style="color:#60a5fa; font-weight:700; text-align:right;">{skor_akademik:.4f}</td></tr>
            <tr><td style="padding:6px 0; border-bottom:1px solid #1e2536;">Skor Ekonomi</td>
                <td style="color:#4ade80; font-weight:700; text-align:right;">{skor_ekonomi:.4f}</td></tr>
            <tr><td style="padding:6px 0; border-bottom:1px solid #1e2536;">Skor Kompetensi</td>
                <td style="color:#fb923c; font-weight:700; text-align:right;">{skor_kompetensi:.4f}</td></tr>
            <tr><td style="padding:6px 0;">Estimasi Skor Hybrid</td>
                <td style="color:#f472b6; font-weight:700; text-align:right;">{skor_hybrid_est:.4f}</td></tr>
            </table>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        st.markdown("#### Cari Data Siswa dari Dataset")
        all_ids = df_hybrid['ID Siswa'].tolist()
        selected_id = st.selectbox("Pilih ID Siswa", all_ids)

        if selected_id:
            row = df_hybrid[df_hybrid['ID Siswa'] == selected_id].iloc[0]
            c1, c2, c3 = st.columns(3)
            c1.metric("Ranking Hybrid", f"#{int(row['Ranking_Hybrid'])}")
            c2.metric("Skor Hybrid",    f"{row['Skor_Hybrid']:.4f}")
            c3.metric("Prob ML",        f"{row['probabilitas_ML']*100:.2f}%")

            c4, c5, c6 = st.columns(3)
            c4.metric("Skor TOPSIS",   f"{row['Skor_TOPSIS']:.4f}")
            c5.metric("IPK (C1)",       f"{row['C1']:.2f}")
            c6.metric("Prediksi ML",    "✅ Layak" if row['prediksi_ML']==1 else "❌ Tidak")

            st.markdown(f"""
            <div class="card" style="margin-top:16px;">
            <div class="card-title">Rekomendasi</div>
            {badge(row['Rekomendasi'])}
            </div>
            """, unsafe_allow_html=True)

            # Radar chart kriteria siswa ini
            vals = [row[k] for k in KODE]
            fig_radar = go.Figure()
            fig_radar.add_trace(go.Scatterpolar(
                r=vals, theta=KOLOM,
                fill='toself', fillcolor='rgba(96,165,250,0.15)',
                line=dict(color='#60a5fa', width=2),
                name=selected_id
            ))
            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True, color='#475569'),
                    angularaxis=dict(color='#94a3b8')
                ),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#94a3b8',
                title=f'Profil Kriteria — {selected_id}',
                title_font_color='#e2e8f0',
                height=400
            )
            st.plotly_chart(fig_radar, use_container_width=True)
