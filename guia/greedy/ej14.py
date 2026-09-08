"""
Enunciado ejercicio 14:
(★★) Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. 
Implementar un algoritmo Greedy que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”). 

Indicar y justificar la complejidad del algoritmo implementado. 
¿El algoritmo implementado da siempre la solución óptima? Justificar

"""

"""
planteo:
maso menos la misma shit, solo que ahora estamos en R².

por cada submarino, voy a tener que recorrer la matriz n.m para actualizar la matriz.
siendo: 
en el rango del faro, 
- un 1 si en esa posicion de la matriz pongo un faro y cubre 1 submarino
- un 2 si en esa pos. el faro cubre 2 submarinos
etc.

entonces por cada submarino tengo que comprobar.


NO es óptimo. peudo encontrqar un caso que en vez de poner 4 faros pone 5.


"""


# devolver una lista de faros. Cada faro debe ser una tupla con su posición en (x,y)
# matriz booleana, indica True en las posiciones con submarinos
def submarinos(matriz):
    return [(0,0)]