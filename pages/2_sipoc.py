import streamlit as st

st.title("SIPOC")
st.write("Edita la tabla. Mantén 1–3 ítems por categoría para que sea defendible en clase.")

df = st.session_state["sipoc"]
edited = st.data_editor(df, num_rows="dynamic", use_container_width=True, hide_index=True)
st.session_state["sipoc"] = edited
