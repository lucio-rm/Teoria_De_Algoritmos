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
    flujo[("super_fuente", "S")] = 7 # completar
    flujo[("super_fuente", "X")] = 2 # completar
    flujo[("S", "V")] = 4 # completar
    flujo[("S", "U")] = 3 # completar
    flujo[("V", "T")] = 3 # completar
    flujo[("V", "W")] = 1 # completar
    flujo[("W", "T")] = 6 # completar
    flujo[("U", "W")] = 4 # completar
    flujo[("X", "Z")] = 2 # completar
    flujo[("Z", "W")] = 1 # completar
    flujo[("Z", "U")] = 1 # completar
    flujo[("U", "Z")] = 0 # completar

    conjunto_super_fuente = ['super_fuente', 'S', 'U', 'V', 'W', 'X', 'Z'] # completar
    conjunto_sumidero = ["T"] # completar

    return flujo, conjunto_super_fuente, conjunto_sumidero

