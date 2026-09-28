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
    if not matriz or not matriz[0]:
        return 0
    filas = len(matriz)
    columnas = len(matriz[0])
    
    M_MATRIZ = [[0] * columnas for _ in range(filas)] #así sería crear una tabla para la matriz de tamaño real de la matriz original.

    #caso base: el comienzo del laberinto
    M_MATRIZ[0][0] = matriz[0][0] # y si es un obstaculo ¿?
    for i in range(filas): 
        for j in range(columnas):
            if i == 0 and j == 0:
                continue
            
            de_arriba = -1
            de_izquierda = -1
            if i > 0:
                de_arriba = M_MATRIZ[i-1][j] # ir una fila para atras es venir de arriba
            if j > 0:
                de_izquierda = M_MATRIZ[i][j-1] # ir una columna para la izq es venir por la izquierda.
            
            M_MATRIZ[i][j] = max(de_izquierda, de_arriba) + matriz[i][j]

    RECORRIDO = _reconstruccion(M_MATRIZ, filas, columnas)
    return M_MATRIZ[filas-1][columnas-1] #devuelvo la esquina, que esta el valor máximo.

def _reconstruccion(M_MATRIZ, filas, columnas):
    """
    idea reconstruccion.
    voy a la esquina inferior izquierda de la matriz.
    si el valor es igual al de arriba o izquierda, significa que no cambió. y no se usó
    si cambió, se usó.
    
    tiene que decidir si vino de arriba o de la izquierda
    """
    RECORRIDO = [] # guardo los índices que se recorrieron en el laberinto.
    i = filas -1
    j = columnas - 1

    RECORRIDO.append((i, j)) # si o si donde termina tienq ue estar, me habia re olvidado

    # voy para atras tipo minotauro hasta llegar al inicio del laberinto
    while i > 0 or j > 0:
        if i == 0:
            j -= 1 # su no puedo subir mas solo puedo ir a la izquierda
        elif j == 0:
            i -= 1 #misma shet
        else:
            # comparo quien fue el crack que aportó el valor maximo
            if M_MATRIZ[i-1][j] >= M_MATRIZ[i][j-1]:
                i -= 1 # de_arriba
            else:
                j -= 1 # de_izquierda
                
        RECORRIDO.append((i, j))
    # no olvidarme, en la reconstruccion tiene que estar la esencia de la ecuacion de la recurrencia.
    return RECORRIDO[::-1] # porque esta invertido, lo cambio para que este bien.



"""
Justificación de la complejidad:

- temporal: O(n.m), siendo n la cantidad de filas, m la cantidad de columnas.
    recorro todas las filas y columnas para poner bien los valores.

- espacial: O(n.m)
    como mucho, los arreglos creados (RECORRIDO Y M_MATRIZ) van a ocupar O(nm) en espacio.
"""