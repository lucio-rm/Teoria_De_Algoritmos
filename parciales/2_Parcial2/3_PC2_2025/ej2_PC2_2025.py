"""
Enunciado 2. 
Para poder cortar con el juego del rival, Scaloni cuenta con información precisa minuto a minuto. 
En un momento dado, tiene la información perfecta de qué jugador puede darle un pase a cuál otro (independientemente de quién tenga la pelota) o marcar un gol.
Scaloni quiere saber a qué jugador, o jugadores, es indispensable marcar para evitar que nos marquen un gol. Suponiendo que una jugada arranca en el arquero contrario, y que se tiene la información de qué jugador de ese equipo puede pasarle la pelota a cuál/es otro/s (incluyendo al arquero), considerando que esto no es necesariamente recíproco (no todos los jugadores pueden hacer los mismos pases o goles, ¿o vos podés dar los mismos pases que Messi?), y cuáles jugadores podrían marcar un gol en ese momento, indicar cuáles son los mínimos jugadores contrarios a marcar de tal forma que no sea posible que nos marquen un gol (*no podemos marcar
al arquero*). 

Resolver este problema utilizando *redes de flujo*. Pueden suponer que la función flujo(red, s, t) les devuelve tanto la asignación de flujo a cada arista, como también la Red Residual resultante de aplicar el algoritmo de Ford-Fulkerson. 
Indicar y justificar la complejidad del algoritmo planteado. Para todo el problema, considerar que, si bien hay un único arquero, podrían haber n jugadores de campo (simplemente para no quedarse con que son 10 nada más).

"""

"""
planteo:


"""
from grafo import Grafo
def marcar_jugadores(hacen_gol, pases):
    if not hacen_gol or not pases:
        return []
    
    S = "Fuente" # arquero rival
    T = "Sumidero" # arco nuestro
    
    red, ficticios = crear_red(hacen_gol, pases)

    goles = flujo(red, S, T)
    
    marcar = []

    for goleadores in red.adyacentes(T):
        if goleadores in ficticios:
            continue
        if goles[goleadores] == 0:
            marcar.append(goleadores)
    
    return marcar

def crear_red(gol, pases, S, T):
    """
    gol: lista de jugadores que pueden meter gol
    pases: un diccionario de listas del jugador 'i' que puede darle pase a los jugadores 'j' <------------ el arquero rival esta incluido
    """
    ficticios = set()

    
    grafo = Grafo(dirigido=True, list(pases.keys()))
    
    for nombre, jugadores_pases in pases.items():
        for pase in jugadores_pases:
            grafo.agregar_arista(nombre, pase, 1)

    grafo.agregar_vertice(T)
    for jugadores in gol:
        grafo.agregar_arista(jugadores, T, 1)

    #soluciono problema de posibles aristas antiparalelas para la ejecución del ford-fulkerson
    for v in grafo.obener_vertices():
        for w in grafo.adyacentes(v):
            if grafo.estan_unidos(w, v):    
                ficticio = f"ficticio{nombre}{pase}"
                grafo.agregar_arista(nombre, ficticio, 1)
                grafo.agregar_arista(ficticio, pase, 1)
                ficticios.add(ficticio)

    return grafo, ficticios





"""
Justificacion de la complejidad:
V = n jugadores + arco nuestro + ficticios
E = pases que pueden hacer entre jugadores + quienes pueden hacer goles

- crear_red(): O(V + E)
agrego vertices+ficticios-> O(V)
creo aristas ---> O(E)

- ford_fulkerson():
Cota genérica: O(V.E²) (por demostración de Edmonds-Karp)

Pero como sé que cada arista tiene una capacidad de 1, y el BFS cuesta O(V + E), se van a ejecutar 'n' BFS's

--> O(n.(V + E))


Complejidad temporal final:
O(n.(V + E) + V + E) = O(V+E(n + 1))

V = n jugadores + arco nuestro (1) + ficticios (en el peor de los casos, se crean n/2 ficticios) = n + 1 + n/2 = n + n/2

E = pases, en el peor de los casos es todos pueden darle pases a todos + todos pueden hacer gol = n² + n 

~~~ reemplazando

O((n + n/2 + n² + n)(n + 1))
(n + n²).(n+1) = n² + n + n³ + n² = 2n² + n + n³ = O(n³)


Complejidad espacial: O(V + E) = O(n + n/2 + n + n²) = O(n²)
"""