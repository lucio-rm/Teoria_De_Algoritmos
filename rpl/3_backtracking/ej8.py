"""
Enunciado ej8:
Implementar un algoritmo de backtracking que, dados dos grafos, determine si existe un Isomorfismo entre ambos.

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

UFFFF , no me acuerdo como verga era este.

era analizar un vertice, y analizar una posible solucion en decir "che, si este es el vertice, se tiene que comportar iiiigual que el posible_vertice del grafo_2, no? tiene que tener la misma cantidad de adyacentes, y esos adyacentes tienen que tener el mismo comportamiento (llamado recursivo ahi), sino cambio a otor, sino vuelvo al backtrcking."
esta bien ese pensamiento?

"""

"""
planteo ej.8:
- busco una biyección entre el grafo 1 y el grafo 2. es decir, mapear cada vértice de g1 con uno de g2, preservando su estructura de aristas.
- primero descarto lo obvio: si tienen distinta cantidad de vértices, devuelvo False.
- voy iterando los vértices de g1 y para cada uno pruebo asignarle un vértice de g2 que aún no haya sido usado
- antes de asignarlo, verifico: para todo vértice ya mapeado de g1, la existencia (o no) de arista con el vértice actual de g1 DEBE ser exactamente igual a la existencia (o no) de arista en g2 entre los vértices mapeados correspondientes
- uso un diccionario "mapping" para acordarme quién es pareja de quién.
- mi caso base: pude mapear todos los vértices de g1
"""
def _es_mapeo_valido(g1, g2, v1, v2, mapping):
    for u1, u2 in mapping.items():
        # si la conexion entre v1 y sus mapeados previos es distinta a la de v2 y sus mapeados previos
        if g1.estan_unidos(v1, u1) != g2.estan_unidos(v2, u2):
            return False
    return True

def _isomorfismo_rec(g1, g2, vertices_g1, indice, mapping, usados_g2):
    # caso base: mapeamos todos
    if indice == len(vertices_g1):
        return True
        
    v1 = vertices_g1[indice]
    
    # pruebo contra todos los vertices de g2
    for v2 in g2.obtener_vertices():
        if v2 not in usados_g2:
            if _es_mapeo_valido(g1, g2, v1, v2, mapping):
                mapping[v1] = v2
                usados_g2.add(v2)
                
                if _isomorfismo_rec(g1, g2, vertices_g1, indice + 1, mapping, usados_g2):
                    return True
                    
                # backtrackinGoat
                del mapping[v1]
                usados_g2.remove(v2)
                
    return False

def hay_isomorfismo(g1, g2):
    v1 = g1.obtener_vertices()
    v2 = g2.obtener_vertices()
    
    if len(v1) != len(v2):
        return False
        
    return _isomorfismo_rec(g1, g2, v1, 0, {}, set())

"""
Justificacion de la complejidad
- temporal: O(V! * V). Donde V es la cantidad de vértices de cada grafo. Generamos todas las permutaciones posibles de mapeo de vértices (esto es el factorial, probamos V opciones para el primero, V-1 para el segundo...). Por cada intento de mapeo, la validación chequea las aristas contra los vértices ya mapeados, costando O(V).
- espacial: O(V). La profundidad máxima del call stack recursivo es V. Las estructuras adicionales ("mapping" y "usados_g2") también albergan a lo sumo V elementos. 

P o NP-Completo?

buscar algoritmo de babai
"""