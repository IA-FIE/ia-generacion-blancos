import csv
import random
from modelo import disparos

ALTO_BLANCO = 14
ANCHO_BLANCO = 12
ALTO_MATRIZ = ALTO_BLANCO * 4
ANCHO_MATRIZ = ANCHO_BLANCO * 4

class Blanco:
    """ Matriz que representa la superficie del blanco de MOTE """
    def __init__(self):
        self.matriz = [(["0"]*ANCHO_MATRIZ) for i in range(ALTO_MATRIZ)]

    def mostrar_matriz(self):
        for row in self.matriz:
            print(*row)

    def recibir_impactos(self,impactos):
        derecha = random.randint(0, ANCHO_MATRIZ- impactos.max_ancho)
        abajo = random.randint(0, ALTO_MATRIZ - impactos.max_ancho)
        for impacto in impactos:
            x, y = derecha + impacto.posicion[0], abajo + impacto.posicion[1]
            self.matriz[y][x] = impacto.indicador

    def guardar_csv(self, filename):
        with open(file=filename, mode="w") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerows(self.matriz)



if __name__ == "__main__":
    blanco = Blanco()
    impactos = disparos.Impactos()
    try:
        impactos.generar_disparos(max_ancho=12, max_alto=12)
        blanco.recibir_impactos(impactos)
        blanco.mostrar_matriz()
        blanco.guardar_csv("nuevo.csv")
    except disparos.ValueTooSmall:
        print("No se puedo ingresar los impactos.")
        blanco.mostrar_matriz()