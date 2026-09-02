"""
Enunciado 03:
Un árbol es un grafo no dirigido que cumple con las siguientes propiedades:

a. E = V - 1

b. Es acíclico

c. Es conexo

Por teorema, si un grafo cumple dos de estas tres condiciones, será árbol (y por consiguiente, cumplirá la tercera). 
Haciendo uso de ésto (y únicamente de ésto), se pide implementar una función que reciba un grafo no dirigido y determine si se trata de un árbol, o no. 
Indicar el orden de la función implementada.

"""

#uso funciones de los ejercicios anteriores, ya que me sirven en este.

def es_arbol(g):
    vertices = g.obtener_vertices()
    cant_v = len(vertices)
    
    # un caso borde sería tener el grafo vacío (es un arbol ¿?)
    # porque si V=0, E=0, no cumple E = V-1 (0 != -1), por lo que daría False
    
    # valido la Propiedad A: E = V - 1
    cant_e = _cantidad_aristas(g)
    if cant_e != (cant_v - 1):
        return False
        
    # valido la Propiedad C: es conexo
    # si cumple que E = V - 1 Y tambien es conexo, por teorema YA ES un arbol.
    return _es_conexo(g)

def _cantidad_aristas(g):
    #en un grafo no dirigido, si sumamos los adyacentes de todos los V,
    # contamos cada arista exactamente 2 veces (una por cada extremo)
    suma_grados = 0
    for v in g.obtener_vertices():
        suma_grados += len(g.adyacentes(v))
    return suma_grados // 2


from collections import deque
def _es_conexo(grafo):
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
Complejidad del algoritmo: siendo V = vertices, E = aristas del grafo

las funciones auxiliares utilizadas:
- cantidad_aristas() cuesta O(V + E), ya que por cada vertice del grafo, analizamos sus adyacentes, que distan de ser los totales del grafo.
- es_conexo() cuesta O(V + E), ya explicado (utiliza un recorrido BFS)

O(V + E) + O(V + E) = O(2V + 2E) = O(V + E)

complejidad temporal final: O(V + E)
"""