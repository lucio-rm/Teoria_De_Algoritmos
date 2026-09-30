"""

Ej.14 (★★★):
Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad de ser circular. Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa. Podemos enumerar a la primer casa como la casa 0, de la cual podríamos obtener g0 , la casa a su derecha es la 1, que nos daría g1, y así hasta llegar a la casa n-1, que nos daría gn-1 . Toda casa i se considera adyacente a las casas i-1 e i+1. Además, como la calle es circular, la casas 0 y n-1 también son vecinas. 
El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían muy rápido. No le daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos. El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema. 

Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a partir de recibir un arreglo de las ganancias obtenibles. Para esto, escribir y describir la ecuación de recurrencia correspondiente. 
Indicar y justificar la complejidad del algoritmo propuesto.


"""

"""
planteo:

primete del juan the vagician? como se dice vago en ingles, vague?
vagician
juan el vago
porque no puede trabajar (robar) dos días seguidos

y gran diferenci, calle circular. de eso no hay en quilmes.
una rotonda cuenta como calle circular? supongoq ue si

0 y n-1 son vecinas, no puedo robar ninguna de las dos

tendría dos casos:
- A: empiezo robando en la casa 0, porque son multimillonarios. robo la 0
        . no puedo robar la n-1 ni la 2
        . hago el mismo algoritmo de juancete para ese rango
- B: empiezo robando en la 1, porque la info de la 0 era mentira. robo la 1
        . no puedo robar ni la 0 ni la 3
        . misma shet rango (1, n-1)

comparo los dos casos y devuelvo esa reconstruccion

tendría que funcar


ec. recurrencia

OPT(i) ganancia max acumulada hasta la casa i:

OPT(i) = max(ganancias[i] + OPT(i-2), OPT(i-1)) ----> lineaaaal, no mas matrices


"""

def lunatico(ganancias):
    cant = len(ganancias)
    # casos base:
    if cant == 0:
        return []
    elif cant == 1:
        return [0] # a cuál robé
    elif cant == 2:
        return [0] if ganancias[0] >= ganancias[1] else [1]

    #me fijo las posiciones originales de las casas, previo a los casos de robo
    indices = list(range(cant))

    # primer caso, los de la casa 0 son unos giles. les robo al carajo y me apiado de los de la 1 y n-1
    ganancia_0, casas_0 = _juan_og(ganancias[2:cant-1], indices[2:cant-1])
    ganancia_0 += ganancias[0] # de la primer casa (no lo pasé por parametro
    casas_0 = [0] + casas_0 #mismo

    #segundo caso, me di cuenta que los de la 1 son mas giles y los de la n-1 mas todavia. perdono a los que viven en 0
    ganancia_1, casas_1 = _juan_og(ganancias[1:cant], indices[1:cant])
    #aca ya no sumo nada porque 1 fue incluido en el param. el problema con antes fue de que si yo hacia R(0, cant-1) tal vez elegia la 1 en vez de la 0 y me metía el robo en los de backtracking que me faltan
    
    #me fijo quien ganó y empiezo a robar ya mismo
    if ganancia_0 >= ganancia_1:
        return casas_0
    else:
        return casas_1


def _juan_og(ganancias, indices_reales):
    # estaría bien asi? otra forma de resolver ej. de PD, o no?
    # ec. recurrencia es una sola. pero el tener varios casodsd e partida, me hacen ejecutar el algoritmo una cantidad fija de veces. bastante goat porque sigue siendo polinomial. buena técnica.
    cant = len(ganancias)
    if cant == 0:
        return 0, []
    if cant == 1:
        return ganancias[0], [indices_reales[0]] # ahorra tiempo ¿?

    M_CASAS = [0] * (cant + 1)

    M_CASAS[1] = ganancias[0]

    for i in range(2, cant + 1):
        #aplico ec. recurrencia
        M_CASAS[i] = max(ganancias[i-1] + M_CASAS[i -2], M_CASAS[i-1])

    # reconstruccion
    CASAS_ROBADAS = []
    i = cant

    while i >= 1:
        if i == 1:
            if M_CASAS[1] > 0:
                CASAS_ROBADAS.append(indices_reales[0])
            break # asi evito el bucle recontrainficnito

        # me fijo si el optimo vino de haber robado la casa actual i
        # reconstruccion = aplicar ec. recurrencia inversamente para saber el comportamiento
        if ganancias[i-1] + M_CASAS[i -2 ] >= M_CASAS[i-1]:
            CASAS_ROBADAS.append(indices_reales[i-1])
            i -= 2
        else:
            i -= 1

    return M_CASAS[cant], CASAS_ROBADAS[::-1]



"""
Justificacion de la complejidad:
- temporal : O(n) polinomialGoat, siendo n la cantidad de casas en la calle privada circular
. hice slices en O(n)
. bucle _juan_og itera como mucho O(n), haciendo comparaciones (O(1))
. reconstruccion O(n)
O(n) + O(n) + O(n) = O(3n) = O(n), goat

- espacial: O(n)
. todo lo usado, listas de indices o M_CASAS, tienen como mucho n elementos.
"""