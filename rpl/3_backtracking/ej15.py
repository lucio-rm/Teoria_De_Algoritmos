"""
Enunciado ej.15:
Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. 
Implementar un algoritmo que, por backtracking, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos).

"""
"""
planteo:
W lugares

P[i] contiene la cantidad de personas que integran el grupo i ---> n grupos

esta verga es un subset sum, o knapsack.
P[i] = valor
encontrar la mayor suma de valores que sea <= W 

"""
def max_grupos_bodegon(P, W):
    if W <= 0 or not P:
        return []

    sol_parcial = []
    sol_optima = []

    # le paso tambien el indice y la suma acumulada
    solucion = _bodegon_rec(P, W, 0, 0, sol_parcial, sol_optima)
    return solucion if not None else []

def _bodegon_rec(P, W, indice, sum_ac, sol_parcial, sol_optima):
    if indice == len(P):
        # si ya no tengo grupos por fijarme
        if sum_ac <= W:
            # si justo sigue siendo <= W, entra en la mesa asi comen todos y no se quedan con hambre
            return sol_optima + [sol_parcial]
            #tengo entendido que eso crea una copia de un nuevo arreglo (con el sol_parcial), sin tocar el anterior
        return sol_optima
    else:
        valor_actual = P[indice]

    """
    posibles podas:
    si se que ninguno de los valores que siguen sumados a la sum_ac son <= W, tengo que volver.
    """
    conviene_seguir = False
    for valor in range(indice+1, len(P)):
        if valor + sum_ac <= W:
            conviene_seguir = True
            #eso significa que en algun momento , por este lado, me va a ir bien.
    """
    tengo 2 opciones:
    o la familia me cae bien y come en la mesa
    o no come.
    """
    if valor_actual + sum_ac <= W:
        vos_comes = _bodegon_rec(
            P,
            W,
            indice+1,
            sum_ac + valor_actual,
            sol_parcial + [valor_actual],
            sol_optima
        )
    else: 
        vos_comes = None

    no_comiste = _bodegon_rec(
        P,
        W,
        indice+1,
        sum_ac,
        sol_parcial,
        sol_optima
    )

    if vos_comes is None or not conviene_seguir:
        # si no elijo al grupo, o los que siguen no estan ok
        return no_comiste

    if sum(vos_comes) >= sum(no_comiste):
        return vos_comes
    else:
        return no_comiste


"""
justificacion de la complejidad:
- temporal: mucha mucha mucha exponencial bla blab la

- espacial: no se ya es tarde.


"""