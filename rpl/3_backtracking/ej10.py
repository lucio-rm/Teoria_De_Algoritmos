"""
Enunciado ej.10:
Implementar un algoritmo tipo Backtracking que reciba una cantidad de dados n y una suma s. La función debe devolver todas las tiradas posibles de n dados cuya suma es s. Por ejemplo, con n = 2 y s = 7, debe devolver [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]. 
¿De qué complejidad es el algoritmo en tiempo? ¿Y en espacio?

"""
"""
planteo:
tengo ganas de hacerlo por PD, pero bueno


se puede llenar una matriz
- se sabe que cada dado tiene 6 valores {1, 2, 3, 4, 5, 6}

por cada n, se agrega otro for?

tipo
for lado_d1 in range(1, 7):
    for lado_d2 in range(1, 7):
        ...
        // se me va para n!?

sol_parcial va a tener las posibles combinaciones


un indice fijo que va a ser el primer dado. el valor 0 no existe, asi que cuando termino de recorrer todos los valores de ese dado, terminó.

el indice va a ser el valor de todos los lados del dado.


n me dice la cantidad de arreglos [1, ..., 6] que tengo posibles para combinar.



bien. 
cada recursión representa un dado tirado.

"""

def sumatoria_dados(n, s):
    if n == 0 or s == 0:
        return []
    sol_parcial = [] # la tirada actual de dados
    sol_optima = [] #todas las tiradas

    return _sumatoria_rec(n, s, 0, sol_parcial, sol_optima)


def _sumatoria_rec(n, s, suma_acumulada, sol_parcial, sol_optima):
    # caso base: tiré n dados
    if len(sol_parcial) == n:
        if suma_acumulada == s:
            #encontre un exito , devuelvo una copia del optimo actual
            sol_optima.append(sol_parcial)
            return sol_optima[:]
        # si no sumó exactamente s, no agrego nada y devuelvo lo mejor que tenía
        return sol_optima

    for lao in range(1, 7):
        #posible rama: al sumar este lado no me paso del S
        if suma_acumulada + lao <= s:
            sol_optima = _sumatoria_rec(n, s, suma_acumulada + lao, sol_parcial + [lao], sol_optima)
            # arr + [num] = suponer arr = [1, 2]. arr + [num] == [1, 2, num]. crea un nuevo arreglo.
            
    return sol_optima #devuelvo lo mejor que conseguí


"""
Justificacion de la compeljidad:
- temporal : muhco mucho mucho exponencial feo 
me permiti hacer igual el for, porque los lados de un dado son conocidos y una constante conocida. no creo que sea una mala practica del for v in grafo que decian. porque es constante conocida y "chica".
- espacial: O(las posibles combinaciones.)

"""