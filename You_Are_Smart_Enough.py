import random
import time



#preparar los números de forma aleatoria
random1 =random.randint(1, 99)
random2 =random.randint(1, 99)
random3 =random.randint(1,3)

#Función de pregunta sumas
def suma (val1, val2):
    respuesta = val1+val2
    return respuesta

#Función de un temporizador obtenida de: https://www.wikihow.com/Make-a-Countdown-Program-in-Python
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("BOOM!!")


puntos = 0
print("Bienvenidos jugadores! Para superar la primera prueba deben conseguir 3 puntos mínimo")

print("Primera pregunta: Cuál es el átomo más chico de la tabla periódica?")
respuesta1 = str(input())


if respuesta1 == "H":
    print("Correcto")
    puntos = puntos + 1
    print("Tienes", puntos,"puntos")
else:
    print("Incorrecto")
    print("Tienes", puntos,"puntos")

print("Pregunta 2: Cuánto es 17 + 44?")

respuesta2 = int(input())
if respuesta2==(suma(17, 44)):
    print("Correcto")
    puntos = puntos + 1
    print("Tienes", puntos,"puntos")
else:
    print("Incorrecto")
    print("Tienes", puntos,"puntos")

print("Pregunta 3: Cuánto es", random1 ,"+ ", random2 ,"?")
respuesta2 = int(input())

if respuesta2 == (suma(random1 , random2)):
    print("Correcto!")
    puntos = puntos + 1
    print("Tienes ", puntos,"puntos")
else:
    print("Incorrecto")
    print("Tienes ", puntos,"puntos")

print("Pregunta 4: En qué número estoy pensando del 1 al 3?")
respuesta3 = int(input())

if respuesta3 == (random3):
    print("Correcto!")
    puntos = puntos + 1
    print("Tienes ", puntos,"puntos")
else:
    print("Incorrecto, yo estaba pensando en:", random3)
    print("Tienes ", puntos,"puntos")

if puntos >= 3:
    print("Felicidades por pasar a la segunda prueba, el código de acceso es: 42069")
else:
    print("No conseguiste los puntos necesarios")
    print("Tu computadora se autodestruirá en:")
    countdown(10)
    exit()

acceso = int(input())
if acceso == 42069:
    print("Acceso garantizado")
else:
    print("Acceso denegado, tu computadora se autodestruirá en:")
    countdown(10)
    exit()

dado_jugador = random.randint(1,20)
dado_computadora = random.randint(1,20)

print("Segunda fase: Pelea de dados")
print("Deberás probar suerte con un dado de 20 lados contra la computadora")
print("Pero antes de eso, responde esta pregunta para conseguir un dado de 5 lados de ventaja")
print("Redondo soy y es cosa anunciada, si a la derecha estoy algo valgo pero si a la izquierda estoy no valgo nada. Qué numero soy?")
respuesta_acertijo = int(input())

if respuesta_acertijo == 0:
    print("Felicidades, conseguiste el dado de 5 caras")
    d5 = random.randint(1,5)
else:
    print("Lo siento, no conseguiste nada")
    d5 = 0

def pelea_dados(var1, var2, d5):
    var1 = var1 + d5
    if var1 >= var2:
        resultado_dados = True
    else:
        resultado_dados = False
    return resultado_dados

resultado_dados = pelea_dados(dado_jugador, dado_computadora, d5)
if resultado_dados == True:
    print("Ganaste el duelo con una puntuación de: ", dado_jugador + d5,"Mientras que la computadora obtuvo: ", dado_computadora)
else:
    print("Haz perdido el duelo con una puntuación de:",dado_jugador + d5,"Mientras que la computadora obtuvo:",dado_computadora)
    print("Tu computadora se autodestruirá en:")
    countdown(10)
    exit()
