# ══════════════════════════════════════════════════════════════
# Mi App · Streamlit
# Ficha 3387591 · SENA CTM Itagüí · 2026
# Completá cada sección con los datos de tu proyecto
# ══════════════════════════════════════════════════════════════

import streamlit as st
import pandas as pd

# ══════════════════════════════════════════════════════════════
# CONFIGURACIÓN
# ══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="SPA N&M",
    page_icon="💆‍♀️",
    layout="wide"
)

# ══════════════════════════════════════════════════════════════
# DATOS
# ══════════════════════════════════════════════════════════════
datos = [
    {
        "Cliente": "María",
        "Servicio": "Masaje relajante",
        "Precio": 80000,
        "Estado": "Finalizado"
    },
    {
        "Cliente": "Laura",
        "Servicio": "Limpieza facial",
        "Precio": 60000,
        "Estado": "Pendiente"
    },
    {
        "Cliente": "Camila",
        "Servicio": "Manicure",
        "Precio": 35000,
        "Estado": "Finalizado"
    },
    {
        "Cliente": "Sofía",
        "Servicio": "Pedicure",
        "Precio": 40000,
        "Estado": "Pendiente"
    },
    {
        "Cliente": "Valentina",
        "Servicio": "Masaje relajante",
        "Precio": 80000,
        "Estado": "Finalizado"
    }
]

df = pd.DataFrame(datos)

# ══════════════════════════════════════════════════════════════
# SIDEBAR — FILTROS
# ══════════════════════════════════════════════════════════════
st.sidebar.title("Filtros")

servicio = st.sidebar.selectbox(
    "Selecciona un servicio",
    ["Todos"] + list(df["Servicio"].unique())
)

if servicio != "Todos":
    df_filtrado = df[df["Servicio"] == servicio]
else:
    df_filtrado = df

# ══════════════════════════════════════════════════════════════
# TÍTULO
# ══════════════════════════════════════════════════════════════
st.title("💆‍♀️ Sistema de Gestión SPA N&M")
st.write(
    "Aplicación para administrar servicios, clientes y citas del SPA N&M."
)

# ══════════════════════════════════════════════════════════════
# MÉTRICAS
# ══════════════════════════════════════════════════════════════
st.subheader("📊 Métricas Generales")

col1, col2, col3 = st.columns(3)

total_clientes = len(df_filtrado)
ingresos_totales = df_filtrado["Precio"].sum()
servicios_finalizados = (
    df_filtrado["Estado"] == "Finalizado"
).sum()

col1.metric("Total Clientes", total_clientes)
col2.metric("Ingresos Totales", f"${ingresos_totales:,}")
col3.metric("Servicios Finalizados", servicios_finalizados)

# ══════════════════════════════════════════════════════════════
# TABLA
# ══════════════════════════════════════════════════════════════
st.subheader("📋 Registros")

st.dataframe(
    df_filtrado,
    use_container_width=True
)

# ══════════════════════════════════════════════════════════════
# GRÁFICA
# ══════════════════════════════════════════════════════════════
st.subheader("📈 Servicios Más Solicitados")

servicios = df_filtrado["Servicio"].value_counts()

st.bar_chart(servicios)

# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════
st.divider()
st.caption("Proyecto SPA N&M · SENA CTM Itagüí · 2026")