"""
Enunciado ejercicio 16:
(★★★★) Sea una matriz A de tamaño nxn, con todos valores distintos. Un índice (i,j) es un máximo local si A[i,j] es estrictamente mayor que todos su vecinos que existan (arriba, abajo, izquierda, derecha). 
Implementar un algoritmo de División y Conquista que permita encontrar algún máximo local en tiempo O(n). 
Justificar adecuadamente la complejidad del algoritmo.
Prestar mucha atención a la ecuación de recurrencia escrita, ya que esto puede develar un error en el algoritmo planteado.

"""

"""
planteo:
para este ejercicio habia visto  una clase que lo explicaba.
pero no me acuerdo como era la movida para hacerlo D&C

en una matriz A^nxn

1ero: (todo con costo O(n))
    - me fijo la primer fila si hay un maximo local.
    - hago lo mismo con la ultima fila.
    - lo mismo con la primer columna
    - ultima columna
    - fila del medio.
    
entonces, si no hay un maximo local en ninguno de esos lados, voy a tener en la matriz como 4 "cuadrados" 

y hay un teorema (no se si es un teorema o si esta chequeado o me estoy confundiendo con algo), sé que en cualquiera de esos cuadrados, voy a uno de esos, me fijo el numero mayor. y devuelvo ese. sé con certeza que:
    - el numero mayor en cualquiera de esos cuadrados, es un máximo local.
    - recorrer eso es mucho menor a n, por lo que no romperia la complejidad.
    
hacer eso en O(n) ¿?

"""

"""
planteo:
- Buscar en las filas/columnas de los bordes destruye la posibilidad de reducir 
  el problema geométricamente a un solo cuadrante cerrado.
- El algoritmo correcto es la "Búsqueda de la Cruz" (Cross Finding):
  1. Tomas la columna del medio y la fila del medio. (Esto forma una cruz).
  2. Encuentras el máximo global de los elementos que componen esa cruz. (Cuesta O(n)).
  3. Chequeas los 4 vecinos de ese máximo.
  4. Si ninguno es mayor, ¡bingo! Es un máximo local de la matriz.
  5. Si un vecino es mayor (por ejemplo, el de arriba a la derecha), ENTONCES 
     existe una garantía matemática de que el Cuadrante Superior Derecho contiene 
     al menos un máximo local.
  6. Llamas a recursión reduciendo la búsqueda SOLO a ese cuadrante (n/2 x n/2).
"""

def _maximo_local_matriz_rec(A, fil_ini, fil_fin, col_ini, col_fin):
    # Caso base: si la submatriz se reduce a una sola celda
    if fil_ini == fil_fin and col_ini == col_fin:
        return fil_ini, col_ini, A[fil_ini][col_ini]

    mid_f = (fil_ini + fil_fin) // 2
    mid_c = (col_ini + col_fin) // 2
    
    max_val = -float('inf')
    max_f, max_c = -1, -1
    
    # Encontramos el máximo en la "Cruz" (O(n) iteraciones)
    for c in range(col_ini, col_fin + 1):
        if A[mid_f][c] > max_val:
            max_val = A[mid_f][c]
            max_f, max_c = mid_f, c
            
    for f in range(fil_ini, fil_fin + 1):
        if A[f][mid_c] > max_val:
            max_val = A[f][mid_c]
            max_f, max_c = f, mid_c
            
    # Verificar vecinos del máximo de la cruz cuidando los bordes del cuadrante actual
    vecinos = []
    if max_f > fil_ini: vecinos.append((A[max_f-1][max_c], max_f-1, max_c)) # Arriba
    if max_f < fil_fin: vecinos.append((A[max_f+1][max_c], max_f+1, max_c)) # Abajo
    if max_c > col_ini: vecinos.append((A[max_f][max_c-1], max_f, max_c-1)) # Izquierda
    if max_c < col_fin: vecinos.append((A[max_f][max_c+1], max_f, max_c+1)) # Derecha
    
    vecino_mayor = max(vecinos, key=lambda x: x[0]) if vecinos else (float('-inf'), -1, -1)
    
    # Si el máximo de la cruz es mayor o igual a sus vecinos, encontramos un máximo local
    if max_val >= vecino_mayor[0]:
        return max_f, max_c, max_val
        
    # Si no, el vecino mayor dicta a qué cuadrante nos movemos
    vf, vc = vecino_mayor[1], vecino_mayor[2]
    
    if vf < mid_f and vc < mid_c: # Superior Izquierdo
        return _maximo_local_matriz_rec(A, fil_ini, mid_f - 1, col_ini, mid_c - 1)
    elif vf < mid_f and vc > mid_c: # Superior Derecho
        return _maximo_local_matriz_rec(A, fil_ini, mid_f - 1, mid_c + 1, col_fin)
    elif vf > mid_f and vc < mid_c: # Inferior Izquierdo
        return _maximo_local_matriz_rec(A, mid_f + 1, fil_fin, col_ini, mid_c - 1)
    else: # Inferior Derecho
        return _maximo_local_matriz_rec(A, mid_f + 1, fil_fin, mid_c + 1, col_fin)

def maximo_local_matriz(A):
    if not A or not A[0]:
        return None
    return _maximo_local_matriz_rec(A, 0, len(A)-1, 0, len(A[0])-1)


"""
Justificacion de complejidad:
- Ecuación de recurrencia: T(n) = T(n/2) + O(n).
- A = 1 (Llamamos a D&C sobre un único cuadrante de la matriz).
- B = 2 (El cuadrante tiene tamaño n/2 x n/2).
- f(n) = O(n) porque recorrer la fila central y la columna central para 
  encontrar el máximo de la cruz requiere evaluar '2n' elementos (lineal respecto a n).
- Aplicando el Teorema Maestro: log_2(1) = 0. C = 1.
- Como C > log_B(A) (1 > 0), el costo de f(n) domina.
- La complejidad final es estrictamente O(n).
"""