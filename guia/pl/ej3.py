"""
Ej.3 (★):
Implementar un modelo de programación lineal que resuelva el problema de Vertex Cover mínimo (ejercicio 13 de BT).

"""
"""
planteo:

Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. 


- Constantes:
V vértices
E aristas
cada vertice tiene adyacentes.

- Variables:
V_{i} a cada vertice 'i' del grafo G.
E_{i} a cada arista 'i' del grafo G.

- Inecuaciones:
quiero que cada arista tenga la menor cantidad de vertices.
∀(i, k) e E: X_{i} + X_{k} <= 1.
Para todo par de vertices conectados por la arista (i, k), trato de forzar elegir siempre 1 de esos dos.

- Función Objetivo:
lo que yo busco en este ejercicio, es minimizar la cantidad de aristas elegidas.
Por consecuencia, minimizar la cantidad de vértices elegidos.

min sum(X_{i})

"""


# pulp

