from utils.backtracking import juego_bt
from utils.pl import juego_pl
from utils.leer_archivo import leer_archivo, construir_solucion
import glob

def dimensiones_tablero(ruta):
    tablero = leer_archivo(ruta)
    n = len(tablero)
    m = len(tablero[0])
    return n, m

def leer_resultados(ruta):
    resultados = {}
    with open(ruta) as archivo:
        linea = archivo.readline()
        while linea != "":
            nombre = linea.strip()
            if nombre != "":
                cantidad = int(archivo.readline().strip())
                resultados[nombre] = cantidad
            linea = archivo.readline()
    return resultados

def test(resultados: dict, test_catedra: list[str]):
    rutas_ord = sorted(test_catedra, key=lambda r: dimensiones_tablero(r)[0] * dimensiones_tablero(r)[1])
    exitosos = 0
    for i in range(len(rutas_ord)):
        print(f"--- Test: {i} -------------------------")
        tablero = leer_archivo(rutas_ord[i])
        _, _, _, bt = construir_solucion(tablero, juego_bt(tablero))
        _, _, _, pl = construir_solucion(tablero, juego_pl(tablero))
        if len(bt) == resultados[rutas_ord[i]] and len(pl) == resultados[rutas_ord[i]]:
            print(f"--- Test: exitoso ---")
            exitosos += 1
        else:
            print(f"--- Test: fallido ---")
        print(f"Esperado: {resultados[rutas_ord[i]]}, Devuelto: (BT: {len(bt)}) (PL: {len(pl)})\n")
    print(f"Tests: {len(rutas_ord)}/{exitosos}")

def main():
    #print("---- Test del Curso ----\n")
    #ruta_catedra = "./tp3_test/catedra/resueltos/resueltos_x_archivo.txt"
    #test_catedra = glob.glob("./tp3_test/catedra/*.txt")
    #resultados = leer_resultados(ruta_catedra)
    #test(resultados, test_catedra)
    print("\n\n---- Test Propios ----")
    ruta_propia = "./tp3_test/propios/manejables/resueltos/resueltos_x_archivo.txt"
    test_propio = glob.glob("./tp3_test/propios/manejables/*.txt")
    resultados_prop = leer_resultados(ruta_propia)
    test(resultados_prop, test_propio)
    
if __name__ == "__main__":
    main()