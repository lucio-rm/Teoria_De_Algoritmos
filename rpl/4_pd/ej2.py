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
"""
def scheduling(charlas):
    charlas.sorted(lambda x: x[0])
    dicc_p = _siguiente_a_quien(charlas)
    return []

def _siguiente_a_quien(charlas):
    dicc_p = []
    for c in charlas:
        c = 0
    return dicc_p