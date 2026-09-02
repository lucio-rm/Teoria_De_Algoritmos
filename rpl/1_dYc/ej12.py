"""
Enunciado 12:
Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es). Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional (obviando el utilizado por la recursividad y variables de tipos simples). ¿Cual es la complejidad del algoritmo?

Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). Luego, pensar a partir de allí el caso de 8 elementos, etc… para encontrar el patrón.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""

def alternar(arr):
    pass