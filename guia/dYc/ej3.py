"""
Enunciado ejercicio 3:
(★) Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número n, en tiempo O(logn). 
Por ejemplo, para n=10 debe devolver 3, y para n=25 debe devolver 5. 

Justificar la complejidad del algoritmo.

"""

"""
planteo:
- El espacio de posibles respuestas para la parte entera de la raíz cuadrada de `n` (para n >= 1) está comprendido siempre entre 0 y `n`.
- Utilizo búsqueda binaria sobre este rango de valores [0, n].
- Calculo el punto medio `mid`. Si `mid * mid == n`, esa es la raíz exacta.
- Si `mid * mid < n`, `mid` podría ser la respuesta (porque buscamos la parte entera, redondeada hacia abajo), así que la guardo, pero sigo buscando en la mitad superior `[mid + 1, high]` por si existe un entero mayor que cumpla.
- Si `mid * mid > n`, `mid` es demasiado grande, descarto la mitad superior y busco en la inferior `[low, mid - 1]`.
"""

def parte_entera_raiz(n):
    if n < 0:
        return -1 # Caso de error no manejable en reales
    if n == 0 or n == 1:
        return n
        
    def busqueda_binaria(low, high, mejor_respuesta):
        if low > high:
            return mejor_respuesta
            
        mid = (low + high) // 2
        cuadrado = mid * mid
        
        if cuadrado == n:
            return mid
        elif cuadrado < n:
            # 'mid' es un candidato válido, pero podría haber uno más grande.
            return busqueda_binaria(mid + 1, high, mid)
        else:
            # 'mid' se pasó, busco un número más chico.
            return busqueda_binaria(low, mid - 1, mejor_respuesta)

    return busqueda_binaria(1, n, 1)

"""
justificacion de complejidad:
Utilizando el Teorema Maestro: T(N) = aT(N/b) + f(N)
*(Nota: Aquí N no es el tamaño de un arreglo, sino el VALOR del número de entrada n, o más precisamente, el tamaño del espacio de búsqueda [0, n]).*
- a = 1 (una sola llamada recursiva).
- b = 2 (el espacio de valores posibles se divide a la mitad en cada paso).
- f(N) = O(1) (las multiplicaciones y comparaciones numéricas se asumen de tiempo constante).
La ecuación es T(N) = T(N/2) + O(1).
Calculamos log_b(a) = log_2(1) = 0.
Por Teorema Maestro (Caso 2), la complejidad es Θ(log n). 
"""