"""
Ej.15 (★★★):
Dada una soga de n metros (n≥2) implementar un algoritmo que, utilizando programación dinámica, permita cortarla (en partes de largo entero) de manera tal que el producto de los largos de cada una de las partes resultantes sea máximo. El algoritmo debe devolver el valor del producto máximo alcanzable. 
Tener en cuenta que la soga puede cortarse varias veces, como se muestra en el ejemplo con n = 10. Indicar y justificar la complejidad del algoritmo. 
Ejemplos:
. n = 2  -> Debe devolver 1 (producto máximo es 1 * 1)
. n = 3  -> Debe devolver 2 (producto máximo es 2 * 1)
. n = 4  -> Debe devolver 4 (producto máximo es 2 * 2)
. n = 5  -> Debe devolver 6 (producto máximo es 2 * 3)
. n = 6  -> Debe devolver 9 (producto máximo es 3 * 3)
. n = 10 -> Debe devolver 36 (producto máximo es 3 * 3 * 4)
"""
"""
planteo:

pienso directo en la ec. recurrencia
OPT(i), siendo i la cantidad de metros
OPT(1) = 1 = nopuedocortarla
OPT(2) = 1 = 1 * 1
OPT(3) = 2 = 2 * 1
OPT(4) = 4 = 2 * 2
OPT(5) = 6 = 2 * 3
OPT(6) = 9 = 3 * 3
OPT(10) = 36 = 3 * 3 * 4


osea tengo que buscar la mejor partición.

cort(i), devuelve todas las combinaciones en las que se puede cortar la soga de i metros.

cort(2) = [(1, 1)]
cort(3) = [(2, 1), (1, 1, 1)]
cort(4) = [(3, 1), (2, 2), (1, 1, 1, 1), (2, 1, 1), (1, 1, 2)]
cort(5) = [(3, 2), ]

  1 --- 2 --- 3 --- 4 --- 5
  - -(1,1)--(1,2)

cort(2) = [(1, 1)]
cort(3) = [(2, 1), (cort(2), 1)]
cort(4) = [(3, 1), (2, 2), (cort(3), 1), (cort(2), cort(2))]
cort(5) = [(4, 1), (3, 2), (cort(4), 1), (cort(3), cort(2))]
cort(6) = [(5, 1), (4, 2), (3, 3), (cort(5), 1), (cort(4), cort(2)), (cort(3), cort(3))]

se encuentra un patron.

OPT(i) = max[(OPT(i-1), 1)]

2 = (1, 1)
3 = (2, 1)
4 = (3, 1) , (2, 2)
5 = (4, 1) , (3, 2)
6 = (5, 1) , (4, 2) , (3, 3)
7 = (6, 1) , (5, 2) , (4, 3)
8 = (7, 1) , (6, 2) , (5, 3) , (4, 4)
9 = (8, 1) , (7, 2) , (6, 3) , (5, 4)
10 = (9, 1) , (8, 2), (7, 3) , (6, 4) , (5, 5)

hay patron.
como se ven los subproblemas?
cuando viene messi?

si tengo n, y messi me dice que sabe cuanto es OPT(sicorto1m)
osea
voy cortando de pedacitos y me fijo cuánto me conviene
teniendo 5m
tengo varias opciones:
corto 1m = (4, 1)
corto 2m = (3, 2)
corto 3m = (2, 3) --> este ya no me sirve, tuve uqe haber parado antes

si es impar: para hasta el (mid+1, mid)
si es par: para hasta el (mid, mid)

----- vi clase eze
OPT(i) = max(k*OPT(i-k) ; OPT(k) * OPT(i-k); K * (i-k) ; OPT(k) * (i-k))



OPT(n) = max__paratodo_i E [1, n-1] de:
max ( 
    . i * (n-1)
    . OPT(i) * OPT(n-1)
    . OPT(i) * (n-1)
    . i * OPT(n-1)
)

OPT(n) = (max[i, OPT(i)], max[n-1, OPT(n-1)])
.
"""

def problema_soga(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    OPT = [0] * (n+1)
    OPT[1] = 1
    OPT[2] = 1
    for i in range(3, n+1):
        OPT[i] = _una_baaaanda_ec_rec(i, OPT)
    return OPT[n]

def _una_baaaanda_ec_rec(n, OPT):
    maximo = 0
    for i in range(1, n):
        opcion_1 = i * (n-i)
        opcion_2 = i * OPT[n-i]
        opcion_3 = OPT[i] * (n-i)
        opcion_4 = OPT[i] * OPT[n-i]
        maximo = max(maximo, opcion_1, opcion_2, opcion_3, opcion_4)
    return maximo

#okey, podia ponerlo en una lista con los valores y retornar el maximo, mal ahi


"""
justificacion de la complejidad:

- temporal: O(n), como mucho voy a hacer (n-1) iteraciones. god
<= O(n²), no? porque por cada iteracion llamo a la func. aux

- espacial: O(n), porque el arreglo de OPTIMOS como mucho se va a a llenar de N elementos (el optimo de cada uno)
"""