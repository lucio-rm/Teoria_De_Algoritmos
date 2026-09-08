"""
Enunciado ejercicio 16:
(★★★) El club de Amigos de Siempre prepara una cena en sus instalaciones en la que desea invitar a la máxima cantidad de sus 'n' socios. Sin embargo por protocolo cada persona invitada debe cumplir un requisito: Sólo puede ser invitada si conoce a al menos otras 4 personas invitadas.

a. Nos solicitan seleccionar el mayor número posible de invitados. Proponer una estrategia greedy óptima para resolver el problema.

b. Los organizadores desean que cada invitado pueda conocer nuevas personas. Por lo que nos solicitan que adicionemos una nueva restricción a la invitación: Sólo puede asistir si NO conoce al menos otras 4 personas invitadas. Modifique su propuesta para satisfacer esta nueva solución.

"""

# conocidos: lista de pares de personas que se conocen, cada elemento es un (a,b)
def obtener_invitados(conocidos):
    if not conocidos:
        return []
        
    # construyo el mapa de adyacencia (quién conoce a quién) usando diccionarios y sets
    adyacentes = {}
    for par in conocidos:
        persona_a = par[0]
        persona_b = par[1]
        
        if persona_a not in adyacentes:
            adyacentes[persona_a] = set()
        if persona_b not in adyacentes:
            adyacentes[persona_b] = set()
            
        adyacentes[persona_a].add(persona_b)
        adyacentes[persona_b].add(persona_a)
        
    # inicializo la lista con las personas que no cumplen el requisito inicial (< 4 conocidos)
    por_eliminar = [persona for persona, conocidos_set in adyacentes.items() if len(conocidos_set) < 4]
    
    # estrategia Greedy de reducción / eliminación:
    #saco a los que no cumplen, lo que puede causar un efecto cascada sobre sus conocidos
    while por_eliminar:
        persona_actual = por_eliminar.pop()
        
        if persona_actual in adyacentes:
            # uso list() para iterar sobre una copia estática de los vecinos
            #y me evito el 'RuntimeError: Set changed size during iteration'
            vecinos_estaticos = list(adyacentes[persona_actual])
            
            for vecino in vecinos_estaticos:
                if vecino in adyacentes:
                    # le aviso al vecino que esta persona ya no asistirá a la cena
                    adyacentes[vecino].discard(persona_actual)
                    
                    # si al sacarla, el vecino ahora conoce a menos de 4 personas invitadas, se lo agenda para eliminar
                    if len(adyacentes[vecino]) < 4:
                        por_eliminar.append(vecino)
            
            # borro definitivamente a la persona de la lista de invitados
            del adyacentes[persona_actual]
            
    # devuelvo la lista final con los invitados que sobrevivieron al filtro
    return list(adyacentes.keys())



"""
Justificación Ejercicio (Selección de Invitados - k-Core con k=4):

- Complejidad Temporal: O(V + E). Sea 'V' la cantidad de personas únicas y 'E' la cantidad de duplas 
  en la lista 'conocidos'. Construir el diccionario de adyacencia toma O(E). Filtrar los elementos 
  iniciales toma O(V). En la reducción golosa, cada persona entra y sale de la lista 'por_eliminar' 
  a lo sumo una vez O(V), y recorrer sus vecinos implica que cada arista (relación de conocidos) 
  se evalúa como mucho dos veces O(E). Al usar operaciones de conjuntos (set.discard) y diccionarios, 
  el acceso es O(1) promedio. Por lo tanto, la complejidad total es lineal O(V + E), ideal para pruebas de volumen.

- Complejidad Espacial: O(V + E), requerido para almacenar el mapa de adyacencia de los conocidos en memoria.

- ¿Por qué se trata de un algoritmo Greedy?: Porque aplica una regla de optimización local irrevocable en cada paso: 
  si en el estado actual una persona tiene menos de 4 conocidos invitados, es imposible que forme parte de la 
  solución final óptima, por lo que se la descarta de inmediato sin reconsiderar la decisión a futuro.

- ¿El algoritmo da siempre la solución óptima?: SÍ. 
  Demostración por argumento de optimalidad/reducción: Sea 'S' el conjunto máximo de invitados que cumplen el requisito 
  (la solución óptima global), y sea 'A' el conjunto que devuelve nuestro algoritmo. Al comenzar con todos los socios 
  disponibles, sabemos que S está contenido en nuestro conjunto inicial. Si nuestro algoritmo elimina a una persona 'X', 
  es porque en ese momento tiene menos de 4 conocidos vivos. Como 'S' es un subconjunto válido de personas donde TODOS 
  tienen al menos 4 conocidos dentro de 'S', 'X' jamás podría tener 4 conocidos dentro de 'S'. Por ende, 'X' no pertenece 
  a 'S'. Siguiendo este principio por inducción, ninguna de las personas eliminadas por la heurística golosa podría 
  pertenecer a la solución óptima, garantizando que el conjunto final remanente es el máximo posible absoluto.
"""
