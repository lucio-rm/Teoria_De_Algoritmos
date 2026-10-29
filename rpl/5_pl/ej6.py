"""
Ej.6 (★★★):
Implementar un modelo de programación lineal que resuelva el problema de Independent Set Máximo.

"""
"""
planteo:

Independent Set máximo: no pueden haber más de dos vértices adyacentes en el independent set.
Quiero la mayor cantidad de vértices a elegir.

- Constantes:
Grafo G = (V, E), conjuntos de adyacentes ady(i) para cada i ∈ V, y la constante M = |V| + 1.

- Variables:
Sea X_i ∈ {0, 1} una variable binaria para cada vértice i ∈ V, que vale 1 si el vértice i es incluido
en el Ind. Set, y 0 si no.

- Inecuaciones:
Si un vértice i es seleccionado (X_i = 1), el término de la big-M se anula y fuerza a que ninguno de sus adyacentes pueda ser seleccionado.
Si Y_i = 0, la cota derecha pasa a valer |V| + 2, desactivando la restricción para los ady. (|V| inecuaciones en total)

∀i ∈ V:    Y_i + ∑ Y_k ≤ 1 + M.(1 - Y_i)
              k∈ady(i)

- Función Objetivo:
Maximizar la cantidad total de vértices en el Independent Set

max ∑ Y_i
   i∈V

"""

# pulp.
