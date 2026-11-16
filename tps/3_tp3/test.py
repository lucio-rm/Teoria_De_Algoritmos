# despues borrar:
"""
tiene que correr el
. bt
. PL
. Aproximaciones

contra todos los tests que pongamos (catedra/propio)
"""

from utils.backtracking import juego_bt
from utils.pl import juego_pl
from utils.leer_archivo import leer_archivos

nose = float('habria que representar el tablero¿?')
#no se, los de la catedra busco los que tengan solucion
ESPERADO_3_3 = nose
ESPERADO_6_5 = nose
ESPERADO_12_10 = nose
ESPERADO_20_15 = nose
ESPERADO_30_20 = nose
ESPERADO_35_24 = nose
ESPERADO_45_28 = nose
ESPERADO_150_40 = nose
# HABRA QUE COMPARARLO CON el GENERAL 'Resultados Esperados.txt' ? es por ahi creo.

ESPERADO_X1_X_PROPIO = nose
ESPERADO_X2_X_PROPIO = nose
ESPERADO_X3_X_PROPIO = nose
ESPERADO_X4_X_PROPIO = nose
ESPERADO_X5_X_PROPIO = nose
ESPERADO_X6_X_PROPIO = nose


def test(esperados, rutas):
    obtenidos = []
    for ruta in rutas:
        sophia_bt, mateo_bt = juego_bt(leer_archivos(ruta))
        sophia_pl, mateo_pl = juego_pl(leer_archivos(ruta))
        obtenidos.append((sophia_bt, mateo_bt))
        obtenidos.append((sophia_pl, mateo_pl))
        # claramente esta mal, pero creo que iria por ahi?
        # o hacer 2 tests, uno test_pl, otro test_bt (y tal vez otra func con test_aprox, e ir por ahi? no me acuerdo si aprox. era con sets de datos, creo que si.)
        
    for i in range(len(obtenidos)):
        obtenido = obtenidos[i]
        esperado = esperados[i]
        print(f"Esperado: {esperado}")
        print(f"Obtenido: {obtenido}")
        if obtenido == esperado:
            print("OK")
        else:
            print("ERROR")

def main():
    esperados = [ESPERADO_3_3, ESPERADO_6_5, ESPERADO_12_10, ESPERADO_20_15, ESPERADO_30_20, ESPERADO_35_24, ESPERADO_45_28, ESPERADO_150_40]
    rutas = ["tp2_test/catedra/20.txt", "tp2_test/catedra/25.txt", "tp2_test/catedra/50.txt", "tp2_test/catedra/100.txt", "tp2_test/catedra/1000.txt", "tp2_test/catedra/2000.txt", "tp2_test/catedra/10000.txt"]
    esperados_propios = [ESPERADO_X1_X_PROPIO, ESPERADO_X2_X_PROPIO, ESPERADO_X3_X_PROPIO, ESPERADO_X4_X_PROPIO, ESPERADO_X5_X_PROPIO, ESPERADO_X6_X_PROPIO]
    rutas_propias = ["tp2_test/propios/50_propio.txt", "tp2_test/propios/150_propio.txt", "tp2_test/propios/500_propio.txt", "tp2_test/propios/700_propio.txt", "tp2_test/propios/1000_propio.txt", "tp2_test/propios/5000_propio.txt"]

    print("\n---- Test Proporcionados ----\n")
    test(esperados, rutas)
    print("\n---- Test Propios ----\n")
    test(esperados_propios, rutas_propias)
    print("\n---- Test Finalizados ----\n")
if __name__ == "__main__":
    main()