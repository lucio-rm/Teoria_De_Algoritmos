"""
Ej.1 (★):
Implementar un modelo de programación lineal que resuelva el Problema de la Mochila de valor máximo (ejercicio 7 de PD).

"""
"""
planteo:
knapsack problem

tengo
- W capacidad
- n elementos, con cada uno (peso, valor)

~ con cada elemento tengo 2 opciones: elegirlo o no elegirlo.
    . ese pensamiento me permite pensar en variables binarias (0 no elegirlo, 1 elegirlo).
~ si o si los elementos que elija , su suma tiene que ser menorIgual a W.


componentes:
- Constantes:
tope W
n elementos. (peso_n, valor_n)

- Variables:
Sea X_{i} E {0, 1} una variable binaria que vale 1 si elijo el elemento. 0 si no.
Representa a los elementos elegidos.

- Inecuaciones:
La suma de todos los elementos elegidos tiene que ser menorIgual a W.
Sum(X_{i} . peso_{i}) <= W
ej: 
X_{1} . p_{1} + X_{2} . p_{2} + X_{3} . p_{3} + X_{4} . p_{4} <= W
suponiendo que uso x1 y x3, van a valer 1. x2 y x4 van a valer 0. entonces:
X_{1} . p_{1} + X_{3} . p_{3} <= W


- Función Objetivo:
\max sum(X_{i} . valor_{i})
Quiero maximizar el valor de cada elemento que utilizo (cumpliendo con la inecuacion).

"""

# pulp.
