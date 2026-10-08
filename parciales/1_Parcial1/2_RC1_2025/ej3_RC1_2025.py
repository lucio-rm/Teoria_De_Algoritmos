"""
Enunciado ejercicio 3:
Un PathSelection de un grafo dirigido G y un conjunto de caminos P1, P2, ..., Pc, es un subconjunto de dichos caminos tal que ninguno de ellos compartan ningún nodo entre sí. 
Implementar un algoritmo que obtenga el PathSelection más grande posible de un Grafo y un conjunto de caminos dado. 
Obviamente, implementarlo con un algoritmo por bactracking (si te sale hacerlo polinomial con otra técnica, te aseguramos el 10 en la materia, pero no te prometemos darte nada del millón de dólares).
"""
"""
planteo:
me costó una locura entender la consigna.

tengo un grafo dirigido

tengo un conjunto de caminos.

quiero agarrar la mayor cantidad de caminos siempre y cuando no se superpongan vertices.


es facil

tengo 2 opciones, 2 ramas
o elijo el camino
o no lo elijo

si lo elijo, tengo que fijarme que no rompa compatibilidad con los visitados.

si no lo elijo, me fijo que pasaba si no lo elegía.
"""
# from grafo import Grafo

def biggest_PathSelection(grafo, caminos):
    if not grafo or not caminos:
        return []

    # aviso que no lo voy a hacer polinomial asi la rta la subo yo y me gano todo yo. el 10 me lo gano sin regalar eso. me gano un 20 de última
    
    sol_parcial = [] # el mejor conjunto de caminos que pude conseguir hasta ahora
    sol_optima = [] # lo mejor que pude conseguir con el grafo y los caminos dados.

    visitados = set() #operacion O(1), de nodos visitados.

    indice = 0

    return _pathSelection_bt(caminos, indice, sol_parcial, sol_optima, visitados)


def _pathSelection_bt(caminos, indice, sol_parcial, sol_optima, visitados):
    # poda . si se que los caminos que faltan no van a superar mi solucion optima, no hace falta que vaya por ese lado.
    caminos_restantes = len(caminos) - indice
    if len(sol_parcial) + caminos_restantes <= len(sol_optima):
        return sol_optima #no puedo mejorar lo que mejor que conseguí hasta ahora.
    
    # caso base
    if indice == len(caminos):
        # si ya recorrí todos los caminos, devuelvo lo mejor que pude hacer.
        if len(sol_parcial) > len(sol_optima):
            # si la solucion de esta rama fue mejor a lo que tenía como mejor_global
            return sol_parcial[:] # devuelvo una foto de lo mejor que pude tener.
        return sol_optima

    cam_actual = caminos[indice]

    """
    podas:
    . si sé que tiene como mínimo 1 vertice ya visitado, no lo voy a agarrar.
    """

    if _puedo_usar(cam_actual, visitados):
        # si lo puedo usar, empieza la opcion 1: Elijo el camino actual.
        # agrego todos los vertices del camino a visitados
        _agregar(cam_actual, visitados)
        sol_parcial.append(cam_actual)

        sol_optima = _pathSelection_bt(caminos, indice+1, sol_parcial, sol_optima, visitados)
        
        #deshago, backtrackinGoat
        sol_parcial.pop()
        _sacar(cam_actual, visitados)


    # opcion 2: no elijo el camino actual, y me fijo que hubiera pasado.
    sol_optima = _pathSelection_bt(caminos, indice+1, sol_parcial, sol_optima, visitados)

    return sol_optima

#no use el grafo. ayuda. que carajo hice mal. si ya los caminos me dan todos los nodos, para que carajo lo necesito? #help.

def _puedo_usar(camino, visitados):
    for v in camino:
        if v in visitados:
            return False
    return True

def _agregar(cam_actual, visitados):
    for v in cam_actual:
        visitados.add(v)

def _sacar(cam_actual, visitados):
    for v in cam_actual:
        visitados.remove(v)


"""
Justificacion de la complejidad:

- temporal: O(2^n)

- espacial: O(V), siendo V la cantidad de nodos. en el peor de los casos van a haber V / 2 caminos. tdos caminos de 2 nodos.


"""