"""


Ej.6 (★★):
Dado el teclado numérico de un celular, y un número inicial k, encontrar la cantidad de posibles números de longitud n empezando por el botón del número inicial k. Restricción: solamente se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual. 
Implementar el algoritmo por programación dinámica. 
Indicar y justificar la complejidad del algoritmo implementado. Ejemplos:

- Para n=1 empezando por cualquier dígito, solamente hay un número válido (el correspondiente dígito)
- Para N=2, depende de con cuál dígito se comienza:
- Empezando por 0, son válidos 08 (cantidad: 1)
- Empezando por 1, son válidos 12, 14 (cantidad: 2)
- Empezando por 2, son válidos 21, 23, 25 (cantidad: 3)
- Empezando por 3, son válidos 32, 36 (cantidad: 2)
- Empezando por 4, son válidos 41, 45, 47 (cantidad: 3)
- Empezando por 5, son válidos 52, 54, 56, 58 (cantidad: 4)
- Empezando por 6, son válidos 63, 65, 69 (cantidad: 3)
- Empezando por 7, son válidos 74, 78 (cantidad: 2)
- Empezando por 8, son válidos 80, 85, 87, 89 (cantidad: 4)
- Empezando por 9, son válidos 96, 98 (cantidad: 2)

"""
"""
planteo:

primo del problema del laberinto.

se puede repetir el numero

numero inicial k.
cantidad de iteraciones/cadenas longitud n.

1 2 3
4 5 6
7 8 9
  0 

dependiendo de donde comience.

1 -> der, abajo = 2
2 -> izq, der, abajo = 3
3 -> izq, abajo = 2
4 -> arriba, der, abajo = 3
5 -> arriba, der, izq, abajo = 4
6 -> arriba, izq, abajo = 3
7 -> arriba, der = 2
8 -> arriba, der, izq, abajo = 4
9 -> arriba, izq = 2
0 -> arriba = 1

cada uno tiene una optimalidad distinta. 
distinto comportamiento, distintos casos bases.

i = fila ; j = columna
OPT(1) = OPT(i, j+1) + OPT(i+1, j) = OPT(2) + OPT(4) 
OPT(2) = OPT(1) + OPT(3) + OPT(5)
OPT(3) = OPT(2) + OPT(6)
OPT(4) = OPT(1) + OPT(5) + OPT(7)
OPT(5) = OPT(2) + OPT(4) + OPT(6) + OPT(8)
OPT(6) = OPT(3) + OPT(5) + OPT(9)
OPT(7) = OPT(4) + OPT(8)
OPT(8) = OPT(5) + OPT(7) + OPT(9) + OPT(0)
OPT(9) = OPT(6) + OPT(8)
OPT(0) = OPT(8)

(# parecido al de los escalones?)
tengo que armar una matriz con todas las soluciones/posibles soluciones ¿?
n - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10
k - - - - - - - - - - - - - - - - - - - - 
1 - 1 - 2 - 6
2 - 1 - 3 - 8
3 - 1 - 2 - 6
4 - 1 - 3 - 8
5 - 1 - 4 - 13
6 - 1 - 3 - 8
7 - 1 - 2 - 7
8 - 1 - 4 - 9
9 - 1 - 2 - 7
0 - 1 - 1 - 4

OPT(n, k) = SUM(vecino_de_k) [OPT(n-1, vecino_de_k)]
"""

def numeros_posibles(k, n):
    # caso base 
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # meto todos los vecinos a mano (esta bien esto o rompe OPC(open-closed principle)), tipo si quiero poner nuevos digitos inventados con nuevos vecinos, tengo que toquetear esto.
    vecinos = [
        [8], #0
        [2, 4], #1
        [1, 3, 5], #2
        [2, 6], #3
        [1, 5, 7], #4
        [2, 4, 6, 8], #5
        [3, 5, 9], #6
        [4, 8], #7
        [5, 7, 9, 0], #8
        [6, 8] #
    ]
    """
    creo la tabla
    filas: de 0 hasta n (n+1 tengo entendido que nos sirve por los indices (comodidad de no estar haciendo i-1 todo el tiempo))
    columnas: 10 (una por cada digito del 0 al 9). num. cte.
    """
    M_TABLA = [[0] * 10 for _ in range(n + 1)]
    # lo puedo llegar a hacer en O(1), o no? me guardo solo una columna. para la prox. ¿?

    # voy llenando la tabla que puse en el planteo. caso base que todos tienen uno.
    for digito in range(10):
        M_TABLA[1][digito] = 1

    # lleno la tabla desde 2 hasta n
    for longitud in range(2, n + 1):
        for digito in range(10):
            
            # uso la ec. de recurrencia
            suma_vecinos = 0
            for v in vecinos[digito]:
                suma_vecinos += M_TABLA[longitud - 1][v]
                
            M_TABLA[longitud][digito] = suma_vecinos

    return M_TABLA[n][k] # devuelvo lo que me piden


"""
Justificación de la complejidad

- temporal: O(k.n), pseudo-polinomial? por estar pendiente completamente de la longitud en bites de 'n'
siendo k una constante conocida, 10. se puede considerar complejidad O(n) ?
n iteraciones, por 10 digitos, que tienen como maximo 4 vecinos. O(nx4x10) = O(n).
- espacial: O(1) si guardo los resultados que solo me importan (del paso anterior, tipo fibonacci).
(ahora mismo uso O(n), son las 23:51 y me da paja seguir pensando)

"""