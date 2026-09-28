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


"""
def juan_el_vago(trabajos):
    if not trabajos:
        return []
    cant = len(trabajos)
    M_DIAS = [0] * cant
    M_DIAS[0] = trabajos[0]
    M_DIAS[1] = max(trabajos[0], trabajos[1])
    M_DIAS[2] = max(trabajos[0] + trabajos[2], trabajos[1])

    #lleno la tabla de optimalidades (se dice asi¿?)
    for i in range(3, cant+1):
        M_DIAS[i] = max(trabajos[i] + M_DIAS[i-2], M_DIAS[i-1])
    
    indice = cant
    DIAS_TRABAJADOS = [] # esta bien en mayuscula? o bien para el orto?
    while indice >= 0:
        """
        reconstrucción:
        tengo que ir de atras para adelante. desde el final de la tabla.
        me fijo:
        ult = ultimovalor
        ante_ult = ...
        ante_pen = ...
        
        si en ult trabajé, significa que en ante_ult no, por lo que el óptimo de esas dos pos es igual.
        
        """
    return DIAS_TRABAJADOS[::-1] # O(n) para invertirlo, no?