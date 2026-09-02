"""
Enunciado ejercicio 2:
Implementar un algoritmo que reciba un grafo y determine si el mismo es un grafo bipartito, o no. 
Es decir, la función "es_bipartito" debe devolver "True" si el grafo recibido por parámetro es efectivamente bipartito, False en caso contrario. 
Que un grafo sea Bipartito implica que puede separarse los vértices en dos grupos S y T, tal que para cada par de vértices de S no exista arista entre sí (lo mismo para T), que la intersección entre S y T sea vacía y que la unión sea igual al conjunto de todos los vértices del grafo.

A fines del ejercicio, considerar que se pueden ver todos los vértices del grafo en un orden aleatorio con "for v in grafo", y el grafo cuenta con la primitivas "hay_arista(origen, destino)" (devuelve bool), "adyacentes(vertice)" que devuelve una lista de vértices adyacentes al indicado, y v"ertices()" que nos devuelve todos los vértices (lista).

El grafo internamente se encuentra implementado con listas de adyacencia (en su versión de diccionario de diccionarios), a considerar para la complejidad.


"""

import sys
# Para el caso de querer implementar un DFS, 
# para que no hayan problemas en la prueba de volumen
sys.setrecursionlimit(10000)

from collections import deque # para simular el comportamiento del TDA Cola

def es_bipartito(grafo):
    visitados = set()
    colores = {}

    for v in grafo.vertices(): # por si hay mas de una componente conexa
        if v not in visitados:

            if not _recorrido_bfs(grafo, visitados, colores, v):
                return False

    # si llega hasta acá es porque esta todo ok
    return True

def _recorrido_bfs(grafo, visitados, colores, origen):
    cola = deque() # CrearColaEnlazada() -> O(1)

    visitados.add(origen)
    cola.append(origen) # Encolar() -> O(1)
    colores[origen] = 0

    while cola: #while not cola.EstaVacia() 
        vertice = cola.popleft() # Desencolar() -> O(1)

        for ady in grafo.adyacentes(vertice):
            if ady not in visitados:
                visitados.add(ady)
                cola.append(ady)
                colores[ady] = 1 - colores[vertice] # siempre el contrario al padre
            else:
                if colores[ady] == colores[vertice]:
                    # no es bipartito
                    return False

    return True

"""
Complejidad del algoritmo: (siendo V = vertices, E = aristas del grafo)

Recorre todos los vertices del grafo a lo sumo 1 vez y en cada uno recorro sus aristas salientes (que distan de ser las totales del grafo).

acceder, agregar a la cola y al conjunto de visitados cuesta O(1)

Complejidad temporal final: O(V + E)


Complejidad espacial: O(V), 
ya que a lo sumo la cola, colores, y visitados van a llegar a tener V elementos


"""