"""
Enunciado ejercicio 15:
(★★) Se tiene una colección de n libros con diferentes espesores, que pueden estar entre 1 y 'n' (valores no necesariamente enteros). Tu objetivo es guardar esos libros en la menor cantidad de cajas. Todas las cajas disponibles son de la misma capacidad 'L' (se asegura que L≥n).
Obviamente, no podés partir un libro para que vaya en múltiples cajas, pero sí podés poner múltiples libros en una misma caja, siempre y cuando los espesores no superen esa capacidad L. 

Implementar un algoritmo Greedy que obtenga las cajas, tal que se minimicen la cantidad de cajas a utilizar. 

Indicar y justificar la complejidad del algoritmo implementado. 
Justificar por qué se trata de un algoritmo greedy. 
¿El algoritmo propuesto encuentra siempre la solución óptima? Justificar. 
¿Qué cambios aplicarías si supieras que los espesores sólo fueran números enteros de un rango acotado? Describir cómo afecta a la complejidad, y a su optimalidad.

"""

"""
planteo:

estoy pensandolo algo parecido a subset sum.

osea tendría que ser óptimo porque si os i ya tenemos toda la colección de libros.


ahora el temita esta:
- como hacerlo/pensarlo de manera greedy
- como no cagarla para no hacerlo en O(n²)

regla greedy:
    - si el libro no pasa la capacidad, lo pongo.
    - si pasa, agrego otra caja.


"""

def cajas(capacidad, libros):
    if not libros:
        return []
    
    # cada caja va a ser una lista con los pesos individuales de sus libros
    lista_cajas = []
    
    for peso_libro in libros:
        ubicado = False
        
        # busco la primera caja donde entre el libro actual
        for fila in range(len(lista_cajas)):
            caja_actual = lista_cajas[fila]
            
            # sumo los libros que ya tiene la caja para ver si hay espacio
            if sum(caja_actual) + peso_libro <= capacidad:
                caja_actual.append(peso_libro)
                ubicado = True
                break
                
        # si no entró en ninguna caja existente, abrimos una nueva caja
        if not ubicado:
            lista_cajas.append([peso_libro])
            
    return lista_cajas


"""
Justificación:

- Complejidad: 
    - temporal: recorre los N libros, y si la caja no esta llena, recorre la lista de C cajas. complejidad = O(n.C). como sé que C siempre va a ser <= n, complejidad temporal: O(n²)
    - espacial: a lo sumo, O(n), siendo n la cantidad de libros. si todos los libros son de espesor == capacidad, estamo en la shit.
    
- Greedy:

    - regla Greedy: siempre que pueda, meto un libro en la caja. y si no, agarro otra caja. eso va a hacer que agarre la menor cantidad de cajas.
    - optimalidad: en el estado actual (agarro un libro), meto el libro en la prier caja que pueda. y sino, agarro otra caja. en la sucesion de óptimos locales (optimo local = haber podido meter un libro en la caja siempre que pueda no agarrar otra), va a significar el óptimo global.
Óptimalidad real: no es óptimo. porque siempre que puede mete en la primer caja sin visión de la BIG Picture, por lo que ignora si pudo haber metido en otra caja para que el proximo libro a agarrar entre en la que iba a seleccionar el. Se podría arreglar esto con Programación Dinámica, o no?. a no ser que se encuentre un algoritmo mejor, no es óptimo.

"""

