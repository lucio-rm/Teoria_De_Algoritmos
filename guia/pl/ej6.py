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

"
okey.
esta mal, pero no tan mal.
hay que mejorar los tiempos de ejecución.
con esa fórmula, tengo E inecuaciones.
SIEMPRE que se pueda, reducir la cantidad de inecuaciones al mínimo. sino se considera R o M el ejercicio.
"

- f. objetivo2:
∀i, X_i + sum ( Y_k <= 1 + M(1 - Y_i))
        k E ady(i)

SIEMPRE DECIR CUÁNTO ES M, (M SIEMPRE TIENE QUE SER LO MENOR POSIBLE, nunca infinito. en este caso M = |V| + 1)

- Función Objetivo:
lo que yo busco en este ejercicio, es maximizar la cantidad de vertices elegidos.
max sum(X_{i})


"""
