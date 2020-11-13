# Juego de ahorcado con ejercicio al azar matemático o teórico.
# El usuario tiene seis errores permitidos antes de perder y a cada error el dibujo se va completando

import random


def actualizar_score():
    try:
        proyecto = open("proyecto.csv", "r+", encoding="UTF-8")
        # El proyecto abre el archivo, si ya existe
    except:
        proyecto = open("proyecto.csv", "w", encoding="UTF-8")
        # Si el archivo no existe, lo crea

        proyecto.write("Nombre alumno, Puntaje\n")
        # Para darle formato al archivo

    else:
        proyecto.readline()

        proyecto.close()


def consultar_score():
    try:
        proyecto = open("proyecto.csv", "r", encoding="UTF-8")
        # El proyecto abre el archivo, si ya existe
    except:
        print("No se encontró un archvo existente de score")
    else:
        proyecto.readline()

        proyecto.close()


# Preguntas tipo PLANEA obtenidas del cuadernillo de Nuevo León
# Las preguntas son en variables para poder hacerlo random
pregunta1 = """En tres años Martín tendrá el doble de la edad que tenía hace un año. Si en cuatro años su prima
    Rosa tendrá tres veces la edad que tenía hace dos. ¿Cuál de los dos es el mayor? \n a= Martín es mayor \n b=Rosa es mayor \n c=tienen la misma edad"""
pregunta2 = "Encuentra el valor de x cuando: 3x-1=x+3"
pregunta3 = """Para comprar un boleto de lotería María aportó $10, Luis $8 y Lupita $7.
    El boleto resultó ganador de $30 000 y decidieron repartirlo proporcionalmente de acuerdo
    con lo que cada uno aportó para comprarlo. ¿Cuánto dinero le corresponde a Luis?"""
pregunta4 = """Una fotografía con 10 cm de ancho y 12 cm de ancho se amplió primero al doble de su tamaño
    y luego al cuádruple. ¿Cuál es la medida final de ancho de la fotografía?. """
pregunta5 = """Una ____ es una igualdad en la cual hay términos conocidos y términos desconocidos. El término
    desconocido se llama incógnita y se representa con letras"""
pregunta6 = """Un cono de papel reciclable para tomar agua mide 9 cm de altura y 5cm el radio de la base.
    ¿Cuál es el volumen aproximado del cono? Calcula pi con 3.14"""
pregunta7 = """Antes de encender un congelador el termómetro marcaba una temperatura de 25° y después de
    encenderlo durante cinco horas la temperatura bajó 33°. ¿Qué temperatura marcó el termómetro despues de estar
    encendido cinco horas?"""
pregunta8 = """A la hora del receso los estudiantes de manera inmediata y de manera indistinta. ¿Qué
    probabilidad tiene de salir primero un hombre? considerando que en el grupo hay 35 estudiantes y de ellos 22
    son mujeres y 13 son hombres. """
pregunta9 = """Los talonarios con boletos de una rifa se dividen en series: la primera series corresponde a los
    números del 1 al 145, la segunda serie del 146 al 290, la tercera serie del 291 al 435 y asi sucesivamente.
    ¿Cuál es el número de la séptima serie?"""
pregunta10 = """Un terreno de forma rectangular mide el doble de largo que de ancho. Si su área es de 98 metros
    cuadrados, ¿Cuáles son sus medidas?"""
pregunta11 = """La distancia Tierra-Sol, en el perihelio, es de 144.6 millones de kilómetros. ¿Cómo se expresa
    esta cantidad en notación científica?"""
pregunta12 = """La suma de las estaturas de Rosa, Julia y Lucero es de 4.5 m. La estatura de Rosa es de 1.49 y
    la de Julia 1.46 m. ¿Cuál es la estatura de Lucero?"""
# Lista de preguntas para que pueda ser random
lista_preguntas = [[pregunta1, pregunta2, pregunta3, pregunta4, ], [pregunta5, pregunta6, pregunta7, pregunta8],
                   [pregunta9, pregunta10, pregunta11, pregunta12]]
lista_respuestas = [["c", "2", "9600", "191"], ["ecuacion" or "ecuación", "235.5", "-8" or "-8°", "0.37"],
                    ["1015", "7,14" or "7 y 14", "1.466X10^8", "1.55"]]


def menu():
    # Presentar reglas del juego
    print("¡Bienvenido a Matemáticas ahorcadas!")
    print("El objetivo del juego es resolver la operación dado unos espacios.")
    print("El juego tiene las siguientes reglas: ")
    print("1. Solo puedes escoger un número o letra por intento. ")
    print("2. El muñequito cuenta de seis partes, por lo que tienes 6 intentos.")
    print("3. Si adivinas toda la palabra o número correcto antes de ser ahorcado ganas, de lo contrario pierdes.")
    print("4. Si repites una letra que ya habías dicho tienes derecho a otro intento.")
    opcion = input("¿Deseas empezar una partida o deseas salir?")
    return opcion


def utilities():
    global ganados
    global perdidos
    global total
    print("1. Guardar score")
    print("2. Checar score")
    print("3. Proseguir al juego")


def name():
    # Verificar nombre de usuario
    opciond = input("¿Es la primera vez que juegas?")
    if opcinod == "si" or opciond == "Si":
        proyecto.write(name)
    return opciond


def palabra_usuario(palabra):
    # Modifica los espacios del juego y agrega "espacios para escribir ---"
    lista_respuestas = list(palabra)
    for i in range(len(lista_respuestas)):
        separacion.append(lista_respuestas[i])
        lista_espacios.append(" _ ")


def verificacion_respuesta(letra):
    # Para verificar si la palabra/número esta dentro de la respuesta"
    if letra in respuesta:
        resultado = True
    else:
        resultado = False
    return resultado


def revelar_letra(letra):
    # Si el usuario ingresa correctamente el número o palabra, se despliega su "input"
    for i in range(len(separacion)):
        if separacion[i] == letra:
            lista_espacios[i] = letra


def dibujo(fallos):
    # Muestra el dibujo a partir de los fallos del usuario.
    if fallos == 0:
        print("""
                 __________
                |         |
                |         
                |        
                |        
                |
                |______
                \n""")
    elif fallos == 1:
        print("""
                     __________
                    |         |
                    |         0
                    |        
                    |        
                    |
                    |______
                    \n""")
    elif fallos == 2:
        print("""
             __________
            |         |
            |         0
            |         |
            |       
            |
            |______
            \n""")
    elif fallos == 3:
        print("""
                 __________
                |         |
                |         0
                |        /|
                |       
                |
                |______
                        \n""")
    elif fallos == 4:
        print("""
             __________
            |         |
            |         0
            |        /|\\
            |        
            |
            |______
                \n""")
    elif fallos == 5:
        print("""
                 __________
                |         |
                |         0
                |        /|\\
                |        / 
                |
                |______
            \n""")


opcion = menu()
opcion = opcion.lower()
ganados = 0
perdidos = 0
total = 0
while opcion == "empezar":
    separacion = []
    lista_espacios = []
    fallos = 0
    historial = ""
    rand_lista = random.randint(0, (len(lista_preguntas)) - 1)
    rand_elemento = random.randint(0, (len(lista_preguntas[rand_lista]) - 1))
    pregunta = lista_preguntas[rand_lista][rand_elemento]
    print(pregunta)
    respuesta = lista_respuestas[rand_lista][rand_elemento]
    palabra_usuario(respuesta)
    espacios = "".join(lista_espacios)
    dibujo(fallos)
    print(espacios)

    # Si el while llega a 6, se acabaría el juego. Sirve de condicion
    while espacios != respuesta and fallos < 6:
        letra = input("Ingresa una letra o número: ")
        # Prevenir repeticion de letra o número del usuario.
        while letra in historial:
            print("Esa letra ya la habías ingresado")
            letra = input("Ingresa una nueva letra: ")
        resultado = verificacion_respuesta(letra)
        if resultado == True:
            print("¡Es correcto!")
            revelar_letra(letra)
            espacios = "".join(lista_espacios)
            dibujo(fallos)
            print(espacios)
            historial += letra
        else:
            print("¡Incorrecto!")
            fallos += 1
            dibujo(fallos)
            print(espacios)
            historial += letra
    if fallos == 6:
        print("Lo lamento, has perdido :(")
        print("La respuesta era", respuesta)
        print("""
                 __________
                |         |
                |         0
                |        /|\\
                |        / \\
                |
                |______
                \n""")
        perdidos += 1
        total += 1
    else:
        print("¡Felicidades!, has ganado :)")
        # Para que se vaya sumando las jugadas ganadas
        ganados += 1
        total += 1
    opcion = input("Ingrese \"empezar\" si desea jugar una nueva partida.")
