"""
Enunciado 10:
Implementar una función (que utilice división y conquista) de complejidad O(n) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución.

Aclaración: Este ejercicio puede resolverse, casi trivialmente, utilizando una tabla de hash. Para hacer interesante el ejercicio, resolver puramente por división y conquista.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(n)". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
"""


"""
planteo:

como lo haces O(n) ¿?
siendo D&C, sabes que tenes que hacer 2 llamados y 2 particiones (o 3 y 3, o 4 y 4, etc.) asi me queda logB(A) = 1. con C = 0. entonces, no tengo que hacer un recorrido mas.

"""

def mas_de_la_mitad(arr):
    return False


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

    # tengo que saber como contar cual aparecemas veces en O(1).
    # # si no, cuento cuantas veces aparecen en el arr actual
    # conteo_izq = conteo_der = 0

    # for i in range(ini, fin+1):
    #     if arr[i] == candidato_izq:
    #         conteo_izq += 1
    #     elif arr[i] == candidato_der:
    #         conteo_der += 1

    #me fijo cual es mayoria del segmento
    mitad = (fin - (ini+1)) // 2 # cuento todos los elementos

    if candidato_izq is not None and conteo_izq > mitad:
        return candidato_izq
    elif candidato_der is not None and conteo_der > mitad:
        return candidato_der
    else:
        return None # no consiguieron pasar a la mitad.

