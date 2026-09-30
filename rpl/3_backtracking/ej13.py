"""
Enunciado ej.13:
Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. 
Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover.

Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo.

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
- todas las aristas del grafo
- uno de sus extremos en dicho conjunto

receta bt:
1. si ya encontre solucion, la devuelvo y termino
2. avanzo si puedo
3. pruebo si la solucion parcial es valida
    a) si no lo es, voy pa tras y vuelvo al 2.
    b) si lo es, llamo recursivamente y vuelvo pal 1.
-. si llegué hasta aca, ya probe con todo y no encontre una solucion


indice_vertice
solucion_parcial
solucion
grafo

_recolectando_vertec(grafo, indice, sol_parcial, sol_oficial)

_es_compatible(grafo, sol_parcial, vertice)
    . me fijo si el vertice que quiero agregar es adyacente de alguno
"""
from grafo import Grafo

def vertex_cover_min(grafo):
    vertices = grafo.obener_vertices()
    if not vertices:
        return []
    sol_parcial, sol_oficial = [], []
    vertex_cover = _recolectando_vertex(grafo, vertices, 0, sol_parcial, sol_oficial)

    return vertex_cover

def _recolectando_vertex(grafo, vertices, indice, sol_parcial, sol_oficial):
    if len(sol_parcial) == len(vertices):
            sol_oficial = sol_parcial
            return sol_oficial[:] #una copia devuelvo. por que?

    v_actual = vertices[indice]
    if not v_actual in sol_parcial:
        if _es_compatible(v_actual, sol_parcial, grafo):
            sol_parcial.append(v_actual)
            _recolectando_vertex(grafo, vertices, indice+1, sol_parcial, sol_oficial)
        else:
            # hago bactracking
            

def _es_compatible(vertice, sol_parcial, grafo):
    ady = grafo.adyacentes(vertice) # una lista de adyacentes del vertice
    for v in sol_parcial:
        if v in ady:
            return False
    return True
