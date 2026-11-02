"""
Enunciado ejercicio 12:
(★★★) Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es). Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional (obviando el utilizado por la recursividad). 
Indicar y justificar su complejidad temporal.

Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). 
Luego, pensar a partir de allí el caso de 8 elementos, etc… para encontrar el patrón.

"""

"""
planteo:
- El enunciado exige no utilizar espacio adicional (O(1) espacial). Hacer un swap 
  de elementos individuales destruye la secuencia, y tu código fallaba al 
  intentar cruzar llamadas lógicas usando `and`.
- El algoritmo requiere mover bloques enteros. Dividimos el arreglo en dos mitades 
  (A y B). Cada mitad se divide en dos cuartos. 
  Arreglo original: [C1, C2, C3, C4] | [D1, D2, D3, D4]
- Tomamos el SEGUNDO cuarto [C3, C4] y lo intercambiamos (swap) completamente 
  con el TERCER cuarto [D1, D2] como se grafica en las filminas.
  Queda: [C1, C2] + [D1, D2] | [C3, C4] + [D3, D4]
- Ahora la primera mitad tiene todos los sub-índices de la primera mitad, y la 
  segunda tiene los sub-índices de la segunda mitad. Llamamos a División y 
  Conquista recursivamente en la mitad izquierda y en la derecha.
"""

def modificado(arreglo):
    _modificado_rec(arreglo, 0, len(arreglo))
    return arreglo

def _modificado_rec(arreglo, ini, fin):
    n = fin - ini
    
    # Caso base: Si quedan 2 elementos (C_i, D_i), ya están en posición
    if n <= 2:
        return
        
    mid = ini + (n // 2)
    cuarto = n // 4
    
    # Swap entre el segundo cuarto y el tercer cuarto
    # Segundo cuarto empieza en 'ini + cuarto'
    # Tercer cuarto empieza en 'mid'
    for i in range(cuarto):
        idx_izq = ini + cuarto + i
        idx_der = mid + i
        arreglo[idx_izq], arreglo[idx_der] = arreglo[idx_der], arreglo[idx_izq]
        
    # Llamadas recursivas a las nuevas mitades particionadas
    _modificado_rec(arreglo, ini, mid)
    _modificado_rec(arreglo, mid, fin)

"""
Justificación de la complejidad:
Para el Teorema Maestro: T(n) = A.T(n/B) + O(n^C)
- A = 2 (Hacemos dos llamadas recursivas: mitad izquierda y mitad derecha).
- B = 2 (Cada sub-arreglo es exactamente la mitad del tamaño de n).
- f(n) = O(n). El ciclo `for` realiza `n // 4` operaciones de swap. Descartando 
  la constante (1/4), el costo de partir los bloques in-situ es lineal respecto 
  a 'n', por ende C = 1.

Calculamos log_B(A) = log_2(2) = 1.
Como log_B(A) == C (1 == 1), estamos en el caso 2 del Teorema Maestro.
La ecuación tiende a O(n^C * log n).
Complejidad temporal final: Θ(n log n).
Complejidad espacial: O(1) auxiliar (cumpliendo con el requerimiento de no 
utilizar espacio adicional más allá de la pila de recursión).
"""