import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title="Tipología de Clientes - Raíces Andinas", layout="wide")

with st.sidebar:
    # Mostrar el logo arriba del menú
    logo = Image.open("logo_raices.jpg")
    st.image(logo, use_column_width=True)
    selected = option_menu(
        menu_title="Menú Principal",
        options=["Inicio", "Base de Datos", "Clusters", "Perfiles", "Transiciones", "Conclusiones"],
        icons=["house", "table", "diagram-3", "person-lines-fill", "shuffle", "check-circle"],
        menu_icon="cast",
        default_index=0,
    )


df = pd.DataFrame({
    "cluster": [0, 1, 2, 0, 1, 2],
    "año": [2020, 2020, 2020, 2021, 2021, 2021],
    "clientes": [1500, 4000, 1800, 1600, 4200, 1700],
    "monto_promedio": [3000, 5200, 4100, 3200, 5300, 4000]
})

if selected == "Inicio":
    st.title("📊 Tipología de Clientes de la Cooperativa Raíces Andinas")
    st.markdown("""
    Este proyecto analiza los perfiles de socios migrantes de la Cooperativa Raíces Andinas entre 2020 y 2025,
    utilizando técnicas de análisis de clúster para identificar segmentos estratégicos en colocación, captación
    y fidelización de servicios financieros.
    """)
    st.info("Fuente: Informe 'JARDÍN AZUAYO TIPOLOGÍA' 📄")

elif selected == "Base de Datos":
    st.header("🔍 Vista previa de la base de datos")
    st.dataframe(df)

elif selected == "Clusters":
    st.header("📈 Distribución de Clusters por Año")
    fig = px.bar(df, x="año", y="clientes", color="cluster", barmode="group",
                 title="Clientes por Cluster y Año")
    st.plotly_chart(fig, use_container_width=True)

elif selected == "Perfiles":
    st.header("🧬 Perfil Financiero Promedio por Cluster")
    perfil = df.groupby("cluster").mean(numeric_only=True).reset_index()
    fig = px.bar(perfil, x="cluster", y="monto_promedio", color="cluster",
                 title="Monto Promedio por Cluster", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(perfil)

elif selected == "Transiciones":
    st.header("🔀 Análisis de Transiciones entre Clusters")
    st.markdown("Próximamente: Diagrama de Sankey para visualizar movimientos entre clusters año a año.")

elif selected == "Conclusiones":
    st.header("✅ Conclusiones y Recomendaciones")
    st.markdown("""
    - El cluster 1 representa el grupo más numeroso y con mayores montos promedio.
    - El cluster 2 muestra potencial de captación, pero menor estabilidad.
    - El análisis ayuda a diseñar productos financieros diferenciados por segmento.
    """)
    st.success("Se recomienda utilizar estos hallazgos para fortalecer la fidelización de socios migrantes.")
