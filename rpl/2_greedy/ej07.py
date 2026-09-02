"""
Enunciado 07:
Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación y los precios aumentan todo el tiempo. El precio del producto i el día j es R[i]^{j + 1} (j comenzando en 0). Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción


"""

def precios_inflacion(R):
    return 0