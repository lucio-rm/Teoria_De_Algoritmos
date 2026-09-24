"""
Enunciado 01:

Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a #V, devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.

Métodos del grafo:
Grafo(dirigido = False, vertices_init= []) para crear (hacer 'from grafo import Grafo')
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
parecido al coloreo de grafos, no? o IS¿?

me tengo que curtir con backtracking. es importante. lleva mas codigo que dificultad conceptual.

tengo:
- grafo no dirigido
- numero n < a len(grafo.obtener_vertices())
devuelvo:
- subconjunto de n
    - lista de vertices
    - esa misma lista, entre cada par de vertices no tienen que ser adyacentes entre sí.
    
resolución:
- para conseguir la lista, pienso primero en las hojas del grafo. sé que esas mismas van a ser


Backtracking es siempre recursivo?


rta:
ej1
- No utilizaste backtracking en lo absoluto. Hiciste un enfoque iterativo lineal que solo chequea los vértices una vez de manera greedy (sin deshacer decisiones). En backtracking necesitás usar recursión (o una pila simulando recursión) para explorar el espacio de opciones: ¿qué pasa si pongo este vértice en el conjunto? ¿Y si no lo pongo? Si probando una rama me equivoco, "deshago" (backtrack) y pruebo por el otro camino. Ese for-loop en una sola pasada no sirve para deshacer decisiones. Y recordá que en backtracking, podar cuando sabemos que no hay solución es la clave.
"""
"""
planteo ej.1:
- hago planteamiento
- pienso en cómo se piensa el ejercicio: necesito encontrar un set independiente de tamaño n.
- me pregunto: ¿qué decisiones tengo que tomar? en cada vértice del grafo, tengo dos opciones: lo incluyo en mi subconjunto o no lo incluyo.
- si lo incluyo, tengo que verificar que sea válido (que no sea adyacente a ninguno que ya elegí en mi conjunto parcial).
- mi caso base: si mi subconjunto tiene tamaño n, gané y lo devuelvo. si llegué al final de los vértices y no conseguí tamaño n, devuelvo None o lista vacía.
- si incluyéndolo eventualmente encuentro solución, la devuelvo. si no, lo saco del subconjunto (esto es el backtracking real) y pruebo qué pasa si no lo incluyo en esa rama recursiva.
- una poda excelente que puedo agregar: si los vértices que me quedan por recorrer sumados a los que ya tengo en la solución son menos que 'n', no llego, corto la rama antes.
"""
def es_compatible(grafo, v, solucion_parcial):
    for w in solucion_parcial:
        if grafo.estan_unidos(v, w):
            return False
    return True

def _independent_set_bt(grafo, vertices, v_indice, n, solucion_parcial):
    if len(solucion_parcial) == n:
        return solucion_parcial[:] #es a lo mejor que puedo llegar
        
    # poda: si los que tengo + los que quedan son menos que n, no llego
    if len(solucion_parcial) + (len(vertices) - v_indice) < n:
        return None
        
    v = vertices[v_indice]
    
    # primero: trato de agregar a v
    if es_compatible(grafo, v, solucion_parcial):
        solucion_parcial.append(v)
        sol = _independent_set_bt(grafo, vertices, v_indice + 1, n, solucion_parcial)
        if sol is not None:
            return sol
        solucion_parcial.pop() #aca se hace el Backtracking! deshago
        
    # primero: no agrego a v
    return _independent_set_bt(grafo, vertices, v_indice + 1, n, solucion_parcial)

def no_adyacentes(grafo, n):
    if n > len(grafo.obtener_vertices()):
        return None
    vertices = grafo.obtener_vertices()
    return _independent_set_bt(grafo, vertices, 0, n, [])
"""
Justificacion de la complejidad
- temporal: O(2^V) donde V es la cantidad de vértices. en el peor caso (por ejemplo, el subconjunto de tamaño n no existe o el grafo no tiene aristas), para cada vértice tomamos 2 decisiones en nuestro árbol recursivo: lo agregamos o no lo agregamos. la validación de compatibilidad cuesta a lo sumo O(V), resultando en O(V * 2^V).
- espacial: O(V) por la memoria necesaria para el call stack de la recursión (profundidad máxima V llamadas) y la lista de solucion_parcial que puede almacenar hasta n <= V vértices.
y qué se puede mejorar, y si s posible. (PvsNP): Encontrar un Independent Set (o decidir si existe uno de tamaño K) es un problema NP-Completo conocido. No existe un algoritmo determinístico de tiempo polinomial O(V^k) para resolverlo en el caso general (asumiendo que P != NP). Lo que se puede hacer es mejorar el factor constante mediante podas más inteligentes (como ordenar vértices por grado de menor a mayor, o podar por conectividad), pero la complejidad en el peor caso seguirá siendo exponencial.
"""