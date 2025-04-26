


def hay_camino(tablero, fila_inicio, columna_inicio, fila_final, columna_final):
    # Orden de movimiento:
    # ↓  →  ↑  ←
    incremento = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]
    tablero[fila_inicio][columna_inicio] = 'P'

    return crear_camino(tablero, fila_inicio , columna_inicio, fila_final, columna_final, incremento)
def crear_camino(tablero, fila_actual, columna_actual, fila_final, columna_final, incremento):
    if fila_actual == fila_final and columna_actual == columna_final:
        return True
    else:
        solucion_encontrada = False
        k = 0
        while not solucion_encontrada and k < len(incremento):
            nueva_fila = fila_actual + incremento[k][0]
            nueva_columna = columna_actual + incremento[k][1]
            if nueva_fila >= 0 and nueva_columna >= 0 \
                and nueva_fila < len(tablero) and nueva_columna < len(tablero[nueva_fila]) \
                and tablero[nueva_fila][nueva_columna] == 'E':
                tablero[nueva_fila][nueva_columna] = 'P'
                solucion_encontrada = crear_camino(tablero, nueva_fila, nueva_columna, fila_final, columna_final, incremento)
                if not solucion_encontrada:
                    tablero[nueva_fila][nueva_columna] = 'E'
            k += 1
        return solucion_encontrada

def imprimir_matriz(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            print(" %5c" % (matriz[i][j]),end='')
        print()


tablero = [
    ['E', 'W', 'E', 'E', 'E', 'E', 'E', 'E', 'W', 'E', 'W', 'W'],
    ['E', 'E', 'E', 'W', 'W', 'W', 'E', 'W', 'W', 'E', 'E', 'E'],
    ['W', 'W', 'E', 'E', 'W', 'E', 'E', 'E', 'W', 'W', 'W', 'E'],
    ['W', 'E', 'E', 'W', 'W', 'E', 'W', 'E', 'E', 'E', 'E', 'E'],
    ['E', 'E', 'W', 'W', 'E', 'E', 'E', 'E', 'W', 'E', 'W', 'W'],
    ['E', 'W', 'W', 'E', 'E', 'W', 'W', 'W', 'W', 'E', 'E', 'E'],
    ['E', 'E', 'E', 'E', 'W', 'W', 'E', 'E', 'E', 'E', 'W', 'E'],
    ['E', 'W', 'E', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'E'],
    ['E', 'W', 'E', 'E', 'E', 'E', 'W', 'E', 'E', 'E', 'W', 'W'],
    ['E', 'W', 'W', 'E', 'W', 'E', 'E', 'E', 'W', 'E', 'E', 'E'],
    ['W', 'W', 'E', 'E', 'W', 'W', 'E', 'W', 'W', 'E', 'W', 'E'],
    ['E', 'E', 'E', 'W', 'W', 'E', 'E', 'E', 'W', 'E', 'W', 'E']
]
imprimir_matriz(tablero)
print("Laberinto resuelto: ")
if hay_camino(tablero, 0, 0, len(tablero) -1, len(tablero[0]) - 1):
    imprimir_matriz(tablero)
