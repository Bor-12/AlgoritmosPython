#Problema 39
def backtracking(comienzo, candidatos, solucion_parcial, suma_actual, suma_objetivo, soluciones):
    if suma_actual == suma_objetivo:
        soluciones.append(solucion_parcial[:])
    elif suma_actual > suma_objetivo:
        return
    else:
        for i in range(comienzo, len(candidatos)):

            solucion_parcial.append(candidatos[i])
            suma_nueva = suma_actual + candidatos[i]
            backtracking(i, candidatos,solucion_parcial , suma_nueva, suma_objetivo, soluciones)
            solucion_parcial.pop()


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    soluciones = []
    backtracking(0,candidates, [], 0, target, soluciones)
    return soluciones
print(combinationSum([2,3,6,7], 7))
print(combinationSum([2,3,5], 8))