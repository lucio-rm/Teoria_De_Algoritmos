"""
Enunciado ej.11:
Escribir un algoritmo que, utilizando backtracking, dada una lista de enteros positivos L y un entero n devuelva todos los subconjuntos de L que suman exactamente n.

"""
"""
planteo:

subset sum ¿?

lista de enteros y subconjuntos que de n

es como el dado pero ahora tiene múltiples lados de valores desconocidos

"""

def sumatorias_n(lista, n):
    if n == 0 or not lista:
        return []
    sol_parcial = [] # la combinacion del momento
    sol_optima = [] # la mejor combinacion que puedo conseguir

    #con indice 0 y suma acumulada de 0
    return _sumatoria_rec(lista, n, 0, 0, sol_parcial, sol_optima)

def _sumatoria_rec(lista, n, indice, sum_ac, sol_parcial, sol_optima):
    if indice == len(lista):
        # llegué al final
        if sum_ac == n:
            #justo si lo que conseguí hasta ahora me dio n, lo guardo y devuelvo una foto de lo que consegui hasta ahora
            sol_optima.append(sol_parcial)
            return sol_optima[:]
        return sol_optima[:]
    else:
        valor_actual = lista[indice]
    
    """
    arbol de decisiones:
    elijo el actual o no lo elijo
    """
    if sum_ac + valor_actual <= n:
        sol_optima = _sumatoria_rec(lista, n, indice+1, sum_ac + valor_actual, sol_parcial + [valor_actual], sol_optima)

    # no lo elijo
    sol_optima = _sumatoria_rec(lista, n, indice+1, sum_ac, sol_parcial, sol_optima)

    return sol_optima




"""
justificacion de la complejidad:
- temporal: O(2^n), 2 deciciones, se abre todo el arbol recursivo de subproblemas y recorro todo + podes (sigue siendo exponencial)
- espacial: cant combinaciones que den exactamente n. en el peor de los casos, O(len(lista))! ?
"""

