"""
Uno de los problemas más conocidos que se resuelven mediante la técnica de backtracking es el de las N reinas de ajedrez. En este ejercicio se pide
 resolver el problema de las N torres, también usando backtracking.

Las torres se pueden mover en horizontal y vertical, por lo que se trata de ubicar N torres en un tablero cuadrado de N × N casillas, de manera que solo
haya una torre en cada fila y en cada columna, sin que se ataquen entre ellas.

En concreto, se pide escribir un programa que calcule todas las posibles soluciones y las imprima por pantalla.
"""

def N_torres(n):
    solucion = [-1] * n
    filas_libres = [True] * n
    N_torres_recursivo(0, solucion, filas_libres, n)
def N_torres_recursivo(i, solucion_parcial, filas_libres, n):
    if i == n:
        print(solucion_parcial)
    else:
        for k in range(n):
            if filas_libres[k]:
                filas_libres[k] = False
                solucion_parcial[i] = k
                N_torres_recursivo(i +1, solucion_parcial, filas_libres, n)
                filas_libres[k] = True

N_torres(4)
