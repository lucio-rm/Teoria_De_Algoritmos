import random

"""
es el pto 5: 
para cada columna j de forma independiente, mantiene las piedras verdes con probabilidad 1/2, sino mantiene las celestes.

complejidad: O(n * m) cuando construimos el tablero resultante 
(O(m) la decisión).
"""
def aprox_gringo_hinz(tablero: list[list[str]]) -> list[str]:
    m = len(tablero[0]) if tablero else 0
    colores_col = ["V" if random.random() < 0.5 else "C" for _ in range(m)]
    return colores_col





"""
pto 7 (el de Greedy):
para cada columna j (sucesion de optimo local), elige el color ('V' o 'C') que cubra la mayor cantidad de filas que siguen vacias
costo O(n * m)
"""
def aprox_greedy(tablero: list[list[str]]) -> list[str]:
    n = len(tablero)
    m = len(tablero[0]) if n > 0 else 0
    fila_cubierta = [False] * n
    colores_col = ["-"] * m
    
    for j in range(m):
        ganancia_v = 0
        ganancia_c = 0
        
        for i in range(n):
            if not fila_cubierta[i]:
                if tablero[i][j] == "V":
                    ganancia_v += 1
                elif tablero[i][j] == "C": 
                    ganancia_c += 1
    
        if ganancia_v == 0 and ganancia_c == 0:
            # si no cubre filas nuevas, elegimos el color que mas veces aparece en  la columna
            cant_v = sum(1 for i in range(n) if tablero[i][j] == "V")
            cant_c = sum(1 for i in range(n) if tablero[i][j] == "C")
            elegido = "V" if cant_v >= cant_c else "C"
        else:
            elegido = "V" if ganancia_v >= ganancia_c else "C"
    
        colores_col[j] = elegido
        for i in range(n):
            if tablero[i][j] == elegido:
                fila_cubierta[i] = True
    
    return colores_col



"""
pto 7 (ahora por pricing method porque somos unos cracks):
un greedy premium

la idea es que cada fila no cubierta i con k_i piedras que le quedan en las columnas que le siguen tiene un precio de urgencia p_i = 2^(-k_i) * leer teoría abajo de todo
(aca es como lod e priority que habiamos hecho en sisop)

en cada columna j se elige el color que maximice el precio total salvado.

complejidad: O(n * m).
"""

def aprox_pricing_method(tablero: list[list[str]]) -> list[str]:
    n = len(tablero)
    m = len(tablero[0]) if n > 0 else 0
    fila_cubierta = [False] * n 
    
    piedras_restantes = [sum(1 for j in range(m) if tablero[i][j] in ("V",  "C")) for i in range(n)]
    colores_col = ["-"] * m
    
    for j in range(m):
        precio_v = 0.0
        precio_c = 0.0
    
        for i in range(n):
            celda = tablero[i][j]
            if not fila_cubierta[i] and celda in ("V", "C"):
                # le aplico el precio (la formula de arriba) a las oportunidades que faltan
                peso = 2.0 ** (-piedras_restantes[i])
    
                if celda == "V":
                    precio_v += peso
                else:
                    precio_c += peso
    
        elegido = "V" if precio_v >= precio_c else "C"
        colores_col[j] = elegido
    
    
        for i in range(n):
            if tablero[i][j] in ("V", "C"):
                piedras_restantes[i] -= 1
                if tablero[i][j] == elegido:
                    fila_cubierta[i] = True

    
    return colores_col




"""
*
Teoría (general, no sólo de este problema) del por qué exponencial negativa: 
Aviso ultrasound (INVESTIGADO CON IA ---->Mark Zumbebebemberg)


es muy común en algoritmos de optimización. 
Se usa una base exponencial como (2^{-k_{i}}) para garantizar una jerarquía de prioridades estricta donde los elementos más urgentes siempre superen a cualquier combinación de elementos menos urgentes.

usar (2^{-k_{i}})
razones matemáticas y computacionales:
• En el sistema binario, una potencia de 2 es mayor que la suma de todas las potencias anteriores ((2^n > sum_{j=0}^{n-1} 2^j)). Al usar exponentes negativos, si un ítem (i) tiene mayor urgencia (es decir, un (k_{i}) más pequeño), su peso (2^{-k_{i}}) será siempre mayor que la suma de los pesos de todos los ítems con menor urgencia ((k_j > k_i)).
• Control de holguras (slacks). Si (k_{i}) representa el tiempo restante hasta una fecha límite (deadline), cuando (k_i = 0) el precio llega a su máximo ((2^0 = 1)). A medida que hay más tiempo de sobra ((k_{i}) crece), el precio cae drásticamente hacia cero sin volverse negativo.
• Eficiencia computacional. En arquitecturas de computadoras que trabajan en binario, multiplicar o dividir por potencias de 2 equivale a un simple desplazamiento de bits (bit-shifting). Esto hace que los cálculos y representaciones en punto flotante sean exactos y muy rápidos.

Ejemplos de cómo escala el precio

Para ver la diferencia entre niveles de urgencia, observa cómo cambia el valor según el parámetro (k_{i}) (asumiendo que un (k_{i}) menor significa mayor urgencia):

Nivel ((k_{i}))	Fórmula	    Precio 	Significado práctico
0	            (2^{0}) 	1.000	Urgencia máxima (vencimiento inmediato).
1	            (2^{-1})    0.500	Alta urgencia (valelamitadqu elnivel 0).
2	            (2^{-2})	0.250	Urgencia media.
3	            (2^{-3})	0.125	Urgencia baja.
10	            (2^{-10})	0.00097	Casi despreciable frente a los primeros niveles.

"""