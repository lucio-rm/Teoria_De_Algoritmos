"""
Enunciado ej7:
Implementar un algoritmo de backtracking que, dado una pieza de caballo en un tablero de ajedrez de n x n, determine si existen los movimientos a realizar para que el caballo logre pasar por todos los casilleros del tablero una única vez.
Recordar que el caballo mueve en forma de L (dos casilleros en una dirección, y un casillero en forma perpendicular).

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe.

Métodos del grafo:
Grafo(dirigido = False, vertices_init = []) para crear (hacer 'from grafo import Grafo')
agregar_vertice(self, v)
borrar_vertice(self, v)
agregar_arista(self, v, w, peso = 1)
el resultado será v <--> w
borrar_arista(self, v, w)
estan_unidos(self, v, w)
peso_arista(self, v, w)
obtener_vertices(self)
Devuelve una lista con todos los vértices del grafo
vertice_aleatorio(self)
adyacentes(self, v)
str

"""
"""
planteo:

acá, tengo que hacer una funcion "movimiento_caballo()" para analizar las poibles soluciones de moviemiento en "L"?
teniendo en cuenta que si o si tengo que pasar una vez en el tablero.


"""

"""
planteo ej.7:
- el tablero es una grilla n x n. mi objetivo es encontrar un camino hamiltoniano, es decir, un recorrido que pase por las n*n celdas exactamente una vez
- no haaace falta armar un grafo explícito, las celdas (fila, columna) son mis vértices y los saltos del caballo son mis adyacencias.
- tengo que crearme la funcioncita que me devuelva los saltos en "L" validos, filtrando los que se caigan del tablero
#extra: a todo esto, si aplicamos la regla de L no optimizaría el problema de N-Reinas? a chequear
- no sé en qué celda arranca el caballo, así que tengo que probar arrancar en (0,0), luego en (0,1), etc., hasta que alguno me de el camino completo.
- mi estado recursivo lleva la celda actual, un conjunto de "visitados" para la búsqueda O(1) y una lista de "camino" por si me piden devolverlo (aunque acá con devolver True alcanza).
- mi caso base: ¿tengo n*n elementos en visitados? devuelvo True.
- si la recursión desde un salto devuelve False, deshago el "add" a visitados y pruebo el siguiente salto.
"""

def _movimientos_validos(n, fila, columna):
    saltos = [ #funciona siempre?
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    return [(fila + df, columna + dc) for df, dc in saltos if 0 <= fila + df < n and 0 <= columna + dc < n] #holy shet, busqué como era pa lo de los saltos y lo hizo asi. rompe claaaaramente principio KOP ¿?

def _knight_tour_rec(n, fila, columna, visitados):
    # caso base: pisamos todas las celdas
    if len(visitados) == n * n:
        return True
        
    for nf, nc in _movimientos_validos(n, fila, columna):
        if (nf, nc) not in visitados:
            visitados.add((nf, nc))
            
            if _knight_tour_rec(n, nf, nc, visitados):
                return True
                
            # backtracking
            visitados.remove((nf, nc))
            
    return False

def knight_tour(n):
    # probamos arrancar desde cada celda del tablero
    for i in range(n):
        for j in range(n):
            visitados = {(i, j)}
            if _knight_tour_rec(n, i, j, visitados):
                return True
    return False

"""
Justificacion de la complejidad
- temporal: O(8^{N^2}) donde N es la dimensión del tablero. Desde cada celda de las N^2 posibles, el caballo tiene a lo sumo 8 movimientos posibles. En el peor caso, el árbol de exploración explora todas estas combinaciones.
- espacial: O(N^2). La profundidad máxima del call stack de la recursión es exactamente el número de casilleros del tablero, y el conjunto de "visitados" también almacenará como máximo N^2 elementos.

Investigación: ¿se puede mejorar?
Existen heurísticas como la regla de Warnsdorff (un enfoque greedy que elige siempre la celda siguiente con menos opciones de salto futuras) que resuelve el problema en tiempo lineal para casi todos los casos, reduciendo la poda inmensamente. Sin embargo, para Backtracking puro, el peor caso sigue siendo exponencial.
"""