"""
Enunciado 07b:
En Wakanda, tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero Wakanda está atravesando una era de deflación y los precios disminuyen todo el tiempo. El precio del producto i el día j+1 es exactamente la mitad del precio en el día j. El arreglo R[i] indica todos los precios del primer día. Si bien para reducir costos se debería esperar a que los productos sigan bajando, los tiempos de entrega no nos permiten esperar, y cada día debemos comprar uno de los productos.
Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""
"""
Modificación para deflación: Si los precios caen constantemente (deflación), 
queremos que los productos más caros caigan durante más tiempo para ahorrar 
más dinero. La regla se invierte: ordenamos de menor a mayor (R.sort()), 
comprando lo más barato primero y lo más caro al final.
"""
def precios_deflacion(R):
    if not R:
        return 0
        
    # ordeno de menor a mayor
    R.sort()
    
    costo_total = 0.0
    for j, precio_base in enumerate(R): # enumerate para tener el indice del dia y el precio
        # el precio se divide por 2 elevado al número de días transcurridos (j)
        costo_dia = precio_base / (2 ** j)
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