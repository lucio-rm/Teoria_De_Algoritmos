"""
Enunciado 15:
Es el año 1700, y la pirata Barba-ra Verde atacó un barco de la Royal British Shipping & Something, que transportaba una importante piedra preciosa de la corona británica. Al parecer, la escondieron en un cofre con muchas piedras preciosas falsas, en caso de un ataque. Barba-ra Verde sabe que los refuerzos británicos no tardarán en llegar, y deben huir lo más rápido posible. El problema es que no pueden llevarse el cofre completo por pesar demasiado. Necesita encontrar rápidamente la joya verdadera. La única forma de descubrir la joya verdadera es pesando. Se sabe que la joya verdadera va a pesar más que las imitaciones, y que las imitaciones pesan todas lo mismo. Cuenta con una balanza de platillos para poder pesarlas (es el 1700, no esperen una balanza digital).

Indicar la posición de la Joya verdadera.

En el ejemplo de código inicial de la actividad mostramos un llamado de ejemplo a la función balanza, a la que se le deben pasar los dos conjuntos de joyas a verificar. La cantidad de joyas en cada conjunto debe ser la misma, para que el resultado de la balanza de platillos nos dé información.
Si los dos platillos pesan lo mismo, balanza devuelve 0.
Si el primer platillo es más pesado, balanza devuelve 1.
Si el segundo platillo es más pesado, balanza devuelve -1.

"""

from balanza import *

"""
cambio el planteo.
"""
def encontrar_joya(grupo):
    if not grupo: 
        return None
    return _joya_rec(grupo, 0, len(grupo) - 1)

def _joya_rec(grupo, ini, fin):
    # caso base: queda una sola joya
    if ini == fin:
        return ini

    #cantidad de elementos en el rango actual
    n = fin - ini + 1
    
    # cuantos elementos van a ir a cada lado de la balanza
    mitad = n // 2
    
    # armo los grupos recortando el arreglo original para pasárselos a la balanza
    #lado izquierdo: desde 'ini' hasta 'ini + mitad' (sin incluir)
    grupo_izq = grupo[ini : ini + mitad]
    # lado derecho: los siguientes 'mitad' elementos
    grupo_der = grupo[ini + mitad : ini + 2 * mitad]
    
    resultado = balanza(grupo_izq, grupo_der)
    
    if resultado == 0:
        # pesan igual: la joya verdadera es la que quedó afuera (el último elemento del rango)
        return fin
    elif resultado > 0:
        # el grupo izquierdo es más pesado: la joya está entre 'ini' y 'ini + mitad - 1'
        return _joya_rec(grupo, ini, ini + mitad - 1)
    else:
        # el grupo derecho es más pesado: la joya está entre 'ini + mitad' y 'ini + 2*mitad - 1'
        return _joya_rec(grupo, ini + mitad, ini + 2 * mitad - 1)

"""
Complejidad:
teorema maestro, bla bla bla

"""