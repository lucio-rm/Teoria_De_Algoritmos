"""
Enunciado ej5:

Un camino hamiltoniano, es un camino de un grafo, que visita todos los vértices del grafo una sola vez. Implementar un algoritmo por backtracking que encuentre un camino hamiltoniano de un grafo dado.


"""
"""
planteo:

no hay mucho para pensar, lo dice la consigna. tengo que encontrar un camino que recorra todos los vertices del grafo una sola vez.

tengo que tener 2 visitados?
visitado_general()
visitado_camino()?

y que uno sea el oficial, que sé que esta bien y es el que devuelvo?
y el otro que sea el del momento, el que voy reconstruyendo?

o uso solo ese último y listo?
no terminé de entender cuando y por qué devolvemos una copia del arreglo/lista/solución.

"""


def camino_hamiltoniano(grafo):
    vertices = grafo.obtener_vertices()
    if len(vertices) == 0:
        return []
    solucion_parcial = []
    return _cam_ham_rec(grafo, vertices, 0, solucion_parcial)

def _cam_ham_rec(grafo, vertices, v_indice, solucion_parcial):
    visitados_camino = set()

    v = vertices[v_indice]

    if v not in visitados_camino:
        visitados_camino.add(v) # agrego el vertice al camino hamiltoneano

        for ady in grafo.adyacentes(v):
            if ady not in visitados_camino:
                if _puedo_agregarlo(grafo, ady, visitados_camino):
                    visitados_camino.add(ady)
                    solucion_parcial.append(ady)
                    return _cam_ham_rec(grafo, vertices, v_indice + 1, solucion_parcial)
            else:
                #tengo que volver, si es adyacente y ya fue visitado, hago el BACKtracking, no?
                solucion_parcial.pop()
    return []

def _puedo_agregarlo(grafo, vertice, visitados_camino):
    for ady in grafo.adyacentes(vertice):
        if ady in visitados_camino:
            return False

    return True

"""
Justificacion de la complejidad:
blablabla
temporal : O(2^V), porque por cada vertice del grafo, se abre en la poda recursiva la opción de utilizarlo y no utilizarlo.
(esta bien esa justificacion asi bien de nasheeeeeeeeeeeEE?????????????)
espacial: O(V), porque a lo sumo visitados_camino() va a llenarse con n vertices, que n < v, por lo que O(v) es correcto.

"""