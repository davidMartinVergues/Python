#Tipos de datos en Python
#para crear un comentario debemos poner # y a partir de ese momento el interprete ignora
#lo que pongamos
#Para crear una variable en python es tan sencillo, como 
# IDENTIFICADOR_VARIABLE = VALOR
variable = 1
#Lo identificadores en python deben cumplir ciertas normas:
#Solo pueden comenzar por letras o guiones bajos
_variable = 1
variable = 1
#No son validos
# 1variable = 1
# $variables = 1
#Y sin embargo si es valido si los numeros estan en el cuertpo
variable_1 = 1

#Es python un lenguaje tipado?
#Para ver el tipo de una variable tenemos la funcion type(variable)
#para imprimier algo por pantalla tenemos la funcion print()
#las podemos combinar para ver los tipos
# print(type(VARIABLE))
numero = 1
print(type(numero))
#Desde el punto de vista de sintaxis python es no tipado, pero a nivel interno es fuertemente 
#tipado, a nivel interno hace algo el DuckTyping

#Tipos primitivos
#Enteros
numero = 1
print(type(numero))

#Rango de valores de un entero
#No tienen un rango
numero = 1266666666666666666662388888888888888888888219999999999999999999000000000000000011111111111111888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
print(type(numero))
print(numero)

#Mas enteros podemos trabajar en diferentes base numericas
numero = 101
print(type(numero))
print(numero)

#Hexadecimal basicamente tenemos del 0 al 9 y de A - F, es decir 16 valores
numero = 0x101
print(type(numero))
print(numero)
#Algoritmo de conversion
#primero separamos las cifras y las sumamos
# 0x101 = 1 + 0 + 1
#Multiplicamos las cifras por la base
# 0x101 = 1 * 16 + 0 * 16 + 1 * 16
#Tercer paso elevamos la base a la posicion que ocupa desde la 0 de derecha a izquierda
# 0x101 = 1 * 16**2 + 0 * 16**1 + 1 * 16** 0
#Hacemos la cuenta
# 0x101 = 256 + 0 + 1 = 257
#Octal teneoms 0 - 7 es decir 8 valores
numero = 0o101
print(type(numero))
print(numero)

#Binario tenemos 0-1 es decir 2 valores
numero = 0b101
print(type(numero))
print(numero)
# 0b101 = 1*2**2 + 0*2**1 + 1*2**0
# 0b101 = 4 + 0 + 1 = 5

#Flotantes
flotante = 1.2
print(type(flotante))
print(flotante)

#Admiten notacion cientifica es de eEXPONENTE
# que basicamente usa de base 10 y es el elevado a loq ue le indiquemos
flotante = 1.2e3 #aqui equivale a 1.2 * 10**3
print(type(flotante))
print(flotante)

#Puede ser negativo el exponente, aqui divide no multiplica
flotante = 1.2e-3 #equiva a 1.2/10**3
print(type(flotante))
print(flotante)

#Rango de valores, tiene precision maxima de 16 decimales y OJO no da error
#simplemente acorta y listo
flotante = 1.88888888888888888899999999999999999999999999999999999944444444444444444444477777777777777777777773333333333333333333333
print(type(flotante))
print(flotante)

#Operaciones basicas
#OJO CON LOS REDONDEOS
print(1.1 + 2.2)
print(0.1 + 0.1 + 0.1 - 0.3)

#Complejos
complejo = 3 + 4j
print(type(complejo))
print(complejo)

#Mutabilidad e inmutabilidad de las variables
numero = 1
print(numero)
numero = 100
print(numero)

#Las variables por defecto son INMUTABLES
#en python a nivel de memoria todo lo que almacenamos en la memoria tiene un id unico
#tenemos una funcion id() que nos devuelve ese numero
numero = 1
print(id(numero))
numero = 100
print(id(numero))

#OJO con la memoria
numero = 1
numero_2 = 1
print(id(numero))
print(id(numero_2))
numero_2 = 100
print(id(numero))
print(id(numero_2))

numero = 1
numero_2 = 1
print(id(numero))
print(id(numero_2))
print(id(1))

#Tenemos los tipos booleanos (bool)
verdadero = True
falso = False

#Es caseSensitive, diferencias mayusculas de minusculas
# tenemos lo que se conoce como un conjunto de conectivas completo
# and, or y not
#And solo es verdad si y solo si ambos operandos son verdad
print(False and False)
print(False and True)
print(True and False)
print(True and True)
#Or es verdadero si al menos uno de los operandos es verdadero
print(False or False)
print(False or True)
print(True or False)
print(True or True)

#El operador unario not, qeu es la negacion
print(not True)
print(not False)

#Operadores de comparacion
#==, >=, >, <=, <, !=
print(1==1)
print(1>=1)
print(1>1)
print(1<=1) 
print(1<1)
print(1!=1)

#Ejemplos
print(False and False or True)
print(True or False and False)
print(0 and not 1 or 1 and not 0 or 1 and 0)
#Tenemos las llamadas operaciones cortocircuitadas, se ve muy claramane con el siguiente ejemplo
#si es capaz de determinar el resultado de una operacion al princpio no evalua el resto
print(1/0)
print(1 and 1/0)
print(1 or 1/0)

#Operadores binarios
# & (and), | (or), ~ (not) y ^ (exor)
print(0 & 0)
print(0 & 1)
print(1 & 0)
print(1 & 1)

# | or
print(0 | 0)
print(0 | 1)
print(1 | 0)
print(1 | 1)

# ~ not
print(~1)
print(~0)

#Como funciona esto realmente
a = 4
b = 5
print(a & b)
print(a | b)

#Lo que hace es convertir a binario e ir comparando bit a bit
#   a = 4
#   b = 5
#   4 => 0b100
#   5 => 0b101
#4 & 5 = 0b100 => 4
#4 | 5 = 0b101 => 5

#Para representar numeros negativos tenemos varias formas en binario
#La primera es signo magnitud, basicamente se añade un 0 al principio del numero
# entiendiend por el principio la izquierda si es positivo
# y un uno si es negatvo
# + 5 => 0101
# - 5 => 1101
#Tenemso un problema el doble 0
# 0 = 0
# +0 = 00
# -0 = 10
#Complemento a uno, lo que nos indica es que para representar un numero en negativo
#hacemos el complemento, basicamente es negar bit a bit
# 5 = 0101
#-5 = 1010
#Pero tenemos un problema
#  0 = 00
# -0 = 11
# Complemento a dos
# Hacemos el complemento a uno del numero y al resultado le sumamos uno
#  5 = 0101
#  5 = 1010
#  1 = 0001
# -5 = 1011
#No tenemos +0 y -0
#  0 => 0000
#  0 => 1111
#  1 => 0001
# -0 => 0000

#Python tiene una peculiaridad a la hroa de imprimir internamente trabaja en C2
print(bin(0))
print(bin(~0))
print(bin(1))
print(bin(~1))
print(bin(2))
print(bin(~2))
print(bin(3))
print(bin(~3))
print(bin(4))
print(bin(~4))
print(bin(5))
print(bin(~5))



# ^ (exor)
print(0 ^ 0)
print(0 ^ 1)
print(1 ^ 0)
print(1 ^ 1)

#Se usa mucho para los cifrados
mensaje = 5
clave = 6
cifrado= 5 ^ 6
print(cifrado)
desrifrar = cifrado ^ clave
print(desrifrar )

#Strings
#Son un tipo de dato que representa un conjunto ordenado de caracteres
#y que ademas son INMUTABLES
cadena = "Hola Mundo"
print(type(cadena))
print(cadena)

#Tenemos 4 formas de definir los stings
#Opcion 1 - Comillas dobles
str_1 = "Hola Mundo" 
print(type(str_1))
print(str_1)

#Opcion 2 - Comillas simples
str_2 = 'Hola Mundo'
print(type(str_2))
print(str_2)

#Opcion 3 - Comillas triples dobles
str_3 = """Hola Mundo""" 
print(type(str_3))
print(str_3)

#Opcion 4 - Comillas triples simples
str_4 = '''Hola Mundo'''
print(type(str_4))
print(str_4)

#La explicacion son 2 cosas
#El primer caso es si tenemos que poner comillas dentro de comillas
string = "Hola 'Mundo'"
print(string)
string = 'Hola "Mundo"'
print(string)

#Las comillas triples tanto las simples como las dobles, habilitan la sintaxis HEREDOC
#Basicamente hace referencia a los string multilinea
string = """En un lugar de la mancha
de cuyo nombre no quiero acordarme.."""
print(string)

#PAra meter caracteres como el salto de linea o el retorno de carro usamos la anotacion
# basada en el escae de caracteres especiales \n salto de linea \r retorno de carro \t tabulacion
string = "En un lugar de la mancha\nde cuyo nombre no quiero acordarme.."
print(string)

#Con las comillas triples no precisamos esto
string = """En un lugar de la mancha
de cuyo nombre no quiero acordarme.."""
print(string)

#RECORDAD SON INMUTABLES
#Uan vez creadas NO podemos manipular valores individuales
cadena = "hola mundo"
cadena[0]= "H"
print(cadena)

#No onstante si podemos cambiar todo el string
cadena = "hola mundo"
cadena = "adios mundo"
print(cadena)

#PAra acceder a los caracteres de una cadena, lo podemos hacer por posicion 
#CADENA[POS]
#la posicion comienza a contar en 0 y tenemos hasta la longitud -1 de la cadena
#tenemos una funcion len(CADENA), nos devuelve la longitud de una cadena
#si intentamos acceder a una posicion que no existe da error
cadena = "Hola Mundo"
print(len(cadena))

#Tambien tenemos el conocido como slicing, que es la obtencion de subcojunconjuntos de datos
#en elementos iterables
# En los strings es basicamente una forma de obtener subcadenas de una cadena dada
# CADENA[POS_INICIAL:POS_FINAL:STEP]
#POS_INICIAL, es desde donde pillamos el substring (por defecto es 0)
#POS_FINAL, es hasta donde tenemos el substring IMPORTANTE no se 
# inculye en el slice esta posicion (por defecto es longitud del string)
#STEP, es el paso para recorrer el string (por defecto es 1)
cadena = "Hola Mundo"
print(cadena[0:6:1]) #Hola M
cadena = "Hola Mundo"
print(cadena[2:6:1]) #la M
cadena = "Hola Mundo"
print(cadena[0:10:1]) #Hola Mundo
cadena = "Hola Mundo"
print(cadena[0:10:2]) #Hl ud
cadena = "Hola Mundo"
print(cadena[::]) #es una copia de la cadena dado lso valores por defecto [0:longitud:1]

#Ademas de esto los slices no comprueban lso limites
cadena = "Hola Mundo"
print(cadena[10000000000000000::]) #cadena vacia
cadena = "Hola Mundo"
print(cadena[:88888888888888:]) #toda la cadena
cadena = "Hola Mundo"
print(cadena[::88888888888888]) #primer elemento

#Los strings en python admiten indices negativos
#Los indices negativos se cuentan desde el final de la cadena
#y su rango de valores es desde -1 hasta -longitud
cadena = "Hola Mundo"
print(cadena[-1])
print(cadena[-10])

#Los slicing tambien pueden ser negativos
cadena = "Hola Mundo"
print(cadena[-1:-5:]) #cadena vacia porque no podemos ir desde -1 a -5 sumandole uno
cadena = "Hola Mundo"
print(cadena[-1:-5:-1]) #esto da la subcadena odnu porque va desde -1 a -5 restando de uno en uno
cadena = "Hola Mundo"
print(cadena[::-1]) #Invertir una cadena

#Los strings tienen una serie de metodos que nos permiten realizar ciertas operaciones con ellos
# CADENA.METODO(PARAMS)
cadena = "           Hola Mundo               "
print(len(cadena))
print(cadena)

#Tenemos 3 metodos para devolver una COPIA de la cadena sin los espacios
#strip() eliminar los espacios por delante y por detras
cadena = "           Hola Mundo               "
print(len(cadena.strip()))
print(cadena.strip())

#Con rstrip solo los de la derecha
cadena = "           Hola Mundo               "
print(len(cadena.rstrip()))
print(cadena.rstrip())

#con lstrip los de la izquierda
cadena = "           Hola Mundo               "
print(len(cadena.lstrip()))
print(cadena.lstrip())

#Admiten un parametro que es opcional que es caracter a eliminar por defecto es el espaio en blanco
cadena = "@@@@@@@@@@@@@Hola Mundo@@@@@@@@@@@@"
print(len(cadena.strip("@")))
print(cadena.strip("@"))

#Tenemos tambien funciones de busqueda para determinar si un substring esta dentro de otro
#el primero es el operador "in"
print("ola" in "hola")
#Tenemos 2 metodos para retornar la posicion de la primera ocurrencia del substring dentro del sting princpipal
#CADENA.index(SUBSTRING)
cadena = "hola mundo"
print(cadena.index("mundo"))
#CADENA.find(SUBSTRING)
cadena = "hola mundo"
print(cadena.find("mundo"))

#La diferencia entre estos dos metodos es que sucede cuando no encuentra el string
cadena = "hola mundo"
print(cadena.index("adios")) #devuelve error si no existe el substring
print(cadena.find("adios")) #devuelve -1 si no existe

#Tambien una serie de metodos para comprobar condiciones sobre la cadena,estos
#devolveran True o False en funcionde si se cumpen o no
cadena = "Hola mundo"
# isupper() devuelve true si esta toda la cadena en mayusculas
print(cadena.isupper())
# islower()devuelver true si esta todo en minusculas
print(cadena.islower())
#Si todo son numeros (solo enteros)
# isnumeric()
cadena = "1234"
print(cadena.isnumeric())

# isalpha(), solo si es alfanumerico (es decir no numeros)
cadena = "1234"
print(cadena.isalpha())

#Listas
#Es un conjunto ordenado de elementos que pueden ser heterogeneos, es decir de cualquier tipo
#Para declarar las listas en python tenemos 2 maneras
# NOMBRE_LISTA = list()
#la segunda
# NOMBRE_LISTA = []
lista = []
print(type(lista))
print(lista)

lista_2 = list()
print(type(lista_2))
print(lista_2)

#Podemos inicializarlas con valores
lista = [1,2,3,4,5,6]
print(type(lista))
print(lista)

#Podemos acceder a los elementos de las listas de la misma forma que accedemos
#a lo elementos de un string
lista=[1,2,3,4,5,6]
print(lista[0])

#Las listas son MUTABLES a diferencia de lso tipos que hemos visto hasta ahora
lista=[1,2,3,4,5,6]
lista[0]="hola"
print(lista)

#Al ser mutable podemos añadir y eliminar elementos
#para añadir elementos a una lista tenemos 2 formas
# la primera es el metodo append()
# LISTA.append(VALOR)
#lo que hacer es añadir el valor al FINAL de lista
lista = [1,2,3,4]
lista.append("hola")
print(lista)
#La segunda forma de añadir elementos es con el metodo insert
# LISTA.insert(POS,VALOR)
#este metodo añade el elemento en la posicion que le indiquemos, ojo no borra los otros elementos
#sino que los desplazara
lista = [1,2,3,4]
lista.insert(1,"hola")
print(lista)

#Para borrar tenemos 2 formas
#la primera es usando el operador del y la posicion
lista = [1,2,3,4]
del lista[1]
print(lista)

#La segunda forma es con los metodos propios de las llistas
#el metodo remove() elimina la primera ocurrencia del valor en la lista
# LISTA.remove(VALOR)
lista = [1,2,3,4,5]
lista.remove(2)
print(lista)

#tambien soporta el uso de slices como los string solo que en este caso devuelve sublistas
lista = [1,2,3,4,5,"a","b","c"]
print(lista[0:3:2])

lista = list(range(101)) #lista con valores de 0 a 100
#Queremos lo siguiente usando slices:
#devolver los numeros pares
print(lista[0:101:2])
print(lista[::2])
#devolver los numeros impares
print(lista[1:101:2])
print(lista[1::2])
#invertir la lista
print(lista[::-1])
print(lista[-1:-102:-1])
#conseguir los ultimos 10 numeros en orden inverso
print(lista[-1:-11:-1])
print(lista[100:90:-1])
print(lista[len(lista)-1:len(lista)-11:-1])
#conseguir los ultimos 10 numeros en orden natural
print(lista[91:101:1])
print(lista[len(lista)-10::])
print(lista[-10::])
#conseguir los primeros 50 numeros
print(lista[0:50:1])
print(lista[:50:])

#Las listas tienen funciones y metodos que se les pueden aplicar
# a las listas le podemos aplicar la funcion len() nos develve el numero de lemeentos de una lista
lista = [1,2,3,4,5]
print(len(lista))

#enems las funciones para lstas numericas
# sum(LISTA) devuelve la suma
# max(LISTA) devueleve el valor mas alto
# min(LISTA) devuelve el valor ma bajo

lista =[1,4,235,678,9]
print(sum(lista))
print(max(lista))
print(min(lista))

#Tenemso metodos de interes
# el metodo sort() nos devuelve la lista ordenada
lista =[1,4,235,678,9]
lista.sort()
print(lista)

#Podemos invertir el orden, le pasariamos al sort un argumento llamado reverse=True
lista =[1,4,235,678,9]
lista.sort(reverse=True)
print(lista)

#El metodo sort no es exclusivo de listas matematicas
lista = ["a","g","b","c"]
lista.sort()
print(lista)
#Tambien le podemos aplicar el reverse
lista = ["a","g","b","c"]
lista.sort(reverse=True)
print(lista)
#Ojo con las mayusculas, las mayusculas van antes que las minusculas
lista = ["a","g","A","Z","b","c"]
lista.sort()
print(lista)

#No se pueden mezclar tipos
lista = ["a","g","b","c",2,1,2]
lista.sort()
lista_ordenada = lista
print(lista_ordenada)

#Ademas las listas pueden contener cualquier tipo de dato
#Ejemplo de matriz una lista que contiene listas
lista = [[1,2],[3,4]]
print(lista[0]) #fila 0
print(lista[0][1]) # fila 0 columna 1

#Si no modificar la originalno queda mas remedio que hacer copias
lista = ["a","g","b","c"]
copia = lista[::]
copia.sort(reverse=True)
print(copia)
print(lista)

#Tuplas
#Las tupas son como las listas es decir un conjunto ordenado de objetos
#pero con la diferencia de que las tuplas son INMUTABLES
#Tendran todos las funciones y metodos de las listas menos las que la modifican, nada de añadir,eliminar, o modificar
#para crear una tupla se usa
# tupla = ()
tupla = (1,2,3,4)
print(type(tupla))
print(tupla)

#podemos hacer slice acceder a elementos
tupla = (1,2,3,4)
print(tupla[0])
print(tupla[1:2:])

#No tenemos metodos para añadir y no se peuden modificar
tupla = (1,2,3,4)
tupla[0]="hola"
print(tupla)

#Diccionarios
#Losdiccionarios estan compuestos por un conjunto de pares clave:valor
#Los diccionarios en python son al igual que las listas MUTABLES
# los diccionrios se crear usando {}
# diccionario = {CLAVE_1:VALOR_1, CLAVE_2:VALOR_2, CLAVE_N: VALOr_N}

diccionario = {"nombre":"Jane", "apellido":"Doe"}
print(type(diccionario))
print(diccionario)

#Para acceder a sus valores lo haremos a traves de la clave
#que lso dicionario no tienen orden
diccionario = {"nombre":"Jane", "apellido":"Doe"}
print(diccionario["nombre"])

#Las claves en los diccionarios son unicas
#si utilizamos una clave que ya existe lo que hacemos en realidad
#es modificar el valor
diccionario = {"nombre":"Jane", "apellido":"Doe"}
diccionario["nombre"] = "James"
print(diccionario)

#Para recuperar las claves tenemos un metodo llamado keys()
# DICCIONARIO.keys()
diccionario = {"nombre":"Jane", "apellido":"Doe"}
print(diccionario.keys())
#Pero la mejor forma para saber si una clave ya existe es el operador in
diccionario = {"nombre":"Jane", "apellido":"Doe"}
# clave in diccionario
print("nombre" in diccionario)
#podemos recuperar solo los valores
#tenemos el metodo values()
#diccionario.values()
diccionario = {"nombre":"Jane", "apellido":"Doe"}
print(diccionario.values())

#Para acceder a un elemento podemos hacerlo con la key directamente
diccionario = {"nombre":"Jane", "apellido":"Doe"}
print(diccionario["nombre"])

#Pero tiene el problema de que si intentamos acceder a una key que no existe da error
diccionario = {"nombre":"Jane", "apellido":"Doe"}
print(diccionario["pais"])

#Para solucionar esto, tememos un metodo que es el get
# DICCIONARIO.get(CLAVE,VALOR_POR_DEFECTO)
#VALOR_POR_DEFECTO, es optativo y por defecto vale None
diccionario = {"nombre":"Jane", "apellido":"Doe"}
print(diccionario.get("pais"))

#si le ponemos el argunento vamos con el valor por defeto
diccionario = {"nombre":"Jane", "apellido":"Doe"}
print(diccionario.get("pais","NO EXISTE LA CLAVE"))

#Para añadir nuevos elementos, no hay un metodo directamente como modifcar pero con claves que no existen
diccionario = {"nombre":"Jane", "apellido":"Doe"}
diccionario["pais"]="USA"
print(diccionario)

#Para eliminar podemos usar el del
diccionario = {"nombre":"Jane", "apellido":"Doe"}
del diccionario["nombre"]
print(diccionario)

#Tambien tenemos el metodo pop que nos permite eliminar
#DICCIONARIO.pop(CLAVE)
diccionario = {"nombre":"Jane", "apellido":"Doe"}
diccionario.pop("nombre")
print(diccionario)


#Conjuntos
#es una coleccion de elementos MUTABLE y que no admite duplicados
#los conjuntos se definen de dos formas
#para definir un conjunto vacio 
#conjunto = set()
#para definir un conjunto con valores
#conjunto = {1,2,3,4}

conjunto = set()
print(type(conjunto))
print(conjunto)

#Probamo con valores
conjunto = {1,2,3,4,5}
print(type(conjunto))
print(conjunto)

#IMPORTANTE
conjunto = {1,2,3,4,5,3,4,5,3,2}
print(type(conjunto))
print(conjunto)

#No tienen orden, asi que no podemos recupear valores por posicion
#para conocer si un elemento esta dentro de un conjunto usamos el operador in
conjunto = {1,2,3,4,5}
print(1 in conjunto)

#Podemos añadir elementos a un conjunto
#para ello usamos el metodo add(ELEMENTO)
#CONJUNTO.add(ELEMENTO)
conjunto = {1,2,3,4,5}
conjunto.add(10)
print(conjunto)

#podemos eliminar elementos igual que los diccionarios con el pop
#CONJUNTO.pop(VALOR) elimina el ultimo en ser añadido
conjunto = {1,2,3,4,5}
conjunto.pop()
print(conjunto)
#tenemos el metodo clear
conjunto = {1,2,3,4,5}
conjunto.clear() #Elimina todos los elementos
print(conjunto)
#y un elemento en particular para ello usaremos el remove
conjunto = {1,2,3,4,5}
conjunto.remove(2)
print(conjunto)

#Soporta el algebra de conjuntos
vehiculos = {"BMW", "AUDI","SEAT"}
motos = {"BMW", "DUCATI", "HARLEY"}
#Union todos los elementos de ambos conjuntos sin repetidos
print(vehiculos.union(motos))

#Diferencia los elementos del primer conjunto que no estan incluidos en el segundo
print(vehiculos.difference(motos))

#Interseccion los elementos comunes a ambos conjuntos
print(vehiculos.intersection(motos))


