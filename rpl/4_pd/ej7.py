"""


Ej.7 (★★★):
Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. 
Implementar un algoritmo que, por programación dinámica, reciba los valores y pesos de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total. 
Indicar y justificar la complejidad del algoritmo implementado.

"""
"""
planteo:

maldito knapsack 0/1 problem. no se porq ue se le dice 0/1, creo que porque son numeros enteros

ec. recurrencia: (agarrarlo y restar el peso, o no agarrarlo y fijarme con todos los elemen. sin ese)
OPT(i, W) = max(v_i + OPT(i, W-W_i), OPT(i-1, W)) paratodo W_i <= W

maso menos mismo que el ej.6, matriz pero ahora con 2 incógnitas ninguna

W --- 0 - 1 - 2 - 3 - 4 - ... - W
elem
e_0 - - - V_0
e_1 - - - -
e_2 - - - -
e_3 - - - 
e_4 - - - 
e_5 - - - 

no sé, y así.

tengo que devolver los elementos que uso, asi que tengo uqe usar la reconstrucción.

reconstrucción:
tengo la
TABLA_VALORES
"""

# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    cant = len(elementos)
    if cant <= 0 or W == 0:
        return []

    # creo la tabla, con len(elementos) filas y W+1 columnas (base 1, para no estar haciendo el i-1 constante + tener el W = 0)
    TABLA_VALORES = [[0] * cant for _ in range(W + 1)]

    #lleno cuando W = 0 -> pa la ecuacion de recurrencia no me tire error
    for i in range(cant):
        TABLA_VALORES[i][0] = 0
        
    for i in range(1, W+1): #W incluido
        for e in range(cant):
            valor = elementos[e][0]
            peso = elementos[e][1]
#OPT(i, W) = max(v_i + OPT(i, W-W_i), OPT(i-1, W))
            if peso <= i:
                TABLA_VALORES[e][i] = max(valor + TABLA_VALORES[e-1, W-peso], TABLA_VALORES[e-1, W])
            else:
                TABLA_VALORES[e][i] = TABLA_VALORES[e-1][i] #le meto el OPT del anterior
    
    return _reconstruccion(TABLA_VALORES)


def _reconstruccion(TABLA_VALORES):
    ELEMENTOS_USADOS = []


    
    return ELEMENTOS_USADOS[::-1] # hace falta invertirlo?


"""
Justificación de la complejidad:
- temporal: O(n.W), siendo n la cantidad de elementos en la mochila y W la capacidad.
 ya que itero todos los elementos por cada opcion de capacidad hasta llegar a W

- espacial: O(n.W), porque como mucho la TABLA_VALORES va a llenarse con n filas y W columnas.
se puede optimizar?

"""