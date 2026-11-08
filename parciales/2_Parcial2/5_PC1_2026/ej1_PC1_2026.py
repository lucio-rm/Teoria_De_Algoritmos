"""
Enunciado 1. 
El problema de Hitting Set Relajado es el mismo problema que Hitting Set, pero en el cual se permite que hayan hasta K conjuntos que no hayan sido “hitteados” (es decir, que ninguno de sus elementos sea parte del Hitting Set). 

Implementar un modelo de programación lineal que permita obtener un Hitting Set Relajado de tamaño mínimo (el valor de K pueden asumir que está definido en algún lado como una constante). 
Indicar la cantidad de inecuaciones definidas

"""

"""
planteo:

1. Constantes y Variables
K : numero de K conjuntos que pueden no estar hitteados
U : conjunto de elementos universal
S : subconjuntos de elementos ∈ U ( que tengo que hittear 1 elemento por cada uno )

X_{i} : Variable entera binaria, i ∈ U. 
Representa 1 si hitteo al elemento y lo agrego al Hitting Set, 0 si no.

S_{i} : Variable binaria entera, i ∈ {0, 1, 2, ..., len(S))
Representa 1 si el subconjunto de elementos fue hitteado, 0 si no.
2. Restricciones
--- ∀i ∈ U,     ∑ X_{i} ≥ len(S) - K
por cada elemento: voy a terminar eligiendo, como mínimo, len(S)-K elementos. (siempre que se pueda)
U inecuaciones

--- ∀i ∈ S,     ∑ S_{i} ≥ len(S) - K
La cantidad de Subconjuntos cubiertos, tienen que ser sí o sí len(S)-K

Inecuaciones totales: (U + S) # es lo mejor ¿?

3. Funcion Objetivo
    U
min ∑ X_{i} 
   i=0
Tengo que minimizar la cantidad de elementos hitteados.

"""