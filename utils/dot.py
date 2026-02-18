def steps_to_dot(df, mode="ASIS") -> str:
    """
    Genera un DOT sencillo para st.graphviz_chart (acepta string DOT). :contentReference[oaicite:2]{index=2}
    mode: ASIS o TOBE (solo cambia el texto mostrado)
    """
    lines = ["digraph G {", "rankdir=LR;", 'node [shape=box, style="rounded"];']
    prev = None

    for _, row in df.sort_values("#").iterrows():
        idx = int(row["#"])
        actor = str(row.get("Actor", "")).strip()
        act = str(row.get("Actividad", "")).strip()

        extra = ""
        if mode == "ASIS":
            extra = str(row.get("Dolor_ASIS", "")).strip()
            label = f"{idx}. {actor}: {act}\\nDolor: {extra}"
        else:
            extra = str(row.get("Mejora_TOBE", "")).strip()
            ia = str(row.get("Palanca_IA", "")).strip()
            label = f"{idx}. {actor}: {act}\\nMejora: {extra}\\nIA: {ia}"

        node = f"n{idx}"
        safe_label = label.replace('"', "'")
        lines.append(f'{node} [label="{safe_label}"];')

        if prev is not None:
            lines.append(f"{prev} -> {node};")
        prev = node

    lines.append("}")
    return "\n".join(lines)
