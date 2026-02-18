import streamlit as st
from utils.dot import steps_to_dot

st.title("AS-IS / TO-BE")
mode = st.radio("Vista", ["ASIS", "TOBE"], horizontal=True)

df = st.session_state["steps"]
edited = st.data_editor(df, num_rows="dynamic", use_container_width=True, hide_index=True)
st.session_state["steps"] = edited

st.subheader("Diagrama del proceso (auto)")
dot = steps_to_dot(edited, mode=mode)
st.graphviz_chart(dot, use_container_width=True)  # DOT string aceptado :contentReference[oaicite:4]{index=4}

if mode == "ASIS":
    st.warning("Asegúrate de explicitar dolores (retrabajo, esperas, errores, PII, falta de trazabilidad).")
else:
    st.success("Asegúrate de que cada mejora tenga palanca SI/IA y un control (auditoría/HITL/PII).")
