#!/usr/bin/env python
import argparse

from modelo import tirador

def validar_int_args(arg:int, max:int):
    return arg > 2 and arg <= max


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="directorio", type=str,
                        help="Directorio donde se guardarán los CSV de blancos generados. No debe existir en .")
    parser.add_argument(dest="max_alto", type=int,
                        help="Alto máximo de la dispersion de los disparos, no puede ser menor a 3 unidades ni puede ser"
                             " mayor a la altura de la matriz del blanco o sea 28 unidades.")
    parser.add_argument(dest="max_ancho", type=int,
                        help="Ancho máximo de la dispersion de los disparos, no puede ser menor a 3 unidades ni puede "
                             "ser mayor a la anchura de la matriz del blanco o sea 24 unidades.")
    args = parser.parse_args()
    if validar_int_args(args.max_alto, 28) and validar_int_args(args.max_ancho, 24):
        tirador = tirador.Tirador()
        for _ in range(10):
            # Ancho y alto es la dispersion de los disparos
            # 12 por 12 representa aprobado en la tabla de calificacion
            # La ubicacion en el blanco y dentro de la dispersion
            # son aleatorio con distr uniforme
            tirador.tirar(max_alto=args.max_alto, max_ancho=args.max_ancho)
        tirador.guardar_blancos(args.directorio)
    else:
        print("Ancho o alto incorrecto. --help para ayuda.")
