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
    
    # creo grafo, mas que nada para poder hacer el recorrido entre los colores mejor
    # le pongo un vertices = colectivo, total el problema es por cada parada y no entre paradas
    grafo = Grafo(dirigido=False, vertices_init = colectivos)

    """
    y tengo que ponerle las relaciones entre vertices. va a ser un grafo con multiples subgrafos (que van a ser las paradas)
    entre paradas no van a estar conectadas
    pero por cada parada, las lineas entre ellas si
    conecto cada colectivo con los otros que comparten parada
    """
    for lineas in paradas:
        for i in range(len(lineas)):
            for j in range(i+1, len(lineas)):
                v = lineas[i]
                w = lineas[j]

                if not grafo.estan_unidos(v, w):
                    grafo.agregar_arista(v, w)

    lista_colectivos = grafo.obtener_vertices()

    k = 1 # k = 0 niente

    while k >= 0:
        colores = {} # dicc para guardar los colores puestos
        if _coloreo_bt(grafo, lista_colectivos, 0, k, colores):
            return k
        k += 1
    # si o si va a encontrarse un k, en el peor de los casos k = len(vertices) del grafo. 

def _es_color_valido(grafo, colectivo, color_a_probar, colores):
    """
    este es tipo un filtro o poda
    me fijo si alguno de los colectivos adyacentes ya tiene el color que quiero usar
    aca la complejidad se me va al pingo pero bueno. siempre BTgoat >>>> fuerza bruta
    """
    for ady in grafo.adyacentes(colectivo):
        if ady in colores and colores[ady] == color_a_probar:
            return False
    return True

def _coloreo_bt(grafo, lista_colectivos, indice, k, colores):
    if indice == len(lista_colectivos):
        # si ya le pude poner un color a cada colectivo
        return True

    colectivo_goatee = lista_colectivos[indice]

    for col in range(1, k+1):
        #pruebo con todos los colores del 1 al k
        if _es_color_valido(
            grafo,
            colectivo_goatee,
            col,
            colores
        ):
            colores[colectivo_goatee] = col

            # voy al sgte colectivo
            if _coloreo_bt(grafo, lista_colectivos, indice+1, k, colores):
                return True


            # deshago al carajovich (la parte del backtracking)
            del colores[colectivo_goatee]

    # si probe todos los colores y ninguno sirvió, esa rama no me sirve bruv
    return False


"""
justificacion de la complejidad:

- temporal:


- espacial:


"""