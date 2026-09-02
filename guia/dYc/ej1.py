"""
Enunciado ejercicio 1:
(★) Se cuenta con un arreglo de enteros ordenado de manera ascendente que contiene exactamente un número duplicado (es decir, todos los demás elementos son distintos, sin duplicados). 
Implementar una función que encuentre dicho número utilizando división y conquista. 
Indicar y justificar la complejidad del algoritmo, utilizando el Teorema Maestro.
"""

"""
planteo:
arreglo ordenado ascendente

tiene UN solo duplicado

encontrar el numero, D&C

eso significa que van a estar desfazados de su indice.

la clave tiene que estar en que estan ordenados.

caso base:
- tengo 1 elemento: revuelvo None (no hay duplicado)
- tengo 2 elementos: si son iguales, devuelvo uno de ellos. si no, devuelvo None



yo tengo que poder "descartar" alguna mitad, solo por el hecho de que estan ordenados. no sé cómo.
no sé por qué

el caso mas basico es mirar uno por uno y cuesta O(n)
tengo que hacerlo en menos.

para eso, logn. descarto una mitad .

    voy al medio.
    si el siguiente o el anterior son iguales al medio, devuelvo el medio.
    
    
arr = [2, 15, 22, 33, 42, 66, 66]


len(arr) = 7
medio = 7 // 2 = 3

arr[medio] = 33
medio a la izq y a la der, != 33.
ahora sabiendo eso, a qué lado llamo? si tengo la misma cantidad de elementos de un lado y del otro?


existe la posibilidad de bajarlo a O(logn)? siento que sí, al saber la info de que esta ordenado. pero no se me ocurre.


"""