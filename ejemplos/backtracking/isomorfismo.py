def distribucion_aristas(grafo):
    grados = {}
    vertices_x_grado = {}
    total = 0
    for v in grafo:
        grados[v] = len(grafo[v])
        if len(grafo[v]) not in vertices_x_grado:
            vertices_x_grado[len(grafo[v])] = 0
        vertices_x_grado[len(grafo[v])] += 1
        total += len(grafo[v])
    return grados, vertices_x_grado, total // 2


def posibilidades(grados1, grados2):
    posibles = {}
    for v in grados1:
        grado = grados1[v]
        posibles[v] = set()
        for w in grados2:
            if grado == grados2[w]:
                posibles[v].add(w)
    return posibles


def son_isomorfismos(grafo1, grafo2):
    if len(grafo1) != len(grafo2):
        return None
    grados1, vertices_x_grado1, total1 = distribucion_aristas(grafo1)
    grados2, vertices_x_grado2, total2 = distribucion_aristas(grafo2)
    if total1 != total2:
        return None
    if vertices_x_grado1 != vertices_x_grado2:
        return None

    return _son_isomorfismos_rec(grafo1, grafo2, posibilidades(grados1, grados2), {})


def _son_isomorfismos_rec(grafo1, grafo2, posib, asignaciones):
    if len(asignaciones) == len(grafo1):
        return asignaciones

    siguiente = min(posib, key=lambda v: len(posib[v]))
    if posib[siguiente] == 0:
        return None

    for asig in posib[siguiente]:
        asignaciones[siguiente] = asig
        posibilidades_nuevas = posib.copy()

        for v in grafo1:
            if asig in posib[v]:
                posibilidades_nuevas[v].remove(asig)

        ady_asig = set(grafo2.adyacentes(asig))
        for w in grafo1.adyacentes(siguiente):
            if w not in asignaciones:
                posibilidades_nuevas[w] = posibilidades_nuevas[w] & ady_asig

        solucion = _son_isomorfismos_rec(grafo1, grafo2, posibilidades_nuevas, asignaciones)
        if solucion is not None:
            return solucion
        del asignaciones[siguiente]

    return None


def son_isomorfismos_sencillito(grafo1, grafo2):
    if len(grafo1) != len(grafo2):
        return None
    grados1, vertices_x_grado1, total1 = distribucion_aristas(grafo1)
    grados2, vertices_x_grado2, total2 = distribucion_aristas(grafo2)
    if total1 != total2:
        return None
    if vertices_x_grado1 != vertices_x_grado2:
        return None


    return _son_isomorfismos_sencillito_rec(grafo1.obtener_vertices(), 0, grafo1, grafo2, {})


def asignacion_valida(actual, grafo1, grafo2, asignaciones):
    for w in grafo1:
        if w in asignaciones:
            if grafo1.hay_arista(actual, w) != grafo2.hay_arista(asignaciones[actual], asignaciones[w]):
                return False
    return True


def _son_isomorfismos_sencillito_rec(vertices, indice, grafo1, grafo2, asignaciones):
    if indice == len(grafo1):
        return asignaciones

    actual = vertices[indice]
    for posibilidad in grafo2:
        asignaciones[actual] = posibilidad
        if asignacion_valida(actual, grafo1, grafo2, asignaciones):
            solucion = _son_isomorfismos_sencillito_rec(vertices, indice + 1, grafo1, grafo2, asignaciones)
            if solucion is not None:
                return solucion
        del asignaciones[actual]
    return None


def subsetsum(elementos, n):
    elementos = list(filter(lambda elem: elem <= n, elementos))
    sol, suma = _subsetsum(elementos, 0, n, sum(elementos), ([], 0), ([], 0))
    return sol


def _subsetsum(elementos, indice, n, suma_restantes, solucion_parcial, sol_optima):
    if indice == len(elementos):
        return sol_optima

    actual, suma = solucion_parcial
    optimo_actual, suma_optima = sol_optima
    if suma + suma_restantes <= suma_optima:
        return sol_optima
    if suma > suma_optima:
        sol_optima = (suma, solucion_parcial[:])

    elem = elementos[indice]
    suma_restantes -= elem
    if suma + elem <= n:
        actual.append(elem)
        suma += elem
        if suma == n:
            return (actual, suma)
        else:
            sol_optima = _subsetsum(elementos, indice + 1, n, suma_restantes, (actual, suma), sol_optima)
        actual.pop()
    return _subsetsum(elementos, indice + 1, n, suma_restantes, solucion_parcial, sol_optima)

