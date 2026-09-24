"""
Enunciado ej6:
Dada una matriz de 9x9, implementar un algoritmo por backtracking que llene la matriz con números del 1 al 9, dadas las condiciones del Sudoku (si es posible). Las condiciones son:
(i) Las celdas están dispuestas en 9 subgrupos de 3x3.
(ii) Cada columna y cada fila no puede repetir número.
(iii) Cada subgrupo de 3x3 no puede repetir número.

Las posiciones de la matriz con valor 0 se espera que se completen, las posiciones con valores entr 1 y 9 no deben modificarse.

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe.



"""
"""
planteo:

por cada celda, puedo tener una posible_solucion.
para que sea una posible solucion (por ahora pienso una lista de numeros int.
tengo que considerar leer cada fila y columna, y descartar todos los numeros que YA aparaecen en esa misma. ananananananaannashe)

esta ejercicio es una baaaaandovich. dale.


"""

"""
este costó una baaaaaaaaaaaaaaaaaaaaanda

planteo ej.6:
- itero la matriz buscando una celda con valor 0
- si no hay ceros, es que la matriz ya esta completamente llena y devuelvo true (no pasaba nunca)
- cuando encuentro el cero, hago un for del 1 al 9.
- pregunto si es valido poner ese numero en la fila, columna y submatriz de 3x3 correspondientes.
- si es valido, lo escribo. llamo recursivamente
- si la recursion pincha, borro el numero volviendolo 0 (backtracking) y el for prueba el que le sigue.
- si se me acaban los numeros del for, devuelvo false.
"""
def es_valido_sudoku(matriz, fila, col, num):
    #verifico fila
    for c in range(9):
        if matriz[fila][c] == num:
            return False
            
    # verifico columna
    for f in range(9):
        if matriz[f][col] == num:
            return False
            
    # verifico subgrilla 3x3 (existe un sudoku con más? se considera mas dificil?)
    f_inicio = (fila // 3) * 3
    c_inicio = (col // 3) * 3
    for f in range(f_inicio, f_inicio + 3):
        for c in range(c_inicio, c_inicio + 3):
            if matriz[f][c] == num:
                return False
                
    return True

def _resolver_sudoku_bt(matriz):
    for f in range(9):
        for c in range(9):
            if matriz[f][c] == 0:

                for num in range(1, 10):
                    if es_valido_sudoku(matriz, f, c, num):
                        matriz[f][c] = num #meeeto
                        
                        if _resolver_sudoku_bt(matriz):
                            return True
                            
                        matriz[f][c] = 0 # BacktrackinGoat
                return False # si probe del 1 al 9 y ninguno anduvo, la rama no tiene solucion

    return True # si no encontre 0, ya resolvi el zzzzudoku

def resolver_sudoku(matriz):
    _resolver_sudoku_bt(matriz)

    return matriz

"""
Justificacion de la complejidad ej.6:
- temporal: O(9^C), donde C es la cantidad total de celdas vacías (ceros) en la matriz inicial. Por cada celda vacia, ramificamos hasta 9 caminos posibles. Las comprobaciones de validez toman un máximo de 27 comparaciones O(1).
- espacial: O(C). La pila de llamadas recursivas alcanzará una profundidad igual a la cantidad de celdas vacías C a llenar (a lo sumo 81 en una cuadrícula vacía). Modificamos la matriz in-place, lo que evita almacenar copias redundantes.

NPCOOOOOOOOOOOOOOOOOOOOoooooooooooooooooomplete?
"""