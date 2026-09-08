"""
Enunciado 14:
Se sabe, por el teorema de Bolzano, que si una función es continua en un intervalo [a, b], y que en el punto a es positiva y en el punto b es negativa (o viceversa), necesariamente debe haber (al menos) una raíz en dicho intervalo. Implementar una función raiz que reciba una función (univariable) y los extremos mencionados a y b, y devuelva una raíz dentro de dicho intervalo (si hay más de una, simplemente quedarse con una). La complejidad de dicha función debe ser logarítmica del largo del intervalo [a, b]. Asumir que por más que se esté trabajando con números enteros, hay raíz en dichos valores: Se puede trabajar con floats, y el algoritmo será equivalente, simplemente se plantea con ints para no generar confusiones con la complejidad. Justificar la complejidad de la función implementada.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista en complejidad logarítmica". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

"""
"""
pplanteo:
- el Teorema de Bolzano dice que si f(a) y f(b) tienen signos opuestos, 
  hay una raíz entre ellos.
- encuentro el punto medio: mid = (a + b) // 2.
- evaluo f(mid). Si es 0, termino.
- para saber con qué mitad me quedo o elijo, evaluo los signos. Si f(a) y f(mid) 
  tienen el mismo signo, la cruzaron sin tocar el cero, entonces el cambio de 
  signo ocurre entre mid y b. si tienen signos opuestos, el cambio está entre a y mid.
- verifico si f(a) * f(mid) < 0 (creeeo que con floats y numeros grandes podria 
  haber overflow. Para evitar overflow, investigué y se tiene que evaluar comparaciones puras).
"""

def raiz(f, a, b):
    #mejoro el caso base: Si el intervalo se cerró o quedan dos vecinos pegados comparo cuál de los dos enteros (a o b) deja a la función más cerca de cero.
    if (b - a) <= 1:
        return a if abs(f(a)) <= abs(f(b)) else b
    mid = (a + b) // 2
    f_mid = f(mid)
    
    if f_mid == 0:
        return mid
        
    f_a = f(a)
    
    # hago el chequeo de cambio de signo lógica
    #Si f(a) es negativo y f(mid) positivo, o viceversa, el signo cambió aca
    if (f_a < 0 < f_mid) or (f_a > 0 > f_mid):
        return raiz(f, a, mid)
    else:
        #el cambio de signo tieneq ue estar en la otra mitad
        return raiz(f, mid, b)

"""
Justificacion de complejidad:
- temporal: T(n) = T(n/2) + O(1), siendo 'n'  la longitud del intervalo [a, b].
  Aplicando Teorema Maestro: A=1, B=2, f(n)=O(1). 
  log_b(A) = log_2(1) = 0. C = 0. Estamos en el Caso 2.
  La complejidad es Θ(log n).
- espacial: Θ(log n) debido al overhead de la pila de recursión (call stack).
"""
