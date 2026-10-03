"""
Enunciado ej.12:
Modificar el algoritmo anterior para que, dada una lista de enteros positivos L y un entero n, devuelva un subconjunto de L que sume exactamente n, o, en caso de no existir, que devuelva el subconjunto de suma máxima sin superar el valor de n.

"""
"""
planteo:
el subconjunto de suma máxima sin superar el valor de n.

en el llamado recursivo tengo que chequear eso.

si no llegó a == n, pero sigue siendo menor, lo guardo.

sol_parcial --> los que tienen == n
sol_sub_parcial --> el subconjunto mas cercano a n
sol_parcial = sol_sub_parcial if sol_parcial [] else: sol_parcial
sol_optima.append(sol_parcial)
return sol_optima[:]


spoiler: salio bien pal culo

tengo que devolver una sola lista.

uso una sola sol_parcial, porque tevuevlo el mejor subconjunto. uno solito.
"""
def max_sumatoria_n(lista, n):
    if n <= 0 or not lista:
        return []
    sol_parcial = []
    # indice = 0, suma actual = 0
    solucion =  _sumatoria_rec(lista, n, 0, 0, sol_parcial)

    return solucion if not None else []


def _sumatoria_rec(lista, n, indice, sum_ac, sol_parcial):
    if indice == len(lista):
        # si llego al final, devuelvo el subconjunto que pude llegar a armar
        return sol_parcial
    #esta bueno, porque ahora tengo 2 formas de armar subconjuntos, o == n, o < n.
    
    # si justo sumé == n, devuelvo eso y al carajo
    if sum_ac == n:
        return sol_parcial

    valor_actual = lista[indice]

    """
    mismo con lo que venimos trabajando, o elijo el valor actual o no
    """

    if sum_ac + valor_actual <= n:
        the_chosen_one = _sumatoria_rec(
            lista, 
            n,
            indice +1,
            sum_ac + valor_actual,
            sol_parcial + [valor_actual]
        )
    else:
        # si cuando lo quería poner, me daba mas que n, MATO AL CHOSEN ONE
        the_chosen_one = None

    # no elijo
    not_chosen = _sumatoria_rec(
        lista,
        n,
        indice+1,
        sum_ac,
        sol_parcial
    )

    if the_chosen_one is None:
        return not_chosen

    # y ahora comparo cuál iso un mejor trabajo y me lleva mas a n
    if sum(the_chosen_one) >= sum(not_chosen):
        return the_chosen_one
    else:
        return not_chosen

"""
complejidad:
misma shet temporal que el anterior

pero creo que el espacial no, a lo sumo va a ser 1 subconjunto, que en el peor de los casos va a ser len(lista) (que len(lista) = 3, n = 3, y lista = [1, 1, 1] algo asi.).


"""