"""
Enunciado ejercicio 2:
(★) Explicar por qué el Algoritmo de Prim (para obtener el MST de un grafo no dirigido) es un Algoritmo Greedy.

"""

"""
Justificación Greedy de Prim:
1. Regla Greedy: Dado un conjunto de vértices ya añadidos al árbol (S), en cada 
   paso se selecciona la arista de MENOR peso que conecte cualquier vértice 
   dentro de S con cualquier vértice fuera de S.
2. Al elegir siempre una arista que va hacia afuera de S, se garantiza que no se formen ciclos. La decisión es irrevocable.
3. Subestructura Óptima: En cada paso, el árbol crece localmente de la forma 
   más barata posible. Al igual que Kruskal, se apoya en la 'Propiedad del Corte' 
   para garantizar el óptimo global.
"""