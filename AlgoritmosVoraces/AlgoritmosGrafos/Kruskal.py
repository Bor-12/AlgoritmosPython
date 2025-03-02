from queue import PriorityQueue

def find(conjunto_disjunto, vertice):
    if conjunto_disjunto[vertice] == -1:
        return vertice
    return conjunto_disjunto[vertice]

def union(conjunto_disjunto, raiz1, raiz2):
        conjunto_disjunto[raiz2] = raiz1

def kruskal(lista_de_aristas, n):
    pq = PriorityQueue()
    for peso, origen, destino in lista_de_aristas:
        pq.put((peso, origen, destino))
    conjunto_disjunto = [-1] * n
    sol = []

    while len(sol) < n:
        peso, origen, destino = pq.get()
        x = find(conjunto_disjunto, origen)
        y = find(conjunto_disjunto, destino)

        if x != y:
            sol.append((peso, origen, destino))
            union(conjunto_disjunto, x, y)

    return sol


lista_aristas = [
    (3, 2, 3),
    (8, 4, 6),
    (1, 0, 2),
    (2, 0, 3) ,
    (6, 0, 6),
    (9, 3, 5),
    (1, 3, 4),
    (5, 1, 5),
    (7, 1, 6),
    (5, 2, 6),
    (2, 1, 4)
]


sol = kruskal(lista_aristas, 7)

# Imprimir el Árbol de Expansión Mínima
print("Árbol de Expansión Mínima (MST):")
for peso, origen, destino in sol:
    print(f"Arista ({origen} - {destino}) con peso {peso}")

