#Problema 74
#Lo primero que se me ocurrio O(log(m) + log(n))
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    #primero busco la fila en donde esta
    izquierda = 0
    derecha = len(matrix) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if matrix[medio][0] <= target:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    fila = derecha
    izquierda = 0
    derecha = len(matrix[fila])
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if matrix[fila][medio] == target:
            return True
        elif matrix[fila][medio] <= target:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return False
#La complejidad que piden en el enunciado O(log(m* n))
def searchMatrix2(matrix, target):
    #Trato a la matriz como su fuese un array
    filas = len(matrix)
    columnas = len(matrix[0])
    izquierda = 0
    derecha = filas * columnas - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        fila = medio // columnas
        columna = medio % columnas
        if matrix[fila][columna] == target:
            return True
        elif matrix[fila][columna] <= target:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return False



matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3
print(searchMatrix(matrix, target))  # → True
print(searchMatrix2(matrix, target))
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 13
print(searchMatrix(matrix, target))  # → False
print(searchMatrix2(matrix, target))
