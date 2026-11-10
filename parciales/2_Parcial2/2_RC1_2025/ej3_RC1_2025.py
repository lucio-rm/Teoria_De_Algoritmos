"""
Enunciado 3. 
El problema conocido como Feedback Vertex Set (FVS) indica: 
Dado un grafo (dirigido, o no) y un número entero k, ¿existe un subset de vértices del grafo de tamaño a lo sumo k, tal que si eliminamos dichos vértices del grafo, este queda acíclico?

Demostrar que FVS es un problema NP-Completo. 
Para esto, recomendamos recordar que el problema de Vertex Cover es un problema NP-Completo. 
También, recomendamos recordar cómo fue que demostramos en clase que Dominating Set es un problema NP-Completo, también a través de Vertex Cover.

"""

"""
planteo:

-1. Leer el enunciado

0. Plantear el problema como versión de decisión
    . version de decision -----(T/F)------> QUEREMOS ESTA
    . version de optimización -------> exponencial

A LO SUMO
AL MENOS
. k, v

1. Desmotrar que el problema está en NP.
Un problema pertenece a NP, cuando dada una solución propuesta (certificado), podes validar su correctitud en tiempo polinomial (certificador).

SOLUCION ----------> VALIDAR --------> TRUE/FALSE
                    polinomialmente


                    
                    
                    CODEAR (Y)
                    0. que te pide el problema
                    1. que es la solucion
                    2. def problema(grafo, valor, k, solucion)
                        return TrueFalse
                    3. filtros chequeos nashe
                        1. que los de la solucion esten en el grafo
                        2. validarlo con el a lo sumo y el k
                        3. las propiedades del probelma
                    
                    
                    
2. Reducir un problema NP-Completo (conocido) a el problema del ej.

 X -----> Y
X ≤p Y

X es NP-Completo, conocido.



YO NO SE HACER X
SE HACER Y

X NO PUEDE SER MAS DIFICIL QUE HACER Y

Y ES AL MENOS TAN DIFICIL COMO X



---------- HACER UNA TRANSFORMACIÓN POLINOMIAL

Tengo una instancia de X que me da True <------> Tengo una instancia particular de Y que me da True



3. Demostrarlo
. Metodo Directo / por absurdo

IMPORTANTE: NO CHAMUYAR


ida y vuelta


ida: demostrar que si tengo instancia X true ----> Y true
vuelta: tengo instancia particular de Y True ----> X true

"""


