from queue import PriorityQueue
from typing import List, Tuple

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

print(dijkstra(grafo, inicio=0))

