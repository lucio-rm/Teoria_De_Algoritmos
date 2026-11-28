"""
Validador - Certificador
para demostrar polinomialidad.

Punto 1 de la consigna, leer boceto_estructura linea ~21

(usarlo en los tests para verificar que no algoritmo rompa nada del problema ¿?)
"""


"""
planteo:

certificador polinomial O(n * m) para la versión de decisión del Juego de las Piedras.
Verifica que:
- 1. Las dimensiones coincidan y tablero_solucion sea un subconjunto válido de piedras
del tablero_original (no se agregaron piedras ni se cambiaron colores)
- 2. Ninguna columna tenga piedras de ambos colores ('V' y 'C')
- 3. Toda fila tenga al menos una piedra
"""


def validador_decision(tablero_original: list[list[str]], tablero_solucion: list[list[str]])-> bool:
    n = len(tablero_original)
    if n == 0 or len(tablero_solucion) != n: 
        return False
    m = len(tablero_original[0])

    # verificor subconjunto valido en O(n * m)
    for i in range(n):
        if len(tablero_solucion[i]) != m:
            return False
        for j in range(m):
            orig = tablero_original[i][j]
            sol = tablero_solucion[i][j]
            
            if sol not in (".", "V", "C"):
                return False
            if sol != "." and sol != orig:
                return False
    
    # verificar restriccion de columnas (a lo sumo tiene que haber un color por columna) ~~~~> O(n * m)
    for j in range(m):
        tiene_verde = False
        tiene_celeste = False
        for i in range(n):
            if tablero_solucion[i][j] == "V":
                tiene_verde = True
            elif tablero_solucion[i][j] == "C":
                tiene_celeste = True
            if tiene_verde and tiene_celeste:
                return False
    
    #verifico restriccion de filas (al menos una piedra por fila) en O(n * m)
    for i in range(n):
        tiene_piedra = False
        for j in range(m):
            if tablero_solucion[i][j] in ("V", "C"):
                tiene_piedra = True
                break
            
        if not tiene_piedra:
            return False
    
    return True






