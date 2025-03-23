"""Dado un número entero n, genera todas las combinaciones de números enteros positivos cuya suma sea n, sin importar el orden."""
def combinaciones_suma_enteros(n):
    soluciones = []
    def backtrack(lista_actual):
        if sum(lista_actual) == n:
            return soluciones.append(lista_actual[:])
        elif sum(lista_actual) > n:
            return
        for i in range(1, n + 1):
            lista_actual.append(i)
            backtrack(lista_actual)
            lista_actual.pop()
    backtrack([])
    return soluciones
print(combinaciones_suma_enteros(5))