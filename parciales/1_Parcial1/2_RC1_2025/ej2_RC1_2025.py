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
from collections import deque
# from grafo import Grafo
def matching_maximo(grafo):
    # O(V+E) calculo grados
    grados = {v: len(grafo.adyacentes(v)) for v in grafo.obtener_vertices()}
    hojas = deque([v for v, g in grados.items() if g <= 1])

    matching = []
    visitados = set()

    while hojas:
        v = hojas.popleft()
        if v in visitados:
            continue
        padre = None #busco el único vecino disponible
        for w in grafo.adyacentes(v):
            if w not in visitados:
                padre = w
                break
        if padre is not None:
            matching.append((v, padre))
            visitados.add(v)
            visitados.add(padre)

            #actualizo los grados de los vecinos del padre para encontrar nuevas hojas
            for u in grafo.adyacentes(padre):
                if u not in visitados:
                    grados[u] -= 1
                    if grados[u] <= 1:
                        hojas.append(u)
    return matching


"""
Justificacion de la complejidad:

--------------- temporal:
- obtener_vertices() recorre los V vertices del grafo. O(V).
- calcular los grados de todos los vertices:
    . recorre todos los vértices del grafo, y por cada vertice recorre las aristas. Que distan de ser las totales del grafo, por lo que el costo es O(V + E). 
- ordenar los grados, para elegir primero de manera avariciosa los de menor grado para no cubrir/usar vértices de más.
    . ordenar los grados con V vertices tiene un costo de O(V.logV)
- por vada vertice del grafo (ordenado por grado), se recorren sus adyacentes (utilizando la funcion auxiliar '_matching_greedy'), que distan de ser los totales del grafo. En el peor de los casos el costo es O(V + E)

Complejidad temporal: O(V.(logV + E))

--------------- espacial: O(V), siendo V la cantidad de vértices en el grafo.
Como mucho se utiliza un espacio extra de O(V). y en el caso de conjunto, en el peor del os casos termina utilizando O(E), y como para un grafo con estas propiedades hay mayor cantidad de vertices que de aristas, termina quedando en O(V). (V > E)

Justificacion de las propiedades Greedy:

- Regla Greedy: Siempre que pueda, guardo la arista.
Se logró la optimalidad* en el algoritmo gracias a haber empezado con los de menor grado y calculado los grados del vértice antes de ejecutar el guardado.
Se trata de un algoritmo greedy, ya que viendo el estado local (analizando los adyacentes de un vértice) elijo el óptimo local (agarrar la arista siempre y cuando no se junte con otro vértice ya visitado).
Y en la sucesión de óptimos globales, se llegó al óptimo global (el matching máximo).
Siempre, de manera avariciosa, se elige la arista que tiene conectado si o si el vértice con menor grado en el óptimo local.


*Demostración de la optimalidad:
Demostración por inducción:
siendo V la cantidad de vertices, y E la cantidad de aristas.
y siempre manteniendo las propiedades originales del grafo (sin ciclos y bipartito)

siendo k el conjunto (V, E) con la cantidad (V = k+1, E = #V-1), y manteniendo propuesta
- paso base: k = 1, 
V = 2, E = 1. matching máximo = 1. elige la arista del grafo que conecta a los dos vertices

k = 2:
V = 3, E = 2.
(A -- B -- C). matching máximo = 1. elige cualquiera de las dos aristas, cumpliendo con el matching máximo.


- paso inductivo: p(k+1)

si se que
p(k+1) = V = (k+1)+1, E = (#V-1)
y está demostrado que para k es óptimo, si se le suma 1 vertice y 1 arista, no va a cmabiar el resultado. no va a cambiar la optimalidad, como mucho cambia para mejor y se encuentra un matching máximo de mayor valor (si se agrega como hoja y adyacente a otros).
"""
"""
justificacion de verdad (optimalidad):
Una hoja tiene grado 1. Solo puede unirse a su padre. Si no la unes a su padre, la hoja queda aislada (pierdes 1 arista potencial). Si la unes, podrías impedir que el padre se una a otro nodo, pero el intercambio es de 1 a 1 (no pierdes cantidad). Al eliminar la hoja y el padre, se generan nuevas hojas y repites.

"""