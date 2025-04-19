from queue import PriorityQueue

from typing import List, Tuple, Union
# El algoritmo de Prim construye un árbol de expansión mínima partiendo de un nodo,
# añadiendo siempre la arista más corta que conecte un nodo del árbol con uno que aún no está en él.
def prim(lista_de_aristas, raiz, n):
    pq = PriorityQueue()
    visitados = [False] * n
    sol = []

    visitados[raiz] = True

    for peso, origen, destino in lista_de_aristas:
        if origen == raiz:
            pq.put((peso, origen, destino))
        elif destino == raiz:
            pq.put((peso, destino, origen))

    while len(sol) < n - 1 and not pq.empty():
        peso, origen, destino = pq.get()

        if not visitados[destino]:
            visitados[destino] = True
            sol.append((peso, origen, destino))

            for peso, a, b in lista_aristas:
                if a == destino and not visitados[b]:
                    pq.put((peso, a, b))
                elif b == destino and not visitados[a]:
                    pq.put((peso, b, a))

    return sol

lista_aristas = [
    (3, 2, 3),
    (8, 4, 6),
    (1, 0, 2),
    (2, 0, 3),
    (6, 0, 6),
    (9, 3, 5),
    (1, 3, 4),
    (5, 1, 5),
    (7, 1, 6),
    (5, 2, 6),
    (2, 1, 4)
]


sol = prim(lista_aristas, raiz=0, n=7)
print(sol)

print("Árbol de Expansión Mínima (MST) - Algoritmo de Prim:")
for peso, origen, destino in sol:
    print(f"Arista ({origen} - {destino}) con peso {peso}")
