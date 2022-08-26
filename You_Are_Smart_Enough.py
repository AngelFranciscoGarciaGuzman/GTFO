import random

#preparar los números de forma aleatoria
a=random.randint(1, 99)
b=random.randint(1, 99)
c=random.randint(1,3)


puntos = 0
print("Bienvenidos jugadores!")

pregunta1 = (input("Primera pregunta: Cuál es el átomo más chico de la tabla periódica?"))

if pregunta1 == "H":
    print("Correcto")
    puntos = puntos + 1
    print("Tienes", puntos,"puntos")

else:
    print("Incorrecto")
    print("Tienes", puntos,"puntos")

#función de pregunta de 
def preguntamate (val1, val2):
    respuesta = val1+val2
    return respuesta

print("Pregunta 2: Cuánto es 17 + 44?")

respuestamate = int(input())
if respuestamate==(preguntamate(17, 44)):
    print("Correcto")
    puntos = puntos + 1
    print("Tienes", puntos,"puntos")
else:
    print("Incorrecto")
    print("Tienes", puntos,"puntos")

print("Pregunta 3: Cuánto es", a,"+ ", b," ?")
respuestamate2 = int(input())

if respuestamate2 == (preguntamate(a, b)):
    print("Correcto!")
    puntos = puntos + 1
    print("Tienes ", puntos,"puntos")
else:
    print("Incorrecto")
    print("Tienes ", puntos,"puntos")

print("Pregunta 4: En qué número estoy pensando del 1 al 3?")
respuestarandom = int(input())

if respuestarandom == (c):
    print("Correcto!")
    puntos = puntos + 1
    print("Tienes ", puntos,"puntos")
else:
    print("Incorrecto")
    print("Tienes ", puntos,"puntos")

print("Fin de la demo, gracias por jugar!")