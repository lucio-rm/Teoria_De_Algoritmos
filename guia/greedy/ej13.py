"""
Enunciado ejercicio 13:
(★★) Tenemos una ruta recta muy larga, de 'K' kilómetros, sobre la cual hay casas dispersas. En dichas casas vive gente que usa mucho sus celulares. El intendente a cargo la ruta debe renovar por completo el sistema de antenas, teniendo que construir sobre la ruta nuevas antenas. Cada antena tiene un rango de cobertura de 'R' kilómetros (valor constante conocido). 

Implementar un algoritmo Greedy que reciba las ubicaciones de las casas, en número de kilómetro sobre esta ruta (números reales positivos) desordenadas, y devuelva los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan cobertura, y se construya para esto la menor cantidad de antenas posibles. 

Indicar y justificar la complejidad del algoritmo implementado. 
Justificar por qué se trata de un algoritmo greedy. 
¿El algoritmo da la solución óptima siempre?

"""

"""
planteo:
K kilometros - recta
antena - cubre radio R
lista de las ubicaciones de casas


parecido al de los patrulleros, tengo que poner una antena que cubra lo máximo posible.
"""

def cobertura(casas, R, K):
    if not casas:
        return []
        
    casas_ordenadas = sorted(casas) # ordeno de menor a mayor y hago una copia
    
    pos_antenas = []
    fila = 0
    cantidad_casas = len(casas_ordenadas)
    
    while fila < cantidad_casas:
        # 'fila' representa la primera casa a la izquierda que todavía NO tiene cobertura.
        #pongo la antena exactamente R kilómetros adelante de esta casa para exprimir 
        # su rango de cobertura hacia atrás al máximo posible.
        posicion_antena = min(casas_ordenadas[fila] + R, K)
        pos_antenas.append(posicion_antena)
        
        # como la antena tiene un radio de cobertura de R kilómetros, su alcance
        # máximo hacia la derecha de la ruta llega hasta posicion_antena + R
        cobertura_maxima = posicion_antena + R
        
        # sigo con el índice saltando todas las casas que caigan dentro de esta zona protegida
        while fila < cantidad_casas and casas_ordenadas[fila] <= cobertura_maxima:
            fila += 1
            
    return pos_antenas

"""
Justificación:

- Complejidad:
    . temporal: O(nlogn), ya que hacemos un recorrido de n casas (O(n)), y anteriormente habiamos ordenado el arreglo (O(nlogn)). 
        (O(n) + O(nlogn) = O(nlogn))
    . espacial: O(n), ya que en el peor de los casos "pos_antenas" va a tener guardado n elementos. (es en el caso de que cada casa esté a más de R rango entre ellas)

- Greedy:
    . Regla Greedy: la regla greedy que se cumple es en base a la posicion de las casas, poder minimizar la cantidad de antenas usadas.
    . Secuencia: en la secuencia de estados locales (pos), agarro mi óptimo local (cubro la mayor cantidad de radio/distancia posible) por cada posicion. Lo que me lleva al óptimo global, que es minimizar la cantidad de antenas usadas.
    . Optimalidad: es óptimo, ya que por demostracion por induccion se puede demostrar que este mismo algoritmo cumple la optimalidad.

"""