"""
Enunciado 01:

Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a #V, devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.

Métodos del grafo:
Grafo(dirigido = False, vertices_init= []) para crear (hacer 'from grafo import Grafo')
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
parecido al coloreo de grafos, no?

me tengo que curtir con backtracking. es importante. lleva mas codigo que dificultad conceptual.

tengo:
- grafo no dirigido
- numero n < a len(grafo.obtener_vertices())
devuelvo:
- subconjunto de n
    - lista de vertices
    - esa misma lista, entre cada par de vertices no tienen que ser adyacentes entre sí.
    
resolución:
- para conseguir la lista, pienso primero en las hojas del grafo. sé que esas mismas van a ser


Backtracking es siempre recursivo?

"""
def no_adyacentes(grafo, n):
    'Devolver una lista con los n vértices, o None de no ser posible'
    pass

