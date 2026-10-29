"""
Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover.

Implementar un modelo de programación lineal que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo.

Métodos del grafo:
Grafo(dirigido = False, vertices_init = []) para crear (hacer 'from grafo import Grafo')
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
Recordar que aquí estamos usando PuLP para resolver el problema porque es la forma programática de poder evaluarlo en RPL. A la hora del parcial lo que nos es relevante es el modelo.

"""
"""
planteo:

Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. 


- Constantes:
Grafo G = (V, E), con V vértices y E el conjunto de aristas

- Variables:
Sea X_{v} ∊ {0, 1} una variable binaria entera para cada vértice v ∊ V.
Vale 1 si se elije el vértice (y forma parte del Vertex Cover), 0 en caso contrario.

- Inecuaciones:
quiero que cada arista tenga la menor cantidad de vertices. al menos uno de sus vértices tiene que ser elegido. para cada arista ∊ E.

∀(i, k) ∊ E:    X_{i} + X_{k} ≥ 1.

Para todo par de vertices conectados por la arista (i, k), trato de forzar elegir siempre 1 de esos dos.
(como mucho van a ser |E| inecuaciones)

- Función Objetivo:
El objetivo es minmizar la cantidad de vértices a agarrar.

min ∑(X_{v})
  v ∊ V (vertices del grafo)

"""

import pulp

def vertex_cover_min(grafo):
    return []