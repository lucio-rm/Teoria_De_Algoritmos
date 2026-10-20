"""
Ej.7 (★★):
Implementar un modelo de programación lineal que determine la cantidad mínima de colores a utilizar para poder pintar a un grafo de colores, de tal forma que ningún adyacente comparta color entre sí.

"""
"""
planteo:

- Constantes:
k cantidad de colores
v cant vertices

- Variables:
X_i E {0, 1, 2, ..., k}, siendo una variable entera binaria la cual me indica el color de la cual fué seleccionada.

- Inecuaciones:
∀i, X_i vértice del grafo:
X_i != X_j
j ady(i)
por cada vertice X_i, tiene que tener un valor distinto a sus adyacentes.

- Función Objetivo:
min (X_i), la idea es minimizar la cantidad de colores a utilizar.

"""

# pulp