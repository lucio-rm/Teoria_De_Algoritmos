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

tengo que tener una variable que me guarde todo lo que ando sumando en los anteriores pasods de arma

sumaAcumula

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
            #encontre un exito , devuelvo una copia del optimo actual polque puede seguir mejorando
            sol_optima.append(sol_parcial)
            return sol_optima[:]
        # si no sumó exactamente s, no agrego nada y devuelvo lo mejor que tenía
        return sol_optima
    else:
        dados_que_quedan = n - len(sol_parcial) - 1 #me fijo cuantos dados me quedan por tirar

    for lao in range(1, 7):
        la_nueva_suma = suma_acumulada + lao
        #posible rama: al sumar este lado no me paso del S
        
        """
        mejoro podas que me olvidé, que el maldito rpl me anda enseñando
        solo sigo si:
        - no me paso de s en el turno de ahora (la suma nueva <= s)
        - con todo lo que queda, si todos sacan 6, tengo chances de pasar o igualar s
        - con lo que queda, si todos sacan 1, no me voy a pasar de s
        """
        puedo_llegar = la_nueva_suma + (dados_que_quedan * 6) >= s
        no_me_paso = la_nueva_suma + (dados_que_quedan * 1) <= s
        if la_nueva_suma <= s and puedo_llegar and no_me_paso:
            sol_optima = _sumatoria_rec(n, s, la_nueva_suma, sol_parcial + [lao], sol_optima)
            # arr + [num] = suponer arr = [1, 2]. arr + [num] == [1, 2, num]. crea un nuevo arreglo.
            
    return sol_optima #devuelvo lo mejor que conseguí


"""
Justificacion de la compeljidad:
- temporal : muhco mucho mucho exponencial feo 
me permiti hacer igual el for, porque los lados de un dado son conocidos y una constante conocida. no creo que sea una mala practica del for v in grafo que decian. porque es constante conocida y "chica".
- espacial: O(las posibles combinaciones.)

"""