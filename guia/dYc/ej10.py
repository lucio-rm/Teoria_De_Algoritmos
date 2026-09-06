"""
Enunciado ejercicio 10:
(★★★★) Resolver el ejercicio anterior, por división y conquista, en complejidad O(n), dada la misma aclaración. 
Justificar la complejidad de la solución.

"""

"""
planteo:
En O(n).

La idea es que sabemos que si o si , si hay un numero ganador mas de la mitad, tiene que haber 2 numeros de ese mismo uno al lado del otro.
El caso "borde" sería que el arreglo sea de cantidad impar y que justo el que mas se repita no tenga uno al lado del otro y el último elemento sea ese mismo. pero con una sola pasada (O(n)) lo chequeo y listo.

"""
def _mas_mitad_rec(arr):
    if len(arr) == 1:
        return arr[0] # si queda 1 elemento, ese mismo es el ganador

    posibles_ganadores = []
    for i in range(0, len(arr)-1, 2):
        if arr[i] == arr[i+1]:
            posibles_ganadores.append(arr[i])

    candidato = _mas_mitad_rec(posibles_ganadores) if posibles_ganadores != [] else None
    
    if candidato is not None and arr.count(candidato) > len(arr) // 2:
        return candidato
    
    if len(arr) % 2 != 0 and arr.count(arr[-1]) > len(arr) // 2:
            return arr[-1]
    
    return None

def mas_de_la_mitad(arr):
    candidato = _mas_mitad_rec(arr)
    return False if candidato is None or arr.count(candidato) <= len(arr) // 2 else True


"""
Complejidad: O(n)
Teorema Maestro, bla bla bla

"""