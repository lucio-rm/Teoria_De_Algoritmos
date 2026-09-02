"""
Enunciado 05:
Un autor decidió escribir un libro con varias tramas que se puede leer de forma no lineal. Es decir, por ejemplo, después del capítulo 1 puede leer el 2 o el 73; pero la historia no tiene sentido si se abordan estos últimos antes que el 1.

Siendo un aficionado de la computación, el autor ahora necesita un orden para publicar su obra, y decidió modelar este problema como un grafo dirigido, en dónde los capítulos son los vértices y sus dependencias las aristas. Así existen, por ejemplo, las aristas (v1, v2) y (v1, v73).

Escribir un algoritmo que devuelva un orden en el que se puede leer la historia sin obviar ningún capítulo. Indicar la complejidad del algoritmo.

"""
from collections import deque
# es un ejercicio de orden_topologico
def obtener_orden(grafo):
    grados_entrada = {vertice: 0 for vertice in grafo.obtener_vertices()}
    
    for v in grafo.obtener_vertices():
        for ady in grafo.adyacentes(v):
            grados_entrada[ady] += 1

    #calculé el grado de entrada, y ahora encolo los capitulos queno tienen dependencia
    cola = deque()
    for v, grado in grados_entrada.items():
        if grado == 0:
            cola.append(v)

    orden_historia = []

    while cola:
        v = cola.popleft()
        orden_historia.append(v)

        # cuando "leo" un capitulo v, le resto 1 de dependencia a todos los que le siguen
        for ady in grafo.adyacentes(v):
            grados_entrada[ady] -= 1

            # si quedó sin dependencias previas, ya se puede leer
            if grados_entrada[ady] == 0:
                cola.append(ady)

    # se supone que si la lista final no tiene todos los vertices, hay un ciclo
    return orden_historia

"""
Complejidad del algoritmo: (siendo V = vertices, E = aristas del grafo)

Para calcular los grados de entrada, itero todos los V y recorro sus adyacentes, que distan de ser los totales del grafo, una vez ( por ser un grafo dirigido ), eso cuesta O(V + E)

Recorro el diccionariod e grados que tiene tamaño V, costando O(V)

Cada vertice entra y sale de la cola una sola vez (O(V)) y al salir miramos sus adyacentes, que distan (nuevamente) de ser los totales del grafo. las aristas recorridas vuelven a ser E.
cuesta O(V + E)

Complejidad temporal final: O(V + E) + O(V) + O(V + E) = O(V + E).
Es óptimo porque es imposible ordenar los capitulos sin mirar al menos una vez cada uno y cada una de sus restricciones


Complejidad espacial: O(V), a lo sumo los grados_entrada, la cola y la lista orden_historia guardan V elementos.

"""