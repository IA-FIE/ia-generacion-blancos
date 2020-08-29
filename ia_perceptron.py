from modelo import tirador
import numpy as np
from sklearn.neural_network import MLPClassifier
import time


if __name__ == "__main__":
    tirador = tirador.Tirador()
    clasificacion = []
    CANT_DATOS = 7500
    # Creamos CANT_DATOS muestras mitad aprobadas y mitad desaprobadas
    for _ in range(CANT_DATOS // 2):
        tirador.tirar(max_ancho=12, max_alto=12)
        clasificacion.append(1) # Lo clasificamos como 1 "Aprobado"
        tirador.tirar_mal(max_ancho=22, max_alto=22)
        clasificacion.append(0) # Lo clasificamos como 0 "Desaprobado"

    # Metemos los datos en numpy arrays y los acomodamos
    matriz_datos = np.array(tirador.get_datos(), dtype=float)
    matriz_clasificacion = np.array(clasificacion, dtype=float)
    # Aplanamos los datos
    matriz_datos= matriz_datos.reshape(CANT_DATOS, 28 * 24)

    # Creamos el perceptron y lo entrenamos
    inicio = time.time()
    clf = MLPClassifier(solver='adam', activation="logistic",max_iter=400, random_state=1,hidden_layer_sizes=(672//6,))
    clf = clf.fit(matriz_datos, matriz_clasificacion)
    tirador.descartar_blancos()
    # Prueba de prediccion de buen desempeño
    CANT_PRUEBA = 100
    # Hago 10 Blancos aprobados
    for _ in range(CANT_PRUEBA):
        tirador.tirar(max_alto=10, max_ancho=10)
        prueba = tirador.get_datos()
    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    print(f'Acertó {clf.predict(matriz_prueba).sum()} de {CANT_PRUEBA} blancos aprobados.')
    tirador.descartar_blancos()

    # Prueba de prediccion de mal desempeño
    # Hago 100 blancos desaprobados
    for _ in range(CANT_PRUEBA):
        tirador.tirar_mal(max_alto=22, max_ancho=22)
        prueba = tirador.get_datos()
    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    print(f'Acertó {CANT_PRUEBA - clf.predict(matriz_prueba).sum()} de {CANT_PRUEBA} blancos desaprobados.')
    tirador.descartar_blancos()
    fin = time.time()
    tiempo_total = fin - inicio
    print(tiempo_total)

#OUTPUT DE EJEMPLO
#Acertó 58.0 de 100 blancos aprobados.
#Acertó 58.0 de 100 blancos desaprobados.