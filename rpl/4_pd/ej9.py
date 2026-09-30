"""

Ej.9 (★★★):
Tenemos un conjunto de números v1, v2, ⋯ ,vn, y queremos obtener un subconjunto de todos esos números tal que su suma sea igual o menor a un valor V, tratando de aproximarse lo más posible a V. 
Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores, y la suma objetivo V, y devuelva qué elementos deben ser utilizados para aproximar la suma lo más posible a V, sin pasarse. 
Indicar y justificar la complejidad del algoritmo implementado.


"""
"""
planteo:

devolver qué elementos == reconstruccion
99,9% de que lo toman en el parcial la reconstruccion


bueno, ec. recurrencia
tengo 2 opciones con un elemento. lo tomo o no lo tomo.

OPT(n) = max(V_n + OPT(n-1), OPT(n-1)). siempre y cuando el valor no me pase a V.

ya practicamos algo de este estilo.

OPT(0) = 0

okey, tengo que hacerlo de 2 variables, es parecido al knapsack

OPT(n, v) = max(OPT(n-1, v-V_n), OPT(n-1, v))

entonces tengo
V - 0 - 1 - 2 - 3 - 4 - 5 . . . V
n
elementos
blablabala

"""
def subset_sum(elementos, v):
    if not elementos or v <= 0:
        return []
    cant = len(elementos)
    # creo tabla de v+1 columnas y cant elementos + 1. asi sé que la primer fila es no usar ningun elemento. y tenerlo en base 1 me sirve para los indices
    M_TABLA = [[0] * (v+1) for _ in range(cant+1)]

    for i in range(1, cant+1):
        valor = elementos[i-1] #desfasaje
        for obj in range(1, v+1): #v  incluido
            if valor <= obj:
                M_TABLA[i][obj] = max(valor + M_TABLA[i-1][obj - valor], M_TABLA[i-1][obj])
            else:
                #voy al anterior
                M_TABLA[i][obj] = M_TABLA[i-1][obj]
    
    return _reconstruccion(M_TABLA, elementos, v)


def _reconstruccion(M_TABLA, elementos, v):
    ELEMENTOS_USADOS = []
    # aplicar la ec. de recurrencia inversa
    i = len(elementos)
    obj = M_TABLA[i][v] # el objetivo real alcanzado, puede ser que no sea igual a V.
    
    while i > 0 and obj > 0:
        # si lo usé significa que el anterior al de la esquina tiene otro obj
        valor = elementos[i-1]
        if valor <= obj and M_TABLA[i][obj] == (valor + M_TABLA[i-1][obj- valor]):
            ELEMENTOS_USADOS.append(valor)
            obj -= valor
        
        i -= 1 # voy al anterior, en cualquier caso.
    return ELEMENTOS_USADOS[::-1]



"""
Justificacion de la complejidad
mismo que los anteriores 382382 ejercicios.
"""