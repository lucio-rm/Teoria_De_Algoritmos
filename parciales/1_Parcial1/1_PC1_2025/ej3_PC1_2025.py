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
    
    sol_parcial = [] # la cantidad de charlas elegidas en mi rama

    return _is_bt(charlas, 0, sol_parcial) # le paso el indice tambien

def _is_bt(charlas, indice, ultimo_fin, sol_parcial):
    if indice == len(charlas):
        # llegue al final de la lista, devuelvo una foto de lo mejor que conseguí
        return sol_parcial[:]

    charla_actual = charlas[indice]
    ini_act = charla_actual[0]
    fin_act = charla_actual[1]

    # rama 1: si elijo
    # solo evalúo si no se solapa con la anteiror
    if ini_act >= ultimo_fin:
        # lista concatenada, crea una nueva sol_parcial con la charla actual como el último elemento
        te_elijo = _is_bt(charlas, indice+1, fin_act, sol_parcial + [charla_actual])
    else:
        te_elijo = None

    # rama 2, no la elijo
    no_gracias = _is_bt(charlas, indice+1, ultimo_fin, sol_parcial)

    if te_elijo is None:
        return no_gracias

    # y ahora me fijo cuál pudo meter mas charlas adentro
    if len(te_elijo) >= len(no_gracias):
        return te_elijo
    else:
        return no_gracias
    

    

"""
Justificación de la complejidad:

- temporal: O(2^n), ya que recorro las dos subramas y siendo n la cantidad de charlas

- espacial: O(n), ya que en el peor de los casos ocupo como mucho n elementos (todas las charlas fueron compatibles)
"""
