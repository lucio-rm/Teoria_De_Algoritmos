"""
Enunciado:
Implementar un algoritmo randomizado que permita estimar el valor de π (𝜋).
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
    . hacer un algoritmo randomizado que permita estimar el valor de π (𝜋).
    . Recomiendan recordar:
        . el área de un cuadrado de lado 2 es 4.
        . el área de un círculo de diámetro 2 es, casualmente, π.
    . va a recibir la cantidad de iteraciones a utilizar para aproximar
        . a más iteraciones, que aproxime mejor.
.

    1. Representación (Cromosoma e Individuo): Cómo codificás una solución candidata.
.
Número flotante, que empieza con un valor default 3.14 y sigue con un 3.14x en una iteración. en 2 iteraciones : 3.14xx, y asi.
la idea es que en cada iteración se quede sólo con los padres que acertaron, y crear hijos que ya empezaron correctamente.
el hijo ya va a ir por 3.141 si el padre acertó. se queda con la idea del número aagregado correctamente, los genes correctos.
si hay otro que quedó "cerca", con un 3.142, también va a tener hijos. depende esa del Fitness.
La idea es que cuanto más cerca estén del valor de 𝜋, es mejor. 

IDEA: + iteraciones ====> + generaciones ====> + cercano a 𝜋 va a ser.


    2. Función de Aptitud (Fitness): Una función objetivo que te dice "qué tan bueno" es un individuo.
.
f(num) = |num - 𝜋| ===> me da qué tan alejado de 𝜋 está. si quedó muy alejado ===> lo MATO. nashe.

    3. Selección: Te quedás con un porcentaje de los mejores individuos de la población actual para que sean padres 
(prime tip: usa heapq.nlargest o nsmallest para agarrar el top 30%, más un pequeño porcentaje de elitismo que pasa intacto para no perder la mejor solución histórica).
.
de ésto no tengo idea.
por iteración cuántas generaciones corro? cómo me doy cuenta que se "generan", si por cada iteracion i genero 100 generaciones, estoy rompiendo la complejidad temporal al carajovich, o no? al ser un numero fijo, no?

Qué selección uso ¿?, supongo que algo del fitness rank que habia dicho el del MIT.

y dependiendo de las generaciones cque cree, tambien se me va al carajo la complejidad espacial. o no?


    4. Cruce (Crossover / Recombinación): Agarrás dos padres seleccionados y mezclás sus genes para crear un hijo nuevo, esperando combinar buenas características de ambos (por ejemplo, elegir gen a gen al azar de ind1 o ind2).
.
de toda la población que creé, agarro los que mejor fitnes tuvieron, y creo hijos en parte a eso.
la idea es que tengan esos genes que funcionaron, asi para la próxima iteración siguen avanzando.

    5. Mutación: Con una probabilidad baja (PROB_MUTACION), alterás aleatoriamente un gen del hijo (por ejemplo, haciendo un swap de dos posiciones). Evita que la población se estanque en un máximo local y mantiene la diversidad.
.
Bueno, eso. aplico una probabilidad baja (de 0.2 quiero probar) para que de esos hijos ganadores ir alterandolos un poco en cómo van a seguir creciendo.

"""
"""
aproach 2:
no habia entendido nada.
reset.
------------------------
el algoritmo tiene que descubrir 𝜋 optimizando algo geométrico sin saber nunca cuánto vale 𝜋 .
.
Qué hay que optimizar? :
Un circulo de diametro 1 tiene un perimetro exacto de 2.𝜋.r = 2.𝜋.0.5 = 𝜋
Si meto K puntos adentro o sobre el borde de ese circulo uniendolos
--> el perimetro máximo posible que pueden alcanzar esos puntos cuando se acomodan perfecto es : 𝜋 (je)
.


1. Representación (individuo y Cromosoma):
Un solo pj va a ser una lista de K puntos (no se, ej: 60 ¿?) que viven en la circunferencia de radio r = 0.5
    -> tip(IA):
Para no usar cos/sen que usan radiantes y 𝜋: genero un vector cualquiera (x, y) ∈ [-1, 1] y normalizo a longitud 0.5
Algebra lineal : 
norma = raiz(x² + y²) ==> (0.5 . x , 0.5 . y)
                             /norma   /norma
. para que no se crucen las lineas, un individuo es una lista ordenada de esos K puntos recorriendo el círculo.


2. Fitness
fitness(individuo) es calcular el perímetro del polígono
. la suma de las distancias euclidianas entre el punto 0 y 1, 1 y 2, y cerrando el k-1 al 0.
    . idea:
    cuando los puntos estan amontonados o mal distribuidos, el perimetro va a dar chico.
    cuando los hijos hereden puntos mejor espaciados, el perimetro va  crecer acercandose a 𝜋 como máximo global.

"""


import random
import math

CANTIDAD_POBLACION = 30
CANTIDAD_VERTICES = 80 # a mas vertices , el poligono se puede pegar mas al circulo real
ELITISTA = 3
SELECCION = 10
PROB_MUTACION = 0.2
LONGITUD = 2 #radio 2 en el primer cuadrante -> el arco mide exactamente 𝜋
PC = 0.15  # prob. base del mejor individuo 

def normalizar(x, y):
    norma = math.hypot(x, y) # === sqrt(x**2 + y**2), I guess it's more clean?

    if norma == 0:
        return (LONGITUD, 0.0)

    return (LONGITUD * x / norma, LONGITUD * y / norma)


def crear_individuo():
    # la idea es generar la cantidad_vertices puntos sobre el circulo de radio 0.5
    puntos_internos = []
    # genreo cant_veritces - 2 puntoso internos en el 1er cuadrante
    
    for _ in range(CANTIDAD_VERTICES - 2):
        x = random.uniform(0.001, 1.0)
        y = random.uniform(0.001, 1.0)

        puntos_internos.append(normalizar(x, y))

    # le clavo los dos extremos del arco de radio 2: (0,2) arriba y (2,0) abajo
    individuo = [(0.0, 2.0)] + puntos_internos + [(2.0, 0.0)]
    individuo.sort(key=lambda punto: punto[0]) #ordeno por x asi no se cruza nada

    return individuo


def fitness(individuo):
    # con math.dist() se calcula la distancai euclidiana (esta bien eso¿?)
    perimetro_arco = 0.0

    for i in range(len(individuo) - 1):
        perimetro_arco += math.dist(individuo[i], individuo[i+1])

    return perimetro_arco

def crossover(padre1, padre2):
    # mezclar el adn de mami y papi
    # una combinacion convexa (un promedio ponderado con alpha ∈ [0, 1]) te da un punto intermedio en el segmento que los une
    hijo = [(0.0), (2.0)] # extremo izq
    # mezclo los puntos internos (del 1 al CANTIDAD_VERTICES - 2)
    alpha = random.uniform(0.3, 0.7)  # peso aleatorio cerca del punto medio (0.5)
    
    for i in range(1, len(padre1) - 1):
        x1, y1 = padre1[i]
        x2, y2 = padre2[i]

        # hago el cruce
        promedio_x = alpha * x1 + (1.0 - alpha) * x2
        promedio_y = alpha * y1 + (1.0 - alpha) * y2

        # y lo empujo de vuelta al borde del circulo de radio 2
        hijo.append(normalizar(promedio_x, promedio_y))

    hijo.append((2.0, 0.0)) #extremo derecho fijo

    hijo.sort(key=lambda punto: punto[0]) #garantiza que sigan ordenados por x
    return hijo

def mutar(individuo):
    # Mutación NO es "eliminar al padre si es malo" (eso ya lo hizo Selección al descartarlo).
    # Mutación es alterar levemente un gen de un HIJO nuevo para explorar nuevas posiciones:
    
    # del hijo recien creado, modificarlo in-place algun gen del hijo al azar
    # (es mover un poco un vertice para probar suerte)
    
    
    if random.random() < PROB_MUTACION:
        # TODO: Elegir un punto al azar del individuo, moverlo un poquito y re-normalizarlo a radio 0.5
        pass

def estimar_pi(iteraciones):
    poblacion = [crear_individuo() for _ in range(CANTIDAD_POBLACION)]
    generaciones = max(5, iteraciones // CANTIDAD_POBLACION) # esto es para que no se me vaya al pingo el timeLimit de rpl

    # precalculo los pesos una sola vez
    PESOS_RANK = [((1 - PC) ** i) * PC for i in range(CANTIDAD_POBLACION - 1)]
    PESOS_RANK.append((1 - PC) ** (CANTIDAD_POBLACION - 1))  
    # leer el RANK SELECTION de los apuntes del MIT.
    


    for _ in range(generaciones):
        # 1. evaluar y ordenar de mayor a menor fitness
        ordenados = sorted(poblacion, key=fitness, reverse=True)
        
        # 2. elitismo
        nueva_poblacion = [ind[:] for ind in ordenados[:ELITISTA]]
        padres = ordenados[:SELECCION]
        # el boliche VIP donde los mas facheros (los de mejor ranking) tienen mas chances de levantar
        p1, p2 = random.choices(ordenados, weights=PESOS_RANK, k=2)

        
        # 3. crossover y mutacion hasta llenar CANTIDAD_POBLACION
        while len(nueva_poblacion) < CANTIDAD_POBLACION:
            p1, p2 = random.choices(ordenados, weights=PESOS_RANK, k=2)
            # p1, p2 = random.sample(padres, 2)
            hijo = crossover(p1, p2)
            mutar(hijo)
            nueva_poblacion.append(hijo)
            
        poblacion = nueva_poblacion

    mejor_individuo = max(poblacion, key=fitness)
    return fitness(mejor_individuo)
