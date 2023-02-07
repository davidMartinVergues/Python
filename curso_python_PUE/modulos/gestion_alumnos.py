from funciones_alumnos import cargar_alumnos, calcular_media

if __name__ == "__main__":
    alumnos = cargar_alumnos()
    media_alumnos = calcular_media(alumnos)
    print(f"La media de la clase es {round(media_alumnos,2)}")
