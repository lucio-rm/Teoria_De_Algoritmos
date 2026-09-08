"""
Enunciado 17:
Una función lineal se define como f(x) = a x + b.
Si tenemos dos funciones lineales f_1(x) = a_1 x + b_1 y
f_2(x) = a_2 x + b_2, entonces la composición puede simplificarse a:
f_3(x) = f_1(f_2(x)) = (a_1 a_2) x + (a_1 b_2 + b_1). Es decir, tenemos una nueva función lineal, cuyos a y b son los resultates marcados.

Utilizando división y conquista, implementar una función
composicion_n(a, b, c, n) que reciba los valores de a y b de una función lineal,
c y n y determine el valor de f^n(c) = f(f(f(...f(c)) (n composiciones de la
función f consigo misma) en tiempo \mathcal{O}(\log n).
Justificar adecuadamente la complejidad del algoritmo implementado.

Recomendamos primero obtener los valores de a y b que corresponden a f^n(x). La cuenta final es trivial.

¿Querés más ayudas? En el enunciado en la guía hay unas más (no las ponemos directo en caso que lo quieras pensar directamente, en la guía podemos ocultarlos y aquí no).

"""

"""
planteo:
n = 1:
    f(c) = ac + b

n = 2:
    f(f(c)) = a(ac + b) + b
    f²(c) = a²c + b(1 + a)

n = 3:
    f(f(f(c))) = a(a(ac + b) + b) + b
    f³(c) = a³c + b(1 + a + a²)

n = 4:
    f(f(f(f(c)))) = a(a(a(ac + b) + b) + b) + b
    f⁴(c) = a⁴c + b(1 + a + a² + a³)
.

de ahi puedo sacar la ecuacion de recurrencia: (ya sabiendo que n >= 1)
f^n(c) = (a^n).c + b.(1 + sum(de i=2 hasta n) de a^(i-1) --> para el caso de n = 1, sumatoria vacía es = 0. 
o sino, aplico la serie geométrica
f^n(c) = (a^n).c + b.(1 + (a^n - a)/(a - 1) ) , para todo a != 1

una vez hecho eso, me fijo que dice la consigna xd porque me pide CALCULAR la f

me pide calcular el valor de f. teniendo los valores de a, b, c y n.

    trato de usar un pensamiento logico como el calcular la raiz entera de un numero n.
    sé que el resultado de raiz de n esta entre [0, n]

sé que:
    - n >= 1. si es otra cosa, error.
    - si c = 0 && b = 0. -> para todo a, n -> f() = 0.
        - si son distintos a 0, 
            si a == 0, f() = b
            sino, f() > b.
            
    - si a = 1, tiro error? o descarto eso que pensé de la ecuacion de recurrencia?
    

"""
def composicion_n(a, b, c, n):
    # n >= 1 según las restricciones del enunciado
    a_nuevo, b_nuevo = _calculo_rec(a, b, n)
    return (a_nuevo * c) + b_nuevo

def _calculo_rec(a, b, n):
    # Caso base: f^1(x) tiene los mismos a y b originales
    if n == 1:
        return a, b

    if n % 2 == 0:
        #si n es par, calculo f^{n/2}
        a_medio, b_medio = _calculo_rec(a, b, n // 2)
        #compongo f^{n/2} consigo misma -> f_1(x) = f_2(x) = f^{n/2}(x)
        # formula: (a_1 * a_2)x + (a_1 * b_2 + b_1)
        a_final = a_medio * a_medio
        b_final = a_medio * b_medio + b_medio
        return a_final, b_final
    else:
        # AYUDA 2: Si n es impar, calculamos f^{n-1} (que va a ser par)
        a_par, b_par = _calculo_rec(a, b, n - 1)
        # Componemos la original f(x) con f^{n-1}(x) -> f(f^{n-1}(x))
        # f_1 es la original (a, b) y f_2 es la par (a_par, b_par)
        a_final = a * a_par
        b_final = a * b_par + b
        return a_final, b_final

"""
JUSTIFICACIÓN DE COMPLEJIDAD:

1. COMPLEJIDAD TEMPORAL: O(log n)
Para el caso general (cuando n es par), podemos modelar la función con la ecuación 
de recurrencia del Teorema Maestro:
T(n) = A * T(n / B) + O(n^C)
T(n) = 1 * T(n / 2) + O(1)

Donde:
- A = 1: Se realiza exactamente un único llamado recursivo por nivel.
- B = 2: El tamaño del problema (n) se divide a la mitad en cada paso par.
- O(1) (C = 0): Las operaciones que se hacen al volver de la recursión para resolver 
  la composición matemática son puramente aritméticas (sumas y multiplicaciones constantes).

Evaluando las condiciones del Teorema Maestro:
log_B(A) = log_2(1) = 0.
Como log_B(A) es igual a C (0 == 0), caemos en el segundo caso del Teorema Maestro.
Por lo tanto, la complejidad temporal es:
T(n) = O(n^C * log n) = O(n^0 * log n) = O(log n)

Nota sobre el caso impar: Cuando n es impar, el algoritmo reduce el problema a n-1, 
lo que genera de forma inmediata un caso par en la siguiente llamada. Esto como máximo 
duplica el número total de llamadas a la función (agregando un paso extra O(1)), por lo 
que no altera la clase de complejidad, manteniéndose firmemente en O(log n).


2. COMPLEJIDAD ESPACIAL: O(log n)
A nivel de estructuras de datos el uso de memoria es O(1) ya que no se realizan copias 
de arreglos ni se almacena información en colecciones dinámicas. 
Sin embargo, al ser un algoritmo recursivo de Divide y Vencerás, cada llamada se apila 
en la memoria del sistema (Call Stack). Debido a que n se reduce a la mitad de forma 
logarítmica en los casos pares, la profundidad máxima que alcanzará la pila de ejecución 
será proporcional a log_2(n). Por ende, la complejidad espacial total es O(log n).
"""
