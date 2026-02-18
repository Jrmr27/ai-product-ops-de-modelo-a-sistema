import streamlit as st
import pandas as pd

st.title("Backlog (Epics → User Stories → AC)")
st.caption("Usa Priority (Must/Should/Could/Won't), Estimate (puntos), Value y Risk.")

df = st.session_state["backlog"]
edited = st.data_editor(df, num_rows="dynamic", width="stretch", hide_index=True)
edited["Estimate"] = pd.to_numeric(edited.get("Estimate", 1), errors="coerce").fillna(1).clip(lower=1).astype(int)
edited["Value"] = pd.to_numeric(edited.get("Value", 1), errors="coerce").fillna(1).clip(lower=1).astype(int)
edited["Risk"] = pd.to_numeric(edited.get("Risk", 1), errors="coerce").fillna(1).clip(lower=1).astype(int)

# Prioridad simple: score = Value / Estimate (con ajuste por Risk)
edited["Score"] = (edited["Value"] + (edited["Risk"] * 0.3)) / edited["Estimate"]
st.session_state["backlog"] = edited

st.subheader("Ranking sugerido (Score)")
rank = edited.sort_values("Score", ascending=False)[["Epic","User Story","Priority","Estimate","Value","Risk","Score"]]
st.dataframe(rank, width="stretch")

