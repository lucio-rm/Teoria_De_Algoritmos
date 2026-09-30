"""


Ej.10 (★★★):
Manejamos un negocio que atiende clientes en Londres y en California. Nos interesa cada mes decidir si operar en una u otra ciudad. Los costos de operación para cada mes pueden variar y son dados por 2 arreglos: L y C, con valores para todos los meses hasta n. Naturalmente, si en un mes operamos en una ciudad, y al siguiente en una distinta, habrá un costo fijo M por la mudanza. 
Dados los arreglos de costos de operación en Londres (L) y California (C), indicar la secuencia de las n localizaciones en las que operar durante los n meses, sabiendo que queremos minimizar el total de los costos de operación. Se puede empezar en cualquier ciudad. 
Indicar y justificar la complejidad del algoritmo implementado.

"""
"""
planteo:
ec. recurrencia
OPT_L(i) es el costo minimo total acumuilado hasta el mes i, temrinando el mes i operando en Londres
OPT_C(i) idem, terminando el mes i operando en California

si quiero terminar el mes en Londres:
- estaba en L el mes anterior y me quedo
- estaba en C y me mudo (pago el M)
si quiero terminar el mes en C:
- estaba en C el mes anterior y me quedo
- estaba en L y me mudo (pago M)

OPT_L[n] = L[n] + min(OPT_L[n-1], M + OPT_C[n-1])
OPT_C[n] = C[n] + min(OPT_C[n-1], M + OPT_L[n-1])





"""
def plan_operativo(arreglo_L, arreglo_C, costo_M):
    n = len(arreglo_L)
    if n == 0:
        return []

    #armo las tablas, base 1 para manejar bien comodo los indices como vengo haciendo
    OPT_L = [0] * (n+1)
    OPT_C = [0] * (n+1)

    #caso base, mes 0 = costo 0
    OPT_L[0] = 0
    OPT_C[0] = 0 # igual, ya tendría que estar ese 0, o no?

    for i in range(1, n+1):
        costo_L_hoy = arreglo_L[i-1]
        costo_C_hoy = arreglo_C[i-1]

        #armo las opciones que hay
        quedarse_en_L = OPT_L[i-1] + costo_L_hoy
        mudarse_a_L = OPT_C[i-1] + costo_M + costo_L_hoy
        OPT_L[i] = min(quedarse_en_L, mudarse_a_L)

        # opciones para terminar en C
        quedarse_en_C = OPT_C[i-1] + costo_C_hoy
        mudarse_a_C = OPT_L[i-1] + costo_M + costo_C_hoy
        OPT_C[i] = min(quedarse_en_C, mudarse_a_C)

    #siempre armo una func aux para la ereconstruccion? es buena practica? o no pasa nada si lo hago aca=
    PLAN = []

    # si me paro en el último mes y veo que ciudad termina siendo más barata
    if OPT_L[n] <= OPT_C[n]:
        ciudad_actual = "Londres"
    else:
        ciudad_actual = "California"
    PLAN.append(ciudad_actual)

    #voy desde el mes n-1 ahcia atras hasta el mes 1
    for i in range(n, 1, -1):
        costo_L_hoy = arreglo_L[i-1]
        costo_C_hoy = arreglo_C[i-1]

        if ciudad_actual == "Londres":
            #y aca pienso la ec. recurrencia de vuelta tipo inversa
            # vino de quedarse en londres o de mudarse dese california
            if OPT_L[i] == OPT_L[i-1] + costo_L_hoy:
                ciudad_actual = "Londres"
            else: 
                ciudad_actual = "California"
        else:
            if OPT_C[i] == OPT_C[i-1] + costo_C_hoy:
                ciudad_actual = "California" #tenia que ponerlo en una constante externa, no?
            else:
                ciudad_actual = "Londres"
        PLAN.append(ciudad_actual)
        
    return PLAN[::-1] # doy vuelta, orden cronlogico (mes 1 al 133131313)