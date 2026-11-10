"""
Enunciado 2. 
Shane Hollander e Ilya Rozanov, las dos máximas estrellas y eternos rivales de la liga de hockey sobre hielo, deben organizar durante los playoffs la distribución de equipamiento oficial entre las distintas arenas donde se juegan los partidos. 
Cuentan con un grafo dirigido y pesado donde las aristas representan rutas terrestres y su peso indica la capacidad (en bolsos) del camión asignado a ese tramo. 
En cada vértice tenemos un valor w(v) que implica: 
- si es positivo, se trata de un depósito desde el cual se pueden cargar hasta esa cantidad de bolsos
- si es negativo, se trata de una arena que necesita recibir esa cantidad de bolsos para que se pueda disputar el partido
- si es 0, es simplemente un punto de trasbordo donde se puede cambiar de camión.

Usando *redes de flujo*, implementar un algoritmo que reciba dicho grafo y determine si es posible cumplir con los requisitos de todas las arenas. 
No es necesario indicar cómo serían los traslados. 

Indicar y justificar la complejidad del algoritmo implementado. 
El análisis de la complejidad debe ser completo.

"""

"""
planteo:

tengo:
- blsos
- grafo dirigido pesado
    aristas = rutas
    peso = capacidad que puedo llevar por ese camino con el camión.
- cada vértice tiene un valor
    . positivo : me da 'x' cantidad de bolsos pal camion
    . negativo : tengo que dar 'x' cantidad de bolsos
    . 0: me chupa un huevo. me van a ayudar para el camino.
.



puedo tener posibles aristas antiparalelas?
bucles?
limpiar el grafo.
Los bucles los ignoro, se encarga el ff. pero tengo que borrar las antiparalelas si es que existen.

"""

def cumple_requisitos(grafo):
    vertices = grafo.obtener_vertices
    if not grafo or not vertices:
        return True
    red, ficticios = crear_red(grafo)

    flujo = ford_fulkerson(red)

    """
    para saber que cumple con los requisitos, tuvo que haber "llenado" o "cumplido" con cada arena del grafo, la cual pedía cierta capacidad de bolsos.
    ese valor que pedían, lo puse como peso creado con la arista V--->T
    
    asi que si al sumidero le llegó 'x' cantidad de flujo máximo, tiene que ser la misma cantidad de "requisitos" que pedían. Sino, es que debemos bolsos.
    """

    bolsos_requeridos = 0
    for v in vertices:
        if v < 0:
            valor = v * (-1) #lo paso a positivo
            bolsos_requeridos += valor

    return bolsos_requeridos == flujo["Sumidero"]


def crear_red(grafo):
    S = "Fuente"
    T = "Sumidero"
    ficticios = []
    red = (grafo) # copio el grafo
    vertices = red.obtener_vertices()
    vertices = vertices + S + T
    
    for vertice in vertices:
        if vertice == S or vertice == T:
            continue
        valor = vertice
        if vertice > 0:
            red.agregar_arista(S, vertice, valor)
        elif vertice < 0:
            red.agregar_arista(vertice, T, valor)

    # borro antiparalelas, welcome a los ficticios
    visitados = set()
    for vertice in vertices:
        if vertice == S or vertice == T:
            continue
        for w in red.obtener_adyacentes():
            if vertice == S or vertice == T:
                continue
            if w in visitados:
                peso = red.obtener_peso_arista(w, vertice)
                red.borrar_arista(w, vertice)
                fic = f"ficticio{w}{vertice}" #qué vergovich hace la 'f' aca ¿?

                red.agregar_arista(w, fic, peso)
                red.agregar_arista(fic, vertice, peso)
    
    
    return red, ficticios

# en el parcial voy a asumir que el ff esta implementado. pero quiero implementarlo en la práctica asi practico je.
def ford_fulkerson(red):
    flujo = {}

    return flujo




"""
Justificacion de la complejidad:
V = cantidad de vértices originales en el grafo
E = cantiadd de aristas originales en el grafo
F = cantidad de vertices ficticios agregados
2 = S + T (vertices agregados a la red)
V' = cantidad de vertices de la red = V + 2 + F
E' = cantiad de aristas originales + creadas

- ford_fulkerson : Por demostracion de Edmonds-Karp, el costo del ford_fulkerson para conseguir el flujo máximo es de O(V'.E'²)

- crear_red : 
    . obtener_vertices() = O(V)
    . por cada vértice positivo y negativo, los conecto con S o T correspondientes. costo O(V + 2 (el S y T))
    . por cada vertice de la red, recorro los adyacentes (que distan de ser los totales del grafo) para eliminar las aristas antiparalelas creando un vértice ficticio. costo O(V + E)

- cumple_requisitos: sumado a todo eso, recorro una vez más los vertices del grafo para guardar los valores negativos, para saber si el flujo máximo cumple con éste. costo O(V)


Complejidad temporal final: 
. O(V'.E'²) + O(V) + O(V) + O(V + E)
. = O(V'.E'² + 3V + E)
. como V'.E'² > 3V + E

Complejidad temporal: O(V'.E'²)


Complejidad espacial: O(V' + E')


"""