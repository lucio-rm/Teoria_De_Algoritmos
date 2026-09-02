"""
Enunciado 04:

Implementar un algoritmo que reciba un grafo dirigido, un vértice V y un número N, y devuelva una lista con todos los vértices que se encuentren a exactamente N aristas de distancia del vértice V. 

Indicar el tipo de recorrido utilizado y el orden del algoritmo. Justificar.

"""

from collections import deque

def a_n_aristas(grafo, v, n):
    vertices = grafo.obtener_vertices()
    if v not in vertices:
        return [] # en el caso que el vertice origen no esté

    visitados = set()
    orden = {}
    # voy a recorrer todos (hasta orden N) y devuelvo solo los son de orden N
    cola = deque()

    cola.append(v)
    visitados.add(v)
    orden[v] = 0

    while cola:
        vertice = cola.popleft()

        if orden[vertice] == n:
            continue # si ya el vertice padre tiene orden N, no hace falta que recorra sus adyacentes (van a ser mayores a N)
        for ady in grafo.adyacentes(vertice):
            if ady not in visitados:
                visitados.add(ady)
                cola.append(ady)
                orden[ady] = orden[vertice] + 1

    lista_cumplen = []
    for vert, valor in orden.items():
        if valor == n:
            lista_cumplen.append(vert)
    
    return lista_cumplen


"""
Justificacion del algoritmo: ( siendo V = vertices, E = aristas del grafo )
el recorrido utilizado es un recorrido BFS, asi recorro RADIALMENTE el grafo y me guardo el orden de cada vertice, asi guardo los que tengan orden exacto N.

complejidad temporal:

es O(V + E) , ya que por cada vertice me fijo en sus adyacentes, que distan de ser los totales del grafo.

y al final ('for vert, valor in orden.items()') recorro a lo sumo V vertices.

complejidad temporal final : O(V) + O(V + E) = O(2V + E) = O(V + E)

complejidad espacial:
O(V), porque a lo sumo la cola, orden y visitados van a ser ocupados con V elementos.

"""