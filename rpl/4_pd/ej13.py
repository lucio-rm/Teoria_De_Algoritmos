"""


Ej.13 (★★★):
Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse.

Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos). 
Indicar y justificar la complejidad del algoritmo.

"""
"""
planteo:

este es lo mismo que el knapscak o subset, o estoy loco?
W = long de la mesa
elem - grupo vector P
tamaño grupo ~ peso y valor

me piden el conjutno de grupos === reconstrucción basandome en si el valor de la celda cambió


ec. recurrencia:
con OPT(i, w) dos variables la maxima cantidad de asientos ocupados considerando los primeros i grupos con una mesa de tamaño w

OPT(i, w) = max(P(i-1) + OPT(i-1, w- P(i-1)), OPT(i-1, w))
- si P(i-1) <= w

a puro for y estamo?
"""
def bodegon_dinamico(P, W):
    if not P or W <= 0:
        return []

    cant = len(P)

    #tabla base 1 para estar comodo con los indices, W+1 columnas y cant+1 filas 
    M_TABLA = [[0] * (W+1) for _ in range(cant + 1)]

    #lleno la tabla
    for i in range(1, cant+1):
        personas = P[i-1] #desfasaje por lo que habia hecho en la creacion de la tabla
        for w in range(1, W + 1):
            if personas <= w:
                #a pura ec. recurrencia
                M_TABLA[i][w] = max(personas + M_TABLA[i-1][w - personas], M_TABLA[i-1][w])
            else:
                M_TABLA[i][w] = M_TABLA[i-1][ w]

    # parte de recosntruccion. es buena practica dejarla en una func auxiliar?
    GRUPOS_ELEGIDOS = []
    i = cant
    w = W
    while i > 0 and w > 0:
        # aplicl la ec. recurrencia inversa, si el valor cambio comparandolo con el de arriba
        #el grupo se sentó
        if M_TABLA[i][w] != M_TABLA[i -1][w]:
            GRUPOS_ELEGIDOS.append(P[i-1])
            w -= P[ i - 1]

        i -= 1 #siempre voy al anterior
        
    return GRUPOS_ELEGIDOS[::-1] # para que quede en orden cronologico, rpl master.



"""
Justificacion de la complejidad:

- temporal: O(n.W) siendo n la cantidad de grupos y W es la capacidad de la mesa. es pesoudo-polinoimoal si esta comlpetamente dependiente de la capacidad. reconstruccion = O(n)

- espacial: O(n.W) porque como mucho la M_TABLA va a tener esa cantidad de elementos.
"""