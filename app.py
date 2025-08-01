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
            "🎯 Segmentos y KPIs",
            "🧪 Simulador Estratégico",
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
    
    # Métricas en tiempo real en sidebar
    st.markdown("### 📈 Dashboard en Vivo")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Socios", "48,127", "+2.3%")
    with col2:
        st.metric("Remesas 2024", "$5.49B", "+8.1%")
    
    # Progreso del pitch
    progress = (list(selected.split(" ", 1)).index(selected.split(" ", 1)[1]) if " " in selected else 0) / 5
    st.progress(progress)
    st.caption(f"Progreso del pitch: {int(progress*100)}%")

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
            🚀 EL BOOM FINANCIERO QUE ECUADOR ESTÁ IGNORANDO
        </h1>
        <p style="color: #f0f0f0; font-size: 1.4rem; margin-top: 1rem; font-weight: 300;">
            Mientras otros sectores luchan, los migrantes mueven <strong>$5.8 BILLONES</strong> anuales
        </p>
    </div>
    ''', unsafe_allow_html=True)

    # Hook emocional y datos impactantes
    st.markdown('''
    <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%); padding: 2rem; border-radius: 15px; margin-bottom: 2rem; border-left: 6px solid #ff6b6b;">
        <h2 style="color: #2c3e50; font-size: 2.2rem; margin-bottom: 1rem; text-align: center;">
            💰 LA REALIDAD QUE CAMBIA TODO
        </h2>
        <div style="font-size: 1.3rem; color: #2c3e50; line-height: 1.8; text-align: center;">
            <strong>Cada 24 horas, los ecuatorianos en EE.UU. envían $15.1 millones a casa.</strong><br>
            <span style="font-size: 1.1rem; color: #e74c3c;">Eso es más que el PIB diario de 3 provincias juntas.</span><br><br>
            <em style="font-size: 1.2rem; color: #8e44ad;">"No son solo números... son 2.3 millones de ecuatorianos construyendo el futuro desde la distancia"</em>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Métricas impactantes con animación visual
    st.markdown("### 🔥 LOS NÚMEROS QUE ROMPEN ESQUEMAS")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(45deg, #FF6B6B, #FF8E53); padding: 1.5rem; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(255,107,107,0.3); transition: transform 0.3s;">
            <h2 style="color: white; font-size: 2.5rem; margin: 0; font-weight: 900;">$5.491B</h2>
            <p style="color: white; font-size: 1.1rem; margin: 0.5rem 0; font-weight: 600;">Remesas 2024</p>
            <small style="color: #ffe0e0; font-size: 0.9rem;">
                <strong>19x más</strong> que la Inversión<br>Extranjera Directa
            </small>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(45deg, #4ECDC4, #44A08D); padding: 1.5rem; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(78,205,196,0.3);">
            <h2 style="color: white; font-size: 2.5rem; margin: 0; font-weight: 900;">68%</h2>
            <p style="color: white; font-size: 1.1rem; margin: 0.5rem 0; font-weight: 600;">Desde EE.UU.</p>
            <small style="color: #e0f7f5; font-size: 0.9rem;">
                <strong>$942M</strong> trimestrales<br>desde Nueva York y NJ
            </small>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(45deg, #A770EF, #CF57A3); padding: 1.5rem; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(167,112,239,0.3);">
            <h2 style="color: white; font-size: 2.5rem; margin: 0; font-weight: 900;">$208M</h2>
            <p style="color: white; font-size: 1.1rem; margin: 0.5rem 0; font-weight: 600;">Solo a Azuay</p>
            <small style="color: #f0e5ff; font-size: 0.9rem;">
                En <strong>solo 3 meses</strong><br>Cuenca es epicentro
            </small>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="background: linear-gradient(45deg, #FFA726, #FB8C00); padding: 1.5rem; border-radius: 15px; text-align: center; box-shadow: 0 8px 16px rgba(255,167,38,0.3);">
            <h2 style="color: white; font-size: 2.5rem; margin: 0; font-weight: 900;">21%</h2>
            <p style="color: white; font-size: 1.1rem; margin: 0.5rem 0; font-weight: 600;">Inversión Inmobiliaria</p>
            <small style="color: #fff3e0; font-size: 0.9rem;">
                <strong>1 de cada 5</strong> familias<br>construye patrimonio
            </small>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Comparativa impactante
    st.markdown('''
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 15px; margin: 2rem 0;">
        <h3 style="color: white; text-align: center; font-size: 1.8rem; margin-bottom: 1.5rem;">
            🥊 REMESAS vs. EXPORTACIONES TRADICIONALES
        </h3>
        <div style="display: flex; justify-content: space-around; text-align: center;">
            <div>
                <h4 style="color: #4CAF50; font-size: 1.5rem; margin: 0;">$5.491B</h4>
                <p style="color: white; margin: 0;">💸 REMESAS</p>
            </div>
            <div style="color: white; font-size: 2rem; align-self: center;">VS</div>
            <div>
                <h4 style="color: #FF9800; font-size: 1.2rem; margin: 0;">$5.191B</h4>
                <p style="color: white; margin: 0;">🦐 Camarón</p>
            </div>
            <div style="color: white; font-size: 2rem; align-self: center;">VS</div>
            <div>
                <h4 style="color: #FFC107; font-size: 1.2rem; margin: 0;">$3.600B</h4>
                <p style="color: white; margin: 0;">🍌 Banano</p>
            </div>
        </div>
        <p style="color: #e8eaf6; text-align: center; margin-top: 1rem; font-style: italic;">
            Los migrantes son el motor económico #1 del país
        </p>
        <div style="text-align: right; margin-top: 0.3rem;">
        <small style="color: #bdbdbd;">Fuente: Banco Central del Ecuador</small>
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

    # La oportunidad dorada específica
    st.markdown('''
    <div style="background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%); padding: 2.5rem; border-radius: 20px; margin: 2rem 0; text-align: center; border: 3px solid #FF8C00; box-shadow: 0 12px 24px rgba(255,165,0,0.4);">
        <h2 style="color: #8B4513; font-size: 2.8rem; margin-bottom: 1rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);">
            🎯 OPORTUNIDAD RAÍCES ANDINAS
        </h2>
        <div style="background: rgba(255,255,255,0.9); padding: 1.5rem; border-radius: 15px; margin: 1rem 0;">
            <p style="color: #2c3e50; font-size: 1.4rem; margin-bottom: 1rem; font-weight: 600;">
                Si RAÍCES ANDINAS captura solo el <strong style="color: #e74c3c;">3%</strong> de las remesas de Azuay:
            </p>
            <h1 style="color: #27ae60; font-size: 3.5rem; margin: 1rem 0; font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);">
                +$6.24M
            </h1>
            <p style="color: #8B4513; font-size: 1.2rem; font-weight: 600;">
                trimestrales en nuevos depósitos
            </p>
        </div>
        <div style="display: flex; justify-content: space-around; margin-top: 2rem;">
            <div>
                <h3 style="color: #2c3e50; font-size: 1.5rem; margin: 0;">630</h3>
                <p style="color: #8B4513; margin: 0;">Nuevos Socios</p>
            </div>
            <div>
                <h3 style="color: #2c3e50; font-size: 1.5rem; margin: 0;">$24.96M</h3>
                <p style="color: #8B4513; margin: 0;">Potencial Anual</p>
            </div>
            <div>
                <h3 style="color: #2c3e50; font-size: 1.5rem; margin: 0;">40%</h3>
                <p style="color: #8B4513; margin: 0;">Crecimiento Cartera</p>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Insights estratégicos
    col_insight1, col_insight2 = st.columns(2)
    
    with col_insight1:
        st.markdown('''
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 15px; height: 200px;">
            <h4 style="color: white; margin-bottom: 1rem;">💡 INSIGHT DEMOGRÁFICO</h4>
            <p style="color: #e8eaf6; font-size: 1rem; line-height: 1.6;">
                Los socios migrantes de RAÍCES (39 años promedio) están en su <strong>pico de productividad financiera</strong>, 
                6 años mayores que el migrante promedio (32.9 años). Esto significa mayor capacidad de ahorro y planificación a largo plazo.
            </p>
        </div>
        ''', unsafe_allow_html=True)
    
    with col_insight2:
        st.markdown('''
        <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); padding: 1.5rem; border-radius: 15px; height: 200px;">
            <h4 style="color: #2c3e50; margin-bottom: 1rem;">🎯 VENTAJA GEOGRÁFICA</h4>
            <p style="color: #2c3e50; font-size: 1rem; line-height: 1.6;">
                El 59% de ecuatorianos en EE.UU. viven en NY y NJ. RAÍCES puede crear <strong>alianzas estratégicas</strong> 
                en estas zonas para capturar remesas directamente desde el origen, reduciendo costos de intermediación.
            </p>
        </div>
        ''', unsafe_allow_html=True)

    # Call to action final
    st.markdown('''
    <div style="background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); padding: 2rem; border-radius: 15px; text-align: center; margin-top: 2rem;">
        <h3 style="color: white; font-size: 1.8rem; margin-bottom: 1rem;">
            🚀 EL MOMENTO ES AHORA
        </h3>
        <p style="color: #bdc3c7; font-size: 1.2rem; margin-bottom: 1.5rem;">
            Mientras las instituciones tradicionales ignoran este mercado, RAÍCES ANDINAS puede posicionarse como 
            <strong style="color: #3498db;">EL PUENTE FINANCIERO</strong> entre los sueños migrantes y la realidad familiar.
        </p>
        <div style="background: rgba(52, 152, 219, 0.2); padding: 1rem; border-radius: 10px; border-left: 4px solid #3498db;">
            <p style="color: #ecf0f1; font-size: 1.1rem; margin: 0; font-style: italic;">
                "No estamos hablando de capturar remesas... estamos hablando de construir el futuro financiero de las familias ecuatorianas"
            </p>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Próximo paso
    st.success("🎯 **PRÓXIMO PASO:** Implementar segmentación inteligente de socios migrantes para capturar esta oportunidad de $5.8B proyectados para 2025.")

    # Métricas adicionales en sidebar o expandible
    with st.expander("📊 Datos Adicionales de Soporte"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Inclusión Financiera Ecuador", "74%", "26% sin bancarizar")
            st.metric("Pagos Digitales", "51%", "49% usa efectivo")
        with col2:
            st.metric("Concentración NY + NJ", "59%", "1.35M ecuatorianos")
            st.metric("Crecimiento Q1 2025", "9.5%", "vs Q1 2024")
        with col3:
            st.metric("Destino Vivienda", "21%", "$1.154B anuales")
            st.metric("Préstamos Formales", "25%", "75% mercado potencial")

elif "🏦 Quiénes Somos" in selected:
    st.markdown('<h1 class="main-header">🏦 COAC Raíces Andinas</h1>', unsafe_allow_html=True)
    st.markdown("### *28 años construyendo sueños, conectando corazones*")
    
    # Datos clave en columnas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Años de Historia", "28", "Desde 1996")
        st.metric("Provincias", "7", "Cobertura nacional")
    with col2:
        st.metric("Socios Activos", "48,127", "+2.3% anual")
        st.metric("Patrimonio", "$85M", "Sólido respaldo")
    with col3:
        st.metric("Oficinas", "24", "Cerca de ti")
        st.metric("Empleados", "420", "Equipo comprometido")

    # Análisis FODA visual mejorado
    st.markdown("### 🔍 Análisis Estratégico FODA")
    foda_col1, foda_col2 = st.columns(2)
    
    with foda_col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%); padding: 20px; border-radius: 15px; margin: 10px 0;'>
            <h4>💪 FORTALEZAS</h4>
            <ul>
                <li>Capital sólido ($85M patrimonio)</li>
                <li>Base migratoria fiel (15,000+ socios)</li>
                <li>Tecnología en expansión digital</li>
                <li>Presencia territorial consolidada</li>
            </ul>
        </div>
        
        <div style='background: linear-gradient(135deg, #cce5ff 0%, #b3d9ff 100%); padding: 20px; border-radius: 15px; margin: 10px 0;'>
            <h4>🌟 OPORTUNIDADES</h4>
            <ul>
                <li>Remesas crecientes (+8.1% anual)</li>
                <li>Alianzas con fintech globales</li>
                <li>Mercado digital subutilizado</li>
                <li>Nuevos productos migratorios</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with foda_col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%); padding: 20px; border-radius: 15px; margin: 10px 0;'>
            <h4>⚠️ DEBILIDADES</h4>
            <ul>
                <li>Adopción digital lenta (45% vs 70% mercado)</li>
                <li>Canales móviles subutilizados</li>
                <li>Segmentación básica de clientes</li>
                <li>Productos poco personalizados</li>
            </ul>
        </div>
        
        <div style='background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%); padding: 20px; border-radius: 15px; margin: 10px 0;'>
            <h4>🚨 AMENAZAS</h4>
            <ul>
                <li>Fintech agresivas (Nequi, Kushki)</li>
                <li>Bancos con mejor UX digital</li>
                <li>Migración de clientes jóvenes</li>
                <li>Regulación cambiante</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Timeline de crecimiento
    st.markdown("### 📅 Nuestra Evolución")
    timeline_data = [
        {"año": "1996", "hito": "Fundación en Cuenca", "impacto": "500 socios fundadores"},
        {"año": "2005", "hito": "Expansión nacional", "impacto": "7 provincias, 5,000 socios"},
        {"año": "2015", "hito": "Era digital", "impacto": "Banca online, 25,000 socios"},
        {"año": "2020", "hito": "Pandemia resiliente", "impacto": "Crecimiento del 15%"},
        {"año": "2024", "hito": "Presente", "impacto": "48,127 socios, $85M patrimonio"},
        {"año": "2025", "hito": "Futuro: Segmentación IA", "impacto": "Meta: 60,000 socios"}
    ]
    
    for item in timeline_data:
        color = "#4ECDC4" if item["año"] != "2025" else "#FF6B6B"
        st.markdown(f"""
        <div class="timeline-item" style="border-left-color: {color}">
            <strong>{item['año']}</strong>: {item['hito']}<br>
            <small>{item['impacto']}</small>
        </div>
        """, unsafe_allow_html=True)

elif "🔬 Metodología" in selected:
    st.markdown('<h1 class="main-header">🔬 Ciencia de Datos para Decisiones Inteligentes</h1>', unsafe_allow_html=True)
    
    # Explicación visual del proceso
    st.markdown("### 🧩 El Desafío: De 48,127 socios a 3 segmentos estratégicos")
    
    metodologia_tabs = st.tabs(["🎯 Problema", "🔧 Solución", "⚙️ Algoritmo", "📊 Validación"])
    
    with metodologia_tabs[0]:
        st.markdown("""
        #### 🎯 El Problema Real
        
        **Antes:** 
        - Un solo producto para todos los socios
        - Campañas masivas sin personalización  
        - 23% de tasa de respuesta promedio
        - Pérdida de socios jóvenes (-5% anual)
        
        **El dilema:** ¿Cómo identificar quién necesita qué, cuándo y cómo?
        """)
        
        # Simulación visual del problema
        problema_data = pd.DataFrame({
            'Segmento': ['Todos los socios'] * 5,
            'Métrica': ['Tasa Respuesta', 'Satisfacción', 'Retención', 'Cross-selling', 'NPS'],
            'Valor_Actual': [23, 6.2, 78, 15, 45],
            'Potencial': [45, 8.5, 90, 35, 70]
        })
        
        fig_problema = px.bar(problema_data, x='Métrica', y=['Valor_Actual', 'Potencial'], 
                             title="Brecha de Oportunidad: Actual vs Potencial",
                             barmode='group')
        st.plotly_chart(fig_problema, use_container_width=True)
    
    with metodologia_tabs[1]:
        st.markdown("""
        #### 🔧 La Solución: Segmentación Inteligente
        
        **Analogía futbolística:** 
        - Imagina armar 3 equipos de fútbol perfectos
        - Cada jugador va al equipo donde mejor encaja
        - Los equipos comparten estrategias y tácticas similares
        - Cada equipo necesita un entrenamiento específico
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            **⚽ Equipo Tradicional**
            - Experiencia y estabilidad
            - Juego conservador
            - Alta fidelidad
            """)
        with col2:
            st.markdown("""
            **⚽ Equipo Riesgo**  
            - Necesita más apoyo
            - Potencial de mejora
            - Requiere coaching
            """)
        with col3:
            st.markdown("""
            **⚽ Equipo Tech**
            - Innovación y velocidad
            - Adopción rápida
            - Multicanal
            """)
    
    with metodologia_tabs[2]:
        st.markdown("""
        #### ⚙️ K-Means: El Algoritmo que Revoluciona Nuestra Estrategia
        
        **¿Cómo funciona K-Means?**
        1. **Paso 1:** Definimos 3 "capitanes" de equipo al azar
        2. **Paso 2:** Cada socio se une al capitán más parecido a él
        3. **Paso 3:** Los capitanes se mueven al centro de su equipo
        4. **Paso 4:** Repetimos hasta que los equipos sean estables
        """)
        
        # Visualización interactiva del algoritmo
        st.markdown("##### 🎮 Simulador K-Means")
        if st.button("🎲 Ver Algoritmo en Acción"):
            placeholder = st.empty()
            
            # Simulación de iteraciones
            for i in range(4):
                fig_sim = px.scatter(df_socios.sample(50), x='edad', y='ingresos', 
                                   color='cluster', size='saldo_dpf',
                                   title=f"Iteración {i+1}: Formando Equipos",
                                   color_discrete_map={0: '#8dd3c7', 1: '#ffffb3', 2: '#bebada'})
                placeholder.plotly_chart(fig_sim, use_container_width=True)
                time.sleep(1)
        
        # Variables utilizadas
        st.markdown("""
        **Variables Clave del Modelo:**
        - 👤 **Edad:** Generación y comportamiento
        - 💰 **Ingresos:** Capacidad financiera  
        - 🏦 **Saldo DPF:** Perfil ahorrador
        - 💳 **Capital prestado:** Propensión al crédito
        - ⏰ **Días de mora:** Nivel de riesgo
        - 📱 **Uso digital:** Adopción tecnológica
        """)
    
    with metodologia_tabs[3]:
        st.markdown("""
        #### 📊 Validación del Modelo
        
        **Métricas de Calidad:**
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Silhouette Score", "0.73", "Excelente separación")
        with col2:
            st.metric("Inercia Within-Cluster", "1,245", "Grupos compactos")
        with col3:
            st.metric("Varianza Explicada", "87%", "Modelo robusto")
        
        st.success("✅ **Validación exitosa:** El modelo identifica 3 segmentos claros y diferenciados con alta confianza estadística.")

elif "🎯 Segmentos y KPIs" in selected:
    st.markdown('<h1 class="main-header">🎯 Los 3 Equipos Ganadores</h1>', unsafe_allow_html=True)
    
    # Resumen ejecutivo de segmentos
    st.markdown("### 📋 Resumen Ejecutivo")
    resumen_cols = st.columns(3)
    
    segmentos_info = [
        {
            "nombre": "🧓 Tradicional", 
            "color": "#8dd3c7",
            "socios": "14,438 (30%)",
            "valor": "$42M cartera",
            "oportunidad": "Digitalización asistida",
            "riesgo": "Muy bajo",
            "estrategia": "Fidelización premium"
        },
        {
            "nombre": "⚠️ Riesgo", 
            "color": "#ffffb3", 
            "socios": "24,064 (50%)",
            "valor": "$28M cartera", 
            "oportunidad": "Recuperación proactiva",
            "riesgo": "Alto",
            "estrategia": "Prevención y educación"
        },
        {
            "nombre": "📱 Tech", 
            "color": "#bebada",
            "socios": "9,625 (20%)",
            "valor": "$35M cartera",
            "oportunidad": "Productos premium",
            "riesgo": "Fuga a fintech",
            "estrategia": "Innovación continua"
        }
    ]
    
    for i, seg in enumerate(segmentos_info):
        with resumen_cols[i]:
            st.markdown(f"""
            <div class="segment-card" style="background-color: {seg['color']};">
                <h3>{seg['nombre']}</h3>
                <p><strong>Socios:</strong> {seg['socios']}</p>
                <p><strong>Cartera:</strong> {seg['valor']}</p>
                <p><strong>Oportunidad:</strong> {seg['oportunidad']}</p>
                <p><strong>Estrategia:</strong> {seg['estrategia']}</p>
            </div>
            """, unsafe_allow_html=True)

    # Radar chart mejorado
    st.markdown("### 📊 Perfil Comparativo de KPIs")
    
    # Normalizar datos para mejor visualización
    def normalizar(datos, max_vals):
        return [datos[i]/max_vals[i]*100 for i in range(len(datos))]
    
    max_valores = [50, 5000, 30000, 30000, 20]  # Valores máximos para normalización
    
    tradicional_norm = normalizar(cluster_tradicional, max_valores)
    riesgo_norm = normalizar(cluster_riesgo, max_valores)
    tech_norm = normalizar(cluster_tech, max_valores)
    
    fig_radar = go.Figure()
    
    fig_radar.add_trace(go.Scatterpolar(
        r=tradicional_norm, theta=categorias, fill='toself', name='🧓 Tradicional',
        line_color='#8dd3c7', fillcolor='rgba(141, 211, 199, 0.3)'
    ))
    fig_radar.add_trace(go.Scatterpolar(
        r=riesgo_norm, theta=categorias, fill='toself', name='⚠️ Riesgo',
        line_color='#ffffb3', fillcolor='rgba(255, 255, 179, 0.3)'
    ))
    fig_radar.add_trace(go.Scatterpolar(
        r=tech_norm, theta=categorias, fill='toself', name='📱 Tech',
        line_color='#bebada', fillcolor='rgba(190, 186, 218, 0.3)'
    ))
    
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        title="Perfil de KPIs por Segmento (Escala 0-100)"
    )
    st.plotly_chart(fig_radar, use_container_width=True)
    
    # Análisis de rentabilidad por segmento
    st.markdown("### 💰 Análisis de Rentabilidad")
    
    rentabilidad_data = pd.DataFrame({
        'Segmento': ['Tradicional', 'Riesgo', 'Tech'],
        'ROE': [15.2, 4.1, 18.7],
        'Margen_Financiero': [8.5, 3.2, 9.8],
        'Costo_Servicio': [120, 180, 95],
        'Vida_Util_Cliente': [12, 4, 8]
    })
    
    # Gráfico de rentabilidad
    fig_rent = px.scatter(rentabilidad_data, x='ROE', y='Margen_Financiero', 
                         size='Vida_Util_Cliente', color='Segmento',
                         title="Matriz Rentabilidad vs Margen (tamaño = años de vida útil)",
                         color_discrete_map={'Tradicional': '#8dd3c7', 'Riesgo': '#ffffb3', 'Tech': '#bebada'})
    st.plotly_chart(fig_rent, use_container_width=True)
    
    # Recomendaciones por segmento
    st.markdown("### 🎯 Recomendaciones Estratégicas")
    
    recom_tabs = st.tabs(["🧓 Tradicional", "⚠️ Riesgo", "📱 Tech"])
    
    with recom_tabs[0]:
        st.markdown("""
        #### 🧓 Segmento Tradicional - "Los Leales"
        
        **Características:**
        - Mayor edad promedio (45 años)
        - Alto saldo en DPF ($27,597)
        - Muy baja morosidad (1.5 días)
        - Resistencia al cambio digital
        
        **Estrategias Recomendadas:**
        - 🏆 Programa VIP con beneficios exclusivos
        - 👨‍🏫 Talleres de educación digital presencial
        - 📞 Canal telefónico premium 24/7
        - 🎁 Productos de jubilación y legado
        """)
    
    with recom_tabs[1]:
        st.markdown("""
        #### ⚠️ Segmento Riesgo - "Los Recuperables"
        
        **Características:**
        - Morosidad alta (18 días promedio)
        - Bajo saldo DPF ($316)
        - Mayor volumen (50% de socios)
        - Potencial de mejora significativo
        
        **Estrategias Recomendadas:**
        - 🚨 Sistema de alertas tempranas
        - 📚 Programa intensivo de educación financiera
        - 💬 Call center proactivo de cobranza
        - 🤝 Reestructuración facilitada de deudas
        """)
    
    with recom_tabs[2]:
        st.markdown("""
        #### 📱 Segmento Tech - "Los Innovadores"
        
        **Características:**
        - Edad promedio joven (40 años)
        - Alta adopción digital
        - Multiproducto activo
        - Mayor rentabilidad (ROE 18.7%)
        
        **Estrategias Recomendadas:**
        - 🚀 App móvil con features premium
        - 🏅 Programa de referidos gamificado
        - 💳 Productos fintech (wallets, cripto)
        - 🌍 Servicios para migrantes digitales
        """)

elif "🧪 Simulador Estratégico" in selected:
    st.markdown('<h1 class="main-header">🧪 Laboratorio de Estrategias</h1>', unsafe_allow_html=True)
    st.markdown("### *Experimenta el impacto de tus decisiones antes de implementarlas*")
    
    # Simulador interactivo mejorado
    st.markdown("#### 🎮 Simulador de Impacto")
    
    sim_tabs = st.tabs(["📞 Prevención Mora", "🎯 Cross-Selling", "📱 Digitalización", "💰 ROI Total"])
    
    with sim_tabs[0]:
        st.markdown("##### Estrategia: Llamadas Preventivas al Segmento Riesgo")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            efectividad = st.slider("Efectividad de llamadas preventivas (%)", 0, 100, 35)
            cobertura = st.slider("% del segmento Riesgo contactado", 0, 100, 60)
            
        with col2:
            # Cálculos en tiempo real
            socios_riesgo = 24064
            socios_contactados = int(socios_riesgo * cobertura / 100)
            socios_mejorados = int(socios_contactados * efectividad / 100)
            
            st.metric("Socios Contactados", f"{socios_contactados:,}")
            st.metric("Socios que Mejoran", f"{socios_mejorados:,}")
        
        # Impacto financiero
        mora_actual = 18
        reduccion_mora = efectividad * 0.3  # Factor de impacto
        nueva_mora = max(1, mora_actual - reduccion_mora)
        
        col3, col4, col5 = st.columns(3)
        with col3:
            st.metric("Mora Actual", f"{mora_actual} días", delta=None)
        with col4:
            st.metric("Nueva Mora", f"{nueva_mora:.1f} días", delta=f"-{reduccion_mora:.1f}")
        with col5:
            ahorro_provisions = socios_mejorados * 850  # Ahorro promedio por socio
            st.metric("Ahorro Provisiones", f"${ahorro_provisions:,}")
    
    with sim_tabs[1]:
        st.markdown("##### Estrategia: Cross-Selling Dirigido por Segmento")
        
        # Configuración por segmento
        st.markdown("**Configurar campañas por segmento:**")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**🧓 Tradicional**")
            trad_producto = st.selectbox("Producto", ["DPF Plus", "Seguro Vida", "Crédito Hipotecario"], key="trad")
            trad_conversion = st.slider("Tasa conversión (%)", 0, 50, 15, key="trad_conv")
            
        with col2:
            st.markdown("**⚠️ Riesgo**")
            riesgo_producto = st.selectbox("Producto", ["Microseguro", "Ahorro Programado", "Crédito Emergencia"], key="riesgo")
            riesgo_conversion = st.slider("Tasa conversión (%)", 0, 30, 8, key="riesgo_conv")
            
        with col3:
            st.markdown("**📱 Tech**")
            tech_producto = st.selectbox("Producto", ["Cuenta Digital", "Inversiones Online", "Crédito Express"], key="tech")
            tech_conversion = st.slider("Tasa conversión (%)", 0, 60, 25, key="tech_conv")
        
        # Cálculo de impacto
        ingresos_adicionales = (
            14438 * trad_conversion/100 * 2500 +  # Tradicional
            24064 * riesgo_conversion/100 * 800 +  # Riesgo  
            9625 * tech_conversion/100 * 3500     # Tech
        )
        
        st.markdown("### 💰 Impacto Proyectado Cross-Selling")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Nuevos Productos", f"{int((14438*trad_conversion + 24064*riesgo_conversion + 9625*tech_conversion)/100):,}")
        with col2:
            st.metric("Ingresos Adicionales", f"${ingresos_adicionales:,.0f}")
        with col3:
            costo_campanha = 45000  # Costo estimado campaña
            roi_crossell = (ingresos_adicionales - costo_campanha) / costo_campanha * 100
            st.metric("ROI Campaña", f"{roi_crossell:.1f}%")
    
    with sim_tabs[2]:
        st.markdown("##### Estrategia: Aceleración Digital")
        
        digitalizacion_objetivo = st.slider("Meta: % de socios usando banca digital", 45, 85, 65)
        tiempo_implementacion = st.slider("Tiempo de implementación (meses)", 6, 24, 12)
        
        # Beneficios de digitalización
        socios_actuales_digital = int(48127 * 0.45)  # 45% actual
        socios_objetivo_digital = int(48127 * digitalizacion_objetivo / 100)
        nuevos_digitales = socios_objetivo_digital - socios_actuales_digital
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Socios Digitales Actuales", f"{socios_actuales_digital:,}")
            st.metric("Socios Digitales Objetivo", f"{socios_objetivo_digital:,}")
        with col2:
            ahorro_operacional = nuevos_digitales * 24  # $24 ahorro anual por socio digital
            st.metric("Nuevos Socios Digitales", f"{nuevos_digitales:,}")
            st.metric("Ahorro Operacional Anual", f"${ahorro_operacional:,}")
        
        # Gráfico de progresión
        meses = list(range(1, tiempo_implementacion + 1))
        progresion_digital = [45 + (digitalizacion_objetivo - 45) * (mes / tiempo_implementacion) for mes in meses]
        
        fig_digital = px.line(x=meses, y=progresion_digital, 
                             title="Proyección de Adopción Digital",
                             labels={'x': 'Mes', 'y': '% Adopción Digital'})
        fig_digital.add_hline(y=digitalizacion_objetivo, line_dash="dash", 
                             annotation_text=f"Meta: {digitalizacion_objetivo}%")
        st.plotly_chart(fig_digital, use_container_width=True)
    
    with sim_tabs[3]:
        st.markdown("##### 🎯 ROI Consolidado de Todas las Estrategias")
        
        # Resumen de impactos
        st.markdown("**Impacto Financiero Anual Proyectado:**")
        
        beneficios = {
            "Reducción Provisiones Mora": ahorro_provisions * 12,  # Anualizado
            "Ingresos Cross-Selling": ingresos_adicionales,
            "Ahorro Digitalización": ahorro_operacional,
            "Retención de Socios": 2400000  # Estimado valor de retención
        }
        
        costos = {
            "Implementación Call Center": 180000,
            "Campañas Marketing": 75000,
            "Desarrollo Tecnológico": 320000,
            "Capacitación Personal": 95000
        }
        
        total_beneficios = sum(beneficios.values())
        total_costos = sum(costos.values())
        roi_total = (total_beneficios - total_costos) / total_costos * 100
        
        # Visualización del ROI
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Beneficios", f"${total_beneficios:,.0f}")
        with col2:
            st.metric("Total Inversión", f"${total_costos:,.0f}")
        with col3:
            st.metric("ROI Total", f"{roi_total:.1f}%", delta="Excelente")
        
        # Gráfico de beneficios vs costos
        df_roi = pd.DataFrame({
            'Concepto': list(beneficios.keys()) + list(costos.keys()),
            'Valor': list(beneficios.values()) + [-x for x in costos.values()],
            'Tipo': ['Beneficio'] * len(beneficios) + ['Costo'] * len(costos)
        })
        
        fig_roi = px.bar(df_roi, x='Concepto', y='Valor', color='Tipo',
                        title="Análisis Costo-Beneficio de Estrategias",
                        color_discrete_map={'Beneficio': '#4ECDC4', 'Costo': '#FF6B6B'})
        fig_roi.update_xaxis(tickangle=45)
        st.plotly_chart(fig_roi, use_container_width=True)
        
        if roi_total > 200:
            st.success(f"🎉 ¡Excelente! ROI del {roi_total:.1f}% indica alta viabilidad del proyecto")
        elif roi_total > 100:
            st.info(f"✅ Bueno. ROI del {roi_total:.1f}% sugiere proyecto viable")
        else:
            st.warning(f"⚠️ ROI del {roi_total:.1f}% requiere optimización de estrategias")

elif "🏁 Plan de Acción" in selected:
    st.markdown('<h1 class="main-header">🏁 Hora de la Acción</h1>', unsafe_allow_html=True)
    st.markdown("### *De insights a resultados: El roadmap hacia el éxito*")
    
    # Resumen ejecutivo
    st.markdown("#### 📋 Resumen Ejecutivo")
    resumen_col1, resumen_col2 = st.columns([2, 1])
    
    with resumen_col1:
        st.markdown("""
        **La oportunidad es clara:** Ecuador recibirá $5.8B en remesas en 2025, y solo necesitamos capturar el 5% del mercado de Azuay para crecer $10M trimestrales.
        
        **La solución es precisa:** Segmentación inteligente nos permite personalizar servicios, reducir riesgos y maximizar rentabilidad con un ROI proyectado del 245%.
        
        **El momento es ahora:** Mientras competidores siguen estrategias masivas, nosotros implementamos inteligencia artificial para decisiones personalizadas.
        """)
    
    with resumen_col2:
        st.markdown("""
        <div class="metric-card">
            <h3>ROI Proyectado</h3>
            <h1>245%</h1>
            <p>En 12 meses</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Roadmap temporal
    st.markdown("#### 🗓️ Roadmap de Implementación")
    
    fases = [
        {
            "fase": "Fase 1: Preparación",
            "tiempo": "Mes 1-2",
            "objetivos": ["Conformar equipo de datos", "Validar modelo con muestra", "Definir KPIs de éxito"],
            "entregables": ["Equipo conformado", "Modelo validado", "Dashboard básico"],
            "responsable": "CTO + Gerencia Comercial"
        },
        {
            "fase": "Fase 2: Piloto",
            "tiempo": "Mes 3-4", 
            "objetivos": ["Implementar con 1,000 socios", "Probar estrategias por segmento", "Medir resultados iniciales"],
            "entregables": ["Campañas personalizadas", "Call center configurado", "Primeros resultados"],
            "responsable": "Gerencia Comercial + TI"
        },
        {
            "fase": "Fase 3: Escalamiento",
            "tiempo": "Mes 5-8",
            "objetivos": ["Desplegar a todos los socios", "Automatizar procesos", "Optimizar estrategias"],
            "entregables": ["Sistema en producción", "Procesos automatizados", "ROI positivo"],
            "responsable": "Toda la organización"
        },
        {
            "fase": "Fase 4: Consolidación",
            "tiempo": "Mes 9-12",
            "objetivos": ["Análisis de resultados", "Mejora continua", "Expansión a nuevos segmentos"],
            "entregables": ["Informe de impacto", "Modelo optimizado", "Nuevas oportunidades"],
            "responsable": "Gerencia General"
        }
    ]
    
    for i, fase in enumerate(fases):
        color = ["#4ECDC4", "#667eea", "#FF6B6B", "#95E1D3"][i]
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {color}20 0%, {color}40 100%); 
                    border-left: 5px solid {color}; padding: 20px; margin: 15px 0; border-radius: 10px;">
            <h4>{fase['fase']} ({fase['tiempo']})</h4>
            <p><strong>Responsable:</strong> {fase['responsable']}</p>
            <p><strong>Objetivos:</strong> {' • '.join(fase['objetivos'])}</p>
            <p><strong>Entregables:</strong> {' • '.join(fase['entregables'])}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Recursos necesarios
    st.markdown("#### 💼 Recursos Requeridos")
    
    recursos_cols = st.columns(3)
    
    with recursos_cols[0]:
        st.markdown("""
        ##### 👥 Equipo Humano
        - **Data Scientist** (1 FTE)
        - **Analista Marketing** (1 FTE) 
        - **Especialista Call Center** (2 FTE)
        - **Desarrollador** (0.5 FTE)
        - **Consultor externo** (3 meses)
        
        **Costo:** $15,000/mes
        """)
    
    with recursos_cols[1]:
        st.markdown("""
        ##### 🖥️ Tecnología
        - **Plataforma Analytics** (Tableau/PowerBI)
        - **CRM avanzado** (Salesforce/HubSpot)
        - **Sistema de Llamadas** (upgrade)
        - **APIs de integración**
        - **Infraestructura cloud**
        
        **Costo:** $25,000 inicial + $5,000/mes
        """)
    
    with recursos_cols[2]:
        st.markdown("""
        ##### 📚 Capacitación
        - **Workshop segmentación** (todo el equipo)
        - **Certificación CRM** (equipo comercial)
        - **Análisis de datos** (gerencias)
        - **Atención personalizada** (call center)
        
        **Costo:** $8,000 total
        """)
    
    # Factores críticos de éxito
    st.markdown("#### 🎯 Factores Críticos de Éxito")
    
    factores_cols = st.columns(2)
    
    with factores_cols[0]:
        st.markdown("""
        ##### ✅ Elementos Clave
        - **Compromiso directivo:** Apoyo visible de gerencia general
        - **Calidad de datos:** Información completa y actualizada  
        - **Adopción del equipo:** Capacitación y cambio cultural
        - **Medición constante:** KPIs claros y seguimiento semanal
        - **Flexibilidad:** Capacidad de ajustar estrategias según resultados
        """)
    
    with factores_cols[1]:
        st.markdown("""
        ##### ⚠️ Riesgos a Mitigar
        - **Resistencia al cambio:** Plan de gestión del cambio
        - **Problemas técnicos:** Testing exhaustivo y plan B
        - **Sobrecarga operativa:** Implementación gradual
        - **Competencia:** Velocidad de ejecución
        - **Regulación:** Cumplimiento normativo constante
        """)
    
    # Métricas de éxito
    st.markdown("#### 📊 Métricas de Éxito")
    
    st.markdown("**KPIs Principales a monitorear mensualmente:**")
    
    kpis_data = pd.DataFrame({
        'KPI': ['Tasa de Respuesta Campañas', 'NPS por Segmento', 'Reducción Mora Segmento Riesgo', 
               'Adopción Digital', 'Cross-selling Rate', 'Costo por Adquisición'],
        'Baseline': ['23%', '45 puntos', '18 días', '45%', '15%', '$95'],
        'Meta 6M': ['35%', '55 puntos', '12 días', '60%', '25%', '$75'],
        'Meta 12M': ['45%', '65 puntos', '8 días', '75%', '35%', '$60']
    })
    
    st.dataframe(kpis_data, use_container_width=True)
    
    # Call to action final
    st.markdown("#### 🚀 ¡Es Hora de Decidir!")
    
    cta_col1, cta_col2 = st.columns([2, 1])
    
    with cta_col1:
        st.markdown("""
        **La pregunta no es SI debemos implementar segmentación inteligente.**
        **La pregunta es: ¿Podemos permitirnos NO hacerlo?**
        
        - Competidores avanzan hacia personalización masiva
        - Fintechs capturan clientes jóvenes cada día
        - Remesas crecen 8% anual sin nuestra participación óptima
        - ROI del 245% nos espera con datos que ya tenemos
        """)
        
        st.success("✅ **Recomendación:** Aprobar inversión de $670K para capturar oportunidad de $10M+ trimestrales")
    
    with cta_col2:
        st.markdown("""
        <div class="cta-button" style="text-align: center;">
            <h3>💰 Inversión Total</h3>
            <h2>$670,000</h2>
            <p>ROI: 245% en 12 meses</p>
            <p>Payback: 4.2 meses</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Próximos pasos inmediatos
    st.markdown("#### 📋 Próximos Pasos Inmediatos")
    
    if st.button("🎯 Aprobar Proyecto", type="primary"):
        st.balloons()
        st.success("¡Proyecto aprobado! Iniciando Fase 1 - Preparación")
        
        proximos_pasos = [
            "✅ Conformar equipo de proyecto (Semana 1)",
            "✅ Contratar consultor especializado (Semana 2)", 
            "✅ Definir arquitectura de datos (Semana 3)",
            "✅ Iniciar desarrollo de dashboard (Semana 4)",
            "✅ Primera reunión de seguimiento (Fin de mes)"
        ]
        
        for paso in proximos_pasos:
            st.write(paso)
    
    # Footer inspiracional
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; border-radius: 15px; margin: 20px 0;">
        <h3>"Los datos no mienten, las oportunidades no esperan"</h3>
        <p>Raíces Andinas tiene todo lo necesario para liderar la revolución financiera cooperativa en Ecuador.</p>
        <p><strong>El futuro es de quienes actúan hoy con la información correcta.</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Información de contacto del proyecto
    st.markdown("---")
    st.markdown("**Contacto del Proyecto:** [email] | **Fecha:** Julio 2025 | **Versión:** 2.0")
