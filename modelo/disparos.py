from random import sample
from itertools import product


IMPACTOS_TOT = 6
DISPAROS_SERIE = IMPACTOS_TOT//2

class ValueTooSmall(Exception):
    """ Cuando el alto y ancho de la zona de impactos no llega a contener los impactos totales """
    pass

class Disparo:
    """ Disparo individual que contiene información de posicion y el marcador que lo representa en el blanco """
    def __init__(self, posicion:tuple, indicador:str = "0"):
        self.posicion = posicion
        self.indicador = indicador

    def __repr__(self):
        return str(self.posicion) + " " +self.indicador

class Impactos(list):
    """ Genera y contiene una lista de 6 disparos, como los realizados en el blanco de MOTE """
    def __init__(self, *args):
        list.__init__(self, *args)
        self.max_ancho = 0
        self.max_alto = 0

    def generar_disparos(self,max_ancho,max_alto):
        self.max_ancho = max_ancho
        self.max_alto = max_alto
        if max_ancho * max_alto >= IMPACTOS_TOT:
            posiciones = sample(list(product(range(max_ancho), range(max_alto))), k=IMPACTOS_TOT)
            for pos in posiciones[:DISPAROS_SERIE]:
                self.append(Disparo(posicion=pos,indicador="#"))
            for pos in posiciones[DISPAROS_SERIE:]:
                self.append(Disparo(posicion=pos, indicador="@"))
        else:
            raise(ValueTooSmall)

    def vaciar(self):
        self.clear()

if __name__ == "__main__":
    impactos = Impactos()
    impactos.generar_disparos(max_alto=12, max_ancho=12)
    print(impactos)
    impactos.vaciar()
    impactos.generar_disparos(max_alto=12, max_ancho=12)
    print(impactos)

