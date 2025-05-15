#genera todos los numeros binarios de 2 ^n
def generar_binarios(n):
    solucion = [None] * n

    generar_binarios_recursivo(0, solucion)
def generar_binarios_recursivo(i, solucion_parcial):
    if i == len(solucion_parcial):
        print(solucion_parcial)
    else:
        for k in range(2):
            solucion_parcial[i]  =  k
            generar_binarios_recursivo(i +1,  solucion_parcial)
generar_binarios(n = 4)
print()
#restriccion , no se puede mas de 2 unos seguidos
def generar_binarios_sin11(n):
    solucion = [None] * n
    generar_binarios_recursivo_sin11(0, solucion, False)
def generar_binarios_recursivo_sin11(i, solucion_parcial, unoAntes):
    if i == len(solucion_parcial):
        print(solucion_parcial)
    else:
        for k in range(2):
            if k == 0 or (k == 1 and not  unoAntes):
                solucion_parcial[i]  =  k

                generar_binarios_recursivo_sin11(i +1,  solucion_parcial, k == 1)


generar_binarios_sin11(n = 4)

