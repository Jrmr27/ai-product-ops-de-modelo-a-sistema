import streamlit as st

st.title("DSI Process Redesign Studio")
st.caption("Construye SIPOC + AS-IS/TO-BE + RACI/RAID + reporte exportable.")

ctx = st.session_state["contexto"]

col1, col2 = st.columns(2)
with col1:
    ctx["proceso"] = st.text_input("Nombre del proceso", value=ctx["proceso"])
    ctx["objetivo"] = st.text_area("Objetivo (1–2 líneas)", value=ctx["objetivo"], height=80)
    ctx["alcance"] = st.text_input("Alcance", value=ctx["alcance"])
with col2:
    ctx["volumen_mes"] = st.number_input("Volumen mensual (aprox.)", min_value=1, value=int(ctx["volumen_mes"]), step=100)
    ctx["restricciones"] = st.text_area("Restricciones (PII, auditoría, latencia, etc.)", value=ctx["restricciones"], height=120)

st.session_state["contexto"] = ctx

st.info("Siguiente paso: completa SIPOC → luego mapa AS-IS/TO-BE → luego RACI/RAID → exporta.")
