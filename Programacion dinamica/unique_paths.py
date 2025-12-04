#Problema 62
#Primero quise saber como hacerlo por backtracking haciendo todas las convinacines de caminos, para pensar en como hacer dp en este problema



def uniquePaths(m: int, n: int) -> int:
    solucion_parcial = [None] * (m + n - 2)
    movimientos = [("D", 1, 0), ("R", 0, 1)]
    soluciones = []

    numero_soluciones = backtracking(
        0, 0, solucion_parcial, 0,
        movimientos, soluciones, m, n)

    return numero_soluciones, soluciones


def backtracking(fila_actual, columna_actual,
                 solucion_parcial, posicion_actual_solucion_parcial,
                 movimientos, soluciones,
                 filas, columnas):

    if fila_actual == filas - 1 and columna_actual == columnas - 1:
        soluciones.append(solucion_parcial.copy())
        return 1

    total = 0
    for letra, delta_fila, delta_columna in movimientos:
        nueva_fila = fila_actual + delta_fila
        nueva_columna = columna_actual + delta_columna

        if nueva_fila < filas and nueva_columna < columnas:
            solucion_parcial[posicion_actual_solucion_parcial] = letra
            total += backtracking(nueva_fila, nueva_columna,
                                  solucion_parcial, posicion_actual_solucion_parcial + 1,
                                  movimientos, soluciones,
                                  filas, columnas)
    return total
print(uniquePaths(m = 3 ,  n = 2))
print(uniquePaths(m = 3 ,  n = 7))


# Se puede acortar el número de llamadas guardando en memo el número de caminos
# desde cada celda (fila_actual, columna_actual) para no recalcular subproblemas repetidos.
def uniquePathsDp(m: int, n: int) -> int:
    solucion_parcial = [None] * (m + n - 2)
    movimientos = [("D", 1, 0), ("R", 0, 1)]
    memo = {} # clave (numero filas restantes, numero columnas restantes) -> caminos unicos (int)

    numero_soluciones = backtrackingDp(0, 0,movimientos, m, n, memo)

    return numero_soluciones


def backtrackingDp(fila_actual, columna_actual, movimientos, filas, columnas, memo):
    if fila_actual == filas - 1 and columna_actual == columnas - 1:
        return 1
    total = 0
    if (fila_actual, columna_actual) in memo:
        return memo[(fila_actual, columna_actual)]
    for _, delta_fila, delta_columna in movimientos:
        nueva_fila = fila_actual + delta_fila
        nueva_columna = columna_actual + delta_columna

        if nueva_fila < filas and nueva_columna < columnas:
            total += backtrackingDp(nueva_fila, nueva_columna, movimientos, filas, columnas, memo)
    memo[(fila_actual, columna_actual)] = total
    return total

print(uniquePathsDp(m = 3 ,  n = 2))
print(uniquePathsDp(m = 3 ,  n = 7))


from math import factorial
#Existe una formula para ver el nuemro de convinaciones pero asi no se  aprende nada de progra :)
def uniquePathsFormula(m: int, n: int) -> int:
    return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)


print(uniquePathsFormula(m = 3 ,  n = 2))
print(uniquePathsFormula(m = 3 ,  n = 7))