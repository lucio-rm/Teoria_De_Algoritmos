"""
Implementar un modelo de programación lineal que resuelva el problema de Juan El Vago (ejercicio 4 de PD).

Recordar que aquí estamos usando PuLP para resolver el problema porque es la forma programática de poder evaluarlo en RPL. A la hora del parcial lo que nos es relevante es el modelo.

"""
"""
planteo:
juan el vago

un arreglo de n días.
puedo: trabajar hoy o no trabajar.
si trabajo hoy, no puedo trabajar al día siguiente. (o el día anterior si es que hay).
si trabajo hoy, obtengo la paga del día.
quiero maximizar la paga

- Constantes:
cantidad total de n días.
cada dia tiene una ganancia 'g_i', con i ∊ {1, 2, ..., n}


- Variables:
Al tener la opcion de elegir o no elegir el día para trabajar, utilizo variables binarias enteras.
X_{i} E {0, 1}, cada X_{i} representa el día 'i'. Si vale 0, no trabaja. si vale 1, si.

- Inecuaciones:
Si trabajo en X_{i}, no puedo trabajar en (i-1) y (i+1).
∀i ∊ {1, 2, ..., n-1}: X_i + X_{i+1} ≤ 1

- Función Objetivo:
quiero maximizar el valor a trabajar.
    n
max ∑(X_{i} . g_i)
   i=1

"""

import pulp

def juan_el_vago(trabajos):
    # devolver un arreglo de los índices de días a trabajar
    return []