import os

from modelo import disparos
from modelo.blanco import Blanco
from modelo.disparos import Impactos


class Tirador:
    def __init__(self):
        self.blancos_usados = []

    def tirar(self, max_ancho, max_alto):
        """ Genera los disparos y los impacta en un blanco, el cual guarda el tirador. Los argumendos dan la dispersion
        de los disparos"""
        blanco = Blanco()
        impactos = Impactos()
        try:
            impactos.generar_disparos(max_ancho, max_alto, 1)
            impactos.generar_disparos(max_ancho, max_alto, -1)
            blanco.recibir_impactos(impactos)
            self.blancos_usados.append(blanco)
        except disparos.ValueTooSmall:
            print("No se puedo ingresar los impactos.")

    def tirar_punteria(self, max_ancho,max_alto):
        blanco = Blanco()
        impactos = Impactos()
        try:
            impactos.generar_disparos(max_ancho, max_alto, 1)
            lista_impactos = blanco.recibir_impactos(impactos)
            impactos.vaciar()
            impactos.generar_disparos(max_ancho, max_alto, -1)
            lista_impactos.extend(blanco.recibir_impactos(impactos))
            distancia_centros = calcular_distancia_centros(lista_impactos)
            while 4 > distancia_centros:
                blanco.eliminar_impactos(lista_impactos[3:6])
                del lista_impactos[3:6]
                lista_impactos.extend(blanco.recibir_impactos(impactos))
                distancia_centros = calcular_distancia_centros(lista_impactos)
            self.blancos_usados.append(blanco)
        except disparos.ValueTooSmall:
            print("No se puedo ingresar los impactos.")

    def tirar_mal_c_d_e(self, max_ancho, max_alto):
        blanco = Blanco()
        impactos = Impactos()
        try:
            impactos.generar_dispersos(max_ancho, max_alto)
            lista_impactos = blanco.recibir_impactos(impactos)
            distancia_centros = calcular_distancia_centros(lista_impactos)
            while 4 > distancia_centros:
                blanco.limpiar_blanco()
                impactos.vaciar()
                impactos.generar_dispersos(max_ancho, max_alto)
                lista_impactos = blanco.recibir_impactos(impactos)
                distancia_centros = calcular_distancia_centros(lista_impactos)
            #print(f'Distancia_centros {distancia_centros}')
            self.blancos_usados.append(blanco)
        except disparos.ValueTooSmall:
            print("No se puedo ingresar los impactos.")

    def tirar_mal(self, max_ancho, max_alto):
        blanco = Blanco()
        impactos = Impactos()
        try:
            impactos.generar_dispersos(max_ancho, max_alto)
            lista_impactos = blanco.recibir_impactos(impactos)
            distancia_centros = calcular_distancia_centros(lista_impactos)
            while 4 < distancia_centros:
                blanco.limpiar_blanco()
                impactos.vaciar()
                impactos.generar_dispersos(max_ancho, max_alto)
                lista_impactos = blanco.recibir_impactos(impactos)
                distancia_centros = calcular_distancia_centros(lista_impactos)
            #print(f'Distancia_centros {distancia_centros}')
            self.blancos_usados.append(blanco)
        except disparos.ValueTooSmall:
            print("No se puedo ingresar los impactos.")

    def mostrar_blanco(self, index):
        """ Metodo para que el tirador nos muestre en pantalla 1 de los blancos en su poder. """
        self.blancos_usados[index].mostrar_matriz()
        return

    def guardar_blancos(self, foldername:str):
        """ Dado un nombre de carpeta guarda todos los blancos que posee el tirador en esa carpeta """
        try:
            os.mkdir(foldername)
            for index,blanco in enumerate(self.blancos_usados):
                blanco.guardar_csv(f"./{foldername}/blanco_{index}.csv")
        except FileExistsError:
            print("No se puede crear la carpeta por que ya existe")

    def descartar_blancos(self):
        if len(self.blancos_usados) > 0:
            self.blancos_usados.clear()

    def get_datos(self):
        return list(map(lambda b : b.get_datos(), self.blancos_usados))


def calcular_distancia_centros(lista_impactos):
    """ Determina el centro de la serie de disparos """
    x1, x2, y1, y2 = 0, 0, 0, 0
    for disparo in lista_impactos[0:3]:
        x1 += disparo[0]
        y1 += disparo[1]
    for disparo in lista_impactos[3:6]:
        x2 += disparo[0]
        y2 += disparo[1]
    x1 = x1 // 3
    y1 = y1 // 3
    x2 = x2 // 3
    return calcular_distancia_entre_puntos((x1, y1), (x2, y2))


def calcular_distancia_entre_puntos(p1, p2):
    """ Calcula la distancia entre dos puntos """
    return int(((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5)


if __name__ == "__main__":
    """
    tirador = Tirador()
    for _ in range(10):
        tirador.tirar(max_alto=12,max_ancho=12)
    tirador.guardar_blancos("aprobados")    
    """

    tirador = Tirador()
    for i in range(3):
        tirador.tirar_mal_c_d_e(max_ancho=24, max_alto=28)
        print(f'\nBlanco {i}: {tirador.mostrar_blanco(index=i)}\n')


