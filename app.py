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
""")

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
            "🎯 Perfiles",
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
    # Tu código existente para Hook y Oportunidad...
    st.markdown('<h1 class="main-header">🚀 EL BOOM FINANCIERO QUE ECUADOR ESTÁ IGNORANDO</h1>', unsafe_allow_html=True)
    st.write("Contenido de Hook y Oportunidad...")

elif "🏦 Quiénes Somos" in selected:
    # Tu código existente para Quiénes Somos...
    st.markdown('<h1 class="main-header">🏦 COAC Raíces Andinas</h1>', unsafe_allow_html=True)
    st.write("Contenido de Quiénes Somos...")

elif "🔬 Metodología" in selected:
    # Tu código existente para Metodología...
    st.markdown('<h1 class="main-header">🔬 Metodología de Investigación</h1>', unsafe_allow_html=True)
    st.write("Contenido de Metodología...")

elif "🎯 Perfiles" in selected:
    # Tu código existente para Segmentos y KPIs...
    st.markdown('<h1 class="main-header">🎯 Segmentación de Socios Migrantes</h1>', unsafe_allow_html=True)
    st.write("Contenido de Segmentos y KPIs...")

elif "🧪 Simulador Estratégico" in selected:
    # Tu código existente para Simulador Estratégico...
    st.markdown('<h1 class="main-header">🧪 Laboratorio de Estrategias</h1>', unsafe_allow_html=True)
    st.write("Contenido de Simulador Estratégico...")

elif "🏁 Plan de Acción" in selected or selected == "🏁 Plan de Acción":
    st.markdown('<h1 class="main-header">🏁 Conclusiones y Recomendaciones Estratégicas</h1>', unsafe_allow_html=True)
    
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
    tabs = st.tabs(["🎯 Conclusiones Clave", "💡 Recomendaciones Estratégicas", "📊 Hallazgos por Perfil", "🚀 Roadmap de Implementación"])
    
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
        
        # Additional recommendations sections...
        st.markdown("### 💰 2. Análisis de Rentabilidad por Clúster")
        st.error("""
        **⚠️ CRÍTICO: Comprender el costo real de cada segmento**
        
        En un entorno competitivo, no conocer la rentabilidad real por socio puede dejar a la institución en desventaja 
        frente a competidores más ágiles que aprovechan la analítica avanzada.
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("ROI Tradicionales", "3.2x", "Alto valor en DPF")
        with col2:
            st.metric("ROI Riesgo Financiero", "-0.8x", "Pérdida operativa")
        with col3:
            st.metric("ROI Tecnológico", "2.1x", "Alto potencial")
    
    with tabs[2]:
        st.markdown("## 📊 Resumen de Hallazgos por Perfil")
        
        # Tabla comparativa detallada
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
    
    with tabs[3]:
        st.markdown("## 🚀 Roadmap de Implementación")
        
        # Timeline interactivo
        timeline_data = pd.DataFrame({
            'Fase': ['Fase 1: Quick Wins', 'Fase 2: Gestión de Riesgo', 'Fase 3: Transformación Digital', 'Fase 4: Optimización'],
            'Inicio': ['2025-Q1', '2025-Q2', '2025-Q3', '2026-Q1'],
            'Duración': [3, 6, 9, 12],
            'Prioridad': ['Alta', 'Crítica', 'Alta', 'Media']
        })
        
        st.markdown("### 📅 Cronograma de Implementación")
        
        # Gantt Chart simulado
        fig_gantt = go.Figure()
        
        colors = {'Alta': '#FFA726', 'Crítica': '#EF5350', 'Media': '#66BB6A'}
        
        for idx, row in timeline_data.iterrows():
            fig_gantt.add_trace(go.Bar(
                name=row['Fase'],
                x=[row['Duración']],
                y=[row['Fase']],
                orientation='h',
                marker=dict(color=colors[row['Prioridad']]),
                showlegend=False,
                hovertemplate='<b>%{y}</b><br>Duración: %{x} meses<br>Inicio: ' + row['Inicio'] + '<extra></extra>'
            ))
        
        fig_gantt.update_layout(
            title="Roadmap de Implementación Estratégica",
            xaxis_title="Meses",
            barmode='overlay',
            height=400,
            xaxis=dict(range=[0, 12])
        )
        
        st.plotly_chart(fig_gantt, use_container_width=True)
        
        # Próximos pasos
        st.markdown("### 🎯 Próximos Pasos Inmediatos")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("""
            **Semana 1-2:**
            - Validar hallazgos con gerencia
            - Formar comité de implementación
            - Definir presupuesto inicial
            """)
        with col2:
            st.info("""
            **Semana 3-4:**
            - Seleccionar pilotos por clúster
            - Diseñar protocolos de atención
            - Capacitar personal clave
            """)
        with col3:
            st.warning("""
            **Mes 2:**
            - Lanzar piloto con 100 socios
            - Monitorear KPIs diariamente
            - Ajustar estrategias según resultados
            """)
        
        # Mensaje final con recomendaciones
        st.markdown("---")
        st.markdown("""
        <div style='background-color: #e3f2fd; padding: 20px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #1976d2;'>💡 Mensaje Clave</h3>
            <p style='font-size: 18px; color: #424242;'>
                <strong>La implementación de estas recomendaciones permitirá a la cooperativa no solo 
                entender mejor a sus socios migrantes, sino construir un ecosistema de datos que 
                potencie la toma de decisiones estratégicas y fortalezca su posición competitiva 
                en el mercado.</strong>
            </p>
        </div>
        """)
        
        # Recomendaciones finales detalladas
        st.markdown("---")
        st.markdown("## 🎯 Recomendaciones Estratégicas Finales")
        
        final_rec_tabs = st.tabs(["📊 Gestión de Datos", "💰 Análisis Financiero", "🔄 Mejora Continua", "🚀 Implementación"])
        
        with final_rec_tabs[0]:
            st.info("""
            **📊 Recomendaciones para Gestión de Datos**
            
            **Acciones Prioritarias:**
            - ✅ Actualización periódica de información de socios migrantes
            - ✅ Enriquecimiento de variables demográficas y financieras
            - ✅ Implementación de monitoreo en tiempo real
            - ✅ Creación de dashboards ejecutivos automatizados
            
            **Beneficios Esperados:**
            - Mayor precisión en la segmentación
            - Identificación temprana de cambios de perfil
            - Mejora en la toma de decisiones basada en datos
            """)
        
        with final_rec_tabs[1]:
            st.warning("""
            **💰 Recomendaciones para Análisis Financiero**
            
            **Evaluaciones Necesarias:**
            - 🔍 Cálculo del costo real por clúster
            - 📈 Medición de rentabilidad por perfil de socio
            - ⚖️ Optimización de asignación de recursos
            - 💡 Desarrollo de productos específicos por segmento
            
            **Métricas Clave a Implementar:**
            - ROI por segmento de socios
            - Costo de adquisición por perfil
            - Valor de vida del cliente (LTV)
            - Margen de contribución por clúster
            """)
        
        with final_rec_tabs[2]:
            st.success("""
            **🔄 Recomendaciones para Mejora Continua**
            
            **Proceso de Validación:**
            - 📅 Validación trimestral de estrategias implementadas
            - 📊 Ajuste de tácticas según resultados obtenidos
            - 🚀 Escalamiento de iniciativas exitosas
            - 🔄 Refinamiento continuo del modelo de segmentación
            
            **Ciclo de Mejora:**
            1. Implementar → 2. Medir → 3. Analizar → 4. Ajustar → 5. Repetir
            """)
        
        with final_rec_tabs[3]:
            st.error("""
            **🚀 Recomendaciones para Implementación**
            
            **Fases de Implementación:**
            
            **Fase 1 (Inmediata - 1 mes):**
            - Formar equipo multidisciplinario
            - Definir KPIs y métricas de seguimiento
            - Capacitar personal clave en nuevas estrategias
            
            **Fase 2 (Corto plazo - 3 meses):**
            - Implementar pilotos por cada clúster
            - Monitorear resultados diariamente
            - Ajustar estrategias según feedback
            
            **Fase 3 (Mediano plazo - 6 meses):**
            - Escalar estrategias exitosas
            - Automatizar procesos validados
            - Medir impacto en la rentabilidad
            
            **Fase 4 (Largo plazo - 12 meses):**
            - Consolidar el modelo de segmentación
            - Expandir a otros mercados
            - Desarrollar capacidades predictivas
            """) su posición competitiva 
                en el mercado.</strong>
            </p>
        </div>
        """(

# Debug: Mostrar qué opción está seleccionada (solo para desarrollo)
# st.sidebar.write(f"**Selección actual:** {selected}")
