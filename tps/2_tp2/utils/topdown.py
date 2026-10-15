# Este algoritmo es la version topdown y sin memoization, el unico fin de este codigo es demostrar en las pruebas las ganancias en complejidad del algoritmo bottomup con tabulacion frente a este algoritmo.
def _juego_rec(monedas, i, j):
    if i == j:
        return monedas[i]
    if i + 1 == j:
        return max(monedas[i], monedas[j])
    
    if monedas[i+1] > monedas[j]:
        ganancia_izq = monedas[i] + _juego_rec(monedas, i+2, j)
    else:
        ganancia_izq = monedas[i] + _juego_rec(monedas, i+1, j-1)
        
    if monedas[i] > monedas[j-1]:
        ganancia_der = monedas[j] + _juego_rec(monedas, i+1, j-1)
    else:
        ganancia_der = monedas[j] + _juego_rec(monedas, i, j-2)
        
    return max(ganancia_der, ganancia_izq)

def juego_rec(monedas):
    if len(monedas) == 0: return 0
    return _juego_rec(monedas, 0, len(monedas)-1)