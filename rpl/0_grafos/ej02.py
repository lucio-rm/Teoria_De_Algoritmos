"""
Enunciado 02:
Implementar un algoritmo que determine si un grafo no dirigido es conexo o no. Indicar la complejidad del algoritmo si el grafo está implementado con una matriz de adyacencia.

"""
# from grafo import Grafo

# implemento un recorrido bfs y analizo la cantida de vertices visitados. Teóricamente, si la cantidad de vertices visitados es distinta a la cantidad de vertices del grafo, entonces significa que tiene mas de una componente conexa. Tener mas de una cmp. conexa significa que no es conexo.

from collections import deque
def es_conexo(grafo):
    vertices = grafo.obtener_vertices()

    if not vertices:
        return True #si esta vacio, es conexo ¿?
    
    visitados = set()
    origen = grafo.vertice_aleatorio()
    _recorrido_bfs(grafo, visitados, origen)
        
    return len(visitados) == len(vertices)
    

def _recorrido_bfs(grafo, visitados, origen):
    visitados.add(origen)
    cola = deque() # CrearColaEnlazada() (O(1))
    cola.append(origen) # Encolar() (O(1))
    while cola: #while !cola.EstaVacia()
        vertice = cola.popleft() # desencolar() (O(1))
        for ady in grafo.adyacentes(vertice):
            if ady not in visitados:
                visitados.add(ady)
                cola.append(ady) #encolar() (O(1))


"""
Complejidad del algoritmo: V = vertices, E = aristas del grafo
Obtener vertice aleatorio = O(1)
recorrido bfs:
    por cada vertice del grafo (si es conexo) recorre sus adyacentes (si es que tiene), que distan de ser los totales del grafo.
    encolar y desencolar cuestan O(1) y se hacen a lo sumo V veces.
    complejidad = O(V + E)

grafo.obtener_vertices cuesta O(V)

Complejidad temporal final = O(V) + O(V + E) = O(2V + E) = O(V + E)

Complejidad espacial  = O(V)
como mucho, la cola y el conjunto de visitados van a tener V elementos.

"""