"""
Ej.8 (★★):
Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar “cambio” de una determinada cantidad de plata. Se desea devolver el cambio pedido, usando la mínima cantidad de monedas/billetes. 
Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y devuelva qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizda. 
Indicar y justificar la complejidad del algoritmo implementado.
"""

"""
planteo:
devolver la cantidad de monedas utilizadas == usar reconstruccion. alta pajovich

ec. recurrencia: misma shit que los anteriores 2, va a ser con doble variable. 
C = coins, M = monto
- uso la moneda, o no la uso. OPT me va a devolver la cantidad de monedas utilizadas
OPT(C, M) = min(1 + OPT(C, M-c_i), OPT(C-1, M))

si la uso, tengo la posibilidad de usarla de vuelta.


M - 0 - 1 - 2 - ..., M_total
C
c0- 0 - 1 - 2
c1- 0 - 0 - 1
c2- 0 - 0 - 0 
c3- 0 - 0 -
c4- 0 - 0 -
.
.
.
coins del sistema


asi sigue. en este caso c0 = coin valor 1, c1 = coin valor 2

es la misma mierda que el knapsack
eso pense,  pero influye que ahora no es 0/1. puedo repetir la misma cantidad de monedas, y busco el MINIMO.
"""
def cambio(monedas, monto):
    cant = len(monedas)
    if cant == 0 or monto <= 0:
        return []
    # lleno primero con inf la tabla, porque busco el minimo. si la lleno de 0, siempre va a ganar el 0.
    M_TABLA = [[float('inf')] * (monto + 1) for _ in range(cant+1)]

    for c in range(cant + 1):
        M_TABLA[c][0] = 0
        # caso base, dar vuelto de 0 siempre cuesta 0 monedas pa cualquier W
        
    for c in range(1, cant+1):
        valor = monedas[c-1]
        for d in range(1, monto+1):
            # la ultima moneda y el ultimo valor de monto real, se incluyen.
            if valor <= d:
                #la uso o no la uso
                la_uso = 1 + M_TABLA[c][d-valor] # 1 porque uso 1 cantidad de esa misma moneda
                no_gracias = M_TABLA[c-1][d]

                M_TABLA[c][d] = min(la_uso, no_gracias)
            else:
                # si el valor es mayor a la opcion de monto actual que queda, voy pal anterior
                M_TABLA[c][d] = M_TABLA[c-1][d]
    
    return _reconstruccion(M_TABLA, monedas, monto)

def _reconstruccion(M_TABLA, monedas, monto):
    C_USADAS = []
    cant = len(monedas)
    m_cant = monto

    while cant > 0 and m_cant > 0:
        valor_moneda = monedas[cant-1]

        # se que si uso la moneda c ===> si el monto actual entra, y el valor de la celda coincide con haber sumado 1 a la misma fila (ec. recurrencia)
        if valor_moneda <= m_cant and M_TABLA[cant][m_cant] == 1 + M_TABLA[cant][m_cant - valor_moneda]:

            C_USADAS.append(valor_moneda)
            m_cant -= valor_moneda
        else:
            cant -= 1 #voy a la anterior

    return C_USADAS[::-1] # misma inversion, para que quede cronologicamente el uso de monedas de abajo pa arriba. O(n), siendo n la cantidad de monedas usadas (n <= cant_monedas_totales)

"""
justificación de la complejidad:
blab labla misma cosa
"""