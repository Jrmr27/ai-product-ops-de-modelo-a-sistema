import streamlit as st

st.title("Project Charter")
ch = st.session_state["charter"]

col1, col2 = st.columns(2)
with col1:
    ch["nombre"] = st.text_input("Nombre del proyecto", value=ch["nombre"])
    ch["problema"] = st.text_area("Problema", value=ch["problema"], height=90)
    ch["objetivo"] = st.text_area("Objetivo", value=ch["objetivo"], height=70)
    ch["kpis"] = st.text_area("KPIs (Outcome/Efficiency/Safety)", value=ch["kpis"], height=70)
with col2:
    ch["alcance"] = st.text_area("Alcance", value=ch["alcance"], height=70)
    ch["no_alcance"] = st.text_area("No-alcance", value=ch["no_alcance"], height=70)
    ch["restricciones"] = st.text_area("Restricciones (PII, auditoría, SLO...)", value=ch["restricciones"], height=110)

st.session_state["charter"] = ch

st.subheader("Stakeholders")
st.caption("Edita la tabla (Interés/Influencia y necesidades).")
df = st.session_state["stakeholders"]
st.session_state["stakeholders"] = st.data_editor(df, num_rows="dynamic", width="stretch", hide_index=True)
