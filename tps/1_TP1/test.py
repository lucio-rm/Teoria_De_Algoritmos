from algoritmo import juego

ESPERADO_20 = 7165
ESPERADO_25 = 9635
ESPERADO_50 = 17750
ESPERADO_100 = 35009
ESPERADO_1000 = 357814
ESPERADO_10000 = 3550307
ESPERADO_20000 = 7139357

def leer_archivos(ruta):
    with open(ruta, "r") as archivo:
        archivo.readline()
        numeros = archivo.readline()
        arreglo = [int(n) for n in numeros.split(";")]
        return arreglo

def main():
    esperados = [ESPERADO_20, ESPERADO_25, ESPERADO_50, ESPERADO_100, ESPERADO_1000, ESPERADO_10000, ESPERADO_20000]
    rutas = ["tp1_test/20.txt", "tp1_test/25.txt", "tp1_test/50.txt", "tp1_test/100.txt", "tp1_test/1000.txt", "tp1_test/10000.txt", "tp1_test/20000.txt"]
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
            
if __name__ == "__main__":
    main()