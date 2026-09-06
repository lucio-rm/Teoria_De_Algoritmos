"""
Enunciado ejercicio 10:
(★★★★) Resolver el ejercicio anterior, por división y conquista, en complejidad O(n), dada la misma aclaración. 
Justificar la complejidad de la solución.

"""

"""
planteo:
- Para bajar la complejidad a O(n), no podemos dividir el arreglo en dos y 
  hacer dos llamadas recursivas, porque T(n) = 2T(n/2) + O(n) da O(n log n).
- Necesitamos una sola llamada recursiva: T(n) = T(n/2) + O(n).
- La estrategia es el emparejamiento (Tournament). Si un elemento aparece más de 
  la mitad de las veces, al agrupar los elementos de a pares adyacentes, al 
  menos un par debe estar formado por dos copias de ese elemento ganador.
- Descartamos los pares donde los elementos son distintos. De los pares iguales, 
  guardamos solo un representante y llamamos a la recursión sobre este nuevo 
  arreglo (que mide a lo sumo n/2). 
- El candidato que sobrevive se cuenta linealmente en todo el arreglo original 
  para confirmar si superó la mitad.

"""

def _candidato_mayoritario(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    pares_iguales = []
    # Emparejamos de a dos. Si son iguales, sobrevive uno a la siguiente ronda.
    for i in range(0, len(arr) - 1, 2):
        if arr[i] == arr[i+1]:
            pares_iguales.append(arr[i])

    # Una ÚNICA llamada recursiva sobre un arreglo de tamaño <= n/2
    candidato = _candidato_mayoritario(pares_iguales)

    # Verificamos si el candidato de las rondas superiores es mayoría aquí
    if candidato is not None and arr.count(candidato) > len(arr) // 2:
        return candidato
    
    # Caso borde: si el arreglo es impar, el último elemento quedó sin pelear
    if len(arr) % 2 != 0 and arr.count(arr[-1]) > len(arr) // 2:
        return arr[-1]

    return None

def aparece_mas_mitad(arr):
    return _candidato_mayoritario(arr) is not None

"""
Justificación de la complejidad:
Utilizando el Teorema Maestro: 
Ecuación: T(n) = A.T(n/B) + O(n^C)
- A = 1 (Se realiza una sola llamada recursiva hacia 'pares_iguales').
- B = 2 (El nuevo arreglo tiene como máximo la mitad de los elementos).
- f(n) = O(n). Recorrer el arreglo para armar los pares cuesta O(n), y contar 
  el candidato con `arr.count()` cuesta O(n). Por ende C = 1.

Calculamos log_B(A) = log_2(1) = 0.
Como C > log_B(A) (es decir, 1 > 0), estamos en el caso donde el esfuerzo de 
dividir y combinar domina.
La ecuación tiende a O(n^C) = O(n^1) = O(n).
"""