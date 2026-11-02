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
    flujo[("S", "V")] = 4 # completar
    flujo[("V", "T")] = 3 # completar
    flujo[("V", "W")] = 1 # completar
    flujo[("S", "W")] = 3 # completar
    flujo[("W", "T")] = 5 # completar
    flujo[("S", "U")] = 3 # completar
    flujo[("U", "W")] = 1 # completar
    flujo[("U", "Z")] = 2 # completar
    flujo[("Z", "X")] = 2 # completar
    flujo[("Z", "W")] = 0 # completar
    flujo[("W", "Z")] = 0 # completar
    flujo[("Z", "T")] = 0 # completar
    flujo[("T", "super_sumidero")] = 8 # completar
    flujo[("X", "super_sumidero")] = 2 # completar

    conjunto_fuente = ["S", "U", "V"] # completar
    conjunto_super_sumidero = ['T', 'W', 'X', 'Z', 'super_sumidero'] # completar

    return flujo, conjunto_fuente, conjunto_super_sumidero

