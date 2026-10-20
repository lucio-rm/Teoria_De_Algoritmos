"""
Ej.8 (★★):
Implementar un modelo de programación lineal que permita determinar el clique de tamaño máximo dentro de un grafo. 
Indicar la cantidad de restricciones generadas en función de la cantidad de vértices y aristas (podés usar notación O para esto, no es importante el número exacto).

"""
"""
planteo:
En teoría de grafos, un clique (o camarilla) es un subconjunto de vértices de un grafo en el que cada par de vértices está directamente conectado por una arista.


- Constantes:
V vertices
E aristas
del grafo.


- Variables:
sea X_i E {0, 1} una variable entera binaria, la cual representa 0 si el vértice_i no fue elegido, o 1 de caso contrario.
sea Y_i E {0, 1} lo mismo, pero representando las aristas.

- Inecuaciones:
idea: entre cada subgrafo, la cantidad de aristas tiene que ser igual a la cantidad de vértices.
∀i, j (X_i, Y_j)    X_i <= Y_i(M - (X_i, Y_j))
siendo M = |v| + |E| + 1
y la cantidad de inecuaciones utilizadas son en el peor de los casos: V + E

- Función Objetivo:
maximizar la cantidad de vertices en el subgrafo:
\max(X_i), total maximizando los vértices que cumplan con la inecuación, también maximizo la cantidad de aristas utilizadas.

"""


# pulp.
