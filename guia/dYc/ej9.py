"""
Enunciado ejercicio 9:
(★★★) Implementar una función, que utilice división y conquista, de complejidad O(nlogn) que dado un arreglo de 'n' números enteros devuelva true o false según si existe algún elemento que aparezca más de la mitad de las veces. 
Justificar la complejidad de la solución. 
Ejemplos:
[1, 2, 1, 2, 3] -> false
[1, 1, 2, 3] -> false
[1, 2, 3, 1, 1, 1] -> true
[1] -> true

Aclaración: Este ejercicio puede resolverse, casi trivialmente, ordenando el arreglo con un algoritmo eficiente, o incluso se puede realizar más rápido utilizando una tabla de hash. Para cumplir con la consigna, resolver sin ordenar el arreglo ni con tabla de hash, sino puramente por división y conquista.


"""
"""
planteo:
- Problema del Elemento Mayoritario (K&T Sección 5.3).
- Por teorema, un elemento mayoritario global DEBE ser mayoritario en alguna de las dos mitades.
- D&C: Dividimos el arreglo a la mitad. Pedimos el candidato mayoritario de la izquierda y el candidato de la derecha.
- Si ambos candidatos son iguales, ese es nuestro ganador absoluto para este segmento.
- Si son distintos, iteramos linealmente SOLO sobre este segmento del arreglo (usando punteros low y high) para contar cuántas veces aparece el candidato izquierdo y el candidato derecho. 
- El que tenga más de (longitud_del_segmento // 2) apariciones gana y sube de nivel. Si ninguno supera la mitad, retornamos None.
- Al final de la recursión principal, si obtuvimos un candidato distinto a None, devuelvo True, sino False.
"""
def aparece_mas_mitad(arreglo):
    if not arreglo:
        return False
        
    # Función auxiliar para no copiar arreglos en memoria y mantener punteros
    def dyc_mayoritario(low, high):
        # Caso base: 1 solo elemento. Es mayoría de sí mismo.
        if low == high:
            return arreglo[low]
            
        mid = (low + high) // 2
        
        # Conquista
        cand_izq = dyc_mayoritario(low, mid)
        cand_der = dyc_mayoritario(mid + 1, high)
        
        # Si ambas mitades están de acuerdo en el ganador, retorna ese candidato
        if cand_izq == cand_der:
            return cand_izq
            
        # Si discrepan, contamos las ocurrencias de ambos en el segmento actual
        conteo_izq = 0
        conteo_der = 0
        
        for i in range(low, high + 1):
            if arreglo[i] == cand_izq:
                conteo_izq += 1
            elif arreglo[i] == cand_der:
                conteo_der += 1
                
        # Evaluamos quién es mayoría en este segmento (tamaño = high - low + 1)
        mitad = (high - low + 1) // 2
        
        if cand_izq is not None and conteo_izq > mitad:
            return cand_izq
        elif cand_der is not None and conteo_der > mitad:
            return cand_der
        else:
            return None # Ninguno logró la mayoría en este segmento combinado

    # Ejecución principal
    candidato_final = dyc_mayoritario(0, len(arreglo) - 1)
    
    # Si retornó un candidato, es porque sobrevivió superando la mitad
    # en la raíz de toda la recursión.
    return candidato_final is not None

"""
justificacion de la complejidad:
Utilizando el Teorema Maestro: T(n) = aT(n/b) + f(n)
- a = 2 (se realizan dos llamadas recursivas por nivel, izquierda y derecha).
- b = 2 (el espacio de búsqueda se reduce a la mitad dividiendo entre low y high).
- f(n) = O(n). La función combina los resultados iterando desde `low` hasta `high` (un ciclo for). En el peor de los casos (en la raíz), itera `n` veces. No hay slices que generen overhead innecesario.
Ecuación: T(n) = 2T(n/2) + O(n).
Calculamos log_b(a) = log_2(2) = 1.
El costo de f(n) tiene grado polinomial C = 1.
Como log_b(a) == C, estamos en el Caso 2 del Teorema Maestro.
Complejidad final estricta: Θ(n log n).
Cumple con la restricción del enunciado de no ordenar (que sería n log n pero sin D&C) y de no usar tabla hash (que sería O(n) tiempo pero O(n) espacio no permitido).
"""