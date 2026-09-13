"""
Enunciado ej3:

Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que ubique (si es posible) a n reinas de tal manera que ninguna pueda comerse con ninguna.

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

lo mismo. pero no me sale la lógica del backatrancking.
osea, tenog que ir poniendo uno y uno, hasta llegar a la mejor solución. no?

me estoy comiendo la parte de posible solucion, mejor solucion, o solución óptima , no?.
y me estoy comiendo la parte recursiva, no?

a mejorar, dale dale dale dale dale dale dale dale dale dale.

tengo que poner una reina. tener una func_aux que me diga si en 'x' posicion puedo poner una reina o (me come) la anterior/es y poder ir hasta que si no puedo ponerla, cambiar la pos de la anterior. no?

ej3
- Te rendiste antes de arrancar. "me estoy comiendo la parte recursiva, no?", sí, exacto. La clave de las N reinas es pensar "en esta fila, en qué columna pongo la reina". Para la fila 0, pruebo la columna 0. Paso a la fila 1, pruebo las columnas. Si una reina me come (misma columna o diagonal), la descarto. Si llego a una fila donde no puedo poner ninguna reina, devuelvo atrás (backtrack), saco la reina de la fila anterior, la muevo a la siguiente columna válida, y sigo explorando.


"""
"""
planteo ej.3:
- hago planteamiento
- pienso: un tablero de ajedrez nxn, n reinas. no pueden compartir ni fila, ni columna, ni diagonal.
- me pregunto: si tengo que poner n reinas en un tablero nxn, necesariamente va a ir exactamente una reina por fila (o por columna). 
- entonces mi recursión avanza por filas. en la fila 0, pruebo qué columna usar. en la fila 1, pruebo qué columna usar. ya no me preocupo por las filas.
- chequeo la validez (que no me coman): para la reina que quiero colocar en (fila, columna), me fijo que las que ya coloqué no estén en la misma columna, y que la diferencia absoluta entre las filas no sea igual a la diferencia absoluta entre las columnas (así chequeo de forma matemática ambas diagonales).
- caso base: llegué a la fila n. es decir, coloqué exitosamente mis n reinas.
- voy a guardar la solución como una lista de tuplas de posiciones `(fila, columna)`.
"""
def es_segura(fila, col, reinas):
    for r, c in reinas:
        if c == col: # misma columna
            return False
        if abs(r - fila) == abs(c - col): #misma diagonal
            return False # se matan.
    return True

def _nreinas_bt(n, fila, reinas):
    # Caso base
    if fila == n:
        return reinas[:] # una copia de la mejor rta hasta ahora.
        
    for col in range(n):
        # Decisión: pongo reina en esta columna de la fila actual
        if es_segura(fila, col, reinas):
            reinas.append((fila, col)) # Aplico
            
            sol = _nreinas_bt(n, fila + 1, reinas)
            if sol is not None:
                return sol
                
            reinas.pop() # aplico Backtracking, deshago (voy pa tra)
            
    return None

def nreinas(n):
    if n <= 0: 
        return []
    return _nreinas_bt(n, 0, [])
"""
Justificacion de la complejidad
- temporal: O(n!) (factorial), aunque matemáticamente el límite superior bruto sea O(n^n). Como vamos por fila y descartamos automáticamente colocar dos reinas en la misma fila, la primera fila tiene n opciones, la segunda a lo sumo n-1 (descartando la misma columna), y así sucesivamente. Con la validación de O(n) por cada reina colocada, la complejidad queda O(n * n!).
- espacial: O(n) por la profundidad del call stack (n niveles recursivos, un frame por fila) y el arreglo `reinas` que guarda n posiciones.
y qué se puede mejorar, y si s posible. (PvsNP): El problema clásico de las N-Reinas NO es NP-Completo (la versión de decisión de ubicar o no N reinas es siempre 'Sí' para N>3 y se puede construir en O(n)). Sin embargo, resolverlo explícitamente mediante Backtracking toma tiempo exponencial/factorial. Se puede optimizar muchísimo si en vez de recorrer el arreglo `reinas` en O(n) en `es_segura`, utilizamos tres conjuntos (sets) o boolean arrays para `columnas_usadas`, `diagonales_positivas_usadas` y `diagonales_negativas_usadas` (las cuales se mapean como `fila + col` y `fila - col`). De esta forma el chequeo pasa de O(n) a O(1), bajando radicalmente la constante del algoritmo factorial.
"""