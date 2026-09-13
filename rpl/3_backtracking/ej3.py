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



"""

def nreinas(n):
    return [(0, 0)]