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
    charlas = charlas.sorted(lambda x:x[1], False)
    sol_parcial = set() # la cantidad de charlas elegidas en mi rama
    sol_optima = set() #la mejor cantidad de charlas que pude conseguir

    # armo conjuntos asi puedo hacer operaciones de si esta o no esta
    
    solucion = _is_bt(charlas, 0, sol_parcial, sol_optima) # le paso el indice tambien
    return solucion if not None else []

def _is_bt(charlas, indice, sol_parcial, sol_optima):
    if indice == len(charlas):
        # si ya llegué a recorrer todas las charlas
        if len(sol_parcial) > len(sol_optima):
            return list(sol_parcial[:]) # si es mejor que la otra, nashe
        else:
            return list(sol_optima[:])

    charla_actual = charlas[indice]

    """
    podas:
    si agarrando todas las charlas que quedan (aun siendo superpuestas) no voy a llegar a mi mejor solucion
    
    """
    # opcion la elijo, siempre y cuando no superponga a la ultima
    ult_fin = sol_parcial[-1].fin if len(sol_parcial) > 0 else 0 # si no habia charlas, todo ok.

    contador = 0    
    for i in range(indice+1, len(charlas)):
        ini = charlas[i].inicio
        if ini >= charla_actual.fin:
            contador += 1
    
    #en el mejor de los casos, tendría que superar a mi sol_optima con esta rama, sino no.
    if charla_actual.inicio >= ult_fin and (contador + len(sol_parcial)) > len(sol_optima):
        sol_parcial.append(charla_actual)
        te_elijo = _is_bt(charlas, indice+1, sol_parcial, sol_optima)

        # si pasó, tengo que deshacer lo que hice (backtracking) y fijarme en la otra rama
        del sol_parcial[charla_actual]
    else:
        te_elijo = None
    
    no_gracias = _is_bt(charlas, indice+1, sol_parcial, sol_optima)

    
    if te_elijo is None:
        return no_gracias
    elif no_gracias is None:
        return te_elijo

    # y ahora hago las comparaciones, tengo que devolver la mejor, la de mayor cantidad de charlas
    if len(te_elijo) >= len(no_gracias):
        return te_elijo
    else:
        return no_gracias



"""
Justificación de la complejidad:

- temporal: O(2^n), ya que recorro las dos subramas y siendo n la cantidad de charlas

- espacial: O(n), ya que en el peor de los casos ocupo como mucho n elementos (todas las charlas fueron compatibles)
"""
