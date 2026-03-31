# contenidos.py

def explicacion_larga(base, edad, tema):
    if edad == "6-7 años":
        return f"""
{base}

Imagina que estás aprendiendo esto como si fuera un juego. 
Vamos paso a paso para que lo entiendas fácilmente.

📌 Este tema llamado "{tema}" es importante porque aparece en tu vida diaria.

Puedes aprenderlo usando ejemplos sencillos, dibujos y situaciones reales.

💡 No pasa nada si te equivocas, porque aprender es practicar.
"""

    elif edad == "8-9 años":
        return f"""
{base}

Este tema llamado "{tema}" es muy importante en la escuela.

Nos ayuda a entender mejor cómo funcionan las cosas.

📌 Se puede aplicar en ejercicios, juegos y situaciones reales.

💡 Mientras más practiques, más fácil será.
"""

    else:
        return f"""
{base}

Este tema "{tema}" es fundamental para desarrollar pensamiento lógico y comprensión.

Se utiliza en muchas áreas del conocimiento.

📌 Permite analizar, comparar y resolver problemas.

💡 Entenderlo bien te ayudará en niveles más avanzados.
"""


MATERIAS = {
    "Matemáticas": {
        "sumas": {
            "base": "La suma consiste en juntar cantidades para obtener un total.",
            "preguntas": [
                {"q": "2 + 3", "ops": ["4", "5", "6"], "r": "5"},
                {"q": "4 + 4", "ops": ["6", "8", "7"], "r": "8"},
            ]
        },
        "restas": {
            "base": "La resta consiste en quitar cantidades.",
            "preguntas": [
                {"q": "7 - 2", "ops": ["5", "6", "4"], "r": "5"},
            ]
        },
        "multiplicación": {
            "base": "Multiplicar es sumar varias veces.",
            "preguntas": [
                {"q": "3 x 2", "ops": ["5", "6", "7"], "r": "6"},
            ]
        },
        "división": {
            "base": "Dividir es repartir en partes iguales.",
            "preguntas": [
                {"q": "8 ÷ 2", "ops": ["4", "3", "5"], "r": "4"},
            ]
        },
        "fracciones": {
            "base": "Las fracciones representan partes de un todo.",
            "preguntas": [
                {"q": "1/2 significa", "ops": ["una parte", "dos partes", "tres"], "r": "una parte"},
            ]
        }
    },

    "Español": {
        "sustantivos": {
            "base": "Los sustantivos nombran personas, animales o cosas.",
            "preguntas": [
                {"q": "¿Cuál es sustantivo?", "ops": ["mesa", "correr", "grande"], "r": "mesa"},
            ]
        },
        "verbos": {
            "base": "Los verbos indican acciones.",
            "preguntas": [
                {"q": "¿Cuál es verbo?", "ops": ["correr", "mesa", "rojo"], "r": "correr"},
            ]
        },
        "adjetivos": {
            "base": "Los adjetivos describen características.",
            "preguntas": [
                {"q": "¿Cuál describe?", "ops": ["bonito", "correr", "mesa"], "r": "bonito"},
            ]
        }
    },

    "Ciencias": {
        "animales": {
            "base": "Los animales son seres vivos.",
            "preguntas": [
                {"q": "¿El perro es un animal?", "ops": ["sí", "no"], "r": "sí"},
            ]
        },
        "plantas": {
            "base": "Las plantas necesitan agua y sol.",
            "preguntas": [
                {"q": "¿Qué necesitan?", "ops": ["agua", "metal"], "r": "agua"},
            ]
        }
    },

    "Historia": {
        "prehistoria": {
            "base": "La prehistoria es el periodo antes de la escritura.",
            "preguntas": [
                {"q": "¿Había escritura?", "ops": ["no", "sí"], "r": "no"},
            ]
        }
    },

    "Inglés": {
        "colores": {
            "base": "Los colores en inglés son palabras para describir colores.",
            "preguntas": [
                {"q": "Red es", "ops": ["rojo", "azul"], "r": "rojo"},
            ]
        }
    },

    "Ética": {
        "valores": {
            "base": "Los valores son principios que guían nuestro comportamiento.",
            "preguntas": [
                {"q": "¿Respeto es un valor?", "ops": ["sí", "no"], "r": "sí"},
            ]
        }
    }
}