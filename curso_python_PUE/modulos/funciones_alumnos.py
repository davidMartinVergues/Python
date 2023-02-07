#from matematicas import calcular_media
import matematicas as mat

def cargar_alumnos() -> list:
    """"""
    return [('Juan', 8.0), ('Maria',9.5),('Ivan', 7.8)]

def extraer_notas(l_alumnos:list) -> list:
    """"""
    notas = list()
    for alumno in l_alumnos:
        notas.append(alumno[-1])
    else:
        return notas

def calcular_media(l_alumnos:list) -> float:
    """"""
    if l_alumnos is not None and len(l_alumnos) > 0:
        #return sum(extraer_notas(l_alumnos))/len(l_alumnos)
        return mat.calcular_media(extraer_notas(l_alumnos))