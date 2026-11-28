import pulp
from pulp import LpAffineExpression as Sumatoria

def juego_pl(tablero):
    n = len(tablero)
    m = len(tablero[0])

    x = []
    for j in range(m):
        x.append(pulp.LpVariable("x" + str(j), cat="Binary"))

    e = []
    for i in range(n):
        e.append(pulp.LpVariable("e" + str(i), cat="Binary"))

    problem = pulp.LpProblem("juego_piedras", pulp.LpMinimize)
    problem += Sumatoria([(e[i], 1) for i in range(n)])

    for i in range(n):
        terminos = []
        cant_celestes = 0
        for j in range(m):
            if tablero[i][j] == "V":
                terminos.append((x[j], 1))
            elif tablero[i][j] == "C":
                terminos.append((x[j], -1))
                cant_celestes += 1

        problem += Sumatoria(terminos) + cant_celestes + e[i] >= 1

    problem.solve(pulp.PULP_CBC_CMD(msg=False)) # Esto es unicamente para que no muestre un monton de mensajes por consola

    colores = []
    for j in range(m):
        if pulp.value(x[j]) == 1:
            colores.append("V")
        else:
            colores.append("C")

    return colores

