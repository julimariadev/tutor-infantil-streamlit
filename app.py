import streamlit as st
import random
from contenidos import MATERIAS, explicacion_larga

st.set_page_config(page_title="Tutor PRO MAX", page_icon="🌈")

EDADES = ["6-7 años", "8-9 años", "10-12 años"]

# estado
if "puntos" not in st.session_state:
    st.session_state.puntos = 0

if "pregunta" not in st.session_state:
    st.session_state.pregunta = None

st.title("🌈 Tutor Infantil PRO MAX")

materia = st.selectbox("Materia", list(MATERIAS.keys()))
tema = st.selectbox("Tema", list(MATERIAS[materia].keys()))
edad = st.selectbox("Edad", EDADES)

info = MATERIAS[materia][tema]

# explicación larga
st.subheader("📚 Explicación")
st.info(explicacion_larga(info["base"], edad, tema))

# generar pregunta
if st.button("Generar pregunta"):
    st.session_state.pregunta = random.choice(info["preguntas"])

if st.session_state.pregunta:
    p = st.session_state.pregunta

    st.subheader("🧠 Pregunta")
    st.write(p["q"])

    opcion = st.radio("Respuesta:", p["ops"])

    if st.button("Responder"):
        if opcion == p["r"]:
            st.success("Correcto 🎉")
            st.session_state.puntos += 10
        else:
            st.error("Incorrecto ❌")
            st.info(f"Respuesta correcta: {p['r']}")

st.metric("Puntos", st.session_state.puntos)