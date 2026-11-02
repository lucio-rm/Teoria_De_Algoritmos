"""
Enunciado ejercicio 12:
(★★) Trabajamos para el mafioso Arnook, que es quien tiene la máxima influencia y poder en la zona costera de Ciudad República. Allí reina el caos y la delincuencia, a tal punto que quien termina organizando las pequeñas mafias locales no es otro sino Arnook. 
En particular, nos vamos a centrar en unos pedidos que recibe de parte de dichos grupos por el control de diferentes kilómetros de la ruta costera. Cada pequeña mafia le pide a Arnook control sobre un rango de kilómetros (por ejemplo, la mafia nro 1 le pide del kilómetro 1 al 3.5, la mafia 2 le pide del 3.3333 al 8, etc. . . ). 
Si hay una mafia tomando control de algún determinado kilómetro, no puede haber otra haciendo lo mismo (es decir, no pueden solaparse). Cada mafia pide por un rango específico. Arnook no cobra por kilómetraje sino por “otorgar el permiso”, indistintamente de los kilómetros pedidos. 

Ahora bien, esto es una mafia, no una ONG, y no debe rendir cuentas con nadie, así que lo único que es de interés es maximizar la cantidad de permisos otorgados (asegurándose de no otorgarle algún lugar a dos mafias diferentes). 

Implementar un algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada mafia, y determine a cuáles se les otorgará control, de forma que no hayan dos mafias ocupando mismo territorio, y a su vez maximizando la cantidad de pedidos otorgados. 

Indicar y justificar la complejidad del algoritmo implementado. 
Justificar por qué el algoritmo planteado es Greedy. 
¿El algoritmo da la solución óptima siempre?

"""

"""
planteo (El modelo mental correcto):
1. Este es idéntico a la Selección de Actividades (Charlas en un aula). Las mafias son las charlas, los kilómetros son el horario de inicio y fin.
2. La clave para maximizar es ordenar siempre por el final del rango (Earliest Finish Time) y no por el inicio, ni por la longitud del tramo.
3. Al ordenar por fin, garantizamos liberar la "ruta" lo más rápido posible, dejando la mayor cantidad de espacio libre (kilómetros restantes) para alojar a la siguiente mafia.

> ELI5 (Ejemplo para un niño de 5 años):
Si quieres comer la mayor cantidad de porciones de pizza de diferentes sabores en una fiesta antes de llenarte, eliges siempre los trozos más pequeños primero para dejar espacio en la panza para los siguientes, sin importar de qué lado de la caja los tomes.
"""

def control(rangos):
    # Rangos es una lista de tuplas (km_inicio, km_fin, id_mafia)
    if not rangos:
        return []
        
    # Regla Greedy: Ordenar por km_fin de menor a mayor
    rangos.sort(key=lambda x: x[1])
    
    mafias_aprobadas = []
    km_ocupado_hasta = -1 # Rastrea hasta dónde está ocupada la ruta
    
    for mafia in rangos:
        inicio, fin, id_mafia = mafia
        # Si el rango pedido empieza después de donde termina el último ocupado
        if inicio >= km_ocupado_hasta:
            mafias_aprobadas.append(mafia)
            km_ocupado_hasta = fin # Actualizamos el control territorial
            
    return mafias_aprobadas

"""
Justificación Ejercicio 12:
- Complejidad Temporal: O(n log n). El ordenamiento por `km_fin` es la operación dominante y cuesta O(n log n). Iterar el arreglo para verificar solapamientos toma O(n).
- Complejidad Espacial: O(n) en el peor de los casos para almacenar la lista de mafias_aprobadas.
- ¿Es siempre óptimo?: SÍ. Está matemáticamente demostrado mediante el argumento de Inversiones. Todo schedule (asignación) que se desvíe del ordenamiento por finalización contiene una "inversión". Al corregir esa inversión (intercambiando el orden), la cantidad de asignaciones jamás empeora, demostrando que la solución Greedy siempre converge al óptimo.
"""