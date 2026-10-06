"""
Enunciado ejercicio 1:
Implementar una función que, dado un arreglo *ordenado y sin repetidos* de valores enteros no negativos, obtenga el mínimo valor que *no* se enceuntre en el arreglo. 
Indicar y justificar adecuadamente la complejidad del algoritmo.

Por ejemplo:

minimoExcluido([0, 1, 5]) --> 2
minimoExcluido([1, 3, 5]) --> 0
minimoExcluido([0, 1, 2, 3, 4, 5]) --> 6
minimoExcluido([0, 1, 2, 3, 4, 5, 1234567]) --> 6
"""
"""
planteo:

- ordenado y sin repetidos valores > 0.
- obtener el minimo valor que no se encuentre en el arrelgo

es un ejercicio de algo2 wacho. que onda

dyc avanzado mis dos huevovich


idea:
indices.
mirar losindices. 
si el medio esta corrido, significa que el minimo esta a la izquierda (y se descarta la mitad derecha).
si no esta corrido, descartas mitad izq

el mínimo valor, tengo que ir guardandolo.
"""

def minimoExcluido(arreglo):
    if not arreglo: 
        return -1
    n = len(arreglo)
    ini = 0
    minimo = float('inf')
    return _minimo_dyc(arreglo, ini, n, minimo)
def _minimo_dyc(arreglo, ini, fin, minimo):
    if ini > fin:
        # si ya no quedan elementos para devolver, el minimo es la cantidad de elementos (significa que está ordenado)
        # es el que le sigue a arreglo[n-1]
        # siempre y cuando sea menor a lo que encontramos
        return len(arreglo) if len(arreglo) < minimo else minimo
    
    medio = (ini + fin) // 2

    if arreglo[medio] != medio:
        #significa que está desfazado y el problema esta en el lado izquierdo
        # el medio es un posible sospechoso. pero como sabemos que el problema esta del lado izquierdo, lo ponemos como "techo"
        return _minimo_dyc(arreglo, ini, medio-1, medio)
    else:
        return _minimo_dyc(arreglo, medio, fin, minimo) # medio nuevo piso. el minimo sigue siendo éste.
        # si no esta desfazado el medio, puede estar ordenado y el minimo terminar siendo len(arreglo).

"""
justificacion de la complejidad:

--------- temporal: θ(logn), siendo n la cantidad de elementos en el arreglo.

la ecuación de recurrencia del algoritmo implementado es T(n) = 1.T(n/2) + O(1)
por cada nivel de ejecución y de recursión, se parte el problema a la mitad, y me quedo con una de éstas.

Al tratarse de un problema de División y Conquista, puedo utilizar el Teorema Maestro para tender la ecuación de recurrencia a la complejidad temporal.
T(n) = A.T(n/B) + f(n)
siendo
- A: cantidad de llamados recursivos = 1. Siempre se ejecuta 1 llamado en la función quedandose con 1 mitad.
- B: en cuánto se parte el problema = 2. Se parte entre el lado izquierdo y lado derecho.
- f(n): el costo de combinar y juntar = θ(n^C . log^(k)n) , y como el costo de todo lo que no es recursivo es constante: θ(1), con C = 0 y k = 0.

Y el Teorema maestro nos brinda de que, como logB(A) == C, log2(1) == 0, la complejidad temporal queda como:
θ(n^C . log^(k+1)n), reemplazando los valores de C y k: θ(logn).

También se puede pensar el algoritmo como Búsqueda binaria, siendo muy similar.

-------- espacial: O(1). siendo el espacio adicional utilizado con puras variables constantes.

¿call stack afecta? 

"""

