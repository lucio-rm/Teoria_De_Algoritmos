"""
Ej.16 (★★★★):
Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). 
Tiene la información de estas predicciones en el arreglo p, para todo día i=1,2,...,n. Osvaldo quiere determinar un día j en el cuál comprar la casa, y un día k en el cual venderla (k>j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto, es la de maximizar la ganancia dada por p[k]-p[j].
Implementar un algoritmo de programación dinámica que permita resolver el problema de Osvaldo. 
Indicar y justificar la complejidad del algoritmo implementado.
"""
"""
planteo:

maximizar ganancia p[k] - p[j]


pueden ser 2 ec. recurrencia?

j = comprar ; k = vender

opciones:
------ vendo hoy
- compro hoy y vendo hoy
- la tenia comprada y la vendo hoy

i = dia ; c_v (comprar-vender); t_v (tenia_comprada - vender)
OPT(0) = 0
OPT(1) = c_v
OPT(2) = max(c_v, t_v) -> t_v = tenia_comprada_dia_1
OPT(3) = max(c_v, t_v) -> 

p[i] - p[i] = 0, siempre, no? para que lo queiro en la ec . recurrencia. no caigo.
porque la opcion de comprar y vender hoy es una opcion? porque puede haber peores?

OPT(1) = p[1] - p[1]
(1, 1) --> dia 1, solo puedo comprarla y venderla hoy.

OPT(2) = max(p[2] - p[2], p[2] - p[1])
(2, 2) ; (1, 2) --> dia 2, puedo o c_v hoy, o haberla comprado dia 1 y venderla hoy

OPT(3) = max(p[3], )
(3, 3) ; (2, 3) ; (1, 3) --> dia 3, puedo (c_v hoy), (c dia 2 v hoy) y (c dia 1 v hoy)

OPT(4) = 
(4, 4) ; ()

"""

def compra_venta(p):
    if not p:
        return 0, len(p)
    return 0, len(p) - 1