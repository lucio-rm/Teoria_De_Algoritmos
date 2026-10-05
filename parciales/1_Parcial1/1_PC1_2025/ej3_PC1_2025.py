"""
Enunciado ejercicio 3:

Recordamos el problema de Interval Scheduling: Dado un conjunto de charlas a dar, con un horario de inicio y fin cada una, determinar la máxima cantidad de charlas a dar de tal forma que no haya solapamiento de horarios entre ninguna de las elegidas( devolviendo las charlas que logran esto). 
Resolver el problema de Interval Scheduling utilizando *backtracking*.
"""

"""
planteo:

okey mas facil

tengo 2 opciones

o doy la charla

o no la doy

si la doy, paso al siguiente nivel recursivo con todas las charas horario_inicio >= horario_fin a esta
"""

def interval_scheduling(charlas):
    if not charlas:
        return []

    # podría hacerlo sin ordenarlas?
    ordenadas = sorted(charlas, key=lambda x: x[1])
    # ordenarla me ayuda a los tiempos y a la solucion de las ramas.
    
    sol_parcial = [] # la cantidad de charlas elegidas en mi rama
    sol_optima = []
    
    return _is_bt(ordenadas, 0, 0, sol_parcial, sol_optima) # le paso el indice y el ultimo fin

def _is_bt(charlas, indice, ultimo_fin, sol_parcial, sol_optima):
    # poda: si lo que tengo + lo que queda no supera mi opt actual, chau chau
    charlas_restantes = len(charlas) - indice
    if len(sol_parcial) + charlas_restantes <= len(sol_optima):
        return sol_optima

    if indice == len(charlas):
        if len(sol_parcial) > len(sol_optima):
            # encontre una solucion mejor, hago una foto 
            return sol_parcial[:]
        return sol_optima

    charla_act = charlas[indice]
    ini_act = charla_act[0]
    fin_act = charla_act[1]

    #rama 1: si la elijo (si es compatible
    if ini_act >= ultimo_fin:
        sol_parcial.append(charla_act)

        sol_optima = _is_bt(charlas, indice+1, fin_act, sol_parcial, sol_optima)

        sol_parcial.pop() #backtracking, restauro estado

    # rama 2: no la elijo
    
    sol_optima = _is_bt(charlas, indice+1, ultimo_fin, sol_parcial, sol_optima)


    return sol_optima

"""
Justificación de la complejidad:

- temporal: O(2^n), ya que recorro las dos subramas y siendo n la cantidad de charlas

- espacial: O(n), ya que en el peor de los casos ocupo como mucho n elementos (todas las charlas fueron compatibles)
"""
