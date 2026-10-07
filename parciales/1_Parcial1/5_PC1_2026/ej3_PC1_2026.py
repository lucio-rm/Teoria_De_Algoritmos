"""
Enunciado ejercicio 3:
Implementar un algoritmo que, por *backtracking*, resuelva el problema del ejercicio 2.
"""

"""
planteo:

elijo o no elijo la charla.
no se en qué se diferencia con el IS normal. mas tiempo? mas ramas?


"""


def scheduling(charlas):
    if not charlas:
        return []

    indice = 0
    ult_fin = 0 #0 A.M.
    sol_parcial = []
    sol_optima = []
    
    ordenadas = sorted(charlas, keylambda=lambda x: x[1], reverse=False)
    # ordeno por fin. 
    return _IS_bt(ordenadas, indice, ult_fin, sol_parcial, sol_optima)

def _IS_bt(charlas, indice, ult_fin, sol_parcial, sol_optima):
    if indice == len(charlas):
        # caso base: esta rama ya recorrió todas las charlas
        if len(sol_parcial) > len(sol_optima):
            return sol_parcial[:] # devuelvo una foto (copia) de lo mejor que construí hasta ahora, en esta rama.
        return sol_optima

    charla_actual = charlas[indice]

    """
    podas:
    si ya no es compatible con la última, chau chau.
    """
    if charla_actual.ini >= ult_fin:
        #la elijo.
        sol_parcial.append(charla_actual)
        sol_optima = _IS_bt(charlas, indice+1, charla_actual.fin, sol_parcial, sol_optima)

        # deshago. backtracking.
        sol_parcial.remove(charla_actual)

    # rama 2: no la elijo.
    sol_optima = _IS_bt(charlas, indice+1, ult_fin, sol_parcial, sol_optima)

    return sol_optima


"""
Justificacion de la complejidad:

- temporal: O(2^n), siendo n la cantidad de charlas.

igual no lo piden. lo pongo por costumbre.

- espacial: O(n). sol_parcial y sol_optima van a tener como maximo n elementos.
"""