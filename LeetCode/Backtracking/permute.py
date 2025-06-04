#Problema 46
from typing import List
def generar_permutaciones(i,solucion_parcial, libres, nums, soluciones):
    if i == len(solucion_parcial):
        soluciones.append(solucion_parcial[:])
    else:
        for k in range(len(solucion_parcial)):
            if libres[k]:
                solucion_parcial[i] = nums[k]
                libres[k] = False
                generar_permutaciones(i +1, solucion_parcial, libres, nums, soluciones)
                libres[k] = True

def permute(nums: List[int]) -> List[List[int]]:
    solucion_parcial =  [None] * len(nums)
    soluciones = []
    libres = [True] * len(nums)
    generar_permutaciones(0,solucion_parcial, libres, nums, soluciones)
    return soluciones
print(permute([1,2,3]))
