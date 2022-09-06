from modelo import tirador
from sklearn.neural_network import MLPClassifier
import time
from tqdm import tqdm
from blancos_reales import *


if __name__ == "__main__":
    tirador = tirador.Tirador()
    clasificacion = []
    CANT_DATOS = 90000
    # Creamos CANT_DATOS iguales por cada muestra
    for _ in tqdm(range(CANT_DATOS // 6)):
        tirador.tirar(max_ancho=6, max_alto=6)
        clasificacion.append(1)  # Lo clasificamos como 1 "Aprobado"
        tirador.tirar_punteria(max_ancho=6, max_alto=6)
        clasificacion.append(2)  # Lo clasificamos como 2 "Error punteria"
        tirador.tirar_mal_c_d_e(max_ancho=24, max_alto=28)
        clasificacion.append(3)  # Lo clasificamos como 3 "Error tironeo"
        tirador.tirar_mal_c_d_e(max_ancho=6, max_alto=28)
        clasificacion.append(4)  # Lo clasificamos como 4 "Error respiracion"
        tirador.tirar_mal_c_d_e(max_ancho=24, max_alto=6)
        clasificacion.append(5)  # Lo clasificamos como 5 "Error posicion inestable"
        tirador.tirar_mal(max_ancho=24, max_alto=28)
        clasificacion.append(0)  # Lo clasificamos como 0 "Desaprobado"

    # Metemos los datos en numpy arrays y los acomodamos
    matriz_datos = np.array(tirador.get_datos(), dtype=float)
    matriz_clasificacion = np.array(clasificacion, dtype=float)
    # Aplanamos los datos
    matriz_datos = matriz_datos.reshape(CANT_DATOS, 28 * 24)

    # Creamos el perceptron y lo entrenamos
    inicio = time.time()
    clf = MLPClassifier(solver='adam', activation="tanh",
                        max_iter=800, random_state=4,
                        hidden_layer_sizes=(972//6, 972//9, 972//12),
                        verbose=True)
    clf = clf.fit(matriz_datos, matriz_clasificacion)
    tirador.descartar_blancos()

    # Prueba de prediccion por casos
    CANT_PRUEBA = 100

    # Hago 100 Blancos aprobados
    print("\nPRUEBA APROBADOS")
    for _ in range(CANT_PRUEBA):
        tirador.tirar(max_alto=6, max_ancho=6)
        prueba = tirador.get_datos()
    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    lista_resultados = clf.predict(matriz_prueba).tolist()
    print(f'Acertó {lista_resultados.count(1.0)} de {CANT_PRUEBA} blancos aprobados.')
    tirador.descartar_blancos()
    lista_resultados.clear()

    # Hago 100 Blancos con error de punteria
    print("\nPRUEBA CON ERROR DE PUNTERIA")
    for _ in range(CANT_PRUEBA):
        tirador.tirar_punteria(max_alto=6, max_ancho=6)
        prueba = tirador.get_datos()
    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    lista_resultados = clf.predict(matriz_prueba).tolist()
    print(f'Acertó {lista_resultados.count(2.0)} de {CANT_PRUEBA} blancos con error de punteria.')
    tirador.descartar_blancos()
    lista_resultados.clear()

    # Hago 100 Blancos con error de tironeo
    print("\nPRUEBA ERROR TIRONEO")
    for _ in range(CANT_PRUEBA):
        tirador.tirar_mal_c_d_e(max_ancho=24, max_alto=28)
        prueba = tirador.get_datos()
    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    lista_resultados = clf.predict(matriz_prueba).tolist()
    print(f'Acertó {lista_resultados.count(3.0)} de {CANT_PRUEBA} blancos con error de tironeo.')
    tirador.descartar_blancos()
    lista_resultados.clear()

    print("\nPRUEBA ERROR RESPIRACION")
    for _ in range(CANT_PRUEBA):
        tirador.tirar_mal_c_d_e(max_ancho=6, max_alto=28)
        prueba = tirador.get_datos()
    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    lista_resultados = clf.predict(matriz_prueba).tolist()
    print(f'Acertó {lista_resultados.count(4.0)} de {CANT_PRUEBA} blancos con error de respiracion.')
    tirador.descartar_blancos()

    # Hago 100 Blancos con posicion inestable
    print("\nPRUEBA ERROR POSICION INESTABLE")
    for _ in range(CANT_PRUEBA):
        tirador.tirar_mal_c_d_e(max_ancho=24, max_alto=6)
        prueba = tirador.get_datos()
    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    lista_resultados = clf.predict(matriz_prueba).tolist()
    print(f'Acertó {lista_resultados.count(5.0)} de {CANT_PRUEBA} blancos con error de posicion inestable.')
    tirador.descartar_blancos()
    lista_resultados.clear()

    # Hago 100 blancos con deficiente instruccion
    print("\nPRUEBA DEFICIENTE INSTRUCCION")
    for _ in range(CANT_PRUEBA):
        tirador.tirar_mal(max_alto=28, max_ancho=24)
        prueba = tirador.get_datos()
    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    lista_resultados = clf.predict(matriz_prueba).tolist()
    print(f'Acertó {lista_resultados.count(0.0)} de {CANT_PRUEBA} blancos con defiente instruccion.')
    tirador.descartar_blancos()
    lista_resultados.clear()

    # Prueba de prediccion por casos
    print("\nPrueba caso A")
    blancoA = blancoA.reshape(1, 28 * 24)
    print(f'Prediccion blanco aprobado: {clf.predict(blancoA)} -> debe ser 1')

    print("\nPrueba caso B")
    blancoB = blancoB.reshape(1, 28 * 24)
    print(f'Prediccion blanco con error de puntería: {clf.predict(blancoB)} -> debe ser 2')

    print("\nPrueba caso C")
    blancoC = blancoC.reshape(1, 28 * 24)
    print(f'Prediccion blanco con tironeo: {clf.predict(blancoC)} -> debe ser 3')

    print("\nPrueba caso D")
    blancoD = blancoD.reshape(1, 28 * 24)
    print(f'Prediccion blanco mala respiracion: {clf.predict(blancoD)} -> debe ser 4')

    print("\nPrueba caso E")
    blancoE = blancoE.reshape(1, 28 * 24)
    print(f'Prediccion blanco con posicion inestable: {clf.predict(blancoE)} -> debe ser 5')

    print("\nPrueba caso F")
    blancoF = blancoF.reshape(1, 28 * 24)
    print(f'Prediccion blanco deficiente instruccion: {clf.predict(blancoF)} -> debe ser 0')

    fin = time.time()
    tiempo_total = time.gmtime(fin - inicio)
    res = time.strftime("%M:%S", tiempo_total)
    print(f'TIEMPO TOTAL: {res}m')

#OUTPUT DE EJEMPLO
#Acertó 58.0 de 100 blancos aprobados.
#Acertó 58.0 de 100 blancos desaprobados.