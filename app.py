import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.graph_objects as go

st.set_page_config(page_title="Pitch Empresarial - Raíces Andinas", layout="wide")

# ---------- SIDEBAR E ÍNDICE ----------
with st.sidebar:
    logo = Image.open("logo_raices.jpg")
    st.image(logo, use_container_width=True)
    selected = option_menu(
        menu_title="Menú Pitch Empresarial",
        options=[
            "Hook y Oportunidad",
            "Quiénes Somos",
            "Metodología Entretenida",
            "Resultados y Segmentos",
            "Simulación y Estrategias",
            "Conclusiones y Acción"
        ],
        icons=[
            "lightning", "bank", "magic", "bar-chart", "bezier2", "flag"
        ],
        menu_icon="cast",
        default_index=0,
    )

# ---------- DATOS DE DEMO PARA VISUALIZACIÓN ----------
# Puedes reemplazar con tus datos reales en cada sección
df = pd.DataFrame({
    "cluster": [0, 1, 2, 0, 1, 2],
    "año": [2020, 2020, 2020, 2021, 2021, 2021],
    "clientes": [1500, 4000, 1800, 1600, 4200, 1700],
    "monto_promedio": [3000, 5200, 4100, 3200, 5300, 4000]
})

# KPIs para radar chart
categorias = ["Edad", "Ingresos", "Saldo DPF", "Capital Prestado", "Mora"]
cluster0 = [45.1, 3558.96, 27597.17, 21576.06, 1.5]
cluster1 = [38.4, 3759.42, 315.78, 21282.22, 18]
cluster2 = [39.6, 3962.25, 7656.16, 27802.60, 10.2]

# ---------- SECCIONES DEL PITCH INTERACTIVO ----------

if selected == "Hook y Oportunidad":
    st.title("🚀 Migrantes: El mayor activo financiero de Ecuador (¡y tu cooperativa!)")
    
    st.markdown("""
    > **“Ecuador recibió un récord de USD 5,491 millones en remesas en 2024, más que toda la Inversión Extranjera Directa y que el camarón, el banano o el plátano.”**
    >
    > **En 2025, las remesas crecerán aún más: ¡USD 5.821 millones proyectados!**
    """)

    st.markdown("""
    - 🏦 **El 68%** de las remesas viene de EE.UU. y el **15%** llega solo a la provincia del Azuay.
    - 🧑‍💼 **Edad promedio de migrantes:** 32,9 años. **Edad promedio socios Raíces Andinas:** 39 años.
    - 📈 **Más de 21% de los hogares que reciben remesas las invierten en vivienda o terreno.**
    - 💡 **El 74%** de adultos ecuatorianos ya tiene cuenta bancaria, pero solo la mitad usa pagos digitales: *¡el futuro está en conquistar ese nuevo segmento digital!*
    """)
    
    st.info("Si captamos solo el 5% de las remesas de Azuay, ingresarían más de **USD 10 millones trimestrales** a nuestra cooperativa (solo por migrantes). ¿Vamos a dejarlo pasar?")
    
    st.success("Las remesas no son solo dinero: son sueños, familia, futuro y una gigantesca OPORTUNIDAD de negocio social y rentable. Raíces Andinas tiene el potencial y la confianza para ser el puente financiero entre el migrante y el Ecuador.")
    
    st.image("logo_raices.jpg", width=200)
    
    st.caption("""
    Fuentes: Banco Central del Ecuador, Pew Research Center, Migration Policy Institute, “Datos del Migrante” (2025).
    """)

elif selected == "Quiénes Somos":
    st.header("🏦 Raíces Andinas: Innovación con historia y visión de futuro")
    st.markdown("""
    - **Años en el mercado:** 28  
    - **Socios activos:** 48,000  
    - **Presencia:** 7 provincias, +30 agencias  
    - **Productos:** Créditos, ahorros, inversión, servicios digitales, atención a migrantes
    """)
    st.subheader("🔍 Diagnóstico Estratégico")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **FODA**
        - Fortaleza: Capital sólido, base migrante fiel, tecnología en expansión
        - Oportunidad: Remesas en crecimiento, alianzas globales
        - Debilidad: Bajo uso de canales digitales
        - Amenaza: Fintech, competencia bancaria agresiva
        """)
    with col2:
        st.markdown("""
        **PESTEL**
        - Político: Incentivos migratorios
        - Económico: Fluctuación de remesas
        - Social: Envejecimiento base migrante
        - Tecnológico: Demanda de apps y pagos digitales
        - Legal: Normativas de inclusión financiera
        """)

elif selected == "Metodología Entretenida":
    st.header("🤹 El reto: segmentar para personalizar y crecer")
    st.markdown("""
    Imagina una gran feria, con cientos de socios, cada uno con historias, necesidades y potencial distinto.  
    ¿Cómo encontrar a los socios estrella y a los que necesitan una mano?
    
    - **La clave:** El análisis de clústeres, usando K-Means, crea "equipos" de clientes similares.
    - **¿Por qué K-Means?** Nos permite ver patrones ocultos, detectar riesgos y descubrir oportunidades.
    - **Componentes Principales:** Es como reducir una foto a sus colores esenciales: nos quedamos solo con lo importante para segmentar de verdad.
    """)
    st.info("Un clúster es como un equipo de fútbol: cada uno con su estrategia para ganar el campeonato financiero.")
    st.image("https://cdn.pixabay.com/photo/2017/01/10/19/05/analytics-1971678_1280.png", width=350)
    st.subheader("🔍 ¿Quieres ver los resultados de este 'scouting'? Adelante...")

elif selected == "Resultados y Segmentos":
    st.header("🎯 Perfiles de socios: ¡el mapa de oportunidades!")
    st.markdown("Los datos revelan tres grandes segmentos dentro de la cooperativa:")
    perfiles = [
        {"nombre": "Tradicional 🧓", "color": "#8dd3c7", "desc": "Maduro, ahorrador, poco digital, muy rentable", "oportunidad": "Venta cruzada digital", "riesgo": "Deserción por falta de innovación"},
        {"nombre": "Riesgo ⚠️", "color": "#ffffb3", "desc": "Masivo, alta mora, poco saldo, riesgo alto", "oportunidad": "Prevención proactiva", "riesgo": "Morosidad y provisiones altas"},
        {"nombre": "Tech 📱", "color": "#bebada", "desc": "Joven, usa apps, multiproducto, muy rentable", "oportunidad": "Membresía digital", "riesgo": "Competencia fintech"}
    ]
    cols = st.columns(3)
    for i, seg in enumerate(perfiles):
        with cols[i]:
            st.markdown(f"<div style='background-color:{seg['color']};border-radius:10px;padding:18px'>"
                        f"<h3>{seg['nombre']}</h3>"
                        f"<b>Perfil:</b> {seg['desc']}<br>"
                        f"<b>Oportunidad:</b> {seg['oportunidad']}<br>"
                        f"<b>Riesgo:</b> {seg['riesgo']}</div>", unsafe_allow_html=True)
    st.subheader("📊 Radar de KPIs por segmento")
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=cluster0, theta=categorias, fill='toself', name='Tradicional'))
    fig.add_trace(go.Scatterpolar(r=cluster1, theta=categorias, fill='toself', name='Riesgo'))
    fig.add_trace(go.Scatterpolar(r=cluster2, theta=categorias, fill='toself', name='Tech'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=True)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Fuente: Jardín Azuayo Tipología, pág. 22-23.")

elif selected == "Simulación y Estrategias":
    st.header("🧪 Simulador y Estrategias: ¿Qué pasa si…?")
    st.markdown("""
    **Estrategias recomendadas:**  
    - **Tradicional:** Programa de fidelización, digitalización asistida
    - **Riesgo:** Llamadas proactivas, alertas de pago, educación financiera
    - **Tech:** Membresía premium, apps exclusivas, concursos digitales
    """)
    st.success("¡Simula el impacto de las estrategias!")
    impacto = st.slider("¿Qué porcentaje del cluster 'Riesgo' migramos a 'Tradicional' con llamadas preventivas?", 0, 100, 30)
    mora_base = 18
    mora_impacto = mora_base - impacto*0.08
    st.info(f"Reducirías la mora global de {mora_base} a {mora_impacto:.1f} días (escenario simulado)")
    st.caption("Fuente: Jardín Azuayo Tipología, pág. 27-28.")

elif selected == "Conclusiones y Acción":
    st.header("🏁 El futuro de Raíces Andinas: ¡es ahora!")
    st.markdown("""
    - Personalizar servicios según segmentos aumenta retención y reduce riesgos.
    - La segmentación permite lanzar productos a medida y anticipar movimientos de la competencia.
    - Siguiente paso: conformar equipo para pilotar estrategias en los próximos 6 meses.
    """)
    st.balloons()
    st.info("¿Listos para transformar la cooperativa? El futuro migrante ya llegó. ¡Actuemos juntos!")
    st.caption("Presentación basada en el informe 'Jardín Azuayo Tipología', 2024.")

