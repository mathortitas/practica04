def imprimir_pares(inicio, fin):
    for num in range(inicio, fin + 1):
        tipo = "par" if num % 2 == 0 else "impar"
        print(f"{num} es {tipo}")

inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el número final: "))
imprimir_pares(inicio, fin)

####################################3

def imprimir_tabla(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
imprimir_tabla(numero)

#####################################3

numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
simbolos = ['?', '!', '$', '%', '&', '/', 'ª', 'º']

def validar_nombre(cadena):
    for char in cadena:
        if char in numeros or char in simbolos:
            return False
    return True

def solicitar_nombre(tipo):
    while True:
        cadena = input(f"Ingrese su {tipo}: ")
        if validar_nombre(cadena):
            print(f"{tipo.capitalize()} válido: {cadena}")
            return cadena
        else:
            print(f"{tipo.capitalize()} no válido. Inténtelo nuevamente.")

nombre = solicitar_nombre("nombre")
apellido = solicitar_nombre("apellido")

positivas = ["bueno", "excelente", "bien"]
negativas = ["malo", "pesimo", "no"]
############################
def verificar_comentario(comentario):
    es_positivo = any(palabra in comentario.lower() for palabra in positivas)
    es_negativo = any(palabra in comentario.lower() for palabra in negativas)
    if es_positivo:
        print("Comentario POSITIVO")
    elif es_negativo:
        print("Comentario NEGATIVO")
    else:
        print("Comentario NEUTRAL")

comentario = input("Ingrese el comentario: ")
verificar_comentario(comentario)

#####################
#usare la lib random 
import random
def generar_listas():
    numeros = [random.randint(1, 100) for _ in range(60)]
    multiplos_2 = [n for n in numeros if n % 2 == 0]
    multiplos_3 = [n for n in numeros if n % 3 == 0]
    multiplos_5 = [n for n in numeros if n % 5 == 0]
    return multiplos_2, multiplos_3, multiplos_5

multiplos_2, multiplos_3, multiplos_5 = generar_listas()
print("Múltiplos de 2:", multiplos_2)
print("Múltiplos de 3:", multiplos_3)
print("Múltiplos de 5:", multiplos_5)

#############################
def es_capicua(numero):
    return str(numero) == str(numero)[::-1]

def verificar_rango_capicua(inicio, fin):
    for num in range(inicio, fin + 1):
        if es_capicua(num):
            print(f"{num} es capicúa")
        else:
            print(f"{num} no es capicúa")

inicio = int(input("Ingrese un número inicial (3 cifras): "))
fin = int(input("Ingrese un número final (4 cifras): "))
verificar_rango_capicua(inicio, fin)


#####################
def validar_dni(dni):
    if len(dni) == 8 and dni.isdigit():
        return True
    return False

def solicitar_dni():
    while True:
        dni = input("Ingrese su DNI (8 dígitos): ")
        if validar_dni(dni):
            print("DNI válido:", dni)
            break
        else:
            print("DNI no válido. Inténtelo nuevamente.")

solicitar_dni()


