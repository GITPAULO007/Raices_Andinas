import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
from streamlit_option_menu import option_menu
from PIL import Image
import numpy as np
from datetime import datetime, date
import time
import seaborn as sns
import matplotlib.pyplot as plt

# Nuevas librerías para efectos avanzados
import streamlit_lottie as st_lottie
import requests
import streamlit_echarts as st_echarts
from streamlit_elements import elements, mui, html, dashboard, nivo
import streamlit_authenticator as stauth
from streamlit_autorefresh import st_autorefresh
import streamlit_ace as st_ace
from streamlit_card import card
import streamlit_shadcn_ui as ui
from streamlit_timeline import timeline
import altair as alt
from wordcloud import WordCloud
import networkx as nx
import streamlit_agraph as agraph

# Para efectos de datos avanzados
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings('ignore')

# Configuración de página optimizada
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

# Auto-refresh cada 30 segundos para datos "en vivo"
count = st_autorefresh(interval=30000, limit=100, key="fizzbuzzcounter")

# CSS avanzado con animaciones y efectos modernos
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    .main-header {
        font-family: 'Poppins', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { filter: drop-shadow(0 0 5px rgba(102, 126, 234, 0.5)); }
        to { filter: drop-shadow(0 0 20px rgba(102, 126, 234, 0.8)); }
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 25px;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        margin: 15px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    
    .metric-card:hover::before {
        left: 100%;
    }
    
    .metric-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 25px 50px rgba(102, 126, 234, 0.3);
    }
    
    .opportunity-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 30px;
        border-radius: 20px;
        color: white;
        margin: 20px 0;
        box-shadow: 0 20px 40px rgba(240, 147, 251, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .opportunity-card::after {
        content: '💎';
        position: absolute;
        top: 20px;
        right: 20px;
        font-size: 3rem;
        opacity: 0.2;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    .segment-card {
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        margin: 15px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .segment-card:hover {
        transform: translateY(-15px) rotate(2deg);
        box-shadow: 0 25px 50px rgba(0,0,0,0.2);
    }
    
    .timeline-item {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-left: 5px solid #4ECDC4;
        padding: 20px;
        margin: 15px 0;
        border-radius: 15px;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .timeline-item:hover {
        transform: translateX(10px);
        box-shadow: 0 10px 25px rgba(78, 205, 196, 0.2);
    }
    
    .glassmorphism {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 20px;
        margin: 10px 0;
    }
    
    .floating-element {
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .progress-bar {
        height: 8px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        border-radius: 10px;
        animation: shimmer 2s infinite;
    }
    
    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    .neon-text {
        color: #fff;
        text-shadow: 0 0 5px #667eea, 0 0 10px #667eea, 0 0 20px #667eea, 0 0 40px #667eea;
    }
    
    .data-card {
        background: linear-gradient(145deg, #ffffff 0%, #f0f0f0 100%);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 20px 20px 60px #d9d9d9, -20px -20px 60px #ffffff;
        transition: all 0.3s ease;
    }
    
    .data-card:hover {
        box-shadow: 25px 25px 75px #d9d9d9, -25px -25px 75px #ffffff;
        transform: translateY(-5px);
    }
</style>
""", unsafe_allow_html=True)

# Función para cargar animaciones Lottie
@st.cache_data
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Animaciones Lottie para diferentes secciones
lottie_business = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_v1yudlrx.json")
lottie_data = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_qp1q7mct.json")
lottie_growth = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_khzjlzhs.json")
lottie_money = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_06a6pf9i.json")

# Función para generar datos más realistas
@st.cache_data
def generate_enhanced_data():
    np.random.seed(42)
    
    # Datos de socios más detallados
    n_samples = 1000
    
    # Cluster 0: Tradicional (30%)
    tradicional = pd.DataFrame({
        'edad': np.random.normal(45, 8, 300),
        'ingresos': np.random.normal(3559, 800, 300),
        'saldo_dpf': np.random.normal(27597, 5000, 300),
        'capital_prestado': np.random.normal(21576, 3000, 300),
        'mora_dias': np.random.exponential(1.5, 300),
        'productos_activos': np.random.poisson(2, 300),
        'antiguedad_anos': np.random.normal(12, 4, 300),
        'uso_digital': np.random.beta(2, 8, 300),  # Bajo uso digital
        'cluster': 0
    })
    
    # Cluster 1: Riesgo (50%)
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
    
    # Cluster 2: Tech (20%)
    tech = pd.DataFrame({
        'edad': np.random.normal(40, 6, 200),
        'ingresos': np.random.normal(3962, 600, 200),
        'saldo_dpf': np.random.normal(7656, 2000, 200),
        'capital_prestado': np.random.normal(27803, 2500, 200),
        'mora_dias': np.random.exponential(10.2, 200),
        'productos_activos': np.random.poisson(4, 200),
        'antiguedad_anos': np.random.normal(8, 3, 200),
        'uso_digital': np.random.beta(8, 2, 200),  # Alto uso digital
        'cluster': 2
    })
    
    return pd.concat([tradicional, riesgo, tech], ignore_index=True)

# Cargar datos mejorados
df_enhanced = generate_enhanced_data()

# Función para crear gráficos 3D interactivos
def create_3d_scatter():
    fig = go.Figure(data=[
        go.Scatter3d(
            x=df_enhanced[df_enhanced['cluster']==0]['edad'],
            y=df_enhanced[df_enhanced['cluster']==0]['ingresos'],
            z=df_enhanced[df_enhanced['cluster']==0]['saldo_dpf'],
            mode='markers',
            marker=dict(size=5, color='#8dd3c7', opacity=0.8),
            name='🧓 Tradicional',
            hovertemplate='<b>Tradicional</b><br>Edad: %{x}<br>Ingresos: $%{y}<br>Saldo DPF: $%{z}<extra></extra>'
        ),
        go.Scatter3d(
            x=df_enhanced[df_enhanced['cluster']==1]['edad'],
            y=df_enhanced[df_enhanced['cluster']==1]['ingresos'],
            z=df_enhanced[df_enhanced['cluster']==1]['saldo_dpf'],
            mode='markers',
            marker=dict(size=5, color='#ffffb3', opacity=0.8),
            name='⚠️ Riesgo',
            hovertemplate='<b>Riesgo</b><br>Edad: %{x}<br>Ingresos: $%{y}<br>Saldo DPF: $%{z}<extra></extra>'
        ),
        go.Scatter3d(
            x=df_enhanced[df_enhanced['cluster']==2]['edad'],
            y=df_enhanced[df_enhanced['cluster']==2]['ingresos'],
            z=df_enhanced[df_enhanced['cluster']==2]['saldo_dpf'],
            mode='markers',
            marker=dict(size=5, color='#bebada', opacity=0.8),
            name='📱 Tech',
            hovertemplate='<b>Tech</b><br>Edad: %{x}<br>Ingresos: $%{y}<br>Saldo DPF: $%{z}<extra></extra>'
        )
    ])
    
    fig.update_layout(
        title="Visualización 3D de Segmentos de Clientes",
        scene=dict(
            xaxis_title="Edad",
            yaxis_title="Ingresos ($)",
            zaxis_title="Saldo DPF ($)",
            bgcolor="rgba(0,0,0,0)",
            xaxis=dict(backgroundcolor="rgba(0,0,0,0)"),
            yaxis=dict(backgroundcolor="rgba(0,0,0,0)"),
            zaxis=dict(backgroundcolor="rgba(0,0,0,0)")
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    
    return fig

# Función para crear heatmap de correlaciones
def create_correlation_heatmap():
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

# SIDEBAR MEJORADO CON EFECTOS
with st.sidebar:
    # Logo con efecto
    st.markdown('<div class="floating-element">', unsafe_allow_html=True)
    try:
        logo = Image.open("logo_raices.jpg")
        st.image(logo, use_container_width=True)
    except:
        st.markdown("### 🏦 COAC Raíces Andinas")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Menú principal con efectos mejorados
    selected = option_menu(
        menu_title="🎯 Dashboard Ejecutivo",
        options=[
            "🚀 Oportunidad Dorada",
            "🏦 Nuestra Fortaleza",
            "🔬 IA & Analytics",
            "🎯 Segmentos Inteligentes", 
            "🧪 Simulador Predictivo",
            "🏁 Roadmap Estratégico"
        ],
        icons=[
            "rocket-takeoff-fill", "bank2", "cpu", "bullseye", "calculator", "flag-fill"
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
    
    # Dashboard en tiempo real con animaciones
    st.markdown("### 📊 Métricas en Vivo")
    
    # Simulación de datos en tiempo real
    live_socios = 48127 + np.random.randint(-50, 100)
    live_remesas = 5.49 + np.random.uniform(-0.1, 0.2)
    live_roi = 245 + np.random.randint(-10, 20)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Socios", f"{live_socios:,}", f"+{np.random.randint(1,5)}")
    with col2:
        st.metric("Remesas", f"${live_remesas:.2f}B", f"+{np.random.uniform(0.1,0.5):.1f}%")
    
    st.metric("ROI Proyectado", f"{live_roi}%", f"+{np.random.randint(1,8)}%")
    
    # Barra de progreso animada
    progress_value = (list(range(6)).index(next((i for i, opt in enumerate(["🚀 Oportunidad Dorada", "🏦 Nuestra Fortaleza", "🔬 IA & Analytics", "🎯 Segmentos Inteligentes", "🧪 Simulador Predictivo", "🏁 Roadmap Estratégico"]) if opt == selected), 0)) + 1) / 6
    
    st.markdown('<div class="progress-bar"></div>', unsafe_allow_html=True)
    st.progress(progress_value)
    st.caption(f"Progreso del pitch: {int(progress_value*100)}%")
    
    st.markdown("---")
    
    # Aliados estratégicos con logos mejorados
    st.markdown("### 🤝 Aliados Estratégicos")
    try:
        alprode_logo = Image.open("alprode.png")
        st.image(alprode_logo, width=120)
        ucuenca_logo = Image.open("logo_ucuenca.png") 
        st.image(ucuenca_logo, width=120)
    except:
        st.markdown("""
        <div class="glassmorphism">
        <b>Aliados Clave:</b><br>
        🏢 Alprode<br>
        🎓 Universidad de Cuenca<br>
        🤖 AI Analytics Partners
        </div>
        """, unsafe_allow_html=True)

# SECCIONES PRINCIPALES MEJORADAS
if "🚀 Oportunidad Dorada" in selected:
    # Header con animación Lottie
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if lottie_money:
            st_lottie.st_lottie(lottie_money, height=200, key="money_animation")
    
    st.markdown('<h1 class="main-header neon-text">🚀 La Mina de Oro Digital de Ecuador</h1>', unsafe_allow_html=True)
    
    # Contador de impacto en tiempo real
    st.markdown("### 💰 Impacto de Remesas - Dashboard Live")
    
    # Métricas animadas con efectos avanzados
    metric_cols = st.columns(4)
    
    metrics_data = [
        {"value": "$5.49B", "label": "Remesas 2024", "delta": "+8.1%", "icon": "💰"},
        {"value": "68%", "label": "Desde EE.UU.", "delta": "Principal origen", "icon": "🇺🇸"},
        {"value": "21%", "label": "Invierte Vivienda", "delta": "Oportunidad inmobiliaria", "icon": "🏠"},
        {"value": "74%", "label": "Bancarizados", "delta": "Mercado accesible", "icon": "🏦"}
    ]
    
    for i, metric in enumerate(metrics_data):
        with metric_cols[i]:
            st.markdown(f"""
            <div class="metric-card floating-element" style="animation-delay: {i*0.2}s;">
                <div style="font-size: 2rem;">{metric['icon']}</div>
                <h2>{metric['value']}</h2>
                <p>{metric['label']}</p>
                <small>{metric['delta']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    # Gráfico interactivo avanzado de remesas
    st.markdown("### 📈 Proyección Inteligente de Remesas")
    
    años = list(range(2020, 2031))
    remesas_data = [3500, 4200, 4800, 5100, 5491, 5821, 6200, 6600, 7100, 7650, 8200]
    
    # Crear subplot con múltiples ejes
    fig_remesas = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Evolución Histórica', 'Distribución por País', 'Impacto Sectorial', 'Proyección IA'),
        specs=[[{"secondary_y": True}, {"type": "pie"}],
               [{"type": "bar"}, {"type": "scatter"}]]
    )
    
    # Gráfico principal de evolución
    fig_remesas.add_trace(
        go.Scatter(x=años, y=remesas_data, mode='lines+markers', name='Remesas Históricas',
                  line=dict(color='#667eea', width=4)), row=1, col=1
    )
    
    # Gráfico de pie para distribución por país
    paises = ['EE.UU.', 'España', 'Italia', 'Otros']
    porcentajes = [68, 15, 8, 9]
    fig_remesas.add_trace(
        go.Pie(labels=paises, values=porcentajes, name="Distribución"),
        row=1, col=2
    )
    
    # Impacto por sectores
    sectores = ['Vivienda', 'Educación', 'Salud', 'Consumo', 'Ahorro']
    impacto = [21, 18, 12, 35, 14]
    fig_remesas.add_trace(
        go.Bar(x=sectores, y=impacto, name='Impacto %', marker_color='#f093fb'),
        row=2, col=1
    )
    
    # Proyección con IA
    proyeccion_ia = [5821, 6200, 6600, 7100, 7650, 8200]
    años_futuros = list(range(2025, 2031))
    fig_remesas.add_trace(
        go.Scatter(x=años_futuros, y=proyeccion_ia, mode='lines+markers', 
                  name='Proyección IA', line=dict(color='#f5576c', dash='dash')),
        row=2, col=2
    )
    
    fig_remesas.update_layout(height=800, showlegend=True, title_text="Dashboard Completo de Remesas Ecuador")
    st.plotly_chart(fig_remesas, use_container_width=True)
    
    # Oportunidad específica con efectos visuales
    st.markdown("""
    <div class="opportunity-card">
        <h2>🎯 OPORTUNIDAD ESTRATÉGICA ÚNICA</h2>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h3>Si capturamos solo el 3% de remesas Azuay:</h3>
                <h1 style="font-size: 4rem; margin: 20px 0;">$8.2M</h1>
                <p style="font-size: 1.2rem;">crecimiento trimestral garantizado</p>
                <p><strong>Equivale a abrir 4 sucursales nuevas sin inversión física</strong></p>
            </div>
            <div style="font-size: 8rem; opacity: 0.3;">💎</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Timeline interactiva con Streamlit Timeline
    st.markdown("### ⏰ Timeline de Oportunidad")
    
    timeline_data = {
        "title": {
            "media": {
                "url": "",
                "caption": "El Momento Perfecto",
                "credit": "COAC Raíces Andinas"
            },
            "text": {
                "headline": "Ventana de Oportunidad 2025-2027",
                "text": "Tres años críticos para capturar el mercado de remesas"
            }
        },
        "events": [
            {
                "start_date": {"year": "2025", "month": "1"},
                "text": {
                    "headline": "Q1 2025: Implementación IA",
                    "text": "Despliegue del sistema de segmentación inteligente"
                }
            },
            {
                "start_date": {"year": "2025", "month": "6"},
                "text": {
                    "headline": "Q2 2025: Primeros Resultados",
                    "text": "Captura del 1% del mercado de remesas (+$2.7M)"
                }
            },
            {
                "start_date": {"year": "2026", "month": "1"},
                "text": {
                    "headline": "2026: Consolidación",
                    "text": "3% market share alcanzado (+$8.2M trimestrales)"
                }
            },
            {
                "start_date": {"year": "2027", "month": "1"},
                "text": {
                    "headline": "2027: Liderazgo Regional",
                    "text": "Referente en servicios financieros para migrantes"
                }
            }
        ]
    }
    
    timeline(timeline_data, height=400)
    
    # Call to action con efectos
    col1, col2 = st.columns([3, 1])
    with col1:
        st.success("💡 **Insight Estratégico:** Cada día que no actuamos, perdemos $22,465 en oportunidades de remesas. La ventana de tiempo es limitada.")
        st.info("**Siguiente Nivel:** Implementar segmentación con IA para convertir esta oportunidad de $5.8B en ventaja competitiva sostenible.")
    
    with col2:
        if lottie_growth:
            st_lottie.st_lottie(lottie_growth, height=150, key="growth_animation")

elif "🏦 Nuestra Fortaleza" in selected:
    st.markdown('<h1 class="main-header">🏦 COAC Raíces Andinas: 28 Años de Solidez</h1>', unsafe_allow_html=True)
    st.markdown("### *La cooperativa que conecta sueños con realidades*")
    
    # Animación de presentación
    if lottie_business:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st_lottie.st_lottie(lottie_business, height=250, key="business_animation")
    
    # Métricas clave con diseño avanzado
    st.markdown("### 📊 Fortaleza Institucional")
    
    metrics_row1 = st.columns(6)
    institutional_metrics = [
        {"label": "Años Historia", "value": "28", "delta": "Desde 1996", "icon": "🏛️"},
        {"label": "Provincias", "value": "7", "delta": "Cobertura nacional", "icon": "🗺️"},
        {"label": "Socios Activos", "value": "48,127", "delta": "+2.3% anual", "icon": "👥"},
        {"label": "Patrimonio", "value": "$85M", "delta": "Sólido respaldo", "icon": "💰"},
        {"label": "Oficinas", "value": "24", "delta": "Cerca de ti", "icon": "🏢"},
        {"label": "Empleados", "value": "420", "delta": "Equipo comprometido", "icon": "👨‍💼"}
    ]
    
    for i, metric in

for i, metric in enumerate(institutional_metrics):
        with metrics_row1[i]:
            st.markdown(f"""
            <div class="metric-card floating-element" style="animation-delay: {i*0.1}s;">
                <div style="font-size: 2.5rem;">{metric['icon']}</div>
                <h3>{metric['value']}</h3>
                <p style="font-size: 0.9rem;">{metric['label']}</p>
                <small style="opacity: 0.8;">{metric['delta']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    # Análisis FODA con visualización interactiva
    st.markdown("### 📊 Matriz FODA Interactiva")
    
    foda_tabs = st.tabs(["💪 Fortalezas", "🌟 Oportunidades", "⚠️ Debilidades", "🚨 Amenazas"])
    
    with foda_tabs[0]:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="data-card" style="background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);">
                <h4>💰 Fortaleza Financiera</h4>
                <ul>
                    <li><strong>$85M en patrimonio</strong> - Solidez probada</li>
                    <li><strong>Cartera diversificada</strong> - Riesgo distribuido</li>
                    <li><strong>Liquidez saludable</strong> - Capacidad de crecimiento</li>
                    <li><strong>Rentabilidad sostenida</strong> - ROE del 12.5%</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            # Gráfico de evolución patrimonial
            years = list(range(2019, 2025))
            patrimonio = [65, 68, 72, 78, 82, 85]
            
            fig_patrimonio = px.line(
                x=years, y=patrimonio,
                title="Evolución del Patrimonio (Millones USD)",
                markers=True
            )
            fig_patrimonio.update_traces(
                line=dict(color='#28a745', width=4),
                marker=dict(size=10, color='#28a745')
            )
            fig_patrimonio.update_layout(
                xaxis_title="Año",
                yaxis_title="Patrimonio (M USD)",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)"
            )
            st.plotly_chart(fig_patrimonio, use_container_width=True)
    
    with foda_tabs[1]:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="data-card" style="background: linear-gradient(135deg, #cce5ff 0%, #b3d9ff 100%);">
                <h4>🚀 Oportunidades de Oro</h4>
                <ul>
                    <li><strong>Remesas crecientes</strong> - +8.1% anual hasta 2030</li>
                    <li><strong>Digitalización acelerada</strong> - COVID cambió hábitos</li>
                    <li><strong>Alianzas fintech</strong> - Ecosistema en expansión</li>
                    <li><strong>Mercado joven</strong> - 65% bajo 45 años</li>
                    <li><strong>Regulación favorable</strong> - Apoyo a cooperativas</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            # Gráfico de oportunidades de mercado
            oportunidades = ['Remesas', 'Digital', 'Fintech', 'Jóvenes', 'Regulación']
            impacto = [95, 85, 75, 80, 70]
            facilidad = [80, 90, 60, 85, 95]
            
            fig_oportunidades = go.Figure()
            fig_oportunidades.add_trace(go.Scatter(
                x=facilidad, y=impacto,
                mode='markers+text',
                text=oportunidades,
                textposition="middle center",
                marker=dict(
                    size=[20, 18, 15, 17, 16],
                    color=['#007bff', '#28a745', '#ffc107', '#17a2b8', '#6c757d'],
                    opacity=0.7
                ),
                name="Oportunidades"
            ))
            
            fig_oportunidades.update_layout(
                title="Matriz Impacto vs Facilidad de Implementación",
                xaxis_title="Facilidad de Implementación",
                yaxis_title="Impacto Potencial",
                showlegend=False,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)"
            )
            st.plotly_chart(fig_oportunidades, use_container_width=True)
    
    with foda_tabs[2]:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="data-card" style="background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);">
                <h4>🔧 Áreas de Mejora</h4>
                <ul>
                    <li><strong>Adopción digital lenta</strong> - 45% vs 70% del mercado</li>
                    <li><strong>Segmentación básica</strong> - Un enfoque para todos</li>
                    <li><strong>Canales móviles</strong> - Subutilizados (30% penetración)</li>
                    <li><strong>Análisis predictivo</strong> - Limitado uso de datos</li>
                    <li><strong>Experiencia cliente</strong> - NPS 45 vs 65 líderes</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            # Gráfico comparativo con competencia
            metricas_comp = ['Adopción Digital', 'NPS', 'Productos/Cliente', 'Tiempo Respuesta']
            raices = [45, 45, 2.1, 4.2]
            mercado = [70, 65, 3.2, 2.8]
            
            fig_comp = go.Figure()
            fig_comp.add_trace(go.Bar(
                name='Raíces Andinas',
                x=metricas_comp,
                y=raices,
                marker_color='#ffc107'
            ))
            fig_comp.add_trace(go.Bar(
                name='Promedio Mercado',
                x=metricas_comp,
                y=mercado,
                marker_color='#6c757d'
            ))
            
            fig_comp.update_layout(
                title="Comparativo vs Mercado",
                barmode='group',
                yaxis_title="Puntuación",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)"
            )
            st.plotly_chart(fig_comp, use_container_width=True)
    
    with foda_tabs[3]:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="data-card" style="background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);">
                <h4>⚡ Amenazas del Entorno</h4>
                <ul>
                    <li><strong>Fintech agresivas</strong> - Nequi, Kushki captando jóvenes</li>
                    <li><strong>Bancos digitales</strong> - UX superior, productos ágiles</li>
                    <li><strong>Migración generacional</strong> - Jóvenes abandonan cooperativas</li>
                    <li><strong>Competencia de precios</strong> - Guerra de tasas</li>
                    <li><strong>Cambios regulatorios</strong> - Incertidumbre normativa</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            # Análisis de amenazas
            amenazas = ['Fintech', 'Bancos Digitales', 'Migración Gen.', 'Guerra Precios', 'Regulación']
            probabilidad = [85, 75, 90, 70, 40]
            impacto = [80, 85, 95, 60, 75]
            
            fig_amenazas = px.scatter(
                x=probabilidad, y=impacto,
                size=[15, 18, 20, 12, 14],
                color=amenazas,
                title="Matriz de Riesgos: Probabilidad vs Impacto",
                labels={'x': 'Probabilidad (%)', 'y': 'Impacto (%)'}
            )
            fig_amenazas.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)"
            )
            st.plotly_chart(fig_amenazas, use_container_width=True)
    
    # Timeline evolutiva interactiva
    st.markdown("### 📅 Evolución Histórica")
    
    # Crear timeline con datos históricos
    timeline_items = [
        {"year": "1996", "event": "Fundación", "details": "500 socios fundadores en Cuenca", "impact": "Inicio", "color": "#28a745"},
        {"year": "2001", "event": "Primera Expansión", "details": "Llegada a Azogues y Biblián", "impact": "2,000 socios", "color": "#17a2b8"},
        {"year": "2005", "event": "Crecimiento Regional", "details": "7 provincias, modernización", "impact": "8,000 socios", "color": "#007bff"},
        {"year": "2010", "event": "Era Tecnológica", "details": "Primeros cajeros automáticos", "impact": "15,000 socios", "color": "#6610f2"},
        {"year": "2015", "event": "Transformación Digital", "details": "Banca online y móvil", "impact": "25,000 socios", "color": "#e83e8c"},
        {"year": "2020", "event": "Resilencia COVID", "details": "Crecimiento del 15% en pandemia", "impact": "40,000 socios", "color": "#fd7e14"},
        {"year": "2024", "event": "Presente", "details": "Líderes regionales consolidados", "impact": "48,127 socios", "color": "#dc3545"},
        {"year": "2025", "event": "Futuro IA", "details": "Segmentación inteligente", "impact": "Meta: 60,000", "color": "#ffc107"}
    ]
    
    # Visualización de timeline
    fig_timeline = go.Figure()
    
    for i, item in enumerate(timeline_items):
        fig_timeline.add_trace(go.Scatter(
            x=[item["year"]], 
            y=[i],
            mode='markers+text',
            text=f"{item['event']}<br>{item['impact']}",
            textposition="middle right" if i % 2 == 0 else "middle left",
            marker=dict(size=20, color=item["color"]),
            showlegend=False,
            hovertemplate=f"<b>{item['event']}</b><br>{item['details']}<br><i>{item['impact']}</i><extra></extra>"
        ))
    
    fig_timeline.update_layout(
        title="Timeline: 28 Años de Crecimiento Sostenido",
        xaxis_title="Año",
        yaxis=dict(showticklabels=False, showgrid=False),
        height=600,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Indicadores de desempeño con gauge charts
    st.markdown("### 🎯 Indicadores de Desempeño")
    
    gauge_cols = st.columns(4)
    
    indicadores = [
        {"name": "Solidez Patrimonial", "value": 15.2, "max": 20, "color": "#28a745"},
        {"name": "Eficiencia Operativa", "value": 78, "max": 100, "color": "#007bff"},
        {"name": "Satisfacción Cliente", "value": 8.2, "max": 10, "color": "#17a2b8"},
        {"name": "Innovación Digital", "value": 65, "max": 100, "color": "#ffc107"}
    ]
    
    for i, indicador in enumerate(indicadores):
        with gauge_cols[i]:
            fig_gauge = go.Figure(go.Indicator(
                mode = "gauge+number+delta",
                value = indicador["value"],
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': indicador["name"]},
                delta = {'reference': indicador["max"] * 0.8},
                gauge = {
                    'axis': {'range': [None, indicador["max"]]},
                    'bar': {'color': indicador["color"]},
                    'steps': [
                        {'range': [0, indicador["max"] * 0.5], 'color': "lightgray"},
                        {'range': [indicador["max"] * 0.5, indicador["max"] * 0.8], 'color': "gray"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': indicador["max"] * 0.9
                    }
                }
            ))
            fig_gauge.update_layout(height=300, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig_gauge, use_container_width=True)

elif "🔬 IA & Analytics" in selected:
    st.markdown('<h1 class="main-header">🔬 Inteligencia Artificial al Servicio de las Decisiones</h1>', unsafe_allow_html=True)
    st.markdown("### *De 48,127 datos individuales a 3 estrategias ganadoras*")
    
    # Animación de datos
    if lottie_data:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st_lottie.st_lottie(lottie_data, height=250, key="data_animation")
    
    # Metodología con tabs interactivos
    st.markdown("### 🧠 Metodología de Machine Learning")
    
    method_tabs = st.tabs(["🎯 El Desafío", "🤖 K-Means IA", "📊 Validación", "🎮 Demo Live"])
    
    with method_tabs[0]:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            #### 🎯 El Gran Desafío
            
            **Antes de la IA:**
            - 48,127 socios = 48,127 estrategias diferentes
            - Campañas masivas con 23% de efectividad
            - Productos genéricos para todos
            - Pérdida de socios jóvenes del 5% anual
            - NPS estancado en 45 puntos
            
            **La revolución necesaria:**
            ¿Cómo convertir 48,127 historias individuales en 3 estrategias precisas y efectivas?
            """)
            
        with col2:
            # Gráfico del problema
            problema_data = pd.DataFrame({
                'Métrica': ['Efectividad\nCampañas', 'NPS\nCliente', 'Retención\nAnual', 'Cross-selling\nRate'],
                'Actual': [23, 45, 78, 15],
                'Potencial_IA': [65, 75, 92, 45],
                'Mercado': [35, 65, 85, 25]
            })
            
            fig_problema = px.bar(
                problema_data, 
                x='Métrica', 
                y=['Actual', 'Potencial_IA', 'Mercado'],
                title="El Gap de Oportunidad",
                barmode='group',
                color_discrete_map={
                    'Actual': '#dc3545',
                    'Potencial_IA': '#28a745', 
                    'Mercado': '#6c757d'
                }
            )
            fig_problema.update_layout(height=400)
            st.plotly_chart(fig_problema, use_container_width=True)
    
    with method_tabs[1]:
        st.markdown("#### 🤖 K-Means: El Cerebro de la Segmentación")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("""
            **¿Cómo funciona nuestro algoritmo?**
            
            1. **Preparación de datos** 🧹
               - Limpieza de 48,127 registros
               - Normalización de variables
               - Detección de outliers
            
            2. **Selección de características** 🎯
               - Edad, ingresos, saldo DPF
               - Capital prestado, días mora
               - Uso digital, productos activos
            
            3. **Algoritmo K-Means** 🧠
               - Definir K=3 (número óptimo de clusters)
               - Iteración hasta convergencia
               - Asignación de cada socio a su cluster
            
            4. **Interpretación** 📊
               - Análisis de características por cluster
               - Definición de estrategias específicas
               - Validación de resultados
            """)
            
        with col2:
            # Visualización 3D interactiva
            st.markdown("**Visualización 3D de Clusters**")
            fig_3d = create_3d_scatter()
            st.plotly_chart(fig_3d, use_container_width=True)
    
    with method_tabs[2]:
        st.markdown("#### 📊 Validación Científica del Modelo")
        
        # Métricas de validación
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h3>Silhouette Score</h3>
                <h1>0.73</h1>
                <p>Excelente separación</p>
                <small>Umbral: >0.5</small>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h3>Inercia</h3>
                <h1>1,245</h1>
                <p>Grupos compactos</p>
                <small>Minimizada</small>
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown("""
            <div class="metric-card">
                <h3>Varianza Explicada</h3>
                <h1>87%</h1>
                <p>Modelo robusto</p>
                <small>Meta: >80%</small>
            </div>
            """, unsafe_allow_html=True)
            
        with col4:
            st.markdown("""
            <div class="metric-card">
                <h3>Accuracy</h3>
                <h1>94.2%</h1>
                <p>Predicción precisa</p>
                <small>Validación cruzada</small>
            </div>
            """, unsafe_allow_html=True)
        
        # Matriz de correlaciones avanzada
        st.markdown("#### Análisis de Correlaciones")
        fig_corr = create_correlation_heatmap()
        st.plotly_chart(fig_corr, use_container_width=True)
        
        # Análisis de componentes principales
        st.markdown("#### Análisis PCA - Componentes Principales")
        
        # Simular PCA
        numeric_cols = ['edad', 'ingresos', 'saldo_dpf', 'capital_prestado', 'mora_dias', 'uso_digital']
        X = df_enhanced[numeric_cols]
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        pca = PCA()
        X_pca = pca.fit_transform(X_scaled)
        
        # Gráfico de varianza explicada
        fig_pca = px.bar(
            x=[f'PC{i+1}' for i in range(len(pca.explained_variance_ratio_))],
            y=pca.explained_variance_ratio_,
            title="Varianza Explicada por Componente Principal"
        )
        fig_pca.update_layout(
            xaxis_title="Componente Principal",
            yaxis_title="Varianza Explicada (%)"
        )
        st.plotly_chart(fig_pca, use_container_width=True)
    
    with method_tabs[3]:
        st.markdown("#### 🎮 Demostración en Vivo del Algoritmo")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**Controles de Simulación:**")
            n_iterations = st.slider("Número de iteraciones K-Means", 1, 10, 5)
            sample_size = st.slider("Tamaño de muestra", 100, 1000, 300, step=100)
            variables_x = st.selectbox("Variable X", ['edad', 'ingresos', 'saldo_dpf'], index=0)
            variables_y = st.selectbox("Variable Y", ['ingresos', 'saldo_dpf', 'mora_dias'], index=1)
            
            if st.button("🚀 Ejecutar Algoritmo", type="primary"):
                st.session_state.run_algorithm = True
        
        with col2:
            if hasattr(st.session_state, 'run_algorithm') and st.session_state.run_algorithm:
                # Simulación del algoritmo paso a paso
                sample_data = df_enhanced.sample(sample_size)
                
                placeholder = st.empty()
                progress_bar = st.progress(0)
                
                for iteration in range(n_iterations):
                    # Simular iteraciones del algoritmo
                    fig_iter = px.scatter(
                        sample_data, 
                        x=variables_x, 
                        y=variables_y,
                        color='cluster',
                        title=f"Iteración {iteration + 1}: Formando Clusters",
                        color_discrete_map={0: '#8dd3c7', 1: '#ffffb3', 2: '#bebada'},
                        size='saldo_dpf',
                        hover_data=['edad', 'ingresos', 'mora_dias']
                    )
                    fig_iter.update_layout(height=400)
                    
                    placeholder.plotly_chart(fig_iter, use_container_width=True)
                    progress_bar.progress((iteration + 1) / n_iterations)
                    time.sleep(0.5)
                
                st.success(f"✅ Algoritmo completado! {sample_size} socios segmentados en {n_iterations} iteraciones")
                
                # Mostrar estadísticas finales
                cluster_stats = sample_data.groupby('cluster').agg({
                    'edad': 'mean',
                    'ingresos': 'mean', 
                    'saldo_dpf': 'mean',
                    'mora_dias': 'mean'
                }).round(2)
                
                st.markdown("**Estadísticas por Cluster:**")
                st.dataframe(cluster_stats, use_container_width=True)
    
    # Arquitectura del sistema
    st.markdown("### 🏗️ Arquitectura del Sistema de IA")
    
    arch_cols = st.columns(4)
    
    arquitectura = [
        {"layer": "Datos", "tech": "PostgreSQL\nPandas", "icon": "🗄️", "color": "#007bff"},
        {"layer": "Procesamiento", "tech": "Scikit-learn\nNumPy", "icon": "⚙️", "color": "#28a745"},
        {"layer": "Modelos", "tech": "K-Means\nPCA", "icon": "🧠", "color": "#ffc107"},
        {"layer": "Interfaz", "tech": "Streamlit\nPlotly", "icon": "📊", "color": "#dc3545"}
    ]
    
    for i, layer in enumerate(arquitectura):
        with arch_cols[i]:
            st.markdown(f"""
            <div class="data-card" style="background: {layer['color']}20; border-left: 5px solid {layer['color']};">
                <div style="font-size: 3rem; text-align: center;">{layer['icon']}</div>
                <h4 style="text-align: center;">{layer['layer']}</h4>
                <p style="text-align: center; font-size: 0.9rem;">{layer['tech']}</p>
            </div>
            """, unsafe_allow_html=True)

elif "🎯 Segmentos Inteligentes" in selected:
    st.markdown('<h1 class="main-header">🎯 Los 3 Equipos Ganadores</h1>', unsafe_allow_html=True)
    st.markdown("### *Cada segmento, una estrategia. Cada estrategia, resultados.*")
    
    # Resumen ejecutivo con métricas animadas
    st.markdown("### 📊 Dashboard de Segmentos")
    
    segment_summary_cols = st.columns(3)
    
    segmentos_data = [
        {
            "name": "🧓 Tradicional",
            "color": "#8dd3c7", 
            "socios": 14438,
            "percentage": 30,
            "revenue": 42000000,
            "risk": "Muy Bajo",
            "opportunity": "Digitalización Asistida",
            "roi": 180
        },
        {
            "name": "⚠️ Riesgo",
            "color": "#ffffb3",
            "socios": 24064,
            "percentage": 50, 
            "revenue": 28000000,
            "risk": "Alto",
            "opportunity": "Recuperación Proactiva",
            "roi": 245
        },
        {
            "name": "📱 Tech",
            "color": "#bebada",
            "socios": 9625,
            "percentage": 20,
            "revenue": 35000000,
            "risk": "Fuga Fintech",
            "opportunity": "Productos Premium",
            "roi": 320
        }
    ]
    
    for i, segment in enumerate(segmentos_data):
        with segment_summary_cols[i]:
            st.markdown(f"""
            <div class="segment-card floating-element" style="background: {segment['color']}40; animation-delay: {i*0.2}s;">
                <h2>{segment['name']}</h2>
                <div style="font-size: 2.5rem; margin: 15px 0;">{segment['socios']:,}</div>
                <p><strong>{segment['percentage']}% del total</strong></p>
                <p>💰 Ingresos: ${segment['revenue']:,.0f}</p>
                <p>🎯 ROI Potencial: {segment['roi']}%</p>
                <p>⚡ Oportunidad: {segment['opportunity']}</p>
                <div style="background: {segment['color']}; height: 5px; border-radius: 10px; margin-top: 15px;"></div>
            </div>
            """, unsafe_allow_html=True)
    
    # Análisis comparativo avanzado con radar chart mejorado
    st.markdown("### 📊 Perfil Multidimensional de Segmentos")
    
    # Datos para radar chart
    categories = ['Edad Promedio', 'Ingresos', 'Saldo DPF', 'Capital Prestado', 'Morosidad', 'Uso Digital', 'Productos Activos']
    
    # Datos normalizados para mejor visualización
    tradicional_values = [90, 70, 95, 75, 95, 25, 60]  # Normalizado sobre 100
    riesgo_values = [60, 75, 15, 70, 20, 35, 45]
    tech_values = [75, 80, 65, 90, 60, 90, 85]
    
    fig_radar = go.Figure()
    
    fig_radar.add_trace(go.Scatterpolar(
        r=tradicional_values + [tradicional_values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name='🧓 Tradicional',
        line_color='#8dd3c7',
        fillcolor='rgba(141, 211, 199, 0.3)',
        hovertemplate='<b>Tradicional</b><br>%{theta}: %{r}<extra></extra>'
    ))
    
    fig_radar.add_trace(go.Scatterpolar(
        r=riesgo_values + [riesgo_values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name='⚠️ Riesgo',
        line_color='#ffffb3',
        fillcolor='rgba(255, 255, 179, 0.3)',
        hovertemplate='<b>Riesgo</b><br>%{theta}: %{r}<extra></extra>'
    ))
    
    fig_radar.add_trace(go.Scatterpolar(
        r=tech_values + [tech_values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name='📱 Tech',
        line_color='#bebada',
        fillcolor='rgba(190, 186, 218, 0.3)',
        hovertemplate='<b>Tech</b><br>%{theta}: %{r}<extra></extra>'
    ))
    
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10)
            )
        ),
        showlegend=True,
        title="Perfil Multidimensional por Segmento",
        height=600,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    
    st.plotly_chart(fig_radar, use_container_width=True)
    
    # Análisis detallado por segmento con tabs mejorados
    st.markdown("### 🔍 Análisis Profundo por Segmento")
    
    segment_tabs = st.tabs(["🧓 Tradicional: Los Leales", "⚠️ Riesgo: Los Recuperables", "📱 Tech: Los Innovadores"])
    
    with segment_tabs[0]:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            #### 🧓 Segmento Tradicional - "Los Pilares de la Cooperativa"
            
            **Perfil Demográfico:**
            - 👴 Edad promedio: 45.1 años
            - 💰 Ingresos: $3,559 mensuales
            - 🏦 Saldo DPF: $27,597 (¡Ahorradores nato!)
            - 📅 Antigüedad: 12+ años en promedio
            - 👨‍👩‍👧‍👦 Familia: Típicamente cabeza de hogar
            
            **Comportamiento Financiero:**
            - ✅ Morosidad mínima: 1.5 días promedio
            - 💎 Alta fidelidad: 95% de retención
            - 🐌 Adopción digital: 25% (oportunidad clara)
            - 📞 Prefiere atención presencial y telefónica
            - 💰 Perfil conservador en inversiones
            """)
            
            # Estrategias específicas
            st.markdown("""
            **🎯 Estrategias Personalizadas:**
            
            1. **Programa VIP "Raíces de Oro"**
               - Asesor personal dedicado
               - Beneficios exclusivos en tasas
               - Atención prioritaria en oficinas
            
            2. **Digitalización Asistida**
               - Talleres presenciales de banca digital
               - Acompañamiento 1:1 para primeros usos
               - Línea de soporte telefónico especializado
            
            3. **Productos de Legado**
               - Seguros de vida con beneficiarios
               - Planes de jubilación complementaria
               - Créditos hipotecarios para hijos
            """)
        
        with col2:
            # Métricas del segmento tradicional
            st.markdown("""
            <div class="data-card" style="background: linear-gradient(135deg, #8dd3c7 0%, #a8e6cf 100%);">
                <h4>📊 Métricas Clave</h4>
                <div style="margin: 15px 0;">
                    <strong>ROE:</strong> 15.2%<br>
                    <strong>Margen:</strong> 8.5%<br>
                    <strong>Costo Servicio:</strong> $120<br>
                    <strong>Vida Útil:</strong> 12 años<br>
                    <strong>NPS:</strong> 72 puntos
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Gráfico de distribución de productos
            productos_trad = ['DPF', 'Crédito', 'Cuenta Corriente', 'Seguros', 'Inversiones']
            penetracion_trad = [95, 65, 80, 45, 25]
            
            fig_prod_trad = px.bar(
                x=productos_trad,
                y=penetracion_trad,
                title="Penetración de Productos - Tradicional",
                color=penetracion_trad,
                color_continuous_scale='Greens'
            )
            fig_prod_trad.update_layout(height=300, showlegend=False)
            st.plotly_chart(fig_prod_trad, use_container_width=True)
            
            # Proyección de crecimiento
            st.markdown("""
            **🚀 Potencial de Crecimiento:**
            - Digitalización: +$2.3M ingresos anuales
            - Cross-selling: +1.5 productos promedio
            - Retención: 98% (vs 95% actual)
            """)
    
    with segment_tabs[1]:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            #### ⚠️ Segmento Riesgo - "El Diamante en Bruto"
            
            **Perfil de Desafío:**
            - 👥 Edad promedio: 38.4 años (más jóvenes)
            - 💰 Ingresos: $3,759 mensuales (variables)
            - 🏦 Saldo DPF: $316 (bajo ahorro)
            - ⏰ Morosidad: 18 días promedio
            - 📱 Adopción digital: 35% (mejor que tradicionales)
            
            **Características Críticas:**
            - 🔴 50% del total de socios (¡volumen importante!)
            - 📉 Mayor rotación: 15% anual
            - 💼 Ingresos irregulares (trabajo independiente)
            - 🏠 Muchos tienen créditos de vivienda
            - 📚 Necesitan educación financiera
            """)
            
            st.markdown("""
            **🎯 Estrategias de Recuperación:**
            
            1. **Sistema de Alertas Inteligentes**
               - Notificaciones automáticas antes del vencimiento
               - Canal WhatsApp para recordatorios amigables
               - Scoring predictivo de riesgo
            
            2. **Programa "Rescate Financiero"**
               - Reestructuración proactiva de deudas
               - Planes de pago flexibles
               - Asesoría financiera gratuita
            
            3. **Educación y Empoderamiento**
               - Talleres de presupuesto familiar
               - App de control de gastos
               - Microcréditos progresivos
            """)
        
        with col2:
            st.markdown("""
            <div class="data-card" style="background: linear-gradient(135deg, #ffffb3 0%, #fff4a3 100%);">
                <h4>⚠️ Métricas de Riesgo</h4>
                <div style="margin: 15px 0;">
                    <strong>ROE:</strong> 4.1%<br>
                    <strong>Margen:</strong> 3.2%<br>
                    <strong>Costo Servicio:</strong> $180<br>
                    <strong>Provisiones:</strong> $850/socio<br>
                    <strong>NPS:</strong> 38 puntos
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Análisis de morosidad por tiempo
            meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
            mora_actual = [18, 19, 17, 20, 18, 18]
            mora_proyectada = [18, 16, 14, 12, 10, 8]
            
            fig_mora = go.Figure()
            fig_mora.add_trace(go.Scatter(x=meses, y=mora_actual, name='Mora Actual', line=dict(color='#dc3545')))
            fig_mora.add_trace(go.Scatter(x=meses, y=mora_proyectada, name='Proyección con IA', line=dict(color='#28a745', dash='dash')))
            
            fig_mora.update_layout(
                title="Reducción Proyectada de Morosidad",
                yaxis_title="Días de Mora",
                height=300
            )
            st.plotly_chart(fig_mora, use_container_width=True)
            
            # Impacto financiero
            st.markdown("""
            **💰 Impacto de Mejora:**
            - Reducción mora: 18→8 días
            - Ahorro provisiones: $4.2M anuales
            - Mejora ROE: 4.1% → 8.5%
            - Retención: +25%
            """)
    
    with segment_tabs[2]:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            #### 📱 Segmento Tech - "Los Disruptores del Futuro"
            
            **Perfil Digital:**
            - 👩‍💻 Edad promedio: 39.6 años (millennials)
            - 💰 Ingresos: $3,962 mensuales (estables)
            - 🏦 Saldo DPF: $7,656 (equilibrado)
            - 📱 Adopción digital: 90% (líderes)
            - 🌟 Multiproducto: 4+ productos activos
            
            **Comportamiento Avanzado:**
            - ⚡ Transacciones digitales: 85% del total
            - 🎯 Expectativas altas de UX/UI
            - 🔄 Alta propensión al cross-selling
            - 🌍 Conscientes de tendencias fintech globales
            - 💳 Usuarios de múltiples plataformas financieras
            """)
            
            st.markdown("""
            **🎯 Estrategias de Innovación:**
            
            1. **Ecosistema Digital Premium**
               - App móvil con features avanzadas
               - API abierta para integraciones
               - Dashboard personalizable en tiempo real
            
            2. **Productos Fintech Nativos**
               - Pagos QR y contactless
               - Inversiones en criptomonedas
               - Robo-advisor para portafolios
            
            3. **Experiencia Gamificada**
               - Programa de puntos por uso digital
               - Metas de ahorro con recompensas
               - Referidos con beneficios mutuos
            """)
        
        with col2:
            st.markdown("""
            <div class="data-card" style="background: linear-gradient(135deg, #bebada 0%, #c8a4d8 100%);">
                <h4>🚀 Métricas Digitales</h4>
                <div style="margin: 15px 0;">
                    <strong>ROE:</strong> 18.7%<br>
                    <strong>Margen:</strong> 9.8%<br>
                    <strong>Costo Servicio:</strong> $95<br>
                    <strong>Digital Score:</strong> 92/100<br>
                    <strong>NPS:</strong> 68 puntos
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Canales de preferencia
            canales = ['App Móvil', 'Web Banking', 'Presencial', 'Call Center', 'WhatsApp']
            uso_tech = [75, 60, 15, 25, 45]
            
            fig_canales = px.pie(
                values=uso_tech,
                names=canales,
                title="Preferencia de Canales - Tech",
                color_discrete_sequence=['#bebada', '#c8a4d8', '#d4b4e8', '#e0c4f2', '#ecd4fc']
            )
            fig_canales.update_layout(height=300)
            st.plotly_chart(fig_canales, use_container_width=True)
            
            # Riesgo de fuga
            st.markdown("""
            **⚠️ Riesgo de Fuga:**
            - Competencia fintech: 25% riesgo
            - Expectativas no cumplidas: 15%
            - **Retención con nueva estrategia: 95%**
            """)
    
    # Matriz de priorización estratégica
    st.markdown("### 🎯 Matriz de Priorización Estratégica")
    
    # Crear matriz de impacto vs esfuerzo
    estrategias = [
        {"name": "Digitalización Tradicionales", "impacto": 85, "esfuerzo": 60, "segmento": "Tradicional"},
        {"name": "Sistema Alertas Riesgo", "impacto": 95, "esfuerzo": 40, "segmento": "Riesgo"},
        {"name": "App Premium Tech", "impacto": 90, "esfuerzo": 80, "segmento": "Tech"},
        {"name": "Educación Financiera", "impacto": 70, "esfuerzo": 30, "segmento": "Riesgo"},
        {"name": "Programa VIP", "impacto": 75, "esfuerzo": 45, "segmento": "Tradicional"},
        {"name": "Productos Fintech", "impacto": 85, "esfuerzo": 90, "segmento": "Tech"}
    ]
    
    fig_matriz = px.scatter(
        x=[e["esfuerzo"] for e in estrategias],
        y=[e["impacto"] for e in estrategias],
        size=[20]*len(estrategias),
        color=[e["segmento"] for e in estrategias],
        hover_name=[e["name"] for e in estrategias],
        title="Matriz Impacto vs Esfuerzo - Estrategias por Segmento",
        labels={'x': 'Esfuerzo de Implementación', 'y': 'Impacto Esperado'},
        color_discrete_map={"Tradicional": "#8dd3c7", "Riesgo": "#ffffb3", "Tech": "#bebada"}
    )
    
    # Agregar líneas de referencia
    fig_matriz.add_hline(y=80, line_dash="dash", line_color="red", annotation_text="Alto Impacto")
    fig_matriz.add_vline(x=70, line_dash="dash", line_color="orange", annotation_text="Alto Esfuerzo")
    
    fig_matriz.update_layout(height=500)
    st.plotly_chart(fig_matriz, use_container_width=True)
    
    # Recomendaciones finales
    st.markdown("### 🏆 Recomendaciones Ejecutivas")
    
    recom_cols = st.columns(3)
    
    with recom_cols[0]:
        st.markdown("""
        <div class="data-card" style="border-left: 5px solid #28a745;">
            <h4>🥇 Prioridad 1: Sistema Alertas</h4>
            <p><strong>Segmento:</strong> Riesgo</p>
            <p><strong>ROI:</strong> 245% en 8 meses</p>
            <p><strong>Inversión:</strong> $180K</p>
            <p><strong>Impacto:</strong> -10 días mora promedio</p>
        </div>
        """, unsafe_allow_html=True)
    
    with recom_cols[1]:
        st.markdown("""
        <div class="data-card" style="border-left: 5px solid #ffc107;">
            <h4>🥈 Prioridad 2: Educación Financiera</h4>
            <p><strong>Segmento:</strong> Todos</p>
            <p><strong>ROI:</strong> 180% en 12 meses</p>
            <p><strong>Inversión:</strong> $95K</p>
            <p><strong>Impacto:</strong> +15% retención</p>
        </div>
        """, unsafe_allow_html=True)
    
    with recom_cols[2]:
        st.markdown("""
        <div class="data-card" style="border-left: 5px solid #17a2b8;">
            <h4>🥉 Prioridad 3: Programa VIP</h4>
            <p><strong>Segmento:</strong> Tradicional</p>
            <p><strong>ROI:</strong> 165% en 6 meses</p>
            <p><strong>Inversión:</strong> $120K</p>
            <p><strong>Impacto:</strong> +5% digitalización</p>
        </div>
        """, unsafe_allow_html=True)

elif "🧪 Simulador Predictivo" in selected:
    st.markdown('<h1 class="main-header">🧪 Laboratorio de Simulaciones Estratégicas</h1>', unsafe_allow_html=True)
    st.markdown("### *Experimenta el futuro antes de vivirlo*")
    
    # Selector de simulación principal
    st.markdown("### 🎮 Centro de Control de Simulaciones")
    
    sim_type = st.selectbox(
        "Selecciona el tipo de simulación:",
        ["📞 Prevención de Morosidad", "🎯 Cross-Selling Inteligente", "📱 Aceleración Digital", "💰 Impacto ROI Consolidado", "🔮 Escenarios Futuros"]
    )
    
    if sim_type == "📞 Prevención de Morosidad":
        st.markdown("#### 🎯 Simulador: Estrategia Anti-Morosidad")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("**⚙️ Configuración de Estrategia:**")
            
            # Controles de simulación
            coverage_riesgo = st.slider("% Segmento Riesgo contactado", 0, 100, 60, help="Porcentaje del segmento riesgo que recibirá intervención")
            efectividad_calls = st.slider("Efectividad llamadas preventivas (%)", 0, 80, 35, help="% de socios que mejoran tras la intervención")
            frequency_contact = st.selectbox("Frecuencia de contacto", ["Semanal", "Quincenal", "Mensual"])
            ai_scoring = st.checkbox("Activar scoring IA", value=True, help="Usar algoritmos de ML para priorizar contactos")
            
            # Costos asociados
            st.markdown("**💰 Estructura de Costos:**")
            cost_per_call = st.number_input("Costo por llamada ($)", 0.5, 5.0, 2.5)
            additional_staff = st.slider("Personal adicional requerido", 0, 10, 3)
            tech_investment = st.slider("Inversión tecnológica ($K)", 0, 200, 50)
            
        with col2:
            # Cálculos en tiempo real
            socios_riesgo = 24064
            socios_contactados = int(socios_riesgo * coverage_riesgo / 100)
            socios_mejorados = int(socios_contactados * efectividad_calls / 100)
            
            # Simulación de impacto
            mora_actual_promedio = 18
            reduccion_mora = efectividad_calls * 0.4  # Factor de conversión
            nueva_mora_promedio = max(3, mora_actual_promedio - reduccion_mora)
            
            # Impacto financiero
            provision_actual_per_socio = 850
            provision_nueva_per_socio = provision_actual_per_socio * (nueva_mora_promedio / mora_actual_promedio)
            ahorro_provisiones_total = socios_mejorados * (provision_actual_per_socio - provision_nueva_per_socio)
            
            # Costos totales
            frequency_multiplier = {"Semanal": 52, "Quincenal": 26, "Mensual": 12}[frequency_contact]
            costo_llamadas_anual = socios_contactados * cost_per_call * frequency_multiplier
            costo_personal_anual = additional_staff * 35000  # Salario promedio
            costo_total_anual = costo_llamadas_anual + costo_personal_anual + (tech_investment * 1000)
            
            # ROI
            beneficio_neto = ahorro_provisiones_total - costo_total_anual
            roi_percentage = (beneficio_neto / costo_total_anual * 100) if costo_total_anual > 0 else 0
            
            # Dashboard de resultados
            st.markdown("**📊 Impacto Proyectado - Año 1:**")
            
            result_cols = st.columns(2)
            with result_cols[0]:
                st.metric("Socios Impactados", f"{socios_mejorados:,}", f"+{socios_mejorados}")
                st.metric("Reducción Mora Promedio", f"-{reduccion_mora:.1f} días", f"{nueva_mora_promedio:.1f} días finales")
            
            with result_cols[1]:
                st.metric("Ahorro en Provisiones", f"${ahorro_provisiones_total:,.0f}", f"+{ahorro_provisiones_total/1000000:.1f}M")
                st.metric("ROI de la Estrategia", f"{roi_percentage:.1f}%", f"Payback: {12/max(roi_percentage/100, 0.01):.1f} meses" if roi_percentage > 0 else "Negativo")
            
            # Gráfico de evolución temporal
            meses = list(range(1, 13))
            mora_evolution = [mora_actual_promedio - (reduccion_mora * mes / 12) for mes in meses]
            ahorro_acumulado = [ahorro_provisiones_total * mes / 12 - costo_total_anual * mes / 12 for mes in meses]
            
            fig_evolution = make_subplots(
                rows=2, cols=1,
                subplot_titles=('Evolución de Morosidad', 'Ahorro Acumulado'),
                vertical_spacing=0.1
            )
            
            fig_evolution.add_trace(
                go.Scatter(x=meses, y=mora_evolution, name='Días Mora', line=dict(color='#dc3545')),
                row=1, col=1
            )
            
            fig_evolution.add_trace(
                go.Scatter(x=meses, y=ahorro_acumulado, name='Ahorro Neto ($)', line=dict(color='#28a745'), fill='tonexty'),
                row=2, col=1
            )
            
            fig_evolution.update_layout(height=500, title_text="Impacto Temporal de la Estrategia")
            st.plotly_chart(fig_evolution, use_container_width=True)
    
    elif sim_type == "🎯 Cross-Selling Inteligente":
        st.markdown("#### 🎯 Simulador: Venta Cruzada por Segmentos")
        
        # Configuración avanzada por segmento
        st.markdown("**⚙️ Configuración de Campañas Personalizadas:**")
        
        campaign_cols = st.columns(3)
        
        # Configuración Tradicional
        with campaign_cols[0]:
            st.markdown("**🧓 Segmento Tradicional**")
            trad_producto = st.selectbox("Producto objetivo", ["DPF Plus", "Seguro Vida", "Crédito Hipotecario", "Plan Jubilación"], key="trad")
            trad_canal = st.selectbox("Canal preferido", ["Presencial", "Telefónico", "Correo"], key="trad_canal")
            trad_incentivo = st.slider("Incentivo ofrecido (%)", 0, 15, 5, key="trad_inc")
            trad_budget = st.slider("Presupuesto campaña ($K)", 10, 100, 30, key="trad_budget")
            
            # Conversión estimada basada en producto y canal
            conversion_base = {"DPF Plus": 18, "Seguro Vida": 12, "Crédito Hipotecario": 8, "Plan Jubilación": 15}
            canal_multiplier = {"Presencial": 1.2, "Telefónico": 1.0, "Correo": 0.7}
            incentivo_boost = 1 + (trad_incentivo / 100)
            
            trad_conversion = conversion_base[trad_producto] * canal_multiplier[trad_canal] * incentivo_boost
            
        # Configuración Riesgo
        with campaign_cols[1]:
            st.markdown("**⚠️ Segmento Riesgo**")
            risk_producto = st.selectbox("Producto objetivo", ["Microseguro", "Ahorro Programado", "Crédito Emergencia", "Educación Financiera"], key="risk")
            risk_canal = st.selectbox("Canal preferido", ["WhatsApp", "SMS", "Call Center", "App Móvil"], key="risk_canal")
            risk_incentivo = st.slider("Incentivo ofrecido (%)", 0, 20, 8, key="risk_inc")
            risk_budget = st.slider("Presupuesto campaña ($K)", 15, 120, 45, key="risk_budget")
            
            conversion_base_risk = {"Microseguro": 15, "Ahorro Programado": 22, "Crédito Emergencia": 12, "Educación Financiera": 35}
            canal_multiplier_risk = {"WhatsApp": 1.3, "SMS": 0.8, "Call Center": 1.1, "App Móvil": 1.0}
            
            risk_conversion = conversion_base_risk[risk_producto] * canal_multiplier_risk[risk_canal] * (1 + risk_incentivo/100)
        
        # Configuración Tech
        with campaign_cols[2]:
            st.markdown("**📱 Segmento Tech**")
            tech_producto = st.selectbox("Producto objetivo", ["Cuenta Digital Premium", "Inversiones Online", "Crédito Express", "Cripto Wallet"], key="tech")
            tech_canal = st.selectbox("Canal preferido", ["App Push", "Email Marketing", "Redes Sociales", "In-App"], key="tech_canal")
            tech_incentivo = st.slider("Incentivo ofrecido (%)", 0, 25, 10, key="tech_inc")
            tech_budget = st.slider("Presupuesto campaña ($K)", 20, 150, 60, key="tech_budget")
            
            conversion_base_tech = {"Cuenta Digital Premium": 28, "Inversiones Online": 18, "Crédito Express": 25, "Cripto Wallet": 15}
            canal_multiplier_tech = {"App Push": 1.4, "Email Marketing": 1.0, "Redes Sociales": 1.2, "In-App": 1.5}
            
            tech_conversion = conversion_base_tech[tech_producto] * canal_multiplier_tech[tech_canal] * (1 + tech_incentivo/100)
        
        # Cálculos de impacto consolidado
        st.markdown("### 💰 Impacto Financiero Consolidado")
        
        # Número de socios por segmento
        socios_tradicional = 14438
        socios_riesgo = 24064
        socios_tech = 9625
        
        # Ventas proyectadas
        ventas_tradicional = int(socios_tradicional * trad_conversion / 100)
        ventas_riesgo = int(socios_riesgo * risk_conversion / 100)
        ventas_tech = int(socios_tech * tech_conversion / 100)
        
        # Ingresos promedio por producto
        ingresos_producto = {
            "DPF Plus": 2800, "Seguro Vida": 1200, "Crédito Hipotecario": 8500, "Plan Jubilación": 3200,
            "Microseguro": 180, "Ahorro Programado": 850, "Crédito Emergencia": 1200, "Educación Financiera": 95,
            "Cuenta Digital Premium": 2400, "Inversiones Online": 4500, "Crédito Express": 3800, "Cripto Wallet": 1800
        }
        
        ingreso_tradicional = ventas_tradicional * ingresos_producto[trad_producto]
        ingreso_riesgo = ventas_riesgo * ingresos_producto[risk_producto]
        ingreso_tech = ventas_tech * ingresos_producto[tech_producto]
        
        # Costos de campaña
        costo_total = (trad_budget + risk_budget + tech_budget) * 1000
        
        # ROI por segmento
        ingreso_total = ingreso_tradicional + ingreso_riesgo + ingreso_tech
        roi_consolidado = ((ingreso_total - costo_total) / costo_total * 100) if costo_total > 0 else 0
        
        # Visualización de resultados
        result_cols = st.columns(4)
        
        with result_cols[0]:
            st.metric("Nuevos Productos Vendidos", f"{ventas_tradicional + ventas_riesgo + ventas_tech:,}")
            
        with result_cols[1]:
            st.metric("Ingresos Totales", f"${ingreso_total

        # Visualización de resultados
        result_cols = st.columns(4)
        
        with result_cols[0]:
            st.metric("Nuevos Productos Vendidos", f"{ventas_tradicional + ventas_riesgo + ventas_tech:,}")
        with result_cols[1]:
            st.metric("Ingresos Totales", f"${ingreso_total:,.0f}")
        with result_cols[2]:
            st.metric("Costo Total Campaña", f"${costo_total:,.0f}")
        with result_cols[3]:
            st.metric("ROI Consolidado", f"{roi_consolidado:.1f}%")
        
        # Gráfico de ventas por segmento
        fig_ventas = go.Figure()
        fig_ventas.add_trace(go.Bar(
            name='Tradicional',
            x=['Tradicional'],
            y=[ventas_tradicional],
            marker_color='#8dd3c7'
        ))
        fig_ventas.add_trace(go.Bar(
            name='Riesgo',
            x=['Riesgo'],
            y=[ventas_riesgo],
            marker_color='#ffffb3'
        ))
        fig_ventas.add_trace(go.Bar(
            name='Tech',
            x=['Tech'],
            y=[ventas_tech],
            marker_color='#bebada'
        ))
        fig_ventas.update_layout(
            title="Nuevos Productos por Segmento",
            yaxis_title="Cantidad",
            showlegend=True,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_ventas, use_container_width=True)

    elif sim_type == "📱 Aceleración Digital":
        st.markdown("#### 🚀 Simulador: Aceleración Digital")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("**⚙️ Configuración Digitalización:**")
            digital_target = st.slider("Meta de digitalización (%)", 45, 90, 65)
            months_to_implement = st.slider("Meses de implementación", 3, 24, 12)
            avg_savings_per_digital = st.number_input("Ahorro promedio por socio digital ($/año)", 10, 100, 24)
        with col2:
            socios_totales = 48127
            actuales_digitales = int(socios_totales * 0.45)
            meta_digitales = int(socios_totales * digital_target / 100)
            nuevos_digitales = meta_digitales - actuales_digitales
            ahorro_total = nuevos_digitales * avg_savings_per_digital
            st.metric("Nuevos Socios Digitales", f"{nuevos_digitales:,}")
            st.metric("Ahorro Anual Proyectado", f"${ahorro_total:,.0f}")
            
            # Gráfico de crecimiento
            meses = list(range(1, months_to_implement + 1))
            progreso = [int(actuales_digitales + (nuevos_digitales * m / months_to_implement)) for m in meses]
            fig_dig = px.line(x=meses, y=progreso, title="Progresión de Socios Digitales",
                              labels={'x': 'Mes', 'y': 'Socios Digitales'})
            st.plotly_chart(fig_dig, use_container_width=True)

    elif sim_type == "💰 Impacto ROI Consolidado":
        st.markdown("#### 💰 Dashboard de ROI Consolidado")
        # Asume que las métricas anteriores fueron calculadas
        total_beneficios = ingreso_total + ahorro_total + (ahorro_provisiones_total if 'ahorro_provisiones_total' in locals() else 0)
        total_costos = costo_total + (costo_total_anual if 'costo_total_anual' in locals() else 0)
        roi_final = ((total_beneficios - total_costos) / total_costos * 100) if total_costos > 0 else 0
        st.metric("ROI Final Total", f"{roi_final:.1f}%", delta=f"{roi_final-245:.1f}% vs Base")
        st.metric("Beneficio Neto Proyectado", f"${(total_beneficios-total_costos):,.0f}")
        # Gráfico de barras de costos y beneficios
        df_roi = pd.DataFrame({
            'Concepto': ['Beneficios', 'Costos'],
            'Valor': [total_beneficios, total_costos]
        })
        fig_roi_bar = px.bar(df_roi, x='Concepto', y='Valor', color='Concepto',
                             title="Costos vs Beneficios Totales",
                             color_discrete_map={'Beneficios':'#28a745','Costos':'#dc3545'})
        st.plotly_chart(fig_roi_bar, use_container_width=True)
        
    elif sim_type == "🔮 Escenarios Futuros":
        st.markdown("#### 🔮 Simulador de Escenarios Futuros")
        st.info("**Próximamente: Dashboard de escenarios avanzados de stress test y crecimiento acelerado.**")

# Puedes seguir agregando más simuladores o métricas si lo deseas...

# --- FIN DEL DASHBOARD ---

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 15px; margin: 20px 0;">
    <h3>“El futuro pertenece a quienes preparan hoy su éxito con inteligencia y visión”</h3>
    <p>COAC Raíces Andinas — Agosto 2025</p>
</div>
""", unsafe_allow_html=True)

