"""
Enunciado ejercicio 14:
(★★) Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. 
Implementar un algoritmo Greedy que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”). 

Indicar y justificar la complejidad del algoritmo implementado. 
¿El algoritmo implementado da siempre la solución óptima? Justificar

"""

"""
planteo:
maso menos la misma shit, solo que ahora estamos en R².

por cada submarino, voy a tener que recorrer la matriz n.m para actualizar la matriz.
siendo: 
en el rango del faro, 
- un 1 si en esa posicion de la matriz pongo un faro y cubre 1 submarino
- un 2 si en esa pos. el faro cubre 2 submarinos
etc.

entonces por cada submarino tengo que comprobar.


NO es óptimo. peudo encontrqar un caso que en vez de poner 4 faros pone 5.

estos serían los pasos:
1. guardo en un conjunto las coordenadas de todos los submarinos desprotegidos
2. agrego el mejor faro encontrado a la lista (como tupla x, y)
3. saco del conjunto a todos los submarinos que este faro ya iluminó
"""

def submarinos(matriz):
    if not matriz:
        return []
        
    cantidad_filas = len(matriz)
    cantidad_columnas = len(matriz[0])
    
    # 1. guardo en un conjunto las coordenadas de todos los submarinos desprotegidos
    submarinos_restantes = set()
    for fila in range(cantidad_filas):
        for columna in range(cantidad_columnas):
            if matriz[fila][columna]:  # si hay un submarino (True)
                submarinos_restantes.add((fila, columna))
                
    faros_elegidos = []
    
    #sigo hasta iluminar todos los submarinos
    while submarinos_restantes:
        mejor_cantidad = -1
        mejor_fila, mejor_columna = -1, -1
        
        # recorro cada celda de la matriz para ver dónde conviene poner el faro
        for fila in range(cantidad_filas):
            for columna in range(cantidad_columnas):
                # cuento cuántos submarinos (que siguen desprotegidos) cubre esta posición (radio 2)
                cobertura_actual = 0
                
                # Un radio de 2 significa que nos movemos desde -2 hasta +2 en ejes y diagonales
                for desplazar_f in range(-2, 3):
                    for desplazar_c in range(-2, 3):
                        f_vecina = fila + desplazar_f
                        c_vecina = columna + desplazar_c
                        
                        # Si la celda vecina está dentro de los límites y tiene un submarino sin cubrir
                        if (f_vecina, c_vecina) in submarinos_restantes:
                            cobertura_actual += 1
                            
                # Regla Greedy: nos quedamos con el que cubra más
                if cobertura_actual > mejor_cantidad:
                    mejor_cantidad = coverage_actual = cobertura_actual
                    mejor_fila = fila
                    mejor_columna = columna
                    
        # si ya no puedo cubrir a nadie (caso borde raro), rompo para evitar bucle infinito
        if mejor_cantidad <= 0:
            break
            
        # 2.agrego el mejor faro encontrado a la lista (como tupla x, y)
        faros_elegidos.append((mejor_fila, mejor_columna))
        
        # 3. saco del conjunto a todos los submarinos que este faro ya iluminó
        submarinos_iluminados = []
        for desplazar_f in range(-2, 3):
            for desplazar_c in range(-2, 3):
                f_vecina = mejor_fila + desplazar_f
                c_vecina = mejor_columna + desplazar_c
                if (f_vecina, c_vecina) in submarinos_restantes:
                    submarinos_iluminados.append((f_vecina, c_vecina))
                    
        for submarino in submarinos_iluminados:
            submarinos_restantes.remove(submarino)
            
    return faros_elegidos

"""
Justificación Ejercicio 14:
- Complejidad Temporal: O((n*m)^2). Sea 'n' la cantidad de filas y 'm' la cantidad de columnas de la matriz. 
  En el peor de los casos (matriz llena de submarinos), el bucle while externo se ejecutará hasta (n*m) veces 
  (poniendo un faro por iteración). Adentro, recorremos toda la matriz evaluando cada celda para poner el faro (n*m). 
  El chequeo del radio de 2 celdas toma un tiempo constante fijo de 5x5 = 25 operaciones O(1). 
  Por lo tanto, la complejidad dominante es (n*m) * (n*m) = O((n*m)^2).
  
- Complejidad Espacial: O(n*m) en el peor de los casos, requerido para almacenar las posiciones en el conjunto 
  'submarinos_restantes' y la lista de faros devuelta.

- ¿El algoritmo implementado da siempre la solución óptima?: NO.
- Justificación de optimalidad: El problema de cobertura de celdas mediante un radio en una matriz bidimensional 
  es un caso del "Set Cover Problem" (o "Dominating Set") modelado sobre un grafo de rejilla, el cual pertenece a 
  la categoría de problemas NP-Hard. Las aproximaciones Greedy toman la mejor opción local en cada paso 
  (la celda que más submarinos desprotegidos cubra en el momento), pero esto acarrea decisiones subóptimas globales 
  por falta de visión a futuro, pudiendo dejar submarinos aislados que fuercen la colocación de más faros de los necesarios.
"""
