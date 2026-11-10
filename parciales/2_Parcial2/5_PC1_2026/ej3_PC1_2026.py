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

        # no me sirve solo con chequear que sea a lo sumo J. tengo que verificar que los adyacentes ∈ al subgrafo de la solución.
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



Entonces, sé que teniendoc cualquier instancia / solución de un K-Clique, voy a tener una solución de un SKJC. Ya que, en SKJC, cada vértice del subgrafo tiene una cantidad de adyacentes ∈ [J, K]. Al menos, va a tener J vértices adyacentes ∈ subgrafo, eso significa que a lo sumo puede tener permitido K adyacentes.




Relación entre K-Clique y SKJC:
Si tengo una instancia del K-Clique <----> Tengo una instancia del SKJC ∀ K, J ∈ R.

Relación entre SKJC y K-Clicque:
Si tengo una instancia del SKJC, donde J == K ----> tengo una instancia del K-Clique
(#nota: si J < K, puedo forzar a los vértices a que tengan más ady. hasta llegar a K?)
"""

"""
3. 
Demostración por Método Directo:
Hipótesis ==> Tesis
A -  Si Tengo un K-Clique en g ==> Tengo un SKJC en g

Y para el Si y sólo Si:
B -  Si Tengo un SKJC en g' ==> Tengo un K-Clique en g'



A.
La definición de un K-Clique es, que dado un valor numérico K, un K-Clique es un subgrafo COMPLETO de G, que tiene K vértices.
Un subgrafo completo, significa que cada vértice tiene como adyacente a todos los vértices del subgrafo.

La relación con el SKJC, es que, sabiendo que tengo un K-Clique, si o si voy a tener una instancia del SKJC (siempre y cuando la K sea la misma entre los dos problemas).

(#nota: en el cuaderno voy a hacer un grafico. en el vsStudio ta complicado dibujar bien. pero es sencillo. el dibujo va a ser una instancia del K-Clique y colorear los adyacentes, dando significado a J, etc etc.)

En el problema del SKJC, un J significa que cada vértice del subgrafo se conecte con AL MENOS J vértices. entonces como máximo J puede ser igual a K, y si no lo es, la propiedad permite que cada vértice se conecte con A LO SUMO K vértices, si tengo un K-Clique, cada vértice se esta conectando con a lo sumo K vértices. Por lo que tengo un SKJC.


B.
Ahora, si tengo una instancia del problema SKJC, la transformación que le hago a cualquier solución del problema SKJC, es que a cada vértice, con sus respectivos adyacentes (pueden variar la cantidad), los voy a aumentar hasta llegar a K adyacentes a cada uno.
La razón de esta decisión es que, con una instancia del SKJC, cada vértice va a tener a lo sumo J adyacentes.
Lo cual que si a cada vértice le AUMENTO la cantidad de adyacentes que tiene, sin sobrepasarme de K y llegando HASTA K, cada vértice va a seguir cumpliendo con la propiedad del SKCJ y sigue siendo parte de la solución. Sólo que ahora, con esta nueva instancia creada polinomialmente*, tengo una instancia del K-Clique.

(#nota: acá hago otro dibujo, con una instanciade SKJC que no sea un subgrafo completo, y que lo voy a llevar a éste en tiempo polinomial).


*polinomialmente, me refiero a que la transformación se puede realizar recorriendo cada vértice 'i' de la solución (O(V)) y que por cada vértice, recorro otra vez cada vértice 'j' de la solución, creando la arista (i, j) si no estaba creada. Creando a lo sumo (K-J) aristas en tiempo O(V²).


Concluyendo la demostración,

Para la ida:
Si tengo Cualquier instancia del K-Clique ---> Tengo una instancia del SKJC, sin importar el J propuesto, cumple con la propiedad del problema.


Para la vuelta:
Si tengo Cualquier instancia del SKJC, realizo una transformación de la solución/subgrafo, para cualquier K/J, aumento los adyacentes de cada vértice hasta tener un subgrafo completo*         ----------> Tengo una instancia del K-Clique.

*Tener un subgrafo compelto, mantiene con la propiedad del SKJC.
"""







