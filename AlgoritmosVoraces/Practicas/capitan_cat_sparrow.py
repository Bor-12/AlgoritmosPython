"""
Capitán Cat Sparrow

El capitán Cat Sparrow es el gato más vago del planeta. Sparrow cuenta con varios lugares
de la casa en los que adora dormir y queremos que, para que no se canse al cambiar entre
sus distintas camas, le ayudemos a calcular el camino más corto entre ellas.

Hay que tener en cuenta que Sparrow es muy tiquismiquis y hay ciertas camas entre las
que no le gusta cambiar. Por ejemplo, si está en el edredón de la cama de sus dueños y
quiere cambiar de sitio, nunca irá a una silla del salón, pero sí a su cama en la habitación
de invitados. Debemos proporcionarle el camino que debe hacer sabiendo las conexiones
entre camas y la distancia que deberá recorrer en total.

Entrada:
La primera línea contiene dos enteros 𝑁 y 𝑀, que representan el número de camas que
tiene y el número de conexiones entre ellas.

Las siguientes 𝑀 líneas contienen 3 enteros 𝐶1, 𝐶2 y 𝐷 que indican que existe una
conexión entre las camas 𝐶1 y 𝐶2 y que están a distancia 𝐷.

La última línea contiene dos enteros 𝑆 y 𝐸 que representan las dos camas entre las que se
pide encontrar el camino mínimo.

Salida:
La salida debe mostrar, en la primera línea, la distancia total recorrida entre las camas.
La segunda línea debe mostrar las camas en las que se ha tumbado durante el camino
desde 𝑆 hasta 𝐸.

Ejemplo de entrada:
9 14
0 1 4
0 7 8
1 2 8
1 7 11
2 3 7
2 5 4
2 8 2
3 4 9
3 5 14
4 5 10
5 6 2
6 7 1
6 8 6
7 8 7
0 4

Ejemplo de salida:
21
0 7 6 5 4

Límites:
• 10 ≤ 𝑁 ≤ 1000
• 10 ≤ 𝑀 ≤ 150000
"""
def capturar_datos():
    num_camas, num_conexiones = map(int, input().split())
    grafo = {i: {} for i in range(num_camas)}

    for _ in range(num_conexiones):
        a, b, peso = map(int, input().split())
        grafo[a][b] = peso
        grafo[b][a] = peso

    inicio, destino = map(int, input().split())
    return num_camas, grafo, inicio, destino


def dijkstra(num_camas, grafo, inicio):
    distancia = [float('inf')] * num_camas
    predecesores = [-1] * num_camas
    visitados = [False] * num_camas

    distancia[inicio] = 0

    for _ in range(num_camas):
        nodo_actual = -1
        min_distancia = float('inf')
        for i in range(num_camas):
            if not visitados[i] and distancia[i] < min_distancia:
                min_distancia = distancia[i]
                nodo_actual = i

        if nodo_actual == -1:
            break

        visitados[nodo_actual] = True

        for vecino in grafo[nodo_actual]:
            peso = grafo[nodo_actual][vecino]
            nueva_distancia = distancia[nodo_actual] + peso
            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                predecesores[vecino] = nodo_actual

    return distancia, predecesores


def reconstruir_camino(predecesores, destino):
    camino = []
    actual = destino
    while actual != -1:
        camino.append(actual)
        actual = predecesores[actual]
    camino.reverse()
    return camino


def capitanCatSparrow():
    n, grafo, inicio, fin = capturar_datos()
    distancia_total, predecesores = dijkstra(n, grafo, inicio)
    camino = reconstruir_camino(predecesores, fin)
    print(distancia_total[fin])
    print(' '.join(map(str, camino)))


capitanCatSparrow()

