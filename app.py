import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
from streamlit_option_menu import option_menu
from PIL import Image
import numpy as np
import time
import requests
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Opcionales: solo importa si los usas (comentadas para optimizar)
# import streamlit_lottie as st_lottie
# from streamlit_autorefresh import st_autorefresh
# from streamlit_timeline import timeline

# ----- CONFIGURACIÓN DE PÁGINA -----
st.set_page_config(
    page_title="🚀 Pitch Empresarial - Raíces Andinas", 
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/',
        'Report a bug': "mailto:pitch@raicesandinas.com",
        'About': "# Segmentación Inteligente COAC Raíces Andinas\nPowered by AI & Analytics"
    }
)

# ----- ESTILOS AVANZADOS -----
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    .main-header {font-family: 'Poppins', sans-serif; font-size: 3.5rem; font-weight: 700;
    text-align: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 2rem;
    animation: glow 2s ease-in-out infinite alternate;}
    @keyframes glow {from { filter: drop-shadow(0 0 5px rgba(102, 126, 234, 0.5)); }
    to { filter: drop-shadow(0 0 20px rgba(102, 126, 234, 0.8)); }}
    .metric-card {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 25px; border-radius: 20px; color: white; text-align: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1); margin: 15px; position: relative; overflow: hidden;}
    .segment-card {border-radius: 20px; padding: 25px; text-align: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1); margin: 15px;}
    .data-card {background: linear-gradient(145deg, #ffffff 0%, #f0f0f0 100%);
    border-radius: 15px; padding: 20px; margin: 10px 0; box-shadow: 20px 20px 60px #d9d9d9,
    -20px -20px 60px #ffffff; transition: all 0.3s ease;}
    .progress-bar {height: 8px; background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
    border-radius: 10px;}
    .neon-text {color: #fff; text-shadow: 0 0 5px #667eea, 0 0 10px #667eea,
    0 0 20px #667eea, 0 0 40px #667eea;}
</style>
""", unsafe_allow_html=True)

# ----- FUNCIONES AUXILIARES -----
@st.cache_data
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

@st.cache_data
def generate_enhanced_data():
    np.random.seed(42)
    tradicional = pd.DataFrame({
        'edad': np.random.normal(45, 8, 300),
        'ingresos': np.random.normal(3559, 800, 300),
        'saldo_dpf': np.random.normal(27597, 5000, 300),
        'capital_prestado': np.random.normal(21576, 3000, 300),
        'mora_dias': np.random.exponential(1.5, 300),
        'productos_activos': np.random.poisson(2, 300),
        'antiguedad_anos': np.random.normal(12, 4, 300),
        'uso_digital': np.random.beta(2, 8, 300),
        'cluster': 0
    })
    riesgo = pd.DataFrame({
        'edad': np.random.normal(38, 12, 500),
        'ingresos': np.random.normal(3759, 1200, 500),
        'saldo_dpf': np.random.normal(316, 200, 500),
        'capital_prestado': np.random.normal(21282, 4000, 500),
        'mora_dias': np.random.exponential(18, 500),
        'productos_activos': np.random.poisson(1.5, 500),
        'antiguedad_anos': np.random.normal(5, 3, 500),
        'uso_digital': np.random.beta(3, 7, 500),
        'cluster': 1
    })
    tech = pd.DataFrame({
        'edad': np.random.normal(40, 6, 200),
        'ingresos': np.random.normal(3962, 600, 200),
        'saldo_dpf': np.random.normal(7656, 2000, 200),
        'capital_prestado': np.random.normal(27803, 2500, 200),
        'mora_dias': np.random.exponential(10.2, 200),
        'productos_activos': np.random.poisson(4, 200),
        'antiguedad_anos': np.random.normal(8, 3, 200),
        'uso_digital': np.random.beta(8, 2, 200),
        'cluster': 2
    })
    return pd.concat([tradicional, riesgo, tech], ignore_index=True)

def create_3d_scatter(df_enhanced):
    fig = go.Figure(data=[
        go.Scatter3d(
            x=df_enhanced[df_enhanced['cluster']==0]['edad'],
            y=df_enhanced[df_enhanced['cluster']==0]['ingresos'],
            z=df_enhanced[df_enhanced['cluster']==0]['saldo_dpf'],
            mode='markers',
            marker=dict(size=5, color='#8dd3c7', opacity=0.8),
            name='🧓 Tradicional',
        ),
        go.Scatter3d(
            x=df_enhanced[df_enhanced['cluster']==1]['edad'],
            y=df_enhanced[df_enhanced['cluster']==1]['ingresos'],
            z=df_enhanced[df_enhanced['cluster']==1]['saldo_dpf'],
            mode='markers',
            marker=dict(size=5, color='#ffffb3', opacity=0.8),
            name='⚠️ Riesgo',
        ),
        go.Scatter3d(
            x=df_enhanced[df_enhanced['cluster']==2]['edad'],
            y=df_enhanced[df_enhanced['cluster']==2]['ingresos'],
            z=df_enhanced[df_enhanced['cluster']==2]['saldo_dpf'],
            mode='markers',
            marker=dict(size=5, color='#bebada', opacity=0.8),
            name='📱 Tech',
        )
    ])
    fig.update_layout(
        title="Visualización 3D de Segmentos de Clientes",
        scene=dict(
            xaxis_title="Edad",
            yaxis_title="Ingresos ($)",
            zaxis_title="Saldo DPF ($)",
            bgcolor="rgba(0,0,0,0)"
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig

def create_correlation_heatmap(df_enhanced):
    numeric_cols = ['edad', 'ingresos', 'saldo_dpf', 'capital_prestado', 'mora_dias', 'productos_activos', 'uso_digital']
    corr_matrix = df_enhanced[numeric_cols].corr()
    fig = ff.create_annotated_heatmap(
        z=corr_matrix.values,
        x=list(corr_matrix.columns),
        y=list(corr_matrix.index),
        annotation_text=corr_matrix.round(2).values,
        showscale=True,
        colorscale='RdBu'
    )
    fig.update_layout(
        title="Matriz de Correlaciones - Variables Clave",
        xaxis_title="Variables",
        yaxis_title="Variables"
    )
    return fig

# ----- DATOS -----
df_enhanced = generate_enhanced_data()

# ----- SIDEBAR -----
with st.sidebar:
    try:
        logo = Image.open("logo_raices.jpg")
        st.image(logo, use_container_width=True)
    except:
        st.markdown("### 🏦 COAC Raíces Andinas")
    selected = option_menu(
        menu_title="🎯 Dashboard Ejecutivo",
        options=[
            "🚀 Oportunidad Dorada",
            "🏦 Nuestra Fortaleza",
            "🔬 IA & Analytics",
            "🎯 Segmentos Inteligentes"
        ],
        icons=[
            "rocket-takeoff-fill", "bank2", "cpu", "bullseye"
        ],
        menu_icon="grid-3x3-gap-fill",
        default_index=0,
        styles={
            "container": {"padding": "10px", "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"},
            "icon": {"color": "white", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"5px", "color": "white"},
            "nav-link-selected": {"background-color": "rgba(255,255,255,0.2)", "backdrop-filter": "blur(10px)"},
        }
    )
    st.markdown("---")
    st.markdown("### 📊 Métricas en Vivo")
    live_socios = 48127 + np.random.randint(-50, 100)
    live_remesas = 5.49 + np.random.uniform(-0.1, 0.2)
    live_roi = 245 + np.random.randint(-10, 20)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Socios", f"{live_socios:,}", f"+{np.random.randint(1,5)}")
    with col2:
        st.metric("Remesas", f"${live_remesas:.2f}B", f"+{np.random.uniform(0.1,0.5):.1f}%")
    st.metric("ROI Proyectado", f"{live_roi}%", f"+{np.random.randint(1,8)}%")
    st.markdown("---")

# ----- SECCIONES (¡Agrega tus secciones originales aquí, pegando los bloques del dashboard!) -----
# Por espacio y claridad no se copian aquí todos los bloques de secciones principales,
# pero aquí iría la estructura igual que en tu código original.
# Ejemplo para insertar una sección:

if selected == "🚀 Oportunidad Dorada":
    st.markdown('<h1 class="main-header neon-text">🚀 La Mina de Oro Digital de Ecuador</h1>', unsafe_allow_html=True)
    # ... aquí tu código del dashboard ...
    # ¡Pega aquí tus secciones tal como las tenías, usando las funciones limpias de arriba!

# Repite para las demás secciones: "🏦 Nuestra Fortaleza", "🔬 IA & Analytics", "🎯 Segmentos Inteligentes", etc.

# ----- PIE DE PÁGINA -----
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 15px; margin: 20px 0;">
    <h3>“El futuro pertenece a quienes preparan hoy su éxito con inteligencia y visión”</h3>
    <p>COAC Raíces Andinas — Agosto 2025</p>
</div>
""", unsafe_allow_html=True)
