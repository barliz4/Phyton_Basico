import csv 

preguntas = {}

with open ("datoschat.csv", "r") as archivo:
    lector = csv.DictReader (archivo)
    for fila in lector:
       preguntas [fila ["preguntas"]] = fila ["respuestas"]

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