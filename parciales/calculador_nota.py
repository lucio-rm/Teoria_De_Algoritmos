#!/usr/bin/env python3
import itertools

PUNTOS = {"B": 4, "B-": 3, "B=": 2, "R": 1, "M": 0}

def calc_nota_examenes(puntos):
    nota = 0.37 * puntos + 0.3
    return 10.0 if nota > 10 else round(nota, 2)

def calc_nota_final(nota_ex):
    return 10.0 * 0.30 + nota_ex * 0.70

def obtiene_nota_acta(nex, nfi):
    decimal = round(nfi - int(nfi), 2)
    if decimal == 0.50:
        return int(nfi) + 1 if nex > nfi else int(nfi)
    return round(nfi)

# =====================================================================
# CONFIGURÁ TUS NOTAS ACTUALES ACÁ
# Si no lo rendiste todavía, poné None.
# Recordá que "B--" no existe, usamos "B=" que vale 2 puntos.
# =====================================================================
mis_notas = {
    "Dyc": "B",
    "Greedy": "R",
    "Backtracking": "R",
    "Programación Dinámica": "B-",
    "Programación Lineal": None,
    "Flujo": None,
    "Reducciones": None
}

# 1. Analizar estado actual
puntos_actuales = 0
temas_rendidos = 0
temas_pendientes = []

print("=== ESTADO ACTUAL DE LA CURSADA ===")
for tema, nota in mis_notas.items():
    if nota is not None:
        pts = PUNTOS[nota]
        puntos_actuales += pts
        temas_rendidos += 1
        print(f"  - {tema}: {nota} ({pts} pts)")
    else:
        temas_pendientes.append(tema)
        print(f"  - {tema}: Pendiente (-)")

print(f"\nPuntos acumulados hasta ahora: {puntos_actuales}")

# Determinar el mínimo de puntos totales en examen para sacar 10 en acta
MIN_PUNTOS_PARA_10 = 25
for pts in range(0, 29):
    nex = calc_nota_examenes(pts)
    nfi = calc_nota_final(nex)
    if obtiene_nota_acta(nex, nfi) == 10:
        MIN_PUNTOS_PARA_10 = pts
        break

puntos_faltantes = MIN_PUNTOS_PARA_10 - puntos_actuales
print(f"Puntos mínimos totales en examen para sacar 10 en Acta: {MIN_PUNTOS_PARA_10}")

if puntos_faltantes <= 0:
    print("\n¡Felicitaciones! Con lo que tenés ya te aseguraste el 10 (asumiendo que mantengas los TPs).")
    exit()

print(f"Necesitás conseguir un mínimo de: {puntos_faltantes} puntos adicionales.\n")

# 2. Generar combinaciones posibles para los temas pendientes/recuperatorios
opciones_nota = ["B", "B-", "B=", "R", "M"]

# Vamos a simular qué pasa si recuperás los temas con nota menor a B y qué sacás en los pendientes
temas_a_mejorar = [t for t, n in mis_notas.items() if n is not None and n != "B"]
todos_los_cambios = temas_a_mejorar + temas_pendientes

print("=== HOJA DE RUTA PARA SACAR 10 ===")
print(f"Analizando combinaciones eficientes para {len(todos_los_cambios)} temas...\n")

combinaciones_validas = []

# Probamos todas las combinaciones posibles de notas para los temas que quedan/mejoran
for combo in itertools.product(opciones_nota, repeat=len(todos_los_cambios)):
    # Armamos un diccionario temporal con la simulación
    simulacion = mis_notas.copy()
    
    idx = 0
    # Asignamos las notas simuladas a los recuperatorios (solo si mejoran la nota)
    for tema in temas_a_mejorar:
        nota_simulada = combo[idx]
        if PUNTOS[nota_simulada] > PUNTOS[mis_notas[tema]]:
            simulacion[tema] = nota_simulada
        idx += 1
        
    # Asignamos las notas simuladas a los pendientes del 2do parcial
    for tema in temas_pendientes:
        simulacion[tema] = combo[idx]
        idx += 1
        
    # Calcular puntos de esta simulación
    pts_simulados = sum(PUNTOS[n] for n in simulacion.values() if n is not None)
    
    nex = calc_nota_examenes(pts_simulados)
    nfi = calc_nota_final(nex)
    
    if obtiene_nota_acta(nex, nfi) == 10:
        # Guardamos los cambios reales que se hicieron para no repetir duplicados infinitos
        cambios_str = []
        
        # Mostrar qué habría que hacer en recuperatorios
        for tema in temas_a_mejorar:
            if simulacion[tema] != mis_notas[tema]:
                cambios_str.append(f"Recuperar {tema}: {mis_notas[tema]} -> {simulacion[tema]}")
                
        # Mostrar qué habría que sacar en el 2do parcial
        for tema in temas_pendientes:
            cambios_str.append(f"2do Parcial ({tema}): {simulacion[tema]}")
            
        # Para evitar duplicados en la salida por lógica de combinaciones
        cambios_tupla = tuple(sorted(cambios_str))
        if cambios_tupla not in combinaciones_validas:
            combinaciones_validas.append(cambios_tupla)

# Ordenar combinaciones para mostrar primero las que requieren MENOS recuperatorios (más fáciles)
combinaciones_validas.sort(key=lambda x: len([s for s in x if "Recuperar" in s]))

# Mostrar las mejores opciones
for i, combo in enumerate(combinaciones_validas[:8], 1): # Limitamos a las 8 más eficientes
    print(f"Opción {i}:")
    for accion in combo:
        print(f"  ✔ {accion}")
    print("-" * 50)

