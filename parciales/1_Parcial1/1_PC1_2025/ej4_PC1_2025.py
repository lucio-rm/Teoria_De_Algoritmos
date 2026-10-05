"""
Enunciado ejercicio 4:

Laura está de viaje por Japón y entró a un Centro Pokemon, a comprar merchandising. Va a tratar de llevarse todo lo más valioso (para ella) que pueda y que entre en su mochila. Tiene 2 limitaciones. 
La primera: no puede guardar más peso que lo que permita su mochila (tiene límite hasta W).
La segunda: como sabe que puede entrar en un estado de locura e incociencia temporal, se puso un límite que no comprará por más de P precio *en total* (es decir, la suma de todo lo comprado). 
Cada producto tiene 3 valores asociados: su valor (v_i, que Laura definió en base a su subjetividad), su precio (p_i) y su peso (w_i).

Implementar un algoritmo que, utilizando *programación dinámica*, permita determinar qué productos debe comprar Laura tal que no superen el peso máximo que puede llevar y el precio máximo dispueto a pagar, y que logre maximizar el valor obtenido (dados por la suma de los elementos comprados). 
También escribir el algoritmo que permita reconstruir la solución.
Indicar y justificar la complejidad del algoritmo implementado.

"""

"""
planteo:

limitaciones
- capacidad  -   W
- precio_total - P

producto = (valor v_i, precio p_i, peso w_i)

PD, 
resultado : <= W and <= P and max_valor_posible


devolver qué productos tiene que comprar Laura --> Reconstrucción.


pienso Ec. Recurrencia:


yo quiero saber si comprar o no comprar el producto que estoy viendo.

si compro = OPT(i, P, W) = OPT(i-1, P-p_i, W-w_i) + v_i

no compro = OPT(i, P, W) = OPT(i-1, P, W)

OPT me dice el mejor valor que puedo tener en el momento de comprar el producto i. Me convendrá comprar el producto o no?
si compro, tengo que reducir el precio tope que me queda y la capacidad.

La ecuación de recurrencia queda como:

OPT(i, P, W) = max(v_i + OPT(i-1, P-p_i, W-w_i), OPT(i-1, P, W))

  P- ... - 10 - 9 - 8 ... 0
W i
0   0 
1    1
2
3
4
.
.
.
W


termina siendo una matriz cubica (es un problema en complejidad eso?)
no me estaría dando cuenta la solucion real. pero decime si el algoritmo no funciona o lo hace mal.
"""
def pokemons(productos, P, W):
    if not productos or W <= 0 or P < 0:
        return []
    n = len(productos)
    M_CUBICA = [[[0] * (W+1) for _ in range(P+1)] for _ in range(n+1)]
    # 3 ejes.
    
    for p in range(0, n):
        producto = productos[p]
        valor_actual = producto[0]
        precio_actual = producto[1]
        peso_actual = producto[2]
        for i in range(0, (W+1)):
            for j in range(0, (P+1)):
                if precio_actual > j and peso_actual > i:
                    # y ahora hago la ecuacion de recurrencia
                    agarro = M_CUBICA[p-1][i-peso_actual][j-precio_actual] + valor_actual
                    no_agarro = M_CUBICA[p-1][i][j]

                    M_CUBICA[p][i][j] = max(agarro, no_agarro)
                else:
                    M_CUBICA[p][i][j] = M_CUBICA[p-1][i][j] # voy al anterior

    return _reconstruccion(M_CUBICA, productos, P, W)

def _reconstruccion(M_CUBICA, productos, P, W):
    PRODUCTOS_COMPRADOS = []
    """
    idea de reconstruccion:
    voy al final de la cubica. si el valor cambió (comparado con izq y arriba), significa que lo usé.
    si no cambió, voy al anterior. significa que no pude mejorarlo.    
    """
    p = len(productos)
    i = W
    j = P

    while p >= 0 and i >= 0 and j >= 0:
        actual = M_CUBICA[p][i][j]
        izq = M_CUBICA[p][i-1][j]
        arr = M_CUBICA[p][i][j-1]
        #aplico ec. recurrencia inversa
        if actual > izq and actual > arr:
            #significa que lo compré
            PRODUCTOS_COMPRADOS.append(productos[p-1]) # desfasaje.
            comprado = productos[p-1]
            j -= comprado[1]
            i -= comprado[2]
        p -= 1 #voy al anterior
    
    return PRODUCTOS_COMPRADOS[::-1] # invierto, asi queda en orden cronológico en que los compró Laura



"""
justificacion de la complejidad:
- temporal: 
vamos a tener un problema, como el knapsack problem 0/1 era pseudo-polinomial (O(n.W)), este también y peor aún porque depende de una tercer variable.
O(n.W.P), es proporcional a la capacidad dada y al precio tope que son límites para el problema.

- espacial: O(n.W.P), la matriz cúbica va a ocupar ese espacio adicional.
"""
