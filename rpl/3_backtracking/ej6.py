"""
Enunciado ej6:
Dada una matriz de 9x9, implementar un algoritmo por backtracking que llene la matriz con números del 1 al 9, dadas las condiciones del Sudoku (si es posible). Las condiciones son:
(i) Las celdas están dispuestas en 9 subgrupos de 3x3.
(ii) Cada columna y cada fila no puede repetir número.
(iii) Cada subgrupo de 3x3 no puede repetir número.

Las posiciones de la matriz con valor 0 se espera que se completen, las posiciones con valores entr 1 y 9 no deben modificarse.

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe.

Métodos del grafo:
Grafo(dirigido = False, vertices_init = []) para crear (hacer 'from grafo import Grafo')
agregar_vertice(self, v)
borrar_vertice(self, v)
agregar_arista(self, v, w, peso = 1)
el resultado será v <--> w
borrar_arista(self, v, w)
estan_unidos(self, v, w)
peso_arista(self, v, w)
obtener_vertices(self)
Devuelve una lista con todos los vértices del grafo
vertice_aleatorio(self)
adyacentes(self, v)
str

"""
"""
planteo:



"""


def resolver_sudoku(matriz):
    return matriz