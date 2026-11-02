"""
Ejercicio resuelto

Enunciado:
Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo contiguo de máxima suma, utilizando División y Conquista. 
Indicar y justificar la complejidad del algoritmo. 
Ejemplos:
    [5, 3, 2, 4, -1] →  [5, 3, 2, 4]
    [5, 3, -5, 4, -1] →  [5, 3]
    [5, -4, 2, 4, -1] → [5, -4, 2, 4]
    [5, -4, 2, 4] → [5, -4, 2, 4]

Consideraciones Iniciales
En primer lugar, conviene analizar cuál es la forma que tienen las posibles respuestas al enunciado. Se tratan en este caso de partes del arreglo completo de mayor o menor longitud. Solo se pueden seleccionar elementos contiguos, por lo que los subarreglos posibles serían:

- El primer elemento solo
- El primero y el segundo
	Y así hasta el último siendo 'n' subarreglos que empiezan con el primero
- El segundo solo
- El segundo y el tercero
	Y así hasta el último siendo 'n' - 1 subarreglos que empiezan con el segundo
- Y así siguiendo con los n elementos

La cantidad total de soluciones posibles sería entonces n + (n-1) + ⋯ + 1 , lo cual se puede escribir como:
n
∑ i = (n(n+1))/2
i=1
 
La demostración formal no va al caso, pero se puede recordar aquí (www.youtube.com/watch?v=tpkzn2e5mtI) . Si quisiéramos obtener la mejor solución simplemente comparando cada solución posible, la complejidad temporal del algoritmo sería O(n²).

Cabe destacar también que el algoritmo debe permitir el uso de números negativos. De lo contrario, el subarreglo de máxima suma siempre sería el arreglo completo. Si todos son positivos, nada va a sumar más que todos los elementos del arreglo.


Caso Base

Ahora bien, si el arreglo tiene un solo elemento, la solución es simplemente usar ese elemento sea cual sea su valor. Cuando son dos, puede convenir más usar solo el primero ([1,-1]), solo el segundo ([-1,1]) o ambos ([1,1]) dependiendo del caso. Si son más de dos elementos, se va complicando todo.




División y Conquista

Utilizando el caso base de un elemento, podemos dividir el arreglo por la mitad hasta obtener el caso en que tenemos que comparar dos subarreglos de largo 1.

Pero además de eso, debemos revisar cómo se comparan los arreglos generados por la recursión en cada llamada. Tenemos los elementos del lado izquierdo y del lado derecho de la llamada. Podríamos comparar el subarreglo candidato de cada lado y devolver el que sume más.

Sin embargo esto no es suficiente. En cada llamada, existen subarreglos candidatos que se pueden formar con los elementos del lado izquierdo y derecho, siempre y cuando sean contiguos.

Para aclarar esto, supongamos que en una llamada recursiva tenemos [1,2] en el arreglo derecho y [3,-5] en el lado izquierdo. El mejor subarreglo del lado izquierdo es [1,2] y el mejor del lado derecho es [3]. Pero para el arreglo combinado ([1,2,3,-5]) el mejor subarreglo es [1,2,3].

Eso significa que en cada caso recursivo la mejor solución puede usar solo elementos del lado izquierdo, solo elementos del lado derecho o una combinación de elementos de ambos.

Es una situación similar al ejercicio de puntos más cercanos donde tenemos dos alternativas por la recursión pero hay que tener en cuenta que pasa al medio para asegurar la mejor decisión

Máximo Subarreglo Cruzado

Entonces, dada una llamada recursiva con el mejor candidato del lado izquierdo y derecho, necesitamos obtener el mejor candidato que use elementos de los arreglos a ambos lados de la recursión y que además sea contiguo. A este subarreglo candidato se lo suele llamar subarreglo cruzado. Solo basta con obtener el subarreglo cruzado que sume más.

Para obtener el máximo subarreglo cruzado, podemos aprovecharnos de que tiene que ser contiguo y hacer lo siguiente.

Primero iteraremos el arreglo del lado izquierdo desde su índice mayor hasta el menor. La idea es ir sumando los elementos en una variable e ir guardando el índice que hace que la suma sea máxima. Es necesario que se iteren todos los elementos del arreglo izquierdo pues no se puede asegurar cuál índice será el que maximice la suma.

Se hace lo mismo, pero con el arreglo derecho desde el índice menor hasta el mayor.

Luego, el arreglo cruzado de suma máxima será el arreglo izquierdo y derecho combinados desde el índice que maximiza la suma a izquierda hasta el índice que maximiza la suma a derecha. El subarreglo candidato es contiguo y está formado por las partes de cada lado que suman más.

Teniendo el candidato a izquierda, a derecha y el máximo subarreglo cruzado, se debe comparar cual suma más y devolver esa solución para esa llamada recursiva.

"""

#Implementación

def subarreglo_cruzado(arr):
    med = len(arr) // 2

    suma_parcial = 0
    cruzado_izq = med
    suma_izq = 0
    for i in range(med - 1, -1, -1):
        suma_parcial += arr[i]
        if suma_parcial > suma_izq:
            suma_izq = suma_parcial
            cruzado_izq = i

    suma_parcial = 0
    cruzado_der = med
    suma_der = 0
    for j in range(med, len(arr)):
        suma_parcial += arr[j]
        if suma_parcial > suma_der:
            suma_der = suma_parcial
            cruzado_der = j

    return arr[cruzado_izq : cruzado_der + 1]

def subarreglo_maxima_suma(arr):
    if len(arr) == 1:
        return arr

    med = len(arr) // 2

    izq = subarreglo_maxima_suma(arr[:med])
    der = subarreglo_maxima_suma(arr[med:])
    cruzado = subarreglo_cruzado(arr)

    sumas = (sum(izq), sum(der), sum(cruzado))
    suma_maxima = max(sumas)

    if suma_maxima == sumas[0]:
        return izq
    elif suma_maxima == sumas[1]:
        return der
    else:
        return cruzado


"""
Complejidad

Para justificar la complejidad, utilizamos el teorema maestro. 
Se realizan dos llamadas recursivas para obtener el candidato a izquierda y derecha por lo que A=2. 
En cada llamada recursiva se divide el arreglo por la mitad, por lo tanto B=2. 
Para calcular el arreglo cruzado se deben recorrer ambas mitades hasta el final del ciclo haciendo que sea lineal en función de la cantidad de elementos. Calcular la suma de los subarreglos para comparar también es lineal, siendo el peor caso la suma de un subarreglo que contenga a todos los elementos. Eso significa que los cálculos auxiliares tienen complejidad lineal, resultando en que C=1.

La ecuación de recurrencia queda entonces como:
T(n)=2T(n/2)+O(n)
Haciendo los cálculos correspondientes llegamos a que

log2(2)=1 = C ⟹ O(n⋅log(n))
Es interesante notar que con el enfoque de división y conquista, se aprovechan los cálculos intermedios para poder obtener la solución sin necesidad de probar todas las combinaciones.

"""
