from random import seed, randint
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp

from ejercicio import camino_minimo_piramide
from tests import dijkstra_piramide
from util import time_algorithm

seed(12345)
np.random.seed(12345)
sns.set_theme()

def get_random_pyramid(n: int):
    # Genera una piramide de n filas con pesos positivos entre 1 y 1000
    return [[randint(1, 1000) for _ in range(i + 1)] for i in range(n)]

# 1. Medicion del Algoritmo de PD entre n = 100 y n = 2000 filas
x = np.linspace(100, 2000, 15).astype(int)
print("Midiendo Programacion Dinamica Bidireccional...")
results_pd = time_algorithm(camino_minimo_piramide, x, lambda s: [get_random_pyramid(s)])

# Ajuste por cuadrados minimos O(n^2)
f_n2 = lambda x, c1, c2: c1 * (x**2) + c2
c_n2, _ = sp.optimize.curve_fit(f_n2, x, [results_pd[n] for n in x])
errors_n2 = [np.abs(c_n2[0] * (n**2) + c_n2[1] - results_pd[n]) for n in x]
print(f"Coeficientes PD: c_1 = {c_n2[0]:.4e}, c_2 = {c_n2[1]:.4e}")
print(f"Error cuadratico total O(n^2): {np.sum(np.power(errors_n2, 2)):.6f}")

# Grafico 1: Tiempo de ejecucion y Ajuste n^2
fig, ax = plt.subplots()
ax.plot(x, [results_pd[i] for i in x], label="Medición PD In-Place")
ax.plot(x, [f_n2(n, c_n2[0], c_n2[1]) for n in x], 'r--', label="Ajuste $n^2$")
ax.set_title('Tiempo de ejecución: Camino Mínimo en Pirámide (PD)')
ax.set_xlabel('Cantidad de filas de la pirámide (n)')
ax.set_ylabel('Tiempo de ejecución (s)')
ax.legend()
plt.savefig("informe/images/ajuste_pd_n2.png", dpi=300, bbox_inches='tight')

# Grafico 2: Error absoluto del ajuste
fig, ax = plt.subplots()
ax.plot(x, errors_n2)
ax.set_title('Error de ajuste por Cuadrados Mínimos ($n^2$)')
ax.set_xlabel('Cantidad de filas de la pirámide (n)')
ax.set_ylabel('Error absoluto (s)')
plt.savefig("informe/images/error_ajuste_pd.png", dpi=300, bbox_inches='tight')

# 2. Comparativa contra Dijkstra (usamos tamanos hasta 1000 porque Dijkstra es mucho mas lento)
x_comp = np.linspace(100, 1000, 10).astype(int)
print("Midiendo comparativa contra Dijkstra...")
res_pd_comp = time_algorithm(camino_minimo_piramide, x_comp, lambda s: [get_random_pyramid(s)])
res_dij_comp = time_algorithm(dijkstra_piramide, x_comp, lambda s: [get_random_pyramid(s)])

# Grafico 3: Comparativa PD Bidireccional vs Dijkstra
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(x_comp, [res_dij_comp[n] for n in x_comp], "o-", label="Dijkstra $\Theta(n^2 \log n)$")
ax.plot(x_comp, [res_pd_comp[n] for n in x_comp], "s-", label="PD Bidireccional con Poda $\Theta(n^2)$")
ax.set_title('Comparación Empírica: PD Bidireccional vs. Dijkstra')
ax.set_xlabel('Cantidad de filas de la pirámide (n)')
ax.set_ylabel('Tiempo de ejecución (s)')
ax.legend()
plt.savefig("informe/images/comparativa_pd_vs_dijkstra.png", dpi=300, bbox_inches='tight')
print("¡Gráficos generados con éxito en informe/images/!")

