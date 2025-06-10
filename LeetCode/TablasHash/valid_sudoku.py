from typing import List
# El problema no te pide si se podra completar, por lo tanto solo compruebo si es valido en la forma que esta actualmente
def isValidSudoku(board: List[List[str]]) -> bool:
    TAMANO_TABLERO = 9
    TAMANO_CUADRADO = 3
    VALORES_POSIBLES = 9  # del 1 al 9

    numeros_ocupados_en_filas = [[False] * VALORES_POSIBLES for _ in range(TAMANO_TABLERO)]
    numeros_ocupados_en_columnas = [[False] * VALORES_POSIBLES for _ in range(TAMANO_TABLERO)]
    numeros_ocupados_en_cajas = [[False] * VALORES_POSIBLES for _ in range(TAMANO_TABLERO)]

    for fila in range(TAMANO_TABLERO):
        for columna in range(TAMANO_TABLERO):
            letra = board[fila][columna]
            if letra == '.':
                continue

            numero = int(letra)
            indice_numero = numero - 1  # los indices van de 0 a 8

            id_caja = (fila // TAMANO_CUADRADO) * TAMANO_CUADRADO + (columna // TAMANO_CUADRADO)

            if (numeros_ocupados_en_filas[fila][indice_numero] or numeros_ocupados_en_columnas[columna][indice_numero]
                    or numeros_ocupados_en_cajas[id_caja][indice_numero]):
                return False

            numeros_ocupados_en_filas[fila][indice_numero] = True
            numeros_ocupados_en_columnas[columna][indice_numero] = True
            numeros_ocupados_en_cajas[id_caja][indice_numero] = True

    return True

# Solucion del video
from collections import defaultdict
def isValidSudoku2(board: List[List[str]]) -> bool:
    TAMANO_TABLERO = 9
    TAMANO_CUADRADO = 3

    columnas = defaultdict(set)
    filas = defaultdict(set)
    cuadrados = defaultdict(set)  # clave = (fila // 3, columna // 3)

    for fila in range(TAMANO_TABLERO):
        for columna in range(TAMANO_TABLERO):
            valor = board[fila][columna]
            if valor == ".":
                continue

            clave_cuadro = (fila // TAMANO_CUADRADO, columna // TAMANO_CUADRADO)

            if (
                    valor in filas[fila]
                    or valor in columnas[columna]
                    or valor in cuadrados[clave_cuadro]
            ):
                return False

            filas[fila].add(valor)
            columnas[columna].add(valor)
            cuadrados[clave_cuadro].add(valor)

    return True
print(isValidSudoku(board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))
print(isValidSudoku(board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))
print(isValidSudoku2(board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))
print(isValidSudoku2(board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))