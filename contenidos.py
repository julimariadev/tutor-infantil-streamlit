# contenidos.py

def explicacion_larga(base, edad, tema, materia):
    if edad == "6-7 años":
        return f"""
🌟 Tema: {tema}

{base}

Vamos a aprenderlo paso a paso como si fuera un juego.

📚 Este tema pertenece a {materia} y es importante porque aparece en muchas cosas que ves todos los días.

👀 Puedes imaginar ejemplos en tu casa, en el colegio o jugando.

💡 No te preocupes si no entiendes a la primera, aprender es intentar varias veces.
"""

    elif edad == "8-9 años":
        return f"""
🌟 Tema: {tema}

{base}

Este tema de {materia} te ayudará a entender mejor el mundo.

📚 Lo puedes usar en tareas, ejercicios y situaciones reales.

🧠 Es importante pensar en ejemplos y practicar para comprenderlo bien.

💡 Mientras más practiques, más fácil será dominarlo.
"""

    else:
        return f"""
🌟 Tema: {tema}

{base}

Este tema pertenece a {materia} y es fundamental para desarrollar habilidades de análisis y comprensión.

📚 Se utiliza en diferentes áreas del conocimiento.

🧠 Comprenderlo te permitirá resolver problemas más complejos.

💡 Es importante analizar, practicar y reflexionar sobre lo aprendido.
"""

MATERIAS = {

# =========================
# MATEMÁTICAS
# =========================
"Matemáticas": {
    "sumas": {"base": "La suma consiste en juntar cantidades."},
    "restas": {"base": "La resta consiste en quitar cantidades."},
    "multiplicación": {"base": "Multiplicar es sumar varias veces."},
    "división": {"base": "Dividir es repartir en partes iguales."},
    "fracciones": {"base": "Las fracciones representan partes de un todo."},
    "decimales": {"base": "Los decimales representan partes más pequeñas que un entero."},
    "porcentajes": {"base": "El porcentaje representa una parte de 100."},
    "ecuaciones": {"base": "Las ecuaciones son igualdades con valores desconocidos."},
    "potencias": {"base": "Las potencias representan multiplicaciones repetidas."},
    "raíces": {"base": "Las raíces buscan el número que multiplicado da otro."},
    "probabilidad": {"base": "La probabilidad mide la posibilidad de que ocurra algo."},
    "estadística": {"base": "La estadística analiza datos."},
    "ángulos": {"base": "Los ángulos miden la apertura entre dos líneas."},
    "perímetro": {"base": "El perímetro es la suma de los lados."},
    "área": {"base": "El área mide la superficie de una figura."}
},

# =========================
# ESPAÑOL
# =========================
"Español": {
    "sustantivos": {"base": "Los sustantivos nombran cosas."},
    "verbos": {"base": "Los verbos indican acciones."},
    "adjetivos": {"base": "Los adjetivos describen características."},
    "sinónimos": {"base": "Los sinónimos significan lo mismo."},
    "antónimos": {"base": "Los antónimos son opuestos."},
    "pronombres": {"base": "Los pronombres reemplazan nombres."},
    "conectores": {"base": "Los conectores unen ideas."},
    "oraciones": {"base": "Las oraciones expresan ideas completas."},
    "párrafos": {"base": "Los párrafos organizan ideas."},
    "tildes": {"base": "Las tildes indican la pronunciación."},
    "puntuación": {"base": "La puntuación organiza el texto."},
    "lectura": {"base": "La lectura permite comprender textos."},
    "escritura": {"base": "La escritura expresa ideas."},
    "comunicación": {"base": "La comunicación transmite mensajes."},
    "narración": {"base": "La narración cuenta historias."}
},

# =========================
# CIENCIAS
# =========================
"Ciencias": {
    "animales": {"base": "Los animales son seres vivos."},
    "plantas": {"base": "Las plantas necesitan agua y sol."},
    "cuerpo humano": {"base": "El cuerpo humano tiene órganos."},
    "ecosistemas": {"base": "Los ecosistemas son sistemas naturales."},
    "energía": {"base": "La energía permite el movimiento."},
    "materia": {"base": "La materia ocupa espacio."},
    "átomos": {"base": "Los átomos son partículas pequeñas."},
    "fuerzas": {"base": "Las fuerzas producen movimiento."},
    "gravedad": {"base": "La gravedad atrae objetos."},
    "clima": {"base": "El clima describe el tiempo."},
    "agua": {"base": "El agua es vital para la vida."},
    "aire": {"base": "El aire es necesario para respirar."},
    "electricidad": {"base": "La electricidad produce energía."},
    "luz": {"base": "La luz permite ver."},
    "sonido": {"base": "El sonido es una vibración."}
},

# =========================
# HISTORIA
# =========================
"Historia": {
    "prehistoria": {"base": "La prehistoria es antes de la escritura."},
    "edad antigua": {"base": "La edad antigua incluye civilizaciones."},
    "edad media": {"base": "La edad media es un periodo histórico."},
    "edad moderna": {"base": "La edad moderna trae cambios importantes."},
    "edad contemporánea": {"base": "La edad contemporánea es actual."},
    "independencia": {"base": "La independencia libera países."},
    "colonización": {"base": "La colonización implica dominio."},
    "revoluciones": {"base": "Las revoluciones cambian sistemas."},
    "imperios": {"base": "Los imperios dominan territorios."},
    "cultura": {"base": "La cultura incluye costumbres."},
    "sociedad": {"base": "La sociedad organiza personas."},
    "economía": {"base": "La economía gestiona recursos."},
    "política": {"base": "La política organiza el poder."},
    "guerras": {"base": "Las guerras son conflictos."},
    "paz": {"base": "La paz evita conflictos."}
},

# =========================
# INGLÉS
# =========================
"Inglés": {
    "colores": {"base": "Los colores describen cosas."},
    "números": {"base": "Los números indican cantidad."},
    "saludos": {"base": "Los saludos inician comunicación."},
    "verbos": {"base": "Los verbos indican acciones."},
    "animales": {"base": "Los animales tienen nombres en inglés."},
    "comida": {"base": "La comida tiene vocabulario."},
    "familia": {"base": "La familia tiene palabras específicas."},
    "escuela": {"base": "La escuela tiene vocabulario."},
    "ropa": {"base": "La ropa tiene nombres."},
    "tiempo": {"base": "El tiempo se expresa en inglés."},
    "días": {"base": "Los días tienen nombres."},
    "meses": {"base": "Los meses organizan el año."},
    "preguntas": {"base": "Las preguntas ayudan a conversar."},
    "respuestas": {"base": "Las respuestas completan ideas."},
    "pronombres": {"base": "Los pronombres reemplazan nombres."}
},

# =========================
# ÉTICA Y RELIGIÓN
# =========================
"Ética": {
    "valores": {"base": "Los valores guían el comportamiento."},
    "respeto": {"base": "El respeto es fundamental."},
    "responsabilidad": {"base": "La responsabilidad implica cumplir."},
    "honestidad": {"base": "La honestidad es decir la verdad."},
    "solidaridad": {"base": "La solidaridad ayuda a otros."},
    "justicia": {"base": "La justicia busca equilibrio."},
    "empatía": {"base": "La empatía entiende a otros."},
    "convivencia": {"base": "La convivencia permite vivir juntos."},
    "normas": {"base": "Las normas organizan conducta."},
    "derechos": {"base": "Los derechos protegen personas."},
    "deberes": {"base": "Los deberes son responsabilidades."},
    "libertad": {"base": "La libertad permite elegir."},
    "paz": {"base": "La paz evita conflictos."},
    "tolerancia": {"base": "La tolerancia acepta diferencias."},
    "amor": {"base": "El amor conecta personas."}
}

}