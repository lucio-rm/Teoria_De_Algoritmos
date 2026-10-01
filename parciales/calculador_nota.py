# cuánto vale cada corrección
PUNTOS = {"B": 4, "B-": 3, "B=": 2, "R": 1, "M": 0}

def calc_nota_examenes(puntos):
    nota = 0.37 * puntos + 0.3
    if nota > 10:
        return 10.0
    return round(nota, 2)

def calc_nota_final(nota_ex):
    return 10.0 * 0.30 + nota_ex * 0.70

# un par de combinaciones 
combinaciones = [
    ("7 'B' (Máximo posible)", 28),
    ("1 'B-' y 6 'B'", 27),
    ("2 'B-' y 5 'B'", 26),
    ("3 'B-' y 4 'B'", 25),
    ("1 'B=' y 6 'B'", 26),
    ("2 'B=' y 5 'B'", 24),
    ("3 'B=' y 4 'B'", 22),
    ("4 'B=' y 3 'B'", 20),
    ("5 'B=' y 2 'B'", 18),
]

print(f"{'Composición de Notas':<25} | {'Puntos':<6} | {'Nota Ex.':<8} | {'Final s/Red':<12} | {'Nota Acta'}")
print("-" * 70)

for desc, pts in combinaciones:
    nex = calc_nota_examenes(pts)
    nfi = calc_nota_final(nex)
    
    # Lógica de redondeo considerando el peso de la nota de exámenes en las 50 centésimas (e.g. 9.5, 8.5, etc.)
    # Si la parte decimal está muy cerca de 0.5
    decimal = round(nfi - int(nfi), 2)
    if decimal == 0.50:
        # Tira hacia el lado de la nota de exámenes. 
        # Si la nota de exámenes es más alta que el promedio, redondea hacia arriba.
        if nex > nfi:
            acta = int(nfi) + 1
        else:
            acta = int(nfi)
    else:
        # Redondeo normal para otros casos
        acta = round(nfi)
        
    print(f"{desc:<25} | {pts:<6} | {nex:<8.2f} | {nfi:<12.2f} | {acta}")

