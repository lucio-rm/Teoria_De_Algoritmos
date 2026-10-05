"""
Enunciado ejercicio 2:

El explorador Roberto se embarcó en una misión para encontrar el legendario Templo de los Vientos. En el vasto desierto, hay oasis donde puede recoger provisiones esenciales como agua y comida. Cada oasis tiene recursos limitados. Sin suficientes provisiones, Roberto no podrá cruzar el desierto. Sólo vamos a considerar el hecho de tener k cantidad de provisiones (no si son una cosa u otra).

Implementar un algoritmo *greedy* que permita a Roberto llegar al templo con la menor cantidad de paradas posibles en los oasis. 
Indicar y justificar la complejidad del algoritmo. 
Justificar por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar, si no dar un contraejemplo.
Datos que se reciben:
. Una lista de n elementos que nos indica cuántas provisiones (en cantidad) se pueden conseguir en cada uno de los n oasis.
. Una lista con las distancias del inicio de la travesía al primer oasis, del primero al segundo, del segundo al tercero, y así hasta la final de la travesía (la lista tiene n + 2 elementos).
. La cantidad de provisiones iniciales de Roberto.
. Una constante KM_PROVISION que indica cuántas provisiones se debe consumir para caminar un KM.
"""

"""
planteo:

provisiones = [] len() n -> primer oases -> ... -> n
distancias = [] len() n + 2 -> inicio -> primer oasis -> ... -> n -> final 
provisiones_iniciales
KM_PROVISION

primero recorrería todas las distancias para tener el KM final y poder saber cuántas provisiones mínimas totales voy a necesitar.

y a partir de ahí es agarrar la mayor cantidad de provisiones en cada oasis hasta llegar al total, y no hago más cantidad

no es óptimo, porque ignora el estado futuro (el hecho de tener 1000 en el próximo oasis y haber parado en el actual).
"""

def roberto_confio(provisiones, distancias, p_inicial, KM_PROVISION):
    if not provisiones or not distancias or (distancias[0] // KM_PROVISION) > p_inicial:
        # si las listas estan vacías, o la cantidad de provisiones hasta llegar al primer oasis no me alcanzan, no puedo empezar.
        return -1

    km_totales = 0
    for d in distancias:
        km_totales += d

    p_minimas = (km_totales // KM_PROVISION) - p_inicial
    p_actuales = p_inicial

    cant_paradas = 0
    llego = True

    
    idx_distancias = 0
    idx_provisiones = 0
    while llego:
        """
        secuencia:
        0- si no puedo llegar hasta el próximo Oasis, no puedo llegar al final. return -1.
        1- voy hasta el próximo Oasis, y de manera avariciosa agarro todas las provisiones que hayan ahi.
        2- si llegué al minimo de provisiones necesarias para llegar al final, return
        3- si no , sigo. 
        """
        necesito = distancias[idx_distancias] // KM_PROVISION
        if necesito > p_actuales:
            # si la cant. de provisiones que necesito son mayor a las tengo ahora, sé que no puedo llegar.
            llego = False
            break

        p_actuales += (provisiones[idx_provisiones] - necesito) #agarro toda la cantidad de provisiones del oasis sabiendo que gasté 'necesito' para llegar ahí.
        cant_paradas += 1
        if p_actuales >= p_minimas:
            # puedo tener más, si justo sumé muchas en el oasis y me pasé del mínimo que necesitaba.
            break

        idx_distancias += 1
        idx_provisiones += 1
    return cant_paradas if llego else -1


"""
Jusitifacion de la Complejidad y la Optimalidad:
- temporal: O(n), siendo n la cantidad de oasis.
recorro la lista de distancias: O(n)
en el bucle while, recorro como mucho (n+1). desde el primer oasis hasta el final. O(n)

- espacial: O(1), ya que utilizo puras variables constantes para analizar si llego o no.


- Optimalidad y justificacion Greedy:
El algoritmo implementado se trata de un algoritmo Greedy, ya que de manera avariciosa, en su estado actual (el oasis en el que está parado) agarra la mayor cantidad de provisiones que haya (óptimo local). Y eso lo ejecuta en una sucesión de n veces para llegar a un supuesto óptimo global (menor cantidad de paradas hechas).
La sucesión óptimos locales para un algoritmo Greedy, con el sesgo que tiene, llega al óptimo global. 
Con esa misma regla Greedy: agarrar la mayor cantidad de provisiones en el oasis en el que estoy parado.

NO es óptimo el algoritmo. Se puede demostrar con este contraejemplo:
provisiones = [1, 100000000, 2]
distancias = [1, 1, 500, 2] 
# no sé por qué dice que tiene uqe ser n+2 elementos. aca es. ini -> prim_O -> segun_O -> tercer_O -> fin
# del ini al prim -> 1km, prim al seg -> 1km, seg al ter -> 500km, ter al fin -> 2km. son 4 elementos en el arreglo de distancias. no n+2, n = 3 (3 oasis).

p_actuales = 5
KM_PROVISION = 1


Acá se puede ver cómo el algoritmo elige llegar al primero y agarrar esa 1 provisión que tiene, pudiendo ir directamente al segundo oasis sin hacer la primer parada ("empeorando" su estado actual -> no agarrar nada en el oasis en el medio del desierto) e ir directo a la segunda a agarrar todo y completar con el viaje.

cant_paradas minima es  1.
el algoritmo greedy devuelve  2.

No es óptimo.

"""
"""
# extra: Se puede encontrar el óptimo con la resolución de un algoritmo de Programación Dinámica 
# con la ecuación de recurrencia: OPT(i, p) = min(1 + OPT(i-1, p+(p_i - p_u)), OPT(i-1, p - p_u)), con p negativo se descarta esa rama. (significa que no llego)
buscando la minima cantidad de paradas
siendo 
- i: parada actual 
- p: provisiones
- p_i: provisiones del oasis (parada actual)
- p_u: provisiones usadas (para llegar a la parada actual)
o paro en el oasis (si paro en el oasis agarro claramente las provisiones), o no paro. en los dos casos tengo que restar las provisiones que usé para llegar a esa distancia.

provisiones_posibles => 0 - 1 - ... - p_inicial - 6 - 7 - 8 - 9 - 10 - ... - p_maximo
        PARADAS
ini (p_u = 0)       -   0 - 1 - ... - p_inicial - 6 - 7 - 8
oasis_1 (p_u = d_0 // KM_P)   -  
oasis_2 (p_u = d_1 // KM_P)  -
...       -
oasis_n   -
fin       -
"""

# pre condiciones: las mismas que el ejercicio
# post condiciones: devuelvo las paradas mínimas en las que necesito parar para llegar al final
def pinto_pd(provisiones, distancias, p_inicial, KM_PROVISION):
    if not provisiones or not distancias or (distancias[0] // KM_PROVISION) > p_inicial:
        # o listas vacias, o no pude llegar a la primera parada con las provisiones iniciales
        return []

    # lo correcto sería len(distancias) = n+1
    


"""
correcta resolucion:

pensamiento:
Cuál es la máxima cantidad de provisiones que Roberto puede acumular en el oasis i habiendo hecho exactamente j paradas en total?

las dimensiones de la tabal quedan fijas:
filas (i) : el oasis actual donde está parado Roberto (de 0 a n)
clumnas(j): la cantidad exacta de paradas permitidas en el viaje (de 0 a n)

Defino OPT(i, j) como la máxima cantidad de provisiones que Roberto puede tener al llegar al oasis i habiendo realizado exactamente j paradas en el camino

1. NO parar en el oasis anterior (i-1): venia del oasis i-1 con j paradas acumuladas, y consume las provisiones
opcion_no_parar = OPT(i-1, j) - costo_tramo
2. si paro en (i-1): venia del oasis i-1 habiendo hecho j-1 paradas (gasto 1 parada) y recolecto y consumo provisiones
opcion_parar = OPT(i-1, j-1) + provisiones[i-1] - costo_tramo

ec. recurrencia:
OPT(i, j) = max(opcion_no_parar, opcion_parar)
si alguna da menor a 0, murio de hambre y celda anulada con -inf


"""
def roberto_goat_pd(provisiones, distancias, p_inicial, KM_PROVISION):
    n = len(provisiones)
    costos_tramos = [d // KM_PROVISION for d in distancias]
    # convierto cada distancia en su costo directo en provisiones consumidas
    
    M_PD = [[-float('inf')] * (n+1) for _ in range(n+1)]
    # filas de 0 hasta n oasis hasta el final
    # columnas: n + 1 (desde 0 hasta un maximo de n paradas posibles)
    
    #caso base: punto inicial (fila 0), con 0 paradas hechas
    M_PD[0][0] = p_inicial

    for i in range(1, n+1):
        costo_tramo_act = costos_tramos[i-1]
        for j in range(n+1):
            opcion_no_parar = -float('inf')
            opcion_parar = -float('inf')

            #no paro
            if M_PD[i-1][j] >= costo_tramo_act:
                opcion_no_parar = M_PD[i-1][j] - costo_tramo_act
            # si paro
            if j > 0 and 1 <= i-1 <= n:
                p_oasis_anterior = provisiones[i-2]
                if M_PD[i-1][j-1] >= costo_tramo_act:
                    opcion_parar = M_PD[i-1][j-1] + p_oasis_anterior

            resultado = max(opcion_no_parar, opcion_parar)

            if resultado >= 0:
                M_PD[i][j] = resultado

    # cual es la menor cant. de paradas que logro tener con prov >= 0 (sin morir)
    for j in range(n+1):
        if M_PD[n+1][j] >= 0:
            return j

    return -1 # fue imposible cruzar el sdesierto


"""
justificacion de la complejidad:
- temporal O(n²)

- espacial O(n²)

"""