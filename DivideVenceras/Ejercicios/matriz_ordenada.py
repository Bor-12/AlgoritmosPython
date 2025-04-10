"""
Se pide implementar un algoritmo basado en la estrategia de divide y vencerás para determinar si una matriz A de números enteros está “ordenada”
por filas y columnas independientemente. Para ello, los elementos de cada fila y cada columna deben aparecer en orden no-decreciente.
La matriz A no es necesariamente cuadrada. La siguiente matriz estaría ordenada según el criterio descrito:

        A =
            ⎛ 1   3   6   8  10 ⎞
            ⎜ 2   4   7   9  10 ⎟
            ⎜ 4   8  11  14  14 ⎟
            ⎝ 5  10  12  15  16 ⎠

Cada fila y cada columna está en orden no-decreciente, por lo que A cumple con el criterio.
"""
import numpy as np


def es_matriz_ordenada(matriz):
    filas, columnas = matriz.shape
    if filas == 1 and columnas == 1:
        return True
    elif filas == 0 or columnas == 0:
        return True
    else:
        mitad_filas = filas // 2
        mitad_columnas = columnas // 2

        elementos_centrales_ordenados = True

        # Recorre filas y comprueba si el último elemento de la izquierda
        # es menor o igual al primero de la derecha
        i = 0
        while i < filas and elementos_centrales_ordenados:
            elementos_centrales_ordenados = matriz[i, mitad_columnas - 1] <= matriz[i, mitad_columnas]
            i += 1

        # Recorre columnas y comprueba si el último elemento de arriba
        # es menor o igual al primero de abajo
        j = 0
        while j < columnas and elementos_centrales_ordenados:
            elementos_centrales_ordenados = matriz[mitad_filas - 1, j] <= matriz[mitad_filas, j]
            j += 1

        return (elementos_centrales_ordenados and es_matriz_ordenada(matriz[:mitad_filas, :mitad_columnas]) and es_matriz_ordenada(matriz[:mitad_filas, mitad_columnas:])
                and es_matriz_ordenada(matriz[mitad_filas:, :mitad_columnas]) and es_matriz_ordenada(matriz[mitad_filas:, mitad_columnas:]))

A = np.array([
    [1, 3, 6, 8, 10],
    [2, 4, 9, 7, 10],
    [4, 8, 10, 14, 13],
    [5, 10, 12, 15, 14]
])


print(es_matriz_ordenada(A))
A = np.array([
    [1, 3, 6, 8, 10],
    [2, 4, 7, 9, 10],
    [4, 8, 11, 14, 14],
    [5, 10, 12, 15, 16]
])
print(es_matriz_ordenada(A))
