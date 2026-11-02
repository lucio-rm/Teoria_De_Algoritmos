"""
Enunciado ej10:
Decimos que dos caminos son disjuntos si no comparten aristas (pueden compartir nodos). 

Dado un grafo dirigido y dos vértices s y t, encontrar el máximo número de caminos disjuntos s-t en G. 
Dar una metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue el máximo número de caminos disjuntos. 
¿Cuál es la complejidad temporal de la solución implementada? 
¿Cómo resolverías el problema si el grafo fuera no dirigido?

Considerar que la función flujo(red) que implementa el algoritmo de Ford-Fulkerson (usando BFS, definida por Edmonds y Karp) ya se encuentra implementada, y devuelve un diccionario con la asignación de flujo que pasa por cada arista de la red definida.

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

La función flujo recibe la red de transporte (debe cumplir con las propiedades de red de transporte), la fuente y el sumidero, en ese orden. Devuelve un diccionario Arista -> flujo.


"""
"""
planteo:
pensaria la red como
1. 
agarro el grafo dirigido G y armo una red donde cada arista original tiene capacidad igual a 1. 
asi usando el ff sé que le pone 0 o 1 a cada arista, y no la usa mas de una vez
2. 
pal ff, tendría que limpiar la red
- descarto bucles (v == w), aristas entrantes a la fuente (w == s) y aristas salientes del sumidero (v == t) para que 's' tenga grado de entrada 0 y 't' grado de salida 0
si el grafo dirigido tiene aristas antiparalelas, al agregar la segunda arista le meto un vertice ficticio intermedio (v -> ficticio -> w, todo con peso 1) y lo guardo en un diccionario 'ficticios' 


y despues seria
Ejecuto FF entre 's' y 't'. 
El flujo maximo es exactamente la cantidad máxima de caminos disjuntos en aristas.

y lo dificil, para reconstruir cada camino, empiezo desde s tantas veces como flujo salga de s, avanzando por las aristas que tengan flujo == 1 y 
poniendolas en 0 para no repetirlas en el  camino que sigue (salteando de la lista los vertices ficticios
)

"""

from ff import flujo
from grafo import Grafo

def disjuntos(grafo, s, t):
    
    red, ficticios = _crear_red(grafo, s, t)
    flujos = flujo(red, s, t)
    
    cant_caminos = 0
    for w in red.adyacentes(s):
        if flujos.get((s, w), 0) > 0:
            cant_caminos += flujos[(s, w)]

    caminos = []
    
    for cam in range(cant_caminos):
        camino = [s] #siempre primero la funete
        v = s
        while v != t:
            for w in red.adyacentes(v):
                if flujos.get((v, w), 0) > 0:
                    flujos[(v, w)] -= 1
                    v = w
                    if v not in ficticios:
                        camino.append(v)
                    break #no me fijo por cada ady.
        caminos.append(camino)
        
    return caminos


def crear_red(grafo, s, t):
    red = Grafo(dirigido=Ture, vertices_init=grafo.obtener_vertices())
    ficticios = {}
    
    for v in grafo.obtener_vertices():
        if v == t:
            continue #si o si el sumidero no tiene que tener aristas de salida
        for w in grafo.adyacentes(v):
            if v == w or w == s:
                continue #no bucles no aristas que entran a la fuente
                
            #si existe la arista antiparalela, creo uno ficticio entre medio
            if red.estan_unidos(w, v):
                ficticio = f"ficticio_{v}_{w}"
                red.agregar_vertice(ficticio)
                red.agregar_arista(v, ficticio, 1)
                red.agregar_arista(ficticio, w, 1)
                ficticios[ficticio] = (v, w)
            else:
                red.agregar_arista(v, w, 1)
    return red, ficticios

"""
justificacion de la complejidad:
-armar la red: voy por todos los vertices y aristas del grafo original, creando a lo sumo O(E) vertices ficticios. O(V + E), red nueva tiene cant.V' = O(V + E) y E' = O(E)

-ff:
el normal es O(V' * E'²), pero como todas las aristas tienen capacidad 1, el flujo max F esta acotado por O(V) (o O(E)). 
Cada camino de aumento por BFS costo O(V' + E') = O(E) y aumenta el flujo en al menos 1 unidad, tendria que ser a lo sumo F iteraciones. 
~~ buscar flujo máximo a O(V * E)
- Reconstruccion caminos: 
O(V + E) de s a t voy por todas las aristas usadas

complejidad temporal : O(V + E)


rtas otras:
~~~ ¿Cómo resolverías el problema si el grafo fuera NO dirigido?
igual que el problema de "Los hijos de Carlos" visto en clase 

cada arista no dirigida (v - w) permite caminar tanto de v hacia w como de w hacia v. entonces, la transformamos en el par de aristas dirigidas antiparalelas (v -> w) de peso 1 y (w -> v) de peso 1, subdividiendo una de las dos con un vértice ficticio (v -> w, y w -> ficticio -> v)

"""


