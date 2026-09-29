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

    # creo la tabla, con cant + 1 filas y
    # W+1 columnas (base 1, para no estar haciendo el i-1 constante + tener el W = 0. columna = 0, capacidad cero. fila 0 = ningun elemento)
    TABLA_VALORES = [[0] * (W + 1) for _ in range(cant + 1)]

    for i in range(1, cant + 1):
        #el elemento real es i-1, por el corrimiento que meti en la TABLA_VALORES
        valor = elementos[i -1][0]
        peso = elementos[i-1][1]

        for w in range(1, W + 1):
            if peso <= w:
                # aplico ec. recurrencia. o lo llevo o no
                venite_crack = valor + TABLA_VALORES[i-1][w-peso]

                vos_no = TABLA_VALORES[i-1][w]

                TABLA_VALORES[i][w] = max(venite_crack, vos_no)
            else:
                # si no entra heredo el optimo anterior
                TABLA_VALORES[i][w] = TABLA_VALORES[i-1][w]
    
    
    return _reconstruccion(TABLA_VALORES, elementos, W)


def _reconstruccion(TABLA_VALORES, elementos, W):
    ELEMENTOS_USADOS = []
    i = len(elementos)
    w = W

    #voy para atras desde la esquina inferior derecha
    while i > 0 and w > 0:
        # si es distinto al anterior, significa que lo usé
        if TABLA_VALORES[i][w] != TABLA_VALORES[i-1][w]:
            elemento_goat = elementos[i-1]
            ELEMENTOS_USADOS.append(elemento_goat)
            w -= elemento_goat[1] # le saco el peso
        i -= 1 # voy para el anterior

    
    return ELEMENTOS_USADOS[::-1] # hace falta invertirlo? cronologicamente devuelvo? rpl what do u want


"""
Justificación de la complejidad:
- temporal: O(n.W), siendo n la cantidad de elementos en la mochila y W la capacidad.
 ya que itero todos los elementos por cada opcion de capacidad hasta llegar a W
llenar la tabla cuesta O(n.W)
la reconstruccion tambien.

algoritmo pseudopolinomial. depende totalmente de W. y del pasaje a bits que tanto influye? ya con decir que depende de un valor numerico alcanza, o no?

- espacial: O(n.W), porque como mucho la TABLA_VALORES va a llenarse con n filas y W columnas.
se puede optimizar? como el ej del celular que solo miro el anterior, este sería igual (pero con 2?)

"""