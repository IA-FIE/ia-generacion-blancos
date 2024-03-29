import csv
import random
from modelo import disparos

ALTO_BLANCO = 14
ANCHO_BLANCO = 12
ALTO_MATRIZ = ALTO_BLANCO * 2
ANCHO_MATRIZ = ANCHO_BLANCO * 2


class Blanco:
    """ Matriz que representa la superficie del blanco de MOTE """
    def __init__(self):
        self.matriz = [(["0"]*ANCHO_MATRIZ) for i in range(ALTO_MATRIZ)]

    def mostrar_matriz(self):
        for row in self.matriz:
            print(*row)

    def recibir_impactos(self, impactos):
        derecha = random.randint(0, ANCHO_MATRIZ - impactos.max_ancho)
        abajo = random.randint(0, ALTO_MATRIZ - impactos.max_alto)
        lista_impactos = []
        for impacto in impactos:
            x, y = derecha + impacto.posicion[0], abajo + impacto.posicion[1]
            lista_impactos.append((x, y))
            self.matriz[y][x] = impacto.indicador
        return lista_impactos

    def guardar_csv(self, filename):
        with open(file=filename, mode="w", newline='') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerows(self.matriz)

    def get_datos(self):
        return self.matriz

    def limpiar_blanco(self):
        self.matriz = [(["0"]*ANCHO_MATRIZ) for i in range(ALTO_MATRIZ)]

    def eliminar_impactos(self, lista_impactos):
        for x, y in lista_impactos:
            self.matriz[y][x] = "0"


if __name__ == "__main__":
    blanco = Blanco()
    impactos = disparos.Impactos()
    try:
        impactos.generar_disparos(max_ancho=24, max_alto=28, indicador=1)
        impactos.generar_disparos(max_ancho=24, max_alto=28, indicador=-1)
        blanco.recibir_impactos(impactos)
        blanco.mostrar_matriz()
        blanco.guardar_csv("blanco.csv")
    except disparos.ValueTooSmall:
        print("No se puedo ingresar los impactos.")
        blanco.mostrar_matriz()
