import numpy as np
from plot_disparos import heatmap, FILAS, COLUMNAS

blanco1 = np.zeros((28,24))
blanco1[6][11] = -1
blanco1[12][13] = -1
blanco1[15][13] = -1

blanco1[10][13] = 1
blanco1[13][10] = 1
blanco1[14][15] = 1


if __name__ == "__main__":
    heatmap(blanco1, FILAS, COLUMNAS)