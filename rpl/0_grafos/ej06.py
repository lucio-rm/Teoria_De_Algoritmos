"""
Enunciado 06:
Implementar un algoritmo que reciba un grafo dirigido y nos devuelva la cantidad de componentes débilmente conexas de este. 
Indicar y justificar la complejidad del algoritmo implementado.

Recordamos que una componente débilmente conexa de un grafo dirigido es un conjunto de vértices que, si al grafo le sacáramos la dirección (lo volvemos no dirigido) sería una componente conexa del mismo.

"""

def cantidad_componentes_debiles(grafo):
    # 1. construyo las aristas entrantes para poder recorrer el grafo hacia atrás
    entrantes = {v: [] for v in grafo.obtener_vertices()}
    for v in grafo.obtener_vertices():
        for ady in grafo.adyacentes(v):
            entrantes[ady].append(v)
            
    visitados = set()
    cantidad_componentes = 0
    
    # 2. recorro un DFS modificado por cada componente
    for v in grafo.obtener_vertices():
        if v not in visitados:
            cantidad_componentes += 1
            # pongo el recorrido para pintar toda la componente débil
            _dfs_debil(grafo, entrantes, visitados, v)
            
    return cantidad_componentes

def _dfs_debil(grafo, entrantes, visitados, v):
    visitados.add(v)
    
    # recorro hacia adelante (aristas salientes habituales)
    for ady in grafo.adyacentes(v):
        if ady not in visitados:
            _dfs_debil(grafo, entrantes, visitados, ady)
            
    # recorro hacia atrás (aristas entrantes)
    for ant in entrantes[v]:
        if ant not in visitados:
            _dfs_debil(grafo, entrantes, visitados, ant)


"""
Complejidad del algoritmo: (V vertices, E aristas del grafo)
1. itero los V vertices y miro sus aristas salientes. como es un grafo dirigido, la suma de todas las salidas es exactamente E. Armar el diccionario cuesta O(V + E)
2. cada vertice entra a "_dfs_debil" exactamente una vez gracias al conjunto de visitados. adentro del a funcion se miran sus aristas salientes y sus aristas entrantes. Al final de todo el algoritmo, cada arista se habra mirado exactamente 2 veces (una del derecho y otra del revez) . Eso cuesta O(V + E)

Complejidad temporal final: O(V + E) + O(V + E) = O(V + E)

Complejidad espacial: O(V + E), 
ya que el diccionario entrantes guarda una lista por cada vertice, y en total, todas las listas suman E elementos. (visitados cuesta a lo sumo O(V))

"""