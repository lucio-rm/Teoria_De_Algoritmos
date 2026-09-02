"""
Enunciado ejercicio 6:
(★) Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar “cambio” de una determinada cantidad de plata. 
Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes. El algoritmo recibirá un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y debe devolver qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizda. 
Indicar y justificar la complejidad del algoritmo implementado. 
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar si es óptimo, o dar un contraejemplo. 
¿Por qué se trata de un algoritmo Greedy? Justificar

"""

"""
planteo:
- Ordenar las monedas de mayor a menor.
- Iterar sobre las monedas: si la moneda es menor o igual al cambio restante, 
  uso la división entera para saber CUÁNTAS de esa moneda puedo usar de golpe.
- Actualizo el cambio restante usando el módulo.
- Repito hasta que el cambio sea 0.
"""

def dar_cambio(monedas, cambio_objetivo):
    # Ordenar monedas de mayor a menor O(m log m)
    monedas.sort(reverse=True)
    
    resultado = {}
    resto = cambio_objetivo
    
    for moneda in monedas:
        if resto == 0:
            break
        if moneda <= resto:
            cantidad = resto // moneda
            resultado[moneda] = cantidad
            resto = resto % moneda
            
    if resto > 0:
        return None # No se pudo dar el cambio exacto con este sistema
    return resultado

"""
Justificacion de complejidad:
- Si 'm' es la cantidad de denominaciones de monedas, ordenarlas cuesta O(m log m).
- Iterar sobre el arreglo cuesta O(m).
- Las operaciones matemáticas adentro son O(1).
- Complejidad final: O(m log m). Es independiente del número de plata 'cambio_objetivo'.
"""

"""
Justificación Greedy y ¿Encuentra siempre el óptimo?:
- Regla Greedy: Tomar la mayor cantidad posible de la moneda de mayor denominación 
  disponible que no supere el cambio restante.
- ¿Es ÓPTIMO? NO. El algoritmo Greedy solo garantiza el óptimo global en sistemas 
  monetarios "Canónicos" (como el sistema argentino o estadounidense), donde las 
  denominaciones están diseñadas para que el greedy funcione (ej: cada moneda 
  es al menos el doble de la anterior, o combinaciones amigables).
- CONTRAEJEMPLO (Fundamental para el examen):
  Sistema monetario: [1, 5, 6]
  Cambio objetivo: 10
  - El algoritmo Greedy elegirá: una de 6, y luego cuatro de 1. Total = 5 monedas.
  - La solución Óptima real es: dos de 5. Total = 2 monedas.
  Para sistemas no canónicos, el problema requiere Programación Dinámica (Dynamic Programming).
"""