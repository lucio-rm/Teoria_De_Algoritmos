"""
Enunciado08:
Dados un conjunto de n elementos, y 2 arreglos de longitud n, con dichos elementos. El arreglo A está completamente ordenado de menor a mayor. El arreglo B se encuentra desordenado. Indicar, por división y conquista, la cantidad de inversiones necesarias al arreglo B para que quede ordenado de menor a mayor, con un orden de complejidad mejor que O(n^2). Justificar la complejidad del algoritmo mediante el teorema maestro.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "en tiempo mejor que O(n^2)". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""

"""
planteo:
- es una variante del merge sort
- divido B recursivamente (para el D&C)
- truco del merge: si el elemento de la mitad izquierda es mayor que el de la derecha, significa que esta invertido respecto a todos los elementos restantes de la mitad izquierda (porque las dos mitades ya estan ordenadas).
- segun investigue, el arreglo A es redundante asumiendo que los elmeento tienen orden natural.

"""

def contar_inversiones(A, B):
    arr_ordenado, cant_inversiones = _merge_sort_conteo(B)
    return cant_inversiones

def _merge_sort_conteo(arr):
    if len(arr) <= 1:
        return arr, 0 # no hay inversiones

    medio = len(arr) // 2

    # voy a querer guardarme las inversiones de los dos lados para agregarlas al total
    izq, inv_izq = _merge_sort_conteo(arr[:medio])
    der, inv_der = _merge_sort_conteo(arr[medio:])

    # hago el merge y cuento las inversiones que cruzan las mitades
    mergeado, inv_merge = _merge_y_cuenta(izq, der)

    #inversiones totales :
    return mergeado, (inv_izq + inv_der + inv_merge)


def _merge_y_cuenta(izq, der):
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            # si el de la derecha es menor, hay inversion con todos los elementos que quedan en la mitad izquierda
            resultado.append(der[j])
            inversiones += (len(izq) - i)
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])

    return resultado, inversiones



"""
Justificacion de la complejidad:

Al ser un ejercicio de Division y Conquista, puedo verificar la complejidad temporal usando el Teorema Maestro: T(n) = A.T(n/B) + f(n)
(lo mismo que un merge sort)

Complejidad temporal: O(nlogn)
Complejidad espacial: O(n)
"""