from utils.algoritmo import juego
from utils.leer_archivo import leer_archivos

ESPERADO_20 = (5234, 4264)
ESPERADO_25 = (7491, 6523)
ESPERADO_50 = (14976, 13449)
ESPERADO_100 = (28844, 22095)
ESPERADO_1000 = (1401590, 1044067)
ESPERADO_2000 = (2869340, 2155520)
ESPERADO_10000 = (34107537, 25730392)

ESPERADO_50_PROPIO = (13915, 11184)
ESPERADO_150_PROPIO = (40709, 30392)
ESPERADO_500_PROPIO = (141120, 105697)
ESPERADO_700_PROPIO = (198645, 153182)
ESPERADO_1000_PROPIO = (280649, 207442)
ESPERADO_5000_PROPIO = (1432796, 1085973)


def test(esperados, rutas):
    obtenidos = []
    for ruta in rutas:
        sophia, mateo = juego(leer_archivos(ruta))
        obtenidos.append((sophia, mateo))
        
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
    esperados = [ESPERADO_20, ESPERADO_25, ESPERADO_50, ESPERADO_100, ESPERADO_1000, ESPERADO_2000, ESPERADO_10000]
    rutas = ["tp2_test/catedra/20.txt", "tp2_test/catedra/25.txt", "tp2_test/catedra/50.txt", "tp2_test/catedra/100.txt", "tp2_test/catedra/1000.txt", "tp2_test/catedra/2000.txt", "tp2_test/catedra/10000.txt"]
    esperados_propios = [ESPERADO_50_PROPIO, ESPERADO_150_PROPIO, ESPERADO_500_PROPIO, ESPERADO_700_PROPIO, ESPERADO_1000_PROPIO, ESPERADO_5000_PROPIO]
    rutas_propias = ["tp2_test/propios/50_propio.txt", "tp2_test/propios/150_propio.txt", "tp2_test/propios/500_propio.txt", "tp2_test/propios/700_propio.txt", "tp2_test/propios/1000_propio.txt", "tp2_test/propios/5000_propio.txt"]

    print("\n---- Test Proporcionados ----\n")
    test(esperados, rutas)
    print("\n---- Test Propios ----\n")
    test(esperados_propios, rutas_propias)
    print("\n---- Test Finalizados ----\n")
if __name__ == "__main__":
    main()