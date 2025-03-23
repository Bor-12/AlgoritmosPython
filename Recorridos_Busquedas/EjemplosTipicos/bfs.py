def bfs(vertice_inicial, vertice_final, grafo):
    n = len(grafo)
    cola = [vertice_inicial]
    visitados = [False] * n
    padre = [None] * n  # Para reconstruir el camino

    visitados[vertice_inicial] = True

    while cola:
        actual = cola.pop(0)
        if actual == vertice_final:
            break
        for vecino in grafo[actual]:
            if not visitados[vecino]:
                visitados[vecino] = True
                padre[vecino] = actual
                cola.append(vecino)

    # Reconstruir el camino desde vertice_final hacia atrás
    if not visitados[vertice_final]:
        return []  # No hay camino

    camino = []
    actual = vertice_final
    while actual is not None:
        camino.append(actual)
        actual = padre[actual]
    camino.reverse()

    return camino


grafo = {
    0: [2, 1],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

print(bfs(0, 4, grafo))
