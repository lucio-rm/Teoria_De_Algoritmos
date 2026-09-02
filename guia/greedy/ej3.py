"""
Enunciado ejercicio 3:
(★) Explicar por qué el Algoritmo de Dijkstra (para obtener caminos mínimos desde un vértice, en un grafo con pesos positivos) es un Algoritmo Greedy.

"""

"""
Justificación Greedy de Dijkstra:
1. Regla Greedy: En cada paso, de entre todos los vértices no visitados, se 
   selecciona aquel que tenga la menor distancia tentativa acumulada desde el origen.
2. Una vez que un vértice es seleccionado como el 
   más cercano, se lo marca como visitado y su distancia mínima se considera 
   definitiva (irrevocable).
3. Subestructura Óptima: Si el camino más corto del origen a B pasa por A, el 
   subcamino de origen a A también debe ser el más corto posible. (Nota: Esto 
   solo garantiza el óptimo si NO hay pesos negativos. Si los hay, la regla 
   greedy irrevocable de Dijkstra falla porque un camino futuro podría 'restar' 
   distancia, arruinando la presunción de definitividad).
"""
