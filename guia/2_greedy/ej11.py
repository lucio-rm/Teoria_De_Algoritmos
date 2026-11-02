"""
Enunciado ejercicio 11:
(★★) Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo 'P', por encima del cual se rompen. 
Implementar un algoritmo greedy que, teniendo una lista de pesos de 'n' productos comprados, encuentre la mejor forma de distribuir los productos en la menor cantidad posible de bolsas. 
Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. 

¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. 
Indicar y justificar la complejidad del algoritmo implementado.

"""

"""
planteo (El modelo mental correcto):
1. Estamos frente al "Bin Packing Problem" (Empaquetado de Contenedores). 
2. Rompiendo tu ilusión de P=NP: Este problema es matemáticamente intratable (NP-Hard) para soluciones exactas polinomiales. Tu lógica de un solo ciclo asume que agrupar el primero con el siguiente disponible será óptimo, pero es una trampa cognitiva. No inventaste un algoritmo nuevo, usaste una heurística conocida como "First Fit" (Primer Ajuste).
3. Para hacerlo Greedy y conseguir una *buena aproximación* (aunque no la óptima siempre), la mejor regla es "First Fit Decreasing" (FFD): ordenamos los pesos de mayor a menor y tratamos de meter los más pesados primero en las bolsas abiertas. Si no caben, abrimos otra.

> ELI5 (Ejemplo para un niño de 5 años):
Imagina que tienes que guardar peluches gigantes y canicas pequeñas en cajas. Si empiezas llenando las cajas con las canicas primero, cuando quieras meter el peluche gigante, no entrará y tendrás que usar una caja nueva entera. Pero si guardas el peluche gigante primero, las canicas pequeñas se pueden colar en los espacios huecos que sobraron en esa misma caja.
"""

def cantidad_bolsas(pesos, p):
    # Ordenamos de mayor a menor peso (First Fit Decreasing)
    pesos.sort(reverse=True)
    
    bolsas = [] # Lista donde cada elemento es el peso acumulado en una bolsa
    
    for peso in pesos:
        ubicado = False
        # Buscamos la primera bolsa donde el producto entre
        for i in range(len(bolsas)):
            if bolsas[i] + peso <= p:
                bolsas[i] += peso
                ubicado = True
                break
                
        # Si no entró en ninguna bolsa existente, abrimos una nueva
        if not ubicado:
            bolsas.append(peso)
            
    return len(bolsas)

"""
Justificación Ejercicio 11:
- Complejidad Temporal: O(n^2). Ordenar toma O(n log n). Para cada uno de los 'n' pesos, podríamos llegar a recorrer hasta 'n' bolsas (si todos van en bolsas separadas). Por lo tanto, O(n^2).
- Complejidad Espacial: O(n) para almacenar el peso acumulado de las bolsas.
- ¿Es siempre óptimo?: NO. 
- Contraejemplo irrefutable: 
  Sea P = 10, y los pesos: [6, 5, 4, 3, 2].
  La suma de todo es 20, por lo que el óptimo teórico es 2 bolsas (Caja 1: 6+4=10, Caja 2: 5+3+2=10).
  Tu algoritmo Greedy (FFD) hará esto:
  - Mete el 6 en Bolsa 1.
  - Mete el 5 en Bolsa 2.
  - El 4 no entra con el 6 ni con el 5. Abre Bolsa 3.
  - El 3 entra con el 6 (6+3=9). Bolsa 1 ahora tiene 9.
  - El 2 entra con el 5 (5+2=7). Bolsa 2 ahora tiene 7.
  Resultado Greedy: 3 bolsas. Resultado Óptimo: 2 bolsas. 
  Q.E.D. P sigue siendo distinto de NP.
"""