NULL_ELEM = "."

def leer_archivo(ruta: str) -> list[list[str]]:
    tablero = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            tablero.append(list(linea))
    return tablero


def construir_solucion(tablero: list[list[str]], colores_col: list[str]):
    n = len(tablero)
    m = len(tablero[0]) if n > 0 else 0
    removidas = []
    vacias = []
    for i in range(n):
        cant_vacias = 0
        for j in range(m):
            color = tablero[i][j]
            if color == NULL_ELEM:
                cant_vacias += 1
                continue
            if color != colores_col[j]:
                tablero[i][j] = NULL_ELEM
                removidas.append((i, j))
                cant_vacias += 1
        if cant_vacias == m:
            vacias.append(i)
    return tablero, colores_col, removidas, vacias

