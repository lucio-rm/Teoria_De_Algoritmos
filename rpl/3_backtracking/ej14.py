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


bueno se quedó bugeado, pero no . no es lo mismo que vortex.
son NP-completos ?

vertex mira aristas

dominating set mira vertices. todo vertice del grafo tiene queestar, o tener un vecino que esté



o esta en la sol_actual 
o al menos uno de sus adyacentes está en la sol_actual

"""
from grafo import Grafo


def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    if not vertices:
        return []
    preguntame = set()
    resultado = _recolectando_ds(grafo, vertices, 0, preguntame)

    #acá, la peor situacion es que no haya un vertex_cover mínimo a la cantidad de vertices
    if resultado == None:
        return vertices
    else:
        return resultado

def _es_ds_esto(grafo, sol_actual):
    for v in grafo.obtener_vertices():
        if v in sol_actual:
            continue
        tiene_vecino_goat = False
        for w in grafo.adyacentes(v):
            if w in sol_actual:
                tiene_vecino_goat = True
                break
        if not tiene_vecino_goat:
            return False
    return True

def _recolectando_ds(grafo, vertices, indice, sol_parcial):
    if indice == len(vertices):
        if _es_ds_esto(grafo, sol_parcial):
            return list(sol_parcial) #devuelvo una compia tipo lista + rpl me pide lista je
        return None #no es solucion valida
    
    v_actual = vertices[indice]

    #ahora las decisiones, lo incluyo o no
    
    no_te_quiero = _recolectando_ds(grafo, vertices, indice+1, sol_parcial)
    
    #ahorasi
    sol_parcial.add(v_actual)
    si_te_quise = _recolectando_ds(grafo, vertices, indice+1, sol_parcial)

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


