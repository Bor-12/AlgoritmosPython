#Problema 47
from typing import List


def generar_permutaciones(i, solucion_parcial,  frecuencias, candidatos, soluciones):
    if i == len(solucion_parcial):
        soluciones.append(solucion_parcial[:])
    else:
        for k in range(len(candidatos)):
            if frecuencias[candidatos[k]] > 0:
                frecuencias[candidatos[k]] -= 1
                solucion_parcial[i] = candidatos[k]
                generar_permutaciones(i +1,  solucion_parcial,frecuencias, candidatos, soluciones)
                frecuencias[candidatos[k]] += 1
def permuteUnique(nums: List[int]) -> List[List[int]]:
    frecuencias = {}
    candidatos = []
    for num in nums:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1
            candidatos.append(num)

    print(frecuencias)
    solucion_parcial = [None] * len(nums)
    soluciones = []
    generar_permutaciones(0, solucion_parcial, frecuencias, candidatos, soluciones)
    return soluciones
print(permuteUnique([1,1,2]))