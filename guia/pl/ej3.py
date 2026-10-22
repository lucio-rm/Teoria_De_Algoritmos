"""
Ej.3 (★):
Implementar un modelo de programación lineal que resuelva el problema de Vertex Cover mínimo (ejercicio 13 de BT).

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


# pulp

