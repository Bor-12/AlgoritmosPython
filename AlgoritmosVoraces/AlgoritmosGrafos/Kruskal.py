from queue import PriorityQueue
from typing import List, Tuple, Union


def find(conjunto_disjunto: List[int], nodo: int) -> int:
    representante = nodo
    while conjunto_disjunto[representante] >= 0:
        representante = conjunto_disjunto[representante]

    actual = nodo
    while conjunto_disjunto[actual] >= 0:
        padre = conjunto_disjunto[actual]
        conjunto_disjunto[actual] = representante
        actual = padre

    return representante


def union(conjunto_disjunto: List[int], raiz1: int, raiz2: int) -> int:
    if raiz1 == raiz2:
        return raiz1

    if conjunto_disjunto[raiz2] < conjunto_disjunto[raiz1]:
        conjunto_disjunto[raiz1] = raiz2
        return raiz2
    elif conjunto_disjunto[raiz2] > conjunto_disjunto[raiz1]:
        conjunto_disjunto[raiz2] = raiz1
        return raiz1
    else:
        conjunto_disjunto[raiz2] = raiz1
        conjunto_disjunto[raiz1] -= 1
        return raiz1


def kruskal(lista_de_aristas: List[Tuple[int, int, float]], n: int) -> Union[Tuple[int, List[Tuple[int, int, float]]], None]:
    pq = PriorityQueue()

    for origen, destino, peso in lista_de_aristas:
        pq.put((peso, (origen, destino)))

    conjunto_disjunto = [-1] * n
    sol = []

    while not pq.empty():
        peso, (origen, destino) = pq.get()
        x = find(conjunto_disjunto, origen)
        y = find(conjunto_disjunto, destino)

        if x != y:
            sol.append((origen, destino, peso))
            _ = union(conjunto_disjunto, x, y)

    if len(sol) == n - 1:
        return n, sol
    else:
        return None
