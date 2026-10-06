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

aproach:
mismo greedy. elijo por fin.
peeero, como es un horario fijo, de 24 horas. pero lo complicado está en entender la relacion de los que empiecan pm y terminan am, la teca esta en:
- hacer una linea de 48 horas.

(0)----(a.m)1-------------------(p.m)1---------------|(24)------(a.m)2--------------------(p.m)2---------------|(48)

entonces.
posibles escenarios: (E = empieza, T = termina)

1- E=a.m, T=a.m, E < T.
2- E=a.m, T=a.m, E > T. (da toda la vuelta, e.g:  4 A.M., 3 A.M.)
3- E=a.m, T=p.m

4- E=p.m, T=p.m, E < T
5- E=p.m, T=p.m, E > T
6- E=p.m, T=a.m

lo que yo propongo es asignarles valores nuevos. a cada charla, con respecto a la linea de 48hs. para saber si termina en 
(a.m)2 o (p.m)2
no tengo que ignorar que cuando dan la vuelta, aparecen de vuelta las otras.
ejemplo:
    (0)----(a.m)1-------------------(p.m)1---------------|(24)------(a.m)2--------------------(p.m)2---------------|(48)
(6pm, 6am) ->                               |----------------------------|                               |---------
(9pm, 4am) ->                                   |--------------------|                                        |----
(3am, 2pm) ->    |--------------|                                |----------------------------|
(1pm, 7pm) ->                |---------------|                                        |---------------------|


- elegir por inicio -> mal
- elegir por menor_colisiones -> mal
- elegir por fin ¿?





- que pasa si parto las clases? cuando pasan de las 24 horas? siguen siendo 1. pero con importancia de 2 (siguen con valor=1)
e.g:
(6pm, 6am) -> (6pm, 0am) && (0am, 6am)

- por duracion/colisiones?
(6pm, 6am) -> 12hs, 3 colisiones
(9pm, 4am) -> 7hs, 2 colisiones
(3am, 2pm) -> 11hs, 3 colisiones
(1pm, 7pm) -> 6hs, 2 colisiones

oh que casualidad, las de menor duracion y colisiones terminan siendo las favoritas.

- contraejemplo?


"""