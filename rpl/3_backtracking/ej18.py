"""
Enunciado ej.18:
Implementar un algoritmo que, por backtracking, obtenga la cantidad total de posibles ordenamientos topológicos de un grafo dirigido y acíclico.

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

orden topologico --> ayed --> es algo como las materias de fiuba que tienen correlativas que unos vertices tienen prioridad antes que otros.
problema de grafo dirigido --> grados de entrada  -> flechitas que apuntana  un vertice

me tengoq ue ir fijando los vertices que tengan grado de entrada == 0, por esos empiezo ( si es que no se usaron)

siempre voy a necesitar saber los grados de entrada de los vertices

si elijo un vertice lo uso y como que lo saco del grafo --> le tengoq ue restar el grado de entrada a todos los adyacentes que tenga (le saque la dependencia de hacer analisis matematico 1 antes de AM2, porque ya aproba AM1)

el next step siempre es ir al siguiente vertice que tenga grado de entrada 0.


cuando vuelvo d el arecursion sumo 1 al que le habia restado, como cuando antes hacia tipo sol_parcial.remove(valor_actual)


"""

def contar_ordenamientos(grafo):
    if not grafo:
        return 0

    vertices = grafo.obtener_vertices()

    #lo tuvieron que hebr puesto como primitiva je
    grados_entrada = {v: 0 for v in vertices}
    for v in vertices:
        for ady in grafo.adyacentes(v):
            grados_entrada[ady] += 1

    visitados = set()

    solucion = _contar_rec(grafo, vertices, grados_entrada, visitados)
    return solucion

def _contar_rec(grafo, vertices, grados_entrada, visitados):
    # caso baseovich
    if len(visitados) == len(vertices):
        # si ya puse todosl os vertices en el ordenamiento, encontre 1 camino topologico
        return 1
    total_caminos = 0

    # me fijo por cuales empiezo (gradosE = 0)
    for v in vertices: #esto es una de las cosas que nos habian dicho que no se podia? el for v in grafo? signod e pregunta.
        if v not in visitados and grados_entrada[v] == 0:
            # vos sos crack, te meto == rama de los subproblemas open
            visitados.add(v)
            for ady in grafo.adyacentes(v):
                grados_entrada[ady] -= 1

            total_caminos += _contar_rec(grafo, vertices, grados_entrada, visitados)

            for ady in grafo.adyacentes(v):
                grados_entrada[ady] += 1

            visitados.remove(v) #deshago completamente BT BT BTBTBT baaaacktrackinGoat
    return total_caminos



"""
justificacion de la complejidad:

- temporal: mucho mucho

- espacial: mmmm
"""