"""
Ej.2 (★):
Implementar un modelo de programación lineal que resuelva el problema de Juan El Vago (ejercicio 4 de PD).

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
n elementos
cada elemento tiene un valor_{n}

- Variables:
Al tener la opcion de elegir o no elegir el día para trabajar, utilizo variables binarias.
X_{i} E {0, 1}, cada X_{i} representa el día 'i'.

- Inecuaciones:
Si trabajo en X_{i}, no puedo trabajar en (i-1) y (i+1).
X_{i-1} + X_{i} <= 1
X_{i} + X_{i+1} <= 1
y eso me permite trabajar en (i-1) y (i+1)

- Función Objetivo:
quiero maximizar el valor a trabajar.

max sum(X_{i})
"""


# pulp
