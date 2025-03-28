def capturar_datos():
    entrada = input().split()
    numero_de_camas = int(entrada[0])
    numero_de_conexiones_entre_camas = int(entrada[1])

    grafo = {i: [] for i in range(numero_de_camas)}

    for _ in range(numero_de_conexiones_entre_camas):
        c1, c2, d = map(int, input().split())
        grafo[c1].append((c2, d))
        grafo[c2].append((c1, d))

    s, e = map(int, input().split())

    return numero_de_camas, grafo, s, e


def encontrar_camino_minimo(n, grafo, inicio, fin):
    distancias = [float('inf')] * n
    visitado = [False] * n
    anterior = [-1] * n
    distancias[inicio] = 0

    # Cola de prioridad simulada como lista (sin imports)
    cola = [(0, inicio)]  # (distancia, nodo)

    while cola:
        # Buscar el nodo con menor distancia actual (simula heapq)
        min_idx = 0
        for i in range(1, len(cola)):
            if cola[i][0] < cola[min_idx][0]:
                min_idx = i
        distancia_actual, nodo_actual = cola.pop(min_idx)

        if visitado[nodo_actual]:
            continue
        visitado[nodo_actual] = True

        if nodo_actual == fin:
            break

        for vecino, peso in grafo[nodo_actual]:
            if visitado[vecino]:
                continue
            nueva_dist = distancia_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                anterior[vecino] = nodo_actual
                cola.append((nueva_dist, vecino))

    # Reconstruir el camino
    camino = []
    actual = fin
    while actual != -1:
        camino.append(actual)
        actual = anterior[actual]
    camino.reverse()

    return distancias[fin], camino


def capitanCatSparrow():
    n, grafo, inicio, fin = capturar_datos()
    distancia_total, camino = encontrar_camino_minimo(n, grafo, inicio, fin)
    print(distancia_total)
    print(' '.join(map(str, camino)))


capitanCatSparrow()
