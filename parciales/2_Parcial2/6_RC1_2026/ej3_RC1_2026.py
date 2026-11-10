"""
Enunciado 3. 
El problema de La mochila con bolsillos se define como: 
Dado un valor V , un conjunto de n elementos con pesos p1, p2, ..., pn cada uno y valores v1, v2, ..., vn, una mochila con k diferentes compartimientos, donde en cada uno de estos compartimientos tiene capacidad para hasta Wj de peso (para j = 1, 2, ..., k), 
¿Es posible definir elementos para cada uno de los comportamientos (sin repetir elementos) tal que ningun compartimiento vea su capacidad sobrepasada, y que la suma total de valores de elementos guardados sea al menos V ?
Demostrar que el problema de La mochila con bolsillos es un problema NP-Completo.

"""

"""
planteo:


0. Problema en modo decisión.
Ya puesto en el enunciado. la suma total de valores de elementos guardados sea *al menos* V.
"""

"""
1. Pertenece a NP
Que pertenezca a NP significa que, dada una solucion comprometedora (certificado) del problema, puedo verificarla con un validador su correctitud en tiempo polinomial (certificador).

tengo que verificar:
. me dan:
    . un valor V
    . conjunto de n elementos (peso, valor)
    . k compartimientos (cada uno con capacidad de hasta W_{j})
    . una solución, que no repite elementos, tal que ningun compartimiento se sobrepase y que la suma total de elementos guardados sea al menos V.
La solucion va a ser representada con una lista de listas.
cada sublista va a representar cada contenedor. y adentro de esa sublista va a representar los elementos adentro del respectivo contenedor_{j}
"""

def validador(V, elementos, k, solucion, W):
    # check 1: que la solución no tenga contenedores o elementos de más
    if len(solucion) > len(k):
        return False
    total_elementos = sum((len(contenedor) for contenedor in solucion))
    if total_elementos != len(elementos) :
        return False
    
    # check 2: que todos los elementos de la solucion, existan en el conjunto original + que no sobrepasen el W_{j} del contenedor
    S_elementos = []
    indice = 0
    indice_desfazado = 1 # el j ∈ [1, ..., k]
    while indice < len(solucion):
        contenedor = solucion[indice]
        max_cap = W[indice_desfazado]
        
        cap = 0
        for elem in contenedor:
            if elem not in elementos:
                return False
            S_elementos.append(elem)
            cap += elem.valor
        
        if cap > max_cap:
            return False
        
        indice += 1
        indice_desfazado += 1
    
    # check 3: que no se repitan elementos
    #S_elementos = [elem for contenedor in solucion for elem in contenedor]
    no_repe = set(S_elementos)
    if len(S_elementos) != len(no_repe):
        return False

    # check 4: que la suma de los elementos de la solución sean al menos V.
    total = sum(S_elementos)
    if total < V:
        return False

    # si pasó todos los chequeos, esta todo ok. forma parte de la solución
    return True
"""
Complejidad del validador:
C: cantidad de contenedores
E: cantidad de elementos

recorro cada contenedor : O(C)
recorro cada elemento adentro de los contenedores: O(E)
sumo cada elemento de la solución: O(E)

complejidad total: O(C + E), manteniendo la polinomialidad.
"""



"""
2. NP-C ≤p Problem

Problema NP-Completo conocido a elegir: (claramente je) El Problema de la Mochila.

Para poder demostrar que el problema de la mochila con bolsillos es un problema NP-Completo, puedo reducir un problema conocido NP-Completo a éste mismo. Demostrando que el problema de la mochila con bolsillos (McB) termina siendo *al menos* tan dificil que el Problema de la Mochila.

Primero, tengo que hacer la reducción, fijarme la transformación (si es necesaria) polinomial que necesito para poder reducir un problema al otro.

El Knapsack problem 0/1 (KP), consiste en elegir los elementos que la suma maximice el valor, y que no sobrepase una capacidad W.

caracteristicas 
KP
. elementos (peso, valor)
. maximizar valor
. no sobrepasar capacidad W de la mochila

McB
. elementos (peso, valor)
. obtener una suma de valor ≥ V
. guardar los elementos en contenedores (total k), cada uno con una capacidad W_{j}



KP es una instancia particular del McB, del cual k = 1, con cap. W

"""




"""
3. Demostracion si y solo sí.

Tengo una instancia del KP <----> Tengo una instancia particular del McB

Por método directo, demuestro la reducción.

Tengo una instancia del Knapsack Problem 0/1, Sé que sin transformación necesaria, tengo una instancia del problema de la mochila con bolsillos. Del cual tiene 1 solo bolsillo, con capacidad W, y el valor V = valor obtenido óptimo en KP.

Asumiendo que tengo una instancia del KP, voy a tener una del McB. Si no lo tuviera, no tendría una solución válida del KP. Cualquier solución válida que no sobrepase el W del KP, va a cumplir con ese V obtenido al McB, de 1 solo bolsillo con Cap.W

Y la vuelta, asumo que tengo una instancia particular del McB, con 1 solo bolsillo, con cap. W, y sumando al menos un valor V.

Voy a tener una solución del KP, no va a ser tal vez la óptima, pero va a ser una instancia del Knapsack Problem. Si no lo tuviera, significa que no tengo tampoco una instancia del problema de la mochila con bolsillos. Si no tengo una solucion del KP, no voy a tener una solución del McB con 1 bolsillo y cap. W.

"""
