import streamlit as st
import random

st.set_page_config(page_title="Tutor PRO", page_icon="🎮", layout="centered")

# =========================
# ESTILOS PRO
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #0b1020 0%, #1a2a5a 100%);
}

.title {
    text-align: center;
    color: white;
    font-size: 2.6rem;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #cdd8ff;
    margin-bottom: 20px;
}

.card {
    background: white;
    border-radius: 20px;
    padding: 18px;
    margin-top: 15px;
    text-align: center;
    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    cursor: pointer;
}

.card:hover {
    transform: scale(1.03);
}

.question-box {
    background: white;
    border-radius: 20px;
    padding: 20px;
    margin-top: 20px;
    color: #222;
}

.stButton > button {
    width: 100%;
    border-radius: 15px;
    padding: 12px;
    font-weight: bold;
    background: linear-gradient(90deg, #7b61ff, #5b8cff);
    color: white;
}

.reward {
    background: #ffd166;
    padding: 10px;
    border-radius: 15px;
    text-align: center;
    font-weight: bold;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# DATOS
# =========================
data = {
    "Matemáticas": [
        {"q": "¿Cuánto es 2 + 3?", "options": ["4", "5", "6"], "a": "5"},
        {"q": "¿Cuánto es 4 x 2?", "options": ["6", "8", "10"], "a": "8"},
    ],
    "Español": [
        {"q": "¿Cuál es un antónimo de 'alto'?", "options": ["bajo", "grande", "fuerte"], "a": "bajo"},
        {"q": "¿'feliz' y 'contento' son?", "options": ["antónimos", "sinónimos", "verbos"], "a": "sinónimos"},
    ],
    "Ciencias": [
        {"q": "¿Qué necesitan las plantas?", "options": ["agua", "metal", "plástico"], "a": "agua"},
    ],
    "Geografía": [
        {"q": "¿Capital de Colombia?", "options": ["Bogotá", "Lima", "Quito"], "a": "Bogotá"},
    ]
}

# =========================
# ESTADO
# =========================
if "materia" not in st.session_state:
    st.session_state.materia = None

if "pregunta" not in st.session_state:
    st.session_state.pregunta = None

if "puntos" not in st.session_state:
    st.session_state.puntos = 0

if "vidas" not in st.session_state:
    st.session_state.vidas = 3

# =========================
# HEADER
# =========================
st.markdown("<div class='title'>🎮 Tutor Infantil PRO</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Aprende jugando y gana puntos ⭐</div>", unsafe_allow_html=True)

st.metric("⭐ Puntos", st.session_state.puntos)
st.metric("❤️ Vidas", st.session_state.vidas)

# =========================
# SELECCIÓN VISUAL
# =========================
st.subheader("📚 Elige una materia")

cols = st.columns(2)

materias = list(data.keys())

for i, m in enumerate(materias):
    if cols[i % 2].button(m):
        st.session_state.materia = m
        st.session_state.pregunta = random.choice(data[m])

# =========================
# MOSTRAR PREGUNTA
# =========================
if st.session_state.pregunta:

    p = st.session_state.pregunta

    st.markdown(f"""
    <div class="question-box">
        <h3>🧠 {p["q"]}</h3>
    </div>
    """, unsafe_allow_html=True)

    opcion = st.radio("Elige una respuesta:", p["options"])

    if st.button("🎯 Responder"):
        if opcion == p["a"]:
            st.success("🎉 ¡Correcto!")
            st.session_state.puntos += 10
        else:
            st.error("❌ Incorrecto")
            st.session_state.vidas -= 1

        if st.session_state.vidas > 0:
            st.session_state.pregunta = random.choice(data[st.session_state.materia])
        else:
            st.warning("💔 Te quedaste sin vidas. Reinicia el juego.")
            st.session_state.pregunta = None

# =========================
# RECOMPENSAS
# =========================
if st.session_state.puntos >= 30:
    st.markdown("<div class='reward'>🏆 ¡Eres un campeón!</div>", unsafe_allow_html=True)

# =========================
# RESET
# =========================
if st.button("🔄 Reiniciar juego"):
    st.session_state.puntos = 0
    st.session_state.vidas = 3
    st.session_state.pregunta = None