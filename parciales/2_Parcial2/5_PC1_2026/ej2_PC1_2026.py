"""
Enunciado 2. 
Un *plan de piso* consiste de n interruptores y n luces con sus ubicaciones. 
Además, un *diseño de iluminación* es una asignación de interruptores y luces (qué luces controla cada interruptor). Un plan de piso es ergonómico si para él existe al menos un diseño de iluminación ergonómico. 
Que un diseño sea ergonómico significa que, para cada interruptor de luz que haya, este maneje una única luz (lámpara, lamparita, etc.), y esa luz *sea además visible desde el lugar donde está el interruptor*. 
En los ejemplos del dorso de este enunciado, el ejemplo de la izquierda es ergonómico, pero el de la derecha no. 

Implementar, utilizando redes de flujo, un algoritmo ergonomicidad(interruptores, luces) que permita determinar si el plan es ergonómico, o no. 
En caso que lo sea, devolver las asignaciones de (interuptor, luz) que correspondan. 
Suponer que existe una función visible(interruptor, luz) que determina si la luz es visible desde el interruptor, y que dicha función ejecuta en tiempo constante. 

Indicar y justificar la complejidad del algoritmo implementado. 
El análisis de la complejidad debe ser completo.

(ver grafico)

"""

"""
planteo:
ergonomico:
maneje una sola luz , y que sea visible desde esa luz between luz-interruptor


pienso en poner ady. a cada coso que sea visible.

bastante sencillo.

Conversion a red de flujo:

Grafo de forma bipartito
Fuente S -> conectada  a cada Luz (capa 1)
cada luz -> conectada a cada interruptor que pueda ver
Interruptor (capa 2) -> conectados c/u al Sumidero T

Todo con cap. 1.

Si al sumidero le llegan 3 de flujo, significa que se usaron los 3 interruptores. y de la unica forma que suceda eso es que le llegue a cada uno 1 de flujo de cada luz. Y que estén conectados significa que son visibles entre sí. --> piso ergonómico.

"""


#tengo que crear el ford-fulkerson?
from grafo import Grafo

def visible(interruptor, luz):
    return True

def ergonomicidad(interruptores, luces):
    if not interruptores or not luces:
        return False
    
    red = crear_red(interruptores, luces)
    
    flujo = ford_fulkerson(red)

    return flujo["Sumidero"] != len(interruptores)

def crear_red(interruptores, luces):
    S = "Fuente"
    T = "Sumidero"
    v_iniciales = [S, T]
    vertices = v_iniciales + interruptores + luces
    grafo = Grafo(dirigido=True, vertices)
    for v in grafo.obtener_vertices():
        if v in interruptores:
            grafo.agregar_arista(S, v, 1)
            for luz in luces:
                if visible(v, luz):
                    grafo.agregar_arista(v, luz, 1)

        if v in luces:
            grafo.agregar_arista(v, T, 1)

    return grafo

def ford_fulkerson(red):
    #asumo red limpia (en este caso funcó, la creé bien)
    flujo = {}
    



"""
Justificacion de la complejidad:

. TEMPORAL:
- visible = O(1)
- crear_red = O(I.L), siendo I la cantidad de interruptores, y L cant. luces.
en el peor de los casos, todos son visibles con todos. entonces, por cada interruptor tengo que recorrer cada luz para agregar esa arista de cap. 1

- ford_fulkerson = O(V.E). la cota genérica demostrada por Edmonds-Karp de O(V.E²) baja, ya que sé que a lo sumo va a ejecutar una cantidad acotada de recorridos, ya que por cada arista va a recorrerse 1 cantidad de flujo.

- ergomicidad = llama a todo.

complejidad temporal final: O(V.E) + O(I.L), siendo V = cant. luces + cant. Interruptores + Sumidero + Fuente.
O( (2 + L + I).E + I.L) = O(E.L.I + L.I) = como E es cant.aristas y algo.L.I > L.I

complejidad: O(E.L.I)


Complejidad espacial: O(L + I), ocupando espacio en la red (el grafo creado).
"""

