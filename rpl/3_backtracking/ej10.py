"""
Enunciado ej.10:
Implementar un algoritmo tipo Backtracking que reciba una cantidad de dados n y una suma s. La función debe devolver todas las tiradas posibles de n dados cuya suma es s. Por ejemplo, con n = 2 y s = 7, debe devolver [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]. 
¿De qué complejidad es el algoritmo en tiempo? ¿Y en espacio?

"""
"""
planteo:
tengo ganas de hacerlo por PD, pero bueno


se puede llenar una matriz
- se sabe que cada dado tiene 6 valores {1, 2, 3, 4, 5, 6}

por cada n, se agrega otro for?

tipo
for lado_d1 in range(1, 7):
    for lado_d2 in range(1, 7):
        ...
        // se me va para n!?

sol_parcial va a tener las posibles combinaciones


un indice fijo que va a ser el primer dado. el valor 0 no existe, asi que cuando termino de recorrer todos los valores de ese dado, terminó.

el indice va a ser el valor de todos los lados del dado.


n me dice la cantidad de arreglos [1, ..., 6] que tengo posibles para combinar.

"""

def sumatoria_dados(n, s):
    if n == 0 or s == 0:
        return []
    sol_parcial = set()
    sol_optima = set()
    MATRIZ_DADOS = _crear_dados(n)
    return _sumatoria_rec(n, s, MATRIZ_DADOS, 1, sol_parcial, sol_optima)

def _crear_dados(n):
    # todos = {}
    # for i in range(n):
    #     arreglo = [0] * 6 # 6 lados
    #     indice = 0
    #     for lado in range(1, 7):
    #         arreglo[indice] = lado
    #         indice += 1
    #     todos[i] = arreglo

    M_MATRIZ_COMBINACIONES = [[0] * (n-1) for _ in range(6)]
    # hago n-1 columnas en la matriz, en la cual el primer dado lo voy a usar de indice. no va a estar en la matriz.
    # hago 6 filas, que van a representar el {1, 2, 3, 4, 5, 6}
    lado = 1
    for i in range(6):
        for j in range(n):
            M_MATRIZ_COMBINACIONES[i][j] = lado

        lado += 1
    
    return M_MATRIZ_COMBINACIONES

def _sumatoria_rec(n, s, MATRIZ_DADOS, indice, sol_parcial, sol_optima):
    if len(sol_parcial) > len(sol_optima):
        # cuando la cantidad de combinaciones que tiene sol_parcial es mayor a la optima
        sol_optima = sol_parcial[:]
        # paso una copia porque puede seguir mejorando.

    if indice == 7:
        return sol_optima # sé que no hay nada mejor.

    """
    recorro la matriz. fila y columnas.
    por cada columna pruebo si la suma me da s
    
    tengo que probar con la primer columna.
    (suponer indice = 1)
    indice + M[i][0] = [1, 1] = 1 + 1 = 2
    indice + M[i+1][0] = [1, 2] = 1 + 2 = 3
    ...
    tengo que guardarme las combinaciones para despues probar con la proxima (si es que hay)
    
    comb_1 ([1, 1]) + M[i][1] ([1]) = [1, 1, 1] = 1 + 1 + 1 = 3
    comb_2 ([1, 2]) + M[i+1][1] ([2]) = [1, 2, 2] = 1 + 2 + 2 = 5  
    ...
    
    Backtracking + podas = si sé que la suma ya es mayor, no sigo probando.
    """
    dado = 0
    for fila in range(1, 7):
        valor = MATRIZ_DADOS[fila][dado]
        if indice + valor == s:
            sol_parcial.add([indice, valor])




    # cuando ya probé con todos los dados posibles, voy al siguiente valor de mi dado main
    return _sumatoria_rec(n, s, indice+1, sol_parcial, sol_optima)


