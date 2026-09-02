"""
Enunciado 05:

Implementar Merge Sort. Justificar la complejidad del algoritmo mediante el teorema maestro.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea de ordenamiento "por Merge Sort". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""
"""
planteo:
merge sort. Ordenamiento con complejidad O(nlogn).
partis el arreglo en subarreglos, y al final haces un merge con los dos subarreglos (izq y der)

"""
def merge_sort(arr):
    # tengo 1 o 0 elementos, estarían ya ordenados.
    if len(arr) <= 1:
        return arr

    medio = len(arr) // 2

    izq = merge_sort(arr[:medio])
    der = merge_sort(arr[medio:])
    
    return _merge(izq, der)

def _merge(arr_i, arr_d):
    devuelvo = []
    i = j = 0

    # comparo hasta terminar con una de las mitades
    while i < len(arr_i) and j < len(arr_d):
        if arr_i[i] <= arr_d[j]:
            devuelvo.append(arr_i[i])
            i += 1
        else:
            devuelvo.append(arr_d[j])
            j += 1

    # agrego los que quedan. uso "extend" que agrega todos los elementos de un arreglo iterable al final de otro.
    devuelvo.extend(arr_i[i:])
    devuelvo.extend(arr_d[j:])

    # fijese que siempre priorizo el lado izquierdo ,  asi mantengo la "estabilidad" del MergeSort
    # estable = mantiene el orden del arrelgo original. si hay dos "6" , el que estaba antes que el otro, va a mantenerse asi.
    
    return devuelvo


"""
Justificacion de la complejidad:
Al ser un algoritmo de Division y Conquista, puedo verificar la complejidad utilizando el Teorema Maestro:
T(n) = A.T(n/B) + f(n)

siendo:
A: cantidad de llamados recursivos = 2. siempre llamo para lado izquierdo y derechod el arreglo
B: en cuanto parte el problema = 2. lado izquierdo y derecho.
f(n) el costo de partir y juntar = O(n^C), C = 1. Ya que el "slicing" en Python cuesta O(n), y la función "_merge" recorre todos los elementos de ambas mitades con un loop while, lo cual también es estrictamente O(n).

La ecuacion de recurrencia queda como:

T(n) = T(n/2) + O(n)

y como:
. logB(A) = C, log2(2) = 1
. f(n) = θ(n^C . log^(k)n), con C = 1 y k = 0.

la ecuacion tiende a: T(n) = θ(n^C.log^(k+1)n) = θ(n.logn).
θ: es la cota superior e inferior al mismo tiempo.

La complejidad temporal es θ(nlogn)

La complejidad espacial es O(n), ya que manejar slicing en Python manda copias del arreglo original en cada llamado recursivo. Y además, a la lista "devolver" la llenamos de N elementos.
(siendo O(n) + O(n) = O(2n) = O(n))

"""