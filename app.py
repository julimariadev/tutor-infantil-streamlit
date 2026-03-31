import streamlit as st
import random

st.set_page_config(page_title="Tutor Infantil PRO", page_icon="🌈", layout="centered")

# =========================
# ESTILOS (ADAPTA OSCURO/CLARO)
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #0b1020 0%, #1a2a5a 100%);
}

.title {
    text-align: center;
    color: white;
    font-size: 2.4rem;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #dbe4ff;
    margin-bottom: 20px;
}

.card {
    background: white;
    border-radius: 20px;
    padding: 20px;
    margin-top: 15px;
    color: #222 !important;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

.card h3 {
    color: #1f2a44 !important;
}

.card p {
    color: #333 !important;
    line-height: 1.7;
}

.question {
    background: #f4f6ff;
    border-radius: 15px;
    padding: 15px;
    margin-top: 10px;
}

.stButton > button {
    width: 100%;
    border-radius: 15px;
    padding: 12px;
    font-weight: bold;
    background: linear-gradient(90deg, #7b61ff, #5b8cff);
    color: white;
}
</style>
""", unsafe_allow_html=True)

# =========================
# CONTENIDOS
# =========================
contenidos = {
    "Matemáticas": {
        "sumas": {
            "base": "Sumar significa juntar cantidades para obtener un total.",
            "ejemplo": "Si tienes 3 manzanas y te dan 2 más, ahora tienes 5.",
            "preguntas": [
                {"q": "¿Cuánto es 2 + 2?", "ops": ["3", "4", "5"], "r": "4"},
                {"q": "¿Cuánto es 5 + 1?", "ops": ["6", "7", "5"], "r": "6"},
                {"q": "¿Cuánto es 3 + 3?", "ops": ["6", "7", "5"], "r": "6"},
            ]
        }
    },
    "Español": {
        "antónimos": {
            "base": "Los antónimos son palabras que tienen significados opuestos.",
            "ejemplo": "Alto y bajo son opuestos.",
            "preguntas": [
                {"q": "¿Antónimo de 'frío'?", "ops": ["caliente", "tibio", "hielo"], "r": "caliente"},
                {"q": "¿Antónimo de 'grande'?", "ops": ["pequeño", "alto", "largo"], "r": "pequeño"},
            ]
        }
    }
}

# =========================
# FUNCIONES
# =========================
def generar_explicacion(base, edad):
    if edad == "6-7 años":
        return base + " Imagina que estás jugando. Aprenderemos paso a paso con ejemplos fáciles."
    elif edad == "8-9 años":
        return base + " Ahora veremos más ejemplos para entender mejor."
    else:
        return base + " Analizaremos este tema con más profundidad."

# =========================
# ESTADO
# =========================
if "tema" not in st.session_state:
    st.session_state.tema = None

if "pregunta_index" not in st.session_state:
    st.session_state.pregunta_index = 0

if "puntos" not in st.session_state:
    st.session_state.puntos = 0

# =========================
# UI
# =========================
st.markdown("<div class='title'>🌈 Tutor Infantil PRO</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Aprende jugando 🎮✨</div>", unsafe_allow_html=True)

st.metric("⭐ Puntos", st.session_state.puntos)

materia = st.selectbox("📚 Materia", list(contenidos.keys()))
tema = st.selectbox("✏️ Tema", list(contenidos[materia].keys()))
edad = st.selectbox("🧒 Edad", ["6-7 años", "8-9 años", "10-12 años"])

if st.button("✨ Aprender"):
    st.session_state.tema = contenidos[materia][tema]
    st.session_state.pregunta_index = 0

# =========================
# MOSTRAR CONTENIDO
# =========================
if st.session_state.tema:
    t = st.session_state.tema

    explicacion = generar_explicacion(t["base"], edad)

    st.markdown(f"""
    <div class="card">
        <h3>🌟 Explicación</h3>
        <p>{explicacion}</p>

        <h3>📌 Ejemplo</h3>
        <p>{t["ejemplo"]}</p>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # QUIZ MULTIPLE
    # =========================
    preguntas = t["preguntas"]
    i = st.session_state.pregunta_index

    if i < len(preguntas):
        p = preguntas[i]

        st.markdown(f"""
        <div class="question">
            <strong>🧠 Pregunta {i+1}:</strong>
            <p>{p["q"]}</p>
        </div>
        """, unsafe_allow_html=True)

        opcion = st.radio("Elige:", p["ops"], key=i)

        if st.button("Responder"):
            if opcion == p["r"]:
                st.success("🎉 ¡Correcto!")
                st.session_state.puntos += 10
            else:
                st.error("❌ Incorrecto")

            st.session_state.pregunta_index += 1

    else:
        st.success("🏆 Terminaste el tema")

# =========================
# RESET
# =========================
if st.button("🔄 Reiniciar"):
    st.session_state.tema = None
    st.session_state.puntos = 0
    st.session_state.pregunta_index = 0