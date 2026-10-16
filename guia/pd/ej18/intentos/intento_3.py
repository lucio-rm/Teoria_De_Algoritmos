"""
mejoras:
- codigo limpio, ya oficial
- corrijo indices, ec recurrencia que me comi en el codigo
- optimizacion de memoria
- optimizacion de no uso de ESTRELLA
"""
def camino_minimo_piramide(piramide: list[list[int]]) -> tuple[int, list[list[int]]]:
    """
    encuentra el camino de suma minima desde la cima (0, 0) hasta la base de una piramide
    de n filas con pesos positivos, permitiendo movimientos descendentes a (i+1, j), (i+1, j+1)
    y movimientos laterales dentro de la misma fila a (i, j-1) e (i, j+1).

    Complejidad Temporal: θ(n²) respecto a las filas, equivalente a θ(|V|) lineal en la entrada.
    Complejidad Espacial: θ(n²) in-place sobre matriz escalonada unica.
    """
    if not piramide:
        return 0, []

    n = len(piramide)

    # creo la tabla con solo (i + 1) celdas para la fila i. ( que van a ser los enteros que tiene cada fila )
    # no hace falta matriz ESTRELLA, hago el two-pass in-place sobre OPT
    OPT = [[0] * (i + 1) for i in range(n)]

    # Casos base para las primeras dos filas (n = 1 y n = 2)
    OPT[0][0] = piramide[0][0]
    if n == 1:
        return OPT[0][0], [[0, 0]]

    OPT[1][0] = piramide[1][0] + OPT[0][0]
    OPT[1][1] = piramide[1][1] + OPT[0][0]

    # lleno la tabla por capas desde la fila 2 hasta n - 1
    for i in range(2, n):
        p = 0 # primer elemento de la fila (esquina izquierda)
        d = 1 # segundo elemento de la fila
        u = i # ultimo elemento de la fila (esquina derecha)
        a = u - 1 # anteultimo elemento de la fila

        # first-pass, Derecha a Izquierda (pre-calculo de OPT* guardado in-place en OPT[i])
        # por poda de dominancia geometrica, la esquina derecha (u) no puede mejorar a (a).
        OPT[i][a] = piramide[i][a] + min(OPT[i-1][a-1], OPT[i-1][a])

        for j in range(a-1, 0, -1):
            # wvalua bajar desde arriba-izquierda, bajar desde arriba-derecha o venir de la derecha (OPT*)
            OPT[i][j] = piramide[i][j] + min(
                OPT[i - 1][j - 1],
                OPT[i - 1][j],
                OPT[i][j + 1]
            )

        # two-pass: Izquierda a Derecha (consolidacion de OPT)
        # esquina izquierda (p = 0): baja desde (i-1, 0) o viene desde la derecha (OPT*[i][1])
        OPT[i][p] = piramide[i][p] + min(OPT[i - 1][p], OPT[i][d])

        # segundo elemento (d = 1): por poda de dominancia en esquina izquierda, OPT[i][1] == OPT*[i][1].
        # no hace falta actualizacion porque ya tiene OPT*[i][1].

        # elementos centrales hasta el anteultimo: comparan su OPT* actual contra venir desde la izquierda
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
    CAMINO.append([fila, columna]) # donde llegué si o si.

    # mientras no se llegue a la cima (0, 0)
    while fila > 0: # cuando fila es == 0, ya sé que llegué al único elemento que hay. (el inicio).
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
            # por las dudas (nunca se alcanza con tabla OPT consistente)
            break

        CAMINO.append([fila, columna])

    return CAMINO[::-1] #devuelvo el camino cronológicamente.
