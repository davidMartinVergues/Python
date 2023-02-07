#Estructuras de control en Python
#Basicamene npython tenemos 2 tipos de estructiras las de decision y las iterativas
#Dentro de las estructiras de decision en python tenemos una unica instruccion de este tipo
#If - elif - else
#La forma basica es un unico if
# if CONDICION_EVALUABLE:
#   BLOQUE_CODIGO este codigo solo se ejcutara si la condicion es satifecha
numero = 5

if numero==10:
    print("El valor es igual a 10")

print("Fuera del if")

#Podemos tener un unico bloque else al final del if, que es optativo y se ejecutara en caso
#de que no se cumpla la codicion
numero = 5

if numero==10:
    print("El valor es igual a 10")
else:
    print("El valor no es 10")

print("Fuera del if")

#Ademas de esto en python podemos incluir despues del if mas condiciones, usando otro bloque
#optatyivo que es el bloque elif
numero = 5

if numero==10:
    print("El valor es igual a 10")
elif numero==1:
    print("El numero es igual a 1")
elif numero == 5:
    print("El numero es igual a 5")

print("Fuera del if")

#Podemos combinar todo lo anterior
numero = 50

if numero==10:
    print("El valor es igual a 10")
elif numero==1:
    print("El numero es igual a 1")
elif numero == 5:
    print("El numero es igual a 5")
else:
    print("El valor no es 10, ni es 1, ni es 5")

print("Fuera del if")

#Vamos a por las estructuras repetitivas
# Tenemos 2, for y while
# El for se utilza para recorrer iterables (tipos de datos que contienen otros datos), por
#ejemplo listas, tuplas, diccionarios, conjuntos y strings
#for VARIABLE_TEMP in ITERABLE:
lista = [1,2,3,4,5,6]

for numero in lista:
    print(numero)

#Con strings tambien funciona
cadena = "hola mundo"

for letra in cadena:
    print(letra)

#tuplas
lista = (1,2,3,4,5,6)

for numero in lista:
    print(numero)

#diccionarios
#Con esto solo devuelve las claves
diccionario = {"nombre":"Jane", "apellido":"Doe"}
for elemento in diccionario:
    print(elemento)

#si queremos las claves y los valroes hay truco
diccionario = {"nombre":"Jane", "apellido":"Doe"}
#Conel items, nos va adeolver la clave y el valor y las debemos asignar por ORDEN a dos variables
for key,value in diccionario.items():
    print(key)
    print(value)

#Python tiene un par de peculiaridades en las asignaciones
#asiganciones en cadena
var_1 = var_2 = var_3 = 1000
print(var_1, var_2, var_3)

#Ademas de esto tenemos el packing y unpacking
lista = [1,2,3]

var_1 = lista[0]
var_2 = lista[1]
var_3 = lista[2]

print(var_1, var_2, var_3)

#El packing y ubnpaking nos permite simplificar esto respecto a elementos iterables

var_1, var_2, var_3 = 1,2,3
print(var_1, var_2, var_3)

#con la lista
lista = [1,2,3]
var_1, var_2, var_3 = lista
print(var_1, var_2, var_3)

#Esto es elmotivo por el cual esto fncion
diccionario = {"nombre":"Jane", "apellido":"Doe"}
print( diccionario.items())

#Los for en python no estan pensados como en otros lenguajes para ir desde un valr a otro
#pero tenemos la funcion range que nos permite generar iterables para usarlos con el for
#y asi simular ese comportamiento
# range(VALOR_INICIAL, VALOR_FINAL, STEP)
#VALOR_INICIAL, valor optativo por defecto 0
#VALOR_FINAL, obligatorio y no es incluye en el rango generado
#STEP, es el salto entre valores generados
#Solo con el valor final obligatorio
for numero in range(10):
    print(numero)
#Con valor inicial y final
for numero in range(2,10):
    print(numero)
#Con todo
for numero in range(2,10,2):
    print(numero)

#El otro bucle es el while
# el whle se repite mientras se cumpla se cumpla la condicion
# while CONDICION:

numero = 1
#No se ejecuta porque no se cumple la condicion
while numero > 5:
    print(numero) 

#ahora "bien", ahora me he pasado al bucle inficto
numero = 1
while numero < 5:
    print(numero)

#Ahora si que si, tampoco ojo con la condcion
numero = 1
while numero < 5:
    print(numero)
    numero = numero - 1

#Lo importante es controlar correctamente la condicion de finalizacion que debe ser alcanzable
numero = 1
while numero < 5:
    print(numero)
    numero = numero + 1

#Los while y los for tienen un else
numero = 1
while numero < 5:
    print(numero)
    numero = numero + 1
else:
    print("Me ejecuto cuando se cumple la condicion")

for numero in range(10):
    print(numero)
else:
    print("ME ejecuto al acabar de iterar")

#Tenemos 3 palarbas reservadas, break, continue y pass
#el break es salida incondicional de un bucle
for numero in range(10):
    print(numero)
    break
#Puede ir con un if
for numero in range(10):
    print(numero)
    if numero ==3:
        break
#Ojo con el else
for numero in range(10):
    print(numero)
    if numero ==3:
        break
else:
    print("Ha terminado")

#El continue nos lleva de nuevo a la estructura de control

numero = 1
while numero < 5:
    print(numero)
    continue
    numero = numero + 1
else:
    print("Me ejecuto cuando se cumple la condicion")

#se puede combinar con un  if
numero = 1
while numero < 5:
    numero = numero + 1

    if numero ==3:
        print(numero)
    else:
        continue
    print("Iteramos")
else:
    print("Me ejecuto cuando se cumple la condicion")

#La palabra reservada pass es la instruccion vacia no hace nada
for numero in range(10):
    pass

#Leer valores por teclado en Python
#Para esto Python nos da la funcion input()
# variable = input("PROMT")
cadena = input("Introduce una cadena ")
print(cadena)

#Ojo con los tipos de datos, el input SIEMPRE devuleve un string, independientemente de los valores
#que le introduzcamos
numero = input("Introduce un numero ")
print(numero)
print(type(numero))
if(numero == 1):
    print("Numero vale 1")
else:
    print("Numero no vale 1")

#Si queremos leer un numero debemos convertirlo, para ello en python tenems funciones que se llaman
#igual que el tipo de dato para hacer las conversiones, int(), float(), str(), bool(), complex()
#Por ejemplo si queremos leer un entero
cadena = input("Introduce el numero ")
numero = int(cadena)
print(type(numero))

#Se puede hacer mas resumida asi:
numero = int(input("Introduce un numero "))
print(type(numero))
