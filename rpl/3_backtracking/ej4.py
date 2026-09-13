"""
Enunciado ej4:
Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un máximo Independent Set del mismo.


"""
"""
planteo:

es la misma shit que el ej.1, o no? solo que ahora en vez de tener un numero prioritario 'n'. buscamos la mayor cantidad hasta no poder más, no?

ahora, como vergovich sé yo cuál es la mayo cantidad, o que tengo que volver para atras (hacer la poda) de forma tal que sé que el anterior tuvo que ir para otro lado? hay una formula para saber que en 'x' grafo , saber automaticament4 cuántos puedo hacer?

digo, consigno un IS comoe l ej.1, ahora cómo sé que es el máximo? y no habia otra forma de conseguir más? existe un teorema sobre esto?

"""
"""
planteo ej.4:
- como me piden el maximo independent set, tengo que probar todas las combinaciones validas y quedarme con la mas grande.
- llevo un registro de la "mejor_solucion".
- recorro los vertices. por cada vertice tomo la decision de agregarlo o no agregarlo[cite: 1].
- si lo agrego, me aseguro que no sea adyacente a ninguno que ya puse en mi solucion parcial.
- la poda clave aca para no hacer fuerza bruta inútil: si la cantidad de vertices que tengo en mi solucion parcial, sumada a la cantidad de vertices que todavia me faltan procesar, es menor o igual a la longitud de mi "mejor_solucion" actual, corto la rama. no tiene sentido seguir bajando porque aunque agregue a todos los que quedan, no voy a superar mi record.
"""
def max_independent_set(grafo):
    vertices = grafo.obtener_vertices()
    return _max_is_rec(grafo, vertices, 0, [], [])

def _es_compatible(grafo, v, solucion_parcial):
    for w in solucion_parcial:
        if grafo.estan_unidos(v, w):
            return False
    return True

def _max_is_rec(grafo, vertices, indice, solucion_parcial, mejor_solucion):
    # Caso base: procesamos todos los vértices
    if indice == len(vertices):
        if len(solucion_parcial) > len(mejor_solucion):
            return solucion_parcial[:]
        return mejor_solucion
    
    # Poda: si asumiendo que metemos todos los que quedan no superamos el máximo, podamos
    if len(solucion_parcial) + (len(vertices) - indice) <= len(mejor_solucion):
        return mejor_solucion

    v = vertices[indice]

    # Decisión 1: Lo incluyo (si es válido)
    if _es_compatible(grafo, v, solucion_parcial):
        solucion_parcial.append(v)
        mejor_solucion = _max_is_rec(grafo, vertices, indice + 1, solucion_parcial, mejor_solucion)
        solucion_parcial.pop() # Backtracking
    
    # Decisión 2: No lo incluyo
    mejor_solucion = _max_is_rec(grafo, vertices, indice + 1, solucion_parcial, mejor_solucion)

    return mejor_solucion

"""
Justificacion de la complejidad ej.4:
- temporal: O(2^V). En el peor de los casos, por cada uno de los V vértices, abrimos dos ramas recursivas (usarlo o no usarlo). El chequeo de adyacencia toma a lo sumo O(V). La poda recorta drásticamente el tiempo real, pero el peor caso teórico sigue siendo exponencial.
- espacial: O(V). La pila de recursión se anida hasta V veces. Las listas "solucion_parcial" y "mejor_solucion" guardan a lo sumo V vértices.
El Independent Set es un problema NP-Completo, por lo que no se conoce un algoritmo polinomial determinístico que lo resuelva para el caso general de cualquier grafo.
"""