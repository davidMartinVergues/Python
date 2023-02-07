#Repaso general
#Reglas de identificacion de variables
#No pueden empezar por numeros
#Solo pueden empezar por letras o "_", no pueden empezar por numeros o simbolos
#Tampoco puede ser una palabra reservada (acordaroes uqe sonmuy poquitas)
1variable = 1
$variable = 1
@variable = 1
variable_1 = 1

#Tipos simples,enteros, flotantes, complejos, booleanos, None, son inmutables
#Tipos complejos, string (inmutable), listas, tuplas(inmutable), diccionarios, conjuntos, los demas son mutables
#Tanto las listas como las tuplas, pueden almacenar cualquier tipo de objeto en python
#las listaspueden listas dentro (matriz), olas listaspueden tener tuplas
#Acordaros que los strings, son inmutable como las tuplas, asi que no se comportan como las listas
#eso significa que una vez credas no podemos añadir mas elementos
#Se puede hacer slicing
cadena = "Hola mundo"
print(cadena[:2])
#Se pueden concatnear aunque el resultado es un nuevo stirng
cadena = cadena + "Adios"
print(cadena)
#Al ser inmyable no podemos hacer lo siguiente:
cadena[0]="H"

#Slices CADENA[POS_INICIAL, POS_FINAL, STEP]
cadena = "Hola mundo"
print(cadena[1:-2]) #Funciona y se carga la primera y las dos ultimas

#Diccionarios
diccionario = {"clave":12}
diccionario = {"clave":12, "clave_2":24}
diccionario = {1:12}
diccionario = {1:12,2:34}

#Operadores logicos and, or y not
#Operadores a nivel de bits(bitwise) & (And), |(or), ~(not), ^(exor), << (desplazamiento hacia la izquierda), >> (desplazamiento a la derecha 
#numero = 0b101
#Es como multiplicar
#print(numero << 5)
#print(bin(numero << 5))
#Es como dividir:
#print(numero >> 1)
#print(bin(numero >> 1))

#Flotantes
#OJO con el truncado
matematica = 1.23e2 #es como multplicar por 10 elevado a este numero
print(matematica)
matematica = 1.23e-2 #es comdo dvidir por 10 elevado a este numero
print(matematica)

#Diferencia entre find e index
cadena = "Hola Mundo"
#Si esta lo que bscamos es igual
print(cadena.find("M"))
print(cadena.index("M"))

#Sino
cadena = "Hola Mundo"
print(cadena.find("z")) #-1
print(cadena.index("z")) #Error

#Sort
#Solo numeros enteros OK
lista = [34,5,2,1]
lista.sort()
print(lista)

#Enteros y decimales OK
lista = [34,5,2,1,6.5,9.0]
lista.sort()
print(lista)

#Enteros, decmales y complejos ERROR
lista = [34,5,2,1,6.5,9.0,4j]
lista.sort()
print(lista)

#Strings solo OK
lista = ["z","f","a","e"]
lista.sort()
print(lista)

#Numeros  + strings ERROR
lista = [34,5,2,1,"a","b"]
lista.sort()
print(lista)
