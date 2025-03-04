from queue import PriorityQueue
from typing import Dict, List, Tuple
def dijkstra(grafo: Dict[int, List[Tuple[int, int]]], inicio: int) -> Tuple[Dict[int, float], Dict[int, int]]:
    distancia = {}
    for nodo in grafo:
        distancia[nodo] = float('inf')
    distancia[inicio] = 0
    predecesores = {}
    for nodo in grafo:
        predecesores[nodo] = None
    pq = PriorityQueue()
    pq.put((0, inicio))
    while not pq.empty():
        distancia_actual, nodo_actual = pq.get()

        for vecino, peso in grafo[nodo_actual]:
            nueva_distancia = distancia_actual + peso

            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                predecesores[vecino] = nodo_actual
                pq.put((nueva_distancia, vecino))
    return distancia, predecesores
grafo = {
    0: [(1, 10), (2, 3)],
    1: [(2, 1), (3, 2)],
    2: [(1, 4), (3, 8), (4, 2)],
    3: [(4, 7)],
    4: [(3, 9)]
}
print(dijkstra(grafo, inicio = 0))







