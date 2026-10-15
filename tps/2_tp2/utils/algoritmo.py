def juego(monedas):
    if len(monedas) == 0:
        return 0, 0

    n = len(monedas)

    OPT = [[0] * n for _ in range(n)]

    for i in range(n):
        OPT[i][i] = monedas[i] 
        if i < n -1:
            OPT[i][i+1] = max(monedas[i], monedas[i+1]) 
    for long in range(3, n+1): 
        for i in range(n - long + 1):
            j = i + long -1
            
            if monedas[i+1] > monedas[j]:
                ganancia_izq = monedas[i] + OPT[i+2][j]
            else:
                ganancia_izq = monedas[i] + OPT[i+1][j-1] 

            if monedas[i] > monedas[j-1]:
                ganancia_der = monedas[j] + OPT[i+1][j-1]
            else:
                ganancia_der = monedas[j] + OPT[i][j-2]

            OPT[i][j] = max(ganancia_izq, ganancia_der)
    guia = _reconstruccion(monedas, OPT)
    return partida(monedas, guia)

def _reconstruccion(monedas, OPT):
    QUE_PASO = []
    i = 0
    j = len(monedas) -1

    turno_sophia = True

    while i <= j: 
        if turno_sophia:
            if i == j:
                QUE_PASO.append(0) 
                break

            if monedas[i+1] > monedas[j]:
                ganancia_izq = monedas[i] + (OPT[i+2][j] if (i+2) <= j else 0) 
            else:
                ganancia_izq = monedas[i] + (OPT[i+1][j-1] if (i+1) <= j-1 else 0) 

            if OPT[i][j] == ganancia_izq:
                QUE_PASO.append(0)
                i += 1
            else:
                QUE_PASO.append(1)
                j -= 1
        else:
            if monedas[i] > monedas[j]:
                i += 1
            else:
                j -= 1

        turno_sophia = not turno_sophia 

    return QUE_PASO 


def partida(monedas: list[int], QUE_PASO: list[int]):
    pts_mateo = 0
    pts_sophia = 0
    i = 0
    j = len(monedas) - 1
    turno_sophia = True
    paso = 0
    while i <= j:
        if turno_sophia:
            if QUE_PASO[paso] == 1:
                moneda = monedas[j]
                j -= 1
            else:
                moneda = monedas[i]
                i += 1
            pts_sophia += moneda
            paso += 1
        else:
            if monedas[i] > monedas[j]:
                moneda = monedas[i]
                i += 1
            else:
                moneda = monedas[j]
                j -= 1
            pts_mateo += moneda
        turno_sophia = not turno_sophia
    return pts_sophia, pts_mateo
