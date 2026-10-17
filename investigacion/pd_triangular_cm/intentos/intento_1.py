
"""
planteo1:
como máximo puedo venir de mis 4 lados.
Ec. Recurrencia:
OPT[i][j] = v_{i}{j} + 
    { OPT[i][j+1] , j < i
min { OPT[i][j-1] , j > 0
    { OPT[i-1][j-1] , j > 0 and i > 0
    { OPT[i-1][j] , i > 0
"""
# resolucion 1: 
"""
Aclaración:
errónea. porque quiero acceder al OPT[i][j+1] (por ejemplo) y no va a estar llenado. si el camino ideal mínimo requería que vaya por ese lado, no lo puede averiguar.
"""
def cam_min(piramide):
    if not piramide:
        return []
    n = len(piramide) - 1

    OPT = [[float('inf')] * (n) for _ in range(n)]
    OPT[0][0] = piramide[0][0] # el inicio

    # lleno la tabla PD
    for i in range(1, n):
        for j in range(0, i+1):
            minimos = [float('inf')] * 4
            # siempre que puedo, accedo:
            if j < i: minimos[0] = OPT[i][j+1] # el de la derecha
            if j > 0: minimos[1] = OPT[i][j-1] # el de la izquierda
            if i > 0 and j > 0: minimos[2] = OPT[i-1][j-1]
            if i > 0: minimos[3] = OPT[i-1][j]

    i = n-1
    dest = (float('inf'), i, 0) 
    """
    como la tabla OPT guarda los optimos de haber llegado a cada pos, recorro la última fila, fjandome a cuál llegué con el menor valor posible
    """
    idx = 0
    while idx <= i:
        if OPT[i][idx] < dest[0]: #el valor
            dest[0] = OPT[i][idx]
            dest[2] = idx # en qué pos de la ult. fila lo encontré.
        idx += 1

    return _reconstruccion_1(piramide, OPT, dest)

def _reconstruccion_1(piramide, OPT, destino):
    if destino[1] == float('inf'):
        return [] # no pude llegar al final
    # sigue reconstruccion. etc etc.
