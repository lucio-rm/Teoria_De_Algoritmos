"""
Ej.4 (★):
Implementar un modelo de programación lineal que resuelva el problema de Dominating Set mínimo (ejercicio 14 de BT).

"""
"""
planteo:
Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: 
o bien (i) pertenece a D; 
o bien (ii) es adyacente a un vértice en D.

- Constantes:
V vértices
E aristas
cada vertice tiene adyacentes.


- Variables:
V_{i} a cada vertice 'i' del grafo G.
E_{i} a cada arista 'i' del grafo G.

- Inecuaciones:
quiero que cada arista tenga la menor cantidad de vertices. y / o que ya pertenezca a D, no agregar. (ahi tengo que agregar el Big-M?)
∀(i, k) e E: X_{i} + X_{k} <= 1.
Para todo par de vertices conectados por la arista (i, k), trato de forzar elegir siempre 1 de esos dos.



- Función Objetivo:
lo que yo busco en este ejercicio, es minimizar la cantidad de vertices elegidos.
min sum(X_{i})

"""

# pulp

