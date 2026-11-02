import heapq
from algoritmo import camino_minimo_piramide

def dijkstra_piramide(piramide):
    """Implementacion de referencia con Dijkstra O(n^2 log n) para validar correctitud y medir tiempos."""
    if not piramide:
        return 0, []
    n = len(piramide)
    dist = [[float('inf')] * (i + 1) for i in range(n)]
    padre = [[None] * (i + 1) for i in range(n)]
    
    dist[0][0] = piramide[0][0]
    pq = [(piramide[0][0], 0, 0)]
    
    while pq:
        d, r, c = heapq.heappop(pq)
        if d > dist[r][c]:
            continue
        vecinos = []
        if r + 1 < n:
            vecinos.append((r + 1, c))
            vecinos.append((r + 1, c + 1))
        if c > 0:
            vecinos.append((r, c - 1))
        if c < r:
            vecinos.append((r, c + 1))
            
        for nr, nc in vecinos:
            nd = d + piramide[nr][nc]
            if nd < dist[nr][nc]:
                dist[nr][nc] = nd
                padre[nr][nc] = [r, c]
                heapq.heappush(pq, (nd, nr, nc))
                
    min_val = min(dist[n - 1])
    min_col = dist[n - 1].index(min_val)
    
    camino = []
    curr = [n - 1, min_col]
    while curr is not None:
        camino.append(curr)
        curr = padre[curr[0]][curr[1]]
    return min_val, camino[::-1]

def correr_tests():
    casos = [
        ("Caso 1 fila", [[7]]),
        ("Caso 2 filas", [[5], [2, 9]]),
        ("Caso desvío lateral simple", [
            [1],
            [100, 1],
            [1, 1, 100],
            [1, 100, 100, 100]
        ]),
        ("Caso Patologico Serpiente (Zig-Zag)", [
            [1],
            [999, 1],
            [1, 1, 1],
            [1, 999, 999, 999],
            [1, 1, 1, 1, 999],
            [999, 999, 999, 1, 999, 999]
        ])
    ]
    
    for nombre, piramide in casos:
        val_pd, cam_pd = camino_minimo_piramide(piramide)
        val_dij, cam_dij = dijkstra_piramide(piramide)
        suma_camino = sum(piramide[r][c] for r, c in cam_pd)
        assert val_pd == val_dij == suma_camino, f"Fallo en {nombre}: PD={val_pd}, Dij={val_dij}, Suma={suma_camino}"
        print(f"[OK] {nombre} -> Costo Minimo: {val_pd} | Pasos del camino: {len(cam_pd)} | Camino: {cam_pd}")

if __name__ == "__main__":
    correr_tests()


