
def suma_subconjuntos(numeros, target):
    soluciones = []
    def backtrack(start, solucion_actual, suma_actual):
        if suma_actual ==  target:
            return soluciones.append(solucion_actual[:])
        if suma_actual > target:
            return
        for i in range(start, len(numeros)):
            solucion_actual.append(numeros[i])
            backtrack(i + 1, solucion_actual, suma_actual + numeros[i])
            solucion_actual.pop()
    backtrack(0,[],0)
    return soluciones

#otra forma de hacerlo
def suma_subconjuntos_por_resta(numeros, target):
    soluciones = []
    def backtrack(start, solucion_actual, suma_actual):
        if suma_actual ==  0:
            return soluciones.append(solucion_actual[:])
        if suma_actual < 0:
            return
        for i in range(start, len(numeros)):
            solucion_actual.append(numeros[i])
            backtrack(i + 1, solucion_actual, suma_actual - numeros[i])
            solucion_actual.pop()
    backtrack(0,[],target)
    return soluciones
numeros = [5,1,3,2,77, 0, 8, 3]
target = 99
print(suma_subconjuntos(numeros, target))
print(suma_subconjuntos_por_resta(numeros, target))

def suma_subconjuntos2(numeros, target) -> bool:
    def backtrack(start, suma_actual):
        if suma_actual == target:
            return True
        if suma_actual > target or start == len(numeros):
            return False
        for i in range(start, len(numeros)):
            if backtrack(i + 1, suma_actual + numeros[i]):
                return True
        return False

    return backtrack(0, 0)


numeros = [5,1,3,2,77, 0, 8, 3]
target = 99
print(suma_subconjuntos2(numeros, target))