from modelo import tirador


if __name__ == "__main__":
    tirador =  tirador.Tirador()

    for _ in range(10):
        # Ancho y alto es la dispersion de los disparos
        # 12 por 12 representa aprobado en la tabla de calificacion
        # La ubicacion en el blanco y dentro de la dispersion
        # son aleatorio con distr uniforme
        tirador.tirar(max_alto=12,max_ancho=12)

    tirador.guardar_blancos("aprobados")