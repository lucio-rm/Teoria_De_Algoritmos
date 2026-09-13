import sys

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
                sys.stdout.write("Primera moneda para Sophia;")
            else:
                pts_sophia += monedas[fin]
                fin -= 1
                sys.stdout.write("Última moneda para Sophia;")
        else:
            if monedas[inicio] >= monedas[fin]:
                pts_mateo += monedas[fin]
                fin -= 1
                sys.stdout.write("Última moneda para Mateo;")
            else:
                pts_mateo += monedas[inicio]
                inicio += 1
                sys.stdout.write("Primera moneda para Mateo;")
        turno = not turno
        
    sys.stdout.write(f"\nGanancia de Sophia: {pts_sophia}")
    return pts_sophia
    