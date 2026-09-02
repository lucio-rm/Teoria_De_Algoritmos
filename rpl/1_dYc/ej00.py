"""
Enunciado 00:
Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo contiguo de máxima suma, utilizando División y Conquista. 
Indicar y justificar la complejidad del algoritmo. 

Ejemplos:
[5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
[5, 3, -5, 4, -1] ->  [5, 3]
[5, -4, 2, 4, -1] -> [5, -4, 2, 4]
[5, -4, 2, 4] -> [5, -4, 2, 4]
[-3, 4, -1, 2, 1, -5] -> [4, -1, 2, 1]

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""

"""
planteo:
busco 3 candidateos:
1. el mejor subarreglo de izq-mid
2. el mejor subarreglo de mid-der
3. el mejor subarreglo continuo entre los dos

devuelvo el mejor de esos 3.
"""
def max_subarray(arr):
    if len(arr) == 1:
        return arr

    medio = len(arr) // 2

    sub_izq = max_subarray(arr[:medio])
    sub_der = max_subarray(arr[medio:])
    sub_cruzado = _subarreglo_continuo(arr)

    candidatos = (sum(sub_izq), sum(sub_der), sum(sub_cruzado)) # una tupla con los totales de sumar cada elementos de cada subarreglo
    ganador = max(candidatos)

    if ganador == candidatos[0]:
        return sub_izq
    elif ganador == candidatos[1]:
        return sub_der
    else:
        return sub_cruzado


#busco los indices mas grandes del lado izquierdo y derecho, los que estan entre medio van a ir al subarreglo
def _subarreglo_continuo(arr):
    medio = len(arr) // 2

    max_indice_izq = medio
    suma_total = 0 # para saber cuando parar
    suma_izq = 0
    
    for i in range(medio-1, -1, -1):
        suma_total += arr[i]
        if suma_total > suma_izq:
            suma_izq = suma_total
            max_indice_izq = i


    # reinicio, busco por derecha
    suma_total = 0
    suma_der = 0
    max_indice_der = medio

    for i in range(medio, len(arr)):
        suma_total += arr[i]
        if suma_total > suma_der:
            suma_der = suma_total 
            max_indice_der = i

    return arr[max_indice_izq:max_indice_der+1]




"""
Complejidad del algoritmo:

Al ser un algoritmo de División y Conquista, puedo justificar la complejidad utilizando el Teorema Maestro: T(n) = A.T(n/B) + f(n)
siendo:
n: la cantidad de elementos del arreglo
A: la cantidad de llamados recursivos = 2 . el del subarreglo derecho e izquierdo
B: en cuanto parto el problema = 2. En parte izquierda y derecha.
f(n) : el costo de partir y juntar los resultados = O(n^C), C = 1. la funcion "subarreglo_continuo" recorre en el peor de los casos todo el arreglo.

La ecuación de recurrencia queda como:
T(n) = 2.T(n/2) + O(n)

y como : logB(A) = C, log2(2) = 1, la ecuación tiende a ----> O(n^Clogn) = O(n.logn)



Complejidad espacial:  O(n), ya que en el peor de los casos voy a terminar "juntando" los dos lados del arreglo en uno.

"""