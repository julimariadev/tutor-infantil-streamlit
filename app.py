import streamlit as st
import random

st.set_page_config(
    page_title="Tutor Infantil Interactivo",
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
<style>
    .main {
        background-color: #fefaf6;
    }
    h1 {
        text-align: center;
        color: #ff6b6b;
    }
    .stButton > button {
        background-color: #6c63ff;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 18px;
        font-size: 16px;
    }
    .bloque {
        background-color: #ffffff;
        padding: 18px;
        border-radius: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

contenidos = {
    "Matemáticas": {
        "sumas": {
            "explicacion": "Sumar es juntar cantidades. Si tienes 2 manzanas y te dan 3 más, ahora tienes 5 manzanas.",
            "ejemplo": "2 + 3 = 5",
            "pregunta": "¿Cuánto es 4 + 2?",
            "respuesta": "6"
        },
        "restas": {
            "explicacion": "Restar es quitar una cantidad. Si tienes 5 dulces y comes 2, te quedan 3.",
            "ejemplo": "5 - 2 = 3",
            "pregunta": "¿Cuánto es 7 - 3?",
            "respuesta": "4"
        },
        "multiplicación": {
            "explicacion": "Multiplicar es sumar varias veces la misma cantidad. Por ejemplo, 3 veces 2 es como sumar 2 + 2 + 2.",
            "ejemplo": "3 x 2 = 6",
            "pregunta": "¿Cuánto es 2 x 4?",
            "respuesta": "8"
        }
    },
    "Español": {
        "sustantivos": {
            "explicacion": "Los sustantivos son palabras que nombran personas, animales, lugares o cosas.",
            "ejemplo": "Niño, perro, casa y escuela son sustantivos.",
            "pregunta": "¿La palabra 'mesa' es un sustantivo?",
            "respuesta": "sí"
        },
        "adjetivos": {
            "explicacion": "Los adjetivos describen cómo es una persona, animal o cosa.",
            "ejemplo": "En 'perro grande', la palabra 'grande' es un adjetivo.",
            "pregunta": "En 'flor bonita', ¿cuál es el adjetivo?",
            "respuesta": "bonita"
        },
        "verbos": {
            "explicacion": "Los verbos son palabras que indican acciones.",
            "ejemplo": "Correr, saltar, leer y cantar son verbos.",
            "pregunta": "¿La palabra 'jugar' es un verbo?",
            "respuesta": "sí"
        }
    },
    "Ciencias": {
        "los animales": {
            "explicacion": "Los animales son seres vivos. Nacen, crecen, se alimentan y necesitan agua y aire.",
            "ejemplo": "El perro, el gato y la mariposa son animales.",
            "pregunta": "¿El perro es un ser vivo?",
            "respuesta": "sí"
        },
        "las plantas": {
            "explicacion": "Las plantas son seres vivos que necesitan agua, luz del sol y tierra para crecer.",
            "ejemplo": "El girasol y el árbol son plantas.",
            "pregunta": "¿Qué necesitan las plantas para crecer?",
            "respuesta": "agua y luz del sol"
        },
        "el cuerpo humano": {
            "explicacion": "El cuerpo humano tiene partes como la cabeza, los brazos, las piernas y el corazón.",
            "ejemplo": "Con las piernas caminamos y con los ojos vemos.",
            "pregunta": "¿Con qué parte del cuerpo vemos?",
            "respuesta": "ojos"
        }
    },
    "Geografía": {
        "continentes": {
            "explicacion": "Los continentes son grandes porciones de tierra del planeta Tierra.",
            "ejemplo": "América, África, Asia, Europa y Oceanía son continentes.",
            "pregunta": "¿América es un continente?",
            "respuesta": "sí"
        },
        "mapas": {
            "explicacion": "Los mapas sirven para representar lugares, países, ciudades y caminos.",
            "ejemplo": "Un mapa de Colombia muestra sus regiones y departamentos.",
            "pregunta": "¿Para qué sirve un mapa?",
            "respuesta": "para mostrar lugares"
        },
        "colombia": {
            "explicacion": "Colombia es un país de América del Sur. Tiene muchas regiones, montañas, ríos y costas.",
            "ejemplo": "Bogotá es la capital de Colombia.",
            "pregunta": "¿Cuál es la capital de Colombia?",
            "respuesta": "bogotá"
        }
    }
}

mensajes_motivadores = [
    "🌟 ¡Muy bien, sigue aprendiendo!",
    "🎉 ¡Excelente trabajo!",
    "👏 ¡Lo estás haciendo genial!",
    "🚀 ¡Cada vez sabes más!",
    "🧠 ¡Tu esfuerzo vale mucho!"
]

st.title("🎓 Tutor Infantil Interactivo")
st.write("¡Hola! Soy tu tutor amigable. Vamos a aprender juntos de forma divertida.")

materia = st.selectbox(
    "📚 Elige una materia:",
    list(contenidos.keys())
)

temas_disponibles = list(contenidos[materia].keys())

tema = st.selectbox(
    "✏️ Elige un tema:",
    temas_disponibles
)

edad = st.selectbox(
    "🧒 Edad aproximada del niño:",
    ["6-7 años", "8-9 años", "10-12 años"]
)

if "tema_actual" not in st.session_state:
    st.session_state.tema_actual = None

if "respuesta_correcta" not in st.session_state:
    st.session_state.respuesta_correcta = None

if "puntos" not in st.session_state:
    st.session_state.puntos = 0

if st.button("Explicar tema"):
    info = contenidos[materia][tema]
    st.session_state.tema_actual = info
    st.session_state.respuesta_correcta = info["respuesta"]

if st.session_state.tema_actual:
    info = st.session_state.tema_actual

    st.markdown(f"""
    <div class="bloque">
        <h3>🌟 Explicación</h3>
        <p>{info["explicacion"]}</p>
        <h3>📌 Ejemplo</h3>
        <p>{info["ejemplo"]}</p>
        <h3>❓ Pregunta</h3>
        <p>{info["pregunta"]}</p>
    </div>
    """, unsafe_allow_html=True)

    respuesta_nino = st.text_input("💬 Escribe tu respuesta:")

    if st.button("Revisar mi respuesta"):
        if respuesta_nino.strip() == "":
            st.warning("Por favor, escribe una respuesta.")
        else:
            respuesta_usuario = respuesta_nino.strip().lower()
            respuesta_correcta = st.session_state.respuesta_correcta.strip().lower()

            if respuesta_correcta in respuesta_usuario or respuesta_usuario in respuesta_correcta:
                st.success("✅ ¡Respuesta correcta!")
                st.success(random.choice(mensajes_motivadores))
                st.session_state.puntos += 1
            else:
                st.error("❌ No exactamente. Intenta de nuevo.")
                st.info(f"Respuesta esperada: {st.session_state.respuesta_correcta}")
                st.info("💪 No pasa nada, equivocarse también ayuda a aprender.")

st.markdown("---")
st.subheader("⭐ Puntaje")
st.write(f"Llevas **{st.session_state.puntos}** punto(s).")