"""
Enunciado 08:
Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción


"""

"""
planteo:
lo hago en base peso/valor, y guardo el mas grande.
no es optimo. a no ser que sean divisibles.

"""
def mochila(elementos, W):
    # creo tuplas con (ratio, valor, peso, elemento_original)
    elementos_procesados = []
    for i in range(len(elementos)):
        valor = elementos[i][0]
        peso = elementos[i][1]
        ratio = valor / peso
        # guardo el elemento original (valor, peso) en lugar del índice
        elementos_procesados.append((ratio, valor, peso, elementos[i]))
        
    # ordeno de mayor a menor ratio valor/peso
    elementos_procesados.sort(key=lambda x: x[0], reverse=True)
    
    capacidad_restante = W
    elementos_guardados = []
    
    for item in elementos_procesados:
        ratio, valor, peso, objeto_original = item
        # si el elemento cabe entero en la mochila, lo agregamos
        if peso <= capacidad_restante:
            capacidad_restante -= peso
            # agrego el objeto (valor, peso) que espera el corrector
            elementos_guardados.append(objeto_original)
            
    return elementos_guardados
"""
Justificación Greedy y Complejidad (Ej 8):

- Complejidad: O(n log n). Calcular los ratios toma O(n). Ordenar los elementos 
  toma O(n log n). Iterar para guardarlos toma O(n). Total: O(n log n).

- Regla Greedy: Elegir siempre el elemento que tenga la mayor proporción 
  de (Valor / Peso) que aún quepa en la mochila.
  
- ¿Es siempre óptimo?: NO. Para el caso discreto (0-1), donde los elementos no se 
  pueden partir, el algoritmo Greedy falla. Un elemento con gran ratio 
  puede dejar un espacio vacío inútil en la mochila, desperdiciando capacidad. 
  Para garantizar el óptimo aquí se requiere Programación Dinámica.
  
- ¿Diferencias si se pueden fraccionar?: Si se pueden partir (Fractional 
  Knapsack), el algoritmo Greedy SÍ es siempre óptimo. En vez de saltear el 
  elemento que no cabe, simplemente cortamos la fracción exacta que llena el 
  espacio restante de la mochila, logrando eficiencia matemática perfecta.
"""

