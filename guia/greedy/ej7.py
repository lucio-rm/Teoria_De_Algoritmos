"""
Enunciado ejercicio 7:
(★★) Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. 
Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación y los precios aumentan todo el tiempo. 
El precio del producto 'i' el día 'j' es R[i]^(j+1) (j comenzando en 0). 
Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. 

Indicar y justificar la complejidad del algoritmo implementado. 

¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. 
¿Por qué se trata de un algoritmo Greedy? Justificar 
¿Qué modificaciones se deben realizar para un estado de deflación, con productos que bajan de precio todo el tiempo?

"""


"""
Ejemplo para un niño de 5 años (ELI5):
Imagina que los juguetes de una tienda se vuelven mágicamente más caros cada día 
que pasa. Si quieres comprar un robot gigante carísimo y una pelota barata, 
compras el robot hoy mismo antes de que su precio explote hasta las nubes, y 
dejas la pelota para mañana, porque su aumento no dolerá tanto.
"""

def precio_min(R):
    # Validamos entradas vacías
    if not R:
        return 0
        
    # Ordenamos de mayor a menor (Regla Greedy)
    R.sort(reverse=True)
    
    costo_total = 0
    # Utilizamos enumerate para tener el día (índice j) y el precio base a la vez
    for j, precio_base in enumerate(R):
        # El día 'j' comienza en 0. El costo es precio_base^(j+1)
        costo_dia = precio_base ** (j + 1)
        costo_total += costo_dia
        
    return costo_total

"""
Justificación Greedy y Complejidad (Ej 7):

- Complejidad: O(n log n) por el ordenamiento del arreglo inicial. El ciclo 
  for itera 'n' veces con operaciones O(1). Complejidad final: O(n log n).
  
- Regla Greedy: En cada iteración (día 'j'), seleccionamos el producto con el 
  precio base más alto disponible en el arreglo.
  
- ¿Es siempre óptimo?: Sí. Se demuestra mediante el Argumento de Intercambio 
  (Exchange Argument). Si intercambiamos el orden de compra de un producto caro 
  (A) y uno barato (B), obligando a A a ser comprado un día después, el 
  crecimiento exponencial de A será mucho mayor que el ahorro logrado al comprar 
  B un día antes.
  
- Modificación para deflación: Si los precios caen constantemente (deflación), 
  queremos que los productos más caros caigan durante más tiempo para ahorrar 
  más dinero. La regla se invierte: ordenamos de menor a mayor (`R.sort()`), 
  comprando lo más barato primero y lo más caro al final.
"""