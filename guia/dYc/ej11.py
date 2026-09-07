"""
Enunciado ejercicio 11:
(★★★★) Implementar una función, que utilice división y conquista, de complejidad O(n) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de dos tercios de las veces. 
Justificar la complejidad de la solución.

"""
"""
planteo:
mas de 2 tercios.
en vez de partir 2 mitades, tener 2 posibles ganadores, 
parto en 3 veces (B = 3), tengo 3 posibles ganadores

hago eso

o
en vez de comparar con  > len(arr) // 2
hago 3/4 * len(arr) -->  (len(arr)*3) // 4
"""

def _mas_tercios_rec(arr):
    if len(arr) == 1:
        return arr[0] # si queda 1 elemento, ese mismo es el ganador

    posibles_ganadores = []
    for i in range(0, len(arr)-1, 2):
        if arr[i] == arr[i+1]:
            posibles_ganadores.append(arr[i])

    candidato = _mas_tercios_rec(posibles_ganadores) if posibles_ganadores != [] else None
    
    if candidato is not None and arr.count(candidato) > (len(arr)*3) // 4:
        return candidato
    
    if len(arr) % 2 != 0 and arr.count(arr[-1]) > (len(arr)*3) // 4:
            return arr[-1]
    
    return None

def mas_de_la_tercios(arr):
    candidato = _mas_tercios_rec(arr)
    return False if candidato is None or arr.count(candidato) <= (len(arr)*3) // 4 else True


"""
Complejidad: O(n)
Teorema Maestro, bla bla bla

"""