"""
Enunciado 1.
Se está formando una nueva comisión de actividades culturales de un pueblo. Cada habitante es miembro de 0 o más clubes, y de exactamente 1 partido político. 
Cada uno de los n clubes debe nombrar a un representante ante la nueva comisión de actividades culturales, con las siguientes restricciones: 
- cada partido político no puede tener más de n/2 simpatizantes en la comisión, y además queremos minimizar la cantidad simpatizantes a un mismo partido político; 
- cada persona puede representar a solo un club, cada club debe estar representado por un miembro.

Implementar un modelo de programación lineal que dada la información de los habitantes (a qué clubes son miembros, a qué partido pertenecen), nos permita obtener los representantes válidos, que además minimicen la cantidad de simpatizantes a un mismo
partido político. 

Indicar la cantidad de inecuaciones definidas en el modelo

"""

"""
planteo:


1. Constantes y Datos

- habitante -> miembro de ≥0 clubes y =1 partido político
- n clubes -> 1 representante
    . partido político ≤ (n/2) simpatizantes en la comision
    . minimizar cant. simpatizantes en un mismo partido político
    . cada persona puede representar a un club
    . cada club representado (must) por 1 miembro

C : clubes
H : habitantes
R : representantes
P : partido político
S : Simpatizantes

2. Variables

R_{i}{j} : variable binaria entera, i ∈ R, j ∈ C
Donde vale 1 si el representante i representa al club j, 0 si no.

H_{i}{j} : variable binaria entera, i ∈ H, j ∈ P
Donde vale 1 si el habitante es de el partido político j, 0 si no.

H_{i}{k} : variable entera, i ∈ H, k ∈ C
Donde va a terminar valiendo de cuántos k clubes el habitante i es miembro 



3. Función Objetivo

Objetivo: Minimizar la cantidad de simpatizantes a un mismo partido político.
    H
min ∑ H_{i}{k} , ∀ k ∈ P
   i=0

(#nota: aca quiero hacer como un 2 for loops. por cada k, quiero minimizar la sumatoria de los H_{i}. esta bien asi como lo puse?)

4. Restricciones

A --- Si o si, por cada representante, tiene que representar a 1 solo club.
         C
∀ i ∈ R, ∑ R_{i}{j} = 1
        j=0

B --- Por cada habitante, entre todos los partidos políticos tiene que ser de 1 solo.
         P
∀ i ∈ H, ∑ H_{i}{j} = 1
        j=0

C --- Por cada habitante, puede ser miembro de 0 o más clubes.
         C
∀ i ∈ H, ∑ H_{i}{k} ≥ 0
        k=0

D --- La cantidad de simpatizantes por cada partido político no puede ser más de (n/2) (n es la cantidad de clubes, que lo represento con la constante C)
        H
∀ j ∈ P ∑ H_{i}{j} ≤ C/2
       i=0

---
Total de inecuaciones: 
A = 1
B = 1
C = C inecuaciones
D = H inecuaciones

Total = 2 + C + H => C + H inecuaciones.

"""