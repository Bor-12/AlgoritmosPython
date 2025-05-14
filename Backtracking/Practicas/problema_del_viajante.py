import math
def capturar_datos():
    n = int(input())
    coordenadas = []
    for _ in range(n):
        x, y = map(float, input().split())
        coordenadas.append((x, y))
    return coordenadas

def distancia(ciudad1, ciudad2):
    return math.sqrt((ciudad1[0] - ciudad2[0])**2 + (ciudad1[1] - ciudad2[1])**2)

def calcular_matriz_distancias(coordenadas):
    n = len(coordenadas)
    matriz = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            d = distancia(coordenadas[i], coordenadas[j])
            matriz[i][j] = d
            matriz[j][i] = d
    return matriz

def tsp(coordenadas):
    n = len(coordenadas)
    matriz = calcular_matriz_distancias(coordenadas)
    visitados = [False]*n
    camino_actual = [0]
    visitados[0] = True
    mejor_camino = []
    mejor_distancia = [float('inf')]

    tsp_recursivo(0, 0.0, 1, camino_actual, visitados, mejor_camino, mejor_distancia, matriz)

    return mejor_distancia[0], mejor_camino

def tsp_recursivo(ciudad_actual, distancia_actual, nivel, camino_actual, visitados, mejor_camino, mejor_distancia, matriz):
    n = len(matriz)

    if nivel == n:
        distancia_total = distancia_actual + matriz[ciudad_actual][0]
        if distancia_total < mejor_distancia[0]:
            mejor_distancia[0] = distancia_total
            mejor_camino.clear()
            mejor_camino.extend(camino_actual)
        return

    for siguiente in range(1, n):  # No hace falta visitar la 0 porque es el origen
        if not visitados[siguiente]:
            nueva_distancia = distancia_actual + matriz[ciudad_actual][siguiente]
            if nueva_distancia < mejor_distancia[0]:  # Poda si ya supera la mejor distancia
                visitados[siguiente] = True
                camino_actual.append(siguiente)
                tsp_recursivo(siguiente, nueva_distancia, nivel + 1, camino_actual, visitados, mejor_camino, mejor_distancia, matriz)
                camino_actual.pop()
                visitados[siguiente] = False

coordenadas = capturar_datos()
distancia_min, camino = tsp(coordenadas)

print(f"{distancia_min:.4f}")
print(" ".join(map(str, camino)))
