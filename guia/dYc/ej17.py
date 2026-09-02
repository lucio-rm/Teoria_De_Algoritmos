"""
Enunciado ejercicio 17:
(★★★) Una función lineal se define como $f(x) = a x + b$. 
Si tenemos dos funciones lineales $f_1(x) = a_1 x + b_1$ y $f_2(x) = a_2 x + b_2$, entonces la composición puede simplificarse a: $f_3(x) = f_1(f_2(x)) = \left(a_1 a_2 \right) x + \left(a_1 b_2 + b_1\right)$. 
Es decir, tenemos una nueva función lineal, cuyos $a$ y $b$ son los resultates marcados.

Utilizando división y conquista, implementar una función composición_n(a, b, c, n) que reciba los valores de $a$ y $b$ de una función lineal, c y n y determine el valor de $f^n(c) = f(f(f(…f(c))$ ($n$ composiciones de la función $f$ consigo misma) en tiempo $\mathcal{O}(\log n)$. 
Justificar adecuadamente la complejidad del algoritmo implementado.

Ayudas:
Recomendamos primero obtener los valores de $a$ y $b$ que corresponden a $f^n(x)$. La cuenta final es trivial.

Quiero unas ayudas más:
* Si $n$ es par, entonces los los valores de $a$ y $b$ corresponden a los de $f^{\frac{n}{2}}\left(f^{\frac{n}{2}}(x)\right)$. * Si $n$ es impar, los valores de $a$ y $b$ son los que corresponden a los de $f\left(f^{n-1}(x)\right)$.


"""
