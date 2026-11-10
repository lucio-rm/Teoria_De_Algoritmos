"""
Enunciado 2. 
Para poder cortar con el juego del rival, Scaloni cuenta con información precisa minuto a minuto. 
En un momento dado, tiene la información perfecta de qué jugador puede darle un pase a cuál otro (independientemente de quién tenga la pelota) o marcar un gol.
Scaloni quiere saber a qué jugador, o jugadores, es indispensable marcar para evitar que nos marquen un gol. Suponiendo que una jugada arranca en el arquero contrario, y que se tiene la información de qué jugador de ese equipo puede pasarle la pelota a cuál/es otro/s (incluyendo al arquero), considerando que esto no es necesariamente recíproco (no todos los jugadores pueden hacer los mismos pases o goles, ¿o vos podés dar los mismos pases que Messi?), y cuáles jugadores podrían marcar un gol en ese momento, indicar cuáles son los mínimos jugadores contrarios a marcar de tal forma que no sea posible que nos marquen un gol (*no podemos marcar
al arquero*). 

Resolver este problema utilizando *redes de flujo*. Pueden suponer que la función flujo(red, s, t) les devuelve tanto la asignación de flujo a cada arista, como también la Red Residual resultante de aplicar el algoritmo de Ford-Fulkerson. 
Indicar y justificar la complejidad del algoritmo planteado. Para todo el problema, considerar que, si bien hay un único arquero, podrían haber n jugadores de campo (simplemente para no quedarse con que son 10 nada más).

"""

"""
planteo:


"""