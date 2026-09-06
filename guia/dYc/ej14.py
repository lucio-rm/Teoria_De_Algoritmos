"""
Enunciado ejercicio 14:
(★★) Se sabe, por el teorema de Bolzano, que si una función es continua en un intervalo [a, b], y que en el punto 'a' es positiva y en el punto 'b' es negativa (o viceversa), necesariamente debe haber (al menos) una raíz en dicho intervalo. Implementar una función raiz que reciba una función (univariable) y los extremos mencionados a y b, y devuelva una raíz dentro de dicho intervalo (si hay más de una, simplemente quedarse con una). La complejidad de dicha función debe ser logarítmica del largo del intervalo [a, b]. 
Asumir que por más que se esté trabajando con números enteros, hay raíz en dichos valores: 
Se puede trabajar con floats, y el algoritmo será equivalente, simplemente se plantea con ints para no generar confusiones con la complejidad. 

Justificar la complejidad de la función implementada.

"""
"""
planteo:
raiz:
la raiz seria cuando en el intervalo [a, b], f(num) = 0, 

tengo una idea.
caso borde: (f(a) > 0 && f(b) > 0) || (f(a) < 0 && f(b) < 0) { return None, o 0? } 
caso base: 
- (f(a) == f(b) && f(a) == 0) return a
- f(a) == 0 return a
- f(b) == 0 return b


pienso en ir al medio de 
mid: (a + b) // 2.

si f(mid) == 0: return mid

si f(mid) > 0:
    - si f(a) < 0, la raiz esta en [a, mid]
    - si f(a) > 0, la raiz esta en [mid, b]
si f(mid) < 0:
    - si f(a) < 0, la raiz esta en [mid, b]
    - si f(a) > 0, la raiz esta en [a, mid]
"""
def raiz(funcion, a, b):
    if (funcion(a) > 0 and funcion(b) > 0) or (funcion(a) < 0 and funcion(b) < 0):
        return None

    if (funcion(a) == funcion(b) and funcion(a) == 0):
        return a
    elif funcion(a) == 0:
        return a
    elif funcion(b) == 0:
        return b

    mid = (a + b) // 2
    if funcion(mid) == 0:
        return mid
    elif funcion(mid) > 0:
        if funcion(a) < 0:
            return raiz(funcion, a, mid)
        else:
            return raiz(funcion, mid, b)
    else:
        if funcion(a) < 0:
            return raiz(funcion, mid, b)
        else:
            return raiz(funcion, a, mid)


"""
Complejidad: siendo n la cantidad de elementos

temporal:
Al ser un ejercicio de División y Conquista, puedo utilizar el Teorema Maestro para justificar la complejidad temporal:
T(n) = A.T(n/B) + f(n)
siendo:
- A: cantidad de llamados recursivos = 1. siempre se ejecuta 1 llamado recursivo por vez. nunca 2.
- B: en cuánto se parte el problema = 2. en el peor de los casos, se parte en [a,mid] y [mid,b]
- f(n): el costo de partir y combinar = O(n^C), C = 0. ya que el costo de todo lo que no es recursivo es constante (O(1)).

la ecuación de recurrencia queda como:
T(n) = T(n/2) + O(n⁰) -> T(n) = T(n/2) + O(1)

Teniendo logB(A) = log2(1) = 0, y logB(A) = C.
f(n) = θ(n^C.log^k(n)) , con C = logB(A) y k = 0, la ecuacion queda como: T(n) = θ(n^C.log^(k+1)(n)) 

complejidad temporal: T(n) = θ(log(n))

complejidad espacial: O(1), ya que manejamos solo variables (complejidad constante).

"""