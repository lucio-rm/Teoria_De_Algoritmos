import glob
import os
from utils.pl import juego_pl
from utils.leer_archivo import leer_archivo, construir_solucion

CARPETA = "./tp3_test/propios/manejables"
SALIDA = f"{CARPETA}/resueltos/resueltos_x_archivo.txt"


def vacias(tablero, solucion):
    _, _, _, filas_vacias = construir_solucion(tablero, solucion)
    return len(filas_vacias)


def main():
    rutas = glob.glob(f"{CARPETA}/*.txt")

    tableros = {r: leer_archivo(r) for r in rutas}
    rutas_ord = sorted(rutas, key=lambda r: len(tableros[r]) * len(tableros[r][0]))

    os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
    with open(SALIDA, "w") as salida:
        for i, ruta in enumerate(rutas_ord):
            tablero = tableros[ruta]
            n, m = len(tablero), len(tablero[0])
            print(f"--- Resolviendo {i + 1}/{len(rutas_ord)}: {n}x{m} ---", flush=True)

            pl = vacias(tablero, juego_pl(tablero))

            salida.write(f"{ruta}\n{pl}\n\n")



if __name__ == "__main__":
    main()