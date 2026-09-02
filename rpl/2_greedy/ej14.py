"""
Enunciado 14:
Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. Implementar un algoritmo Greedy que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”). Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado da siempre la solución óptima? Justificar

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe.

Métodos del grafo:
Grafo(dirigido = False, vertices_init = []) para crear un grafo no dirigido (hacer 'from grafo import Grafo')
Grafo(dirigido = True, vertices_init = []) para crear un grafo dirigido (hacer 'from grafo import Grafo')
agregar_vertice(self, v)
borrar_vertice(self, v)
agregar_arista(self, v, w, peso = 1)
borrar_arista(self, v, w)
estan_unidos(self, v, w)
peso_arista(self, v, w)
obtener_vertices(self)
Devuelve una lista con todos los vértices del grafo
vertice_aleatorio(self)
adyacentes(self, v)
str

"""

# devolver una lista de faros. Cada faro debe ser una tupla con su posición en (x,y)
# matriz booleana, indica True en las posiciones con submarinos
def submarinos(matriz):
    return [(0,0)]