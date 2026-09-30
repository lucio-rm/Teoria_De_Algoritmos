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

    M_CAMPANAS = [[0] * (P+1) for _ ]
    
    return []