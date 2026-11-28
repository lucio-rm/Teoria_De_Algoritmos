import random

ENCABEZADO = "# Tablero de n filas y m columnas. Cada línea es una fila: '.' es una celda vacía, 'V' una piedra verde y 'C' una piedra celeste\n"

def generar_tablero(n, m, densidad):
    tablero = []

    for _ in range(n):
        fila = ""

        for _ in range(m):
            if random.random() < densidad:
                fila += random.choice(["V", "C"])
            else:
                fila += "."

        tablero.append(fila)

    return tablero

def generar_tablero_dificil(n, m, piedras_por_fila):
    k = min(piedras_por_fila, m)
    tablero = []
    for _ in range(n):
        fila = ["."] * m
        for col in random.sample(range(m), k):
            fila[col] = random.choice(["V", "C"])
        tablero.append("".join(fila))
    return tablero

def generar_familia_exponencial(carpeta, m_min, m_max, factor_n, piedras_por_fila, reps):
    random.seed(12345)

    for m in range(m_min, m_max + 1):
        n = factor_n * m
        for rep in range(reps):
            tablero = generar_tablero_dificil(n, m, piedras_por_fila)
            with open(f"{carpeta}/m{m:02d}_n{n}_r{rep}.txt", "w") as archivo:
                archivo.write(ENCABEZADO)
                archivo.write("\n".join(tablero))

def generar_familia(carpeta, k, m_min, m_max, n_max, p, dens_min, dens_max):
    extra = n_max - m_max

    for i in range(k):
        t = i / (k - 1)
        m_f = m_min + (m_max - m_min) * t
        m = round(m_f)
        n = round(m_f + extra * t**p)
        densidad = random.uniform(dens_min, dens_max)

        tablero = generar_tablero(n, m, densidad)

        with open(f"{carpeta}/{n}_{m}.txt", "w") as archivo:
            archivo.write(ENCABEZADO)
            archivo.write("\n".join(tablero))

def main():
    generar_familia_exponencial("./tp3_test/propios/manejables", 4, 35, 3, 2, 3)

    #generar_familia("./tp3_test/propios/masivos", 70, 100, 2000, 2000, 2, 0.1, 0.4)

if __name__ == "__main__":
    main()