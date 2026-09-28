"""

Ej.2 (★★★):
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Además, cada charla tiene asociado un valor de ganancia. 
Implementar un algoritmo que, utilizando programación dinámica, reciba un arreglo que en cada posición tenga una charla representada por una tripla de inicio, fin y valor de cada charla, e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida. 

Indicar y justificar la complejidad del algoritmo implementado.


"""

"""
planteo:
ahora si tengo que armar un memoization. 

tambien tengo que saber qué charlas estas superpuestas con otras.

minimo e indispensable: ordenar por inicio.

no me acuerdo qué variables, arreglos, dicc, etc. iban en mayuscula. de memoization. y por que ¿?

primero tengo que pensar en la ecuacion de recurrencia.
subproblemas: dar la charla, o no dar la charla.

OPT(j) = max(vj + OPT(p(j)), OPT(j-1))

tengo que tener el arreglo p(jotas) para saber a donde va la superposicion de charlas.

"""
def scheduling(charlas):
    if not charlas:
        return []
    c_ordenadas = sorted(charlas, key=lambda x: x[1]) # ordenar por fin
    
    # calculo p(j)
    dicc_p = _calcular_p(c_ordenadas)
    
    # resuelvo por pd y reconstruyo
    return _scheduling_dinamico(c_ordenadas, dicc_p)


def _calcular_p(charlas):
    """
    Para cada charla j, encuentra el índice de la ultima charla compatible que termina antesigual al inicio de la charla j.
    importantisimo = se usa busqueda binaria para garantizar O(n log n) en total
    """
    n = len(charlas)
    p = [0] * (n + 1)  # se usa base 1 para los índices de las charlas
    
    for j in range(1, n + 1):
        inicio_actual = charlas[j - 1][0]
        
        #busqueda binaria en las charlas anteriores (0 hasta j-2)
        izq, der = 0, j - 2
        pos_compatible = 0  # 0 significa que ninguna anterior es compatible
        
        while izq <= der:
            medio = (izq + der) // 2
            if charlas[medio][1] <= inicio_actual:
                pos_compatible = medio + 1  # guardo en base 1
                izq = medio + 1  # se busca si hay una más adelante que también termine antes
            else:
                der = medio - 1
                
        p[j] = pos_compatible
    return p


def _scheduling_dinamico(charlas, dicc_p):
    cant = len(charlas)
    
    # guardo el valor optimo
    M_SCHE = [0] * (cant + 1)
    
    # lleno la tabla
    for j in range(1, cant + 1):
        # uso la ec. de recurrencia
        valor_charla = charlas[j - 1][2]
        opcion_tomar = valor_charla + M_SCHE[dicc_p[j]]
        opcion_no_tomar = M_SCHE[j - 1]
        
        M_SCHE[j] = max(opcion_tomar, opcion_no_tomar) 
        
    # hago la reconstrucción para saber cuales charlas devolver
    # voy de atras para adelante en M_SCHE para ver cuales elijo
    charlas_elegidas = []
    j = cant
    while j > 0:
        valor_charla = charlas[j - 1][2]
        # si el valor cambió porque sumo esta charla, es porque la elegimos
        if valor_charla + M_SCHE[dicc_p[j]] >= M_SCHE[j - 1]:
            charlas_elegidas.append(charlas[j - 1])
            j = dicc_p[j]  # voy a la última charla compatible
        else:
            j -= 1  # no la elijo, voy a la anterior 
            
    # como fué de atras para adelante, las invertimos para que queden cronológicas
    return charlas_elegidas[::-1] #era eso o usar .inverted()

"""
Justificación de la complejidad:
temporal: O(n log n) siendo n la cantidad de charlas.
- Ordenamiento: ordear las charlas por fin  O(n log n)
- calculo de P: itero n veces, y en cada iteración hacemos una busqueda binaria sobre un rango máximo de n elementos. O(n) * O(log n) = O(n log n).
- ec. recurrencia: Recorremos las n charlas una sola vez. En cada paso pregunto en O(1) a M_SCHE y dicc_p. O(n).
- Reconstrucción: En el peor de los casos recorro la tabla hacia atras en n pasos. O(n)

O(n log n) + O(n log n) + O(n) + O(n) = O(n log n).

espacial: O(n)
A lo sumo voy a tener N elementos guardados.
"""