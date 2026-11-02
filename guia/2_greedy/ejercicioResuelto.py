"""
Ejercicio resuelto

Enunciado

Implementar un algoritmo greedy que permita obtener el Dominating Set mínimo (es decir, que contenga la menor cantidad de vértices) para el caso de un árbol (en el contexto de teoría de grafos, no un árbol binario). 
Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. 
Indicar si el algoritmo siempre da solución óptima. Si lo es, explicar detalladamente, sino dar un contraejemplo.


Consideración
Dado que es posible que para cuando estén realizando los ejercicios de Greedy aún no hayan visto sobre el problema de Dominating Set, aquí damos su definición:

Un dominating set de un grafo es un subconjunto de vértices de dicho grafo tal que, para cada vértice del grafo, dicho vértice pertenece al dominating set, o bien alguno de sus adyacentes pertenece al dominating set.

"""
"""
Solución
Una primera idea que puede surgir es justamente pensar en los grados de los vértices. 
Tal como vimos Además, sabiendo que todo árbol de al menos 2 vértices tiene al menos 2 hojas que (al igual que el resto de vértices en el árbol) deben “ser dominadas”, quedaría una decisión que tomar: 
o bien incluir la hoja en el dominating set, o a sus respectivos adyacentes. 

Dado que queremos minimizar la cantidad de vértices en el dominating set, nos conviene poner el vértice que “más pueda dominar”. En particular, es claro que conviene el adyacente a la hoja, que puede cubrir más de uno.

Acá pueden surgir varios errores. 
El error más común es el siguiente: 
ordenar de menor a mayor grado, agregando el vértice y “anulando los que siguen”. Esto es un error porque estamos justamente agarrando al vértice contrario al que nos conviene (de óptimo local, nada). 
Ok, corrijamos eso, podríamos decir que ordenamos de menor a mayor grado, y en ese orden nos quedamos con el adyacente a dicho vértice. 
El problema ahora es que puede haber vértices ya dominados que generan la falsa ilusión de que un vértice estaría dominando efectivamente la mayor cantidad posible de vértices por ser sus adyacentes. 
Entonces, por lo mencionado, tenemos que considerar cuáles vértices ya están siendo dominados (es decir, quienes o bien están en el conjunto o tienen un ayacente en el conjunto). 
Esto empieza a tener algo de sentido. 
¿El problema? Esto tiene un error conceptual gravísimo: técnicamente, no es un algoritmo greedy. Si quien lee dice “pero si ordené!”, ordenar no hace que un algoritmo sea greedy. Ordenar es únicamente una optimización que encontramos cuando el valor por el que vamos a ir buscando “el siguiente mínimo/máximo” no se ve alterado. 
Pero en este caso, eso no es cierto. Acá nos interesa ver por grado, a medida que, básicamente, estamos eliminando vértices del grafo para dejar de considerarlos. Esto altera el grado que debo considerar, por lo que el estado cambió y debo buscar el nuevo mínimo. 
El tema aquí es que haber ordenado y no considerar las modificaciones quita el elemento “local”. Cuando decimos que buscamos un óptimo local, justamente es local al estado de la iteración como la tenemos, no necesariamente esto está relacionado al estado original. 
Hay algoritmos donde el estado original va a permanecer para servirnos como óptimos locales (ejemplo, el algoritmo de Kruskal), pero en otros no es el caso y hay que ir considerando las actualizaciones (ejemplos, Dijkstra y Huffman). 
Por supuesto esto demora más, pero… es óptimo. La otra alternativa no es siquiera óptima, además de no ser enteramente greedy.


Para darles un contraejemplo, supongamos un grafo:
A - B - D - F
    |   |
    C   E
En este caso, inicialmente cubriremos B (o D), eliminando a A, C y D en el camino, dejándonos con E y F, los cuáles ambos deberían ser incluídos, dejándonos con un Dominating Set de 3 vértices cuando el óptimo es de 2 (B y D). 
Podríamos seguir agregando condiciones, pero hay que tener cuidado de no decir “bueno, ahora intento considerar una opción y otra”, cuando un algoritmo greedy aplica una simple regla para buscar el óptimo local.


Entonces, volvemos a plantear la solución realmente greedy:

Buscamos un vértice de grado 1. A su adyacente lo agregamos al dominating set.
Agregamos al conjunto de vértices dominados al vértice que agregamos al dominating set y a todos sus adyacentes
Eliminamos del grafo a: el vértice de grado 1, al agregado al dominating set, y también a todos los adyacentes al vértice agregado que sean hojas (es decir, este podría estar vinculado a varias hojas), o que por eliminar a este pasaran a ser hojas (ya dominadas, no traen otro beneficio).
Volvemos a buscar algún vértice de grado 1 aplicando la misma lógica, hasta que no queden vértices en el grafo, o solo queden vértices de grado 0
Finalmente, si no quedan vertices de grado 1 pero el grafo aún tiene vertices (necesariamente todos los vértices que quedan tienen grado 0), agregamos al dominating set a los vértices del grafo que aún no están en el conjunto de dominados.
"""
from tdas import grafo
def dominating_set_arbol(grafo):
    ds = set()
    dominados = set()
    while len(grafo) > 0:
        v = obtener_vertice_grado_1(grafo)
        if v is None:
            break

        w = grafo.obtener_grado_adyacentes(v)[0]
        ds.add(w)
        dominados.add(w)
        for x in grafo.adyacentes(w):
            dominados.add(x)
            if len(grafo.adyacentes(x)) <= 2:
                grafo.borrar_vertice(x)
        grafo.borrar_vertice(w)
    
    for v in grafo:
        if v not in dominados:
            ds.add(v)

    return ds

def obtener_vertice_grado_1(grafo):
    for v in grafo:
        if len(grafo.adyacentes(v)) == 1:
            return v

"""
Hay otras formas de implementar esto (buscar en cada iteración a los vértices de grado 1 y aplicar esta lógica), que en sí sería lo mismo. También se puede obviar “eliminar” los vértices y simplemente ir modificando un diccionario con grados y cosas por el estilo.



La complejidad de este algoritmo es O(n²), por la búsqueda de vértices de grado 1 en cada iteración. 

El algoritmo es greedy ya que iterativamente, a través de una regla sencilla, se busca aquel vértice que me maximiza la cantidad de hojas a dominar, las cuales son fáciles de detectar lo que conviene. 
Siendo este el óptimo local. Al saber que alguno de estos tiene que ir si o si, y que al eliminar una hoja siempre vamos a seguir teniendo un árbol (→ va a tener al menos 2 hojas), entonces esta lógica siempre será correcta. Y por esto mismo el algoritmo será óptimo (no pedimos una demostración formal en el parcial, pero la idea viene justamente por ese lado, y usando el absurdo).

Alguien podría pensar que al no borrar todos los vértices adyacentes al que estamos agregando cometemos un error porque no estamos considerando que este ya se encuentra dominado. 
Esto es un error: estamos justamente considerando que a pesar de estar dominado, esto no hace que no convenga nunca incluirlo (mirar el contraejemplo anterior). 
Si no se lo elimina es porque tiene otro adyacente que aún falta por dominar.



"""