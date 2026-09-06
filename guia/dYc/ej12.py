"""
Enunciado ejercicio 12:
(★★★) Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es). Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional (obviando el utilizado por la recursividad). 
Indicar y justificar su complejidad temporal.

Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). 
Luego, pensar a partir de allí el caso de 8 elementos, etc… para encontrar el patrón.

"""

"""
planteo:

con los casos bases ya estaria

2 elem
    C1, D1 -> return
4 elem
    C1, C2, D1, D2 -> swap arr[1] y arr[2]
8 elem
    misma cosa, llamado recursivo hasta tener 4 elementos
    
    
la teca es ver al arrelgo original partido en dos:
primer mitad: arrC
segunda mitad: arrD
y listo.
como es potencia de 2, sabemos que nunca va a ser impar y nos vamos a "comer" elementos.
"""

def modificado(arreglo):
    cant = len(arreglo)

    return _modificado_rec(arreglo, 0, cant // 2, cant//2, cant)

def _modificado_rec(arreglo, iniA, finA, iniB, finB):
    if iniA == finA and iniB == finB:
        # quedan 2 elementos totales del arreglo { C1, D1}
        return arreglo
    if iniA == (finA-1) and iniB == (finB-1):
        # quedan 4 elementos en total {C1, C2, D1, D2} tengo que hacer el swap
        arreglo[iniA], arreglo[iniB] = arreglo[iniB], arreglo[iniA]

    midA = (iniA + finA) // 2
    midB = (iniB + finB) // 2
    
    return _modificado_rec(arreglo, iniA, midA, iniB, midB) and _modificado_rec(arreglo, midA, finA, midB, finB)

"""
Justificacion de la complejidad:
para mantener la complejidad espacial en O(1), y no romperla, me manejo con variables constantes en O(1) y no rompo nada.
acceder al arreglo cuesta O(1)

después, teorema maestro bla bla bla
"""