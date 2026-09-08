"""
Enunciado 09:
Tenemos tareas con una duración y un deadline (fecha límite), pero pueden hacerse en cualquier momento, intentando que se hagan antes del deadline. Una tarea puede completarse luego de su deadline, pero ello tendra una penalización de latencia. Para este problema, buscamos minimizar la latencia máxima en el que las tareas se ejecuten. Es decir, dados los arreglos de: T tiempo de duraciones de las tareas y L representando al deadline de cada tarea, si definimos que una tarea i empieza en S_i, entonces termina en F_i = S_i + T_i, y su latencia es L_i = F_i - D_i (si F_i > D_i, sino 0).
Nuestra latencia máxima será aquella i que maximice el valor L_i.
Implementar un algoritmo que defina en qué orden deben realizarse las tareas, sabiendo que al terminar una tarea se puede empezar la siguiente. Indicar y justificar la complejidad del algoritmo implementado.

Devolver un arreglo de tuplas, una tupla por tarea, en el orden en que deben ser realizadas, y que cada tupla indique: (el tiempo de la tarea i T_tareas[i] y la latencia resultante L_i de esa tarea).

¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""




"""
planteo:
Lo haces SOLo en base al deadline, haces el que primer deadline tenga.
es optimo.
comprobas que el tiempo de tarea maxima va a ser siempre el mismo si mantenes ese requisito del deadline.

Earliest Deadline First (EDF) (greetings mr Kleinberg and mrs Tardos)
"""

def minimizar_latencia(L_deadline, T_tareas):
    # L_deadline: lista con los deadlines de cada tarea
    # T_tareas: lista con las duraciones (tiempos) de cada tarea
    
    # Empaquetamos las tareas para poder ordenarlas por su deadline
    tareas = []
    for i in range(len(T_tareas)):
        duracion = T_tareas[i]
        deadline = L_deadline[i]
        tareas.append((duracion, deadline))
        
    # ordeno de menor a mayor por deadline (x[1])
    tareas_ordenadas = sorted(tareas, key=lambda x: x[1])
    
    tiempo_actual = 0
    resultado = []
    
    for tarea in tareas_ordenadas:
        duracion, deadline = tarea
        
        # el tiempo de finalización (Fi) de la tarea actual
        tiempo_actual += duracion
        
        # latencia individual de la tarea: Li = Fi - Di
        latencia = tiempo_actual - deadline
        
        # si la latencia da negativa (terminó antes del deadline), se considera 0
        if latencia < 0:
            latencia = 0
            
        # agregamos al resultado con el formato exacto de RPL: (duracion, latencia)
        resultado.append((duracion, latencia))
        
    return resultado


"""
Justificación Greedy y Complejidad :

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