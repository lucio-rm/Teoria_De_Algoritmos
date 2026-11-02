"""
Enunciado ejercicio 13:
(★★) Debido a la trágica situación actual, es necesario realizar tests para detectar si alguna persona está contagiada de COVID-19.
El problema es que los insumos tienden a ser bastante caros, y no vivimos en un país al que los recursos le sobren.

Supongamos que por persona se toma más de una muestra (lo cual es cierto, pero a fines del ejercicio supongamos que son muchas muestras), y que podemos realizar un testeo a más de una persona al mismo tiempo mezclando las muestras (lo cual también es cierto): 
determinamos un conjunto de personas a testear, obtenemos una muestra de cada una de ellas, las “juntamos”, y al conjunto le realizamos el test. 
Si el test resulta negativo, implica que todas las personas testeadas en conjunto resultaron negativas. 
Si resulta positivo, implica que al menos una de las personas testedas resulta positiva.

Suponer que existe una función pcr(grupo), que devuelve true si al menos una persona del grupo es COVID-positivo, y false en caso contrario (los grupos pueden estar formados por 1 o más personas). 
Suponer que la positividad es extremadamente baja, e inclusive pueden suponer que va a haber una única persona contagiada (por simplicidad).

Implementar un algoritmo que dado un conjunto de n personas, devuelva la o las personas contagiadas, utilizando la menor cantidad de tests posibles (considerando la notación Big Oh). 
En dicha notación, ¿cuántos tests se estarán utilizando?

Pueden considerar que habrá una única persona contagiada, pero esto no cambiará el análisis a realizar.

"""
"""
planteo:
- El objetivo primario es MINIMIZAR LA CANTIDAD DE TESTS (llamadas a pcr()).
- Sabemos por enunciado que hay un único contagiado (esto es vital, si hubiese más 
  de uno, este D&C no garantiza encontrarlos a todos en O(log n)).
- Dividimos el grupo en dos mitades: Izquierda y Derecha.
- Regla de oro: TESTEAMOS SOLO UNA MITAD. Si le hacemos el test a la mitad 
  Izquierda y da positivo, el contagiado está ahí. 
- La magia matemática: Si la mitad Izquierda da negativo, ¡NO NECESITAMOS 
  TESTEAR LA DERECHA! Por descarte absoluto, el contagiado DEBE estar en la Derecha.
  Nos ahorramos un test por nivel de recursión.
"""

def pcr(grupo):
    return True 

def _contagiado_rec(grupo, ini, fin):
    # caso base: Si queda 1 sola persona, la encontramos. Cero tests requeridos aquí.
    if ini == fin:
        return grupo[ini]

    mid = (ini + fin) // 2
    
    # Hacemos un solo test por nivel recursivo.
    # El slicing aquí genera O(n) temporal, pero el problema evalúa 
    # la cantidad de tests = llamadas a pcr().
    if pcr(grupo[ini:mid + 1]):
        # Dio positivo, buscamos en esta mitad.
        return _contagiado_rec(grupo, ini, mid)
    else:
        # Dio negativo. Por inferencia, está en la otra mitad. No gastamos test.
        return _contagiado_rec(grupo, mid + 1, fin)

def buscar_contagiado(grupo):
    if not grupo:
        return None
    return _contagiado_rec(grupo, 0, len(grupo) - 1)

"""
Justificacion de complejidad:
- Operaciones (Tests): En cada llamado recursivo, partimos el problema a la mitad 
  y realizamos EXACTAMENTE 1 test. 
  La cantidad de tests está dada por: T(n) = T(n/2) + 1. 
  Por Teorema Maestro (A=1, B=2, C=0), esto es O(log n) tests.
- Complejidad Espacial: O(log n) por la pila de llamadas recursivas.
"""