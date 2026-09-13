"""
Enunciado ej5:

Un camino hamiltoniano, es un camino de un grafo, que visita todos los vértices del grafo una sola vez. Implementar un algoritmo por backtracking que encuentre un camino hamiltoniano de un grafo dado.


"""
"""
planteo:

no hay mucho para pensar, lo dice la consigna. tengo que encontrar un camino que recorra todos los vertices del grafo una sola vez.

tengo que tener 2 visitados?
visitado_general()
visitado_camino()?

y que uno sea el oficial, que sé que esta bien y es el que devuelvo?
y el otro que sea el del momento, el que voy reconstruyendo?

o uso solo ese último y listo?
no terminé de entender cuando y por qué devolvemos una copia del arreglo/lista/solución.

"""
"""
planteo ej.5:
- como el camino hamiltoniano tiene que visitar todos los vertices una vez[cite: 1, 14], necesito un conjunto de visitados para no repetir y una lista para guardar el camino en orden[cite: 1].
- no se de que vertice salgo, asi que pruebo iniciar el backtracking desde cada vertice iterativamente[cite: 1].
- en la funcion recursiva, me fijo en los adyacentes del vertice actual. si hay uno que no visite, lo agrego a visitados y al camino, y llamo recursivamente[cite: 1].
- si llegue a que la longitud de mi camino es igual a la cantidad de vertices totales, gane. devuelvo el camino[cite: 1].
- si fallo, le aplico backtracking a los visitados (remove) y al camino (pop) para habilitarlo por otro lado[cite: 1].
"""
def camino_hamiltoniano(grafo):
    vertices = grafo.obtener_vertices()
    if not vertices:
        return []
    
    camino = []
    visitados = set()
    
    for v in vertices:
        if _camino_hamiltoniano_dfs(grafo, v, visitados, camino, len(vertices)):
            return camino
    return None

def _camino_hamiltoniano_dfs(grafo, v, visitados, camino, total_vertices):
    visitados.add(v)
    camino.append(v)
    
    if len(visitados) == total_vertices:
        return True
        
    for w in grafo.adyacentes(v):
        if w not in visitados: # Esta es la poda natural
            if _camino_hamiltoniano_dfs(grafo, w, visitados, camino, total_vertices):
                return True
                
    # Backtracking: deshacemos para probar otra rama
    visitados.remove(v)
    camino.pop()
    
    return False

"""
Justificacion de la complejidad ej.5:
- temporal: O(V!), ya que en el primer paso tenemos V opciones, luego podemos tener (V-1) opciones de adyacentes, y así sucesivamente en un grafo muy denso. En grafos menos densos la complejidad se acota, pero teóricamente es factorial por backtracking.
- espacial: O(V). La recursión baja hasta una profundidad máxima de V. El set de "visitados" y la lista de "camino" ocupan O(V) de memoria extra.
El problema de encontrar un Camino Hamiltoniano es NP-Completo[cite: 14]. No existen mejoras de complejidad temporal a polinomiales (asumiendo P!=NP).
"""