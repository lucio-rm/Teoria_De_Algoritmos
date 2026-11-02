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
- Hay que encontrar un elemento más pesado usando una balanza.
- Una balanza REQUIERE que ambos lados tengan la misma cantidad de elementos.
- Si la cantidad de joyas es par, dividimos a la mitad y pesamos. La más pesada 
  se queda.
- Si la cantidad es IMPAR (ej: 5), si dividimos a la mitad (2 y 2), nos SOBRA 1.
- Pesamos los dos grupos de 2. 
  - Si pesan lo mismo, ¡la joya es la que apartamos! (Caso ganador temprano).
  - Si uno pesa más, la joya está en ese grupo (y descartamos la apartada).
"""

def balanza(g1, g2):
    return 

def _joya_rec(grupo):
    n = len(grupo)
    
    # Caso base
    if n == 1:
        return grupo[0]

    # Determinamos el tamaño de los grupos a pesar.
    # Si es impar, mid deja al último elemento afuera del pesaje.
    mid = n // 2
    
    grupo_izq = grupo[:mid]
    grupo_der = grupo[mid:2*mid] # Si n=5, mid=2. izq=[0,1], der=[2,3], aisla el [4]
    
    resultado = balanza(grupo_izq, grupo_der)
    
    if resultado == 0:
        # Pesan lo mismo. La joya verdadera es el impar que quedó aislado.
        # Solo ocurre si 'n' era impar.
        return grupo[-1]
    elif resultado > 0:
        # La mitad izquierda es más pesada
        return _joya_rec(grupo_izq)
    else:
        # La mitad derecha es más pesada
        return _joya_rec(grupo_der)

def buscar_joya(grupo):
    if not grupo: return None
    return _joya_rec(grupo)

"""
Justificacion de complejidad:
- Temporal: T(n) = T(n/2) + O(n). 
  NOTA: Si se pasan sub-arreglos usando slices (`grupo[:mid]`), el f(n) es O(n).
  Según el Teorema Maestro (A=1, B=2, C=1): C > log_2(1). 
  La complejidad terminaría siendo O(n).
  Si pasáramos índices (ini, fin) en lugar de crear nuevas listas con slices, 
  f(n) sería O(1), y la complejidad temporal sería O(log n). El enunciado espera 
  la lógica indexada para lograr el O(log n).
"""