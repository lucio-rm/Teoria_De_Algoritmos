"""
Enunciado ej.7: 
vertices:
S->V: 6  ;  S->W: 3  ;  V->T: 3  ;  V->W: 1  ;  W->T: 7  ;  S->U: 5  ;  U->W: 1  ;  U->Z: 2  ;  Z->W: 3  ;  W->Z: 9  ;  Z->X: 3


Hacer un seguimiento de obtener el flujo máximo en la siguiente red de transporte, realizando las modificaciones previas que fueran necesarias. Luego, definir cuáles son los dos conjuntos del corte mínimo en dicha red.

Nota sobre RPL: no hay forma de evaluar un seguimiento por esta plataforma, así que se propone rellenar los valores de flujo para las aristas existentes, y dar los dos conjuntos del corte mínimo.

"""

def obtener_flujo():
    flujo = {}
    vertices = "S", "T", "U", "V", "W", "X", "Z", "super_sumidero"
    flujo[("S", "V")] = 0 # completar
    flujo[("V", "T")] = 0 # completar
    flujo[("V", "W")] = 0 # completar
    flujo[("S", "W")] = 0 # completar
    flujo[("W", "T")] = 0 # completar
    flujo[("S", "U")] = 0 # completar
    flujo[("U", "W")] = 0 # completar
    flujo[("U", "Z")] = 0 # completar
    flujo[("Z", "X")] = 0 # completar
    flujo[("Z", "W")] = 0 # completar
    flujo[("W", "Z")] = 0 # completar
    flujo[("Z", "T")] = 0 # completar
    flujo[("T", "super_sumidero")] = 0 # completar
    flujo[("X", "super_sumidero")] = 0 # completar

    conjunto_fuente = [] # completar
    conjunto_super_sumidero = [] # completar

    return flujo, conjunto_fuente, conjunto_super_sumidero
