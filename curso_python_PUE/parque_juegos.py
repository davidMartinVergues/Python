def calcular(a:int, b:int, c:int) -> tuple:
    return a , b + c

def sumar(*numeros):
    return sum(numeros)


if __name__ == "__main__":

    resultado_sumar_1_1 = sumar(1,1)
    resultado_sumar_1_1_4_5 = sumar(1,1,4,5)
    resultado_sumar_1_1_4 = sumar(1,1,4)

    print(resultado_sumar_1_1)
    print(resultado_sumar_1_1_4)
    print(resultado_sumar_1_1_4_5)




    resultado = calcular(1,2,3) #(1, 5)
    print(type(resultado))
    print(f"Resultado {resultado}")

    _, valor2 = calcular(3, 2, 1) #deconstruccion
    #print(f"Tipo valor1:{type(valor1)}")
    print(f"Valor2:{valor2}")

    #lista
    numeros_0_99 = list(range(100))
    cabecera, *cola = numeros_0_99
    suma_cola = sum(cola)
    print(f"Cabecera:{cabecera}")
    print(f"Resto:{cola}")

