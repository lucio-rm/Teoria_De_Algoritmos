"""
Enunciado ej9:
Se tiene una lista de materias que deben ser cursadas en el mismo cuatrimestre, cada materia está representada con una lista de cursos/horarios posibles a cursar (solo debe elegirse un horario por cada curso). Cada materia puede tener varios cursos. Implementar un algoritmo de backtracking que devuelva un listado con todas las combinaciones posibles que permitan asistir a un curso de cada materia sin que se solapen los horarios. Considerar que existe una función son_compatibles(curso_1, curso_2) que dados dos cursos devuelve un valor booleano que indica si se pueden cursar al mismo tiempo.

"""
"""
planteo:

alta paja pensar este.

por cada posible_solución tengo que analizar que no se solapeen entrer comisiones de otras materias y elegir varia cantidad y seguir asi y que pase cierto "filtro" , no?

como lo ves realizarlo de esa manera?



"""

"""
planteo ej.9:
- tengo una lista de materias. cada materia tiene una lista de cursos posibles. debo elegir solo UNO por materia.
- esto no es un grafo directamente, es el clásico combinatorio: en la materia 0, pruebo el curso 0. paso a la materia 1, pruebo sus cursos. si se solapan, lo descarto y pruebo el siguiente.
- al igual que las N reinas, avanzo por "materia" (como las filas).
- llevo una "solucion_parcial" con los cursos que voy anotando. para validar un curso nuevo, uso la funcion que me dieron y chequeo contra todo lo que ya tengo en mi solucion_parcial.
- mi caso base: la cantidad de cursos anotados es igual a la cantidad total de materias. cuando esto pasa, lo guardo en una lista "soluciones_finales" (haciendo una copia de la lista parcial).
- luego de la llamada recursiva, SIEMPRE saco el curso de la solucion parcial para que el bucle intente con el proximo curso de esa materia. acá devuelvo siempre una lista llena al final, no corto con "return True".
"""

from compatibles import *

def _curso_es_valido(curso_nuevo, solucion_parcial):
    for curso_anotado in solucion_parcial:
        if not son_compatibles(curso_nuevo, curso_anotado):
            return False
    return True

def _combinaciones_rec(materias, indice_materia, solucion_parcial, combinaciones_finales):
    # caso base: anotamos 1 curso por cada materia
    if indice_materia == len(materias):
        combinaciones_finales.append(solucion_parcial[:]) # ojo acá, siempre copia
        return
        
    for curso in materias[indice_materia]:
        if _curso_es_valido(curso, solucion_parcial):
            solucion_parcial.append(curso)
            
            _combinaciones_rec(materias, indice_materia + 1, solucion_parcial, combinaciones_finales)
            
            # backtracking (necesitamos encontrar TODAS, asi que siempre deshacemos)
            solucion_parcial.pop()

def obtener_combinaciones(materias):
    combinaciones_finales = []
    _combinaciones_rec(materias, 0, [], combinaciones_finales)
    return combinaciones_finales

"""
Justificacion de la complejidad
- temporal: O(K^M * M). Sea M la cantidad de materias, y K la cantidad máxima de cursos que tiene una materia. En cada nivel de recursión iteramos sobre K ramas posibles. Como la profundidad es M, exploramos K^M hojas. Por cada curso que queremos agregar, lo verificamos contra los que ya tenemos en la solución parcial (costo O(M)).
- espacial: O(M) de forma auxiliar. El call stack desciende hasta una profundidad M. La lista "solucion_parcial" pesa O(M). Notar que el espacio ocupado por "combinaciones_finales" dependerá de cuántas soluciones válidas existan, lo cual puede llegar a O(K^M * M) y exceder el espacio de trabajo auxiliar, pero algorítmicamente se evalúa el espacio interno en memoria.
Se podría pre-procesar las compatibilidades para tenerlas en una matriz en memoria O(1) pero la combinatoria general del problema seguirá siendo exponencial.
"""