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