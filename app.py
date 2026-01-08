import streamlit as st
import pandas as pd

# ---------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------
st.set_page_config(
    page_title="Catálogo de Asociaciones | Facultad de Psicología UADY",
    layout="wide"
)

# ---------------------------
# ESTILOS (CSS)
# ---------------------------
st.markdown("""
<style>
body {
    background-color: #FFFFFF;
}
.card {
    background-color: #FFFFFF;
    border: 2px solid #0A2342;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
}
.card h3 {
    color: #0A2342;
}
.badge {
    display: inline-block;
    background-color: #F2B705;
    color: #0A2342;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 12px;
    margin-right: 5px;
}
.label {
    font-weight: bold;
    color: #0A2342;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# TÍTULO
# ---------------------------
st.markdown(
    "<h1 style='color:#0A2342;'>Catálogo de Asociaciones | Facultad de Psicología UADY</h1>",
    unsafe_allow_html=True
)

st.write("Buscador de asociaciones vinculadas al programa de voluntariado.")

# ---------------------------
# CARGA DE DATOS DESDE GITHUB
# ---------------------------
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/TU_USUARIO/TU_REPOSITORIO/main/catalogo_asociaciones.csv"
    return pd.read_csv(url)

df = load_data()

# ---------------------------
# BUSCADOR
# ---------------------------
search = st.text_input("🔍 Buscar asociación por nombre")

if search:
    df = df[df["nombre"].str.contains(search, case=False, na=False)]

# ---------------------------
# MOSTRAR ASOCIACIONES EN FICHAS
# ---------------------------
for idx, row in df.iterrows():

    with st.container():
        st.markdown(f"""
        <div class="card">
            <h3>{row['nombre']}</h3>
            <p><span class="label">Objetivo:</span> {row['objetivo']}</p>
            <p><span class="label">ODS relacionadas:</span></p>
            <p>
                {"".join([f"<span class='badge'>{ods.strip()}</span>" for ods in str(row['ods']).split(",")])}
            </p>
            <p><span class="label">Cupos de voluntariado:</span> {row['cupos_voluntariado']}</p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("📌 Ver información completa"):
            st.markdown(f"""
            **Actividades posibles:**  
            {row['actividades']}

            **Persona supervisora:**  
            {row['persona_supervisora']}

            **Contacto:**  
            {row['contacto']}

            **Requisitos específicos:**  
            {row['requ]()

