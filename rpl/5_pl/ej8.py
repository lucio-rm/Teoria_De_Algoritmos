"""
Implementar un modelo de programación lineal que permita determinar el clique de tamaño máximo dentro de un grafo. Indicar la cantidad de restricciones generadas en función de la cantidad de vértices y aristas (podés usar notación O para esto, no es importante el número exacto).

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
Recordar que aquí estamos usando PuLP para resolver el problema porque es la forma programática de poder evaluarlo en RPL. A la hora del parcial lo que nos es relevante es el modelo.

"""
"""
planteo:
...un clique es un subconjunto de vertices de un grafo en el que cada par de vértices está directamente conectado por una arista.

(todos son adyacentes entre sí. si dos v NO tienen un aarista que los una, NO pueden etar juntos en el Clique. es igual al Ind.Set pero restringiendo a los NO adyacentes en lugar de los adyacentes)

- Constantes:
Grafo G = (V, E). Para cada vértice i ∈ V, se define su conjunto de no adyacentes como 
ady(i) = {k ∈ V tal que {i} | (i, k) ∉ E}. Constante bigM M = |V| + 1.

- Variables:
Sea X_{i} ∈ {0, 1} una variable binaria entera para cada vértice i ∈ V, que vale 1 si el vértice i pertenece
al Clique, y 0 en caso contrario.

- Inecuaciones:
Si un v i es incluido en el Clique (X_i = 1), ninguno de los vértices que no tienen arista con el puede ser incluido en el cliqui cliqui

∀i ∈ V:    X_{i} + ∑ X_{k} ≤ 1 + M.(1-X_{i})
                k ∈ ¬ady(i)
(exactamente |V| restricciones)

- fun Objetivo:
quieo minimizar la cantidad de vértices adentro del Clique:

max ∑ X_{i}
  i ∈ V


"""

import pulp

def clique_maximo(grafo):
    if not grafo:
        return []
    vertices = grafo.obtener_vertices()
    if not vertices:
        return []
    
    problem = pulp.LpProblem("clique_max", pulp.LpMaximize)

    # variables (1 si esta el v en el clique)
    x = {v: pulp.LpVariable(f"x_{v}", cat="Binary") for v in vertices}

    # inecuaciones
    # si elijo a v(x_v = 1) no puedo elegir a ninguno de los vecinardos
    M = len(vertices) + 1
    for v in vertices:
        adyacentes = set(grafo.adyacentes(v))
        no_ady = [w for w in vertices if w != v and w not in adyacentes]

        if no_ady:
            problem += x[v] + pulp.lpSum(x[w] for w in no_ady) <= 1 + M*(1-x[v])

    #fun obj. quiero maximizar la suma de vertices en el clique
    problem += pulp.lpSum(x[v] for v in vertices)

    # resuelvo
    problem.solver()
    sol = [v for v in vertices if round(pulp.value(x[v])) == 1]
    return sol



