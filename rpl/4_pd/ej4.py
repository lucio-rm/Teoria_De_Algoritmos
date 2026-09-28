"""
Ej.4 (★★):
Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar dos días seguidos. Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación dinámica, el máximo monto a ganar, sabiendo que no aceptará trabajar dos días seguidos. 
Hacer una reconstrucción para verificar qué días debe trabajar. 

Indicar y justificar la complejidad del algoritmo implementado.
"""
"""
planteo:
ec. recurrencia:
subproblemas.

o trabajo el dia o no trabajo. (se puede pensar también como el scheduling).

mismo que el de las escaleras tambien.

casos bases:
OPT(n), siendo n la cantidad de dias en el arreglo
OPT(0) = 0
OPT(1) = v_1
OPT(2) = max(v_1, v_2)
OPT(3) = max(v_1 + v_3, v_2)

OPT(4) = max(v_4 + OPT(2), OPT(3))
OPT(5) = max(v_5 + OPT(3), OPT(4))

mas generalizado:
OPT(n) = max(v_n + OPT(n-2), OPT(n-1))


pensandolo en una forma iterativa (bottom-up, no top-down)

para el memoization si o si tengo que usar un arreglo M_RECORDAR para guardar los días y el optimo.
mismo que el del weighted schedule.


reconstrucción:
tengo que ir de atras para adelante. desde el final de la tabla.
me fijo:
ult = ultimovalor
ante_ult = ...
ante_pen = ...

si en unlt trabajé, significa que ult != ante_ult.
si en ante_ult trabajé, significa que ult == anteult
si ante_pen trabajé, ante_pen == ante_ult

. ese planteamiento estuvo mal.
"""
def juan_el_vago(trabajos):
    if not trabajos:
        return []
    cant = len(trabajos)
    M_DIAS = [0] * (cant + 1) # + 1 para que el indice maximo sea exactamente cant
    # como está en base 1, ahora M_DIAS[cant_dias_que_hay]
    M_DIAS[0] = 0 # 0 dias, 0
    M_DIAS[1] = trabajos[0] # 1 dia, ese mismo.
    #lleno la tabla de optimalidades (se dice asi¿?)
    for i in range(2, cant+1):
        M_DIAS[i] = max(trabajos[i-1] + M_DIAS[i-2], M_DIAS[i-1])
        #trabajos[i-1] es el valor del trabajo actual por el desfasaje
    
    
    indice = cant
    DIAS_TRABAJADOS = [] # esta bien en mayuscula? o bien para el orto?
    
    while indice >= 1:
        # si no hay M_DIAS[i-2] para comparar, se trbaajo ese dia si se aportó valor
        if indice == 1:
            if M_DIAS[1] > 0:
                DIAS_TRABAJADOS.append(0)
            break
            
        # si el optimo actual vino de trabajar ese dia
        if trabajos[indice-1] + M_DIAS[indice-2] >= M_DIAS[indice - 1]:
            DIAS_TRABAJADOS.append(indice - 1)
            indice -= 2 # si trabajé, se anula el anterior
        else:
            indice -= 1
            

    return DIAS_TRABAJADOS[::-1] # O(n) para invertirlo, no?

"""
Justificación de la complejidad:
- temporal: O(n)
O(n) para llenar la tabla de dias con los optimos, y O(n) para la reconstrucción. siendo n la cantidad de dias para trbaajar

- espacial: O(n)
a lo sumo va a ser eso, guardado en arreglos.

"""