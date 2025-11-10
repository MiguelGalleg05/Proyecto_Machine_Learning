import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ==============================
#  CARGA DE DATOS
# ==============================
REPORT_DIR = "../monitoring"
latest_report = sorted(
    [f for f in os.listdir(REPORT_DIR) if f.endswith(".csv")],
    reverse=True
)[0]

df = pd.read_csv(os.path.join(REPORT_DIR, latest_report))

# ==============================
#  CONFIG GENERAL
# ==============================
st.set_page_config(
    page_title="Monitoreo de Data Drift",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        .main {padding-top: 20px;}
        .metric-box {
            border-radius: 10px;
            background-color: #1e2227;
            padding: 18px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
#  SIDEBAR
# ==============================
st.sidebar.header("📁 Reporte más reciente")
st.sidebar.success(latest_report)

# FILTRO POR TIPO
types = st.sidebar.multiselect(
    "Filtrar por tipo de variable",
    options=df["type"].unique(),
    default=df["type"].unique()
)

df_filtered = df[df["type"].isin(types)]

# ==============================
#  ENCABEZADO
# ==============================
st.markdown("## 📊 Monitoreo de Data Drift del Modelo")
st.markdown(
    """
    Esta aplicación permite visualizar métricas de drift y detectar desviaciones 
    significativas entre la población histórica y la actual.
    """
)

# ==============================
# TABLA LIMPIA
# ==============================
st.markdown("### 📋 Tabla de métricas de drift")

alert_colors = {
    "Bajo": "🟢 Estable",
    "Moderado": "🟡 Atención",
    "Alto": "🔴 Crítico"
}

def map_alert(psi):
    if pd.isna(psi):
        return "🟢 Estable"
    if psi < 0.10:
        return "🟢 Estable"
    elif psi < 0.25:
        return "🟡 Atención"
    else:
        return "🔴 Crítico"

df_filtered["alert"] = df_filtered["psi"].apply(map_alert)

st.dataframe(
    df_filtered[["feature", "type", "ks_pvalue", "psi", "js_distance", "chi_pvalue", "alert"]],
    use_container_width=True
)

# ==============================
#  GRAFICAS
# ==============================
st.markdown("### 📈 Métricas de Drift por Variable")

# PSI
psi_df = df_filtered[df_filtered["psi"].notna()]
if len(psi_df) > 0:
    fig = px.bar(
        psi_df,
        x="feature",
        y="psi",
        title="PSI (Population Stability Index)",
        color="psi",
        color_continuous_scale="blues"
    )
    st.plotly_chart(fig, use_container_width=True)

# KS
ks_df = df_filtered[df_filtered["ks_pvalue"].notna()]
if len(ks_df) > 0:
    fig = px.bar(
        ks_df,
        x="feature",
        y="ks_pvalue",
        title="Kolmogorov-Smirnov (KS)",
        color="ks_pvalue",
        color_continuous_scale="greens"
    )
    st.plotly_chart(fig, use_container_width=True)

# JS
js_df = df_filtered[df_filtered["js_distance"].notna()]
if len(js_df) > 0:
    fig = px.bar(
        js_df,
        x="feature",
        y="js_distance",
        title="Jensen-Shannon Divergence",
        color="js_distance",
        color_continuous_scale="reds"
    )
    st.plotly_chart(fig, use_container_width=True)

# ==============================
# LEYENDA
# ==============================
st.info(
    """
    **Interpretación PSI**
    - < 0.10 → ✅ Control  
    - 0.10 – 0.25 → ⚠️ Atención  
    - ≥ 0.25 → 🚨 Drift crítico  
    """
)
