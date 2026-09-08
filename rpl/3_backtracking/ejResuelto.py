"""
Ejercicio resuelto
(★★★★) El problema conocido como Feedback Vertex Set (FVS) indica: Dado un grafo (por simplificación, no dirigido), indicar vértices a eliminar de dicho grafo de tal manera que el grafo quede acíclico.

Implementar un algoritmo que, por backtracking, encuentre el mínimo FVS (es decir, el conjunto de menor cantidad de vértices a remover). Si bien es obvio, el grafo no cuenta con una primitiva tiene_ciclos (e, incluso, si la tuviera, sería poco conveniente usarla, recomendamos pensar por qué).

Solución
El problema en sí a priori no tendría una enorme diferencia con otros ejercicios de Bactracking, salvo por la necesidad de detectar ciclos. El tema aquí es que podemos aplicar una gran poda, que además es extremadamente evidente: si una componente conexa no presenta ciclos, no tiene ningún sentido analizar qué pasaría si sacamos a un vértice de dicha componente. Simplemente es estamos perdiendo el tiempo. Este tipo de podas medianamente evidentes que muestran entender el problema y no simplemente saberse una formula de Backtracking es algo que se espera que se realice. Restaría realmente mucho no hacerlo.

Entonces, a partir de esto se puede plantear de diferentes formas. Lo que vamos a plantear aquí es ir vértice por vértice del grafo, dentro de un conjunto de vértices que (hasta ahora) tenga sentido ir analizando. Entonces, cada vez que sacamos un vértice, calculamos nuevamente cuáles tienen sentido, y los que no (componente conexa sin ciclos) directamente los sacamos.

Se podría hacer también que cada vez que vamos a analizar un vértice, se chequee si la componente a la que perteence es acíclica, y en ese caso saltearlo. Esto sería correcto, se tomaría como correcto totalmente (a fin de cuentas, muestra entender qué mejora se puede hacer en función de entender el problema), pero esto puede mejorarse para evitar hacer una operación lineal por cada vértice en todo momento, e ir ya reduciendo.

Entonces, primero vamos a hacer una breve función que nos determine las componentes conexas de un grafo:
"""
def componentes_conexas(grafo):
    visitados = set()
    componentes = []
    for v in grafo:
        if v not in visitados:
            componente = []
            dfs_comp(grafo, v, visitados, componente)
            componentes.append(componente)
    return componentes

def dfs_comps(grafo, v, visitados, componente):
    componente.append(v)
    visitados.add(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            dfs_comps(grafo, w, visitados, componente)
#Esto es una función lineal sobre el grafo (en vértices y aristas, $\mathcal{O}(V+E)$).

#Ahora hacemos una breve función que nos determine si una componente tiene ciclos. La hacemos con BFS, únicamente porque la anterior la hicimos con DFS (por supuesto, hacerla con DFS estaría bien):

def tiene_ciclo(grafo, componente):
    cola = Cola()
    origen = componente[0]
    cola.encolar(origen)
    visitados = set()
    visitados.add(origen)
    padres = {origen: None}
    while not cola.esta_vacia():
        v = cola.desencolar()
        for w in grafo.adyacentes(v):
            if w in visitados:
                if w is not padre[v]: # si es el padre, no es un ciclo
                    return True
            else:
                padres[w] = v
                visitados.add(w)
                cola.encolar(v)
    return False
#Entonces nuestra idea es: iniciamos obteniendo las componentes conexas del grafo y ya filtrar las que no tienen ciclos. Luego, por cada vértice que aún está en una componente con ciclo, vemos qué pasa si lo sacamos (y recalculamos las componentes –> pueden cambiar porque podríamos estar sacando un vértice que en este punto sea un punto de articulación de lo que resta del grafo). Este último paso sería incluso mejorable si mantuviéramos cuenta de las componentes conexas del grafo, y cuando sacamos un vértice vemos las componentes que hay a partir de este (sin contarlo… digamos, similar a lo hecho en la función componentes_conexas). Esto implicaría un tanto más de programación que incluso no creemos que traiga muchas mejoras (y no esperamos que lo hagan porque justamente, implica mucho más de desarrollo para mantener todo en cuenta). Obviamente, en un TP podría ser conveniente explorar esta posibilidad, y analizar cuánto mejora una determinada poda.

def fvs_rec(grafo_actual, vertices_posibles, sol_parcial, sol_minima):
    if len(vertices_posibles) == 0:
        if len(sol_parcial) < len(sol_minima):
            return sol_parcial[:]
        else:
            return sol_minima

    # La poda obvia de casi todo problema, si ya no somos mejores al óptimo actual, cortamos. 
    if len(sol_parcial) >= len(sol_minima):
        return sol_minima

    # lo saco para no considerarlo
    # es más fácil que ir por índices, siendo que vamos a ir recalculando
    posible = vertices_posibles.pop()

    solucion_minima = fvs_rec(grafo_actual, vertices_posibles, sol_parcial, sol_minima)

    adyacentes = grafo_actual.adyacentes(posible)
    grafo_actual.borrar_vertice(posible)
    nuevos_posibles = potenciales(grafo_actual)
    sol_parcial.append(posible)
    solucion_minima = fvs_rec(grafo_actual, nuevos_posibles, sol_parcial, solucion_minima)
    
    # Backtrack para futuros llamados. No hice una copia porque eso es más costoso que simplemente
    # sacar un vértice y volverlo a poner
    vertices_posibles.append(posible)
    grafo_actual.agregar_vertice(posible)
    for v in adyacentes:
        grafo_actual.agregar_arista(posible, v)

    return solucion_minima
    

def potenciales(grafo):
    nuevos_posibles = []
    for comp in componentes_conexas(grafo):
        if tiene_ciclo(grafo, comp):
            for v in comp:
                nuevos_posibles.append(v)
    return nuevos_posibles

def fvs(grafo):
    # se podria hacer una copia del grafo para no estarlo modificando
    # la solución mínima inicial la consideramos una con todos los vértices, que es una solución trivial
    # (y seguro mejorable)
    return fvs_rec(grafo, potenciales(grafo), [], grafo.vertices())
