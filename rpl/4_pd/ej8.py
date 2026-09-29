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
OPT(C, M) = min(OPT(C-1, M-c_i), OPT(C-1, M))

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
"""
def cambio(monedas, monto):
    cant = len(monedas)
    if cant == 0 or monto <= 0:
        return []

    M_TABLA = [[0] * (monto + 1) for _ in range(monedas+1)]

    for c in range(1, monedas+1):
        for d in range(1, monto+1):
            # la ultima moneda y el ultimo valor de monto real, se incluyen.
            valor = monedas[c-1]
            if valor <= d:
                #la uso o no la uso
                la_uso = valor + M_TABLA[c-1][d-valor]
                no_gracias = M_TABLA[c-1][valor]

                M_TABLA[c][d] = max(la_uso, no_gracias)
            else:
                # si el valor es mayor a la opcion de monto actual que queda, voy pal anterior
                M_TABLA[c][d] = M_TABLA[c-1][d]
    
    return _reconstruccion(M_TABLA, monedas, monto)

def _reconstruccion(M_TABLA, monedas, monto):
    C_USADAS = []
    cant = len(monedas)
    m_cant = monto

    while cant > 0 and m_cant > 0:
        # si el valor cambió, es que se usó esa moneda para ese mismo valor:
        if M_TABLA[cant][m_cant] != M_TABLA[cant-1][m_cant]:
            moneda_usada = monedas[cant-1]
            C_USADAS.append(moneda_usada)
            m_cant -= moneda_usada
        else:
            cant -= 1 #voy a la anterior

    #mismo, voy a la esquina inferior derecha
    
    return C_USADAS[::-1] # misma inversion, para que quede cronologicamente el uso de monedas de abajo pa arriba. O(n), siendo n la cantidad de monedas usadas (n <= cant_monedas_totales)

"""
justificación de la complejidad:
blab labla misma cosa
"""