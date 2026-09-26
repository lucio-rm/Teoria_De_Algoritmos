"""
1. Ej.1 (★):
Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor del n-ésimo número de fibonacci. 
Indicar y justificar la complejidad del algoritmo implementado. 

Definición:
. n = 0 --> Debe devolver 1
. n = 1 --> Debe devolver 1
. n --> Debe devolver la suma entre los dos anteriores números de fibonacci (los fibonacci n-2 y n-1)
"""

"""
planteo:

primero pienso en la ecuación de recurrencia --> forma de los subproblemas

sé los casos bases y sé el patrón que sigue.

T(N) = OPT(N-2) + OPT(N-1)

utilizo un for para llenar un arreglo de memoria (tecnica memoization).

después de eso, sería averiguar el fibonacci de N
que es la parte de reconstrucción.

igual creo que no hace falta. es hacer N iteraciones. y no utilizo un arreglo para recordar, solo las dos últimas

"""

def fibonacci(n):
    if n <= 1:
        return 1

    actual = 1
    anterior = 0
    total = 0
    for i in range(n):
        total = actual + anterior
        anterior = actual
        actual = total
        i += 1

    return total


"""
Justificación de la complejidad:

- temporal: O(n), siendo n la cantidad de iteraciones necesarias hasta llegar al n-ésimo valor de la secuencia de fibonacci.
- espacial: O(1), utilizando variables se consigue una complejidad espacial constante.


"""

