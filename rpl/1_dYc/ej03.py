"""
Enunciado 03:
Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número n, en tiempo O(log n). Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe devolver 5. Justificar el orden del algoritmo.

Aclaración: no se requiere el uso de ninguna librería de matemática que calcule la raíz cuadrada, ni de forma exacta ni aproximada.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(log(n))". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""
"""
planteo:
casos bases:
n < 0 ¿?
n = 0, devuelvo 0
n = 1, devuelvo 1
.
para lograr un logn, tengo que descartar la mitad de los resultados posibles.

sé que los resultados posibles E [1, n].
voy a n//2, si el cuadrado del medio no es == n, 
- si < n, 
    se que el resultado es [medio, n]
- si > n,
    [1, medio]
    
voy guardando en una variable la "mejor aproximacion", por las dudas de nunca encontrar un a / a² == n

"""

def parte_entera_raiz(n):
    if n < 0:
        return 0 #¿? no se que devolvería.
    elif n == 1 or n == 0:
        return n
    
    return _busqueda_recursiva(n, 1, n, 1)

def _cuadrado(n):
    return n*n

def _busqueda_recursiva(n, ini, fin, mejor_aprox):
    if ini > fin:
        return mejor_aprox # ya no me queda para llamar recursivamente, devuelvo lo mejor que encontré

    medio = (ini + fin) // 2

    if _cuadrado(medio) == n:
        return medio
    elif _cuadrado(medio) < n:
        # mid candidato valido, pero puede haber uno mejor
        return _busqueda_recursiva(n, medio+1, fin, medio)
    else:
        # medio² > n
        return _busqueda_recursiva(n, ini, medio-1, mejor_aprox) #busco uno mas chico


"""
Justificacion de la complejidad:

Al ser un ejercicio de D&C, puedo justificar la complejidad temporal utilizando el Teorema Maestro: 
T(n) = A.T(n/B) + f(n).
siendo:
A: cantidad de llamados recursivos = 1. siempre se ejecuta 1 llamado, nunca 2 o más
B: en cuanto se parte el problema = 2. se parte a la mitad.
f(n): el costo de partir y juntar = O(n^C), C = 0, ya que el costo de todo lo que no es recursivo es constante (O(1)). "_cuadrado()" es O(1), y el resto son puros "if".

La ecuación de recurrencia queda como:
T(n) = T(n/2) + O(n⁰) = T(n/2) + O(1)

y como logB(A) = C, log2(1) = 0, la ecuacion tiende a O(n^C.logn) = O(n⁰logn) = O8logn)

La complejidad temporal es O(logn)

La complejidad espacial es O(1), ya que utilizamos variables y llamados constantes. todo O(1).

"""