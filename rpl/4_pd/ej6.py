"""


Ej.6 (★★):
    Dado el teclado numérico de un celular, y un número inicial k, encontrar la cantidad de posibles números de longitud n empezando por el botón del número inicial k. Restricción: solamente se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual. Implementar el algoritmo por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado. Ejemplos:
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