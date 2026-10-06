"""
Enunciado ejercicio 2:
Analicemos la siguiente variante del problema de scheduling que vimos en clase. Tenemos un procesador que puede operar 24 horas al día, todos los días. 
Tenemos diferentes tareas, donde cada una tiene un horario de inicio y fin fijos. Si se decide realizar una determinada tarea, esta se realiza todos los días. Considerar que algunos trabajos pueden empezar antes de la medianoche y terminar luego de medianoche, y he aquí la diferencia con el problema de scheduling que vimos en clase.
Dada una lista de n tareas, implementar un algoritmo *greedy* que nos devuelva el listado de mayor cantidad de tareas que se puedan realizar, considerando que el procesador solo puede ejecutar una tarea en un determinado momento. 

Indicar y justificar la complejidad del algoritmo. Justificar por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar, si no dar un contraejemplo.

Por ejemplo, si tenemos las tareas definidas por los siguientes intervalos:
(6 P.M., 6 A.M.), (9 P.M., 4 A.M.), (3 A.M., 2 P.M.), (1 P.M., 7 P.M.)
La solución óptima sería elegir el trabajo de 
(9 P.M., 4 A.M.) y el de (1P.M., 7 P.M.).
"""

"""
planteo:



"""