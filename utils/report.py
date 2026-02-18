import io
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import cm

def _df_to_table(df):
    data = [list(df.columns)] + df.astype(str).values.tolist()
    t = Table(data, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("FONTSIZE", (0,0), (-1,-1), 8),
    ]))
    return t

def build_markdown(ss) -> str:
    ctx = ss["contexto"]
    md = []
    md.append(f"# DSI Process Redesign Studio — Reporte\n")
    md.append(f"- Fecha: **{date.today().isoformat()}**\n")
    md.append("## 1. Contexto\n")
    md.append(f"- Proceso: **{ctx['proceso']}**\n")
    md.append(f"- Objetivo: {ctx['objetivo']}\n")
    md.append(f"- Alcance: {ctx['alcance']}\n")
    md.append(f"- Volumen/mes: {ctx['volumen_mes']}\n")
    md.append(f"- Restricciones: {ctx['restricciones']}\n")

    md.append("\n## 2. SIPOC\n")
    md.append(ss["sipoc"].to_markdown(index=False))

    md.append("\n\n## 3. AS-IS (pasos)\n")
    md.append(ss["steps"][["#", "Actor", "Actividad", "Sistema", "Dolor_ASIS"]].to_markdown(index=False))

    md.append("\n\n## 4. TO-BE (mejoras + SI/IA)\n")
    md.append(ss["steps"][["#", "Actor", "Actividad", "Mejora_TOBE", "Palanca_IA"]].to_markdown(index=False))

    md.append("\n\n## 5. RACI\n")
    md.append(ss["raci"].to_markdown(index=False))

    md.append("\n\n## 6. RAID\n")
    md.append(ss["raid"].to_markdown(index=False))

    md.append("\n\n## 7. RAGA (lite)\n")
    md.append("- Riesgos: PII, alucinación, latencia, dependencia ITSM.\n")
    md.append("- Alternativas: (A) más HITL vs (B) más automatización con guardrails.\n")
    md.append("- Gobernanza: owners definidos (Service Owner/SRE/Data Steward/Legal).\n")
    md.append("- Acción: piloto controlado + métricas (valor/coste/riesgo).\n")

    return "\n".join(md)

def markdown_to_pdf_bytes(ss) -> bytes:
    styles = getSampleStyleSheet()
    buf = io.BytesIO()
    doc = SimpleDocTemplate(
        buf, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm
    )
    story = []

    ctx = ss["contexto"]
    story.append(Paragraph("DSI Process Redesign Studio — Reporte", styles["Title"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(f"Proceso: <b>{ctx['proceso']}</b>", styles["BodyText"]))
    story.append(Paragraph(f"Objetivo: {ctx['objetivo']}", styles["BodyText"]))
    story.append(Paragraph(f"Volumen/mes: {ctx['volumen_mes']}", styles["BodyText"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("SIPOC", styles["Heading2"]))
    story.append(_df_to_table(ss["sipoc"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("AS-IS", styles["Heading2"]))
    story.append(_df_to_table(ss["steps"][["#", "Actor", "Actividad", "Sistema", "Dolor_ASIS"]]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("TO-BE + SI/IA", styles["Heading2"]))
    story.append(_df_to_table(ss["steps"][["#", "Actor", "Actividad", "Mejora_TOBE", "Palanca_IA"]]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("RACI", styles["Heading2"]))
    story.append(_df_to_table(ss["raci"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("RAID", styles["Heading2"]))
    story.append(_df_to_table(ss["raid"]))

    doc.build(story)
    return buf.getvalue()
utils/__init__.py
# utils package
