import streamlit as st
import pandas as pd

# ===========================
# CONFIGURACIÓN GENERAL
# ===========================
st.set_page_config(
    page_title="Catálogo de Asociaciones | Facultad de Psicología UADY",
    layout="wide"
)

# ===========================
# ESTILOS
# ===========================
st.markdown("""
<style>
body {
    background-color: #FFFFFF;
}
.card {
    background-color: #FFFFFF;
    border: 2px solid #0A2342;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 20px;
}
.card h3 {
    color: #0A2342;
    margin-bottom: 10px;
}
.label {
    font-weight: 600;
    color: #0A2342;
}
.badge {
    display: inline-block;
    background-color: #F2B705;
    color: #0A2342;
    padding: 4px 12px;
    border-radius: 18px;
    font-size: 12px;
    margin: 3px 6px 3px 0;
}
</style>
""", unsafe_allow_html=True)

# ===========================
# TÍTULO
# ===========================
st.markdown(
    "<h1 style='color:#0A2342;'>Catálogo de Asociaciones | Facultad de Psicología UADY</h1>",
    unsafe_allow_html=True
)
st.write("Buscador de asociaciones vinculadas al programa de voluntariado.")

# ===========================
# CARGA DE DATOS
# ===========================
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/anamdza22/catalogoasociaciones/main/catalogo_asociaciones.csv"
    df = pd.read_csv(url, encoding="utf-8")
    df.columns = df.columns.str.strip()  # Limpieza clave
    return df

df = load_data()

# ===========================
# BUSCADOR
# ===========================
search = st.text_input("🔍 Buscar asociación por nombre")

if search:
    df = df[df["Nombre de la asociación"].str.contains(search, case=False, na=False)]

# ===========================
# MOSTRAR FICHAS
# ===========================
for _, row in df.iterrows():

    ods_lista = str(row["ODS relacionadas"]).split(",")

    st.markdown(f"""
    <div class="card">
        <h3>{row["Nombre de la asociación"]}</h3>

        <p><span class="label">Objetivo:</span><br>
        {row["Objetivo"]}</p>

        <p><span class="label">ODS relacionadas:</span></p>
        <p>
            {"".join([f"<span class='badge'>{ods.strip()}</span>" for ods in ods_lista])}
        </p>

        <p><span class="label">Cupos de voluntariado:</span> {row["Cupo para voluntariado"]}</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📌 Ver información completa"):
        st.markdown(f"""
        **Actividades posibles:**  
        {row["Actividades posibles"]}

        **Persona supervisora:**  
        {row["Persona supervisora"]}

        **Contacto:**  
        {row["Contacto"]}

        **Días y horarios disponibles:**  
        {row["Días y horarios disponibles"]}

        **Requerimientos específicos:**  
        {row["Requerimientos específicos"]}

        **Detalles adicionales:**  
        {row["Detalles"]}
        """)

