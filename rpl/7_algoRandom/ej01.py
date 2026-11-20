"""
Enunciado:
Implementar un algoritmo randomizado que permita estimar el valor de π (pi).
Para esto, recomendamos recordar que el área de un cuadrado de lado 2 es 4, mientras que
el área de un círculo de diámetro 2 es, casualmente, π.

El algoritmo recibirá la cantidad de iteraciones a utilizar para aproximar, y se espera que a más iteraciones, se aproxime mejor.

Si el algoritmo no se trata de un algoritmo aleatorizado (de verdad), se penalizará fuertemente.

"""

"""
planteo TEORÍA:
quiero hacerlo con Genetic Algorithms

Qué dice la clase de estos:

Genetic Algorithms
What if two solutions had babies? 
    SolucionA -- Solucion B
       /             \
    MejorSol_C1     MejorSol_C2

Aplicamos el algoritmo varias veces sin necesidad de usar información previa de base.
Los algoritmos genéticos tratan de usar la información obtenida en generaciones anteriores
---> Se basan en procesos evolutivos.


. Individuos:
Un estado posible de solución al problema. Iniciamos con 'p' individuos. Los individuos iniciales se pueden obtener al azar o con un procesamiento previo.

. Iteración:
Una generación. La iteración i+1 es descendiente de la iteración i.

--------------

Caracterización de un individuo (simplificado)

Un individuo va a tener:

- Cromosomas:
Expresan su naturaleza interna (vector con estado de solucón)
    . Este tiene genes, que representa a una variable del problema.
    . Los genes pueden tomar diferentes alelos (valores posibles, válidos)
Los individuos exitosos deberían poder llevar sus genes a las siguientes generaciones, y si tenemos un grupo de individuos con un patrón común exitoso, esto debería ser más probable.

- Éxito de un individuo:
Función de aptitud (fitness), que sería muy similar a lo que vimos de función objetivo en PL.

- Operadores genéticos (simplificado):
    . Selección
        Qué individuos sobreviven a una generación. Se eligen al x% más apto de según la función de aptitud.
    . Recombinación
        Generamos nueva generación en base a la selección
            .Opción 1 (más sencilla): Reproducción asexual 
                (individuo con mismos cromosomas -> misma instancia, digamos)
            .Opción 2: Reproducción sexual
                agarramos dos individuos, los llevas al boliche más turbio, y esperamos a que suceda lo inevitable. Se combinan los cromosomas (ej: se eligen genes al azar de cada uno, tal vez ponderando por cuál progenitor es más apto; también se puede hacer combinando al azar y los que no se eligieron forman otra instancia). Técnicamente... se podría hacer entre 3 o más. El emparejamiento puede ser al azar, puede preferirse los que tengan mayor aptitud, los que más con menos, etc.)
    . Mutación
        Modificación aleatoria de los genes de los individuos.
        Agarramos un valor umbral entre 0 y 1, y si se llega al valor umbral se modifica el valor (o ubicación) de un gen.

"""







"""
planteo TEORÍA MIT:


GENETIC ALGORITHMS.
~ Naive Evolution
~ mimicking ^
~ choices abound
~ fitness space
~ examples.

Attemps of naive reproduction.

Célula                          ---> CelulaNuc.2.1 (MITOSIS)
Núcleo (con dni de papi y mami) ---> Celulanuc.2.1

Consiguen los cromosomas de las células padres, y se van combinando un poco con los cromosomas de los abuelos también, y así.

Genetic Algorithms -> Nature -> Options of evolutive

ACTG.
Los cromosomas son binarios en el sistema que vamos a construir.

Va a haber una población ~~~> Aplicamos Mutation ~~~> hacemos el crossover, agarramos la parte delantera de uno, trasera de otro y creamos una nueva combinación.

Creamos una nueva población, cada uno tiene un Fitness (e.g, 88, 77, etc.) va a haber una función que el Fitness consigue una probabilidad de cuánto va a sobrevivir en la generación que sigue.
--> Selection, agarra con esa probabilidad de cada uno los que sobrevien

Y asi es el bucle de cada uno.

1 - P_{i} = f_{i} / ∑ f_{i}
                    i
la medición de la probabilidad.
(#nota: fitness no tiene negatividad).


~ muestra un ejemplo de aplicación de genetic algorithms,
f(x,y) = (sin co x)² (sin co y)² e^((x+y)/θ)
entonces, si van a la esquina es lo ideal.

Selection by fitness; no crossover --> problemas. no llegan al óptimo. (tests de 100 generations)
Selection by fitness; x-y crossover -> same problem

Cómo conseguir un mejor mecanismo para un mejor Fitness

-> Candidatos. 
Mecanismo2: Rank Space

P_{1} = P_{c}
P_{2} = (1-P_{c}).P_{c}
P_{n-1} = (1-p_{c})^(n-2) .P_{c}
P_{n} = (1-p_{c})^(n-1)

La probabilidad de "x" es la probabilidad de que no hayan elegido a ninguno de los anteriores antes que ese mismo. (tenes que multiplicarlo con la prob. de elegirlo 
(menos el último, porque no hay otro para elegir je))


~ ej:
Selection by fitness rank; x-y crossover
    . problema: se queda en un máximo local,  y no se fija en uno mejor.
    . solución: diversity
.


Mecanismo3: 

^ Diversity
|------------------X
|              (
|               (
|                (
|                  (
|   (  (  (   ( ( (
+-------------------|-->
                    Fitness
Qué individuo querrías quedarte?

Querés quedarte con los que



Selection by fitness and diversity rank; x-y crossover

La exposición deja explorando a todos.

Una vez alcanzado el máximo, cambias el selection method a fitness rank y listo.





--- El problema es que es naive nature.
Es horrible , es tonto. queremos una teoría real de la biología, pero nadie sabe un carajo. No tenemos mucha buena idea de cómo funciona, porque los cromosomas estan conectados a un contexto que nadie sabe bien cómo funciona.

El Genetic Algorithm, con esa "naive" idea, llega a lograr una buena solución.





 * Diversity Good
 * Ask where the credit lies
.


Practical Applications:

En qué tipo de problema, agarrar una mala parte con una buena, puede llevar a una mejor solución?

----



Podés sistematizar cierto tipos de reglas

IF X
   Y
IF L
   M
If {X' M} ---> then ~~~


Entonces aplicas cierto tipo de reglas reales en problemas aplicables, gratificando orecompensando lo bueno cuando "cumplen" las reglas, y creas cierto tipo de combinación.


----
Evolved Virtual Creatures. by Karl Sims.
----
"""



############################################################






"""
planteo:


Ahora en base a eso quiero resolver el ejercicio de rpl.


Datos:



"""


import random

def estimar_pi(iteraciones):
    return 0
