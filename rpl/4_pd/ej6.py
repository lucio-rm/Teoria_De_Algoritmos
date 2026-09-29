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
    valores = {}
    valores[1] = 2
    valores[2] = 3
    valores[3] = 2
    valores[4] = 3
    valores[5] = 4
    valores[6] = 3
    valores[7] = 2
    valores[8] = 4
    valores[9] = 2
    valores[0] = 1
    # me da paja hacerlo con grafos. es más optimo hacerlo con grafos? en complejidad espacial? temporal?
    vecinos = {}
    vecinos[1] = [2, 4]
    vecinos[2] = [1, 3, 5]
    vecinos[3] = [2, 6]
    vecinos[4] = [1, 5, 7]
    vecinos[5] = [2, 4, 6, 8]
    vecinos[6] = [3, 5, 9]
    vecinos[7] = [4, 8]
    vecinos[8] = [5, 7, 9, 0]
    vecinos[9] = [6, 8]
    vecinos[0] = [8]

    # ponerlos manualmente me siento totalmente de bot + romperia el OPC (Open-Closed Principle), pero bueno. tocará ser bot por el rpl. que forma NO manualmente sería óptima? de alguna forma se lo tengo que poner. O pongo una constante externa fija? (si o si es fija)
    total = 0
    for i in range(n):
        for ady in vecinos[k]:
            total += valores[ady]
    return total


"""
Justificación de la complejidad

- temporal: O(k.n), pseudo-polinomial? por estar pendiente completamente de la longitud en bites de 'n'
siendo k una constante conocida, 10. se puede considerar complejidad O(n) ?
- espacial: O


"""