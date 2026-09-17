# pre condiciones: recibe una lista de enteros que representa la cantidad de monedas del juego.
# post condiciones: devuelve los puntos ganados por sophia, que siempre va a ganar.
def juego(monedas: list[int]):
    pts_mateo = pts_sophia = 0
    inicio = 0
    fin = len(monedas) - 1
    turno = True #True -> Sophia, False -> Mateo
    
    while inicio <= fin:
        if turno:
            if monedas[inicio] > monedas[fin]:
                pts_sophia += monedas[inicio]
                inicio += 1
            else:
                pts_sophia += monedas[fin]
                fin -= 1
        else:
            if monedas[inicio] >= monedas[fin]:
                pts_mateo += monedas[fin]
                fin -= 1
            else:
                pts_mateo += monedas[inicio]
                inicio += 1
        turno = not turno
    return pts_sophia