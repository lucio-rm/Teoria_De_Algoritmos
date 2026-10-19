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
tengo los valores, caliendo true o false. siendo 3-SAT, siempre tengo hasta 3 variables. por condicion.

- Variables:
como pueden valer true o false, cada X_{i} E {1, 0}. 1 si es verdadera, 0 si es falsa.
para representar las negadas, uso (como probabilidad): 1 - X_{i}


- Inecuaciones:
dependiendo la cantidad (no sé como es el problema)
tengo:
X_1 + (1-X_2) + X_3 >= 1. si o si uno de los 3 tiene que valer true.
(1 - X_1) + X_2 + (1 - X_3) >= 2. lo mismo.


- Función Objetivo:
min cant.(X_{i})
la función objetivo trata de minimizar la cantidad de variables a utilizar.
no creo que sea correcta esta funcion.

"""

# pulp.
