"""
Ej.7 (★★):
Implementar un modelo de programación lineal que determine la cantidad mínima de colores a utilizar para poder pintar a un grafo de colores, de tal forma que ningún adyacente comparta color entre sí.

"""
"""
planteo:
como mucho voy a necesitar K = #Vertices (en el peor caso)
entonces hago 2 familias de variables binarias
1- si vale 1 si al vertice v lo pinto de color c
2- que valga 1 si el color c fue usado en al menos un vertice del grafo.

- Constantes:
Grafo G = (V, E), cantidad máxima posible de colores K = |V|, y constante M = |V| + 1

- Variables:
Sea X_{v}{c} ∈ {0, 1} una variable binaria para cada v ∈ V y cada color c ∈ {1,2,...,K}, que vale 1 si el vértice v se pinta de color c, y 0 si no.

Sea U_{c} ∈ {0, 1} una variable binaria para cada color c ∈ {1,2,...,k}, que vale 1 si el color c es usado por algún vértice, y 0 si no se usa.

- Inecuaciones:
1. si o si cáda vertice tiene que estar pintado de exactamente un único color (|V| ecuaciones):
           k
∀v ∈ V:    ∑ X_{v}{c} = 1
          c=1

2. ningun par de vertices ady. tiene que tener el mismo color c (uso big-M por vértice y color para evitar depender de |E|, terminando en |V|.K inecuaciones)
∀v ∈ V, ∀c ∈ {1,2,...,K}:      X_{v}{c} + ∑ X_{w}{c} ≤ 1 + M.(1-X_{v}{c})
                                        w∈ady(v)

3. SI al menos un vértice usa el color c, la variable U_c tiene que activarse en 1 (K inecuaciones, con el truco del OR)
∀c ∈ {1,2,...,K}:       ∑ X_{v}{c} ≤ |V|.U_{c}
                      v ∈ V

- Función Objetivo:
Minimizar la cantidad total de colores usados:
    K
min ∑ U_{c}
   c=1

"""

# pulp