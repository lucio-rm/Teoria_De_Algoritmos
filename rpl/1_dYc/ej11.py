"""
Enunciado 11:
Implementar una función (que utilice división y conquista) de complejidad O(n) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de dos tercios de las veces. Justificar la complejidad de la solución.

Aclaración: Este ejercicio puede resolverse, casi trivialmente, utilizando una tabla de hash. Para hacer interesante el ejercicio, resolver puramente por división y conquista.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(n)". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""
"""
planteo:
divido en 3
busco 3
3 llamados recursivos
o(n) ¿?

"""
def mas_de_dos_tercios(arr):
    return False