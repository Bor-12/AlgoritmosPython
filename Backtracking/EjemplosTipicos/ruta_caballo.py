def ruta_caballo(n, fila_inicial, columna_inicial):
    incremento =  [(1,-2),(2,-1),(2,1),(1,2), \
                   (-1,2),(-2,1),(-2,-1),(-1,-2)]
    solucion = [None] * n
    for i in range(n):
        solucion[i] = [0] * n
    solucion[fila_inicial][columna_inicial] = 1

    if ruta_caballo_recursivo(2, fila_inicial, columna_inicial, solucion, incremento):
        imprimir_matriz(solucion)
def imprimir_matriz(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            print(" %5d" % (matriz[i][j]),end='')
        print()

def ruta_caballo_recursivo(i, fila_actual, columna_actual, solucion, incremento):
    if i > len(solucion) ** 2:
        return True
    else:
        solucion_encontrada = False
        k = 0
        while not solucion_encontrada and k < len(incremento):
            nueva_fila = fila_actual + incremento[k][0]
            nueva_columna = columna_actual + incremento[k][1]
            if nueva_fila >= 0 and nueva_columna >= 0 and \
                nueva_fila < len(solucion) and nueva_columna <len(solucion) \
                    and solucion[nueva_fila][nueva_columna] == 0:

                solucion[nueva_fila][nueva_columna] = i
                solucion_encontrada = ruta_caballo_recursivo(i + 1,nueva_fila, nueva_columna, solucion, incremento)
                if not solucion_encontrada:
                    solucion[nueva_fila][nueva_columna] = 0
            k += 1
        return solucion_encontrada

ruta_caballo(5, 0, 0)