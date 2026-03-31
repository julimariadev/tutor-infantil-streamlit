import streamlit as st
import random

st.set_page_config(
    page_title="Tutor Infantil Interactivo",
    page_icon="🌈",
    layout="centered"
)

# =========================
# ESTILOS
# =========================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #0b1020 0%, #18213f 100%);
    }

    .titulo-principal {
        text-align: center;
        color: white;
        font-size: 2.4rem;
        font-weight: 800;
        margin-bottom: 0.3rem;
    }

    .subtitulo-principal {
        text-align: center;
        color: #dbe4ff;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }

    .tarjeta {
        background: white;
        border-radius: 24px;
        padding: 22px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.18);
        margin-top: 16px;
        color: #222 !important;
    }

    .tarjeta h3 {
        color: #1f2a44 !important;
        margin-top: 10px;
        margin-bottom: 8px;
        font-size: 1.25rem;
    }

    .tarjeta p {
        color: #333 !important;
        font-size: 1rem;
        line-height: 1.65;
        margin-bottom: 10px;
    }

    .mini-tarjeta {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 14px 16px;
        color: white;
        margin-top: 8px;
    }

    .mini-tarjeta strong {
        color: #ffffff;
    }

    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #7b61ff, #5f8cff);
        color: white;
        border: none;
        border-radius: 18px;
        padding: 0.85rem 1rem;
        font-size: 1rem;
        font-weight: 700;
    }

    .stButton > button:hover {
        transform: scale(1.01);
        filter: brightness(1.05);
    }

    .bloque-puntaje {
        background: linear-gradient(90deg, #ff9f43, #ffcf5c);
        border-radius: 20px;
        padding: 16px;
        text-align: center;
        color: #3b2f00;
        font-weight: 700;
        margin-top: 16px;
    }

    .footer-bonito {
        text-align: center;
        color: #cfd8ff;
        font-size: 0.95rem;
        margin-top: 25px;
        margin-bottom: 10px;
    }

    div[data-testid="stMetricValue"] {
        color: white;
    }

    div[data-testid="stMetricLabel"] {
        color: #dbe4ff;
    }

    @media (max-width: 640px) {
        .titulo-principal {
            font-size: 2rem;
        }

        .subtitulo-principal {
            font-size: 0.98rem;
        }

        .tarjeta {
            padding: 18px;
            border-radius: 18px;
        }

        .tarjeta h3 {
            font-size: 1.12rem;
        }

        .tarjeta p {
            font-size: 0.97rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# =========================
# CONTENIDO EDUCATIVO
# =========================
contenidos = {
    "Matemáticas": {
        "sumas": {
            "explicacion": "Sumar es juntar cantidades. Cuando unes dos grupos de cosas, estás sumando. Por ejemplo, si tienes 2 globos y te dan 3 más, ahora tienes 5 globos.",
            "ejemplo": "2 + 3 = 5",
            "dato_curioso": "Usamos las sumas todos los días, por ejemplo cuando contamos juguetes, frutas o lápices.",
            "pregunta": "¿Cuánto es 4 + 2?",
            "respuesta": "6"
        },
        "restas": {
            "explicacion": "Restar es quitar una cantidad. Si tienes algo y una parte se va, entonces haces una resta. Sirve para saber cuánto queda.",
            "ejemplo": "7 - 3 = 4",
            "dato_curioso": "Cuando compartes dulces o pierdes una canica, también estás viendo una resta en acción.",
            "pregunta": "¿Cuánto es 9 - 4?",
            "respuesta": "5"
        },
        "multiplicación": {
            "explicacion": "Multiplicar es sumar varias veces la misma cantidad. Si tienes 3 grupos de 2 manzanas, puedes sumar 2 + 2 + 2 o escribir 3 x 2.",
            "ejemplo": "3 x 2 = 6",
            "dato_curioso": "Las tablas de multiplicar ayudan a contar más rápido y a resolver problemas del día a día.",
            "pregunta": "¿Cuánto es 2 x 5?",
            "respuesta": "10"
        },
        "división": {
            "explicacion": "Dividir es repartir en partes iguales. Si tienes 8 galletas y quieres darlas en 2 grupos iguales, a cada grupo le tocan 4.",
            "ejemplo": "8 ÷ 2 = 4",
            "dato_curioso": "La división es muy útil cuando compartimos cosas de manera justa.",
            "pregunta": "¿Cuánto es 6 ÷ 2?",
            "respuesta": "3"
        },
        "fracciones": {
            "explicacion": "Las fracciones muestran partes de un todo. Por ejemplo, si una pizza está partida en 4 partes y comes 1, comiste un cuarto.",
            "ejemplo": "1/2 significa una de dos partes iguales.",
            "dato_curioso": "También usamos fracciones al medir tiempo, comida o distancia.",
            "pregunta": "Si partes una torta en 2 partes iguales y tomas 1, ¿qué fracción tienes?",
            "respuesta": "1/2"
        }
    },
    "Español": {
        "sustantivos": {
            "explicacion": "Los sustantivos son palabras que nombran personas, animales, lugares o cosas. Nos ayudan a decir de qué o de quién hablamos.",
            "ejemplo": "Niña, perro, parque y mesa son sustantivos.",
            "dato_curioso": "Casi todo lo que puedes ver, tocar o imaginar puede tener un sustantivo.",
            "pregunta": "¿La palabra 'casa' es un sustantivo?",
            "respuesta": "sí"
        },
        "adjetivos": {
            "explicacion": "Los adjetivos describen cómo es una persona, animal o cosa. Dicen si algo es grande, pequeño, bonito, rápido, alegre o colorido.",
            "ejemplo": "En 'flor bonita', la palabra 'bonita' es un adjetivo.",
            "dato_curioso": "Los adjetivos hacen que nuestras oraciones sean más expresivas y divertidas.",
            "pregunta": "En 'perro grande', ¿cuál es el adjetivo?",
            "respuesta": "grande"
        },
        "verbos": {
            "explicacion": "Los verbos son palabras que indican acciones o lo que sucede. Nos dicen qué hace alguien o qué está pasando.",
            "ejemplo": "Correr, saltar, leer, jugar y cantar son verbos.",
            "dato_curioso": "Casi todas las oraciones necesitan un verbo para tener sentido completo.",
            "pregunta": "¿La palabra 'leer' es un verbo?",
            "respuesta": "sí"
        },
        "sinónimos": {
            "explicacion": "Los sinónimos son palabras diferentes que tienen un significado parecido o casi igual.",
            "ejemplo": "Feliz y contento son sinónimos.",
            "dato_curioso": "Usar sinónimos ayuda a no repetir siempre las mismas palabras.",
            "pregunta": "¿'rápido' y 'veloz' son sinónimos?",
            "respuesta": "sí"
        },
        "antónimos": {
            "explicacion": "Los antónimos son palabras que significan lo contrario.",
            "ejemplo": "Alto y bajo son antónimos.",
            "dato_curioso": "Los antónimos nos ayudan a comparar mejor las cosas.",
            "pregunta": "¿'frío' es antónimo de 'caliente'?",
            "respuesta": "sí"
        }
    },
    "Ciencias": {
        "los animales": {
            "explicacion": "Los animales son seres vivos. Nacen, crecen, respiran, se alimentan y necesitan agua y aire para vivir.",
            "ejemplo": "El perro, el pez, la mariposa y el elefante son animales.",
            "dato_curioso": "Algunos animales viven en la selva, otros en el mar y otros en nuestras casas.",
            "pregunta": "¿El gato es un ser vivo?",
            "respuesta": "sí"
        },
        "las plantas": {
            "explicacion": "Las plantas son seres vivos que necesitan agua, luz del sol, aire y tierra para crecer. Muchas plantas producen oxígeno.",
            "ejemplo": "El árbol, la rosa y el girasol son plantas.",
            "dato_curioso": "Las plantas son muy importantes porque ayudan a limpiar el aire.",
            "pregunta": "¿Qué necesitan las plantas para crecer?",
            "respuesta": "agua y luz del sol"
        },
        "el cuerpo humano": {
            "explicacion": "El cuerpo humano tiene muchas partes que trabajan juntas. Con los ojos vemos, con los oídos escuchamos y con las piernas caminamos.",
            "ejemplo": "El corazón bombea sangre por todo el cuerpo.",
            "dato_curioso": "El cerebro es como el jefe del cuerpo porque envía muchas órdenes.",
            "pregunta": "¿Con qué parte del cuerpo vemos?",
            "respuesta": "ojos"
        },
        "los planetas": {
            "explicacion": "Los planetas son grandes cuerpos que giran alrededor del Sol. La Tierra es el planeta donde vivimos.",
            "ejemplo": "Mercurio, Venus, Tierra y Marte son algunos planetas del sistema solar.",
            "dato_curioso": "Júpiter es uno de los planetas más grandes del sistema solar.",
            "pregunta": "¿Cómo se llama el planeta donde vivimos?",
            "respuesta": "tierra"
        },
        "el agua": {
            "explicacion": "El agua es muy importante para la vida. La usamos para beber, cocinar, bañarnos y regar las plantas.",
            "ejemplo": "El agua puede estar en ríos, lagos, mares y nubes.",
            "dato_curioso": "Nuestro cuerpo también tiene mucha agua.",
            "pregunta": "¿El agua es importante para vivir?",
            "respuesta": "sí"
        }
    },
    "Geografía": {
        "continentes": {
            "explicacion": "Los continentes son grandes porciones de tierra del planeta Tierra. Cada continente tiene muchos países, paisajes y culturas.",
            "ejemplo": "América, África, Asia, Europa y Oceanía son continentes.",
            "dato_curioso": "La Antártida es el continente más frío del planeta.",
            "pregunta": "¿América es un continente?",
            "respuesta": "sí"
        },
        "mapas": {
            "explicacion": "Los mapas representan lugares. Sirven para ubicar países, ciudades, ríos, montañas y caminos.",
            "ejemplo": "Un mapa de Colombia muestra sus departamentos, regiones y ciudades importantes.",
            "dato_curioso": "Los mapas también pueden mostrar clima, relieve y mares.",
            "pregunta": "¿Para qué sirve un mapa?",
            "respuesta": "para mostrar lugares"
        },
        "colombia": {
            "explicacion": "Colombia es un país de América del Sur. Tiene montañas, selvas, ríos, dos océanos y muchas regiones naturales.",
            "ejemplo": "Bogotá es la capital de Colombia.",
            "dato_curioso": "Colombia es conocida por su gran variedad de animales, plantas y paisajes.",
            "pregunta": "¿Cuál es la capital de Colombia?",
            "respuesta": "bogotá"
        },
        "regiones naturales": {
            "explicacion": "Las regiones naturales son zonas con características parecidas en clima, paisaje, vegetación y relieve.",
            "ejemplo": "En Colombia existen regiones como la Andina, Caribe, Pacífica, Orinoquía, Amazonía e Insular.",
            "dato_curioso": "Cada región tiene comidas, costumbres y paisajes diferentes.",
            "pregunta": "¿La región Caribe es una región natural de Colombia?",
            "respuesta": "sí"
        },
        "océanos": {
            "explicacion": "Los océanos son enormes masas de agua salada que cubren gran parte de la Tierra.",
            "ejemplo": "El océano Pacífico y el océano Atlántico son muy conocidos.",
            "dato_curioso": "En el fondo del océano viven muchísimos seres vivos.",
            "pregunta": "¿Los océanos tienen agua salada?",
            "respuesta": "sí"
        }
    }
}

mensajes_motivadores = [
    "🌟 ¡Excelente trabajo! Sigue así.",
    "🎉 ¡Muy bien! Cada vez aprendes más.",
    "🚀 ¡Fantástico! Vas como un súper explorador del conocimiento.",
    "👏 ¡Lo hiciste muy bien! Estoy orgulloso de tu esfuerzo.",
    "🧠 ¡Tu mente está creciendo mucho con cada respuesta!",
    "💡 ¡Qué buena respuesta! Se nota que estás poniendo atención."
]

mensajes_error = [
    "💪 No pasa nada. Equivocarse también ayuda a aprender.",
    "🌈 Vamos de nuevo. Tú puedes hacerlo.",
    "📚 Cada intento te hace más fuerte y más inteligente.",
    "✨ Inténtalo otra vez. Aprender es un camino paso a paso."
]

# =========================
# ESTADO
# =========================
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

# =========================
# ENCABEZADO
# =========================
st.markdown("""
<div style='text-align:center; padding-top: 8px;'>
    <div style='font-size: 3rem;'>🌈📚✨</div>
    <div class='titulo-principal'>Tutor Infantil Interactivo</div>
    <div class='subtitulo-principal'>
        Aprende jugando con explicaciones fáciles, ejemplos, datos curiosos y preguntas divertidas.
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# PANEL SUPERIOR
# =========================
col1, col2 = st.columns(2)
with col1:
    st.metric("⭐ Puntaje", st.session_state.puntos)
with col2:
    st.metric("✅ Respuestas correctas", st.session_state.respuestas_correctas)

if st.session_state.intentos > 0:
    progreso = st.session_state.respuestas_correctas / st.session_state.intentos
else:
    progreso = 0.0

st.progress(progreso, text="📈 Tu progreso de aprendizaje")

# =========================
# SELECCIÓN
# =========================
st.markdown("<div class='mini-tarjeta'><strong>👩‍🏫 Tutor del día:</strong> Profe Estrella 🌟</div>", unsafe_allow_html=True)

materia = st.selectbox(
    "📚 Elige una materia:",
    list(contenidos.keys())
)

tema = st.selectbox(
    "✏️ Elige un tema:",
    list(contenidos[materia].keys())
)

edad = st.selectbox(
    "🧒 Edad aproximada del niño:",
    ["6-7 años", "8-9 años", "10-12 años"]
)

# Ajuste suave por edad
mensaje_edad = {
    "6-7 años": "🧸 Aprenderemos con palabras fáciles y pasos cortos.",
    "8-9 años": "🌟 Aprenderemos con ejemplos claros y preguntas divertidas.",
    "10-12 años": "📘 Aprenderemos con un poco más de detalle y comprensión."
}

st.markdown(
    f"<div class='mini-tarjeta'><strong>{mensaje_edad[edad]}</strong></div>",
    unsafe_allow_html=True
)

# =========================
# BOTÓN PRINCIPAL
# =========================
if st.button("✨ Explorar tema"):
    info = contenidos[materia][tema]
    st.session_state.tema_actual = info
    st.session_state.respuesta_correcta = info["respuesta"]

# =========================
# MOSTRAR CONTENIDO
# =========================
if st.session_state.tema_actual:
    info = st.session_state.tema_actual

    st.markdown(f"""
    <div class="tarjeta">
        <h3>🌟 Explicación</h3>
        <p>{info["explicacion"]}</p>

        <h3>📌 Ejemplo</h3>
        <p>{info["ejemplo"]}</p>

        <h3>💡 Dato curioso</h3>
        <p>{info["dato_curioso"]}</p>

        <h3>❓ Pregunta</h3>
        <p>{info["pregunta"]}</p>
    </div>
    """, unsafe_allow_html=True)

    respuesta_nino = st.text_input("💬 Escribe tu respuesta:")

    if st.button("🎯 Revisar mi respuesta"):
        if respuesta_nino.strip() == "":
            st.warning("Por favor, escribe una respuesta antes de revisar.")
        else:
            st.session_state.intentos += 1

            respuesta_usuario = respuesta_nino.strip().lower()
            respuesta_correcta = st.session_state.respuesta_correcta.strip().lower()

            if (
                respuesta_correcta in respuesta_usuario
                or respuesta_usuario in respuesta_correcta
            ):
                st.success("✅ ¡Respuesta correcta!")
                st.success(random.choice(mensajes_motivadores))
                st.session_state.puntos += 10
                st.session_state.respuestas_correctas += 1
            else:
                st.error("❌ No exactamente. Intenta de nuevo.")
                st.info(f"✅ Respuesta esperada: {st.session_state.respuesta_correcta}")
                st.info(random.choice(mensajes_error))

# =========================
# RECOMPENSAS
# =========================
if st.session_state.puntos >= 10 and st.session_state.puntos < 30:
    st.markdown(
        "<div class='bloque-puntaje'>🥉 ¡Ganaste tu primera medalla de aprendizaje!</div>",
        unsafe_allow_html=True
    )
elif st.session_state.puntos >= 30 and st.session_state.puntos < 60:
    st.markdown(
        "<div class='bloque-puntaje'>🥈 ¡Vas excelente! Ya tienes una medalla plateada.</div>",
        unsafe_allow_html=True
    )
elif st.session_state.puntos >= 60:
    st.markdown(
        "<div class='bloque-puntaje'>🥇 ¡Increíble! Eres un campeón del conocimiento.</div>",
        unsafe_allow_html=True
    )

# =========================
# PIE
# =========================
st.markdown("""
<div class='footer-bonito'>
    Hecho con cariño para aprender jugando 🌈✨📚
</div>
""", unsafe_allow_html=True)