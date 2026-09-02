"""
Enunciado 15:
Se tiene una colección de n libros con diferentes espesores, que pueden estar entre 1 y n (valores no necesariamente enteros). Tu objetivo es guardar esos libros en la menor cantidad de cajas. Todas las cajas disponibles son de la misma capacidad L (se asegura que L >= n). Obviamente, no podés partir un libro para que vaya en múltiples cajas, pero sí podés poner múltiples libros en una misma caja, siempre y cuando los espesores no superen esa capacidad L. Implementar un algoritmo Greedy que obtenga las cajas, tal que se minimicen la cantidad de cajas a utilizar. Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. ¿El algoritmo propuesto encuentra siempre la solución óptima? Justificar.
¿Qué cambios aplicarías si supieras que los espesores sólo fueran números enteros? Describir cómo afecta a la complejidad,y a su optimalidad.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""


def cajas(capacidad, libros):
    return []