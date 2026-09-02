"""
Enunciado 07:
El diámetro de una red es el máximo de las distancias mínimas entre todos los vértices de la misma. Implementar un algoritmo que permita obtener el diámetro de una red, para el caso de un grafo no dirigido y no pesado. 
Indicar el orden del algoritmo propuesto.

"""

from collections import deque

def diametro(grafo):
    vertices = grafo.obtener_vertices()
    if not vertices:
        return 0
        
    max_diametro_global = 0
    
    # uso un BFS agarrando cada vertice como origen
    for origen in vertices:
        distancia_max_desde_origen = _bfs_distancia_maxima(grafo, origen)
        
        # Guardamos la distancia más grande que hayamos visto en toda la red
        if distancia_max_desde_origen > max_diametro_global:
            max_diametro_global = distancia_max_desde_origen
            
    return max_diametro_global

def _bfs_distancia_maxima(grafo, origen):
    visitados = {origen}
    
    # en la cola guardo tuplas (vertice, distancia_desde_el_origen)
    cola = deque([(origen, 0)])
    max_distancia = 0
    
    while cola:
        vertice, dist = cola.popleft()
        max_distancia = dist  # el último en salir siempre tiene la distancia más alta
        
        for ady in grafo.adyacentes(vertice):
            if ady not in visitados:
                visitados.add(ady)
                cola.append((ady, dist + 1))
                
    return max_distancia



"""
Complejidad del algoritmo: (siendo V = vertices, E = aristas del grafo)
El recorrido BFS en el grafo no dirigido cuesta O(V + E)
Como ejecuto un BFS una vez por cada vertice del grafo, se multiplica por O(V)

complejidad temporal final: O(V.(V+E)) = O(V² + V.E)

complejidad espacial: O(V) , 
la cola y el conjunto d evisitados por cada iteracion se borran y se vuelven a crear, ocupando un total de V elementos como máximo.

"""