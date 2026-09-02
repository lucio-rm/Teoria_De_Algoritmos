"""
Enunciado 04:
Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es: estrictamente creciente hasta una determinada posición p, y estrictamente decreciente a partir de ella (con 0 < p < N - 1). Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2. Se pide:

1. Implementar un algoritmo de división y conquista de complejidad O(log n) que encuentre la posición p del pico: func PosicionPico(v []int, ini, fin int) int. La función será invocada inicialmente como: PosicionPico(v, 0, len(v)-1), y tiene como pre-condición que el arreglo tenga forma de pico.

2. Justificar la complejidad del algoritmo mediante el teorema maestro.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(log(n))". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""
"""
planteo:
llegar a complejidad O(logn)  = descartar una mitad de los resultados y que el algoritmo siga siendo óptimo

En este caso, en el arreglo 'v' pasado por parámetro:
voy al medio.

tengo 3 casos:
. caso base: me queda 1 elemento, ese mismo es el pico
. estoy antes del pico, de forma creciente
. estoy despues del pico, de forma decreciente.

si v[medio] < v[medio+1]. estoy subiendo, el pico esta estrictamente a la derecha

sino: estaría bajando o en el pico, descarto la izquierda pero no descarto que pueda estar en el medio.



"""

def posicion_pico(v, ini, fin):
    if ini == fin:
        return ini # cuando llego a tener 1 elemento, devuelvo ese mismo.
    
    medio = (ini + fin) // 2

    if v[medio] < v[medio+1]:
        # estoy subiendo, el pico esta estrictamente a la derecha
        return posicion_pico(v, medio+1, fin)
    else:
        # bajando (o en el pico), no descarto que pueda estar en el medio.
        return posicion_pico(v, ini, medio) 

"""
Justificacion de la complejidad:
Al tratarse de un ejercicio de D&C, puedo justificar la complejidad utilizando el Teorema Maestro:
T(n) = A.T(n/B) + f(n)

siendo:
A: cantidad de llamados recursivos = 1. nunca se realizan 2 llamados o mas al mismo tiempo
B: en cuanto se parte el problema = 2. mitad izquierda y derecha.
f(n): el costo de partir y juntar = O(n^C), C = 0. Ya que estamos hablando del costo de todo lo que no es recursivo es O(1), todo constante.

La ecuacion de recurrencia queda como: T(n) = T(n/2) + O(n⁰), T(n) = T(n/2) + O(1)

como:
logB(A) = C, log2(1) = 0
f(n) = θ(n^C . log^k(n)), con C = 0 y k = 0.

la ecuacion tiende a: T(n) = θ(n^C.log^(k+1)n) = θ(logn).
θ: es la cota superior e inferior al mismo tiempo.

La complejidad temporal es θ(logn)

La complejidad espacial es O(1), ya que manejamos punteros y al arreglo no lo modificamos.

"""