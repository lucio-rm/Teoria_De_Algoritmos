"""
Enunciado ej.16:
Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah decidió que en una misma parada de colectivo nunca pararán dos colectivos que usen el mismo color. El problema es que ya saben que eso está sucediendo hoy en día, así que van a repintar todas las líneas de colectivos. 
Por problemas presupuestarios, desean pintar los colectivos con la menor cantidad posible k colores diferentes. Como no quieren parecer un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para saber cuál es ese mínimo valor para cumplir con lo pedido (pintar cada línea con alguno de los k colores, de tal forma que no hayan dos de mismo color coincidiendo en la misma parada). 
Considerando que se tiene la información de todas las paradas de colectivo y qué líneas paran allí, modelar el problema utilizando grafos e implementar un algoritmo que determine el mínimo valor k para resolver el problema. 
Indicar la complejidad del algoritmo implementado.

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
"""
planteo:
similar al problema del coloreo.
tengo que ver
lo que estoy pensando es hacer una funcion que coloree, dependiendo del valor de k que le pase.

tipo:
coloreado = 1 # k = 0 no existe anananashe, solo si no hay grafo (caso megaultrabase)
while coloreado > 0: # coloreado representa el k
    if _coloreo(coloreado, ...):
        # si ya puedo colorear con ese valor de k
        break
    # si no pudo colorear con ese valor, le sumo 1
    coloreado += 1
return coloreado


el _coloreo aplica backtracking.
complejidad temporal: O(k.(2^n)) ¿?

ahora a hacerlo jeje
"""
from grafo import Grafo
def pintar_colectivos(colectivos, paradas):
    if not colectivos or not paradas:
        return 0 # no se puede colorear con ningun valor, valor min = 0 
    # si no hay paradas, significaría que puedo pintar todo con 1 color? a chequear despues con rpl.
    