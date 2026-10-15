"""
Ej.18 (★★) 
Dado un triángulo de n filas representado como una lista de listas, donde la fila i contiene exactamente i+1 enteros, implementar un algoritmo utilizando Programación Dinámica que encuentre un camino desde la cima hasta la base cuya suma de valores sea mínima. 
El recorrido comienza en la posición (0,0). 

Implementar el algoritmo que permita reconstruir la solución. 
Indicar y justificar la complejidad de ambos algoritmos.

"""

"""
planteo1:
como máximo puedo venir de mis 4 lados.
Ec. Recurrencia:
OPT[i][j] = v_{i}{j} + 
    { OPT[i][j+1] , j < i
min { OPT[i][j-1] , j > 0
    { OPT[i-1][j-1] , j > 0 and i > 0
    { OPT[i-1][j] , i > 0
"""
# resolucion 1: 
"""
Aclaración:
errónea. porque quiero acceder al OPT[i][j+1] (por ejemplo) y no va a estar llenado. si el camino ideal mínimo requería que vaya por ese lado, no lo puede averiguar.
"""
def cam_min(piramide):
    if not piramide:
        return []
    n = len(piramide) - 1

    OPT = [[float('inf')] * (n) for _ in range(n)]
    OPT[0][0] = piramide[0][0] # el inicio

    # lleno la tabla PD
    for i in range(1, n):
        for j in range(0, i+1):
            minimos = [float('inf')] * 4
            # siempre que puedo, accedo:
            if j < i: minimos[0] = OPT[i][j+1] # el de la derecha
            if j > 0: minimos[1] = OPT[i][j-1] # el de la izquierda
            if i > 0 and j > 0: minimos[2] = OPT[i-1][j-1]
            if i > 0: minimos[3] = OPT[i-1][j]

    i = n-1
    dest = (float('inf'), i, 0) 
    """
    como la tabla OPT guarda los optimos de haber llegado a cada pos, recorro la última fila, fjandome a cuál llegué con el menor valor posible
    """
    idx = 0
    while idx <= i:
        if OPT[i][idx] < dest[0]: #el valor
            dest[0] = OPT[i][idx]
            dest[2] = idx # en qué pos de la ult. fila lo encontré.
        idx += 1

    return _reconstruccion_1(piramide, OPT, dest)

def _reconstruccion_1(piramide, OPT, destino):
    if destino[1] == float('inf'):
        return [] # no pude llegar al final
    # sigue reconstruccion. etc etc.





"""
planteo2:

corrijo lo erróneo.

preguntas:
- como verga hago para saber el OPT de la derecha al mismo tiempo que accedo a mi pos. pierde PD
- repensar ec. recurrencia desde 0?

~ no volverse exponencial


idea2:
- pensar desde 0
1.
        [ - ]
OPT[0][0] = v_0
~ siempre caso base, el valor del mismo escalon pos(0, 0)

2.
         [0, 0]
      [1, 0][1, 1]
~ si no se llenó el OPT de la derecha, cómo puedo saberlo ¿?
~ pienso en este caso. como ya estoy en la base, lo mejor es llegar desde arriba lo antes posible sin vueltas \footnote{porque sino sumaría valor innecesario: 
(v_{0}{0} + v_{1}{0}) siempre $<=$ (v_{0}{0} + v_{1}{0} + v_{1}{1})
OPT[0][0] = v_{0}{0}
OPT[1][0] = v_{1}{0} + OPT[0][0]
OPT[1][1] = v_{1}{1} + OPT[0][0]


3.
        [0-0]
      [1-0][1-1]
    [2-0][2-1][2-2]
~ acá está lo que quiero tantear.
desde (2-0) puedo:
=> from (1-0) ==> v_{2}{0} + OPT[1][0] 
=> from (2-1) !!! no esta analizado el óptimo. en una dependencia circular entre óptimos (no se cómo se dice.)
# !!! el unico problema es del pelotudo que está a la derecha, y que puede formar del camino minimo óptimo que quiero lograr.
~ ¿ Cómo lo resuelvo ?

=> good -> solo necesito el de la derecha.
~ calcular el óptimo con delay.
~ porque cada uno necesita:
OPT[i][j] = v_{i}{j} + 
    { OPT[i][j+1] , j < i  ===============> derecha ====> *
min { OPT[i][j-1] , j > 0  ===============> izquierda ==> *
    { OPT[i-1][j-1] , j > 0 and i > 0 ====> arriba-izq => ok
    { OPT[i-1][j] , i > 0  ===============> arriba =====> ok

* busco el de izq/der, ese óptimo
* el óptimo, puede utilizar la lógica para "descartar" la dependencia circular.
~ soy el izq. tengo 2 opciones: venir de (1-0) o (2-1).  tengo que agarrar el mínimo.
    ~ suponer (1-0) = C
    ~ para el OPT(2-1) no necesito averiguar el OPT(2-2), porque por qué recorrer una casilla más (con algún peso p) si puedo venir directo de la (1-1).
        ~ OPT(2-1) va a agarrar el mín((1-0, 1-1)). (descarto dep. circular porque me estoy fijando en el izquierdo).
            ~ OPT(2-1) va a ser un OPT* (no el oficial), porque tal vez lo mejor para el OPT(2-1), cuando miremos al der, pueda ser venir por la izq.
~ soy der. mi única opcion va a ser venir de las dos opciones de arriba. sino sumo un peso p innecesario. OPT[2-1] = OPT*[2][1]
OPT[0][0] = v_{0}{0}
OPT[1][0] = v_{1}{0} + OPT[0][0]
OPT[1][1] = v_{1}{1} + OPT[0][0]
    OPT*[2][1] = v_{2}{1} + min(OPT[1][0], OPT[1][1])
OPT[2][0] = v_{2}{0} + min(OPT[1][0], OPT*[2][1])
OPT[2][1] = OPT*[2][1]
OPT[2][2] = v_{2}{2} + min(OPT[1][1], OPT[2][1])


4.
        [0-0]
      [1-0][1-1]
    [2-0][2-1][2-2]
 [3-0][3-1][3-2][3-3]

~ soy izq. (3-0). tengo 2 opciones: venir del (2-0) o del (3-1)
    ~ si vengo del (2-0), ya lo tengo calculado.
    ~ si vengo del (3-1), NO lo tengo calculado.
        ~ calculo un OPT*[3, 1]. del cual, sé que:
            ~ no puedo venir del [3, 0]
            ~ puedo venir del OPT[2-0], del OPT[2-1] o del OPT[3-2] (no calculado.)
                ~ tengo que hacer un OPT[3-2]*, que al descartar la opcion de venir desde el (3-0) y del (3,3) (suma p innecesaria), tengo que agarrar el mínimo de -> OPT[2-1] y OPT[2-2]
    OPT*[3][2] = v_{3}{2} + min(OPT[2][1], OPT[2][2])
    OPT*[3][1] = v_{3}{1} + min(OPT[2][0], OPT[2][1], OPT*[3][2])
OPT[3][0] = v_{3}{0} + min(OPT[2][0], OPT*[3][0])
OPT[3][1] = OPT*[3][1]
OPT[3][2] = min(v_{3}{2} + OPT[3][1], OPT*[3][2]) ^
OPT[3][3] = v_{3}{3} + min(OPT[2][2], OPT[3][2])

++++++ puedo hacer tambien, en varios OPT* , como descarto también las puntas puedo descartar el arriba-izq, porque sería suma de peso p innecesario.
++++++ si estoy desde (3-0), no quiero en OPT*[3-1] que calcule en el min() el 2-0. porque si gana ese, sé con certeza que min(OPT[2-1], OPT*[3-1]) gana 2-1.
            * ese pensamiento lo descarto, ya que para el OPT[3][1], voy a descartar esa lógica. asi que si gana o no, no me importa. no recalculo y lo uso igual, ya fue.
^ se puede pensar en este caso, una posible dependencia circular. pero es falso, porque si para el caso de OPT[3][1] se hubiera elegido el OPT*[3][2] tendría sumando constantes que no van a ganar nunca el mínimo. ir (2-2)->(3-2)->(3-1)->(3-2), siempre va a ser más costoso que (2-2)->(3-2).



5.
        [ - ]
      [ - ][ - ]
    [ - ][ - ][ - ]
  [ - ][ - ][ - ][ - ]
[ - ][ - ][ - ][ - ][ - ]

6.
            [ - ]
          [ - ][ - ]
        [ - ][ - ][ - ]
      [ - ][ - ][ - ][ - ]
    [ - ][ - ][ - ][ - ][ - ]
  [ - ][ - ][ - ][ - ][ - ][ - ]



"""





# testeo:
def main():
    pruebo = 0
    
if __name__ == "__main__":
    main()