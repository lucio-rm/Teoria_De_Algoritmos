"""


Ej.11 (★★):
Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, siendo que las operaciones posibles son:
. (i) aumentar el valor del operando en 1;
. (ii) duplicar el valor del operando.
Implementar un algoritmo que, por programación dinámica, obtenga la menor cantidad de operaciones a realizar (y cuáles son dichas operaciones). Desarrollar la ecuación de recurrencia. 
Indicar y justificar la complejidad del algoritmo implementado. 

Aclaración: asegurarse de que el algoritmo presentado sea de programación dinámica, con su correspondiente ecuación de recurrencia.

"""
"""
planteo:
creo que se puedce hacer por greedy esto. sería más rapido?

ec. recurrencia, mirarlo de atras para adelante
. puedo restarle 1 == sumar uno el paso anterior
. si i es par, puedo dividirlo por 2 == duplicado el valro antes

OPT(i) min. #operaciones desde 0 hastai
OPT(0) = 0  -> caso base
si i es impar: OPT(i) = 1 + OPT(i-1)
si i es par: OPT(i) = 1 + min(OPT(i-1), OPT(i/2))

 y ahi estaría
 no hace falta tabla matriz , amen.

"""
def operaciones(k):
    if k <= 0:
        return []
    
    M_OPERACIONES = [0] * (k+1) #guardo el costo minimo

    for i in range(1, k+1):
        if i % 2 != 0:
            M_OPERACIONES[i] = 1 + M_OPERACIONES[i-1]
        else:
            M_OPERACIONES[i] = 1 + min(M_OPERACIONES[i-1], M_OPERACIONES[i//2])

    # reconstruccino
    
    L_OPERACIONES = []
    i = k

    while i > 0:
        # me fijo buscando queé operacion usé
        if i % 2 == 0 and M_OPERACIONES[i] == 1 + M_OPERACIONES[i // 2]:
            L_OPERACIONES.append("duplicar")
            i //= 2
        else:
            L_OPERACIONES.append("sumar 1")
            i -= 1
    
    return L_OPERACIONES[::-1] # como fuid e k a 0, lo invierto.


"""
justificacion de la complejidad:

- temporal: O(k)
calculo el csoto de cada numero k veces, y la reconstruccion lo mismo (como mucho k pasos) y si usé divisiones, sería mucho menos

- espacial: O(k)
M_OPERACIONES tamaño k + 1 ====> O(k+1) = O(k)


"""