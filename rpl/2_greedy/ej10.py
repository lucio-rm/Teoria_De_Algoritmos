"""
Enunciado 10:
Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado (ordenado por nombre del pueblo) contiene el número de kilómetro donde está ubicada cada una. Se desea ubicar la menor cantidad de policiales (en las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a más de 50 km.
Justificar que la solución es óptima. Indicar y justificar la complejidad del algoritmo implementado.
Ejemplo:

| Ciudad      | Bifurcación |
|-------------|-------------|
| Castelli    | 185         |
| Gral Guido  | 242         |
| Lezama      | 156         |
| Maipú       | 270         |
| Sevigne     | 194         |

Si pongo un patrullero en la bifurcación de Lezama, cubro Castelli y Sevigne. Pero no Gral Guido y Maipú. Necesitaría en ese caso, poner otro. Agrego otro patrullero en Gral Guido. Con eso tengo 2 móviles policiales en bifurcaciones que cubren todas los accesos a todas las ciudades con distancia menor a 50km.
En un caso alternativo donde solamente se consideren las bifurcaciones de Castelli, Gral Guido y Sevigne, la única solución óptima sería colocar un móvil policial en Sevigne.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""

"""
planteo:
1. El arreglo viene ordenado alfabéticamente. La geografía no sabe el abecedario. Lo primero que debo hacer es ordenar las bifurcaciones por su ubicación real (el kilómetro).
2. Para usar la menor cantidad de patrulleros, cada patrullero debe cubrir la MAYOR cantidad de kilómetros posibles hacia la derecha.
3. Si la ciudad 'A' está en el km 10, y debo cubrirla, ¿dónde pongo el patrullero? Si lo pongo en el km 10, cubre del 0 al 60. Pero el tramo 0-9 no me importa. Para exprimir su rango al máximo, lo pongo exactamente 50 km ADELANTE de la ciudad 'A' (en el km 60).
4. Estando en el km 60, cubrirá a la ciudad 'A' hacia atrás (60 - 50 = 10) y cubrirá todo hacia adelante hasta el km 110 (60 + 50 = 110).
5. Descarto (salteo) todas las ciudades que caigan antes del km 110. A la primera que quede afuera, le aplico la misma lógica.

"""
def bifurcaciones_con_patrulla(ciudades):
    if not ciudades:
        return []

    # 1. ordeno espacialmente por el kilómetro de la bifurcación (posición 1 de la tupla)
    ciudades_ordenadas = sorted(ciudades, key=lambda columna: columna[1])
    
    patrullas_elegidas = []
    fila = 0
    cantidad_ciudades = len(ciudades_ordenadas)
    
    while fila < cantidad_ciudades:
        # 'fila' representa la primera ciudad a la izquierda que NO está cubierta
        primera_desprotegida = ciudades_ordenadas[fila]
        
        # busco la ciudad más lejana a la derecha que todavía pueda cubrir a 'primera_desprotegida'
        # Su distancia no puede superar en 50 km a la primera desprotegida
        posicion_limite_faro = primera_desprotegida[1] + 50
        
        indice_faro = fila
        while indice_faro + 1 < cantidad_ciudades and ciudades_ordenadas[indice_faro + 1][1] <= posicion_limite_faro:
            indice_faro += 1
            
        # La ciudad elegida para el patrullero es la que encontramos en 'indice_faro'
        ciudad_faro = ciudades_ordenadas[indice_faro]
        patrullas_elegidas.append(ciudad_faro)
        
        # Esa patrulla cubre hasta su kilómetro + 50 km hacia la derecha
        cobertura_maxima = ciudad_faro[1] + 50
        
        # Avanzamos 'fila' saltando todas las ciudades que ya quedaron cubiertas por este faro
        while fila < cantidad_ciudades and ciudades_ordenadas[fila][1] <= cobertura_maxima:
            fila += 1
            
    return patrullas_elegidas
"""
Justificación Ejercicio 10:
- Complejidad Temporal: O(n log n). El ordenamiento inicial toma O(n log n). El ciclo while exterior y el interior, combinados, visitan cada ciudad exactamente una vez, lo que toma O(n). O(n log n) + O(n) = O(n log n).
- Complejidad Espacial: O(n) en el peor de los casos, donde se requiere un patrullero por cada ciudad.
- ¿Es óptimo?: Sí. Por argumento de intercambio, si un patrullero se coloca a menos de 50km de la ciudad más a la izquierda sin cubrir, desplazarlo exactamente a 50km hacia la derecha nunca dejará de cubrir a esa ciudad, y solo puede aumentar (o mantener igual) la cantidad de ciudades cubiertas hacia la derecha.
"""