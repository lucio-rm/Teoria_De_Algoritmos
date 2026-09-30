"""
Enunciado ej.14:
Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: 
o bien (i) pertenece a D;
o bien (ii) es adyacente a un vértice en D.

Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices.

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
no e slo mismo que el vertex_cover?
si es vertex-cover cumple con eso, o no?

testeo mismo codigo a ver si pasa rpl, despues me fijo si tenog que toquetear algo

"""
from grafo import Grafo

def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    if not vertices:
        return []
    preguntame = set()
    vertex_cover = _recolectando_vertex(grafo, vertices, 0, preguntame)

    #acá, la peor situacion es que no haya un vertex_cover mínimo a la cantidad de vertices
    if vertex_cover == None:
        return vertices
    else:
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
    
    #ahorasi
    sol_parcial.add(v_actual)
    si_te_quise = _recolectando_vertex(grafo, vertices, indice+1, sol_parcial)

    sol_parcial.remove(v_actual) #aplico el backtracking, 
    #cual es la diferencia entre usar remove y 'del' ¿?
    
    #primeroquenada chequeo si alguno de los dos no fue una solucion valida
    if no_te_quiero is None:
        return si_te_quise
    if si_te_quise is None:
        return no_te_quiero

    #como queiro el conjunto minimo tneog que agarrar el de menos vertices
    if len(no_te_quiero) <= len(si_te_quise):
        return no_te_quiero
    else:
        return si_te_quise


"""
justificacion de la complejidad:

- temporal: O(2^n), teniendo 2 ramas de decisiones, y exploro todo haciendo pequeñas podas. sigue siendo exponiencial.

- espacial: O(n), siendo n la cantida de vertices. como mucho la sol_parcial va a tener la cantidad de vertices del grafo.
"""


