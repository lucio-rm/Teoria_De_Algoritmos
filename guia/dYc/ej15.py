"""
Enunciado ejercicio 15:
(★) Es el año 1700, y la pirata Barba-ra Verde atacó un barco de la Royal British Shipping & Something, que transportaba una importante piedra preciosa de la corona británica. 
Al parecer, la escondieron en un cofre con muchas piedras preciosas falsas, en caso de un ataque. Barba-ra Verde sabe que los refuerzos británicos no tardarán en llegar, y deben huir lo más rápido posible. 
El problema es que no pueden llevarse el cofre completo por pesar demasiado. Necesita encontrar rápidamente la joya verdadera. La única forma de descubrir la joya verdadera es pesando. 
Se sabe que la joya verdadera va a pesar más que las imitaciones, y que las imitaciones pesan todas lo mismo. 
Cuenta con una balanza de platillos para poder pesarlas (es el 1700, no esperen una balanza digital).

a. Escribir un algoritmo de división y conquista, para determinar cuál es la verdadera joya de la corona. 
Suponer que hay una función balanza(grupo_de_joyas1, grupo_de_joyas2) que devuelve 0 si ambos grupos pesan lo mismo, mayor a 0 si el grupo1 pesa más que el grupo2, y menor que 0 si pasa lo contrario, y realiza esto en tiempo constante. 

b. Indicar y justificar (adecuadamente) la complejidad de la función implementada.

"""
"""
planteo:
separo en 2 grupos, siendo el arreglo de joyas [ini, fin]
[ini, medio] y [medio, fin]

caso borde: 
    - si el grupo [ini, medio-1] == [medio+1, fin], no hay joya.
    
caso base:
    - si ini <= fin, significa que me queda 1 elemento.
        entonces, ese mismo es la joya.
como se que hay joya, me fijo entre los grupos:
    - si [ini, medio] > [medio+1, fin], descarto mitad derecha
    - sino, descarto mitad izquierda.

"""
def balanza(grupo_de_joyas1, grupo_de_joyas2):
    return 0 if grupo_de_joyas1 == grupo_de_joyas2 else 1 if grupo_de_joyas1 > grupo_de_joyas2 else -1

def hay_joya(grupo):
    cantidad = len(grupo)
    if cantidad == 0:
        return None

    medio = cantidad // 2
    if balanza(grupo[0:medio], grupo[medio+1, cantidad]) == 0:
        return None # no hay joya

    return _diamante_rec(grupo, 0, cantidad)

def _diamante_rec(grupo, ini, fin):
    if ini == fin:
        return grupo[ini] # encontré la joya (queda un solo elemento)

    medio = (ini + fin) // 2

    if balanza(grupo[:medio], grupo[medio+1:fin]) > 0:
        return _diamante_rec(grupo, ini, medio)
    else:
        return _diamante_rec(grupo, medio+1, ini)
    # como sé que hay una joya, no van a ser nunca iguales dos subgrupos.
    

"""
Complejidad:

temporal: busqueda binaria ez teorema maestro etc etc, logn.

espacial: O(n), siendo n la cantidad de joyas. ya que mando siempre copias del grupo original, a la balanza. y como mucho va a analizar/comparar n elementos.

"""