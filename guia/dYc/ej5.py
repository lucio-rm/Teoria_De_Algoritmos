"""
Enunciado ejercicio 5:
(★) Implementar Merge Sort. Justificar la complejidad del algoritmo mediante el teorema maestro.

"""

"""
planteo:
El arreglo se divide recursivamente a la mitad hasta llegar a sub-arreglos de 1 elemento (que por definición están ordenados).
Luego, la función de D&C comienza a retornar y se ejecuta el "Merge", que toma dos sub-arreglos ordenados y los fusiona en uno solo ordenado en tiempo lineal O(n).
Pregunta clave: ¿Cómo evito redundancias? Hago que la misma función principal sea la recursiva.
"""
def merge_sort(arreglo):
    # Caso base: 0 o 1 elemento ya están ordenados.
    if len(arreglo) <= 1:
        return arreglo
    
    # División
    medio = len(arreglo) // 2
    
    # Conquista (Llamado recursivo a la MISMA función)
    izq = merge_sort(arreglo[:medio])
    der = merge_sort(arreglo[medio:])
    
    # Combinación
    return _merge(izq, der)

def _merge(izq, der):
    resultado = []
    i = j = 0
    
    # Comparamos elemento por elemento hasta agotar una de las mitades
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
            
    # Agregamos los remanentes (si una mitad era más larga que la otra)
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    
    return resultado

"""
justificacion de complejidad:

Utilizando el Teorema Maestro: T(n) = aT(n/b) + f(n)
- a = 2 (se hacen dos llamados recursivos, mitad izquierda y mitad derecha).
- b = 2 (el arreglo original se parte a la mitad).
- f(n) = O(n). El costo de f(n) es el costo de DIVIDIR y COMBINAR. El "slicing" en Python cuesta O(n), y la función `_merge` recorre todos los elementos de ambas mitades con un loop while, lo cual también es estrictamente O(n).
Por lo tanto: T(n) = 2T(n/2) + O(n)
Calculamos log_b(a) = log_2(2) = 1.
El grado polinomial de f(n) es C = 1. 
Como log_b(a) == C, estamos en el Caso 2 del Teorema Maestro.

Complejidad final: Θ(n^1 * log n) = Θ(n log n).
"""