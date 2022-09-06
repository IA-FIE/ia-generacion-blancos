import numpy as np
from plot_disparos import heatmap, FILAS, COLUMNAS


def crear_blanco(lista_impactos):
    # Matriz con todos ceros, primero valores de y y luego de x
    blanco = np.zeros((28, 24))
    for impacto in lista_impactos:
        blanco[impacto[0]][impacto[1]] = impacto[2]
    return blanco


# Blanco A: Aprobado
blancoA = crear_blanco(
    [[10, 11, -1], [12, 13, -1], [15, 13, -1],
     [10, 13, 1], [13, 10, 1], [14, 15, 1]])

# Blanco B: error de punteria
blancoB = crear_blanco(
    [[7, 11, -1], [10, 14, -1], [13, 9, -1],
     [4, 17, 1], [6, 14, 1], [9, 19, 1]])

# Blanco C: Tironeo
blancoC = crear_blanco(
    [[5, 8, -1], [15, 20, -1], [25, 6, -1],
     [3,16,1], [12, 2, 1], [21, 16, 1]])

# Blanco D: control de respiración
blancoD = crear_blanco(
    [[5, 7, -1], [11, 10, -1], [22, 3, -1],
     [6, 9, 1], [14, 3, 1], [20, 10, 1]])

# Blanco E: posición inestable
blancoE = crear_blanco(
    [[17, 4, -1], [20, 10, -1], [15, 18, -1],
     [19, 9, 1], [19, 1, 1], [18, 15, 1]])

# Blanco F: Deficiente instrucción
blancoF = crear_blanco(
    [[2, 11, -1], [12, 13, -1], [20, 15, -1],
     [12, 12, 1], [20, 1, 1], [26, 13, 1]])

# Blanco real aprobado
blanco_soldado_A = crear_blanco(
    [[11, 8, -1], [15, 7, -1], [15, 8, -1],
     [14, 8, 1], [16, 8, 1], [16, 12, 1]])

# Blanco real error de punteria
blanco_soldado_B = crear_blanco(
    [[14, 13, -1], [19, 15, -1], [20, 11, -1],
     [23, 11, 1], [23, 16, 1], [27, 14, 1]])

if __name__ == "__main__":
    heatmap(blancoA, FILAS, COLUMNAS)
    heatmap(blancoB, FILAS, COLUMNAS)
    heatmap(blancoC, FILAS, COLUMNAS)
    heatmap(blancoD, FILAS, COLUMNAS)
    heatmap(blancoE, FILAS, COLUMNAS)
    heatmap(blancoF, FILAS, COLUMNAS)
