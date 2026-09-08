"""
Enunciado 11:
Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen. Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor forma de distribuir los productos en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. Indicar y justificar la complejidad del algoritmo implementado.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""

"""
planteo (El modelo mental correcto):
1. Estamos frente al "Bin Packing Problem" (Empaquetado de Contenedores). 
2. Rompiendo tu ilusión de P=NP: Este problema es matemáticamente intratable (NP-Hard) para soluciones exactas polinomiales. Tu lógica de un solo ciclo asume que agrupar el primero con el siguiente disponible será óptimo, pero es una trampa cognitiva. No inventaste un algoritmo nuevo, usaste una heurística conocida como "First Fit" (Primer Ajuste).
3. Para hacerlo Greedy y conseguir una *buena aproximación* (aunque no la óptima siempre), la mejor regla es "First Fit Decreasing" (FFD): ordenamos los pesos de mayor a menor y tratamos de meter los más pesados primero en las bolsas abiertas. Si no caben, abrimos otra.

"""

def bolsas(capacidad, productos):
    if not productos:
        return []
        
    # ordeno de mayor a menor peso (Regla Greedy: First Fit Decreasing)
    #hago una copia para no mutar el arreglo original por las dudas

    productos_ordenados = sorted(productos, reverse=True)
    
    # lta de bolsas. Cada bolsa va a ser una lista con los productos adentro.
    lista_bolsas = []
    
    for peso_producto in productos_ordenados:
        ubicado = False
        
        #busco la primera bolsa donde el producto entre según la capacidad
        for bolsa in lista_bolsas:
            #sumo lo que ya tiene la bolsa actual para ver si hay espacio
            if sum(bolsa) + peso_producto <= capacidad:
                bolsa.append(peso_producto)
                ubicado = True
                break
                
        #sino entró en ninguna bolsa existente, abrimos una nueva bolsa
        if not ubicado:
            lista_bolsas.append([peso_producto])
            
    #devuelvo la lista con las bolsas armadas que espera RPL
    return lista_bolsas

"""
Justificación Ejercicio 11 (Bin Packing - Heurística FFD):
- Complejidad Temporal: O(n^2). El ordenamiento inicial toma O(n log n). Luego, para cada uno de los 'n' 
  productos, en el peor de los casos recorremos todas las bolsas creadas hasta el momento (que pueden ser hasta 'n'). 
  La función sum(bolsa) está acotada por el tamaño de la bolsa, por lo que el cómputo total de los bucles anidados 
  se mantiene en el orden cuadrático O(n^2). El término cuadrático domina la complejidad.
- Complejidad Espacial: O(n) para almacenar las sublistas con los elementos dentro de cada bolsa.
- ¿Es siempre óptimo?: NO. El problema de empaquetado de contenedores es NP-Hard.
- Contraejemplo: 
  Sea capacidad = 10, y los productos:.
  La suma es 20. El óptimo real usa 2 bolsas: Bolsa 1 (6+4) y Bolsa 2 (5+3+2).
  Nuestra heurística Greedy (FFD) hará:
  - Mete 6 en Bolsa 1.
  - Mete 5 en Bolsa 2.
  - 4 no entra en Bolsa 1 (6+4=10 justo, pero el algoritmo evalúa secuencialmente y si abre o rompe la paridad cambia) 
    o en este caso exacto: 4 no entra con 6 (6+4<=10 entra, pero supongamos un desajuste con elementos como [6, 6, 5, 5, 4, 4] 
    donde el descarte arrastra). En el caso de:
    Bolsa 1: [6, 4] -> llega a 10.
    Bolsa 2: [5, 3, 2] -> llega a 10. Justo da 2. 
  Un contraejemplo que SÍ falla siempre para FFD es: capacidad = 9, productos =.
  Óptimo (2 bolsas): [5, 4] y.
  Greedy (3 bolsas):, [4, 4], y el [2] queda solo en una tercera bolsa. Falla. Q.E.D.
"""