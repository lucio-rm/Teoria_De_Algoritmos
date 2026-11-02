"""
Enunciado ejercicio 4:
(★★) Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. 
Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, representando en tuplas los horarios de inicios de las charlas, y sus horarios de fin, e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas. 
Indicar y justificar la complejidad del algoritmo implementado.



"""

"""
planteo:
- El objetivo es maximizar la CANTIDAD de charlas, no la duración.
- Si ordeno por hora de inicio, una charla muy larga que empieza temprano me bloquea todo el día.
- Si ordeno por duración (las más cortas), podría elegir una al mediodía que pise la mañana y la tarde.
- Regla Greedy ÓPTIMA: Seleccionar siempre la charla que TERMINE MÁS TEMPRANO. 
  Al terminar temprano, libera el recurso (el aula) lo antes posible, maximizando 
  el tiempo restante para encajar más charlas.
"""

def maximizar_charlas(charlas):
    # charlas es una lista de tuplas (inicio, fin)
    # Paso 1: Ordenar por horario de fin (índice 1 de la tupla)
    charlas.sort(key=lambda x: x[1])
    
    charlas_seleccionadas = []
    tiempo_fin_actual = -1
    
    # Paso 2: Iterar y aplicar regla golosa
    for charla in charlas:
        inicio, fin = charla
        # Si la charla empieza después o exactamente cuando terminó la anterior
        if inicio >= tiempo_fin_actual:
            charlas_seleccionadas.append(charla)
            tiempo_fin_actual = fin # Actualizo la viabilidad para la próxima
            
    return charlas_seleccionadas

"""
Justificacion de complejidad:
- Ordenar el arreglo de charlas cuesta O(n log n).
- Iterar linealmente el arreglo para seleccionar cuesta O(n).
- Complejidad temporal final: O(n log n) + O(n) = O(n log n).
- Complejidad espacial: O(n) para guardar la lista de seleccionadas en el peor caso.
"""
