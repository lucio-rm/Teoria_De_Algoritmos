"""
Enunciado 17:
Una función lineal se define como f(x) = a x + b.
Si tenemos dos funciones lineales f_1(x) = a_1 x + b_1 y
f_2(x) = a_2 x + b_2, entonces la composición puede simplificarse a:
f_3(x) = f_1(f_2(x)) = (a_1 a_2) x + (a_1 b_2 + b_1). Es decir, tenemos una nueva función lineal, cuyos a y b son los resultates marcados.

Utilizando división y conquista, implementar una función
composicion_n(a, b, c, n) que reciba los valores de a y b de una función lineal,
c y n y determine el valor de f^n(c) = f(f(f(...f(c)) (n composiciones de la
función f consigo misma) en tiempo \mathcal{O}(\log n).
Justificar adecuadamente la complejidad del algoritmo implementado.

Recomendamos primero obtener los valores de a y b que corresponden a f^n(x). La cuenta final es trivial.

¿Querés más ayudas? En el enunciado en la guía hay unas más (no las ponemos directo en caso que lo quieras pensar directamente, en la guía podemos ocultarlos y aquí no).

"""


def composicion_n(a, b, c, n):
    return 0
