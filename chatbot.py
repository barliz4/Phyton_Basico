preguntas = {
    "hola":"hola como estás",
    "bien y tu":"también muy bien",
    "tiene cursos de programacion":"si",
    "donde estan ubicados":"en la ciudad de bucaramanga"
}


def respuestas (pregunta):
    if pregunta in preguntas:
        respuesta = preguntas [preguntas]
    else:
        respuesta = "No entendi tu pregunta"
    return respuesta

print ("Hola soy un bot, en versión 0.0.0.1")

while True:
    pregunta = input ("En que puedo ayudarte?")
    if pregunta == "salir":
        break
    print (respuestas(pregunta))