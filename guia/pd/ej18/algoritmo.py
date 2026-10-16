# pre condiciones: recibe una lista de listas con valores enteros positivos. (forma de pirámide. fila i contiene (i+1) elementos)
# post condiciones: devuelve el camino mínimo en θ(n²) desde la cima (pos(0,0)) hasta la base.
def camino_minimo_piramide(piramide: list[list[int]]) -> tuple[int, list[list[int]]]:
    if not piramide:
        return 0, []

    n = len(piramide)

    OPT = [[0] * (i + 1) for i in range(n)]

    OPT[0][0] = piramide[0][0]
    if n == 1:
        return OPT[0][0], [[0, 0]]

    OPT[1][0] = piramide[1][0] + OPT[0][0]
    OPT[1][1] = piramide[1][1] + OPT[0][0]


    for i in range(2, n):
        p = 0
        d = 1
        u = i 
        a = u - 1 

        # first-pass
        OPT[i][a] = piramide[i][a] + min(OPT[i-1][a-1], OPT[i-1][a])

        for j in range(a-1, 0, -1):
            OPT[i][j] = piramide[i][j] + min(
                OPT[i - 1][j - 1],
                OPT[i - 1][j],
                OPT[i][j + 1]
            )

        # two-pass
        OPT[i][p] = piramide[i][p] + min(OPT[i - 1][p], OPT[i][d])

        # segundo elemento OPT[i][1] == OPT*[i][1].
        for j in range(2, u):
            OPT[i][j] = min(OPT[i][j], piramide[i][j] + OPT[i][j - 1]) # el OPT[i][j] es su OPT*[i][j].

        # esquina derecha (u = i): baja desde su unico padre superior (i-1, u-1) o viene desde la izquierda
        OPT[i][u] = piramide[i][u] + min(OPT[i - 1][u - 1], OPT[i][u - 1])

    # busco destino optimo en la base de la piramide (ultima fila)
    ult = n - 1
    min_valor = float('inf')
    min_col = 0

    for idx in range(ult + 1):
        if OPT[ult][idx] < min_valor:
            min_valor = OPT[ult][idx]
            min_col = idx

    destino = [min_valor, ult, min_col]
    return min_valor, _reconstruccion(piramide, OPT, destino)


def _reconstruccion(piramide: list[list[int]], OPT: list[list[int]], destino: list) -> list[list[int]]:
    """
    idea: 
    reconstruye el camino optimo desde la base hasta la cima (0, 0) aplicando la ecuacion de recurrencia inversa.
    complejidad temporal: O(n) en el mejor caso, O(n²) en el peor caso (camino en zig-zag)
    """
    if destino[0] == float('inf'):
        return []

    CAMINO = []
    fila = destino[1]
    columna = destino[2]
    CAMINO.append([fila, columna])

    # mientras no se llegue a la cima (0, 0)
    while fila > 0:
        valor_actual = piramide[fila][columna]
        opt_actual = OPT[fila][columna]
        buscado = opt_actual - valor_actual

        # priorizo verificar las transiciones verticales hacia la fila superior (fila - 1)
        # y despues las transiciones horizontales en la misma fila, respetando los bordes del triangulo
        if columna > 0 and OPT[fila-1][columna-1] == buscado:
            #vino de arriba-izquierda
            fila -= 1
            columna -= 1
        elif columna < fila and OPT[fila-1][columna] == buscado:
            # vino de arriba-derecha
            fila -= 1
        elif columna > 0 and OPT[fila][columna-1] == buscado:
            # vino de la izquierda
            columna -= 1
        elif columna < fila and OPT[fila][columna+1] == buscado:
            # vino de la derecha
            columna += 1
        else:
            break

        CAMINO.append([fila, columna])

    return CAMINO[::-1] 
