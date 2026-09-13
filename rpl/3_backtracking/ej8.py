"""
Enunciado ej8:
Implementar un algoritmo de backtracking que, dados dos grafos, determine si existe un Isomorfismo entre ambos.

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

UFFFF , no me acuerdo como verga era este.

era analizar un vertice, y analizar una posible solucion en decir "che, si este es el vertice, se tiene que comportar iiiigual que el posible_vertice del grafo_2, no? tiene que tener la misma cantidad de adyacentes, y esos adyacentes tienen que tener el mismo comportamiento (llamado recursivo ahi), sino cambio a otor, sino vuelvo al backtrcking."
esta bien ese pensamiento?

"""


def hay_isomorfismo(g1, g2):
    return False