import streamlit as st
import random

st.set_page_config(
    page_title="Tutor Infantil Interactivo",
    page_icon="🌈",
    layout="centered"
)

# =====================================
# ESTILOS
# =====================================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #0b1020 0%, #17213f 100%);
    }

    .main-title {
        text-align: center;
        color: #ffffff;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #dce6ff;
        font-size: 1.05rem;
        margin-bottom: 1.4rem;
    }

    .info-chip {
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.08);
        color: #ffffff;
        padding: 12px 16px;
        border-radius: 18px;
        margin-bottom: 10px;
        font-weight: 600;
    }

    .card {
        background: #ffffff;
        color: #1d2433 !important;
        border-radius: 24px;
        padding: 24px;
        margin-top: 18px;
        box-shadow: 0 12px 32px rgba(0,0,0,0.22);
        border: 2px solid #eef2ff;
    }

    .card h3 {
        color: #1c2740 !important;
        margin-top: 18px;
        margin-bottom: 10px;
        font-size: 1.25rem;
    }

    .card p {
        color: #2d3748 !important;
        line-height: 1.75;
        font-size: 1rem;
        margin-bottom: 8px;
    }

    .reward-box {
        background: linear-gradient(90deg, #ffd166, #ffb703);
        color: #3a2a00;
        padding: 14px 18px;
        border-radius: 18px;
        text-align: center;
        font-weight: 800;
        margin-top: 14px;
    }

    .footer-box {
        text-align: center;
        color: #dce6ff;
        font-size: 0.95rem;
        margin-top: 26px;
        margin-bottom: 10px;
    }

    .stButton > button {
        width: 100%;
        border: none;
        border-radius: 18px;
        padding: 0.85rem 1rem;
        font-size: 1rem;
        font-weight: 700;
        color: #ffffff;
        background: linear-gradient(90deg, #7b61ff, #4dabf7);
        box-shadow: 0 8px 20px rgba(91, 140, 255, 0.35);
    }

    .stButton > button:hover {
        filter: brightness(1.05);
        transform: scale(1.01);
    }

    div[data-testid="stMetricLabel"] {
        color: #dce6ff;
    }

    div[data-testid="stMetricValue"] {
        color: #ffffff;
    }

    /* Se adapta mejor al modo claro/oscuro porque forzamos colores
       en los bloques internos importantes */
    @media (max-width: 640px) {
        .main-title {
            font-size: 2rem;
        }

        .subtitle {
            font-size: 0.98rem;
        }

        .card {
            padding: 18px;
            border-radius: 18px;
        }

        .card h3 {
            font-size: 1.12rem;
        }

        .card p {
            font-size: 0.97rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# =====================================
# BASE DE CONTENIDOS
# =====================================
contenidos = {
    "Matemáticas": {
        "sumas": {
            "base": "La suma sirve para juntar cantidades. Cuando unes grupos de objetos, estás sumando.",
            "ejemplo": "Si tienes 3 caramelos y te dan 2 más, ahora tienes 5 caramelos. 3 + 2 = 5.",
            "curioso": "Usamos sumas al contar monedas, juguetes, frutas o puntos en un juego.",
            "pregunta": "¿Cuánto es 6 + 2?",
            "respuesta": "8"
        },
        "restas": {
            "base": "La resta sirve para quitar o comparar cantidades. Nos ayuda a saber cuánto queda o cuánto falta.",
            "ejemplo": "Si tienes 8 galletas y comes 3, te quedan 5. 8 - 3 = 5.",
            "curioso": "Restamos cuando compartimos dulces, perdemos una ficha o gastamos dinero.",
            "pregunta": "¿Cuánto es 9 - 4?",
            "respuesta": "5"
        },
        "multiplicación": {
            "base": "Multiplicar es sumar varias veces la misma cantidad. Ayuda a contar más rápido cuando hay grupos iguales.",
            "ejemplo": "Si hay 3 grupos de 4 pelotas, entonces 4 + 4 + 4 = 12, y también 3 x 4 = 12.",
            "curioso": "Las tablas de multiplicar sirven mucho para resolver ejercicios rápido.",
            "pregunta": "¿Cuánto es 3 x 4?",
            "respuesta": "12"
        },
        "división": {
            "base": "La división sirve para repartir en partes iguales. Nos dice cuánto le toca a cada grupo.",
            "ejemplo": "Si tienes 10 lápices y los repartes en 2 grupos iguales, tocan 5 en cada grupo.",
            "curioso": "Dividimos cuando compartimos comida, fichas o tiempo.",
            "pregunta": "¿Cuánto es 8 ÷ 2?",
            "respuesta": "4"
        },
        "fracciones": {
            "base": "Las fracciones muestran partes de un todo. Sirven para expresar cuando algo se divide en partes iguales.",
            "ejemplo": "Si una pizza se divide en 4 partes y comes 1, comiste 1/4.",
            "curioso": "Las fracciones aparecen en recetas, relojes, medidas y repartos.",
            "pregunta": "Si una torta se divide en 2 partes iguales y tomas 1, ¿qué fracción es?",
            "respuesta": "1/2"
        }
    },
    "Español": {
        "sustantivos": {
            "base": "Los sustantivos son palabras que nombran personas, animales, lugares o cosas.",
            "ejemplo": "Niña, perro, escuela, parque, casa y cuaderno son sustantivos.",
            "curioso": "Casi todo lo que vemos, tocamos o imaginamos puede tener un sustantivo.",
            "pregunta": "¿La palabra 'mesa' es un sustantivo?",
            "respuesta": "sí"
        },
        "adjetivos": {
            "base": "Los adjetivos describen cómo es una persona, un animal, un objeto o un lugar.",
            "ejemplo": "En 'flor hermosa', la palabra 'hermosa' describe a la flor.",
            "curioso": "Los adjetivos hacen que los textos sean más bonitos y detallados.",
            "pregunta": "En 'perro grande', ¿cuál es el adjetivo?",
            "respuesta": "grande"
        },
        "verbos": {
            "base": "Los verbos son palabras que expresan acciones, movimientos o estados.",
            "ejemplo": "Correr, saltar, estudiar, comer y jugar son verbos.",
            "curioso": "Sin verbos, muchas oraciones quedarían incompletas.",
            "pregunta": "¿La palabra 'leer' es un verbo?",
            "respuesta": "sí"
        },
        "sinónimos": {
            "base": "Los sinónimos son palabras distintas que tienen un significado parecido o muy cercano.",
            "ejemplo": "Feliz y contento son sinónimos. Rápido y veloz también.",
            "curioso": "Usar sinónimos evita repetir mucho la misma palabra.",
            "pregunta": "¿'rápido' y 'veloz' son sinónimos?",
            "respuesta": "sí"
        },
        "antónimos": {
            "base": "Los antónimos son palabras que tienen significados opuestos o contrarios.",
            "ejemplo": "Alto y bajo, frío y caliente, grande y pequeño son antónimos.",
            "curioso": "Los antónimos ayudan a comparar mejor las cosas.",
            "pregunta": "¿'frío' es antónimo de 'caliente'?",
            "respuesta": "sí"
        }
    },
    "Ciencias": {
        "los animales": {
            "base": "Los animales son seres vivos. Nacen, crecen, se alimentan, respiran y necesitan agua.",
            "ejemplo": "El perro, el gato, la mariposa y el pez son animales.",
            "curioso": "Hay animales que viven en la tierra, otros en el agua y otros vuelan.",
            "pregunta": "¿El perro es un ser vivo?",
            "respuesta": "sí"
        },
        "las plantas": {
            "base": "Las plantas son seres vivos que necesitan agua, luz del sol, aire y suelo para crecer.",
            "ejemplo": "El árbol, la rosa, el pasto y el girasol son plantas.",
            "curioso": "Las plantas ayudan a producir oxígeno y a cuidar el planeta.",
            "pregunta": "¿Qué necesitan las plantas para crecer?",
            "respuesta": "agua y luz del sol"
        },
        "el cuerpo humano": {
            "base": "El cuerpo humano tiene muchas partes que trabajan juntas para que podamos vivir, movernos y aprender.",
            "ejemplo": "Con los ojos vemos, con los oídos escuchamos y con las piernas caminamos.",
            "curioso": "El cerebro ayuda a pensar, recordar y controlar muchas funciones del cuerpo.",
            "pregunta": "¿Con qué parte del cuerpo vemos?",
            "respuesta": "ojos"
        },
        "los planetas": {
            "base": "Los planetas son grandes cuerpos del espacio que giran alrededor del Sol.",
            "ejemplo": "Mercurio, Venus, Tierra y Marte son planetas del sistema solar.",
            "curioso": "La Tierra es el planeta donde vivimos y tiene agua, aire y vida.",
            "pregunta": "¿Cómo se llama el planeta donde vivimos?",
            "respuesta": "tierra"
        },
        "el agua": {
            "base": "El agua es esencial para la vida. La necesitamos para beber, cocinar, limpiar y regar.",
            "ejemplo": "El agua está en ríos, lagos, mares, lluvia y nubes.",
            "curioso": "Gran parte del cuerpo humano también está formada por agua.",
            "pregunta": "¿El agua es importante para vivir?",
            "respuesta": "sí"
        }
    },
    "Geografía": {
        "continentes": {
            "base": "Los continentes son grandes extensiones de tierra en el planeta.",
            "ejemplo": "América, África, Asia, Europa y Oceanía son continentes.",
            "curioso": "Cada continente tiene distintos climas, animales, idiomas y culturas.",
            "pregunta": "¿América es un continente?",
            "respuesta": "sí"
        },
        "mapas": {
            "base": "Los mapas representan lugares y nos ayudan a ubicarnos.",
            "ejemplo": "En un mapa podemos ver países, ciudades, montañas, ríos y mares.",
            "curioso": "Hay mapas físicos, políticos, climáticos y muchos otros tipos.",
            "pregunta": "¿Para qué sirve un mapa?",
            "respuesta": "para mostrar lugares"
        },
        "colombia": {
            "base": "Colombia es un país de América del Sur con gran diversidad de paisajes, culturas y regiones.",
            "ejemplo": "Bogotá es la capital de Colombia.",
            "curioso": "Colombia tiene costas en el mar Caribe y en el océano Pacífico.",
            "pregunta": "¿Cuál es la capital de Colombia?",
            "respuesta": "bogotá"
        },
        "regiones naturales": {
            "base": "Las regiones naturales son zonas que comparten características parecidas como clima, relieve, vegetación y fauna.",
            "ejemplo": "En Colombia están la región Andina, Caribe, Pacífica, Amazonía, Orinoquía e Insular.",
            "curioso": "Cada región tiene paisajes y costumbres propias.",
            "pregunta": "¿La región Caribe es una región natural de Colombia?",
            "respuesta": "sí"
        },
        "océanos": {
            "base": "Los océanos son enormes masas de agua salada que cubren gran parte del planeta Tierra.",
            "ejemplo": "El océano Pacífico y el Atlántico son dos océanos muy importantes.",
            "curioso": "Dentro de los océanos viven miles de especies marinas.",
            "pregunta": "¿Los océanos tienen agua salada?",
            "respuesta": "sí"
        }
    }
}

mensajes_motivadores = [
    "🌟 ¡Excelente trabajo! Sigue aprendiendo con alegría.",
    "🎉 ¡Muy bien! Lo estás haciendo increíble.",
    "🚀 ¡Fantástico! Vas avanzando como una estrella del aprendizaje.",
    "👏 ¡Muy buena respuesta! Se nota tu esfuerzo.",
    "🧠 ¡Estás aprendiendo muchísimo!",
    "💡 ¡Sigue así! Cada intento te hace más fuerte."
]

mensajes_error = [
    "💪 No pasa nada. Equivocarse también enseña.",
    "🌈 Inténtalo otra vez. Tú puedes.",
    "📚 Aprender es practicar paso a paso.",
    "✨ Vas bien. Solo necesitamos otro intento."
]

# =====================================
# FUNCIONES
# =====================================
def generar_explicacion_detallada(materia: str, tema: str, edad: str, info: dict) -> str:
    base = info["base"]

    if edad == "6-7 años":
        return (
            f"{base} "
            f"Imagina que estás jugando o mirando cosas a tu alrededor. "
            f"Cuando aprendes sobre {tema}, puedes entender mejor lo que pasa en la escuela y en la vida diaria. "
            f"Vamos despacito: primero observamos, luego pensamos y después practicamos. "
            f"Lo importante es entender la idea principal con palabras fáciles. "
            f"Si algo parece difícil al principio, no te preocupes, porque aprender toma tiempo y está bien repetir. "
            f"Este tema se puede descubrir con ejemplos simples, como objetos, juegos, dibujos y situaciones cotidianas. "
            f"Cuando comprendes una idea pequeña, luego puedes entender una idea más grande. "
            f"Por eso aprender paso a paso es una gran estrategia."
        )

    if edad == "8-9 años":
        return (
            f"{base} "
            f"Este tema es importante porque aparece en muchas situaciones de la vida diaria y también en la escuela. "
            f"Aprender {tema} te ayuda a pensar mejor, describir, resolver problemas o comprender el mundo, según la materia que elegiste. "
            f"Una buena forma de aprender es mirar un ejemplo, descubrir qué pasa y luego intentarlo por tu cuenta. "
            f"Cuando practicas varias veces, tu mente empieza a reconocer patrones y todo se vuelve más claro. "
            f"No se trata solo de memorizar, sino de entender por qué sucede cada cosa. "
            f"Si observas con atención, verás que este tema está en libros, conversaciones, juegos, naturaleza y muchas actividades cotidianas. "
            f"Cuanto más practiques, más seguridad tendrás al responder preguntas y explicar con tus propias palabras."
        )

    return (
        f"{base} "
        f"Este tema es importante porque desarrolla comprensión, análisis y capacidad para relacionar ideas. "
        f"Aprender {tema} no solo sirve para contestar preguntas, sino también para interpretar mejor situaciones reales, resolver ejercicios y expresar conocimientos con mayor claridad. "
        f"Cuando estudias un tema con atención, puedes identificar sus características, compararlo con otros temas y usarlo en contextos distintos. "
        f"Es muy útil observar ejemplos, descubrir reglas o patrones y luego practicar con tus propias respuestas. "
        f"Además, comprender en profundidad ayuda a recordar por más tiempo y a construir una base sólida para temas más avanzados. "
        f"Por eso es importante leer con calma, pensar en lo que significa cada idea y tratar de explicarla con palabras propias. "
        f"Así el aprendizaje se vuelve más completo, más consciente y mucho más útil."
    )


def generar_ejemplo_detallado(edad: str, ejemplo: str) -> str:
    if edad == "6-7 años":
        return f"{ejemplo} Este ejemplo usa una situación sencilla para que puedas imaginarlo fácilmente."
    if edad == "8-9 años":
        return f"{ejemplo} Observa qué pasa paso a paso y piensa por qué esa respuesta tiene sentido."
    return f"{ejemplo} Analiza bien el ejemplo y trata de descubrir la regla o idea principal que lo explica."


# =====================================
# ESTADO
# =====================================
if "tema_actual" not in st.session_state:
    st.session_state.tema_actual = None

if "respuesta_correcta" not in st.session_state:
    st.session_state.respuesta_correcta = None

if "puntos" not in st.session_state:
    st.session_state.puntos = 0

if "respuestas_correctas" not in st.session_state:
    st.session_state.respuestas_correctas = 0

if "intentos" not in st.session_state:
    st.session_state.intentos = 0

# =====================================
# ENCABEZADO
# =====================================
st.markdown("""
<div style='text-align:center; padding-top: 8px;'>
    <div style='font-size: 3rem;'>🌈🧸📚✨</div>
    <div class='main-title'>Tutor Infantil Interactivo</div>
    <div class='subtitle'>
        Aprende jugando con explicaciones más completas, ejemplos, datos curiosos y retos divertidos.
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# MÉTRICAS
# =====================================
col1, col2 = st.columns(2)
with col1:
    st.metric("⭐ Puntaje", st.session_state.puntos)
with col2:
    st.metric("✅ Correctas", st.session_state.respuestas_correctas)

if st.session_state.intentos > 0:
    progreso = st.session_state.respuestas_correctas / st.session_state.intentos
else:
    progreso = 0.0

st.progress(progreso, text="📈 Tu progreso de aprendizaje")

# =====================================
# SELECCIÓN
# =====================================
st.markdown("<div class='info-chip'>👩‍🏫 Tu guía de hoy es Profe Estrella 🌟</div>", unsafe_allow_html=True)

materia = st.selectbox("📚 Elige una materia:", list(contenidos.keys()))
tema = st.selectbox("✏️ Elige un tema:", list(contenidos[materia].keys()))
edad = st.selectbox("🧒 Edad aproximada del niño:", ["6-7 años", "8-9 años", "10-12 años"])

mensajes_edad = {
    "6-7 años": "🧸 Explicaciones con palabras más fáciles y pasos pequeños.",
    "8-9 años": "🌟 Explicaciones claras con más detalles y ejemplos útiles.",
    "10-12 años": "📘 Explicaciones más completas para comprender mejor el tema."
}

st.markdown(
    f"<div class='info-chip'>{mensajes_edad[edad]}</div>",
    unsafe_allow_html=True
)

# =====================================
# EXPLORAR
# =====================================
if st.button("✨ Explorar tema"):
    info = contenidos[materia][tema]
    st.session_state.tema_actual = info
    st.session_state.respuesta_correcta = info["respuesta"]

# =====================================
# CONTENIDO
# =====================================
if st.session_state.tema_actual:
    info = st.session_state.tema_actual

    explicacion_larga = generar_explicacion_detallada(materia, tema, edad, info)
    ejemplo_largo = generar_ejemplo_detallado(edad, info["ejemplo"])

    st.markdown(f"""
    <div class="card">
        <h3>🌟 Explicación</h3>
        <p>{explicacion_larga}</p>

        <h3>📌 Ejemplo</h3>
        <p>{ejemplo_largo}</p>

        <h3>💡 Dato curioso</h3>
        <p>{info["curioso"]}</p>

        <h3>🎯 Pregunta para pensar</h3>
        <p>{info["pregunta"]}</p>
    </div>
    """, unsafe_allow_html=True)

    respuesta_nino = st.text_input("💬 Escribe tu respuesta:")

    if st.button("🎈 Revisar mi respuesta"):
        if respuesta_nino.strip() == "":
            st.warning("Por favor, escribe una respuesta antes de revisar.")
        else:
            st.session_state.intentos += 1

            respuesta_usuario = respuesta_nino.strip().lower()
            respuesta_correcta = st.session_state.respuesta_correcta.strip().lower()

            if respuesta_correcta in respuesta_usuario or respuesta_usuario in respuesta_correcta:
                st.success("✅ ¡Respuesta correcta!")
                st.success(random.choice(mensajes_motivadores))
                st.session_state.puntos += 10
                st.session_state.respuestas_correctas += 1
            else:
                st.error("❌ Todavía no es la respuesta esperada.")
                st.info(f"Respuesta esperada: {st.session_state.respuesta_correcta}")
                st.info(random.choice(mensajes_error))

# =====================================
# RECOMPENSAS
# =====================================
if 10 <= st.session_state.puntos < 30:
    st.markdown("<div class='reward-box'>🥉 ¡Ganaste tu primera medalla de aprendizaje!</div>", unsafe_allow_html=True)
elif 30 <= st.session_state.puntos < 60:
    st.markdown("<div class='reward-box'>🥈 ¡Muy bien! Ya tienes una medalla plateada.</div>", unsafe_allow_html=True)
elif st.session_state.puntos >= 60:
    st.markdown("<div class='reward-box'>🥇 ¡Increíble! Eres un campeón del conocimiento.</div>", unsafe_allow_html=True)

# =====================================
# PIE
# =====================================
st.markdown("""
<div class='footer-box'>
    Hecho con cariño para aprender jugando 🌈✨🧸📚
</div>
""", unsafe_allow_html=True)