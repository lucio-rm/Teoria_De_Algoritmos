from algoritmo import juego

ESPERADO_20 = 0
ESPERADO_25 = 0
ESPERADO_50 = 0
ESPERADO_100 = 0
ESPERADO_1000 = 0
ESPERADO_10000 = 0
ESPERADO_20000 = 0

ESPERADO_50_PROPIO = 0
ESPERADO_150_PROPIO = 0
ESPERADO_500_PROPIO = 0
ESPERADO_750_PROPIO = 0
ESPERADO_15000_PROPIO = 0

def leer_archivos(ruta):
    with open(ruta, "r") as archivo:
        archivo.readline()
        numeros = archivo.readline()
        arreglo = [int(n) for n in numeros.split(";")]
        return arreglo

def test(esperados, rutas):
    obtenidos = []
    for ruta in rutas:
        obtenidos.append(juego(leer_archivos(ruta)))
        
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
    esperados = [ESPERADO_20, ESPERADO_25, ESPERADO_50, ESPERADO_100, ESPERADO_1000, ESPERADO_10000, ESPERADO_20000]
    rutas = ["tp2_test/catedra/20.txt", "tp2_test/catedra/25.txt", "tp2_test/catedra/50.txt", "tp2_test/catedra/100.txt", "tp2_test/catedra/1000.txt", "tp2_test/catedra/10000.txt", "tp2_test/catedra/20000.txt"]
    esperados_propios = [ESPERADO_50_PROPIO, ESPERADO_150_PROPIO, ESPERADO_500_PROPIO, ESPERADO_750_PROPIO, ESPERADO_15000_PROPIO]
    rutas_propias = ["tp2_test/propios/50_propio.txt", "tp2_test/propios/150_propio.txt", "tp2_test/propios/500_propio.txt", "tp2_test/propios/750_propio.txt", "tp2_test/propios/15000_propio.txt"]
    print("---- Test Proporcionados ----\n")
    test(esperados, rutas)
    print("\n---- Test Propios ----\n")
    test(esperados_propios, rutas_propias)
            
if __name__ == "__main__":
    main()