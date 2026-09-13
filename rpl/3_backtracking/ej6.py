"""
Enunciado ej6:
Dada una matriz de 9x9, implementar un algoritmo por backtracking que llene la matriz con números del 1 al 9, dadas las condiciones del Sudoku (si es posible). Las condiciones son:
(i) Las celdas están dispuestas en 9 subgrupos de 3x3.
(ii) Cada columna y cada fila no puede repetir número.
(iii) Cada subgrupo de 3x3 no puede repetir número.

Las posiciones de la matriz con valor 0 se espera que se completen, las posiciones con valores entr 1 y 9 no deben modificarse.

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe.



"""
"""
planteo:

por cada celda, puedo tener una posible_solucion.
para que sea una posible solucion (por ahora pienso una lista de numeros int.
tengo que considerar leer cada fila y columna, y descartar todos los numeros que YA aparaecen en esa misma. ananananananaannashe)

esta ejercicio es una baaaaandovich. dale.


"""


def resolver_sudoku(matriz):
    return matriz