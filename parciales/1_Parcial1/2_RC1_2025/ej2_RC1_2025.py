"""
Enunciado ejercicio 2:
Dado un grafo sin ciclos (un bosque, el cual es necesariamente bipartito), implementar un *algoritmo greedy* que obtenga el matching máximo. Es decir, el subconjunto máximo de aristas tal que ninguna arista comparta vértice entre sí.
Indicar y justificar la complejidad del algoritmo. El análisis de la complejidad debe estar completo. 
Justificar por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar, si no dar un contraejemplo.
"""
"""
planteo:

subconjunto máximo de aristas / ninguna arista comparta vértice entre sí.

pensar greedy. pensar avariciosamente.

cosas que estoy pensando:
- agarrar primero las aristas de todos los vertices que son hojas.

- pensas en ub bosque. sabes que si empezas agarrando las aristas del núcleo del bosque, podes cubrirlo más rápido.
pero si empezas de afuera...

- adyacencias? contar adyacencias?

- es un problema de bipartito - coloreo k=2, que en vez de pintar vertices pintas aristas. elegis el grupo de mayor cantidad de aristas.

- pienso que es óptimo y que se puede demostrar por inducción.


primer aproach:

Regla Greedy: primer arista que vea la agarro al recarajo. 
    ~ empezando de una hoja.
    ~ menor adyacentes --> menor ban
"""

# from grafo import Grafo
def matching_maximo(grafo):
    if not grafo:
        return 0

    vertices = grafo.obtener_vertices()
    if not vertices:
        return 0 # no hay aristas je

    """
    pienso:
    - grados de entrada/salida
    - ordenarlo de menor a mayor.
    - set() de usados
    """
    grados = {}
    for v in vertices:
        contador = 0
        for _ in grafo.adyacentes(v):
            contador += 1
        grados[v] = contador
    ordenados = sorted(grados, key=lambda x: x[0], reverse=False)

    usados = set()
    conjunto = []
    for v in ordenados: # admite varias componentes conexas
        if v not in usados and grados[v] > 0: # los que no tienen arista no me importan.
            _matching_greedy(grafo, vertices, v, usados, conjunto)
    
    return conjunto


def _matching_greedy(grafo, vertices, origen, usados, conjunto):
    usados.add(origen)
    for ady in grafo.adyacentes(origen):
        if ady not in usados:
            conjunto.append((origen, ady)) # tupla con la arista (origen, ady)


"""
Justificacion de la complejidad:

--------------- temporal:
- obtener_vertices() recorre los V vertices del grafo. O(V).
- calcular los grados de todos los vertices:
    . recorre todos los vértices del grafo, y por cada vertice recorre las aristas. Que distan de ser las totales del grafo, por lo que el costo es O(V + E).
- ordenar los grados, para elegir primero de manera avariciosa los de menor grado para no cubrir/usar vértices de más.
    . ordenar los grados con V vertices tiene un costo de O(V.logV)
- por vada vertice del grafo (ordenado por grado), se recorren sus adyacentes (utilizando la funcion auxiliar '_matching_greedy')






--------------- espacial:



Justificacion de las propiedades Greedy:

- Regla Greedy:


"""