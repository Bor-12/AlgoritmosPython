def n_reinas(n):
    filas_libres = [True] * n
    diagonales_principales_libres = [True] * (2 * n - 1)
    diagonales_secundarias_libres = [True] * (2 * n - 1)
    sol = [None] * n
    n_reinas_recursivo(0, filas_libres, diagonales_principales_libres, diagonales_secundarias_libres, sol)

def n_reinas_recursivo(i, filas_libres, diagonales_principales_libres, diagonales_secundarias_libres, sol):
    n = len(sol)
    if i == n:
        print(sol)
    else:
        for k in range(n):
            if filas_libres[k] and diagonales_principales_libres[i -k + n -1] and diagonales_secundarias_libres[i + k]:
                sol[i] = k

                filas_libres[k] = False
                diagonales_principales_libres[i - k + n - 1] = False
                diagonales_secundarias_libres[i + k] = False

                n_reinas_recursivo(i + 1, filas_libres, diagonales_principales_libres, diagonales_secundarias_libres, sol)

                filas_libres[k] = True
                diagonales_principales_libres[i - k + n - 1] = True
                diagonales_secundarias_libres[i + k] = True
n_reinas(8)