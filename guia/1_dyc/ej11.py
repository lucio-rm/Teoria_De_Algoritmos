"""
Enunciado ejercicio 11:
(★★★★) Implementar una función, que utilice división y conquista, de complejidad O(n) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de dos tercios de las veces. 
Justificar la complejidad de la solución.

"""
"""
planteo:
- Tu instinto de partir en 3 o de alterar las fracciones internas del algoritmo 
  destruye las matemáticas del emparejamiento. Si eliminas un par de elementos 
  distintos, eliminas a lo sumo UN elemento de la mayoría. Si tu umbral interno 
  es 3/4, podrías descartar al ganador prematuramente.
- El Invariante Lógico: Si un número $X$ aparece en más de $2/3$ del arreglo, 
  entonces $X$ aparece estrictamente en más de $1/2$ del arreglo.
- No hay que tocar el algoritmo interno. Usamos EXACTAMENTE la misma función de 
  emparejamiento del Ejercicio 10 para extraer al único candidato posible. 
- La única diferencia ocurre en la función "wrapper" final, donde contamos si 
  ese candidato supera los 2/3 en lugar del 1/2.


"""

def mas_de_dos_tercios(arr):
    candidato = _candidato_mayoritario(arr)
    
    if candidato is None:
        return False
        
    # Solo alteramos la validación global
    return arr.count(candidato) > (len(arr) * 2) // 3


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
"""
Justificación de la complejidad:
La complejidad recae netamente en `_candidato_mayoritario(arr)`, el cual ya 
fue demostrado mediante el Teorema Maestro como estrictamente O(n). 
La operación adicional `arr.count(candidato)` recorre el arreglo una vez en 
tiempo O(n). 
O(n) + O(n) = O(n). Complejidad temporal final: O(n).
"""