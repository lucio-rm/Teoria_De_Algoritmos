"""
Enunciado 01:
Implementar un algoritmo que, dado un grafo no dirigido, nos devuelva un ciclo dentro del mismo, si es que los tiene. Indicar el orden del algoritmo.

Ejemplo
Para el grafo {A: [B], B: [A, C], C: [B]} el resultado sería lista vacía: []
Para el grafo {A: [B, C], B: [A, C], C: [B,A]} el resultado podría ser, entre otros, [A,B,C] ya que existe un camino que recorra A -> B -> C -> A
Métodos del grafo:
- Grafo(es_dirigido = False, vertices_init = []) para crear un grafo no dirigido (hacer 'from grafo import Grafo')
- Grafo(es_dirigido = True, vertices_init = []) para crear un grafo dirigido (hacer 'from grafo import Grafo')
- agregar_vertice(self, v)
- borrar_vertice(self, v)
- agregar_arista(self, v, w, peso = 1)
- borrar_arista(self, v, w)
- estan_unidos(self, v, w)
- peso_arista(self, v, w)
- obtener_vertices(self)
Devuelve una lista con todos los vértices del grafo
- vertice_aleatorio(self)
- adyacentes(self, v)
- str

"""
#from grafo import Grafo

def encontrar_ciclo(g):
    '''
    Devuelve una lista de vertices que conforman el ciclo. En el segundo ejemplo, 
    debería devolver [A, B, C] (o [B, C, A], etc...). 
    Si no hay ciclo, debe devolver None. 
    '''
    visitados = set()
    padres = {}
    
    for v in g.obtener_vertices():
        if v not in visitados:
            padres[v] = None # el origen de esta cmp. conexa no tiene padre
            lista_ciclo = []
            ciclo = _recorrido_dfs(g, visitados, padres, v, lista_ciclo)
            if ciclo is not None:
                return ciclo

    # si llegó hasta aca es que no hay ciclo
    return None


def _recorrido_dfs(grafo, visitados, padres, origen, lista):
    visitados.add(origen)
    
    for ady in grafo.adyacentes(origen):
        if ady not in visitados:
            padres[ady] = origen
            
            ciclo_encontrado = _recorrido_dfs(grafo, visitados, padres, ady, lista)
            if ciclo_encontrado is not None:
                return ciclo_encontrado

        # si ya fue visitado, chequeo que no sea el padre directo
        elif ady != padres[origen]:
            #encuentro el ciclo
            actual = origen
            while actual != ady:
                lista.append(actual)
                actual = padres[actual]
            lista.append(ady)
            # el lista.reverse sería si me piden que quede en el orden del recorrido 
            return lista
    return None

"""
Justificación de la complejidad: siendo V = vertices y E = aristas del grafo.

En el peor de los casos, recorro todos los vértices del grafo.
por cada vertice (en caso de que el grafo tenga más de una componente conexa), 
hago un recorrido dfs.
el recorrido dfs cuesta O(E), porque por cada vertice miro sus adyacentes, que distan de ser los totales del grafo. como es un grafo no dirigido, veo 2 veces cada adyacente. O(2E) = O(E).

Complejidad final: O(V + E)

Complejidad espacial: O(V),
ya que a lo sumo la lista, los dicionarios, el conjunto, van  a tener V elementos.

"""