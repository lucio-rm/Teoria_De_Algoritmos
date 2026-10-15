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
~

OPT[0][0] = v_{0}{0}
OPT[1][0] = v_{1}{0} + OPT[0][0]
OPT[1][1] = v_{1}{1} + OPT[0][0]





4.
        [ - ]
      [ - ][ - ]
    [ - ][ - ][ - ]
 [ - ][ - ][ - ][ - ]

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