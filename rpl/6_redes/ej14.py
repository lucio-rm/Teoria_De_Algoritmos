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

from ff import flujo
from grafo import Grafo

def representantes(miembros):
    # devolver un diccionario NombreRepresentante -> NombreClubRepresentado
    # si no se puede resolver dadas las características del problema, devolver None
    return {}
