"""
Enunciado 07:
Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación y los precios aumentan todo el tiempo. El precio del producto i el día j es R[i]^{j + 1} (j comenzando en 0). Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción


"""

def precios_inflacion(R):
    # valido entradas vacías
    if not R:
        return 0
        
    # ordeno de mayor a menor (Regla Greedy)
    R.sort(reverse=True)
    
    costo_total = 0
    # uso enumerate para tener el día (índice j) y el precio base a la vez
    for j, precio_base in enumerate(R):
        # el día 'j' comienza en 0. El costo es precio_base^(j+1)
        costo_dia = precio_base ** (j + 1)
        costo_total += costo_dia
        
    return costo_total

"""
Justificación Greedy y Complejidad:

- Complejidad: O(n log n) por el ordenamiento del arreglo inicial. El ciclo 
  for itera 'n' veces con operaciones O(1). Complejidad final: O(n log n).
  
- Regla Greedy: En cada iteración (día 'j'), seleccionamos el producto con el 
  precio base más alto disponible en el arreglo.
  
- ¿Es siempre óptimo?: Sí. Se demuestra mediante el Argumento de Intercambio 
  (Exchange Argument). Si intercambiamos el orden de compra de un producto caro 
  (A) y uno barato (B), obligando a A a ser comprado un día después, el 
  crecimiento exponencial de A será mucho mayor que el ahorro logrado al comprar 
  B un día antes.
  
"""