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



ej2
- Intentaste usar BFS (con una cola de iteración) como si fuera un recorrido de grafo clásico. Backtracking requiere explorar en profundidad (DFS) y deshacer estado (quitar colores asignados). Con tu cola, avanzás, asignás un color, pero si te trabás y devolvés falso, no tenés forma de volver al vértice anterior recursivamente, sacarle el color que le pusiste y probar con el siguiente `posible_color`. El esquema recursivo es el más natural y adecuado acá.

"""
"""
planteo ej.2:
- hago planteamiento
- me pregunto: ¿de qué va este coloreo? le quiero asignar 1 color de los n posibles a absolutamente todos los vértices.
- decisiones: me paro en un vértice. ¿qué opciones tengo? los n colores.
- antes de pintar, me pregunto: ¿es válido este color? reviso todos los adyacentes a mi vértice actual. si alguno de sus vecinos ya está pintado con ese mismo color, no puedo usarlo y sigo con el próximo.
- caso base: logré procesar a todos los vértices exitosamente, o sea, llegué a que v_indice == len(vertices). devuelvo True.
- si pruebo los n colores para un vértice y ninguno es válido, o ninguno lleva a una solución final, devuelvo False. al retroceder, hago el "del colores[v]" (backtracking) y el vértice anterior prueba su siguiente color.
"""
def es_color_valido(grafo, v, color, colores):
    for ady in grafo.adyacentes(v):
        if ady in colores and colores[ady] == color:
            return False
    return True

def _colorear_bt(grafo, n, vertices, v_indice, colores):
    if v_indice == len(vertices):
        return True
        
    v = vertices[v_indice]
    
    # pruebo colores de 0 a n-1
    for color in range(n):
        if es_color_valido(grafo, v, color, colores):
            colores[v] = color 
            
            if _colorear_bt(grafo, n, vertices, v_indice + 1, colores):
                return True
                
            del colores[v] # hago el backtracking
            
    return False

def colorear(grafo, n):
    if n == 0 and len(grafo.obtener_vertices()) > 0:
        return False
    vertices = grafo.obtener_vertices()
    colores = {}
    return _colorear_bt(grafo, n, vertices, 0, colores)
"""
Justificacion de la complejidad
- temporal: O(n^V) donde n es la cantidad de colores (las opciones posibles) y V la cantidad de vértices. para cada vértice abrimos un factor de ramificación de n en la recursión en el peor caso, generando un árbol de recursión de n a la potencia V. la validación de adyacencias suma un costo O(V), resultando en O(V * n^V).
- espacial: O(V) por la profundidad del call stack recursivo (un nivel por vértice) y el diccionario de colores que como máximo guarda V elementos.
y qué se puede mejorar, y si s posible. 

este tambien es PNP completo
"""