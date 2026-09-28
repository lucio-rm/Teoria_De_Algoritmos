"""

Ej.3 (★):
Dada una escalera, y sabiendo que tenemos la capacidad de subir escalones de a 1 o 2 o 3 pasos, encontrar, utilizando programación dinámica, cuántas formas diferentes hay de subir la escalera hasta el paso n. 
Indicar y justificar la complejidad del algoritmo implementado. 

Ejemplos: 
- n = 0 -> Debe devolver 1 (no moverse) 
- n = 1 -> Debe devolver 1 (paso de 1) 
- n = 2 -> Debe devolver 2 (dos pasos de 1, o un paso de 2) 
- n = 3 -> Debe devolver 4 (un paso de 3, o tres pasos de 1, o un paso de 2 y uno de 1, o un paso de 1 y un paso de 2) 
- n = 4 -> Debe devolver 7 
- n = 5 -> Debe devolver 13
"""
"""
planteo: 

mismo enunciado, nos muestra comportamiento.
ec . de recurrencia: 
OPT(n) = OPT(n-1) + OPT(n-2) + OPT(n-3)
se puede parecer al de fibonacci.

tenes la opcion de:
hacer 1 paso
hacer 2 pasos
hacer 3 pasos

entonces tengo que tener los 3 casos base listos (1, 2, 3) y despues sigue
OPT(1) = OPT(n-1) = OPT(0) = 1
OPT(2) = OPT(n-1) + OPT(n-2) = OPT(1) + OPT(0) = 1 + 1 = 2
OPT(3) = OPT(n-1) + OPT(n-2) + OPT(n-3) = OPT(2) + OPT(1) + OPT(0) = 2 + 1 + 1 = 4
OPT(4) = OPT(n-1) + OPT(n-2) + OPT(n-3) = OPT(3) + OPT(2) + OPT(1) = 4 + 2 + 1 = 7
OPT(5) = OPT(n-1) + OPT(n-2) + OPT(n-3) = OPT(4) + OPT(3) + OPT(2) = 7 + 4 + 2 = 13

simpre usa:
un_paso + dos_pasos + tres_pasos

pre_anterior
anterior
actual

haciendo n iteraciones: (siendo n la cantidad de escalones)
    total = actual + anterior + pre_anterior
    pre_anterior = anterior
    anterior = actual
    actual = total

"""
def escalones(n):
    total = 0
    pre_anterior = 1 # OPT(n-3)
    anterior = 1 # OPT(n-2)
    if n <= 1: return pre_anterior
    actual = 2 # OPT(n-1)
    # no se si esta bien ese de variable = OPT(n-algo), a chequear.
    if n == 2: return actual
    for i in range(3, n+1):
        total = actual + anterior + pre_anterior
        pre_anterior = anterior
        anterior = actual
        actual = total
    
    return total


"""
Justificacion de la complejidad:
- temporal: O(n), siendo n la cantidad de pasos. simple iteracion.
- espacial: O(1), se pudo optimizar a forma constante, con manejo de variables. porque lo único que tenemos que recordar son los anteriores 3 Optimos
"""
