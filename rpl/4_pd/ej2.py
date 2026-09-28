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
    c_ordenadas = charlas.sorted(lambda x: x[0]) # ordeno por inicio
    dicc_p = _siguiente_a_quien(charlas)
    return _scheduling_dinamico(c_ordenadas, dicc_p)

def _scheduling_dinamico(charlas, dicc_p):
    cant = len(charlas)
    if cant == 0:
        return 0
    M_SCHE = [0] * (cant + 1)
    M_SCHE[0] = 0
    for j in range(1, cant+1):
        M_SCHE = max(charlas[j][2] + M_SCHE[dicc_p[j]], M_SCHE[j-1]) # ecuacion de recurrencia
    return M_SCHE[cant]

# constructor del diccionario de colisiones 'p'
def _siguiente_a_quien(charlas):
    dicc_p = {}
    for i in range(0, len(charlas)): # charla i
        dicc_p[charlas[i]] = None
        inicio = charlas[i][0]
        fin = charlas[i][1]
        for j in range(0, len(charlas)): # charlas j (las que le siguen a i)
            sigue_inicio = charlas[j][0]
            sigue_fin = charlas[j][1]
            if sigue_inicio >= fin:
                dicc_p[charlas[i]] = charlas[j]
                break
            else:
                continue
        if dicc_p[charlas[i]] == None: # no le sigue ninguna sin superponerse.
            dicc_p[charlas[i]] = dicc_p[charlas[i-1]] # va la anterior ¿?
    return dicc_p


"""
Justificación de la complejidad:
Temporal: O(n.logn) siendo n la cantidad de charlas
    - scheduling: ordena O(nlogn)
    - scheduling_dinamico: recorre todas las n charlas. O(n)
    - _siguiente_a_quien: O(nlogn). no sé bien por qué. se que recorro n charlas, y a la primera que empieza despues, la agrego y listo. no recorro n² con cada charla.
Espacial: O(n)
A lo sumo voy a tener N elementos guardados.
"""