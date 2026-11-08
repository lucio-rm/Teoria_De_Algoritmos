"""
Enunciado 2. 
Un *plan de piso* consiste de n interruptores y n luces con sus ubicaciones. 
Además, un *diseño de iluminación* es una asignación de interruptores y luces (qué luces controla cada interruptor). Un plan de piso es ergonómico si para él existe al menos un diseño de iluminación ergonómico. 
Que un diseño sea ergonómico significa que, para cada interruptor de luz que haya, este maneje una única luz (lámpara, lamparita, etc.), y esa luz *sea además visible desde el lugar donde está el interruptor*. 
En los ejemplos del dorso de este enunciado, el ejemplo de la izquierda es ergonómico, pero el de la derecha no. 

Implementar, utilizando redes de flujo, un algoritmo ergonomicidad(interruptores, luces) que permita determinar si el plan es ergonómico, o no. 
En caso que lo sea, devolver las asignaciones de (interuptor, luz) que correspondan. 
Suponer que existe una función visible(interruptor, luz) que determina si la luz es visible desde el interruptor, y que dicha función ejecuta en tiempo constante. 

Indicar y justificar la complejidad del algoritmo implementado. 
El análisis de la complejidad debe ser completo.

(ver grafico)

"""

"""
planteo:
ergonomico:
maneje una sola luz , y que sea visible desde esa luz between luz-interruptor


pienso en poner ady. a cada coso que sea visible.

bastante sencillo.

Conversion a red de flujo:

Grafo de forma bipartito
Fuente S -> conectada  a cada Luz (capa 1)
cada luz -> conectada a cada interruptor que pueda ver
Interruptor (capa 2) -> conectados c/u al Sumidero T

Todo con cap. 1.

Si al sumidero le llegan 3 de flujo, significa que se usaron los 3 interruptores. y de la unica forma que suceda eso es que le llegue a cada uno 1 de flujo de cada luz. Y que estén conectados significa que son visibles entre sí. --> piso ergonómico.

"""




