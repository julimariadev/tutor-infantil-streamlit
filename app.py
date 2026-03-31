import streamlit as st
import random

st.set_page_config(page_title="Tutor PRO MAX", page_icon="🌈", layout="centered")

# =========================================================
# CONFIGURACIÓN
# =========================================================
EDADES = ["6-7 años", "8-9 años", "10-12 años"]
DIFICULTAD = ["Fácil", "Medio", "Avanzado"]

# =========================================================
# BASE DE DATOS COMPLETA
# =========================================================
MATERIAS = {
    "Matemáticas": {
        "sumas": {
            "explicacion": "Sumar es juntar cantidades para obtener un total.",
            "preguntas": [
                {"q": "2 + 3", "ops": ["4", "5", "6"], "r": "5"},
                {"q": "4 + 4", "ops": ["6", "8", "7"], "r": "8"},
                {"q": "6 + 2", "ops": ["7", "8", "9"], "r": "8"}
            ]
        },
        "restas": {
            "explicacion": "Restar es quitar cantidades.",
            "preguntas": [
                {"q": "7 - 2", "ops": ["5", "6", "4"], "r": "5"},
                {"q": "10 - 3", "ops": ["6", "7", "8"], "r": "7"},
            ]
        },
        "multiplicación": {
            "explicacion": "Multiplicar es sumar varias veces.",
            "preguntas": [
                {"q": "3 x 2", "ops": ["5", "6", "7"], "r": "6"},
                {"q": "4 x 3", "ops": ["12", "10", "14"], "r": "12"},
            ]
        }
    },

    "Español": {
        "sustantivos": {
            "explicacion": "Los sustantivos nombran cosas.",
            "preguntas": [
                {"q": "¿Cuál es sustantivo?", "ops": ["mesa", "correr", "grande"], "r": "mesa"},
                {"q": "¿Perro es sustantivo?", "ops": ["sí", "no"], "r": "sí"},
            ]
        },
        "verbos": {
            "explicacion": "Los verbos indican acciones.",
            "preguntas": [
                {"q": "¿Cuál es verbo?", "ops": ["correr", "mesa", "rojo"], "r": "correr"},
            ]
        }
    },

    "Ciencias": {
        "animales": {
            "explicacion": "Los animales son seres vivos.",
            "preguntas": [
                {"q": "¿El perro es un animal?", "ops": ["sí", "no"], "r": "sí"},
            ]
        },
        "plantas": {
            "explicacion": "Las plantas necesitan agua y sol.",
            "preguntas": [
                {"q": "¿Qué necesitan?", "ops": ["agua", "metal"], "r": "agua"},
            ]
        }
    },

    "Geografía": {
        "colombia": {
            "explicacion": "Colombia es un país de América del Sur.",
            "preguntas": [
                {"q": "Capital de Colombia", "ops": ["Bogotá", "Lima"], "r": "Bogotá"},
            ]
        }
    }
}

# =========================================================
# ESTADO
# =========================================================
if "puntos" not in st.session_state:
    st.session_state.puntos = 0

if "nivel" not in st.session_state:
    st.session_state.nivel = 1

if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = None

if "progreso_tema" not in st.session_state:
    st.session_state.progreso_tema = 0

# =========================================================
# HEADER
# =========================================================
st.title("🌈 Tutor Infantil PRO MAX")
st.caption("Aprende con explicaciones, práctica y juego 🎮")

col1, col2 = st.columns(2)
col1.metric("⭐ Puntos", st.session_state.puntos)
col2.metric("🎯 Nivel", st.session_state.nivel)

st.progress(min(st.session_state.puntos / 100, 1.0), text="Progreso general")

# =========================================================
# SELECCIÓN
# =========================================================
materia = st.selectbox("📚 Materia", list(MATERIAS.keys()))
tema = st.selectbox("✏️ Tema", list(MATERIAS[materia].keys()))
edad = st.selectbox("🧒 Edad", EDADES)
nivel = st.selectbox("🎮 Dificultad", DIFICULTAD)

contenido = MATERIAS[materia][tema]

# =========================================================
# EXPLICACIÓN
# =========================================================
st.subheader("🌟 Explicación")
st.info(contenido["explicacion"])

# =========================================================
# PREGUNTA ALEATORIA
# =========================================================
if st.button("🎯 Generar pregunta"):
    st.session_state.pregunta_actual = random.choice(contenido["preguntas"])

# =========================================================
# MOSTRAR PREGUNTA
# =========================================================
if st.session_state.pregunta_actual:

    p = st.session_state.pregunta_actual

    st.subheader("🧠 Pregunta")
    st.write(p["q"])

    opcion = st.radio("Elige respuesta:", p["ops"])

    if st.button("Responder"):

        if opcion == p["r"]:
            st.success("🎉 Correcto!")
            st.session_state.puntos += 10
            st.session_state.progreso_tema += 1
        else:
            st.error("❌ Incorrecto")
            st.info(f"Respuesta correcta: {p['r']}")

        # subir nivel
        if st.session_state.puntos >= st.session_state.nivel * 50:
            st.session_state.nivel += 1
            st.success("🚀 Subiste de nivel!")

# =========================================================
# PROGRESO DEL TEMA
# =========================================================
st.subheader("📊 Progreso del tema")
st.progress(min(st.session_state.progreso_tema / 10, 1.0))

# =========================================================
# RESET
# =========================================================
if st.button("🔄 Reiniciar todo"):
    st.session_state.puntos = 0
    st.session_state.nivel = 1
    st.session_state.pregunta_actual = None
    st.session_state.progreso_tema = 0