P_VERDE = "V"
P_CELESTE = "C"
NULL_ELEM = "."

def juego_bt(tablero):
    filas = len(tablero)
    cols = len(tablero[0]) if filas > 0 else 0
    
    columnas = []
    
    for j in range(cols):
        piedras = {P_VERDE: [], P_CELESTE: []}
        for i in range(filas):
            color = tablero[i][j]
            if color != NULL_ELEM:
                piedras[color].append(i)
        columnas.append(piedras)
    k = 0
    piedras_fila = [0] * filas
    for i in range(filas):
        for j in range(cols):
            if tablero[i][j] != NULL_ELEM:
                piedras_fila[i] += 1

    for elem in piedras_fila:
        if elem == 0: k += 1
    filas_vacias = k
    lista_colores = ["-"] * cols
    while k <= filas:
        colores = resolver_juego(columnas, piedras_fila, lista_colores, 0, k, filas_vacias)
        if colores is not None:
            return colores
        k += 1
    return lista_colores

def resolver_juego(columnas: list[dict], piedras_fila: list[int], colores, j: int, k: int, vacias: int):
    if j == len(columnas):
        return colores.copy()
    
    verdes = columnas[j][P_VERDE]
    celestes = columnas[j][P_CELESTE]
    
    if not verdes and not celestes:
        colores[j] = "-"
        return resolver_juego(columnas, piedras_fila, colores, j + 1, k, vacias)

    if not verdes or not celestes:
        colores[j] = P_CELESTE if not verdes else P_VERDE
        return resolver_juego(columnas, piedras_fila, colores, j + 1, k, vacias)

    res = intentar(columnas, piedras_fila, colores, j, k, vacias, P_CELESTE, verdes)
    if res is not None:
        return res

    return intentar(columnas, piedras_fila, colores, j, k, vacias, P_VERDE, celestes)


def sacar_piedras(filas, piedras_fila) -> int:
    nuevas = 0
    for i in filas:
        piedras_fila[i] -= 1
        if piedras_fila[i] == 0:
            nuevas += 1
    return nuevas

def devolver_piedras(filas, piedras_fila):
    for i in filas:
        piedras_fila[i] += 1

def intentar(columnas, piedras_fila, colores, j, k, vacias, color, a_sacar):
    nuevas = sacar_piedras(a_sacar, piedras_fila)
    res = None
    if vacias + nuevas <= k:
        colores[j] = color
        res = resolver_juego(columnas, piedras_fila, colores, j + 1, k, vacias + nuevas)
    devolver_piedras(a_sacar, piedras_fila)
    return res

