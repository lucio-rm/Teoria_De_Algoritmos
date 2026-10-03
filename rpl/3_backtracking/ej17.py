"""
Enunciado ej.17:
Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. 
Implementar un algoritmo que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”).

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe.

Métodos del grafo:
Grafo(dirigido = False, vertices_init = []) para crear un grafo no dirigido (hacer 'from grafo import Grafo')
Grafo(dirigido = True, vertices_init = []) para crear un grafo dirigido (hacer 'from grafo import Grafo')
agregar_vertice(self, v)
borrar_vertice(self, v)
agregar_arista(self, v, w, peso = 1)
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
parecido al de las patrullas de greedy, o creo que era un ej. de greedy pero no creo que optimo.

ahora tiene que salir optimo si o si.

pruebo:
recorrer toda la matriz.
si encuentro un sumo un 1 a un radio de toda la matriz.
entonces sé que tengo que poner el faro en la posicion donde mayor valor hay.
mmm pero eso no daba optimo mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm la m esta rara no se

este no es como un dominating set
Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: 
o bien (i) pertenece a D;
o bien (ii) es adyacente a un vértice en D.




lo que tengo pensado:
vertices: todas las celdas de la matriz , mas que nada porque puedo poner un faro en cualquier posicion
restriccion: celdas donde hay true hay submarino

arbol subproblemas: o pongo un faro o no lo pongo

"""
# devolver una lista de faros. Cada faro debe ser una tupla con su posición en (x,y)
# matriz booleana, indica True en las posiciones con submarinos
def submarinos(matriz):
    if not matriz:
        return []

    filas = len(matriz)
    columnas = len(matriz[0])

    todas_las_celdas = []

    submarinos = set()

    for fil in range(filas):
        for col in range(columnas):
            todas_las_celdas.append((fil, col))
            if matriz[fil][col]:
                submarinos.add((fil, col))
    # guardo todos los submarino s y celdas
    
    if not submarinos:
        return [] 

    sol_parcial = set()
    
    solucion = _faros_bt(filas, columnas, todas_las_celdas, 0, submarinos, sol_parcial)
    return solucion if not None else []


def _faros_bf(filas, columnas, todas_las_celdas, indice, submarinos, sol_parcial):
    if indice == len(todas_las_celdas):
        # si ya no tengo mas pa recorrer, decidi todo si ponia o no ponia faro, etc etc
        if _quedan_todos_ok(sol_parcial, submarinos, filas, columnas):
            return list(sol_parcial) # lo paso a lista
        return None

    celda_actual = todas_las_celdas[indice]


    # y ahora elijo o no eljiovich
    faro_tonto = _faros_bt(filas, columnas, todas_las_celdas, indice+1, submarinos, sol_parcial)
    #no lo elegi
    
    # si lo elijo
    sol_parcial.add(celda_actual)
    faro_crack = _faros_bt(filas, columnas, todas_las_celdas, indice+1, submarinos, sol_parcial)

    sol_parcial.remove(celda_actual) #limpio, bt bt btb tbtbt

    # me fijo cual es le optimo
    if faro_tonto is None:
        return faro_crack
    if faro_crack is None:
        return faro_tonto

    # y si los dos tienen algo, tengo que devolver la rama que usó menos faros
    if len(faro_tonto) <= len(faro_crack):
        return faro_tonto
    else:
        return faro_crack


# creo una aux que me calcula el radio de 2 celdas alrdededor de un faro
def _celdas_iluminadas_por(faro, filas, columnas):
    fil, col = faro
    iluminadas = set()

    # el radio seria izq-der (-2, 2), arr-abajo(-2,2)
    for ffil in range(-2, 3):
        for ccol in range(-2, 3):
            ffil, ccol = fil + ffil, col + ccol
            if 0 <= ffil < filas and 0 <= ccol < columnas:
                iluminadas.add((ffil, ccol))

    return iluminadas

# func aux que se fija si todos los faros elegidos cubren la totalidad del set
def _quedan_todos_ok(sol_parcial, submarinos, filas, columnas):
    total_iluminados = set()

    for faro in sol_parcial:
        total_iluminados.update(_celdas_iluminadas_por(faro, filas, columnas))

    # y si me queda algun submarino que no esta dentro del conjunto, ñeñeñe
    for sub in submarinos:
        if sub not in total_iluminados:
            return False
    return True
