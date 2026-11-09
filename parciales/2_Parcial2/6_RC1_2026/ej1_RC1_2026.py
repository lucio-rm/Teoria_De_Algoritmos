"""
Enunciado 1. 
El problema de Bin-Packing es el siguiente: dados n elementos de diferentes pesos pi se quiere ubicar a cada elemento en algún contenedor, donde cada contenedor tiene capacidad máxima M (todos los contenedores tienen la misma capacidad). 
Suponer que todos los pi son menores o iguales a M .

Implementar un modelo de *programación lineal* que permita determinar en qué contenedor va cada elemento, de forma de minimizar la cantidad de contenedores utilizados. 
Considerar que, como máximo, vas a usar n contenedores (es imposible tener que usar más).
Indicar la cantidad de inecuaciones definidas.

"""

"""
planteo:

1. Constantes, Datos y Variables
- n elementos, c/u pesos p_{i} distintos (c/p_{i} <= M)
- contenedores, c/u con cap. máx. M (misma cap.)

objetivo: minimizar la cantidad de contenedores a usar.


- X_{i}: variable entera, i ∈ [0, n-1]
∀ X, X = 1. representa cada elemento que tengo que poner en los contenedores.

- C_{j}: variable binaria entera, j ∈ N⁺
representa el contenedor. 1 si fue creado, 0 si no.

2. Restricciones
∀ i ∈ [0, n-1] , X_{i} = 1
n-1
 ∑ X_{i} . p_{i} ≤ ∑ C_{j} . M , ∀ j ∈ N⁺
i=0               

La idea de esta restricción, es que si o si tengo que poner todos los elementos con sus respectivos pesos en contenedores. Entonces C/elemento vale 1 porque lo elijo.
X_{i} no va a tener restricción alguna, todos van a valer 1.

Pero, con respecto a los contenedores, yo no se cuántos voy a utilizar, por lo que depende del valor de la capacidad máxima M.
Si uso un contenedor j, va a tener peso M.
si uso 2, va a ser C_0 . M + C_1 . M = 1.M + 1.M = 2M
2 contenedores, van a tener capacidad 2M. si con eso no ocupo la sumatoria de pesos a cubrir, voy a tener que utilizar más contenedores. Busco minimizar la cantidad de contenedores a utilizar.

total de inecuaciones: A lo sumo, voy a necesitar N inecuaciones. que van a representar el peor caso posible, de tener que usar N contenedores. (tener que cubrir el peso de los elementos con N.M peso.)
(#nota: no sería 1 inecuación?, porque sería la sumatoriad e todos los elementos con su peso menor igual a la cantidad de contenedores a usar. Todo en una línea. Cómo lo representaría PL?)

3. Función Objetivo

Como se ha dicho anteriormente, minimizar la cantidad de contenedores a utilizar.

min ∑ C_{j}, ∀ j ∈ N⁺

"""




"""
Leí slack:

1. Constantes:
- p_i = peso del elemento i
- M = cap. maxima de un bin
- N = cantidad de elementos

2. Variables:
- Y_{i}{j} variable tipo binaria, representa si el elemento i pertenece a la bolsa j
- X_{j} variable tipo binaria, representa si la bolsa j se usa.

3. Funcion objetivo:
    N
min ∑ X_{j}
   j=1
minimiza la cantidad de bolsas que se usan.

4. Restricciones:
1)
garantiza que cada elemento i este en un único bin
    N
    ∑ Y_{i}{j} = 1 , ∀i  
   j=1

2)
si el bin j se toma, la suma de posibles elementos debe ser ≤ M
si el bin j no se toma, la suma de elementos debe ser 0.
    N
    ∑ p_{i} . Y_{i}{j} ≤ M. X_{j} ∀j
   i=1


3)
No más de un bin por elemento
    N
    ∑ X_{j} ≤ N
   j=1



cantidad de restricciones: 2N + 1
"""