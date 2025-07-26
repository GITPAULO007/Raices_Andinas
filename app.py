import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

st.set_page_config(page_title="Tipología de Clientes - Raíces Andinas", layout="wide")

st.title("📊 Tipología de Clientes de la Cooperativa Raíces Andinas")
st.markdown("Visualización y segmentación de clientes migrantes entre 2020 y 2025.")

# Carga de datos (simulada, cámbiala por la real si hace falta)
df = pd.DataFrame({
    "cluster": [0, 1, 2],
    "año": [2020, 2020, 2020],
    "clientes": [1500, 4000, 1800]
})

profile = df.groupby("cluster").mean()

# 1. Mostrar Dataframe
st.subheader("🔍 Vista previa de la base")
st.dataframe(df.head(10))

# 2. Gráfico de clusters por año
st.subheader("📈 Distribución de Clusters")
fig, ax = plt.subplots()
sns.countplot(x=df["cluster"], palette="Set2", ax=ax)
st.pyplot(fig)

# 3. Mostrar perfil promedio
st.subheader("🧬 Perfiles Promedio de Cada Cluster")
st.dataframe(profile.T.style.format("{:.2f}"))
