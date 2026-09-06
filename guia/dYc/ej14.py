"""
Enunciado ejercicio 14:
(★★) Se sabe, por el teorema de Bolzano, que si una función es continua en un intervalo [a, b], y que en el punto 'a' es positiva y en el punto 'b' es negativa (o viceversa), necesariamente debe haber (al menos) una raíz en dicho intervalo. Implementar una función raiz que reciba una función (univariable) y los extremos mencionados a y b, y devuelva una raíz dentro de dicho intervalo (si hay más de una, simplemente quedarse con una). La complejidad de dicha función debe ser logarítmica del largo del intervalo [a, b]. 
Asumir que por más que se esté trabajando con números enteros, hay raíz en dichos valores: 
Se puede trabajar con floats, y el algoritmo será equivalente, simplemente se plantea con ints para no generar confusiones con la complejidad. 

Justificar la complejidad de la función implementada.

"""
"""
pplanteo:
- El Teorema de Bolzano establece que si f(a) y f(b) tienen signos opuestos, 
  hay una raíz entre ellos.
- Encontramos el punto medio: mid = (a + b) // 2.
- Evaluamos f(mid). Si es 0, terminamos.
- Para saber con qué mitad quedarnos, evaluamos los signos. Si f(a) y f(mid) 
  tienen el mismo signo, la cruzaron sin tocar el cero, entonces el cambio de 
  signo ocurre entre mid y b. Si tienen signos opuestos, el cambio está entre a y mid.
- La forma más ingenieril de comprobar "signos opuestos" sin if/else anidados 
  es verificar si f(a) * f(mid) < 0 (aunque con floats y números enormes podría 
  haber overflow, con enteros lógicos es una regla limpia. Para evitar overflow, 
  evaluamos comparaciones puras).
"""

def raiz(f, a, b):
    # Caso base: el intervalo se cerró sobre sí mismo.
    if a == b:
        return a

    mid = (a + b) // 2
    f_mid = f(mid)
    
    if f_mid == 0:
        return mid
        
    f_a = f(a)
    
    # Comprobación de cambio de signo lógica
    # Si f(a) es negativo y f(mid) positivo, o viceversa, el signo cambió acá.
    if (f_a < 0 < f_mid) or (f_a > 0 > f_mid):
        return raiz(f, a, mid)
    else:
        # El cambio de signo debe estar en la otra mitad
        # Hacemos mid + 1 porque ya sabemos que mid no es la raíz exacta
        return raiz(f, mid + 1, b)

"""
Justificacion de complejidad:
- Temporal: T(n) = T(n/2) + O(1), donde 'n' es la longitud del intervalo [a, b].
  Aplicando Teorema Maestro: A=1, B=2, f(n)=O(1). 
  log_b(A) = log_2(1) = 0. C = 0. Estamos en el Caso 2.
  La complejidad es Θ(log n).
- Espacial: Θ(log n) debido al overhead de la pila de recursión (call stack).
"""