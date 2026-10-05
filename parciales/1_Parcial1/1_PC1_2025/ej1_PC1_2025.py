"""
Enunciado ejercicio 1:

Supongamos que contamos con un árbol binario completo. Cada nodo del árbol tiene un valor x_i. Todos los x_i son valores diferentes. Definimos que un nodo v es mínimo local del árbol si su valor es menor al valor de los nodos a los que se conecta(es decir, los hijos que tenga y su padre, si tiene).
Implementar un algoritmo por *división y conquista* que obtenga algún mínimo local del árbol en O(logn). 
Justificar apropiadamente la complejidad del algoritmo implementado.

Considerar que el árbol tiene en su estructura el nombre del nodo, su valor, y las referencias a sus hijos izquierdo y derecho.
"""

"""
planteo:

es el contrario al peak finding.

se puede pensar como un arreglo.
si todos los valores son distintos, sé que puede haber más de un mínimo ocal.
sé con exactitud, que en las dos mitades del arbol (rama izq y der) hay como ínimo un minimo local.

me fijio la raíz.

si raiz < h_i and raiz < h_d:
    return raiz.valor
else:
    if h_i < h_d:
        return dyc(h_i, raiz)
    else:
        return dyc(h_d, raiz)

"""

def minimo_local(arbol):
    if not arbol:
        return None
    return _min_dyc(arbol.raiz, None)

def _min_dyc(nodo, padre):
    if nodo is None:
        return None

    v_izq = nodo.izq.valor if not None else float('inf')
    v_der = nodo.der.valor if not None else float('inf')
    v_padre = padre.valor if not None else float('inf')
    v_actual = nodo.valor
    #las igualdades no me importan porque sé que son todos con distinto valor
    
    if v_actual < v_izq and v_actual < v_der and v_actual < v_padre:
        # si es el mínimo local, tiene que ser menor a todos sus adyacentes
        return nodo
    else:
        # teorema: si el nodo no fue el minimo local, significa que hay un valor mínimo a éste. y sé con certeza que no es el padre. si fuera el padre, entraría en un bucle. 
        # y como empiezo con la raíz, descarto esa posibilidad
        if v_izq < v_der:
            return _min_dyc(nodo.izq, nodo)
        else:
            return _min_dyc(nodo.der, nodo)

"""
justificacion de la complejidad:
- temporal: O(logn).
Al ser un problema de División y Conquista, puedo justificar la complejidad utilizando el Teorema Maestro.
La ecuación de recurrencia general es: T(n) = A.T(n/B) + f(n)
siendo:
- A: cantidad de llamados recursivos = 1.
    siempre se ejecuta 1 llamado recursivo por cada nivel de recursión. nunca 2.
- B: en cuánto se divide el problema = 2.
    de todas las ramas del arbol siempre se elige 1 entre las dos. izq o der. entonces se parte en 2.
- f(n): el costo de dividir y combinar = O(n^c), C = 0. Siendo C el costo de todo lo que no es recursivo, es constante. Puras comparaciones.

la ecuación de recurrencia queda:
- T(n) = T(n/2) + O(1)

y como
f(n) = θ(n^C . log^(k)(n)) con C = 0 y k = 0 
y además, logB(A) = C, log2(1) = 0, la complejidad temporal queda:
θ(n^C . log^(k+1)(n)) = θ(log(n))



- espacial: O(1), no se usa espacio adicional. 
"""