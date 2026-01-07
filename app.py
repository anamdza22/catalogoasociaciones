import streamlit as st
import pandas as pd

# --------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# --------------------------------------------------
st.set_page_config(
    page_title="Catálogo de Asociaciones | Facultad de Psicología UADY",
    layout="wide"
)

# --------------------------------------------------
# ESTILOS (blanco, azul marino, amarillo mostaza)
# --------------------------------------------------
st.markdown("""
<style>
body {
    background-color: white;
}

.title {
    color: #0A2342;
    font-size: 38px;
    font-weight: bold;
}

.subtitle {
    color: #0A2342;
    font-size: 18px;
}

.card {
    border: 2px solid #0A2342;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 20px;
    background-color: white;
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
    font-size: 13px;
    margin-right: 5px;
    margin-top: 5px;
}

.button {
    background-color: #0A2342;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TÍTULO
# --------------------------------------------------
st.markdown('<div class="title">Catálogo de Asociaciones | Facultad de Psicología UADY</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Buscador de asociaciones para programas de voluntariado</div>', unsafe_allow_html=True)
st.markdown("---")

# --------------------------------------------------
# CARGA DE DATOS
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/catalogo_asociaciones.csv")

df = load_data()

# --------------------------------------------------
# BUSCADOR
# --------------------------------------------------
search = st.text_input("🔍 Buscar asociación por nombre, objetivo u ODS")

if search:
    df_filtered = df[
        df["nombre"].str.contains(search, case=False, na=False) |
        df["objetivo"].str.contains(search, case=False, na=False) |
        df["ods"].str.contains(search, case=False, na=False)
    ]
else:
    df_filtered = df

# --------------------------------------------------
# FICHAS DE ASOCIACIONES
# --------------------------------------------------
for idx, row in df_filtered.iterrows():

    with st.container():
        st.markdown(f"""
        <div class="card">
            <h3>{row['nombre']}</h3>
            <p><strong>Objetivo:</strong> {row['objetivo']}</p>
            <p><strong>Cupos de voluntariado:</strong> {row['cupos_voluntariado']}</p>
            <p><strong>ODS relacionadas:</strong></p>
        """, unsafe_allow_html=True)

        # ODS como badges
        ods_list = str(row["ods"]).split(",")
        for ods in ods_list:
            st.markdown(f"<span class='badge'>{ods.strip()}</span>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # --------------------------------------------------
        # DESPLEGABLE CON INFORMACIÓN COMPLETA
        # --------------------------------------------------
        with st.expander("Ver información completa"):
            st.markdown(f"""
            **Actividades posibles:**  
            {row['actividades']}

            **Persona supervisora:**  
            {row['persona_supervisora']}

            **Contacto:**  
            {row['contacto']}

            **Requisitos específicos:**  
            {row['requisitos']}

            **Detalles adicionales:**  
            {row['detalles']}
            """)

