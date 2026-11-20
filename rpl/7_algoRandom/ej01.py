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
import random

def estimar_pi(iteraciones):
    return 0
