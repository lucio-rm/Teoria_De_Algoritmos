"""
Enunciado 06:

Implementar un algoritmo de multiplicación de dos números grandes de longitud n, por división y conquista, con un orden de complejidad mejor que O(n^2). Justificar la complejidad del algoritmo mediante el teorema maestro.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en tiempo mejor que O(n^2)". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""


"""
planteo:
uso el Algoritmo de Karatsuba 
Si hago las multiplicaciones normalmente, haría 4 multiplicaciones de sub-problemas. (O(n²)) 
Para mejorar O(n²), tengo que reducir las multiplicaciones a 3.
teniendo:
x = x1 * 10^m + x0
y = y1 * 10^m + y0

hago 4 pasos
- 1: calculo la longitud máxima (n) de los dos números. mitad m = n // 2.
- 2: parto 'x' e 'y'  (//) y (%) por 10^m.
- 3: hago las 3 multiplicaciones de Karatsuba.
    . z0 = x0 * y0
    . z2 = x1 * y1
    . z1 = (x0 + x1) * (y0 + y1)
- 4: reconstruyo el resultado con la fórmula de Gauss: z2*10^(2m) + (z1 - z2 - z0)*10^m + z0.

"""

def multiplicar(x, y): # a , b
    # caso base: si alguno de los numeros es de 1 digito
    if x < 10 or y < 10:
        return x * y
    
    # convierto a string solo para saber la cantidad de digitos (n)
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    divisor = 10 ** m
    
    x1 = x // divisor  #mitad izquierda
    x0 = x % divisor   # mitad derecha
    
    y1 = y // divisor
    y0 = y % divisor
    
    # las 3 llamadas recursivas de Karatsuba
    z0 = multiplicar(x0, y0)
    z2 = multiplicar(x1, y1)
    z1 = multiplicar(x0 + x1, y0 + y1)
    
    # combinacion de resultados
    return (z2 * (10 ** (2 * m))) + ((z1 - z2 - z0) * (10 ** m)) + z0

"""
justificacion de la complejidad:

Al ser un ejercicio de D&C, puedo utilizar el Teorema Maestro para justificar la complejidad:
T(n) = A.T(n/B) + f(n)

siendo:
- A: cantidad de llamadas recursivas = 3. se hacen exactamente 3 llamadas recursivas: z0, z1, z2
- B: en cuanto se parte el problema = 2. los numeros se parten a la mitad en cada llamada
- f(n): cuanto cuesta partir y juntar = O(n^C), C = 1. las sumas de los numeros y los corrimientos por 10^m toman tiempo lineal respecto a la cantidad de digitos n

La ecuacion de recurrencia queda como: T(n) = 3T(n/2) + O(n).
y como logB(A) > C, log2(3) ≈ 1.58. 1.58 > 1

Complejidad temporal final: Θ(n^(log2(3))) ≈ Θ(n^1.58), que es  menor a O(n²)

Complejidad espacial ?
"""