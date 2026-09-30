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


tengo en BT 2 opciones (por eso 2^n)

incluyo el vertice o no lo incluyo

despues de burradas:
tengo que usar un set() para hacer preguntas en O(1)
y en _es_compatible me tengo que fijar si tiene una arista con NINGUN vertice

y mejor _es_compatible ===> _es_cover_esto
"""
from grafo import Grafo

def vertex_cover_min(grafo):
    vertices = grafo.obener_vertices()
    if not vertices:
        return []
    preguntame = set()
    vertex_cover = _recolectando_vertex(grafo, vertices, 0, preguntame)

    return vertex_cover

def _es_cover_esto(grafo, sol_actual):
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if v not in sol_actual and w not in sol_actual:
                # si hay una arista del grafo sin las dos puntas en la sol_actual, no cubri todo el grafo.
                return False
    return True

def _recolectando_vertex(grafo, vertices, indice, sol_parcial):
    if indice == len(vertices):
        if _es_cover_esto(grafo, sol_parcial):
            return list(sol_parcial) #devuelvo una compia tipo lista + rpl me pide lista je
        return None #no es solucion valida
    
    v_actual = vertices[indice]

    #ahora las decisiones, lo incluyo o no
    
    no_te_quiero = _recolectando_vertex(grafo, vertices, indice+1, sol_parcial)
    
    