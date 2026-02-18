import streamlit as st
from utils.state import init_state

st.set_page_config(page_title="DSI Process Redesign Studio", page_icon="🧩", layout="wide")
init_state()

pages = {
    "Rediseño": [
        st.Page("pages/1_home_contexto.py", title="Home · Contexto", icon="🏠"),
        st.Page("pages/2_sipoc.py", title="SIPOC", icon="🧾"),
        st.Page("pages/3_asis_tobe.py", title="AS-IS / TO-BE", icon="🧭"),
        st.Page("pages/4_raci_raid.py", title="RACI / RAID", icon="🧑‍🤝‍🧑"),
        st.Page("pages/5_exportar.py", title="Exportar", icon="⬇️"),
    ]
}

selected = st.navigation(pages, position="sidebar", expanded=True)
selected.run()
