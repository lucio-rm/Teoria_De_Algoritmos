"""


Ej.12 (★★★):
Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. Tiene un determinado presupuesto P que no puede sobrepasar, y tiene que una serie de campañas publicitarias para elegir. La campaña i cuesta Ci. También se han realizado diversos estudios que permiten estimar cuánta ganancia nos dará cada campaña, que denominaremos Gi. 
Implementar un algoritmo que reciba esta información y devuelva cuáles campañas debe realizar Carlitos. 

Indicar y justificar la complejidad del algoritmo propuesto. 
¿Da lo mismo si los valores están expresados en pesos argentinos, dólares u otra moneda? Por ejemplo, si una campaña cuesta 100 dólares, para pasar a pesos se debe hacer la conversión de divisa.

"""
"""
planteo:
es lomismo que el knapsack o es toy loco?
presupuesto = W, costo = peso del elemento, ganancia = vlaor del elemento

misma ec. recurrencia y tdo
"""
# cada campaña publicitaria i de la forma (Gi, Ci)
def carlitos(c_publicitaria, P):
    cant = len(c_publicitaria)
    if cant == 0 or P <= 0:
        return []

    M_CAMPANAS = [[0] * (P+1) for _ in range(cant + 1)]

    for i in range(1, cant + 1): #igual al kanpsack, lo sacamos de taquito
        ganancia = c_publicitaria[i-1][0]
        costo = c_publicitaria[i-1][1]
        
        for p_actual in range(1, P + 1):
            if costo <= p_actual:
                # aplico ec. recurrencia, me fijo si lo hago o no
                opcion_hacer = ganancia + M_CAMPANAS[i-1][p_actual - costo]
                opcion_no_hacer = M_CAMPANAS[i-1][p_actual]

                M_CAMPANAS[i][p_actual] = max(opcion_hacer, opcion_no_hacer)
            
            else:
                M_CAMPANAS[i][p_actual] = M_CAMPANAS[i-1][p_actual] # voy al anterior

    # reconstrucción:
    CAMPANAS_ELEGIDAS = []
    i = cant
    w = P

    while i > 0 and w > 0:
        if M_CAMPANAS[i][w] != M_CAMPANAS[i-1][w]:
            campana_real = c_publicitaria[i-1]
            CAMPANAS_ELEGIDAS.append(campana_real)
            w -= campana_real[1] # le restoe l csoto del presupuesto actual
        i -= 1 # en cualquier caso, voy pal anterior
        
    return CAMPANAS_ELEGIDAS[::-1] # orden cronologico


"""
justificacion de la complejidad:

- temporal: O(n*P)
por eso mismo, si cambias a pesos argentinos, que se pueden representar con un P muy grande. termina costando mucho en tiempo y espacio, simpilar a exponencial. por eso siempre vamos a querer reperesentar P como un numero chico y enteero.

- espacial: O(n*P)
matriz M_CAMPANAS como mucho va a ser un tamaño de (n+1) * p+1
"""