"""
Enunciado ejercicio 1:
(★) Explicar por qué el Algoritmo de Kruskal (para obtener el MST de un grafo no dirigido) es un Algoritmo Greedy.

"""

"""
Justificación Greedy de Kruskal:
1. Regla Greedy: En cada paso, el algoritmo selecciona la arista de MENOR peso 
   disponible en todo el grafo.
2. La arista solo se añade al MST si NO forma un 
   ciclo con las aristas previamente seleccionadas (verificado mediante Union-Find). 
   Una vez añadida o descartada, la decisión es irrevocable.
3. Subestructura Óptima: Al unir dos componentes conexas usando la arista más 
   barata posible, el problema se reduce a encontrar el MST de las componentes 
   restantes. Asegura el óptimo global porque, por la 'Propiedad del Corte', 
   la arista de menor peso que cruza un corte siempre pertenece al MST.
"""

