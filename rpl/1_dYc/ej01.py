"""
Enunciado 01:
Se cuenta con un arreglo de enteros ordenado de manera ascendente que contiene exactamente un número duplicado (es decir, todos los demás elementos son distintos, sin duplicados). Implementar una función que encuentre dicho número utilizando división y conquista. Indicar y justificar la complejidad del algoritmo, utilizando el Teorema Maestro.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""

"""
planteo:
al no saber si es consecutivo o no, voy a tener que recorrer todo el arreglo sí o sí.
Como el ejercicio requiere una resolución recursiva, voy a llamar lado izquierdo y derecho, y comparar entre sí.



"""

def elemento_duplicado(arr):
    return _duplicado_rec(arr, 0, len(arr) - 1)

def _duplicado_rec(arr, ini, fin):
    if ini >= fin:
        return None
    
    medio = (ini + fin) // 2
    
    # evaluo el medio
    if medio < fin and arr[medio] == arr[medio + 1]:
        return arr[medio]
    if medio > ini and arr[medio] == arr[medio - 1]:
        return arr[medio]
        
    izq = _duplicado_rec(arr, ini, medio - 1)
    if izq is not None:
        return izq
        
    der = _duplicado_rec(arr, medio + 1, fin)
    return der

"""
Justificacion de la complejidad:
Al ser un algoritmo de DyC, justifico utilizando el Teorema Maestro: T(n) = A.T(n/B) + f(n)
A: cantidad de llamados recursivos = 2. en el peor de los casos, voy a terminar llamando pal izq y der.
B: en cuánto parto el problema = 2. parto en lado izquierdo y derecho.
f(n): el costo de partir y juntar los resultados = O(n^C), C = 0. Todo constante el resto de las operaciones.

La ecuación de recurrencia queda como: 
T(n) = 2.T(n/2) + O(1)
y como logB(A) > C, log2(2) > 0, log2(2) = 1, la ecuacion tienda a:
O(n^(logB(A)) = O(n)

La complejidad temporal cuesta O(n), tiene sentido ya que en el peor de los casos recorro todo el arreglo.
La compejidad espacial es O(n), porque paso por parametro al llamado recursivo n/2 elementos. O(n/2) = O(n)

"""













# siendo consecutivo, me fijo el indice y me doy cuenta si se "corrio" de su posicion.
"""
planteo:
voy al medio. si el medio no es el duplicado me fijo cuantos elementos tengo por izquierda y cuantos por derecha.

siendo :
medio
a = cant.izq
b = cant.der
i = primer elemento (arr[0])
j = ultimo elemento (arr[len(arr)-1])

si (medio - a) != i, sé que el duplicado esta en el lado izquierdo.
si (medio + b) != j, sé que el duplicado esta en el lado derecho.

en base a eso, una de esas dos condiciones si o si se va a cumplir si medio no es el duplicado, por lo que el saber que es consecutivo me permite "descartar" una mitad, por lo tanto, bajar la complejidad a O(logn) ya que siempre voy descartando mitades hasta llegar al duplicado.

"""

def elemento_duplicado2(arr):
    cant = len(arr)
    if cant == 1:
        return -1 # no existe un duplicado con 1 elemento en el arreglo

    medio = cant // 2
    if (cant > 1 and arr[medio-1] == arr[medio]) or (medio < cant-1 and arr[medio] == arr[medio+1]):
        return medio
    else:
        cant_izq = len(arr[:medio])
        cant_der = len(arr[medio+1:]) # al "medio" no lo cuento.
        if medio - cant_izq != arr[0]:
            elemento_duplicado2(arr[:medio]) # descarto la mitad derecha
        else:
            elemento_duplicado2(arr[medio:]) # si no se cumple el otro, sé con certeza que esta en el lado derecho. segun el enunciado hay "exactamente" un duplicado.
    


"""
justificacion de la complejidad:

Al ser un ejercicio de Division y Conquista, puedo justificar la complejidad temporal con el Teorema Maestro: T(n) = A.T(n/B) + f(n)
siendo:
A: cantidad de llamados recursivos = 1. si o si, siempre se ejecuta 1 al mismo tiempo.
B: en cuanto se parte el problema = 2. lado izquierdo y derecho.
f(n): el costo de partir y juntar = O(n^C), C = 0. ya que el costo de lo que no es recursivo, es constante.

La ecuación de recurrencia queda como:
T(n) = T(n/2) + O(1)

y como logB(A) = C, log2(1) = 0, la ecuacion tiende a:
O(n^C.logn) = O(logn).


La complajidad temporal es O(logn)
La complejidad espacial es O(n), ya que paso por parametro una copia de n/2 elementos. O(n/2) = O(n)

"""

