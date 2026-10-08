"""
Enunciado ejercicio 4:
Dado un arreglo de números positivos, donde cada elemento representa el máximo número de pasos que podemos dar desde esa posición, implementar un algoritmo que, utilizando programación dinámica determine la menor cantidad de saltos a realizar para llegar al final del arreglo (comenzamos en la posición 0). 
También escribir el algoritmo que permita reconstruir la solución.
Indicar y justificar la complejidad del algoritmo implementado.

Por ejemplo, si el arreglo es [2, 3, 1, 1, 4], la solución óptima es ir desde la posición 0 a la posición 1 (saltando 1 lugar, teniendo máximo 2 desde el inicio), y de allí a la posición 4 (saltando 3 lugares, que es el máximo desde dicha posición), logrando llegar al final en 2 saltos.
"""
"""
planteo:

arreglo  num >= 0

max numeros desde pos[i]

estoy en el final.

si veine del anterior
significa que anterior-1 = 1.

para llegar al final, pude haber usado cualquiera de los anteriores elementos. Siempre y cuando se pueda.
entonces?

OPT[i] = min()

okey. cociné.

OPT[i] = min ( 1 + OPT[n] ), ∀ OPT[n] sii (arr[n] >= i-n )
     n E [0, i-1]

esta perfecto.
soy un nashe.

Complejidad temporal como mucho un n², tener que recorrer todas las opciones. pero lo hago 1 vez y listo.
pa llenar la tabla.
"""
# pre condiciones: recibe un arreglo con la cantidad de pasos máximos que se pueden realizar.
# post condiciones: devuelve en qué posicion del arreglo utilizar los pasos
def pasos_min(arreglo):
    if not arreglo:
        return []
    n = len(arreglo)
    OPT = [float('inf')] * (n+1) #base 1. para saber que pos[0] es no poder.
    OPT[0] = 0
    OPT[1] = 0 #primer elem, 0 pasos para llegar a él.
    M_MINIMOS = [float('inf')] * (n-1) # siempre me voy a fijar al anterior. pos[n] me fijo pos[n-1] nunca llego a n.
    # en el peor de los casos, voy a tener n-1 opciones para elegir. (el último escalon)
    
    for i in range(2, n+1): #siempre en el 1er caso es quedarme parado. si len(arr) = 1. return [0]
        # y ahora aplico la ecuacion de recurrencia.
        escalon = i-1
        
        for j in range(0, escalon): # por cada escalon que puedo hacer hasta el mio.
            if arreglo[j] >= escalon - j: 
                # si o si su valor tiene que ser mayor o igual a la cant. de posiciones que faltan llegar hasta donde estoy.
                M_MINIMOS[j] = 1 + OPT[j+1]# 1 paso + cuanto tardé en llegar a ese. desfasaje.
            else:
                M_MINIMOS[j] = float('inf') #restauro el inf.
        OPT[i] = min(M_MINIMOS)

    return _reconstruccion(arreglo, OPT)

def _reconstruccion(arreglo, OPT):
    CUAL_USE = []
    n = len(arreglo)

    actual = n
    while actual > 0:
        # busco quien fue el j que nos permitio llegar a actual con OPT[actual]-1
        for j in range(actual):
            #tiene que ser un salto viable y ser el optimo anterior
            if arreglo[j] >= (actual-j) and OPT[j] == OPT[actual] -1:
                CUAL_USE.append(j)
                actual = j
                break
    return CUAL_USE[::-1] # cuál use, en orden cronologico de 0 a n.


"""
justificacion de la complejidad:

- temporal: O(n²) siendo n la cantidad de elementos en el arreglo
por cada iteracion de los n elementos del arreglo, para llenar la tabla de OPTIMOS, recorro su cantidad (elementos-1) por cada iteracion además de la anterior. Tiene una cota superior de O(n²)

- espacial: O(n). siendo el espacio extra utilizado de n elementos (n+1 para ser específico) en la tabla y en la reconstrucción, en el peor de los casos, n elementos. 'M_MINIMOS' nunca va a tener más de n elementos tampoco. 
O(n) + O(n) + O(n) = O(3n) = O(n)

"""
