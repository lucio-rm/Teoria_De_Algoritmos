"""
Enunciado 02:
Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros). Se pide una función de complejidad O(log(n)) que encuentre el índice del primer 0. Si no hay ningún 0 (solo hay unos), debe devolver -1.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "en O(log(n))". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción (se hacen pruebas de volumen que deben ejecutar correctamente)

"""
"""
planteo:
tengo que devolver el indice del primer 0.

voy al medio del arreglo. 
si medio es 0 
    es el primer 0 si el de la izquierda al medio es un 1.
    si el de la izquierda es un 0, descarto toda 
si medio es 1
    el de la derecha es 0, entonces es el primer 0
    el de la derecha es 1, decarto mitad izquierda

"""
def indice_primer_cero(arr):
    # caso borde: si el ultimo elemento es 1, no hay ceros.
    if arr[len(arr)-1] == 1:
        return -1
    return _primer_cero_rec(arr, 0, len(arr) - 1)

def _primer_cero_rec(arr, ini, fin):
    if ini > fin:
        return -1
        
    medio = (ini + fin) // 2
    
    # evaluo la convergencia exacta
    if arr[medio] == 0:
        # si es el inicio absoluto o el anterior es 1, es el primer cero
        if medio == 0 or arr[medio - 1] == 1:
            return medio
        # Si no es el primero, el límite está a la izquierda.
        return _primer_cero_rec(arr, ini, medio - 1)
        
    elif arr[medio] == 1:
        # Si es 1, sabemos que el primer 0 debe estar estrictamente a la derecha
        # tambien verifico su vecino inmediato derecho para cortar rapido
        if medio < len(arr) - 1 and arr[medio + 1] == 0:
            return medio + 1
        return _primer_cero_rec(arr, medio + 1, fin)



"""
justificacion de la complejidad:

Al ser un ejercicio de D&C, se pued ejustificar la complejidad temporal utilizando el Teorema Maestro: T(n) = A.T(n/B) + f(n)

siendo:
A: cantidad de llamados recursivos = 1. ya que siempre se realiza el llamado para el lado izq o lado der
B: en cuanto se parte el problema = 2. se parte en lado izq y der
f(n): el costo de partir y juntar = O(n^C), C = 0. Ya que el costo de todo lo que no es recursivo es constante.

La ecuacion de recurrencia queda como:
T(n) = T(n/2) + O(1)

y como logB(A) = C, log2(1) = 0, la ecuacion tiende a O(n^C.logn) = O(logn)

La complejidad temporal es O(logn)

La complejidad espacial es O(n), siendo n la cantidad de elementos en el arrelgo. Ya que paso una copia del arreglo por cada llamado recursivo, terminando en O(n/2). O(n/2) = O(n).

"""
