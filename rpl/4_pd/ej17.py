"""
Ej.17 (not guia?)
Dado un número n, indicar la cantidad más económica (con menos términos) de escribirlo como suma de cuadrados perfectos, utilizando Programación Dinámica. Indicar y justificar la complejidad del algoritmo implementado.

Aclaración: siempre es posible escribir a n como suma de n términos de 1^2, por lo que siempre existe solución. Sin embargo, la expresión 10 = 3^2 + 1^2 es una manera más económica de escribirlo para n=10

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por programación dinámica". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
"""
"""
planteo:
---- clase eze , ya son las 23:40 no doy ma

OPT(n) = paratodo i E [1, raizde(n)] min()


"""
from math import isqrt

def terminos(n):
    if n <= 1:
        return n
    OPT = [0] * (n+1)
    OPT[0] = 1
    OPT[1] = 1

    for numero in range(2, n+1):
        minimo = numero
        for i in range(1, isqrt(numero)+1):
            minimo = min(minimo, 1 + OPT[numero-i*i])
        OPT[numero] = minimo
    
    return OPT[n]

"""
justificacion de la complejidad:

- temporal y espacial: O(n), siendo n la cantidad de elementos.

"""


"""
ej.17 guia:

fact(n) = fact(n-1) . n , n = 0 || 1, == 1.

aproxe(n) = aprox


"""