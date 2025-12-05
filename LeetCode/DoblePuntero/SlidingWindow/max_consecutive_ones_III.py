# Problema  1004
from typing import List
def longestOnes(nums: List[int], k: int) -> int:
    izquierda = 0
    derecha = 0
    maximo = -1
    contador_ceros_en_ventana = 0
    for derecha in range(len(nums)):
        if nums[derecha] == 0:
            contador_ceros_en_ventana += 1

        while contador_ceros_en_ventana > k:
            if nums[izquierda] == 0:
                contador_ceros_en_ventana -= 1
            izquierda += 1

        maximo = max(maximo, derecha - izquierda + 1)
    return maximo


print(longestOnes(nums = [1,1,0,0,1], k = 2))
print(longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
print(longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))