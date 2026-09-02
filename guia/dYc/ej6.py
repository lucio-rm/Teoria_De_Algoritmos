"""
Enunciado ejercicio 6:
(★) Implementar un algoritmo de multiplicación de dos números grandes de longitud n, por división y conquista, con un orden de complejidad mejor que O(n²).

Justificar la complejidad del algoritmo mediante el teorema maestro.

"""

"""
planteo:
Este es el Algoritmo de Karatsuba (Kleinberg & Tardos 5.5). 
Si multiplico normalmente, hago 4 multiplicaciones de sub-problemas. 
Para mejorar O(n²), debo reducir las multiplicaciones a 3.
x = x1 * 10^m + x0
y = y1 * 10^m + y0
Paso 1: Calculo la longitud máxima (n) de los dos números. Calculo la mitad m = n // 2.
Paso 2: Parto 'x' e 'y' usando división entera (//) y módulo (%) por 10^m.
Paso 3: Hago las 3 multiplicaciones de Karatsuba.
- z0 = x0 * y0
- z2 = x1 * y1
- z1 = (x0 + x1) * (y0 + y1)
Paso 4: Reconstruyo el resultado con la fórmula de Gauss: z2*10^(2m) + (z1 - z2 - z0)*10^m + z0.
"""
def mult_big_int(x, y):
    # Caso base: si alguno de los números es de 1 dígito (menor a 10)
    if x < 10 or y < 10:
        return x * y
    
    # Convertimos a string solo para saber la cantidad de dígitos (n)
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    divisor = 10 ** m
    
    # Partimos los números matemáticamente
    x1 = x // divisor  # Mitad alta (izquierda)
    x0 = x % divisor   # Mitad baja (derecha)
    
    y1 = y // divisor
    y0 = y % divisor
    
    # Las 3 llamadas recursivas de Karatsuba
    z0 = mult_big_int(x0, y0)
    z2 = mult_big_int(x1, y1)
    z1 = mult_big_int(x0 + x1, y0 + y1)
    
    # Combinación de resultados
    return (z2 * (10 ** (2 * m))) + ((z1 - z2 - z0) * (10 ** m)) + z0

"""
justificacion de la complejidad:

Utilizando el Teorema Maestro: T(n) = aT(n/b) + f(n)

- a = 3 (Se hacen exactamente 3 llamadas recursivas: z0, z1, z2).
- b = 2 (Los números se parten a la mitad en cada llamada).
- f(n) = O(n) (Las sumas de los números y los corrimientos por 10^m toman tiempo lineal respecto a la cantidad de dígitos n).

Ecuación: T(n) = 3T(n/2) + O(n).
Calculamos log_b(a) = log_2(3) ≈ 1.58.
Como el grado polinomial de f(n) es C=1, tenemos que C < log_b(a) (1 < 1.58).

Estamos en el Caso 1 del Teorema Maestro.
Complejidad final: Θ(n^(log_2 3)) ≈ Θ(n^1.58), que es estrictamente menor a O(n²).
"""