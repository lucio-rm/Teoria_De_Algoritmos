"""
Enunciado 1. 
Manejamos un negocio que atiende clientes en Atenas y en Roma. Nos interesa cada mes decidir si operar en una u otra ciudad.
Los costos de operación para cada mes pueden variar y son dados por 2 arreglos: A y R, con valores para todos los meses hasta n.
Naturalmente, si en un mes operamos en una ciudad, y al siguiente en una distinta, habrá un costo fijo C por la mudanza. 
Dados los arreglos de costos de operación en Atenas (A) y Roma (R), implementar un modelo de *programación lineal* que determine qué
meses se operará desde Atenas, y en cuáles desde Roma, de forma de minimizar el costo total. 

Indicar la cantidad de inecuaciones.

"""

"""
planteo:

1. Constantes y datos:
- R arreglo con los costos de operaciones hechas en Roma   (n meses)
- A arreglo con los costos de operaciones hechas en Atenas (n meses)
- C costo de mudanza
~ minimizar el costo total


2. Variables:
- X_{i}: variable binaria 0/1, i ∈ [0, n]
vale 1 si opero en Roma en el mes i, 0 si no
- Y_{i}: variable binaria 0/1, i ∈ [0, n]
vale 1 si opero en Atenas en el mes i, 0 si no

(
pienso:
. tengo que tener una variable tipo costo para minimizar, sino cómo minimizo?
. cómo indico/veo cuando cambia de ciudad, y le digo "agrega C"

)
- H_{i}: variable binaria entera, i ∈ N_{0}
vale 1 si hubo mudanza en el mes {i}, 0 en caso contrario



3. Función Objetivo:
Minimizar el costo total
     n
min  ∑ (X_{i}.R_{i} + Y_{i}.A_{i} + H_{i}.C)
    i=0


4. Restricciones:
Si o si para un día 'i', tengo que trabajar en Roma *o* en Atenas
    ∀ i ∈ [0, n] ,   X_{i} + Y_{i} = 1 


Mudanza. si en el mes i estoy en Roma y despues me voy, mudanza = 1.

∀i ∈ [0, n-1]
    X_{i} + Y_{i+1} - 1 ≤ H_{i}  
    Y_{i} + X_{i+1} - 1 ≤ H_{i}  
.

total de inecuaciones: 3


"""