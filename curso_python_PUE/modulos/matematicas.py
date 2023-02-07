def calcular_media(numeros:list) -> float:
    if numeros is not None and len(numeros) > 0:
        return sum(numeros) / len(numeros) 