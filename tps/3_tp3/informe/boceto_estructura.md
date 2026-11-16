## Ciclo de vida de un NP-Completo.

* demostrar que es dificil                 --> Reducciones
* resolverlo de forma optima (exponencial) --> BT y PLE
* sacrificar optimalidad por costo P       --> Aproximaciones y Greedy


## Decisión de cumplir propiedad
* tablero $n x m$ celdas
tengo que cumplir:
1. Cada fila tiene al menos una piedra.
2. Ninguna columna tiene piedras de ambos colores.

para saber qué piedras sacar en la columna j:
- o de la columna j me quedo solo con las piedras Verdes
-  ...          ...         ...   con las piedras Celestes
eso ayuda para no pensar en un *nxm*, sino en sólo *m* decisiones que hay que hacer.
una fila $i$ queda cubierta (¬vacia) si al menos una columna $j$ elige el mismo color que la piedra que está en la celda $(i, j)$.

# 8 puntos a cubrir:
## [ ] 1: ∈ NP.
Escribir pseudocodigo del validador + explicar lo de bla bla bla como pertenece a NP.
recibe tablero original y solucion propuesta + verificar en tiempo polinomial (O(NxM)) que las piedras que quedan son un subconjunto válido del original (que cumplan las 2 reglas). 
(MOSTRAR CODIGO + JUSTIFICAR COMPLEJIDAD)

## [ ] 2: Demostración  NP-Completo.
Reducir Pol. 3-SAT ≤ Juego de las Piedras (pasarlo a version de decisión)

Como cada columna elige entre V (True) o C (False) y cada fila necesita al menos un acierto, cada variable de 3-SAT es una columna y cada cláusula es una fila. 
. definir los problemas de decisión
. explicar transformación (∈ P) 
. ejemplo visual 
. demostrar el sii (idavuelta)
grafo con .tex ana ana anashe?
tikz

## [ ] 3: Algoritmo de Backtracking.
todo el arbol de decisiones (mostrar un grafico¿?) (aclarar 2^m hojas en fuerza bruta y todo lo que nos ayuda resolver por bt)
buscar minimizar las filas vacías, aplicar podas -> explicar eso je (esa rama no puede mejorar la mejor solucion del momento)
(#nota: hacer set de datos, despues lo vamos a usar tambien para PL)

## [ ] 4: Algoritmo de PL.
. modelar el problema con variables binarias (una por columna y una por fila para saber si quedo vacía)
. implementarlo en Python (PuLP) y comparar sus tiempos de ejecución contra el Backtracking
(#nota: pajovicvh mediciones (si VaLentin lee esto, usemos las dos compu man no reniegues vos solo))

## [ ] 5: Análisis del algoritmo del Gringo Hinz
. demostrar que elegir al azar (V o C con probabilidad $1/2$ en cada columna) devuelve siempre una solución válida en O(n.m)
. y calcular su cota de aproximación r(A).

## [ ] 6: Mediciones de r(A) y tiempos:
. comparar la sol_exacta contra la del Gringo Hinz en los sets (usemos catedra tambien ¿?)
. correr Hinz en tableros gigantes (infinitos para BT/PLE) para verificar la cota

## [ ] 7: Hacer un algoritmo Greedy de aproximación.
(#nota: hacer más de uno? uno solo? hacer uno con pd? ver clase de las opciones.)
. proponer implementar un algoritmo Greedy 
(ej. rapido:
 decidir columna por columna eligiendo el color que salve más filas que esten en la shit),
. analizar complejidad y compararlo contra Hinz.

## [ ] 8: Conclusiones.
nasheada final.







# secciones:
(#nota: ~ = section/subsection)
0~ Indice 
1~ Resumen
    - resumen de qué vamos a hacer + qué buscamos

2~ El problema
    .1~ Introduccion
        Consigna
    .2~ Planteo del problema + modelado
    .3~ Consecuencias de la optimalidad
        . qué es lo buscado
        . lo que se vaya a encontrar, se va a encontrar al final de todo
3~ Clases de Complejidad y Reducciones
    .1~ P NP NP-C y Reducciones
        . expliacion
        . famosa incógnita de P ? NP
    .2~ Demostración NP
        . explicacion
        . validador (coding shi)
        . justificacion complejidad
    .3~ Demostracion NP-Completitud
        . 3-SAT para el Game
4~ Búsqueda de la Exactitud: Backtracking y PLE
    .1~ Teoría Backtracking y Podas
    .2~ Diseño e Implementación del Backtracking
        . lógica, podas,
        . codigo 
        . analisis complejidad (temporal y espacial)
    .3~ Modelo de Programación Lineal Entera
        . concepto PL + PLC/PLE y por que el PLE
        . definicion variables + constantes/datos + funcion objetivo + restricciones y total de inecuaciones
5~ Aproximaciones
    .1~ Teoría
        . trade-off entre tiempo polinomial y optimalidad garantizada (elk r(A))
    .2~ Análisis del Algoritmo del Gringo Hinz
        . Demostración de validez, complejidad O(N.M)
        . demostracion matemática de la cota r(A)
    .3~ Propuesta de Aproximación Propia
        . el por qué greedy + diseño determinístico
        . pseudocodigo
        . justificacion de la complejidad
    .4~ Pensamiento Algorítmico en la Vida Real
        . Conexión entre los 4 temas (Herbert Simon y la Racionalidad Limitada)
            . saber cuándo podar un camino con Backtracking y cuándo preferir una aproximación a tiempo frente a la parálisis por análisis).
6~ Experimentos y Mediciones
    . el por qué
    .1~ Generacion de sets de datos
        . cómo se armaron los tableros de prueba (variando n, m, y densidad)
    .2~ Tiempos de ejecución
        . BT vs PL vs APROXIMACIONES
    .3~ Corroboración de la Cota r(A) y Calidad
        . Graficos comparando calidad del óptimo vs Gringo Hinz vs Greedy propio
7~ Conclusion
    . hablar en sí de lo visto en el TP
    . ventajas de XXX
    . peligros de XXX?
Bibliografía


