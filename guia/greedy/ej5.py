"""
Enunciado ejercicio 5:
(★) Realizar un seguimiento de aplicar el Algoritmo de Huffman al texto “PRETERINTENCIONALIDAD”, indicando el binario resultante de comprimirlo. 
¿Por qué se trata de un algoritmo Greedy? Justificar

"""

"""
planteo:
cuento frecuencias de letras
armo tabla
armo arbol

agrego al arbol izq = 0, der = 1

sumo a la tabla su referencia binaria (se agrega a la tabla? o es mental? para no calcular una y otra vez)

tengo la palabra


"""

"""

PRETERINTENCIONALIDAD

P - 1
R - 2
E - 3
T - 2
I - 3
N - 3
C - 1
O - 1
A - 2
L - 1
D - 2



1. iteracion 0: Inicializo todas las letras con su freciencia, como hojas.
E   I   N   R   T   A   D   P   C   O   L
3   3   3   2   2   2   2   1   1   1   1


2. iteracion 1: voy juntando los menores (L-O y P-C)

                             (2)     (2)
                             / \     / \
E   I   N   R   T   A   D   P   C   O   L
3   3   3   2   2   2   2   1   1   1   1

3. iteracion 2: junto los menores (frecuencia 2 en este caso) (R-T, A-D, (PC)-(OL))

                                  (4)
                              /       \
             (4)     (4)     (2)      (2)
             / \     / \     / \     /  \ 
E   I   N   R   T   A   D   P   C   O   L
3   3   3   2   2   2   2   1   1   1   1


4. iteracion 3: junto los menores (frec. 3 (I-E) y el N como me quedó solo lo voy a juntar con el siguiente menor (el 4))

           (7)                    (4)
          /   \                /       \
 (6)     /   (4)     (4)     (2)      (2)
 / \    /    / \     / \     /  \    /  \
E   I   N   R   T   A   D   P   C   O   L
3   3   3   2   2   2   2   1   1   1   1

5. iteracion 4: junto los menores (frec 4 (el (AD) y (PCOL)))


                             (8)
                        /          \
           (7)         /          (4)
          /   \       /        /       \
 (6)     /   (4)     (4)     (2)      (2)
 / \    /    / \     / \     /  \    /  \
E   I   N   R   T   A   D   P   C   O   L
3   3   3   2   2   2   2   1   1   1   1



6. iteracion 5: junto los menores (frec 7 y 6 (el (EI) y (NRT)))



       (13)                  (8)
    /       \           /          \
   /       (7)         /          (4)
  /       /   \       /        /       \
 (6)     /   (4)     (4)     (2)      (2)
 / \    /    / \     / \     /  \    /  \
E   I   N   R   T   A   D   P   C   O   L
3   3   3   2   2   2   2   1   1   1   1

7. iteracion 6: como el 8 y 13 quedaron solos, los junto.
                 (21)
         /                    \
       (13)                  (8)
    /       \           /          \
   /       (7)         /          (4)
  /       /   \       /        /       \
 (6)     /   (4)     (4)     (2)      (2)
 / \    /    / \     / \     /  \    /  \
E   I   N   R   T   A   D   P   C   O   L
3   3   3   2   2   2   2   1   1   1   1



Al ser 21 letras, (o sumo todas las frecuencias), chequeo que salió bien.


ahora por cada arista que baje por la izquierda, inserto peso 0. 
arista que baja por derecha, inserto peso 1


                 (21)
        0/                  \1
       (13)                  (8)
    /       \1           /      \1
  0/       (7)         0/       (4)
  /       /   \1       /      0/     \1
 (6)     0/   (4)     (4)     (2)    (2)
0/ \1    /   0/ \1   0/ \1  0/  \1  0/  \1
E   I   N   R   T   A   D   P   C   O   L
3   3   3   2   2   2   2   1   1   1   1

actualizo la tabla:


PRETERINTENCIONALIDAD

P - 1 - 1100
R - 2 - 0110
E - 3 - 000
T - 2 - 0111
I - 3 - 001
N - 3 - 010
C - 1 - 1101
O - 1 - 1110
A - 2 - 100
L - 1 - 1111
D - 2 - 101




convierto la palabra a binario:
  P  R   E   T  E   R  I  N   T  E  N  C   I   O  N  A  L   I  D  A  D 
11000110000011100001100010100111000010110100111100101001111001101100101


pasamos de tener 21 bytes (168 bits) a tener -> 71 bits.



Justificación Greedy de Huffman:
1. Regla Greedy: En cada paso, el algoritmo extrae los DOS nodos con menor 
   frecuencia total del bosque (Min-Heap) y los fusiona creando un nuevo nodo padre.
2. Los nodos fusionados abandonan la cola original 
   y entran como un bloque unificado. No se deshacen las uniones.
3. Subestructura Óptima: Al asignar las primeras fusiones (las ramas más largas 
   del árbol final) a los caracteres menos frecuentes, se garantiza que los 
   caracteres más frecuentes queden más cerca de la raíz (códigos más cortos). 
   Reduce el problema de 'n' caracteres a 'n-1' unificando los dos peores casos.






"""