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
es como que el que haya un duplicado, pero el duplicado es el que tiene covid y tenemos que devolver la posicion.

Voy al medio dl arreglo.
si el arr[ini, medio] tiene UN covid, descarto la mitad derecha.
en caso contrario, descarto mitad izquierda. (ya habiendo analizado que hay uno con covid).


Mi pregunta va, si hay más de una persona contagiada, mi resolución cambiaria. tengo que verificar que en la otra mitad también haya y hasta hacer 2 llamados recursivos.
"""
def pcr(arreglo):
    tienen_covid = True
    return tienen_covid # xd, no nos importa. es para que no me tire error y asumir que estamos  yendo por un camino correcto.
def contagiado(grupo):
    if not pcr(grupo):
        return None # no hay ninguno con covid, valueError.
    cantidad = len(grupo)
    return _contagiado_rec(grupo, 0, cantidad)


def _contagiado_rec(grupo, ini, fin):
    if ini <= fin:
        # si me quedo un elemento o menos, me fijo en ese
        return grupo[ini] if pcr(grupo[ini:fin]) == True else None

    medio = (ini + fin) // 2

    if pcr(grupo[ini:medio]):
        return _contagiado_rec(grupo, ini, medio)
    else:
        return _contagiado_rec(grupo, medio+1, fin)

"""
Complejidad:
temporal: teorema maestro bla bla bla

espacial: mucha mucha muchas copias, asiq ue mucho cmucucuhcuhcuhcu O(N)N enenenenenene

"""