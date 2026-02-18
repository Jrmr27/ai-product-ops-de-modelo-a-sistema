import streamlit as st
from utils.dot import arch_to_dot

st.title("Arquitectura (Componentes + Flujos)")

st.subheader("Componentes")
c = st.session_state["components"]
c2 = st.data_editor(c, num_rows="dynamic", width="stretch", hide_index=True)
st.session_state["components"] = c2

st.subheader("Flujos")
f = st.session_state["flows"]
f2 = st.data_editor(f, num_rows="dynamic", width="stretch", hide_index=True)
st.session_state["flows"] = f2

st.subheader("Diagrama (auto)")
dot = arch_to_dot(c2, f2)
st.graphviz_chart(dot, width="stretch")

