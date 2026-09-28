"""


Ej.5 (★):
Dado un laberinto representado por una grilla, queremos calcular la ganancia máxima que existe desde la posición (0,0) hasta la posición NxM. Los movimientos permitidos son, desde la esquina superior izquierda (el (0,0)), nos podemos mover hacia abajo o hacia la derecha.
Pasar por un casillero determinado (i,j) nos da una ganancia de Vi,j. 
Implementar un algoritmo que, por programación dinámica, obtenga la máxima ganancia a través del laberinto. Hacer una reconstrucción del camino que se debe transitar. 
Indicar y justificar la complejidad del algoritmo implementado. 
Si hay algunos lugares por los que no podemos pasar (obstáculos), ¿cómo se debe modificar para resolver el mismo problema?

"""
"""
planteo:
puedo ir para abajo o para la derecha en la matriz.

tengo 2 opciones.

ec. recurrencia:
OPT(actual) = max(vengo de la izquierda, vengo de arriba) + dinero[actual] <== siempre y cuando no haya obstaculos.

"""

def laberinto(matriz):
    if not matriz:
        return 0
    M_MATRIZ = [0][0] * len(matriz)
    for i in range(len(matriz)): # filas
        for j in range(len(matriz[0])): # columnas ¿? o era al reves
            de_arriba = -1
            de_izquierda = -1
            if i > 0:
                de_izquierda = matriz[i-1][j]
            if j > 0:
                de_arriba = matriz[i][j-1]
            
            M_MATRIZ[i][j] = max(de_izquierda, de_arriba) + matriz[i][j]

    RECORRIDO = _reconstruccion(matriz, M_MATRIZ)
    return M_MATRIZ[len(matriz[0])-1][len(matriz)-1] #devuelvo la esquina, que esta el valor máximo.

def _reconstruccion(matriz, M_MATRIZ):
    """
    idea reconstruccion.
    voy a la esquina inferior izquierda de la matriz.
    si el valor es igual al de arriba o izquierda, significa que no cambió. y no se usó
    si cambió, se usó.
    """
    RECORRIDO = [] # guardo los índices que se recorrieron en el laberinto.
    for i in range(matriz, 0, -1):
        for j in range(matriz[0], 0, -1):
            actual = M_MATRIZ[i][j]
            arriba = M_MATRIZ[i][j-1]
            izquierda = M_MATRIZ[i-1][j]

            if actual == arriba and actual == izquierda:
                continue
            else:
                RECORRIDO.append(actual)
    
    return RECORRIDO[::-1] # porque esta invertido, lo cambio para que este bien.



"""
Justificación de la complejidad:

- temporal: O(n.m), siendo n la cantidad de filas, m la cantidad de columnas.
    recorro todas las filas y columnas para poner bien los valores.

- espacial: O(n.m)
    como mucho, los arreglos creados (RECORRIDO Y M_MATRIZ) van a ocupar O(nm) en espacio.
"""