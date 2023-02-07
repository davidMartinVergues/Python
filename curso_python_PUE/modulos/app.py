def obtener_numero_sesion():
    return 5

#type hint
def saludar(nombre:str, edad:int = 18):
    return f"Hola me llamo {nombre.upper()} y tengo {edad} años."

def obtener_suma_valores(items:list):
    """Retorna la suma de los valores del parametro items"""
    if items is None: return None
    sumatorio = 0
    for item in items:
        sumatorio += item #sumatorio = sumatorio + item
    
    return sumatorio  

def sumar_valores(items:list):
    """Retorna la suma de los valores del parametro items"""
    if items is None: return None
    return sum(items)




if __name__ == "__main__":
    #definicion  de a variabñe que contiene los valores
    valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #valores = None
    #resultado_suma = obtener_suma_valores(valores) 
    resultado_suma = sumar_valores(valores) 
    if resultado_suma is not None:
        print(f"El total de la suma de valores es {resultado_suma}")
    else:
        print("Ha habido un problema")


    num_sesion = obtener_numero_sesion()
    print(f"Hola python sesion {num_sesion} funciones")
    print(f"{saludar('Ricardo', 34)}")

'''
Definir una funcion que recorra una lista y devuelva la suma de los
numeros que contiene
'''

