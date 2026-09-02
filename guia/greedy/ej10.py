"""
Enunciado ejercicio 10:
(★) Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado (ordenado por nombre del pueblo) contiene el número de kilómetro donde está ubicada cada una. Se desea ubicar la menor cantidad de patrullas policiales (en las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a más de 50 km. 
Justificar que la solución es óptima. Indicar y justificar la complejidad del algoritmo implementado. 

Ejemplo:
Ciudad	Bifurcación
Castelli	185
Gral Guido	242
Lezama	    156
Maipú	    270
Sevigne	    194

Si pongo un patrullero en la bifurcación de Lezama, cubro Castelli y Sevigne. Pero no Gral Guido y Maipú. Necesitaría en ese caso, poner otro. Agrego otro patrullero en Gral Guido. Con eso tengo 2 móviles policiales en bifurcaciones que cubren todas los accesos a todas las ciudades con distancia menor a 50km.

En un caso alternativo donde solamente se consideren las bifurcaciones de Castelli, Gral Guido y Sevigne, la única solución óptima sería colocar un móvil policial en Sevigne.

"""


"""
================================================================================
EJERCICIO 10: PATRULLAS POLICIALES (COBERTURA DE INTERVALOS)
================================================================================
planteo (El modelo mental correcto):
1. El arreglo viene ordenado alfabéticamente. La geografía no sabe el abecedario. Lo primero que debo hacer es ordenar las bifurcaciones por su ubicación real (el kilómetro).
2. Para usar la menor cantidad de patrulleros, cada patrullero debe cubrir la MAYOR cantidad de kilómetros posibles hacia la derecha.
3. Si la ciudad 'A' está en el km 10, y debo cubrirla, ¿dónde pongo el patrullero? Si lo pongo en el km 10, cubre del 0 al 60. Pero el tramo 0-9 no me importa. Para exprimir su rango al máximo, lo pongo exactamente 50 km ADELANTE de la ciudad 'A' (en el km 60).
4. Estando en el km 60, cubrirá a la ciudad 'A' hacia atrás (60 - 50 = 10) y cubrirá todo hacia adelante hasta el km 110 (60 + 50 = 110).
5. Descarto (salteo) todas las ciudades que caigan antes del km 110. A la primera que quede afuera, le aplico la misma lógica.

> ELI5 (Ejemplo para un niño de 5 años): 
Imagina que tienes una linterna mágica que ilumina exactamente 5 metros hacia atrás y 5 metros hacia adelante. Si quieres iluminar a un amigo que está parado en la oscuridad, no te paras exactamente sobre él; te paras 5 metros más adelante. Así, la luz lo alcanza a él en el borde trasero, y a la vez iluminas 5 metros más hacia adelante por si hay otro amigo escondido ahí.
"""
from dataclasses import dataclass
@dataclass
class Ciudad:
    nombre: str
    bifurcacion: int

def posicion_patrulleros(ciudades):
    if not ciudades:
        return []

    # 1. Ordenamos espacialmente (por kilómetro)
    ciudades.sort(key=lambda c: c.bifurcacion)
    
    pos_gorra = []
    i = 0
    n = len(ciudades)
    
    while i < n:
        # La ciudad i es la primera que NO está cubierta.
        # Ponemos el patrullero 50km más adelante para exprimir su rango derecho.
        posicion_faro = ciudades[i].bifurcacion + 50
        pos_gorra.append(posicion_faro)
        
        # El patrullero cubre hasta posicion_faro + 50
        cobertura_maxima = posicion_faro + 50
        
        # Avanzamos el índice saltando todas las ciudades que ya quedaron cubiertas
        while i < n and ciudades[i].bifurcacion <= cobertura_maxima:
            i += 1
            
    return pos_gorra

"""
Justificación Ejercicio 10:
- Complejidad Temporal: O(n log n). El ordenamiento inicial toma O(n log n). El ciclo `while` exterior y el interior, combinados, visitan cada ciudad exactamente una vez, lo que toma O(n). O(n log n) + O(n) = O(n log n).
- Complejidad Espacial: O(n) en el peor de los casos, donde se requiere un patrullero por cada ciudad.
- ¿Es óptimo?: Sí. Por argumento de intercambio, si un patrullero se coloca a menos de 50km de la ciudad más a la izquierda sin cubrir, desplazarlo exactamente a 50km hacia la derecha nunca dejará de cubrir a esa ciudad, y solo puede aumentar (o mantener igual) la cantidad de ciudades cubiertas hacia la derecha.
"""