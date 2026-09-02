"""
Enunciado 16:
Sea una matriz A de tamaño n x n, con todos valores distintos. Un índice (i, j) es
un máximo local si A[i, j] es estrictamente mayor que todos su vecinos que existan
(arriba, abajo, izquierda, derecha). Implementar un algoritmo de División y Conquista que permita
encontrar algún máximo local en tiempo O}(n). Justificar adecuadamente la complejidad
del algoritmo. Prestar mucha atención a la ecuación de recurrencia escrita, ya que esto puede develar
un error en el algoritmo planteado.


"""


def minimo_local(matriz):
    # devolvemos posiciones i, j donde esta el minimo local
    return (0, 0)