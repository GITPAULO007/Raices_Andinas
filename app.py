import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.graph_objects as go
import numpy as np
from datetime import datetime
import time

# Configuración de página con favicon y layout optimizado
st.set_page_config(
    page_title="Pitch Empresarial - Raíces Andinas", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para mejorar el diseño
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        margin: 10px;
    }

    .opportunity-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin: 10px 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .segment-card {
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        margin: 10px;
        transition: transform 0.3s ease;
    }
    
    .segment-card:hover {
        transform: translateY(-5px);
    }
    
    .timeline-item {
        background: #f8f9fa;
        border-left: 4px solid #4ECDC4;
        padding: 15px;
        margin: 10px 0;
        border-radius: 8px;
    }
    
    .cta-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 30px;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin: 20px 0;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR MEJORADO ----------
with st.sidebar:
    # Logo principal con mejor presentación
    try:
        logo = Image.open("logo_raices.jpg")
        st.image(logo, use_container_width=True)
    except:
        st.markdown("### 🏦 COAC Raíces Andinas")
    
    # Menú principal mejorado
    selected = option_menu(
        menu_title="📊 Panel de Control",
        options=[
            "🚀 Hook y Oportunidad",
            "🏦 Quiénes Somos",                        
            "🔬 Metodología",
            "🎯 Perfilamientos",            
            "🏁 Plan de Acción"
        ],
        icons=[
            "rocket-takeoff", "bank2", "gear", "bullseye", "calculator", "flag-fill"
        ],
        menu_icon="grid-3x3-gap-fill",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "#4ECDC4", "font-size": "18px"}, 
            "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px"},
            "nav-link-selected": {"background-color": "#667eea"},
        }
    )

    st.markdown("---")

    }
    )

    # POPUP INFORMATIVO DEL PROYECTO
    st.markdown("<br>", unsafe_allow_html=True)
    if st.sidebar.button("ℹ️ Información del Proyecto", use_container_width=True):
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 15px; color: white; margin: 1.5rem 0; box-shadow: 0 8px 16px rgba(102, 126, 234, 0.3);">
            <h2 style="color: white; text-align: center; margin-bottom: 1.5rem; font-size: 1.8rem;">📊 TIPOLOGÍA DE SOCIOS</h2>
            <h3 style="color: #FFD700; text-align: center; font-size: 1.4rem; margin-bottom: 1.5rem;">
                Cooperativa de Ahorro y Crédito<br><strong>RAÍCES ANDINAS</strong>
            </h3>
            <div style="background: rgba(255,255,255,0.15); padding: 1.5rem; border-radius: 12px;">
                <h4 style="color: white; margin-bottom: 1rem; font-size: 1.3rem; text-align: center;">👥 EQUIPO DE INVESTIGACIÓN</h4>
                <ul style="color: white; font-size: 1.1rem; margin: 0; padding-left: 0; list-style: none; line-height: 2;">
                    <li>🔹 <strong>Ariana Abad</strong></li>
                    <li>🔹 <strong>David Alvarado</strong></li>
                    <li>🔹 <strong>Grace Arce</strong></li>
                    <li>🔹 <strong>Paúl Guichay</strong></li>
                    <li>🔹 <strong>Alejandra Zambrano</strong></li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Métricas en tiempo real en sidebar
    st.markdown("### 📈 Dashboard en Vivo")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Socios activos migrantes", "24,014", "Fuente: Informe 2025")
    with col2:
        st.metric("Socios Totales", "819mil", "Fuente: Raíces Andinas")
    st.markdown("---")
    
        # Logos institucionales mejorados
    try:
        alprode_logo = Image.open("alprode.jpeg")
        st.image(alprode_logo, width=250, caption="Alprode")
        cofin_logo = Image.open("cofin_logo.png")
        st.image(cofin_logo, width=250, caption="Erasmus+")
        ucuenca_logo = Image.open("logo_ucuenca.png")
        st.image(ucuenca_logo, width=250, caption="Universidad de Cuenca")
    except:
        st.markdown("**Aliados Estratégicos:**\n- Alprode\n- Universidad de Cuenca")




# ---------- DATOS MEJORADOS PARA VISUALIZACIÓN ----------
# Datos más realistas y completos
np.random.seed(42)
df_socios = pd.DataFrame({
    "cluster": np.repeat([0, 1, 2], 100),
    "edad": np.concatenate([
        np.random.normal(45, 8, 100),
        np.random.normal(38, 12, 100),
        np.random.normal(40, 6, 100)
    ]),
    "ingresos": np.concatenate([
        np.random.normal(3559, 800, 100),
        np.random.normal(3759, 1200, 100),
        np.random.normal(3962, 600, 100)
    ]),
    "saldo_dpf": np.concatenate([
        np.random.normal(27597, 5000, 100),
        np.random.normal(316, 200, 100),
        np.random.normal(7656, 2000, 100)
    ]),
    "mora_dias": np.concatenate([
        np.random.exponential(1.5, 100),
        np.random.exponential(18, 100),
        np.random.exponential(10.2, 100)
    ])
})

# KPIs mejorados para radar chart
categorias = ["Edad Promedio", "Ingresos ($)", "Saldo DPF ($)", "Capital Prestado ($)", "Días Mora"]
cluster_tradicional = [45.1, 3558.96, 27597.17, 21576.06, 1.5]
cluster_riesgo = [38.4, 3759.42, 315.78, 21282.22, 18]
cluster_tech = [39.6, 3962.25, 7656.16, 27802.60, 10.2]

# Datos de proyección de remesas
años_proyeccion = list(range(2020, 2030))
remesas_historicas = [3500, 4200, 4800, 5100, 5491, 5821, 6200, 6600, 7100, 7650]

# ---------- SECCIONES DEL PITCH MEJORADAS ----------

if "🚀 Hook y Oportunidad" in selected:
    # Título principal con impacto
    st.markdown('''
    <div style="text-align: center; padding: 2rem 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; margin-bottom: 2rem;">
        <h1 style="color: white; font-size: 3.5rem; font-weight: 900; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            🌳 EL COOPERATIVISMO TIENE UN NUEVO RETO Y UN VIEJO ALIADO: SUS SOCIOS MIGRANTES.
        </h1>
        <p style="color: #f0f0f0; font-size: 1.4rem; margin-top: 1rem; font-weight: 300;">
            Mientras otros sectores luchan, los migrantes mueven <strong>$5.8 MIL MILLONES</strong> anuales
        </p>
    </div>
    ''', unsafe_allow_html=True)

    # Hook emocional y datos impactantes
    st.markdown('''
    <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%); padding: 2rem; border-radius: 15px; margin-bottom: 2rem; border-left: 6px solid #ff6b6b;">
        <h2 style="color: #2c3e50; font-size: 2.5rem; margin-bottom: 1rem; text-align: center;">
            💰 LA REALIDAD QUE CAMBIA TODO
        </h2>
        <div style="font-size: 1.4rem; color: #2c3e50; line-height: 1.8; text-align: center;">
            <strong>Cada 24 horas, los ecuatorianos en EE.UU. envían más de <span style="color:#e74c3c;">US$18 millones</span> a casa.</strong><br>
            <span style="font-size: 1.2rem; color: #e74c3c;">Eso es más que el PIB diario de varias provincias ecuatorianas.</span><br><br>
            <em style="font-size: 1.3rem; color: #8e44ad;">"No son solo números... son cientos de miles de ecuatorianos construyendo el futuro desde la distancia"</em>
        </div>
        <div style="text-align: right; margin-top: 0.8rem;">
            <small style="color: #bdbdbd;">Fuente: Banco Central del Ecuador (Q1 2025)</small>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Métricas impactantes con animación visual
    st.markdown("### 🔥 LOS NÚMEROS QUE ROMPEN ESQUEMAS")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(45deg, #FF6B6B, #FF8E53); padding: 1.5rem; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(255,107,107,0.3); transition: transform 0.3s;">
            <h2 style="color: white; font-size: 2.5rem; margin: 0; font-weight: 900;">$5.491M</h2>
            <p style="color: white; font-size: 1.1rem; margin: 0.5rem 0; font-weight: 600;">Remesas 2024</p>
            <small style="color: #ffe0e0; font-size: 0.9rem;">
                <strong>Más</strong> que la Inversión<br>Extranjera Directa
            </small>
            <div style="margin-top: 0.5rem;">
                <small style="color: #ffc4c4; font-size: 0.7rem;">Fuente: BCE</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(45deg, #4ECDC4, #44A08D); padding: 1.5rem; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(78,205,196,0.3);">
            <h2 style="color: white; font-size: 2.5rem; margin: 0; font-weight: 900;">75.6%</h2>
            <p style="color: white; font-size: 1.1rem; margin: 0.5rem 0; font-weight: 600;">Desde EE.UU.</p>
            <small style="color: #e0f7f5; font-size: 0.9rem;">
                <strong>US$1.3B</strong> en Q1 2025<br>principal fuente
            </small>
            <div style="margin-top: 0.5rem;">
                <small style="color: #b8f2ed; font-size: 0.7rem;">Fuente: BCE</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(45deg, #A770EF, #CF57A3); padding: 1.5rem; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(167,112,239,0.3);">
            <h2 style="color: white; font-size: 2.5rem; margin: 0; font-weight: 900;">$208M</h2>
            <p style="color: white; font-size: 1.1rem; margin: 0.5rem 0; font-weight: 600;">Solo a Azuay</p>
            <small style="color: #f0e5ff; font-size: 0.9rem;">
                En <strong>3 meses</strong> – epicentro migrante
            </small>
            <div style="margin-top: 0.5rem;">
                <small style="color: #e4d1ff; font-size: 0.7rem;">Fuente: BCE Q1 2025</small>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="background: linear-gradient(45deg, #FFA726, #FB8C00); padding: 1.5rem; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(255,167,38,0.3);">
            <h2 style="color: white; font-size: 2.5rem; margin: 0; font-weight: 900;">21%</h2>
            <p style="color: white; font-size: 1.1rem; margin: 0.5rem 0; font-weight: 600;">Inversión Inmobiliaria</p>
            <small style="color: #fff3e0; font-size: 0.9rem;">
                <strong>1 de cada 5</strong> familias invierte en vivienda
            </small>
            <div style="margin-top: 0.5rem;">
                <small style="color: #ffe0b3; font-size: 0.7rem;">Fuente: Estudio Microeconómico</small>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Comparativa impactante
    st.markdown('''
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 15px; margin: 2rem 0;">
        <h3 style="color: white; text-align: center; font-size: 2rem; margin-bottom: 1.5rem;">
            🥊 REMESAS vs. EXPORTACIONES TRADICIONALES
        </h3>
        <div style="display: flex; justify-content: space-around; text-align: center;">
            <div>
                <h4 style="color: #4CAF50; font-size: 1.8rem; margin: 0;">$5.491M</h4>
                <p style="color: white; margin: 0; font-size: 1.2rem;">💸 REMESAS</p>
            </div>
            <div style="color: white; font-size: 2rem; align-self: center;">VS</div>
            <div>
                <h4 style="color: #FF9800; font-size: 1.5rem; margin: 0;">$5.191M</h4>
                <p style="color: white; margin: 0; font-size: 1.2rem;">🦐 Camarón</p>
            </div>
            <div style="color: white; font-size: 2rem; align-self: center;">VS</div>
            <div>
                <h4 style="color: #FFC107; font-size: 1.5rem; margin: 0;">$3.600M</h4>
                <p style="color: white; margin: 0; font-size: 1.2rem;">🍌 Banano</p>
            </div>
        </div>
        <p style="color: #e8eaf6; text-align: center; margin-top: 1rem; font-style: italic; font-size: 1.2rem;">
            Los migrantes son el motor económico #1 del país
        </p>
        <div style="text-align: right; margin-top: 0.3rem;">
            <small style="color: #bdbdbd;">Fuente: Banco Central del Ecuador</small>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Proyección con gráfico mejorado
    st.markdown("### 📈 LA TRAYECTORIA IMPARABLE")
    
    # Datos para el gráfico
    años = [2020, 2021, 2022, 2023, 2024, 2025]
    remesas_data = [3165, 4816, 5268, 5421, 5491, 5821]
    
    fig = px.area(
        x=años, 
        y=remesas_data,
        title="Crecimiento Explosivo de Remesas Ecuador (Millones USD)",
        labels={'x': 'Año', 'y': 'Remesas (Millones USD)'}
    )
    fig.update_traces(
        fill='tonexty',
        fillcolor='rgba(255, 107, 107, 0.3)',
        line=dict(color='#FF6B6B', width=4)
    )
    fig.update_layout(
        height=400,
        title_font_size=16,
        title_x=0.5,
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    fig.add_vline(
        x=2024, 
        line_dash="dash", 
        line_color="#e74c3c", 
        line_width=3,
        annotation_text="📍 Estamos aquí",
        annotation_position="top"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Insights estratégicos
    col_insight1, col_insight2 = st.columns(2)

    with col_insight1:
        st.markdown('''
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 15px; min-height: 280px;">
            <h4 style="color: white; margin-bottom: 1.5rem; font-size: 1.5rem;">💡 INSIGHT DEMOGRÁFICO</h4>
            <p style="color: #e8eaf6; font-size: 1.2rem; line-height: 1.7;">
                Los socios migrantes de RAÍCES ANDINAS (39 años promedio) están en su <strong>pico de productividad financiera</strong>,
                superando la edad promedio del migrante ecuatoriano (33 años). Esto significa mayor capacidad de ahorro y planificación a largo plazo.
            </p>
            <div style="text-align: right; margin-top: 1rem;">
                <small style="color: #c8d0ff; font-size: 0.8rem;">Fuente: Pew Research Center</small>
            </div>
        </div>
        ''', unsafe_allow_html=True)

    with col_insight2:
        st.markdown('''
        <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 2rem; border-radius: 15px; min-height: 280px;">
            <h4 style="color: #2c3e50; margin-bottom: 1.5rem; font-size: 1.5rem;">🎯 VENTAJA GEOGRÁFICA</h4>
            <p style="color: #2c3e50; font-size: 1.2rem; line-height: 1.7;">
                El 59% de los ecuatorianos en EE.UU., cerca de 550,000 personas, reside en NY y NJ. Esta concentración representa una oportunidad estratégica para que Raíces Andinas fomente alianzas financieras y capture remesas directamente desde el origen.
            </p>
            <div style="text-align: right; margin-top: 1rem;">
                <small style="color: #999; font-size: 0.8rem;">Fuente: Migration Policy Institute</small>
            </div>
        </div>
        ''', unsafe_allow_html=True)

    # ¿POR QUÉ ESTE PROYECTO? - RECUADRO GRANDE COMPLETO
    st.markdown('''
    <div style="background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%); padding: 2rem; border-radius: 15px; text-align: center; margin: 2rem 0;">
        <h3 style="color: #2c3e50; font-size: 2rem; margin-bottom: 1rem;">
            📌 ¿POR QUÉ ESTE PROYECTO?
        </h3>
        <p style="color: #2c3e50; font-size: 2rem; margin-bottom: 1.5rem; line-height: 1.7;">
            Miles de migrantes desde EE.UU. sostienen nuestras economías locales con sus remesas. Entender quiénes son y cómo interactúan con la cooperativa no solo es necesario, es una oportunidad estratégica.
        </p>
        <p style="color: #2c3e50; font-size: 2rem; margin-bottom: 1.5rem; line-height: 1.7;">
            Este proyecto identifica tipologías de socios migrantes, reconociendo patrones clave en su comportamiento transaccional.
        </p>
        <div style="background: rgba(0, 128, 128, 0.2); padding: 1rem; border-radius: 10px; border-left: 4px solid #008080;">
            <p style="color: #008080; font-size: 2.2rem; margin: 0; font-weight: bold;">
                ¿Qué características presentan estos socios que debemos considerar para responder mejor a sus necesidades?
            </p>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Call to action final
    st.markdown('''
    <div style="background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); padding: 2rem; border-radius: 15px; text-align: center; margin-top: 2rem;">
        <h3 style="color: white; font-size: 2rem; margin-bottom: 1rem;">
            🚀 EL MOMENTO ES AHORA
        </h3>
        <p style="color: #bdc3c7; font-size: 1.3rem; margin-bottom: 1.5rem;">
            RAÍCES ANDINAS puede posicionarse como <strong style="color: #3498db;">EL PUENTE FINANCIERO</strong> entre los sueños migrantes y la realidad familiar.
        </p>
        <div style="background: rgba(52, 152, 219, 0.2); padding: 1rem; border-radius: 10px; border-left: 4px solid #3498db;">
            <p style="color: #ecf0f1; font-size: 1.2rem; margin: 0; font-style: italic;">
                "No estamos hablando de capturar remesas... estamos hablando de construir el futuro financiero de las familias ecuatorianas"
            </p>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Próximo paso
    st.success("🎯 **PRÓXIMO PASO:** Implementar segmentación inteligente de socios migrantes para capturar esta oportunidad de $5.800M proyectados para 2025.")

    # Métricas adicionales en sidebar o expandible
    with st.expander("📊 Datos Adicionales de Soporte"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Inclusión Financiera Ecuador", "74%", "26% sin bancarizar")
            st.metric("Pagos Digitales", "51%", "49% usa efectivo")
        with col2:
            st.metric("Concentración NY + NJ", "59%", "~550,000 ecuatorianos")
            st.metric("Crecimiento Q1 2025", "9.5%", "vs Q1 2024")
        with col3:
            st.metric("Destino Vivienda", "21%", "$1.154B anuales")
            st.metric("Sin Crédito Formal", "75%", "Mercado potencial enorme")

elif "🏦 Quiénes Somos" in selected:
    st.markdown('<h1 class="main-header">🏦 COAC Raíces Andinas</h1>', unsafe_allow_html=True)
    st.markdown("### *29 años construyendo sueños, conectando corazones*")

    # Video institucional
    st.markdown("### 🎬 Video Institucional")
    try:
        video_file = open('video_intro_raices.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    except:
        st.info("📹 Video institucional: video_intro_raices.mp4 (cargar archivo en el repositorio)")
    
    st.markdown("---")
    
    # Datos clave en columnas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Años de Historia", "29", "Desde 1996")
        st.metric("Provincias", "8", "Cobertura nacional")
    with col2:
        st.metric("Socios Activos Migrantes", "24,014", "+2.3% anual")
        st.metric("Patrimonio", "$225M", "Sólido respaldo")
    with col3:
        st.metric("Oficinas", "70", "Cerca de ti")
        st.metric("Activos", "1,958M", "Solvencia")

    # Añadir después de las métricas existentes y antes del análisis FODA
    st.markdown("### 📊 Indicadores Financieros")
    ind_col1, ind_col2, ind_col3, ind_col4 = st.columns(4)

    with ind_col1:
        st.metric("Índice de Morosidad", "6.17%", "Gestión eficiente")
    with ind_col2:
        st.metric("Cobertura Cartera Riesgo", "200.04%", "Sólida cobertura")  
    with ind_col3:
        st.metric("Solvencia", "22.54%", "Base patrimonial sólida")
    with ind_col4:
        st.metric("Calificación de Riesgo", "AA+", "Perspectiva estable")

    st.markdown("<br>", unsafe_allow_html=True)

    # Análisis FODA visual mejorado
    st.markdown("### 🔍 Análisis Estratégico FODA")
    foda_col1, foda_col2 = st.columns(2)
    
    with foda_col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%); padding: 20px; border-radius: 15px; margin: 10px 0;'>
            <h4 style="font-size: 2rem;">💪 FORTALEZAS</h4>
            <ul style="font-size: 1.4rem; line-height: 1.6;">
                <li>Foco territorial en zonas de migración.</li>
                <li>Modelo cooperativo participativo.</li>
                <li>Solidez financiera (buen rating, baja mora).</li>
                <li>Infraestructura y tecnología en mejora.</li>
            </ul>
        </div>
        
        <div style='background: linear-gradient(135deg, #cce5ff 0%, #b3d9ff 100%); padding: 20px; border-radius: 15px; margin: 10px 0;'>
            <h4 style="font-size: 2rem;">🌟 OPORTUNIDADES</h4>
            <ul style="font-size: 1.4rem; line-height: 1.6;">
                <li>Alto volumen de remesas hacia Ecuador.</li>
                <li>Interés de migrantes por invertir en el país.</li>
                <li>Avance tecnológico para crear nuevos productos.</li>
                <li>Demanda de educación financiera para migrantes.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with foda_col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%); padding: 20px; border-radius: 15px; margin: 10px 0;'>
            <h4 style="font-size: 2rem;">⚠️ DEBILIDADES</h4>
            <ul style="font-size: 1.4rem; line-height: 1.6;">
                <li>Segmentación y marketing deficientes.</li>
                <li>Personal no capacitado para la atención a migrantes.</li>
                <li>Sin presencia física en el extranjero.</li>
                <li>Lenta adaptación tecnológica y bajo uso de datos.</li>
            </ul>
        </div>
        
        <div style='background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%); padding: 20px; border-radius: 15px; margin: 10px 0;'>
            <h4 style="font-size: 2rem;">🚨 AMENAZAS</h4>
            <ul style="font-size: 1.4rem; line-height: 1.6;">
                <li>Políticas migratorias más restrictivas.</li>
                <li>Cambios en la regulación financiera (SEPS).</li>
                <li>Fuerte competencia de las Fintech.</li>
                <li>Inestabilidad económica (inflación, tipo de cambio).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
elif "🔬 Metodología" in selected:
    st.markdown('<h1 class="main-header">🔬 Metodología de Investigación</h1>', unsafe_allow_html=True)
    
    # Explicación del enfoque metodológico
    st.markdown("### 📊 Enfoque Cuantitativo: De Datos a Insights Estratégicos")
    
    metodologia_tabs = st.tabs(["🎯 Enfoque", "📋 Datos", "⚙️ Procesamiento", "🔍 Modelo", "📊 Validación"])
    
    with metodologia_tabs[0]:
        st.markdown("""
        #### 🎯 Enfoque Metodológico
        
        **Enfoque Cuantitativo Multidimensional:**
        
        🔍 **Exploratorio:** Análisis de clústeres para identificar grupos homogéneos no definidos previamente
        
        📈 **Descriptivo:** Caracterización del comportamiento financiero de cada perfil identificado
        
        🎯 **Aplicado:** Generación de recomendaciones estratégicas basadas en hallazgos analíticos
        """)
        
        # Visualización del proceso metodológico
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            **📊 Análisis Exploratorio**
            - Identificación de patrones
            - Segmentación no supervisada           
            """)
        with col2:
            st.markdown("""
            **🔬 Análisis Descriptivo**  
            - Caracterización de perfiles
            - Análisis de variables clave
            - Comportamiento financiero
            """)
        with col3:
            st.markdown("""
            **🎯 Análisis Aplicado**
            - Estrategias diferenciadas
            - Recomendaciones prácticas
            - Optimización de servicios
            """)
    
    with metodologia_tabs[1]:
        st.markdown("""
        #### 📋 Fuentes de Información y Datos
        
        **Base de Datos Consolidada:**
        - 📞 **Datos de Llamadas:** Interacciones y comunicaciones
        - 💳 **Transacciones:** Historial de operaciones financieras  
        - 💰 **Créditos:** Información crediticia y riesgo
        - 🏦 **Captaciones:** Productos de ahorro y depósitos
        
        **Período de Análisis:** Enero 2020 - Marzo 2025
        
        **Población Objetivo:** Socios migrantes residentes en Estados Unidos
        """)
        
        # Métricas de la base de datos
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Población Total", "29,091", "socios migrantes")
        with col2:
            st.metric("Muestra Final", "24,014", "socios activos")
        with col3:
            st.metric("Variables Analizadas", "41", "indicadores clave")
        
        st.info("✅ **Criterios de Selección:** Socios activos con actividad en últimos 180 días y saldo superior al 25% del SBU")
    
    with metodologia_tabs[2]:
        st.markdown("""
        #### ⚙️ Procesamiento y Preparación de Datos
        
        **Proceso de Limpieza y Consolidación:**
        
        1. **🧹 Depuración:** Eliminación de duplicados y normalización de formatos
        2. **🔗 Integración:** Consolidación de 4 bases independientes en una única base
        3. **📊 Agregación:** Panel de datos no balanceado con métodos específicos por tipo de variable
        """)
        
        # Métodos de agregación
        st.markdown("##### 📈 Métodos de Agregación por Tipo de Variable")
        
        agregacion_data = pd.DataFrame({
            'Tipo de Variable': ['Continuas', 'Contadores', 'Categóricas', 'Métricas Especiales'],
            'Método': ['Suma/Media', 'Suma/Máximo', 'Moda', 'Valor de Cierre'],
            'Propósito': ['Volumen total o nivel medio', 'Acumulado o pico de actividad', 'Categoría más frecuente', 'Estado final del período'],
            'Ejemplos': ['Ingresos, Saldos', 'Número de créditos', 'Estado civil, Género', 'Calificación de riesgo']
        })
        
        st.dataframe(agregacion_data, use_container_width=True)
    
    with metodologia_tabs[3]:
        st.markdown("""
        #### 🔍 Modelo de Segmentación: Metodología Dual
        
        **Proceso de Dos Etapas:**
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🎯 Etapa 1: Análisis de Componentes Principales (PCA)**
            - Reducción de dimensionalidad
            - Eliminación de multicolinealidad  
            - Preparación para clustering
            - Identificación de patrones latentes
            """)
        with col2:
            st.markdown("""
            **⚙️ Etapa 2: Algoritmo K-Means**
            - Segmentación no supervisada
            - Identificación de grupos homogéneos
            - Optimización de centroides
            - Asignación de perfiles
            """)
        
        st.markdown("""
        ##### 🧮 Variables Clave del Modelo
        
        **Dimensiones Analizadas:**
        - 👤 **Demográficas:** Edad, género, estado civil, cargas familiares
        - 💰 **Económicas:** Ingresos estimados, capital prestado, saldos
        - 🏦 **Financieras:** Productos contratados, tasas de interés, morosidad
        - 📱 **Comportamentales:** Uso de servicios digitales, frecuencia transaccional
        - ⚖️ **Riesgo:** Días de mora, calificación crediticia, historial de pagos
        """)
    
    with metodologia_tabs[4]:
        st.markdown("""
        #### 📊 Determinación del Número Óptimo de Clústeres
        
        **Criterios de Validación Aplicados:**
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **📈 Método del Codo**
            - Análisis de inercia (SSE)
            - Identificación del punto de inflexión
            - Equilibrio complejidad-interpretabilidad
            """)
        with col2:
            st.markdown("""
            **🎯 Coeficiente de Silueta**
            - Evaluación de cohesión interna
            - Medición de separación entre grupos
            - Validación de calidad del clustering
            """)
        
        # Simulación de métricas de validación
        st.markdown("##### 🏆 Resultados de Validación")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("K Óptimo", "3", "clústeres seleccionados")
        with col2:
            st.metric("Coeficiente Silueta", "0.40", "separación aceptable")
        with col3:
            st.metric("Reducción Inercia", "65%", "hasta K=3")
        
        st.success("✅ **Decisión Final:** Se seleccionó K=3 como equilibrio entre robustez estadística y utilidad práctica para el análisis de perfiles.")
        
        st.markdown("""
        ##### 🛠️ Herramientas Tecnológicas Utilizadas
        
        **Stack Tecnológico:**
        - **🐍 Python:** Procesamiento y análisis de datos
        - **📊 Pandas/NumPy:** Manipulación de grandes volúmenes de datos  
        - **🔬 Scikit-Learn:** Implementación de PCA y K-Means
        - **⚡ Dask:** Manejo eficiente de big data
        - **📈 Power BI:** Visualización exploratoria inicial
        - **📓 Jupyter Notebook:** Entorno de desarrollo analítico
        """)

elif "🎯 Perfilamientos" in selected:
    st.markdown('<h1 class="main-header">🎯 Segmentación de Socios Migrantes</h1>', unsafe_allow_html=True)
    
    # Introducción con métricas clave
    st.markdown("### 📊 Análisis de Tipología de Socios Migrantes en Estados Unidos")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Población Total", "29,091", "socios migrantes")
    with col2:
        st.metric("Muestra Analizada", "24,014", "socios activos")
    with col3:
        st.metric("Variables Analizadas", "41", "indicadores clave")
    with col4:
        st.metric("Período", "2020-2025", "5 años de datos")
    
    st.markdown("---")
    
    # Tabs principales
    main_tabs = st.tabs(["🔍 Metodología", "👥 Perfiles Identificados", "📈 Análisis Temporal", "💡 Estrategias"])
    
    with main_tabs[0]:
        st.markdown("### 🔬 Metodología de Segmentación")
        
        method_col1, method_col2 = st.columns(2)
        
        with method_col1:
            st.info("""
            **📊 Proceso de Análisis en 2 Etapas:**
            
            1. **PCA (Análisis de Componentes Principales)**
               - Reducción de dimensionalidad
               - Eliminación de multicolinealidad
               - Identificación de patrones latentes
            
            2. **K-Means Clustering**
               - Segmentación no supervisada
               - Identificación de grupos homogéneos
               - K=3 clústeres óptimos
            """)
            
        with method_col2:
            # Visualización del proceso
            st.markdown("**🎯 Determinación del Número Óptimo de Clústeres**")
            
            # Simulación del método del codo
            k_values = list(range(2, 11))
            sse_values = [3.0, 2.8, 2.4, 2.35, 2.3, 2.25, 2.2, 2.15, 2.1]
            
            fig_elbow = go.Figure()
            fig_elbow.add_trace(go.Scatter(
                x=k_values, y=sse_values,
                mode='lines+markers',
                name='SSE',
                line=dict(color='#2196F3', width=3),
                marker=dict(size=10)
            ))
            
            # Marcar el punto óptimo
            fig_elbow.add_trace(go.Scatter(
                x=[3], y=[2.4],
                mode='markers',
                name='K Óptimo',
                marker=dict(size=15, color='#FF4444', symbol='star')
            ))
            
            fig_elbow.update_layout(
                title="Método del Codo",
                xaxis_title="Número de Clústeres (K)",
                yaxis_title="SSE (Inercia)",
                height=300,
                showlegend=True
            )
            
            st.plotly_chart(fig_elbow, use_container_width=True)
            
            # Métricas de validación
            val_col1, val_col2 = st.columns(2)
            with val_col1:
                st.metric("Coeficiente Silueta", "0.40", "Separación aceptable")
            with val_col2:
                st.metric("Reducción Inercia", "65%", "hasta K=3")
    
    with main_tabs[1]:
        st.markdown("### 👥 Tres Perfiles de Socios Identificados")
        
        # Selector de perfil
        selected_profile = st.selectbox(
            "Selecciona un perfil para ver detalles:",
            ["Vista General", "Clúster 0: Socios Tradicionales", "Clúster 1: Riesgo Financiero", "Clúster 2: Tecnológico Multiservicios"]
        )
        
        if selected_profile == "Vista General":
            # Comparación de perfiles
            profiles_data = {
                'Características': ['Edad Promedio', 'Ingresos Mensuales', 'Saldo DPF', 'Capital Prestado', 'Días de Mora', 'Calificación'],
                'Tradicionales (9%)': ['45.1 años', '$3,558.96', '$27,597.17', '$21,576.06', '1.5 días', 'A-2'],
                'Riesgo Financiero (90%)': ['38.4 años', '$3,759.42', '$315.78', '$21,282.22', '18.0 días', 'A-3'],
                'Tecnológico Multiservicios (1.2%)': ['39.6 años', '$3,962.25', '$7,656.16', '$27,802.60', '10.2 días', 'A-2']
            }
            
            df_profiles = pd.DataFrame(profiles_data)
            
            # Mostrar tabla estilizada
            st.dataframe(
            df_profiles.style.highlight_max(subset=['Tradicionales (9%)', 'Riesgo Financiero (90%)', 'Tecnológico Multiservicios (1.2%)']),
            use_container_width=True
            )
            
            # Gráfico de radar comparativo
            categories = ['Edad', 'Ingresos', 'Ahorro DPF', 'Capital', 'Riesgo (inverso)', 'Uso Digital']
            
            fig_radar = go.Figure()
            
            # Datos normalizados para el radar
            tradicionales = [0.9, 0.6, 1.0, 0.7, 0.95, 0.2]
            riesgo = [0.5, 0.65, 0.1, 0.65, 0.2, 0.1]
            tecnologico = [0.6, 0.8, 0.4, 1.0, 0.5, 1.0]
            
            fig_radar.add_trace(go.Scatterpolar(
                r=tradicionales,
                theta=categories,
                fill='toself',
                name='Tradicionales',
                line_color='#4CAF50'
            ))
            
            fig_radar.add_trace(go.Scatterpolar(
                r=riesgo,
                theta=categories,
                fill='toself',
                name='Riesgo Financiero',
                line_color='#FF6B6B'
            ))
            
            fig_radar.add_trace(go.Scatterpolar(
                r=tecnologico,
                theta=categories,
                fill='toself',
                name='Tecnológico Multiservicios',
                line_color='#2196F3'
            ))
            
            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 1]
                    )),
                showlegend=True,
                title="Perfil Comparativo de Clústeres"
            )
            
            st.plotly_chart(fig_radar, use_container_width=True)
            
        else:
            # Detalles específicos del perfil seleccionado
            if "Tradicionales" in selected_profile:
                st.success("**📊 Perfil: El Ancla Financiera**")
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.markdown("""
                    **Características principales:**
                    - 🎯 Mayor edad promedio (45.1 años)
                    - 💰 Mayores saldos en DPF ($27,597)
                    - ⚡ Menor riesgo (1.5 días de mora)
                    - 📱 Bajo uso de servicios digitales
                    - 🏦 Prefieren productos tradicionales
                    
                    **Comportamiento:**
                    - Conservadores y adversos al riesgo
                    - Valoran la seguridad sobre la transaccionalidad
                    - Alta fidelidad a la cooperativa
                    """)
                with col2:
                    st.metric("Tamaño del Segmento", "9%", "~2,161 socios")
                    st.metric("Valor Promedio", "$27,597", "en DPF")
                    st.metric("Riesgo", "Muy Bajo", "1.5 días mora")
                    
            elif "Riesgo Financiero" in selected_profile:
                st.error("**⚠️ Perfil: El Desafío Principal**")
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.markdown("""
                    **Características principales:**
                    - 📉 Mayor tasa de morosidad (18 días)
                    - 💸 Saldos de ahorro muy bajos ($316)
                    - 🚫 Uso muy limitado de servicios
                    - ⚡ Alta fragilidad financiera
                    - 🔄 97% de retención en el clúster
                    
                    **Comportamiento:**
                    - Baja vinculación con la cooperativa
                    - Dificultades para cumplir obligaciones
                    - Requieren intervención urgente
                    """)
                with col2:
                    st.metric("Tamaño del Segmento", "90%", "~21,613 socios")
                    st.metric("Saldo Promedio", "$316", "muy bajo")
                    st.metric("Riesgo", "Alto", "18 días mora")
                    
            elif "Tecnológico" in selected_profile:
                st.info("**🚀 Perfil: El Más Rentable**")
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.markdown("""
                    **Características principales:**
                    - 💳 Mayor capital prestado ($27,802)
                    - 📱 Uso intensivo de servicios digitales
                    - 🔄 Alta transaccionalidad
                    - 💡 Adoptan múltiples productos
                    - ⚠️ 48% migra a riesgo financiero
                    
                    **Comportamiento:**
                    - Altamente activos y comprometidos
                    - Aprovechan toda la gama de servicios
                    - Perfil inestable que requiere monitoreo
                    """)
                with col2:
                    st.metric("Tamaño del Segmento", "1.2%", "~288 socios")
                    st.metric("Capital Promedio", "$27,802", "el más alto")
                    st.metric("Riesgo", "Moderado", "10.2 días mora")
    
    with main_tabs[2]:
        st.markdown("### 📈 Análisis de Transición Temporal")
        
        # Matriz de transición
        st.markdown("#### 🔄 Matriz de Transición Anual entre Clústeres")
        
        transition_matrix = pd.DataFrame({
            'Desde/Hacia': ['Tradicionales', 'Riesgo Financiero', 'Tecnológico Multiservicios'],
            'Tradicionales': ['77%', '3%', '7%'],
            'Riesgo Financiero': ['22%', '97%', '48%'],
            'Tecnológico Multiservicios': ['1%', '1%', '45%']
        })
        
        # Crear heatmap interactivo
        matrix_values = [[0.77, 0.22, 0.01],
                        [0.03, 0.97, 0.01],
                        [0.07, 0.48, 0.45]]
        
        fig_heatmap = go.Figure(data=go.Heatmap(
            z=matrix_values,
            x=['Tradicionales', 'Riesgo Financiero', 'Tecnológico'],
            y=['Tradicionales', 'Riesgo Financiero', 'Tecnológico'],
            text=[[f'{v:.0%}' for v in row] for row in matrix_values],
            texttemplate='%{text}',
            colorscale='RdYlBu_r',
            showscale=True
        ))
        
        fig_heatmap.update_layout(
            title="Probabilidad de Transición entre Clústeres",
            xaxis_title="Clúster Destino (t+1)",
            yaxis_title="Clúster Origen (t)",
            height=400
        )
        
        st.plotly_chart(fig_heatmap, use_container_width=True)
        
        # Insights clave
        col1, col2, col3 = st.columns(3)
        with col1:
            st.warning("""
            **🔍 Hallazgo Clave 1:**
            El clúster de Riesgo Financiero actúa como un "agujero negro" con 97% de retención
            """)
        with col2:
            st.error("""
            **⚠️ Hallazgo Clave 2:**
            48% de los socios Tecnológicos migran a Riesgo Financiero al año siguiente
            """)
        with col3:
            st.success("""
            **✅ Hallazgo Clave 3:**
            Los Tradicionales son los más estables con 77% de permanencia
            """)
        
        # Evolución temporal
        st.markdown("#### 📊 Evolución de la Distribución de Clústeres")
        
        years = [2020, 2021, 2022, 2023, 2024, 2025]
        tradicionales_pct = [4.67, 4.67, 6.33, 7.76, 8.52, 6.40]
        riesgo_pct = [95.33, 94.15, 92.08, 90.37, 88.99, 93.31]
        tecnologico_pct = [0.00, 1.17, 1.59, 1.87, 2.49, 0.29]
        
        fig_evolution = go.Figure()
        
        fig_evolution.add_trace(go.Scatter(
            x=years, y=tradicionales_pct,
            mode='lines+markers',
            name='Tradicionales',
            line=dict(color='#4CAF50', width=3),
            stackgroup='one'
        ))
        
        fig_evolution.add_trace(go.Scatter(
            x=years, y=riesgo_pct,
            mode='lines+markers',
            name='Riesgo Financiero',
            line=dict(color='#FF6B6B', width=3),
            stackgroup='one'
        ))
        
        fig_evolution.add_trace(go.Scatter(
            x=years, y=tecnologico_pct,
            mode='lines+markers',
            name='Tecnológico Multiservicios',
            line=dict(color='#2196F3', width=3),
            stackgroup='one'
        ))
        
        fig_evolution.update_layout(
            title="Distribución Porcentual de Clústeres por Año",
            xaxis_title="Año",
            yaxis_title="Porcentaje de Socios (%)",
            hovermode='x unified',
            height=400
        )
        
        st.plotly_chart(fig_evolution, use_container_width=True)
    
    with main_tabs[3]:
        st.markdown("### 💡 Estrategias Recomendadas por Perfil")
        
        strategy_tabs = st.tabs(["Tradicionales", "Riesgo Financiero", "Tecnológico Multiservicios"])
        
        with strategy_tabs[0]:
            st.markdown("#### 🎯 Estrategias para Socios Tradicionales")
            
            col1, col2 = st.columns(2)
            with col1:
                st.info("""
                **📈 Estrategia 1: Programa de Incentivos a través de promociones en Ventas**
                
                **Objetivo:** Migración progresiva a servicios digitales
                
                **Herramientas:**
                - 🎁 Sorteos mensuales
                - 💰 Descuentos temporales
                - 🏆 Bonificaciones por uso múltiple
                
                **Duración:** Ciclos de 1 mes rotativos
                """)
                
            with col2:
                st.success("""
                **🔄 Estrategia 2: Venta Cruzada Digital**
                
                **Objetivo:** Aumentar adopción de canales digitales
                
                **Herramientas:**
                - 📱 Onboarding digital asistido
                - 🎯 Promociones exclusivas en app
                - 📊 Dashboards personalizados
                
                **Duración:** Implementación en 1 año
                """)
                
        with strategy_tabs[1]:
            st.markdown("#### ⚠️ Estrategias para Socios de Riesgo Financiero")
            
            st.error("""
            **🚨 Estrategia: Programa de Prevención de Mora**
            
            **Objetivo:** Reducir días de mora y mejorar calificación crediticia
            """)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("""
                **📞 Llamadas Preventivas**
                - 72-48 horas antes del vencimiento
                - Tono amable y recordatorio
                - Incentivos por pago anticipado
                """)
            with col2:
                st.markdown("""
                **💬 Mensajes Personalizados**
                - SMS/WhatsApp automatizados
                - Escalamiento gradual del tono
                - Opciones de refinanciamiento
                """)
            with col3:
                st.markdown("""
                **🎯 Sistema Poka-Yoke**
                - Alertas automáticas
                - Bloqueo preventivo
                - Educación financiera
                """)
                
        with strategy_tabs[2]:
            st.markdown("#### 🚀 Estrategias para Socios Tecnológico Multiservicios")
            
            st.info("""
            **👑 Estrategia: Programa VIP de Membresías Exclusivas**
            
            **Objetivo:** Fidelización y prevención de migración a riesgo
            """)
            
            # Simulación de beneficios VIP
            vip_benefits = pd.DataFrame({
                'Beneficio': ['Tasa Preferencial', 'Atención Prioritaria', 'Cashback', 'Límites Ampliados', 'Asesoría Financiera'],
                'Nivel Básico': ['0.5%', '✓', '1%', '10%', 'Mensual'],
                'Nivel Premium': ['1%', '✓', '2%', '25%', 'Quincenal'],
                'Nivel Elite': ['1.5%', '✓', '3%', '50%', 'Semanal']
            })
            
            st.dataframe(vip_benefits, use_container_width=True)
            
            # Métricas de impacto esperado
            st.markdown("#### 📊 Impacto Esperado de las Estrategias")
            
            impact_col1, impact_col2, impact_col3, impact_col4 = st.columns(4)
            with impact_col1:
                st.metric("Reducción Mora", "-25%", "en 6 meses")
            with impact_col2:
                st.metric("Adopción Digital", "+40%", "tradicionales")
            with impact_col3:
                st.metric("Retención VIP", "85%", "tecnológicos")
                
    # Footer con recomendaciones
    st.markdown("---")
    st.markdown("### 🎯 Recomendaciones Clave")
    
    rec_col1, rec_col2, rec_col3 = st.columns(3)
    with rec_col1:
        st.markdown("""
        **📊 Gestión de Datos**
        - Actualización periódica de información
        - Enriquecimiento de variables
        - Monitoreo en tiempo real
        """)
    with rec_col2:
        st.markdown("""
        **💰 Análisis Financiero**
        - Evaluar costo por clúster
        - Medir rentabilidad real
        - Optimizar recursos
        """)
    with rec_col3:
        st.markdown("""
        **🔄 Mejora Continua**
        - Validar estrategias trimestralmente
        - Ajustar según resultados
        - Escalar iniciativas exitosas
        """)

elif "🏁 Plan de Acción" in selected or selected == "🏁 Plan de Acción":
    st.markdown('<h1 class="main-header">📋 Conclusiones y Recomendaciones Estratégicas</h1>', unsafe_allow_html=True)
    
    # Métricas clave del estudio
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Socios Analizados", "24,014", "activos en EE.UU.")
    with col2:
        st.metric("Perfiles Identificados", "3", "segmentos únicos")
    with col3:
        st.metric("Variables Analizadas", "41", "indicadores clave")
    with col4:
        st.metric("Período Analizado", "5 años", "2020-2025")
    
    st.markdown("---")
    
    # Tabs principales
    tabs = st.tabs(["🎯 Conclusiones Clave", "💡 Recomendaciones Estratégicas", "📊 Hallazgos por Perfil"])
    
    with tabs[0]:
        st.markdown("## 🎯 Conclusiones del Análisis de Tipología")
        
        # Hallazgo 1
        with st.expander("🔍 Hallazgo 1: Identificación de Tres Perfiles Diferenciados", expanded=True):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.info("""
                **La aplicación del algoritmo K-Means validó la existencia de tres clústeres con perfiles de comportamiento claramente diferenciados:**
                
                ✅ **Validación estadística robusta** con coeficiente de silueta de 0.40
                ✅ **Segmentos bien definidos** con características únicas
                ✅ **Patrones de comportamiento consistentes** a lo largo del tiempo
                """)
            with col2:
                # Gráfico de distribución
                fig_dist = go.Figure(data=[go.Pie(
                    labels=['Tradicionales', 'Riesgo Financiero', 'Tecnológico'],
                    values=[9, 90, 1.2],
                    hole=.3,
                    marker_colors=['#4CAF50', '#FF6B6B', '#2196F3']
                )])
                fig_dist.update_layout(
                    title="Distribución de Perfiles",
                    height=250,
                    showlegend=False
                )
                st.plotly_chart(fig_dist, use_container_width=True)
        
        # Hallazgo 2
        with st.expander("⚠️ Hallazgo 2: El Agujero Negro del Riesgo Financiero"):
            st.error("""
            **El Clúster de Riesgo Financiero presenta características alarmantes:**
            
            🚨 **90% de la cartera** está en este segmento
            🚨 **97% de retención** - prácticamente imposible salir
            🚨 **18 días de mora promedio** vs 1.5 días en Tradicionales
            🚨 **Saldos mínimos** de apenas $316 en promedio
            """)
            
            # Visualización de la matriz de transición
            fig_transition = go.Figure(data=go.Heatmap(
                z=[[0.77, 0.22, 0.01],
                   [0.03, 0.97, 0.01],
                   [0.07, 0.48, 0.45]],
                x=['Tradicionales', 'Riesgo Financiero', 'Tecnológico'],
                y=['Tradicionales', 'Riesgo Financiero', 'Tecnológico'],
                text=[[f'{v:.0%}' for v in row] for row in [[0.77, 0.22, 0.01], [0.03, 0.97, 0.01], [0.07, 0.48, 0.45]]],
                texttemplate='%{text}',
                colorscale='RdYlBu_r',
                showscale=True
            ))
            fig_transition.update_layout(
                title="Matriz de Transición Anual - El Agujero Negro",
                xaxis_title="Destino",
                yaxis_title="Origen",
                height=350
            )
            st.plotly_chart(fig_transition, use_container_width=True)
        
        # Hallazgo 3
        with st.expander("🚀 Hallazgo 3: El Perfil Tecnológico como Indicador de Riesgo"):
            col1, col2 = st.columns(2)
            with col1:
                st.warning("""
                **El segmento más rentable es también el más inestable:**
                
                ⚡ **Mayor capital prestado**: $27,802
                ⚡ **Uso intensivo de servicios**: Recargas, pagos, transferencias
                ⚡ **PERO**: 48% migra a Riesgo Financiero al año siguiente
                ⚡ Actúa como "trampolín" hacia el riesgo
                """)
            with col2:
                # Gráfico de flujo de migración
                fig_flow = go.Figure(go.Sankey(
                    node=dict(
                        pad=15,
                        thickness=20,
                        line=dict(color="black", width=0.5),
                        label=["Tecnológico T0", "Riesgo Financiero T1", "Tecnológico T1", "Tradicionales T1"],
                        color=["#2196F3", "#FF6B6B", "#2196F3", "#4CAF50"]
                    ),
                    link=dict(
                        source=[0, 0, 0],
                        target=[1, 2, 3],
                        value=[48, 45, 7],
                        color=["rgba(255,107,107,0.4)", "rgba(33,150,243,0.4)", "rgba(76,175,80,0.4)"]
                    )
                ))
                fig_flow.update_layout(
                    title="Flujo de Migración del Perfil Tecnológico",
                    height=300
                )
                st.plotly_chart(fig_flow, use_container_width=True)
    
    with tabs[1]:
        st.markdown("## 💡 Recomendaciones Estratégicas")
        
        # Recomendación 1: Calidad de Datos
        st.markdown("### 📊 1. Mejora en la Gestión de Datos")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info("""
            **Acciones Inmediatas:**
            
            🔹 **Estandarización de bases de datos**
            - Proceso riguroso de limpieza y normalización
            - Eliminación de duplicados y consolidación
            
            🔹 **Enriquecimiento de variables**
            - Mejorar categorización de Actividad Económica
            - Incorporar sector económico específico de EE.UU.
            
            🔹 **Actualización periódica**
            - Establecer política de actualización trimestral
            - El contexto migrante es altamente dinámico
            """)
        with col2:
            # Indicadores de calidad de datos
            quality_metrics = pd.DataFrame({
                'Métrica': ['Completitud', 'Consistencia', 'Actualidad', 'Precisión'],
                'Estado Actual': [65, 70, 55, 75],
                'Meta': [95, 95, 90, 95]
            })
            
            fig_quality = go.Figure()
            fig_quality.add_trace(go.Bar(
                name='Estado Actual',
                x=quality_metrics['Métrica'],
                y=quality_metrics['Estado Actual'],
                marker_color='#FF6B6B'
            ))
            fig_quality.add_trace(go.Bar(
                name='Meta',
                x=quality_metrics['Métrica'],
                y=quality_metrics['Meta'],
                marker_color='#4CAF50'
            ))
            fig_quality.update_layout(
                title="Calidad de Datos: Actual vs Meta (%)",
                height=300,
                barmode='group'
            )
            st.plotly_chart(fig_quality, use_container_width=True)
        
        # Recomendación 2: Análisis Financiero
        st.markdown("### 💰 2. Análisis de Rentabilidad por Clúster")
        
        with st.container():
            st.error("""
            **⚠️ CRÍTICO: Comprender el costo real de cada segmento**
            
            En un entorno competitivo, no conocer la rentabilidad real por socio puede dejar a la institución en desventaja 
            frente a competidores más ágiles que aprovechan la analítica avanzada.
            """)
                   
        # Recomendación 3: Estrategias Diferenciadas
        st.markdown("### 🎯 3. Implementación de Estrategias por Perfil")
        
        strategy_tabs = st.tabs(["Tradicionales", "Riesgo Financiero", "Tecnológico"])
        
        with strategy_tabs[0]:
            st.success("""
            **📈 Estrategias para Socios Tradicionales (9%)**
            
            **1. Programa de Incentivos Digitales**
            - 🎁 Sorteos mensuales para usuarios de app
            - 💰 Bonificaciones por uso múltiple de servicios
            - 📱 Onboarding digital asistido
            
            **2. Venta Cruzada Premium**
            - 🏆 Productos exclusivos para socios leales
            - 📊 Dashboards personalizados de inversión
            - 🔄 Migración gradual a servicios digitales
            """)
            
        with strategy_tabs[1]:
            st.error("""
            **🚨 Estrategias para Riesgo Financiero (90%)**
            
            **1. Programa Intensivo de Prevención de Mora**
            - 📞 Llamadas preventivas 72-48h antes del vencimiento
            - 💬 Sistema automatizado de mensajes (SMS/WhatsApp)
            - 🎯 Sistema Poka-Yoke de alertas automáticas
            
            **2. Educación Financiera Obligatoria**
            - 📚 Módulos online de gestión financiera
            - 🏆 Incentivos por completar cursos
            - 💳 Productos de transición con límites controlados
            """)
            
        with strategy_tabs[2]:
            st.info("""
            **🚀 Estrategias para Tecnológico Multiservicios (1.2%)**
            
            **1. Programa VIP de Membresías Exclusivas**
            - 👑 Tres niveles: Básico, Premium, Elite
            - 💎 Beneficios escalables según comportamiento
            - 🔒 Monitoreo proactivo para prevenir migración
            
            **2. Acompañamiento Personalizado**
            - 👤 Gestor personal asignado
            - 📊 Reportes mensuales de salud financiera
            - 🎯 Alertas tempranas de riesgo
            """)
    
    with tabs[2]:
        st.markdown("## 📊 Resumen de Hallazgos por Perfil")
        
        # Crear visualización comparativa interactiva
        profiles_comparison = pd.DataFrame({
            'Característica': ['Edad Promedio', 'Ingresos Mensuales', 'Saldo DPF', 'Capital Prestado', 'Días de Mora', 'Uso Digital'],
            'Tradicionales': [45.1, 3558.96, 27597.17, 21576.06, 1.5, 20],
            'Riesgo Financiero': [38.4, 3759.42, 315.78, 21282.22, 18.0, 10],
            'Tecnológico': [39.6, 3962.25, 7656.16, 27802.60, 10.2, 100]
        })
        
        # Normalizar valores para mejor visualización
        for col in ['Tradicionales', 'Riesgo Financiero', 'Tecnológico']:
            max_vals = profiles_comparison[[col]].max()
            profiles_comparison[f'{col}_norm'] = profiles_comparison[col] / profiles_comparison[col].max() * 100
        
        # Crear gráfico de radar mejorado
        fig_radar = go.Figure()
        
        fig_radar.add_trace(go.Scatterpolar(
            r=[45.1/45.1*100, 3558.96/3962.25*100, 27597.17/27597.17*100, 21576.06/27802.60*100, (20-1.5)/18*100, 20],
            theta=profiles_comparison['Característica'],
            fill='toself',
            name='Tradicionales',
            line_color='#4CAF50',
            fillcolor='rgba(76,175,80,0.2)'
        ))
        
        fig_radar.add_trace(go.Scatterpolar(
            r=[38.4/45.1*100, 3759.42/3962.25*100, 315.78/27597.17*100, 21282.22/27802.60*100, (20-18)/18*100, 10],
            theta=profiles_comparison['Característica'],
            fill='toself',
            name='Riesgo Financiero',
            line_color='#FF6B6B',
            fillcolor='rgba(255,107,107,0.2)'
        ))
        
        fig_radar.add_trace(go.Scatterpolar(
            r=[39.6/45.1*100, 3962.25/3962.25*100, 7656.16/27597.17*100, 27802.60/27802.60*100, (20-10.2)/18*100, 100],
            theta=profiles_comparison['Característica'],
            fill='toself',
            name='Tecnológico',
            line_color='#2196F3',
            fillcolor='rgba(33,150,243,0.2)'
        ))
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=True,
            title="Comparación Multidimensional de Perfiles",
            height=500
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)
        
        # Tabla comparativa detallada
        st.markdown("### 📋 Métricas Detalladas por Perfil")
        
        detailed_metrics = pd.DataFrame({
            'Métrica': ['Tamaño del Segmento', 'Edad Promedio', 'Ingresos Mensuales', 'Saldo DPF', 
                       'Capital Prestado', 'Días de Mora', 'Calificación', 'Riesgo de Migración'],
            'Socios Tradicionales': ['9% (2,161)', '45.1 años', '$3,558.96', '$27,597.17', 
                                   '$21,576.06', '1.5 días', 'A-2', '22% → Riesgo'],
            'Riesgo Financiero': ['90% (21,613)', '38.4 años', '$3,759.42', '$315.78', 
                                '$21,282.22', '18.0 días', 'A-3', '97% permanencia'],
            'Tecnológico Multiservicios': ['1.2% (288)', '39.6 años', '$3,962.25', '$7,656.16', 
                                         '$27,802.60', '10.2 días', 'A-2', '48% → Riesgo']
        })
        
        st.dataframe(detailed_metrics, use_container_width=True)
