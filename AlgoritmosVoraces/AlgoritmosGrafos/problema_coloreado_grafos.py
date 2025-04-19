def colorear_grafo(grafo: dict[int, list[int]]) -> dict[int, int]:
    colores = {}

    for nodo in sorted(grafo.keys()):
        colores_vecinos = {colores[vecino] for vecino in grafo[nodo] if vecino in colores}
        color = 1
        while color in colores_vecinos:
            color += 1
        colores[nodo] = color

    return colores
grafo = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1]
}

colores = colorear_grafo(grafo)

for nodo in sorted(colores):
    print(f"Nodo {nodo} → Color {colores[nodo]}")
print(f"Colores usados: {max(colores.values())}")

