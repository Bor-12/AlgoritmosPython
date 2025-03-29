"""
Estrategia: Multiplicación de matrices con Strassen

Objetivo:
- Multiplicar dos matrices cuadradas A y B de tamaño n x n (donde n es potencia de 2)
- Reducir el número de multiplicaciones de 8 (en el método clásico) a 7

Pasos:

1. Caso base:
    - Si n == 1 (es decir, matrices 1x1), simplemente multiplicar el único elemento.

2. Dividir:
    - Dividir cada matriz A y B en 4 submatrices de tamaño n/2 × n/2:
        A = | A11  A12 |
            | A21  A22 |
        B = | B11  B12 |
            | B21  B22 |

3. Calcular 7 productos intermedios (en lugar de 8 como en el método clásico):

    M1 = (A11 + A22) × (B11 + B22)
    M2 = (A21 + A22) × B11
    M3 = A11 × (B12 - B22)
    M4 = A22 × (B21 - B11)
    M5 = (A11 + A12) × B22
    M6 = (A21 - A11) × (B11 + B12)
    M7 = (A12 - A22) × (B21 + B22)

4. Combinar los resultados para formar la matriz resultado C:

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

5. Combinar C11, C12, C21, C22 en una única matriz C de tamaño n x n.

Resultado:
- Este algoritmo reduce la complejidad de O(n^3) a O(n^log2(7)) ≈ O(n^2.81)

Nota:
- Si las matrices no son de tamaño potencia de 2, se pueden rellenar con ceros hasta llegar a ese tamaño., pero es mucho menos eficiente que multiplicar
como normalmente hariamos
"""

def rellenar_con_ceros(matriz_a, matriz_b):
    # Obtener dimensiones originales
    filas_a, columnas_a = len(matriz_a), len(matriz_a[0])
    filas_b, columnas_b = len(matriz_b), len(matriz_b[0])

    # Nueva dimensión: el máximo de las dimensiones, redondeado hacia la siguiente potencia de 2
    max_dim = max(filas_a, columnas_a, filas_b, columnas_b)

    # Si ya es potencia de 2, se mantiene; si no, se redondea hacia arriba
    nueva_dimension = 1
    while nueva_dimension < max_dim:
        nueva_dimension *= 2

    # Rellenar matriz A con ceros
    matriz_a_rellena = [
        fila + [0] * (nueva_dimension - columnas_a) for fila in matriz_a
    ] + [[0] * nueva_dimension for _ in range(nueva_dimension - filas_a)]

    # Rellenar matriz B con ceros
    matriz_b_rellena = [
        fila + [0] * (nueva_dimension - columnas_b) for fila in matriz_b
    ] + [[0] * nueva_dimension for _ in range(nueva_dimension - filas_b)]

    return matriz_a_rellena, matriz_b_rellena, nueva_dimension
def recortar_matriz(matriz, filas, columnas):
    return [fila[:columnas] for fila in matriz[:filas]]

def dividir_matriz_en_4(matriz):
    mitad = len(matriz) // 2
    return (
        [fila[:mitad] for fila in matriz[:mitad]],      # submatriz superior izquierda
        [fila[mitad:] for fila in matriz[:mitad]],      # submatriz superior derecha
        [fila[:mitad] for fila in matriz[mitad:]],      # submatriz inferior izquierda
        [fila[mitad:] for fila in matriz[mitad:]]       # submatriz inferior derecha
    )

def sumar_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def restar_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def combinar_submatrices(C11, C12, C21, C22):
    resultado = []
    for i in range(len(C11)):
        resultado.append(C11[i] + C12[i])
    for i in range(len(C21)):
        resultado.append(C21[i] + C22[i])
    return resultado


def strassen(matriz_a, matriz_b, dimension):
    """
    Verifica si 'dimension' NO es potencia de 2.
    En binario, un número que es potencia de 2 tiene exactamente un solo bit en 1
    (por ejemplo: 1 = 0001, 2 = 0010, 4 = 0100, 8 = 1000).
    Si hacemos una puerta AND (operación binaria &) entre 'dimension' y 'dimension - 1',
    el resultado será 0 solo si 'dimension' es potencia de 2.
    Ejemplo potencia de 2:
    8 (1000) & 7 (0111) = 0000 → 0 → es potencia de 2.
    Ejemplo que NO es potencia de 2:
    6 (0110) & 5 (0101) = 0100 → distinto de 0 → NO es potencia de 2.
    Si el resultado es distinto de 0, entonces 'dimension' NO es potencia de 2 y se debe rellenar con ceros.
    """
    if dimension & (dimension - 1) != 0:
        matriz_a_rellena, matriz_b_rellena, nueva_dimension = rellenar_con_ceros(matriz_a, matriz_b)
        resultado = strassen(matriz_a_rellena, matriz_b_rellena, nueva_dimension)
        return recortar_matriz(resultado, len(matriz_a), len(matriz_b[0]))

    if dimension == 1:
        return [[matriz_a[0][0] * matriz_b[0][0]]]
    #dividir:
    A11, A12, A21, A22 = dividir_matriz_en_4(matriz_a)
    B11, B12, B21, B22 = dividir_matriz_en_4(matriz_b)
    nueva_dimension = dimension // 2
    #calcular:
    M1 = strassen(sumar_matrices(A11, A22), sumar_matrices(B11, B22), nueva_dimension)
    M2 = strassen(sumar_matrices(A21, A22), B11, nueva_dimension)
    M3 = strassen(A11, restar_matrices(B12, B22), nueva_dimension)
    M4 = strassen(A22, restar_matrices(B21, B11), nueva_dimension)
    M5 = strassen(sumar_matrices(A11, A12), B22, nueva_dimension)
    M6 = strassen(restar_matrices(A21, A11), sumar_matrices(B11, B12), nueva_dimension)
    M7 = strassen(restar_matrices(A12, A22), sumar_matrices(B21, B22), nueva_dimension)
    #Convinar:
    C11 = sumar_matrices(restar_matrices(sumar_matrices(M1, M4), M5), M7)
    C12 = sumar_matrices(M3, M5)
    C21 = sumar_matrices(M2, M4)
    C22 = sumar_matrices(sumar_matrices(restar_matrices(M1, M2), M3), M6)

    return combinar_submatrices(C11, C12, C21, C22)

matriz_a = [
    [1, 2],
    [3, 4]
]

matriz_b = [
    [5, 6],
    [7, 8]
]

n = 2
print(strassen(matriz_a, matriz_b, n))  # Resultado esperado: [[19, 22], [43, 50]]

# PRUEBA 2
matriz_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz_b = [
    [7, 8],
    [9, 10],
    [11, 12]
]

n = 3
print(strassen(matriz_a, matriz_b, n))  # Resultado esperado: [[58, 64], [139, 154]]

# PRUEBA 3
matriz_a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

matriz_b = [
    [1, 0],
    [0, 1],
    [1, 0],
    [0, 1]
]

n = 5
print(strassen(matriz_a, matriz_b, n))  # Resultado esperado: [[4, 6], [12, 14]]
#PRUEBA 4
matriz_a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matriz_b = [
    [1, 0],
    [0, 1],
    [1, 0],
    [0, 1]
]
n = 5
print(strassen(matriz_a, matriz_b, n))  # Resultado esperado: [[4, 6], [12, 14], [20, 22]]
#Como podemos ver de esta fomra se divide en 8 subproblemas por lo que su complejidad es mayor
def multiplicar_matrices_por_bloques(matriz_a, matriz_b):
    # matriz_a: m x n, matriz_b: n x p
    filas_a, columnas_a = len(matriz_a), len(matriz_a[0])
    filas_b, columnas_b = len(matriz_b), len(matriz_b[0])

    if columnas_a != filas_b:
        raise ValueError("No se pueden multiplicar: dimensiones no compatibles.")

    matriz_a_expandida, matriz_b_expandida, dimension_comun = rellenar_con_ceros(matriz_a, matriz_b)
    matriz_resultado_expandida = multiplicar_divide_venceras(matriz_a_expandida, matriz_b_expandida)
    return recortar_matriz(matriz_resultado_expandida, filas_a, columnas_b)


def multiplicar_divide_venceras(matriz_a, matriz_b):
    dimension = len(matriz_a)

    if dimension == 1:
        return [[matriz_a[0][0] * matriz_b[0][0]]]

    # Dividir en submatrices
    a11, a12, a21, a22 = dividir_matriz_en_4(matriz_a)
    b11, b12, b21, b22 = dividir_matriz_en_4(matriz_b)

    # Calcular los productos parciales clásicos
    c11 = sumar_matrices(
        multiplicar_divide_venceras(a11, b11),
        multiplicar_divide_venceras(a12, b21)
    )

    c12 = sumar_matrices(
        multiplicar_divide_venceras(a11, b12),
        multiplicar_divide_venceras(a12, b22)
    )

    c21 = sumar_matrices(
        multiplicar_divide_venceras(a21, b11),
        multiplicar_divide_venceras(a22, b21)
    )

    c22 = sumar_matrices(
        multiplicar_divide_venceras(a21, b12),
        multiplicar_divide_venceras(a22, b22)
    )

    # Combinar submatrices en la matriz final
    return combinar_submatrices(c11, c12, c21, c22)

matriz_a = [
    [1, 2],
    [3, 4]
]

matriz_b = [
    [5, 6],
    [7, 8]
]

print(multiplicar_matrices_por_bloques(matriz_a, matriz_b))  # Resultado esperado: [[19, 22], [43, 50]]

matriz_a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

matriz_b = [
    [1, 0],
    [0, 1],
    [1, 0],
    [0, 1]
]

print(multiplicar_matrices_por_bloques(matriz_a, matriz_b))  # Resultado esperado: [[4, 6], [12, 14]]

matriz_a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matriz_b = [
    [1, 0],
    [0, 1],
    [1, 0],
    [0, 1]
]

print(multiplicar_matrices_por_bloques(matriz_a, matriz_b))  # Resultado esperado: [[4, 6], [12, 14], [20, 22]]