from random import sample
from itertools import product


IMPACTOS_TOT = 6
DISPAROS_SERIE = IMPACTOS_TOT//2

class ValueTooSmall(Exception):
    """ Cuando el alto y ancho de la zona de impactos no llega a contener los impactos totales """
    pass

class Disparo:
    """ Disparo individual que contiene información de posicion y el marcador que lo representa en el blanco """
    def __init__(self, posicion:tuple, indicador:int = 0):
        self.posicion = posicion
        self.indicador = indicador

    def __repr__(self):
        return str(self.posicion) + "->" + str(self.indicador)


class Impactos(list):
    """ Genera y contiene una lista de 6 disparos, como los realizados en el blanco de MOTE """
    def __init__(self, *args):
        list.__init__(self, *args)
        self.max_ancho = 0
        self.max_alto = 0

    def generar_disparos(self, max_ancho, max_alto, indicador):
        self.max_ancho = max_ancho
        self.max_alto = max_alto
        if max_ancho * max_alto >= IMPACTOS_TOT:
            posiciones = sample(list(product(range(max_ancho), range(max_alto))), k=DISPAROS_SERIE)
            for pos in posiciones:
                self.append(Disparo(posicion=pos, indicador=indicador))
            # print(f'Superficies: {superficies}')
        else:
            raise ValueTooSmall

    def generar_dispersos(self, max_ancho, max_alto, area_deseada = 12.5):
        """Garantiza que al menos uno de los dos triangulos generados tiene un área superiror a la
        maxima que puede tener un triangulo aprobado"""
        self.max_ancho = max_ancho
        self.max_alto = max_alto
        area = 0.0
        while area <= area_deseada:
            self.clear()
            self.generar_disparos(max_ancho=max_ancho,max_alto=max_alto, indicador=1)
            self.generar_disparos(max_ancho=max_ancho, max_alto=max_alto, indicador=-1)
            area = max(self.calcular_superficies())


    def calcular_superficies(self):
        if len(self) == 6:
            tanda = list(filter(lambda d: d.indicador == 1, self))
            coord_tanda_1 = list(map(lambda d: d.posicion, tanda))
            tanda = list(filter(lambda d: d.indicador == -1, self))
            coord_tanda_2 = list(map(lambda d: d.posicion, tanda))
            superficies = superficie_triangulo(coord_tanda_1), superficie_triangulo(coord_tanda_2)
            return superficies

    def determinar_distancia_centros(self):
        """ Determina el centro de la serie de disparos """
        x1, x2, y1, y2 = 0, 0, 0, 0
        for disparo in self[3:]:
            x1 += disparo.posicion[0]
            y1 += disparo.posicion[1]
        for disparo in self[:3]:
            x2 += disparo.posicion[0]
            y2 += disparo.posicion[1]
        x1 = x1 // 3
        y1 = y1 // 3
        x2 = x2 // 3
        #print("Centro de la serie: ({}, {})".format(xc, yc))
        return calcular_distancia_entre_puntos( (x1, y1), (x2, y2) )

    def vaciar(self):
        self.clear()


def superficie_triangulo(puntos):
    if len(puntos) == 3:
        A, B, C = puntos
        return abs(0.5 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])))


def calcular_distancia_entre_puntos(p1, p2):
    """ Calcula la distancia entre dos puntos """
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


if __name__ == "__main__":
    '''
    maximos = []
    impactos = Impactos()
    for i in range(100):
        superficies = []
        for i in range(10000):
            impactos.generar_disparos(max_alto=13, max_ancho=12)
            primer_tanda = list(filter(lambda d : d.indicador == 1, impactos))
            segunda_tanda = list(filter(lambda d: d.indicador == 2, impactos))
            coord_primer_tanda = list(map(lambda d : d.posicion, primer_tanda))
            coord_segunda_tanda = list(map(lambda d: d.posicion, segunda_tanda))
            superficie_primer_tanda = superficie_triangulo(coord_primer_tanda)
            superficie_segunda_tanda = superficie_triangulo(coord_segunda_tanda)
            superficies.append(superficie_primer_tanda)
            superficies.append(superficie_segunda_tanda)
            impactos.clear()
        maximos.append(max(superficies))
    print(max(maximos)) #60.5 si es 12 * 12, 12.5 si es 6 * 6, 2.0 si es 3 * 3
    #Desaprobados:  286 si es 27 * 23, 72 si es 13 * 13, 66 si es 12 * 13
    '''
    impactos = Impactos()
    impactos.generar_dispersos(max_ancho=14, max_alto=14)
    print(impactos)



