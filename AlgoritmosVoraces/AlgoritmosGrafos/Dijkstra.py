from queue import PriorityQueue
from typing import List, Tuple



#El dijkstra trata de conseguir la distancia mínima de un nodo a todos los demás
def dijkstra(grafo: List[List[Tuple[int, int]]], inicio: int) -> Tuple[List[float], List[int]]:
    n = len(grafo)
    distancia = [float('inf')] * n
    predecesores = [-1] * n  # -1 indica que no tiene predecesor
    visitados = [False] * n

    distancia[inicio] = 0
    pq = PriorityQueue()
    pq.put((0, inicio))

    while not pq.empty():
        distancia_actual, nodo_actual = pq.get()

        if visitados[nodo_actual]:  # Si ya fue visitado, lo ignoramos
            continue

        visitados[nodo_actual] = True

        for vecino, peso in grafo[nodo_actual]:
            nueva_distancia = distancia[nodo_actual] + peso

            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                predecesores[vecino] = nodo_actual
                pq.put((nueva_distancia, vecino))

    return distancia, predecesores


grafo = [
    [(1, 10), (2, 3)],
    [(2, 1), (3, 2)],
    [(1, 4), (3, 8), (4, 2)],
    [(4, 7)],
    [(3, 9)]
]

distancias, predecesores = dijkstra(grafo, inicio=0)

print("Conexiones del árbol de caminos mínimos:")
for nodo, predecesor in enumerate(predecesores):
    if predecesor != -1:
        print(f"El nodo {predecesor} está conectado con el nodo {nodo}")
def dijkstra_2(grafo, inicio):
    n = len(grafo)
    distancia = [float('inf')] * n
    predecesores = [-1] * n
    visitados = [False] * n

    distancia[inicio] = 0

    for _ in range(n):
        # Buscar el nodo no visitado con menor distancia
        nodo_actual = -1
        min_distancia = float('inf')
        for i in range(n):
            if not visitados[i] and distancia[i] < min_distancia:
                min_distancia = distancia[i]
                nodo_actual = i

        if nodo_actual == -1:
            break  # No hay más nodos alcanzables

        visitados[nodo_actual] = True

        for vecino, peso in grafo[nodo_actual]:
            nueva_distancia = distancia[nodo_actual] + peso
            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                predecesores[vecino] = nodo_actual

    return distancia, predecesores


grafo = [
    [(1, 10), (2, 3)],
    [(2, 1), (3, 2)],
    [(1, 4), (3, 8), (4, 2)],
    [(4, 7)],
    [(3, 9)]
]

print(dijkstra_2(grafo, inicio=0))

