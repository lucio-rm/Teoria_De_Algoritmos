"""
Enunciado ejercicio 1:
Tenemos un grafo representado con una matriz de adyacencia A. Dicha matriz tiene únicamente unos y ceros (según si dos vértices son adyacentes, o no).
Implementar un algoritmo de *división y conquista* que, dada la matriz A y un valor k, devuelva la cantidad de caminos de longitud k que hay en el grafo correspondiente. 

Analizar y justificar detalladamente la complejidad del algoritmo implementado. Tener mucho cuidado al analizar la complejidad; es probable que no puedas aplicar el teorema maestro. 
En dicho caso, como parte del análisis de la complejidad, explicar por qué no es aplicable el teorema (nuevamente, es probable que no puedas aplicarlo).

Recomendamos recordar que:
- A^m [i] [j] nos dice la cantidad de caminos de longitud m que hay entre i y j.
- Que la multiplicación de matrices se puede considerar como una operación que consume O(n^(log2(7))), siendo n la dimensión de la matriz (cuadrada). Si bien este algoritmo es de división y conquista, no se pide ni es de interés que implementen nada al respecto de esto. Suponé que está disponible la función multiplicar_matrices(A, B).
"""
"""
planteo:

- matriz A y valor k
devolver la cantidad de caminos de longitud k



Este es un ejercicio igual al de las potencias.
yo tengo que usar dyc para resolver la cuestion de tener A^k, y cuento la cantidad de caminos recorriendo la matriz A[i][j].

"""
#funcion basura para orientarme, no importa cómo se comporta. solo sé que multiplica las dos matrices.
def multiplicar_matrices(A, B):
    return A*B

def cant_caminos(A, k):
    if not A or k <= 0:
        return 0 # no hay caminos
    
    MATRIZ_K = _calculo_dyc(A, k)

    contador = 0
    for i in range(0, len(MATRIZ_K[0])): #filas
        for j in range(0, len(MATRIZ_K)): #columnas
            if MATRIZ_K[i][j] == 1:
                #estan conectados, y longitud camino k
                contador += MATRIZ_K[i][j]

    return contador

def _calculo_dyc(A, k):
    if k == 0:
        return 1 # potencia de 0 es 1.
    """
    idea:
    en vez de calcular todas las ramas de A^k == A.A.A... k veces
    calculo A^(k//2), y despues hago multiplicar(A^(k//2), A^(k//2)) == A^k
    entonces solo me encargo de calcular una sola rama.
    
    # si es impar, meto otra multiplicacion de A y listo.   
    """
    mitad = k//2
    resultado = _calculo_dyc(A, mitad)
    nuevo = multiplicar_matrices(resultado, resultado)

    if k % 2 != 0:
        # si era impar, hago una mas
        nuevo = multiplicar_matrices(nuevo, A)

    return nuevo


"""
justificación de la complejidad:

------------ temporal: 
siendo n la cantidad de elementos en la matriz.
el calculo dyc, tiene una ecuación de recurrencia de T(n, k) = T(n, k/2) + O(n^(log2(7)))
el cual por cada llamado recursivo (1 solo), k se divide a la mitad, A queda igual, y k se divide a la mitad. Además, el costo de todo lo que no es recursivo es de O(n^(log2(7))) por la func. auxiliar de 'multiplicar_matrices'. que en el peor de casos se ejecuta 2 veces, por lo que queda el costo de O(n^(log2(7))).

Por eso mismo, no se puede utilizar el Teorema Maestro. Al estar pendiente de 2 variables, y solo 1 cambia de forma (se divide a la mitad), no se puede aplicar el TM en este caso.

(el costo de recorrer la matriz es O(i.j), siendo i cantidad de filas y j cantidad de columnas.)

------------ espacial: O(n), siendo n el espacio de CallStack. por cada llamado recursiva se reutiliza el espacio de la cantidad de elementos de la matriz. no se utiliza espacio adicional. k es una varibale constante, no afecta.
"""