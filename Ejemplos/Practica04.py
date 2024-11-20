
for num in range(0, 11, 2):
    print(num)

###

#Inicializamoslalistavacia
nombres = []
#funcióningresonombre
def ingreso(ele):
    for i in range(0,ele):
        m = input("Ingresar Nombre de la posición{0}:".format(i))
        nombres.append(m)
#Preguntamosdecuantoselementosconformanlalista
l = int(input("De cuantos elementos crearemos la lista de nombres:"))
ingreso(l)
print("\nla lista completade Nombres es:\n",nombres)

####


#Lista de Libros de Mario Vargas Llosa
obras_mvll=["La ciudad y los perros","La casa verde","Pantaleón y las visitadoras"]
#Lista Orden de los libros
orden=["primer","segundo","tercer"]
#Utlizamos `enumerate`
for i, libro in enumerate(obras_mvll):
    print("\nEl " + orden[i] +" libro de Mario Vargas Llosa es: " + libro)

############################

for f in ["Joel", "Nati", "Jehu", "Angeles", "Maryori", "Lucila", "Mirella", "Cesar"]:
    invitation = "Hola " + f + ".  ¡Por favor, ven a mi fiesta el sábado!"
    print(invitation)

###########################

def mysum(xs):
    """ Suma todos los números de la lista xs, y devuelve el total. """
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total
print(mysum([1, 2, 3, 4]))                   # ==>> 10
print(mysum([1.25, 2.5, 1.75]))              # ==>> 5.5
print(mysum([1, -2, 3]))                   # ==>> 2
print(mysum([1, 2, 3, 4]))                   # ==>> 10
print(mysum(range(11)))                     # ==>> 55
print(mysum([]))                            # ==>> 0
#####################################
# Programa que suma los elementos de una lista usando la función sum
m = [1, 2, 3, 4]
resultado = sum(m)
print(resultado)  # Salida: 10
##########################
# Programa que imprime los múltiplos de un número hasta 10
def multiplos(n):
    for i in range(1, 11):
        print(n * i, end="  ")
    print()

# Entrada del usuario
numero = int(input("Ingrese un número: "))
print(f"Los múltiplos de {numero} son: ")
multiplos(numero)
#####################
# Ejemplo de uso de for anidado: creación de tablas
for i in range(4):
    for j in range(4):
        for k in range(2):
            print(i, j, k)
############################
# Programa que calcula la raíz n-ésima de un número
numero = float(input("Ingrese un número: "))
for n in range(2, 101):
    raiz = numero ** (1 / n)
    print(f"La raíz {n}-ésima de {numero} es {raiz}")
################################
# Programa que verifica nombres y apellidos
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
simbolos = ['?', '!', '$', '%', '&', '/', 'ª', 'º']

def validar(cadena):
    for char in cadena:
        if char in numeros or char in simbolos:
            print("Nombre no válido!!!")
            return
    print("Nombre Correcto")

# Entrada de nombre y apellido
nombre = input("Ingrese su nombre: ")
validar(nombre)

apellido = input("Ingrese su apellido: ")
validar(apellido)
