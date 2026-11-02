"""
Enunciado Ej.17 (★★★):
Tito trabaja para la mafia. Debe llevar en camiones de caudales el dinero recaudado por la organización a modo de devolver favores a diferentes estaciones de policía. 
Entre diferentes rutas puede tener que cambiar de camión (para no ser fácilmente detectado), donde cada camión puede tener diferente capacidad. Además, en algunos puntos (escondites de la mafia) puede recoger más dinero.

Tito entonces cuenta con un grafo dirigido con las diferentes rutas, y puntos donde pueda tener que ir cambiando de camión según como cambie de ruta. El grafo es pesado y las aristas tienen como peso la capacidad del camión de caudales a usar por esa ruta. 
En cada vértice tenemos un punto donde podría (o no) poder recoger dinero o tener que dejar un agradecimiento, lo cual está modelado con un valor $w(v)$ (si es positivo, al pasar por allí podemos recoger dinero, si es negativo es que debemos dejar un agradecimiento, si es 0, es simplemente un punto de cambio de camión y nada más). Tito puede comenzar cada recorrido desde donde desee, si bien tiene sentido ir empezando desde algún escondite. 

Usando redes de flujo, implementar un algoritmo que reciba dicho grafo y determine si es posible pagar todos los agradecimientos correspondientes. 
No es necesario indicar cómo serían los recorridos. 

Indicar y justificar la complejidad del algoritmo implementado. El análisis de la complejidad debe ser completo.

"""
"""
planteo:


"""