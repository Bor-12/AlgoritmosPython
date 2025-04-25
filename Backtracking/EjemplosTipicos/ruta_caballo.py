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

def ruta_caballo_recursivo(i, fila_actual, columna_actual, solucion, incremento):
    if i > len(solucion):
        return True
    else:
        solucion_encontrada = False
        k = 0
        while not solucion_encontrada and k < len(incremento):

            fila_actual +=  incremento[k][0]
            columna_actual += incremento[k][1]
            if fila_actual >= 0 and columna_actual >= 0 and \
                fila_actual < len(solucion) and columna_actual < len(solucion) and \
                    solucion[fila_actual][columna_actual] == 0:
                solucion[fila_actual][columna_actual] = i
                solucion_encontrada = ruta_caballo_recursivo(i + 1,fila_actual, columna_actual, solucion, incremento)
                if not solucion_encontrada:
                    solucion_encontrada[fila_actual][columna_actual] = 0
            k += 1
            return solucion_encontrada

ruta_caballo(5, 0, 0)