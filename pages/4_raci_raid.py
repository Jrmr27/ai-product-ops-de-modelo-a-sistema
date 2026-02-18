pages/4_raci_raid.py
import streamlit as st

st.title("RACI / RAID")

st.subheader("RACI (editable)")
raci = st.session_state["raci"]
raci2 = st.data_editor(raci, num_rows="dynamic", use_container_width=True, hide_index=True)
st.session_state["raci"] = raci2

st.subheader("RAID (editable)")
raid = st.session_state["raid"]
raid2 = st.data_editor(raid, num_rows="dynamic", use_container_width=True, hide_index=True)
st.session_state["raid"] = raid2

st.info("Regla práctica: si no hay owners claros (A/R), el TO-BE no es operable.")
