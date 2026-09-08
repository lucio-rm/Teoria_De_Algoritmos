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
    casas.sort() #ordeno de menor a mayor en base a la posicion en la recta K

    dist_min = casas[0] + R # sabemos que el mejor optimo local primero va a ser el de la posicion minima de la primer casa. y el rango va a cubrir todo eso.
    pos_antenas = []
    pos_antenas.append(dist_min - (R//2)) # la posicion de la antena != distancia cubierta por el rango.
    for pos in range(casas):
        if casas[pos] <= dist_min:
            continue # si ya esta cubierta por el rango, sigo.
        else:
            dist_min = casas[pos] + R # actualizo la distancia minima de donde llega el rango.
            pos_antenas.append(casas[pos] - (R//2)) # agrego la posicion de la antena puesta.

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