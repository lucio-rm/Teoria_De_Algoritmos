"""
Enunciado ej2:
Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, indique si es posible pintar cada vértice con n colores de tal forma que no hayan dos vértices adyacentes con el mismo color.

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
si n = 2, sería un ejercicio de grafo bipartito.

ahora, la secuencia de acciones sería esta:
voy a un vertice. le pongo 1 color.
voy a otro vertice, le pongo color_2.
voy a otro, y asi. hasta llegar a color_n.


una vez que llegue a color_n, pude llenar a n vertices de distinto color.

al proximo 'v' visitado, me fijo sus adyacentes. el color que le ponga, tiene que ser distinto a todos los colores de los adyacentes. si no puedo ponerle un color, devuelvo False.


"""

from collections import deque
def colorear(grafo, n):
    if n == 0:
        return True # ¿? si no hay colores para colorear, devuelvo True ¿?
    if n == 1 and len(grafo.obtener_vertices()) > 1:
        return False #imposible colorear.

    color = {} # cada vertice va a tener color 0, 1, 2, 3, ..., n.
    visitados = set()
    cola = deque()

    v = grafo.vertice_aleatorio()
    color[v] = 0
    visitados.add(v)
    cola.append(v)
    # BT ES RECURSIVO ¿?????
    while cola: # while not cola.esta_vacia():
        vertice = cola.popleft() #cola.desencolar() (O(1))

        for ady in grafo.obtener_adyacentes(vertice):
            if ady not in visitados:
                visitados.add(ady)
                posible_color = color[vertice] + 1
                if posible_color <= n and puedo_colorear(ady, posible_color, grafo):
                    color[ady] = posible_color
        
"""
un re quilombo wacho

osea tengo que fijarme todos los colores de los adyacentes de un vertice, y ponerle uno distinto a éste.

pero tengo que poder, si en el próximo vertice no puedo colorearlo, volver y ponerle uno distinto a éste (si puedo) , y volver al próximo y poder clorearlo. ono?

mucha shit.

"""