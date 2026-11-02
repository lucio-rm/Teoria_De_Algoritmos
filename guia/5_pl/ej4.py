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
Grafo G = (V, E), donde para cada vértice v ∊ V, se conoce su conjunto de vértices ady(v).

- Variables:
Sea X_{v} ∊ {0, 1} una variable binaria entera para cada vértice v ∊ V.
Vale 1 si el vértice fue elegido (y pertenece al conjunto D (Dominating Set)), 0 en caso contrario.

- Inecuaciones:
Cumplo con la restricción. Todo vértice v ∈ V tiene que ser dominado. Lo que implica que es él mismo, o uno de sus adyacentes.
(|V| inecuaciones)

∀v ∈ V:    X_v + ∑ X_w ≥ 1.

- Función Objetivo:
lo que yo busco en este ejercicio, es minimizar la cantidad de vertices elegidos → minimizar el tamaño del dominating set.

min ∑(X_{v})
  v ∈ V

"""

# pulp

