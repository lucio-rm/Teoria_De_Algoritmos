"""
Enunciado ej.6:
        3
     V --- T
  6/ \1  /6
S     W <-1--Z
  3\ /6  2 / |
    U -----  |3
        4    |
             X

vertices:
S->V: 6  ;  V->T: 3  ;  V->W: 1  ;  W->T: 6  ;  S->U: 3  ;  U->W: 6  ;  U->Z: 2  ;  Z->W: 1  ;  X->Z: 3  ;  Z->U: 4

Hacer un seguimiento de obtener el flujo máximo en la siguiente red de transporte, realizando las modificaciones previas que fueran necesarias. Luego, definir cuáles son los dos conjuntos del corte mínimo en dicha red.

Nota sobre RPL: no hay forma de evaluar un seguimiento por esta plataforma, así que se propone rellenar los valores de flujo para las aristas existentes, y dar los dos conjuntos del corte mínimo.

"""

def obtener_flujo():
    flujo = {}
    vertices = "super_fuente", "S", "T", "U", "V", "W", "X", "Z"
    flujo[("super_fuente", "S")] = 0 # completar
    flujo[("super_fuente", "X")] = 0 # completar
    flujo[("S", "V")] = 0 # completar
    flujo[("S", "U")] = 0 # completar
    flujo[("V", "T")] = 0 # completar
    flujo[("V", "W")] = 0 # completar
    flujo[("W", "T")] = 0 # completar
    flujo[("U", "W")] = 0 # completar
    flujo[("X", "Z")] = 0 # completar
    flujo[("Z", "W")] = 0 # completar
    flujo[("Z", "U")] = 0 # completar
    flujo[("U", "Z")] = 0 # completar

    conjunto_super_fuente = [] # completar
    conjunto_sumidero = [] # completar

    return flujo, conjunto_super_fuente, conjunto_sumidero