"""
Enunciado ej.18:
Implementar un algoritmo que, por backtracking, obtenga la cantidad total de posibles ordenamientos topológicos de un grafo dirigido y acíclico.

Métodos del grafo:
Grafo(dirigido = False, vertices_init = []) para crear un grafo no dirigido (hacer 'from grafo import Grafo')
Grafo(dirigido = True, vertices_init = []) para crear un grafo dirigido (hacer 'from grafo import Grafo')
agregar_vertice(self, v)
borrar_vertice(self, v)
agregar_arista(self, v, w, peso = 1)
borrar_arista(self, v, w)
estan_unidos(self, v, w)
peso_arista(self, v, w)
obtener_vertices(self)
Devuelve una lista con todos los vértices del grafo
vertice_aleatorio(self)
adyacentes(self, v)
str

"""

def contar_ordenamientos(grafo):
    return 0