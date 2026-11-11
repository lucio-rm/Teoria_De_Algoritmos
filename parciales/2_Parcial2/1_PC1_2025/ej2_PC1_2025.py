"""
Enunciado 2. 
Tenemos un grafo no dirigido que representa una grilla de n x n. Definimos que un vértice en la fila i y columna j es el vértice (i, j).
Todos los vértices tienen exactamente 4 adyacentes, salvo los de los bordes, es decir los de la primera y última fila o columna.

Implementar una función que dado el grafo y m puntos iniciales distintos en la grilla (i1, j1), · · · , (im, jm), determine si existen m caminos disjuntos (de vértices) donde cada uno comience en un punto inicial, y termine en m puntos diferentes del borde. 
En los ejemplos del dorso, el de la izquierda tiene solución (la cuál se muestra) mientras que el de la derecha no tiene solución. 
Utilizar redes de flujo para resolver este problema. 

Indicar y justificar la complejidad del algoritmo implementado.

"""

"""
planteo:

maso menos lo mismo, NO PUEDEN
- pasar por una misma arista
- principalmente, pasar por un mismo vertice ---> cortarlo
- fuente: conectada a los vértices originales
- sumidero: conectado con todos los 4n vértices del borde.
- limpiar no dirigido? me importa? si sé que no puede pisar un mismo vértice


va a cumplirse, si al sumidero le llegan M de flujo.
sino, significa que se "trabó" y tuvo que haber pasado por un vertice que no puede (partido, in->out cap.1) entonces no va a llegar el flujo necesario
"""
from grafos import Grafo
from ford_fulkerson import Flujo

def existen_m(grafo, m):
    if not grafo or not m:
        return True
    
    S = "Fuente"
    T = "Sumidero"
    
    red, ficticios = crear_red(grafo, m, S, T)

    flujo_max, red_residual = Flujo(red, S, T)
    # siendo flujo_max el diccionario con todo el flujo que terminó pasando
    
    total = 0
    for v in red.obtener_vertices():
        if red.estan_unidos(v, T):
            total += flujo_max[(v, T)]
    
    return total >= len(m)

def crear_red(grafo, m, fuente, sumidero):
    red = Grafo(dirigido=True)
    #inf = float('inf')

    red.agregar_vertice(fuente)
    red.agregar_vertice(sumidero)

    ficticios = set()
    
    for v in grafo.obtener_vertices():
        #vertice = (fila, columna)
        v_in = f"{v}_in"
        v_out = f"{v}_out"

        red.agregar_vertice(v_in)
        red.agregar_vertice(v_out)

        red.agregar_arista(v_in, v_out, 1)

    for v in grafo.obtener_vertices():
        v_in = f"{v}_in"
        v_out = f"{v}_out"

        adyacentes = grafo.adyacentes(v)

        for w in adyacentes:

            if red.estan_unidos(f"{w}_out", v_in):
                # si de la vuelta ya estaban unidos, para evitar aristas antiparalelas (por el F-F), creo un ficticio intermedio
                ficticio = f"ficticio{v_in}{f"{w}_out"}"
                red.agregar_arista(v_out, ficticio, 1)
                red.agregar_arista(ficticio, f"{w}_in", 1)
                ficticios.add(ficticio)
            else:
                red.agregar_arista(v_out, f"{w}_in", 1)
                
        #si tiene menos de 4 adyacentes, significa que esta en el borde
        if len(adyacentes) < 4:
            red.agregar_arista(v_out, sumidero, 1)

        # si es uno de los m iniciales:
        if v in m:
            red.agregar_arista(fuente, v_in, 1)
            
    
    
    return red, ficticios




"""
Justificacion de la complejidad:

- crear_red:
    . agrego 2 vertices
    . recorro todos los vertices del grafo original y los separo en v_in v_out + agrego su arista
    . creo las aristas para la red + posibles ficticios + aristas con todos los m conectados con la fuente + aristas con los bordes -> Sumidero
Total:
2 = fuente y sumidero
V = vertices del grafo original
V' = todos los vertices partidos en 2 + ficticios + 2= 2V + V/2 + 2
    en el peor de los casos, voy a crear V/2 vértices ficticios

E = aristas del grafo original
E' = aristas originales pasadas a dirigidas + aristas con la fuente + aristas con el sumidero = 3E + V + V/4
    en el peor de los casos, por cada arista no dirigida, la parto en 2 y una de esas 2 la parto en 2 poniendo el ficticio entre medio --> por cada arista voy a tener 3 en total.
    además, en el peor de los casos, la cantidad de vertices iniciales m van a ser el total ed vertices del grafo, por lo que tengo que crear V aristas.
    y siempre voy a conectar todos los vertices del borde con el sumidero ~son 4/V vertices en el borde
.
pasandolo a las variables del problema:
V = nxn = n²
E = 4n² (cada vertice, como mucho va a tener 4 aristas. nunca mas)

V' = 2n² + n²/2 + 2
E' = 12n² + n² + 4n (aca paso a 4n porque un borde tiene n vertices, los 4 bordes son 4n, los que se conectan al sumidero van a ser 4n vertices por lo que son 4n aristas mas)

crear_red() total: O(V' + E') = O(2n² + n²/2 + 2 + 12n² + n² + 4n)
==> O(n² + n² + n² + n² + n) = O(4n² + n) = O(4n²) = O(n²)



Flujo() -> va a ejecutar el Ford_fulkerson, por lo que por demostración de Edmonds-Karp va a ser un O(V'.E'²)

Como sé que son caminos disjuntos y:
- en todos los caminos no va a repetirse ningun vértice (por eso corto el vertice en in_out con cap 1)
- en todos los caminos no va a repetirse ninguna arista (por eso cada arista con cap.1)
    . si reocrrieran 2 caminos la misma arista, si o si van a tener que visitar 2 vértices iguales. (#nota: al principio puse que las aristas tenian cap. inf, pero lo cambie a 1 para no tener quilombos por las duddas. como al primer camino ya voy a tener que cuando llegan al v_in de un vertice que ya ocupe no va a entrar, no pasa nada pero bueno).
Como sé que a lo sumo se van a ejecutar m BFS's para obtener el flujo máximo, y como m en el peor de los casos es = V = n², la complejidad es:
O(n² . (V' + E')) = O(n².(n² + n²)) = O(n².(n²)) = O(n⁴)


Flujo() --> O(n⁴)


y al final recorro todos los vértices para chequear los que estan conectados con el sumidero y fijarme cuánto flujo pasó por ahi y ver si pasó el flujo que tenia que pasar o no. -> O(V') = O(n²)

Complejidad temporal final:
O(n⁴) + O(n²) + O(n²) = O(n⁴ + 2n²) = O(n⁴).




Complejidad espacial final: O(V' + E'), creando la red.
Y vimos que eso tiene un costo de O(n²).
"""