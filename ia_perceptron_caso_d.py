from modelo import tirador
import numpy as np
from sklearn.neural_network import MLPClassifier
import time
from tqdm import tqdm
from blancos_reales import *


if __name__ == "__main__":
    tirador = tirador.Tirador()
    clasificacion = []
    CANT_DATOS = 30000
    # Creamos CANT_DATOS muestras mitad con error de respiracion y mitad deficiente instruccion
    for _ in tqdm(range(CANT_DATOS // 2)):
        tirador.tirar_mal_c_d_e(max_ancho=6, max_alto=28)
        clasificacion.append(1) # Lo clasificamos como 1 "Error respiracion"
        tirador.tirar_mal(max_ancho=24, max_alto=28)
        clasificacion.append(0) # Lo clasificamos como 0 "Deficiente instruccion"

    # Metemos los datos en numpy arrays y los acomodamos
    matriz_datos = np.array(tirador.get_datos(), dtype=float)
    matriz_clasificacion = np.array(clasificacion, dtype=float)
    # Aplanamos los datos
    matriz_datos = matriz_datos.reshape(CANT_DATOS, 28 * 24)

    # Creamos el perceptron y lo entrenamos
    inicio = time.time()
    clf = MLPClassifier(solver='adam', activation="tanh",max_iter=400, random_state=1,
                        hidden_layer_sizes=(672//6,672//9,672//12), verbose=True)
    clf = clf.fit(matriz_datos, matriz_clasificacion)
    tirador.descartar_blancos()

    # Prueba de prediccion de buen desempeño
    CANT_PRUEBA = 100
    # Hago 100 Blancos con error de respiracion
    print("\nPRUEBA ERROR RESPIRACION")
    for _ in range(CANT_PRUEBA):
        tirador.tirar_mal_c_d_e(max_ancho=6, max_alto=28)
        prueba = tirador.get_datos()
    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    print(f'Acertó {clf.predict(matriz_prueba).sum()} de {CANT_PRUEBA} blancos con error de respiracion.')
    tirador.descartar_blancos()

    # Prueba de prediccion de mal desempeño
    # Hago 100 blancos con deficiente instruccion
    print("\nPRUEBA DEFICIENTE INSTRUCCION")
    for _ in range(CANT_PRUEBA):
        tirador.tirar_mal(max_alto=28, max_ancho=24)
        prueba = tirador.get_datos()
    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    print(f'Acertó {CANT_PRUEBA - clf.predict(matriz_prueba).sum()} de {CANT_PRUEBA} blancos con deficiente instruccion.')
    tirador.descartar_blancos()

    # Prueba de prediccion de buen desempeño (con error de respiracion)
    print("\nPrueba caso D")
    blancoD = blancoD.reshape(1, 28 * 24)
    print(f'Prediccion blanco con error de respiracion: {clf.predict(blancoD)} -> debe ser 1')

    # Prueba de prediccion de mal desempeño
    print("\nPrueba caso A")
    blancoA = blancoA.reshape(1, 28 * 24)
    print(f'Prediccion blanco aprobado: {clf.predict(blancoA)} -> debe ser 0')

    print("\nPrueba caso B")
    blancoB = blancoB.reshape(1, 28 * 24)
    print(f'Prediccion blanco con error de punteria: {clf.predict(blancoB)} -> debe ser 0')

    print("\nPrueba caso C")
    blancoC = blancoC.reshape(1, 28 * 24)
    print(f'Prediccion blanco con error de tironeo {clf.predict(blancoC)} -> debe ser 0')

    print("\nPrueba caso E")
    blancoE = blancoE.reshape(1, 28 * 24)
    print(f'Prediccion blanco con posicion inestable: {clf.predict(blancoE)} -> debe ser 0')

    print("\nPrueba blanco F")
    blancoF = blancoF.reshape(1, 28 * 24)
    print(f'Prediccion blanco deficiente instruccion: {clf.predict(blancoF)} -> debe ser 0')

    fin = time.time()
    tiempo_total = time.gmtime(fin - inicio)
    res = time.strftime("%M:%S", tiempo_total)
    print(f'TIEMPO TOTAL: {res}m')

#OUTPUT DE EJEMPLO
#Acertó 58.0 de 100 blancos aprobados.
#Acertó 58.0 de 100 blancos desaprobados.