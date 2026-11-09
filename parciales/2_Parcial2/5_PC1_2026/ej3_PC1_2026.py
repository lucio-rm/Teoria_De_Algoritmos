"""
Enunciado 3. 
El problema del Subgrafo K-J Completo (SKJC) se define como: 
Dado un grafo y dos valores K y J, ¿existe un subgrafo dentro de dicho grafo, de *a lo sumo* K vértices donde todos los vértices se conecten con *al menos* J de los demás vértices del subgrafo?
Demostrar que el problema del Subgrafo K-J Completo es un problema NP-Completo. 
Recomendamos recordar que el problema de K-Clique es un problema NP-Completo. 

Leer atentamente en la definición del problema los “a lo sumo” y “al menos”.

"""

"""
planteo:


el ejercicio ya está en formato de decision.

tengo que tener SKJC

- GRAFO G
- subgrafo H de G con <= K vértices
- cada vértice de H tiene que tener >= J adyacentes (entre los v del subgrafo)



0. Definir el problema en su versión de Decisión
    . ya está hecho por suerte, solo devuelve True/False.
1. Demostrar que está en NP
    . hablar de qué es NP
    . hacer el validador
2. Reducir un problema NP-Completo a SKJC
    . ya nos dan la pista del K-Clique (esta facil)
    . hablo del K-Clique
    . Encuentro transformación / relación entre Y - X
3. Demuestro la correctitud
    . si y solo si
    . instancia de Y verdadera ↔ instancia construida de X es verdadera
"""

"""
0. ok

1. 
Un problema está en NP si, dada una solución (certificado) del problema, puedo verificar si es correcta en tiempo polinomial mediante un validador (certificador).


2. 
caracteristicas entre K-Clique y SKJC
el clique:
es un subgrafo COMPLETO de un grafo G
es una instancia del SKJC donde J == K
entonces yo sé que si encuentro un subgrafo completo de a lo sumo K vértices, un K-Clique, sé que voy a tener un SKJC de al menos J (siempre y cuando J <= K, pero si J > K no tiene sentido, sería absurdo.).


3. 



"""







