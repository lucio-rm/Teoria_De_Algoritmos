"""
Enunciado 09:
Implementar una función (que utilice división y conquista) de complejidad O(n logn) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución. Ejemplos:

[1, 2, 1, 2, 3] -> false
[1, 1, 2, 3] -> false
[1, 2, 3, 1, 1, 1] -> true
[1] -> true
Aclaración: Este ejercicio puede resolverse, casi trivialmente, ordenando el arreglo con un algoritmo eficiente, o incluso se puede realizar más rápido utilizando una tabla de hash. Para hacer interesante el ejercicio, resolver sin ordenar el arreglo, sino puramente división y conquista.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(n log(n))". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""
"""
planteo:
- segun teorema, el elemento mayoritario global tiene que ser mayoritario en alguna de las dos mitades.
con DyC, consigo los candidatos de izquierda y derecha.
si son iguales:
    tengo candidato absoluto
si son distintos:
    itero solo sobre ese segmento del arreglo cuantas veces aparecen y comparo

el que tenga mas de len(arr)//2, gana. si ninguno supera, devuelvo False


"""
def mas_de_la_mitad(arr):
    if not arr:
        return False

    candidato_final = _dyc_ganador(arr, 0, len(arr)-1)
    
    return candidato_final is not None

def _dyc_ganador(arr, ini, fin):
    if ini == fin:
        # queda 1 elemento, es el mayoría
        return arr[ini]

    medio = (ini + fin) // 2

    candidato_izq = _dyc_ganador(ini, medio)
    candidato_der = _dyc_ganador(medio+1, fin)

    # las dos mitades tienen el mismo ganador, devuelvo ese
    if candidato_izq == candidato_der:
        return candidato_izq

    # si no, cuento cuantas veces aparecen en el arr actual
    conteo_izq = conteo_der = 0

    for i in range(ini, fin+1):
        if arr[i] == candidato_izq:
            conteo_izq += 1
        elif arr[i] == candidato_der:
            conteo_der += 1

    #me fijo cual es mayoria del segmento
    mitad = (fin - (ini+1)) // 2 # cuento todos los elementos

    if candidato_izq is not None and conteo_izq > mitad:
        return candidato_izq
    elif candidato_der is not None and conteo_der > mitad:
        return candidato_der
    else:
        return None # no consiguieron pasar a la mitad.


"""
Justificacion de la complejidad:
Al ser un ejercicio de D&C puedo justificar la complejidad utilizando el Teorema Maestro:
T(n) = A.T(n/B) + f(n)

siendo:
- A: cantidad de llamados recursivos = 2. llamado recursivo para el candidato izquierdo y derecho
- B: en cuanto parte el problema = 2. mitad izquierda y derecha
- f(n): el costo de partir y juntar = O(n^C), C = 1. Ya que recorro esos subsegmentos.

La ecuacion de recurrencia queda:
T(n) = 2.T(n/2) + O(n)

y como:
- logB(A) = C, log2(2) = 1

La complejidad temporal es θ(n.logn)

Complejidad espacial O(1), al manejar todo por indices y ninguna copia ¿?
"""