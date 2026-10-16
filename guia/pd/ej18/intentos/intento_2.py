
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
    ~ y en [3][3], como nunca antes nadie se fijó (logicamente) en este mismo, tampoco crea dependencia.


5.
        [0-0]
      [1-0][1-1]
    [2-0][2-1][2-2]
  [3-0][3-1][3-2][3-3]
[4-0][4-1][4-2][4-3][4-4]
~ puedo predecir qué OPT* voy a necesitar. en fila n-1, in range (1, n-1) -> 1, 2, 3
siendo n = 5 filas:
for i in range(1, n-1):
    OPT*[4, i]
~osea:
    OPT*[4][1]
    OPT*[4][2]
    OPT*[4][3]
~ y ahora el comportamiento es con una iteración desde afuera hasta adentro.
~ sé que el * de 4-1 va a necesitar del *4-2, y asi. pero el 4-3, depende de él mismo.
OPT*[4][3] = v_{4}{3} + min(OPT[3][2], OPT[3][3])
OPT*[4][2] = v_{4}{2} + min(OPT[3][1], OPT[3][2], OPT*[4][3])
OPT*[4][1] = v_{4}{1} + min(OPT[3][0], OPT[3][1], OPT*[4][2])

OPT[4][0] = v_{4}{0} + min(OPT[3][0], OPT*[4][1])
OPT[4][1] = OPT*[4][1]
OPT[4][2] = min(v_{4}{2} + OPT[4][1], OPT*[4][2]) ^ 
OPT[4][3] = min(v_{4}{3} + OPT[4][2], OPT*[4][3])
OPT[4][4] = v_{4}{4} + min(OPT[3][3], OPT[4][3])

^ repito, si *4-1 no tomó el camino del *4-2, tengo que tenerlo en cuenta. es una posibilidad je. si lo toma. no va a ser el min


6.
            [0-0]
          [1-0][1-1]
        [2-0][2-1][2-2]
      [3-0][3-1][3-2][3-3]
    [4-0][4-1][4-2][4-3][4-4]
  [5-0][5-1][5-2][5-3][5-4][5-5]
~ voy a repetir todo. se puede predecir. y se va a presentar la ecuación de recurrencia y la conclusión.

OPT*[5][4] = v_{5}{4} + min(OPT[4][3], OPT[4][4])
OPT*[5][3] = v_{5}{3} + min(OPT[4][2], OPT[4][3], OPT*[5][4])
OPT*[5][2] = v_{5}{2} + min(OPT[4][1], OPT[4][2], OPT*[5][3])
OPT*[5][1] = v_{5}{1} + min(OPT[4][0], OPT[4][1], OPT*[5][2])

OPT[5][0] = v_{5}{0} + min(OPT[4][0], OPT*[5][1])
OPT[5][1] = OPT*[5][1]
OPT[5][2] = min(v_{5}{2} + OPT[5][1], OPT*[5][2])
OPT[5][3] = min(v_{5}{3} + OPT[5][2], OPT*[5][3])
OPT[5][4] = min(v_{5}{4} + OPT[5][3], OPT*[5][4])
OPT[5][5] = v_{5}{5} + min(OPT[4][4], OPT[5][4])

"""
"""
conclusión:

tengo que pre-calcular una tabla de óptimos estrella (OPT*), de la cual realizo este comportamiento:
OPT*[2][1] = v_{2}{1} + min(OPT[1][0], OPT[1][1])

OPT*[3][2] = v_{3}{2} + min(OPT[2][1], OPT[2][2])
OPT*[3][1] = v_{3}{1} + min(OPT[2][0], OPT[2][1], OPT*[3][2])

OPT*[4][3] = v_{4}{3} + min(OPT[3][2], OPT[3][3])
OPT*[4][2] = v_{4}{2} + min(OPT[3][1], OPT[3][2], OPT*[4][3])
OPT*[4][1] = v_{4}{1} + min(OPT[3][0], OPT[3][1], OPT*[4][2])

OPT*[5][4] = v_{5}{4} + min(OPT[4][3], OPT[4][4])
OPT*[5][3] = v_{5}{3} + min(OPT[4][2], OPT[4][3], OPT*[5][4])
OPT*[5][2] = v_{5}{2} + min(OPT[4][1], OPT[4][2], OPT*[5][3])
OPT*[5][1] = v_{5}{1} + min(OPT[4][0], OPT[4][1], OPT*[5][2])

1 fila  - 0
2 filas - 0
3 filas - 1
4 filas - 2
5 filas - 3
6 filas - 4

sacando casos base (1 y 2 filas), que tienen comportamiento normal

para la fila n, necesito (n-2) óptimos estrellas.


~ Ecuación de Recurrencia:
para la ecuación de recurrencia, analizo el comportamiento de forma tal que el primer elemento y el último tiene un comportamiento específico. pero el resto tiene comportamiento normal y predecible.
casos base:
. OPT[0][0] = valor_{0}{0}
. OPT[1][0] = valor_{1}{0} + OPT[0][0]
. OPT[1][1] = valor_{1}{1} + OPT[0][0]

    para cualquier fila i: sé que la fila va desde 0 hasta i
    ~ siendo siempre:
     p = primero = 0
     d = p + 1 = 1
     u = ultimo = i
     a = ante-ultimo = u-1
.
~~~~OPTIMO ESTRELLA: 
caso base:
OPT*[i][a] = valor_{i}{a} + min(OPT[i-1][a-1], OPT[i-1][a]) # demostrar por qué nunca se va de indice (ya cubri los casos (0, 0) (1, 0) y (1, 1))

caso general:
for j in range(a-1, 0, -1) ~~~> desde el antepenúltimo hasta el (d) (si ya el antepenultimo es 0, no entra en el for)
OPT*[i][j] = valor_{i}{j} + min(OPT[i-1][j-1], OPT[i-1][j], OPT*[i][j+1])




~~~~OPT:
OPT[i][p] = valor_{i}{p} + min(OPT[i-1][p], OPT*[i][d])
OPT[i][d] = OPT*[i][d]
OPT[i][for j in range (p+2, u)] = min(valor_{i}{j} + OPT[i][j-1], OPT*[i][j])
...
OPT[i][u] = valor_{i}{u} + min(OPT[i-1][u], OPT[i][u-1])


"""


def camino_minimo_piramide(piramide):
    if not piramide:
        return []
    n = len(piramide)
    ESTRELLA = [[0] * n for _ in range(n)] # se podría optimizar, no voy a utilizar todos.
    OPT = [[0] * n for _ in range(n)] # lo mismo que esto. estoy creando una matriz $n \times n$, cuando sólo voy a utilizar (n/2)

    # casos base:
    OPT[0][0] = piramide[0][0] # el inicio
    if n == 1:
        return OPT[0][0], [0] # un solo elemento, el camino finaliza ahí.
    OPT[1][0] = piramide[1][0] + OPT[0][0]
    OPT[1][1] = piramide[1][1] + OPT[0][0]
    """
    casos base:
    . OPT[0][0] = valor_{0}{0}
    . OPT[1][0] = valor_{1}{0} + OPT[0][0]
    . OPT[1][1] = valor_{1}{1} + OPT[0][0]
        para cualquier fila i: sé que la fila va desde 0 hasta i
        ~ siendo siempre:
        p = primero = 0
        d = p + 1 = 1
        u = ultimo = i
        a = ante-ultimo = u-1
    ~~~~OPTIMO ESTRELLA: 
    caso base:
    OPT*[i][a] = valor_{i}{a} + min(OPT[i-1][a-1], OPT[i-1][a]) # demostrar por qué nunca se va de indice (ya cubri los casos (0, 0) (1, 0) y (1, 1))
    caso general:
    for j in range(a-1, 0, -1) ~~~> desde el antepenúltimo hasta el (d) (si ya el antepenultimo es 0, no entra en el for)
    OPT*[i][j] = valor_{i}{j} + min(OPT[i-1][j-1], OPT[i-1][j], OPT*[i][j+1])
    ~~~~OPT:
    OPT[i][p] = valor_{i}{p} + min(OPT[i-1][p], OPT*[i][d])
    OPT[i][d] = OPT*[i][d]
    OPT[i][for j in range (2, u)] = min(valor_{i}{j} + OPT[i][j-1], OPT*[i][j])
    ...
    OPT[i][u] = valor_{i}{u} + min(OPT[i-1][u], OPT[i][u-1])
    """
    ult = n-1
    
    for i in range(2, n):
        p = 0 # primero
        d = p+1 = 1 # el siguiente del primero
        u = i # ultimo
        a = u-1 # anteUltimo
        
        # lleno tabla OPTIMOS ESTRELLA para fila i
        # caso base de siempre para cada fila i
        ESTRELLA[i][a] = piramide[i][a] + min(OPT[i-1][a-1], OPT[i-1][a]) #nunca me voy de indice, ya que en el peor de los casos (en la primer iteracion)
        # va a ser: i = 2, u = 2, a = 1. por lo que acceder a i-1 y a-1, se puede tranquilamente.
        for j in range(a-1, 0, -1):
            ESTRELLA[i][j] = piramide[i][j] + min(OPT[i-1][j-1], ESTRELLA[i][j+1]) 
            # ecuacion de recurrencia para OPT_ESTRELLA. tampoco me voy de índice con j. porque en el peor de los casos (primera iteracion) (j+1) = a, y estoy accediendo al anteUltimo.
        
        # lleno tabla OPT para fila i
        # casos base:
        OPT[i][p] = piramide[i][p] + min(OPT[i-1][p], ESTRELLA[i][d]) # el primero de cada fila.
        OPT[i][d] = ESTRELLA[i][d] # el segundo de cada fila
        for j in range(2, u): #desde el 2, hasta el anteUltimo, que tienen comportamiento igual para cada caso. ya habiendo pre-calculado la tabla Estrella.
            OPT[i][j] = min(piramide[i][j] + OPT[i][j-1], ESTRELLA[i][j])
        #caso base, último de la fila (lo tengo que hacer despues de llenar la tabla de OPTIMOS).
        OPT[i][u] = piramide[i][u] + min(OPT[i-1][u], OPT[i][u-1]) # puedo poner OPT[i][i] y esas cosas, y no usar 'u'. pero es mejor usarlo para entender mejor.
    
    """
    encontrar a dónde llegamos (el destino), uso la última fila (la base) de la tabla OPT.
    como la tabla OPT guarda los optimos de haber llegado a cada pos, recorro la última fila, fjandome a cuál llegué con el menor valor posible.    
    """
    destino = (float('inf'), ult, 0)
    idx = 0
    while idx <= i:
        if OPT[i][idx] < destino[0]: #el valor
            destino[0] = OPT[i][idx]
            destino[2] = idx # en qué pos de la ult. fila lo encontré. me guardo siempre el mínimo de todos.
        idx += 1
    
    return destino[0], _reconstruccion(piramide, OPT, destino)

def _reconstruccion(piramide, OPT, destino):
    if destino[0] == float('inf'):
        return [] # no se pudo llegar a la base.
    """
    idea de reconstruccion:
    sé con qué valor mínimo llegué, y en qué posición.
    tengo que usar la ec. recurrencia inversa, para fijarme \textbf{desde dónde} vine.
    
    """
    CAMINO = []
    
    fila = destino[1]
    columna = destino[2]
    #fila y columna empiezan desde el final. desde la posición del destino.
    CAMINO.append([fila, columna]) #agrego el final.
    
    while fila > 0 and columna > 0:
        """
        cuando sean (0,0) llegué al inicio. elemento en fila 0 es uno solo. el (0,0)
        ~ me tengo que fijar desde cuál de las puntas (como máximo 4), vine.
        para fijarme, me tengo que fijar cuál es igual a: 
        (valor_actual = OPT[i][j])
        valor_elegido == valor_actual - piramide[i][j]
        """
        # minimo = (float('inf'), fila, columna)
        valor_actual = piramide[fila][columna] # por cada iteración, reescribo el valor actual y optimo actual que necesito.
        opt_actual = OPT[fila][columna]
        buscado = valor_actual - opt_actual # con el que coincida, significa que fuí por ahí.
        
        if columna < fila:
            # puedo acceder al de la derecha, me fijo si ese es el elegido.
            valor = OPT[fila][columna+1]
            if buscado == valor:
                columna += 1
                CAMINO.append([fila, columna])
        elif columna > 0: # no entra si ya encontré el buscado.
            # me fijo con el de la izquierda
            valor = OPT[fila][columna-1]
            if buscado == valor:
                columna -= 1 # fila queda igual.
                CAMINO.append([fila, columna])
        elif columna > 0 and columna > 0:
            # me fijo con el de arriba-izquierda
            valor = OPT[fila-1][columna-1]
            if buscado == valor:
                columna -= 1
                fila -= 1
                CAMINO.append([fila, columna])
        elif columna > 0:
            # me fijo con el de arriba.
            valor = OPT[fila-1][columna]
            if buscado == valor:
                fila -= 1
                CAMINO.append([fila, columna])
        
    return CAMINO[::-1] # en orden cronológico.

