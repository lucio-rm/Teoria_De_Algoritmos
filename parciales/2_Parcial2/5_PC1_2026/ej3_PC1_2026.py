"""
Enunciado 3. 
El problema del Subgrafo K-J Completo (SKJC) se define como: 
Dado un grafo y dos valores K y J, ¿existe un subgrafo dentro de dicho grafo, de *a lo sumo* K vértices donde todos los vértices se conecten con *al menos* J de los demás vértices del subgrafo?
Demostrar que el problema del Subgrafo K-J Completo es un problema NP-Completo. 
Recomendamos recordar que el problema de K-Clique es un problema NP-Completo. 

Leer atentamente en la definición del problema los “a lo sumo” y “al menos”.

"""

"""
planteo:


el ejercicio ya está en formato de decision.

tengo que tener SKJC

- GRAFO G
- subgrafo H de G con <= K vértices
- cada vértice de H tiene que tener >= J adyacentes (entre los v del subgrafo)



0. Definir el problema en su versión de Decisión
    . ya está hecho por suerte, solo devuelve True/False.
1. Demostrar que está en NP
    . hablar de qué es NP
    . hacer el validador
2. Reducir un problema NP-Completo a SKJC
    . ya nos dan la pista del K-Clique (esta facil)
    . hablo del K-Clique
    . Encuentro transformación / relación entre Y - X
3. Demuestro la correctitud
    . si y solo si
    . instancia de Y verdadera ↔ instancia construida de X es verdadera
"""

"""
0. ok
"""
"""
1. 
Un problema está en NP si, dada una solución (certificado) del problema, puedo verificar si es correcta en tiempo polinomial mediante un validador (certificador).
"""
def validador(grafo, solucion, k, j):
    # la solucion va a ser representada con una lista de vértices que representarían una solución candidata del problema. en tiempo polinomial tengo que verificar si es correcta dada el grafo original, y los enteros K y J.
    vertices = grafo.obtener_vertices()

    #check 1: cantidad de vértices de la solución es mayor a la cantidad de vértices generales del grafo
    if len(solucion) > len(vertices):
        return False

    #check 2: que todos los vértices de la solución, estén en el grafo original.
    for vertice in solucion:
        if vertice not in vertices:
            return False

    """
    check 3: verifico propiedades SKJC
    1. que la cantidad de vertices sea menor igual a K
    2. que todos los vertices de la solución tengan como adyacentes a lo sumo J vértices, que TAMBIEN pertenezcan a la solucion (que no sean ajenos al subgrafo)
    """
    if len(solucion) > k:
        return False

    for v in solucion:
        adyacentes = grafo.obtener_adyacentes(v)
        if len(adyacentes) < j or len(adyacentes) > k:
            return False
        for w in adyacentes:
            if w not in solucion:
                return False

    # si pasó todos los chequeos, significa que es una solución correcta del problema SKJC
    return True
"""
Complejidad del certificador:
1. obtengo vertices del grafo -> O(V)
2. recorro los vertices de la solucion -> O(K) (a lo sumo van a ser K)
3. recorro todos los vertices de la solucion y por cada uno, obtengo y recorro sus adyacentes. en el peor de los casos, J == K y la mayor cantidad de adyacentes que puede tener cada vértice (sin romper la propiedad del problema) es igual a la cantidad de vértices del subgrafo, lo cual lo hace un subgrafo completo, lo cual chequearlo termina teniendo un costo de O(K.K) = O(K²)

En el peor de los casos, K va a ser la cantidad de vértices totales del grafo original, lo cual V = K.

Complejidad temporal final: O(V) + O(V) + O(V²) = O(V² + 2V) (como V² > 2V) = O(V²)
Validador en tiempo polinomial.
"""

"""
2. 
caracteristicas entre K-Clique y SKJC
el clique:
es un subgrafo COMPLETO de un grafo G
es una instancia del SKJC donde J == K
entonces yo sé que si encuentro un subgrafo completo de a lo sumo K vértices, un K-Clique, sé que voy a tener un SKJC de al menos J (siempre y cuando J <= K, pero si J > K no tiene sentido, sería absurdo.).
"""

"""
3. 



"""







