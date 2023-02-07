#Funciones en python
#Una funcion no es mas que una agrupaicon de codigo, debe estar identada su cuerpo al mismo nivel
#Definicion  minima de una funcion
def foo():
    pass

#Las funciones pueden tener una cadena de documentacion
def foo():
    """
        Ejemplo de documentacion de mi funcion, se suele poner una pequeña descripcion
        y los parametros de entrada y salida
    """
    pass

#Esta documentacion se puee consultar con el metodo magico __doc__
print(foo.__doc__)

#Las funciones en python pueden devolver valores
#Las funciones en Python SIEMPRE devuelven algo, si no le definimos nosotros
#lo que va a devolver nos devolvera un None
def foo():
    pass

vuelta = foo()
print(vuelta)

#Para definir la devolucion usamos el return
def foo():
    return "Hola Mundo"

vuelta = foo()
print(vuelta)

#Las funciones en pytho  pueden devolver mas de un valor, separando las variables con comas
def foo():
    x = 1
    y = 0

    return x,y

#Realmente nos devuelve una tupla
vuelta = foo()
print(vuelta)

#Las funciones admiten argumentos
def foo(x):
    print(x)

foo("Hola Mundo")

#Por defecto los parametros en python Obligatorios y Posicionales
#Podemos modificar esto
#Par que sean optativos, le podemos indicar en la firma un valor por defecto
def foo(a,b=0):
    print(a,b)

foo() #esta no es valida al no tener el parametro a
foo(1)
foo(1,2)

#Nominales, se le indica en el momento de la invocacion
def foo(x,y,z):
    print("x:",x,"y:",y,"z:",z)

foo(z=3,x=2,y=1)
foo(x=1,y=2,z=3)

#Sepueden combinar ambas cosas

def foo(a,b=0):
    print(a,b)

foo(b=1) #No funciona porque le falta a
foo(a=1)
foo(b=1,a=2)
foo(1,a=20) #No funciona porque le pasaos 2 veces

#Poniendo los dos como optativos
def foo(a=1,b=0):
    print(a,b)

foo(b=1) 
foo(a=1)
foo(b=1,a=2)
foo(1,a=20) #Este el unico caso que no funciona

#Comboando
#Esto no funiona porque los obligatorios deben ir siempre antes
def foo(x=10,y=2,z):
    print("x:",x,"y:",y,"z:",z)

foo(z=3,x=2,y=1)
foo(x=1,y=2,z=3)

#Otra mas
def foo(x,y,z=10):
    print("x:",x,"y:",y,"z:",z)

foo(2,3,z=10)
foo(1,y=2,z=3)

#Parametros variables, para esto usamos el *, si son posicionales
def variables(*valores):
    print(type(valores))
    print(valores)

variables()
variables(1)
variables(1,2)
variables(1,2,3)
variables(1,2,3,4)
variables(1,2,3,4,5)

#Y si son nominales usamos el **
def variables(**valores):
    print(type(valores))
    print(valores)

variables()
variables(x=1)
variables(x=1,z=2)
variables(x=1,z=2,y=3)
variables(x=1,z=2,y=3,m=10)

#Podemos combinar todo
def foo(x,y,z=10, *variables, **otros):
    print("x:",x,"y:",y,"z:",z)
    print(variables)
    print(otros)

foo(1,y=2,z=3)
foo(1,2,3,4,5,z=10)
foo(1,2,3,4,5,z=10,g=100,k=1000)