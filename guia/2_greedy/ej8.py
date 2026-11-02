"""
Enunciado ejercicio 8:
(★★) Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. 
Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total. 

Indicar y justificar la complejidad del algoritmo implementado. 
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. 
¿Por qué se trata de un algoritmo Greedy? Justificar
¿Qué diferencias se perciben si en vez de tener que colocar los elementos completos, se pueden fraccionar para nuestra conveniencia?

"""

"""
planteo:
lo hago en base peso/valor, y guardo el mas grande.
no es optimo. a no ser que sean divisibles.


Ejemplo para un niño de 5 años (ELI5):
Tienes una mochila del colegio y quieres llenarla de los dulces más ricos. 
La regla es simple: miras qué dulce te da más felicidad por cada centímetro que 
ocupa. Pero ¡cuidado! Si metes una caja gigante de chocolates enteros que te 
sobresale de la mochila, capaz te pierdes de meter 50 caramelos pequeños que, 
juntos, eran más ricos.

"""

def mochila_greedy(valores, pesos, W):
    # Creamos tuplas con (ratio, valor, peso, indice_original)
    elementos = []
    for i in range(len(valores)):
        ratio = valores[i] / pesos[i]
        elementos.append((ratio, valores[i], pesos[i], i))
        
    # Ordenamos de mayor a menor ratio valor/peso
    elementos.sort(key=lambda x: x[0], reverse=True)
    
    capacidad_restante = W
    ganancia_total = 0
    elementos_guardados = []
    
    for item in elementos:
        ratio, valor, peso, indice = item
        # Si el elemento cabe entero en la mochila, lo agregamos
        if peso <= capacidad_restante:
            capacidad_restante -= peso
            ganancia_total += valor
            elementos_guardados.append(indice)
            
    return elementos_guardados, ganancia_total

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

