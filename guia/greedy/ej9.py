"""
Enunciado ejercicio 9:
(★★) Tenemos tareas con una duración y un deadline (fecha límite), pero pueden hacerse en cualquier momento, intentando que se hagan antes del deadline. Una tarea puede completarse luego de su deadline, pero ello tendra una penalización de latencia. Para este problema, buscamos minimizar la latencia máxima en el que las tareas se ejecuten. 
Es decir, dados los arreglos de: T tiempo de duraciones de las tareas y L representando al deadline de cada tarea, si definimos que una tarea 'i' empieza en 'Si', entonces termina en 'Fi = Si + Ti', y su latencia es 'Li = Fi - Di' (si Fi>Di, sino 0).
Nuestra latencia máxima será aquella 'i' que maximice el valor Li. 

Implementar un algoritmo que defina en qué orden deben realizarse las tareas, sabiendo que al terminar una tarea se puede empezar la siguiente. Indicar y justificar la complejidad del algoritmo implementado.

Devolver un arreglo de tuplas, una tupla por tarea, en el orden en que deben ser realizadas, y que cada tupla indique: (el tiempo 'Ti' de la tarea 'i', y la latencia resultante Li de esa tarea).

¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. 
¿Por qué se trata de un algoritmo Greedy? Justificar
"""

"""
planteo:
Lo haces SOLo en base al deadline, haces el que primer deadline tenga.
es optimo.
comprobas que el tiempo de tarea maxima va a ser siempre el mismo si mantenes ese requisito del deadline.



Earliest Deadline First (EDF)

Ejemplo para un niño de 5 años (ELI5):
Si tu mamá te da tareas: limpiar tu cuarto (vence hoy), hacer la tarea de mates 
(vence mañana) y bañar al perro (vence el domingo). Empiezas por la que se vence 
hoy para que el regaño (la latencia) no sea tan grande si te retrasas. Ignoras 
cuánto tardas en cada cosa, solo miras cuándo debes entregarlo.
"""


def minimizar_latencia(T, L):
    # Empaquetamos las tareas en tuplas: (duracion, deadline, id_original)
    tareas = []
    for i in range(len(T)):
        tareas.append((T[i], L[i], i))
        
    # Regla Greedy: Ordenar ascendente por deadline (índice 1 de la tupla)
    tareas.sort(key=lambda x: x[1])
    
    tiempo_actual = 0
    latencia_maxima = 0
    resultado = []
    
    for tarea in tareas:
        duracion, deadline, id_tarea = tarea
        
        # El tiempo de finalización (Fi) es el tiempo en el que empezamos + duracion
        tiempo_actual += duracion 
        
        # Calculamos latencia Li = Fi - Di
        latencia = tiempo_actual - deadline
        if latencia < 0:
            latencia = 0 # No hay latencia negativa si terminamos antes
            
        resultado.append((duracion, latencia))
        
        # Guardamos la peor latencia encontrada
        if latencia > latencia_maxima:
            latencia_maxima = latencia
            
    return resultado, latencia_maxima

"""
Justificación Greedy y Complejidad (Ej 9):

- Complejidad: O(n log n). Empaquetar tuplas cuesta O(n). El ordenamiento por el 
  deadline es la operación dominante con O(n log n). El cálculo de tiempos en el 
  ciclo for cuesta O(n). 
  
- Regla Greedy: Ordenar todas las tareas según su deadline (fecha límite) de 
  menor a mayor y ejecutarlas estrictamente en ese orden.
  
- ¿Es siempre óptimo?: SÍ. Está demostrado por el argumento de Inversiones 
  Cualquier schedule que contenga "inversiones" (una tarea con un 
  deadline tardío programada antes que una con un deadline temprano) puede ser 
  revertido intercambiando las tareas contiguas. Al realizar este intercambio, 
  la latencia máxima de ambas tareas jamás empeora. Por inducción, el 
  arreglo completamente ordenado por deadline jamás empeora la latencia máxima, 
  garantizando el óptimo global.
"""