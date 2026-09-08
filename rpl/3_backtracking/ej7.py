"""
Enunciado ej7:
Implementar un algoritmo de backtracking que, dado una pieza de caballo en un tablero de ajedrez de n x n, determine si existen los movimientos a realizar para que el caballo logre pasar por todos los casilleros del tablero una única vez.
Recordar que el caballo mueve en forma de L (dos casilleros en una dirección, y un casillero en forma perpendicular).

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


def knight_tour(n):
    return False