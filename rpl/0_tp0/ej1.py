"""
Enunciado ejercicio 1:
La Escuela Nacional 32 "Alan Turing" de Bragado tiene una forma particular de requerir que los alumnos formen fila. En vez del clásico "de menor a mayor altura", lo hacen primero con alumnos yendo con altura decreciente, hasta llegado un punto que empieza a ir de forma creciente, hasta terminar con todos los alumnos.

Por ejemplo las alturas podrían ser 1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23.

1. Implementar una función indice_mas_bajo que dado un arreglo/lista de alumnos(*) que represente dicha fila, devuelva el índice del alumno más bajo, en *tiempo logarítmico*. Se puede asumir que hay al menos 3 alumnos. En el ejemplo, el alumno más bajo es aquel con altura 0.98.

2. Implementar una función validar_mas_bajo que dado un arreglo/lista de alumnos(*) y un índice, valide (devuelva True o False) si dicho índice corresponde al del alumno más bajo de la fila. (Aclaración: esto debería poder realizarse en tiempo constante)

(*)
Los alumnos son de la forma:

alumno {
    nombre (string)
    altura (float)
}
Se puede acceder a la altura de un alumno haciendo varible_tipo_alumno.altura.

Importante: considerar que si la prueba de volumen no pasa, es probable que sea porque no están cumpliendo con la complejidad requerida.

"""

def indice_mas_bajo(alumnos):
    return _busqueda_recursiva(alumnos, 0, len(alumnos) - 1)

def _busqueda_recursiva(arreglo, ini, fin):
    #caso base: cuando los indices se cruzan o igualan, encontramos al mas bajo
    if ini == fin:
        return ini

    medio = (ini + fin) // 2

    # comparo la altura del alumno medio con su vecino derecho
    if arreglo[medio].altura > arreglo[medio + 1].altura:
        # sigo en la bajada: descarto la izquierda y el medio
        return _busqueda_recursiva(arreglo, medio + 1, fin)
    else:
        # empezó a subir: el mínimo puede ser 'medio' o estar a la izquierda
        return _busqueda_recursiva(arreglo, ini, medio)


def validar_mas_bajo(alumnos, indice):
    # Caso borde de si el indice esta fuera de rango
    if indice < 0 or indice >= len(alumnos):
        return False

    # chequeo el vecino izquierdo (si existe)
    if indice > 0 and alumnos[indice].altura > alumnos[indice - 1].altura:
        return False

    # chequeo el vecino derecho
    if indice < (len(alumnos) - 1) and alumnos[indice].altura > alumnos[indice + 1].altura:
        return False

    # si llega hasta aca es que pasa ambos filtros, encuentro el punto más bajo de la fila
    return True



"""
Complejidad del algoritmo:
la funcion validar_mas_bajo es constante (O(1)), acceder al arreglo y consultar la altura cuesta O(1).

la funcion indice_mas_bajo, usa un algoritmo de División y Consquista. Lo que me permite justificar la complejidad con el Teorema Maestro: T(n) = A.T(n/B) + f(n)
siendo,
A: cantidad de llamados recursivos = 1. siempre llama 1 vez, nunca 2 veces.
B: en cuánto parte el problema = 2. parte en lado izquierdo y derecho.
f(n): el costo de dividir y combinar = O(n^C), siendo C el costo de todo lo que no es recursivo = 0.

la ecuación de recurrencia queda como:
T(n) = T(n/2) + O(1)

y como logB(A) = C, log2(1) = 0, la ecuacion tiende a : O(n^Clogn)

la complejidad temporal queda como O(logn)

la complejidad espacial es O(1), ya que simplemente accedo al arreglo y utilizo variables. costo constante.

"""