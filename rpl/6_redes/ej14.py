"""
Enunciado ej.14:
Se está formando una nueva comisión de actividades culturales de un pueblo. 
Cada habitante es miembro de 0 o más clubes, y de exactamente 1 partido político. 
Cada grupo de interés debe nombrar a un representante ante la nueva comisión de actividades culturales, con las siguientes restricciones: 
- cada partido político no puede tener más de n/2 simpatizantes en la comisión
- cada persona puede representar a solo un club, cada club debe estar representado por un miembro. 

Implementar un algoritmo que dada la información de los habitantes (a qué clubes son miembros, a qué partido pertenecen), nos dé una lista de representantes válidos (Para RPL, lo volvemos diccionario para que el orden no afecte los resultados de las pruebas, y poder consultar fácilmente). 

Indicar y justificar la complejidad del algoritmo implementado.

Considerar que la función flujo(red) que implementa el algoritmo de Ford-Fulkerson (usando BFS, definida por Edmonds y Karp) ya se encuentra implementada, y devuelve un diccionario con la asignación de flujo que pasa por cada arista de la red definida.

- Información de los miembros
Cada miembro tiene los siguientes campos:
miembro: {
    nombre: string con el nombre del miembro
    clubes: lista con los nombres (strings) de los clubes a los que pertenece
    partido_politico: nombre (string) del partido político al que está afiliado
}

Se puede asumir que cada club tiene al menos un miembro asociado.

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

c/u de los 'n' clubes necesita exactamente 1 representante
c/miembro puede representar como mucho a 1 club (que pertenezca)
c/miembro pertenece a exactamente 1 partido politico, iiiimportante ningun partido puede tener más de n/2 representantes en la comision 

pienso Red de Flujo:
fuente 'S' sumidero 'T
serian como 3 capas club -> miem -> part.p (si 2 es bipartito, 3 son tripartito¿?)

(Clubes):
Por c/club, agrego una arista ('S', club) con capacidad 1 (asi fuerzo cada club elija a lo sumo 1 representante)

(Miembros): 
cada miembro  y por cada club al que pertenece, agrego una arista (c, m) con capacidad 1

(Partidos Políticos): 
como cada miembro esta afiliado a un unico partido, agrego una sola arista (m, p) con capacidad 1
aunque al miembro le entren aristas de muchos clubes, como mucho 1 unidad de flujo vaa  salir hacia su partido, garantizando que la persona represente a lo sumo a 1 club

conecto al sumidero cada partido, agrego una arista (p, 'T') con capacidad (n /2), y no dejo que más de n/2 representantes pertenezcan al mismo partido

no me olvido:
meto el FF entre S y T

verifico si el flujo total que sale de S == len(clubes) n. 
si es menor, significa que es imposible cubrir todos los clubes respetando las restricciones==== None
si es igual a n, voy por cada miembro y sus clubes
la arista (club, miembro) que tenga flujo == 1 me va a decir que ese miembro fue asignado como representante de ese club
"""
from ff import flujo
from grafo import Grafo

def representantes(miembros):
    
    if not miembros:
        return {}

    clubes = set()
    partidos = set()

    for miem in miembros:
        partidos.add(miem["partido_politico"])

        for club in miem["clubes"]:
            clubes.add(club)
    
    n_clubes = len(clubes)

    if n_clubes == 0:
        return {}

    max_fans = n_clubes // 2
    if max_fans == 0:
        return None # no se puede resolver asi

    red = Grafo(True)

    fuente = "SS" # SuperFuente
    sumidero = "ST" # SuperSumidero je
    red.agregar_vertice(fuente)
    red.agregar_vertice(sumidero)


    #primero, aristas de la fuente hacia cada club (cap = 1)
    for club in clubes:
        red.agregar_vertice(club)
        red.agregar_arista(fuente, club, 1)

    #2, part. politicos pal sumidero (cap n // 2)
    for par in partidos:
        red.agregar_vertice(par)
        red.agregar_arista(par, sumidero, max_fans)

    # arista club------>miembro cap = 1  &&&& meimbro --__> partido cap = 1 tambien
    for miem in miembros:
        nombre_m = miem["nombre"]
        partido_m = miem["partido_politico"]
        clubes_m = miem["clubes"]

        red.agregar_vertice(nombre_m)
        red.agregar_arista(nombre_m, partido_m, 1)

        for c in clubes_m:
            red.agregar_arista(c, nombre_m, 1)


    # el chad de ff
    flujos = flujo(red, fuente, sumidero)

    # me fijo si cubrio todo los clubes, sino NOne
    flujo_total = sum(flujos.get((fuente, club), 0) for club in clubes)
    if flujo_total < n_clubes:
        return None

    #reconstruccion del dicc
    asignacion = {}
    for miem in miembros:
        nombre_m = miem["nombre"]
        for club in miem["clubes"]:
            if flujos.get((club, nombre_m), 0) == 1:
                asignacion[nombre_m] = club
                break
    
        
    return asignacion


"""
Justificacion de la complejidad

defino:
H: cant de habitantes/miembros.
C: cant de clubes (n).
P: cant de partidos políticos (observando que P <= H, habitante tiene 1 partido)
R: cant total de habitante-club (en el peor caso, R <= H * C)

--creo red G_{f}:
V' = C + H + P + 2(""S y T"") = O(C + H) (lo del P <= H)
E' = C (de S a clubes) + R (de clubes a miembros) + H (de miembros a partidos) + P (de partidos a T) = 
O(C + H + R)
Crear el grafo y ponerle todos los V y E: O(V' + E') = O(C + H + R).

--FF
~~ O(V' * E'²)
O((C + H) * (C + H + R)²)
IMPORTANTEEEEE
como el flujo max esta acotado por la cantidad de clubes F <= C y las capacidades son enteras (importante por el teorema ese integer), cada aumento por BFS cuesta O(V' + E') = O(C + H + R) y se van a hacer como muucho C iteraciones ======~~~~~>>> tiempo O(C * (C + H + R)))

reconstrucción de la solución:
voy por cada miembro y su lista de clubes para verificar que arista tuvo flujo 1
cuesta O(H + R)



Complejidad temporal total: 
O((C + H) * (C + H + R)²)

Complejidad espacial: 
O(C + H + R)
por la red de flujo y el diccionario de flujos


"""



