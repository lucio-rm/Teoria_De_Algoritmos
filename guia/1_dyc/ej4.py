"""
Enunciado ejercicio 4:
(★) Se tiene un arreglo de N>=3 elementos en forma de pico, esto es: estrictamente creciente hasta una determinada posición 'p', y estrictamente decreciente a partir de ella (con 0<p<N-1). Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p=2. 
Se pide: 
a. Implementar un algoritmo de división y conquista de complejidad O(logn) que encuentre la posición p del pico. 

b. Justificar la complejidad del algoritmo mediante el teorema maestro.

"""

def forma_pico(arreglo):
    # Llamamos a la función auxiliar pasando el rango completo del arreglo
    return _pico_recursivo(arreglo, 0, len(arreglo) - 1)

def _pico_recursivo(arreglo, inicio, fin):
    # Caso base: cuando el rango se reduce a un solo elemento, ese es el pico
    if inicio == fin:
        return inicio
        
    medio = (inicio + fin) // 2
    
    # Comparamos con el vecino de la derecha para saber si vamos subiendo o bajando
    if arreglo[medio] < arreglo[medio + 1]:
        # Estamos subiendo: el pico está estrictamente a la derecha
        return _pico_recursivo(arreglo, medio + 1, fin)
    else:
        # Estamos bajando (o en el pico): el pico está a la izquierda o es el 'medio' actual
        return _pico_recursivo(arreglo, inicio, medio)


"""
Justificacion de la complejidad:
Teorema maestro: T(n) = A.T(n/B) + O(n^C)
siendo A: cantidad de llamados recursivos = 1. siempre 1, nunca 2 al mismo tiempo.
B: en cuánto partimos el problema = 2. o lado izquierdo o derecho.
C: el costo de todo lo que no es recursivo = 0. todo constante.

la ecuacion de recurrencia queda como:
T(n) = 1.T(n/2) + O(n^0) = T(n/2) + O(1)
como logB(A) = C, log2(1) = 0, la ecuacion tiende a O(n^Clogn) = O(n^0logn)

complejidad final = O(logn)

"""