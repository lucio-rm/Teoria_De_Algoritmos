"""
Ej.6 (★★★):
Implementar un modelo de programación lineal que resuelva el problema de Independent Set Máximo.

"""
"""
planteo:

Independent Set máximo: no pueden haber más de dos vértices adyacentes en el independent set.
Quiero la mayor cantidad de vértices a elegir.

- Constantes:
V vértices
E aristas
cada vertice tiene adyacentes.


- Variables:
X_{i} a cada vertice 'i' del grafo G.
E_{i} a cada arista 'i' del grafo G.

van a ser variables del tipo Enteras Binarias. E {1, 0}. 1 si fueron elegidas, 0 si no.

- Inecuaciones:
quiero tener la mayor cantidad de vertices que no sean adyacentes entre sí.

∀(i, k) e E: X_{i} + X_{k} <= 1.
Para todo par de vertices conectados por la arista (i, k), trato de forzar elegir siempre 1 de esos dos.
(nota: acá tendría que usar la big-M? no se me ocurre donde poner la condición. 'si soy 0 y tengo la menor cantidad de ady que mis ady, agarrarme ¿?)



- Función Objetivo:
lo que yo busco en este ejercicio, es maximizar la cantidad de vertices elegidos.
max sum(X_{i})


"""
