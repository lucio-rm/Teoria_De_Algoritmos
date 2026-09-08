"""
Enunciado 12:
Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es). Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional (obviando el utilizado por la recursividad y variables de tipos simples). ¿Cual es la complejidad del algoritmo?

Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). Luego, pensar a partir de allí el caso de 8 elementos, etc… para encontrar el patrón.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""
"""
planteo:
- no usar espacio adicional
- pienso en dividir el arreglo en dos mitades 
  (A y B). Cada mitad se divide en dos cuartos. 
  Arreglo original: [C1, C2, C3, C4] | [D1, D2, D3, D4]
- agarro el segundo cuarto [C3, C4] y lo swapeo completamente 
  con el tercer cuarto [D1, D2] 
  queda: [C1, C2] + [D1, D2] | [C3, C4] + [D3, D4]
- ahora la primera mitad tiene todos los sub-indices de la primera mitad, y la 
  segunda tiene los sub-indices de la segunda mitad. Llamo a División y 
  Conquista recursivamente en la mitad izquierda y en la derecha.
"""

def alternar(arreglo):
    _modificado_rec(arreglo, 0, len(arreglo))
    return arreglo

def _modificado_rec(arreglo, ini, fin):
    n = fin - ini
    
    #caso base: Si quedan 2 elementos (C_i, D_i), ya están en posición
    if n <= 2:
        return
        
    mid = ini + (n // 2)
    cuarto = n // 4
    
    # hago el swap
    for i in range(cuarto):
        indice_izq = ini + cuarto + i
        indice_der = mid + i
        arreglo[indice_izq], arreglo[indice_der] = arreglo[indice_der], arreglo[indice_izq]
        
    # Llamadas recursivas a las nuevas mitades particionadas
    _modificado_rec(arreglo, ini, mid)
    _modificado_rec(arreglo, mid, fin)

"""
Justificación de la complejidad:
Para el Teorema Maestro: T(n) = A.T(n/B) + O(n^C)
- A = 2 (Hacemos dos llamadas recursivas: mitad izquierda y mitad derecha).
- B = 2 (Cada sub-arreglo es exactamente la mitad del tamaño de n).
- f(n) = O(n). El ciclo for hace n // 4 operaciones de swap. Descartando 
  la constante (1/4), el costo de partir los bloques in-situ es lineal respecto 
  a 'n', por ende C = 1.

Calculamos log_B(A) = log_2(2) = 1.
Como log_B(A) == C (1 == 1), estamos en el caso 2 del Teorema Maestro.
La ecuación tiende a O(n^C * log n).
Complejidad temporal final: Θ(n log n).
Complejidad espacial: O(1) auxiliar (cumpliendo con el requerimiento de no 
utilizar espacio adicional más allá de la pila de recursión).
"""