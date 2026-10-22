"""
Ej.5 (★):
Implementar un modelo de programación lineal que resuelva el problema de 3-SAT mínimo: 
- que encuentre una solución que satisfaga, utlizando la menor cantidad de variables en true posible.

"""
"""
planteo:
El problema 3-SAT consiste en determinar si existe una asignación de valores verdaderos o falsos para un conjunto de variables de modo que toda la fórmula lógica sea verdadera

f = (X_1 o n(X_2) o X_3) y (n(X_1) o X_2 o n(X_3))

tengo que hacer que f sea verdadera.

- Constantes:
Conjunto de variables booleanas I = {1, 2, ..., n} y conjunto de cláusulas C = {C_1, C_2, ..., C_m}. 
Para cada cláusula c ∈ C, definimos P_c ⊆ I como el subconjunto de variables que aparecen sin negar (positivas) en c 
y N_c ⊆ I como el subconjunto de variables que aparecen negadas en c 
(donde |P_c| + |N_c| = 3).

- Variables:
Sea X_1 ∈ {0, 1} una variable binaria entera para cada i ∈ I, que vale 1 si la variable booleana es True, y 0 si es False.

- Inecuaciones:
Para que toda fórmula sea verdadera, cada cláusula c ∈ C tiene que tener al menos un literal en true (|C| inecuaciones)
∀c ∈ C:    ∑ X_i + ∑(1-X_j) ≥ 1.
        i∈ P_c    j∈ N_c

- Función Objetivo:
Quiero minimizar la cantidad total de variables que son True
    n
min ∑ X_i
   i=1

"""

# pulp.
