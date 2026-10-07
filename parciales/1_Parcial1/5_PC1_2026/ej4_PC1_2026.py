"""
Enunciado ejercicio 4:
Implementar un algoritmo que, por *programación dinámica*, dado un grafo no dirigido y *pesado*, dos vértices s y t, y un número k, determine el costo del camino mínimo entre s y t que utilice *exactamente* k aristas. El camino *puede* repetir vértices (es decir, el camino puede no ser simple). 
También escribir el algoritmo que permita reconstruir la solución. 

Indicar y justificar la complejidad del algoritmo implementado (el de programación dinámica, y también el de la reconstrucción).
"""
"""
planteo:

- grafo no dirigido y pesado.
- vertices s y t
- num k

costo camino mínimo entre s y t, utilizando k aristas. 
se puede repetir vértices.

- y aser reconstrucción.


s ----------------------------------> t
cantidad de aristas k. si o si.
puedo ir por la misma, con tal de llegar a k.

que opciones tengo.
subproblemas
ec. recurrencia
memoization.

subproblemas:

el problema: que no haya K aristas.
asumir que en el grafo hay >= k aristas. (chequearlo en O(E))


reeeeeeeecordar
bellman - ford es un algoritmo de programación dinámica. y encuentra camino mínimo.....................

anda a recordar la ec. recurrencia del bellman - ford. PROBABLE. que tomen algo asi en los parciales /( instancias evaluatorias del C2.

pensar.
estoy en el final. que me conviene======
pensar en el atras.

estoy en este evertice. ¿ por cual de todos mis adyacentes vine? busco el de mínimo camino. pero tal vez ir por otro me convenia.


primero encontrar el camino minimo en la ec. recurrencia. despues fijarme que onda k.
k influye en l aec. recurrencia?
osea es una restricción obligartoria. tien que esar.
mejor aproach:
- estoy en t.
- si estoy en t, que opciones tuve?
vine de mis adyacentes. de cual? el que minimice la llegada. y el que suma k.

OPT[i, k] = min ( OPT[i-1, k-1])
            ∀ ady

OPT tiene quee devolverme el costo del caimno minimo.
la reconstruccion tengo que devolver qué vértices elegi para el camino. se pueden repetir.

tal vez i me chupa un huevo, K es lo mas importante.

tengo que averiguar.
sé que si o si OPT[k] = costo_minimo_para_llegar_a_t
entonces, no me sirve i para nada.

el costo de usar o no usar la arista.
si uso la arista, k + 1.
si no uso la arista, me tengoq ue fijar en otro adyacente.
si o si tiene qe estar la opción de usar la arita, aún asi si valr 3 millones. si es la última para llegar a T y sumar == k, tengo que usarla.

OPT[k] = min(c_v + OPT[k-1])
        ∀ ady(v)

para las opciones de k, tengo que ir fijandome en el radio. qué es lo mejor para cada k. cuál es el camino mínimo.

la condición tiene que ser que cuando llewgue a t, k tiene que valer k je.
como verga hago eso. como pongo esa condicion.
teniendo i = 0, 1, ..., k

i = 0, estoy en s.
i = 1, voy al adyacente de s con menor costo en la arrrrrista.
i = 2. tengo que encontrar el camino minimo de menor peso de longitud i. pudiendo repetir vértices/aristas.


matriz:
i = cantidad de aristas
v = vertice del grafo

OPT[i, v] = min(OPT[i-1, w] + peso_arista(v, w))
        ∀ w ady(v)

si se que estoy en 'v' con 'i' aristas, tuve que haber llegado con el menor costo desde cualquiera de mis adyacentes.
teniendo i - 1 aristas.
"""

def camino_k(grafo, s, t, k):
    if not grafo:
        return []

    vertices = grafo.obtener_vertices() #O(V)

    if not vertices or s not in vertices or t not in vertices:
        return []
    
    M_MATRIZ = [[0] * (k+1) for _ in range(len(vertices))]
    # cada fila representa la cantidad de aristas a usar, las columnas representan el "haber llegado a 'v' con i aristas"
    
    indice = 0
    while indice < len(vertices):
        v = vertices[indice]
        if v == s:
            M_MATRIZ[0][indice] = 0
        else:
            M_MATRIZ[0][indice] = float('inf')
        #si o si tiene que empezar desde s.
    
    for i in range(1, k+1): #empiezo de la primera
        for vertice in range(len(vertices)):
            M_MINIMOS = []
            for ady in grafo.adyacentes(vertice):
                valor = grafo.peso_arista(vertice, ady)
                te_elijo = valor + M_MATRIZ[i-1][ady]
                M_MINIMOS.append(te_elijo)
            M_MATRIZ[i][vertice] = min(M_MINIMOS) 

    return _reconstruccion(M_MATRIZ, grafo, s, t, k) # podría devolver M_MATRIZ[k][t] y listo pero pruebo con la reconstrucción.

def _reconstruccion(M_MATRIZ, grafo, s, t, k):
    CAMINO = []

    costo_min = M_MATRIZ[k][t]
    CAMINO.append(t)
    aristas_usadas = k
    vertice_actual = t
    while costo_min > 0:
        """
        idea de reconstrucción:
        voy a cada adyacente desde el final.
        me fijo cuál elegi comparando con el costo de la arista.
        
        osea si yo vine de W, sé que M_MATRIZ[i-1][W] == costo_min - peso_arista(v, w)
        cuando el costo_min sea 0 significa que ya llegué a s.
        """
        for ady in grafo.adyacentes(vertice_actual):
            if M_MATRIZ[aristas_usadas-1][ady] == costo_min - grafo.peso_arista(vertice_actual, ady):
                CAMINO.append(ady)
                costo_min -= grafo.peso_arista(vertice_actual, ady)
                
                vertice_actual = ady

    return CAMINO[::-1] # lo invierto, para que quede el camino en orden cronológico.



"""
Justificacion de la complejidad:

-------------- temporal:
- obtener_vertices => O(V), siendo V la cantidad de vértices
- llenar la primer fila => O(V)
- recorro k filas. y por cada k fila recorro V vertices ===> O(k.V)
- en la reconstrucción hago un recorrido de K iteraciones (el camino mínimo encontrado en exactamente k aristas)

complejidad temporal: O(k.V)

-------------- espacial: O(k.V), ya que a lo sumo como memoria adicional va a llenarse la matriz de óptimos con k.V elementos. siendo V la cantidad de vertices en el grafo y k la condicion de aristas.
"""


"""

correccion:

mejor reconstruccion

"""

def _reconstruccion(M_MATRIZ, grafo, s, t, k):
    if M_MATRIZ[k][t] == float('inf'):
        return [] #no hay camino posible para k aristas

    CAMINO = [t]
    vertice_actual = t

    for aristas_usadas in range(k, 0, -1):
        for ady in grafo.adyacentes(vertice_actual):
            peso = grafo.peso_arista(vertice_actual, ady)

            #ec. recurrencia al reves
            if M_MATRIZ[aristas_usadas][vertice_actual] == M_MATRIZ[aristas_usadas-1][ady] + peso:
                CAMINO.append(ady)
                vertice_actual = ady

                break #encuentro el origen de este paso, voy pal siguiente k
    return CAMINO[::-1]
