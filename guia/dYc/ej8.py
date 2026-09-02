"""
Enunciado ejercicio 8:
(★) Dados un conjunto de n elementos, y 2 arreglos de longitud n, con dichos elementos. El arreglo A está completamente ordenado de menor a mayor. El arreglo B se encuentra desordenado. 
Indicar, por división y conquista, la cantidad de inversiones necesarias al arreglo B para que quede ordenado de menor a mayor, con un orden de complejidad mejor que O(n²). 
Justificar la complejidad del algoritmo mediante el teorema maestro.

"""
"""
planteo:
- Es una variante de Merge Sort (K&T Sección 5.3: Counting Inversions).
- Dividimos el arreglo B recursivamente.
- El truco está en el Merge: si el elemento de la mitad izquierda es mayor que el de la derecha, significa que está invertido respecto a TODOS los elementos restantes de la mitad izquierda (porque ambas mitades ya están ordenadas).
- La función debe retornar una tupla: (arreglo_ordenado, cantidad_de_inversiones) para no romper el estado de la recursión.
- El arreglo A es redundante asumiendo que los elementos tienen orden natural.
- Nota: Aquí SI podemos usar slices (arreglo[:mid]) porque el costo de combinar (Merge) ya es O(n). Sumar otro O(n) por el slice mantiene el f(n) = O(n), lo cual no rompe el Teorema Maestro (a diferencia del Ejercicio 2 donde f(n) debía ser O(1)).
"""
def inversiones(arrA, arrB):
    # arrA se ignora, asumimos elementos comparables por su valor.
    arreglo_ordenado, cant_inversiones = _merge_sort_conteo(arrB)
    return cant_inversiones

def _merge_sort_conteo(arreglo):
    if len(arreglo) <= 1:
        return arreglo, 0
        
    medio = len(arreglo) // 2
    
    # Desempaquetamos la tupla (arreglo, contador)
    izq, inv_izq = _merge_sort_conteo(arreglo[:medio])
    der, inv_der = _merge_sort_conteo(arreglo[medio:])
    
    # Hacemos el merge y obtenemos las inversiones que cruzan las mitades
    mergeado, inv_merge = _merge_y_cuenta(izq, der)
    
    # Inversiones totales = inv_izq + inv_der + inv_merge
    return mergeado, (inv_izq + inv_der + inv_merge)

def _merge_y_cuenta(izq, der):
    resultado = []
    i = j = inversiones = 0
    
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            # Flaw corregido: Si el de la derecha es menor, hay inversión con 
            # todos los elementos que quedan en la mitad izquierda.
            resultado.append(der[j])
            inversiones += (len(izq) - i)
            j += 1
            
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    
    return resultado, inversiones

"""
justificacion de la complejidad:

Utilizando el Teorema Maestro: T(n) = aT(n/b) + f(n)
- a = 2 (dos llamadas recursivas, partición izquierda y derecha).
- b = 2 (el arreglo se parte a la mitad en cada llamada).
- f(n) = O(n). La fusión recorre linealmente los elementos restantes. Los slices también son O(n). O(n) + O(n) = O(n).
Ecuación: T(n) = 2T(n/2) + O(n).
Calculamos log_b(a) = log_2(2) = 1.
El grado polinomial de f(n) es C = 1.
Como log_b(a) == C, estamos en el Caso 2 del Teorema Maestro.
Complejidad temporal final: Θ(n log n).
"""