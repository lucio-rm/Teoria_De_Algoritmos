"""
Enunciado ejercicio 2:
(★) Se tiene un arreglo en el que se registran los resultados de tests automáticos de una porción de código. 
Este código se encontraba funcionando pero, debido a unos cambios que se están realizando, en algún momento dejó de funcionar. Se registra un 1 si pasa los tests, 0 en caso contrario. De esta manera, el arreglo tendrá la forma [1, 1, 1, ..., 0, 0, ...] (es decir, unos seguidos de ceros). Se pide: 
a. una función de orden O(logn) que, por división y conquista, encuentre el índice del primer 0, de forma que se pueda reconocer rápidamente en qué modificación del código se dejó de pasar los tests. 
Si no hay ningún 0 (solo hay unos), debe devolver -1. 
b. demostrar con el Teorema Maestro que la función es, en efecto, O(logn).

Ejemplos:

[1, 1, 0, 0, 0] →  2
[0, 0, 0, 0, 0] →  0
[1, 1, 1, 1, 1] → -1


"""

"""
planteo:
- Para evitar copiar arreglos y perder los índices originales, uso punteros `low` y `high`.
- Voy al medio. 
- Si el valor en `mid` es 0, evalúo si es el PRIMER 0. Lo es si `mid` es el primer elemento del arreglo (`mid == 0`) o si el elemento anterior es un 1. Si es el primer 0, devuelvo `mid`. Si no, el primer 0 debe estar a la izquierda, así que busco en la mitad izquierda.
- Si el valor en `mid` es 1, los 0s (si existen) deben estar obligatoriamente a la derecha. Busco en la mitad derecha.
"""
def indice_falla(arreglo):
    def busqueda_binaria(low, high):
        if low > high:
            return -1
            
        mid = (low + high) // 2
        
        if arreglo[mid] == 0:
            # ¿Es el primer cero?
            if mid == 0 or arreglo[mid - 1] == 1:
                return mid
            else:
                # El primer cero está más a la izquierda
                return busqueda_binaria(low, mid - 1)
        else:
            # Es un 1, el primer cero está a la derecha
            return busqueda_binaria(mid + 1, high)
            
    return busqueda_binaria(0, len(arreglo) - 1)

"""
justificacion de complejidad:
Utilizando el Teorema Maestro: T(n) = aT(n/b) + f(n)
- a = 1 (se realiza una sola llamada recursiva hacia la izquierda o la derecha).
- b = 2 (el espacio de búsqueda se reduce exactamente a la mitad).
- f(n) = O(1) (calcular el medio y comparar valores en índices específicos toma tiempo constante, no hay copias de arreglos).
Por lo tanto, T(n) = 1T(n/2) + O(1).
Calculamos log_b(a) = log_2(1) = 0.
Como f(n) = O(n^0) = O(1), estamos en el Caso 2 del Teorema Maestro.
Complejidad final: Θ(log n).
"""