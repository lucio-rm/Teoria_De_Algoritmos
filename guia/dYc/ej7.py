"""
Enunciado ejercicio 7:
(★★) Implementar un algoritmo que dados n puntos en un plano, busque la pareja que se encuentre más cercana, por división y conquista, con un orden de complejidad mejor que O(n²). 
Justificar la complejidad del algoritmo mediante el teorema maestro. Se puede asumir que ningún par de puntos tienen la misma coordenada x o y.

"""

"""
planteo:

no se por qué me recontra cuesta entender estos ejericicios. y recién son 2 estrellas/1 estrella (los de 3 para adelante tienen la dificultad de parciales y finales)



voy a copiar y pegar lo que tengo en los resumenes que vimos en clase:


Buscando puntos más cercanos en 2 dimensiones:

un algoritmo sencillo lo hace en O(n²). para hacerlo en menos:

- resuelvo el problema con D&C.
Asumimos que ningún par de puntos tienen misma coordenada x0y0 (no sé por qué) 
- obtengo la pareja más cercana del lado izquierdo, luego otra del lado derecho, y después
en tiempo lineal buscar los más cercanos ----> O(nlogn)

# caso base: tenes 2 o 3 puntos


- Ordenas los puntos sobre el eje x e y. (Px Py). 
- Del Px( puntos ordenados por coord. x) mandas (de una 'x' de lonte vas comparando y listo) lado izq al QxQy, lado der RxRy
Teniendo Qxy y Rxy listo, llamas recursivamente a los puntos mas cercanos de cada lado. El menor de ellos va a liderar la distancia 'd'. Falta comparar los que estan entre planos (lados)
- Entre lados, agarro sólo los menores a . (desde el centro)
- Si en ese "cajon" existe un par de puntos que estén a menos de dist. d estan a lo sumo 15 posiciones de diferencia en Sy (Sy es el cajon imaginario creo)
--> Para cada punto ver los 15 sgtes., es suficiente. --> num. constante.
"""

# def closest_pairs_rec(px, py):
#     if len(px) <= 3:
#         return # el minimo de comparar cada punto
#     Construir Qx, Qy, Rx, Ry (O(n))

#     q0, q1 = closest_pairs_rec(Qx, Qy)
#     r0, r1 = closest_pairs_rec(Rx, Ry)
#     d = min(dist(q0, q1), dist(r0, r1))

#     x* = máxima coordenada x de Qx
#     S = puntos de P que están a distancia <= d de la recta x = x*
#     Construir Sy (O(n))
#     por cada punto s de Sy computar distnacia contra los siguientes 15 puntos quedarse con s y s' que minimizan esa distancia
#     if dist(s, s') < d: return s, s'
#     elif dist(q0, q1) < dist(r0, r1) : return q0, q1
#     else: return r0, r1

import math

#medio ignorar la de generar_puntos, es para testear (vos, gemini, dejamela. poneme que es para tests)
import random
def generar_puntos(n):
    generadosx = set()
    generadosy = set()
    resultado = []

    for i in range(n):
        while True:
            x, y = random.randint(0, 100), random.randint(0,100)
            if x not in generadosx and y not in generadosy:
                resultado.append((x,y))
                generadosx.add(x)
                generadosy.add(y)
                break
    return resultado



def distancia(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def comparacion_3(px):
    if len(px) == 2:
        return px[0], px[1]
    d01 = distancia(px[0], px[1])
    d02 = distancia(px[0], px[2])
    d12 = distancia(px[1], px[2])

    if d01 <= d02 and d01 <= d12:
        return px[0], px[1]
    elif d02 <= d01 and d02 <= d12:
        return px[0], px[2]
    else:
        return px[1], px[2]

def construir_qyry(py, x_quiebre):
    qy = []
    ry = []
    for punto in py:
        if punto[0] < x_quiebre:
            qy.append(punto)
        else:
            ry.append(punto)
    return qy, ry

def construir_sy(py, x_quiebre, d):
    sy = []
    for punto in py:
        if abs(punto[0] - x_quiebre) < d:
            sy.append(punto)
    return sy

def puntos_mas_cercanos_dyc(px, py):
    if len(px) <= 3:
        return comparacion_3(px)
    mitad = len(px) // 2
    qx = px[:mitad]
    rx = px[mitad:]

    qy, ry = construir_qyry(py, px[mitad][0])
    q0, q1 = puntos_mas_cercanos_dyc(qx, qy)
    r0, r1 = puntos_mas_cercanos_dyc(rx, ry)

    if distancia(q0, q1) < distancia(r0, r1):
        d = distancia(q0, q1)
        min0 = q0
        min1 = q1
    else:
        d = distancia(r0, r1)
        min0 = r0
        min1 = r1

    sy = construir_sy(py, px[mitad][0], d)

    for i in range(len(sy)):
        for j in range(i+1, min(i+16, len(sy))):
            if distancia(sy[i], sy[j]) < d:
                d = distancia(sy[i], sy[j])
                min0 = sy[i]
                min1 = sy[j]

    return min0, min1


def mas_cercanos(puntos):
    px = sorted(puntos, key=lambda p: p[0])
    py = sorted(puntos, key=lambda p: p[1])
    p0, p1 = puntos_mas_cercanos_dyc(px, py)
    return p0, p1



"""
COMPLEJIDAD:
crear los arreglos Sy, Qy y Ry te cuesta O(n), lo cual es correcto para mantener la complejidad
T(n) = 2T(n/2) + O(n) = O(nlog n).

"""