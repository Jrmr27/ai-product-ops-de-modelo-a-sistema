import streamlit as st
from utils.report import build_markdown, markdown_to_pdf_bytes

st.title("Exportar entregable")

md = build_markdown(st.session_state)
st.code(md, language="markdown")

c1, c2 = st.columns(2)
with c1:
    st.download_button(
        "⬇️ Descargar .md",
        data=md.encode("utf-8"),
        file_name="dsi_redisenio_reporte.md",
        mime="text/markdown",
        use_container_width=True,
    )

with c2:
    pdf = markdown_to_pdf_bytes(st.session_state)
    st.download_button(
        "⬇️ Descargar .pdf",
        data=pdf,
        file_name="dsi_redisenio_reporte.pdf",
        mime="application/pdf",
        use_container_width=True,
    )
