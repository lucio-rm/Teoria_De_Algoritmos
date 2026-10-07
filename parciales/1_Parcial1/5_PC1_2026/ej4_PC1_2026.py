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

"""