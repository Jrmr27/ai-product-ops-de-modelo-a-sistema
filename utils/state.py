import streamlit as st
import pandas as pd

def init_state():
    ss = st.session_state

    ss.setdefault("contexto", {
        "proceso": "Gestión de incidencias (ejemplo)",
        "objetivo": "Reducir tiempo de ciclo y retrabajo manteniendo control y trazabilidad.",
        "alcance": "L1-L2, no incluye cambios mayores (CAB).",
        "volumen_mes": 6000,
        "restricciones": "PII minimizada; auditoría obligatoria; latencia razonable.",
    })

    # SIPOC como tabla editable
    ss.setdefault("sipoc", pd.DataFrame([
        {"Tipo": "Suppliers", "Item": "Usuarios / Sistemas"},
        {"Tipo": "Inputs", "Item": "Ticket + contexto"},
        {"Tipo": "Process", "Item": "Registrar → clasificar → resolver → cerrar"},
        {"Tipo": "Outputs", "Item": "Solución / escalado / cierre"},
        {"Tipo": "Customers", "Item": "Usuario final / Negocio"},
    ]))

    # AS-IS / TO-BE como tabla de pasos
    base_steps = pd.DataFrame([
        {"#": 1, "Actor": "Usuario", "Actividad": "Abre ticket", "Sistema": "Portal", "Dolor_ASIS": "Información incompleta", "Mejora_TOBE": "Formulario guiado + validación", "Palanca_IA": "Clasificación + extracción"},
        {"#": 2, "Actor": "L1", "Actividad": "Clasifica y enruta", "Sistema": "ITSM", "Dolor_ASIS": "Misrouting frecuente", "Mejora_TOBE": "Enrutado asistido", "Palanca_IA": "Triage semántico"},
        {"#": 3, "Actor": "L2", "Actividad": "Diagnostica", "Sistema": "KB", "Dolor_ASIS": "Búsqueda lenta", "Mejora_TOBE": "Búsqueda contextual", "Palanca_IA": "RAG sobre KB"},
        {"#": 4, "Actor": "L1", "Actividad": "Cierra y documenta", "Sistema": "ITSM", "Dolor_ASIS": "Cierre sin trazabilidad", "Mejora_TOBE": "Cierre con auditoría", "Palanca_IA": "Resumen + logging"},
    ])
    ss.setdefault("steps", base_steps)

    # RACI matriz (actividades x roles) y RAID
    ss.setdefault("roles", ["Service Owner", "SRE", "Data Steward", "Legal"])
    ss.setdefault("actividades", ["Diseñar flujo", "Operar (runbooks)", "Política de datos", "Auditoría"])

    ss.setdefault("raci", pd.DataFrame([
        {"Actividad": "Diseñar flujo", "Service Owner": "A", "SRE": "R", "Data Steward": "C", "Legal": "C"},
        {"Actividad": "Operar (runbooks)", "Service Owner": "A", "SRE": "R", "Data Steward": "C", "Legal": "I"},
        {"Actividad": "Política de datos", "Service Owner": "C", "SRE": "I", "Data Steward": "R", "Legal": "A"},
        {"Actividad": "Auditoría", "Service Owner": "A", "SRE": "R", "Data Steward": "C", "Legal": "C"},
    ]))

    ss.setdefault("raid", pd.DataFrame([
        {"Tipo": "Risk", "Item": "PII en prompts/logs", "Mitigación": "Minimización + filtro + auditoría", "Owner": "Data Steward", "Estado": "Open"},
        {"Tipo": "Assumption", "Item": "KB está actualizada", "Mitigación": "Revisión mensual + owners", "Owner": "Service Owner", "Estado": "Open"},
        {"Tipo": "Issue", "Item": "Latencia alta en picos", "Mitigación": "Caching + límites + fallback", "Owner": "SRE", "Estado": "Open"},
        {"Tipo": "Dependency", "Item": "Acceso a ITSM API", "Mitigación": "Aprobación TI + RBAC", "Owner": "SRE", "Estado": "Open"},
    ]))
