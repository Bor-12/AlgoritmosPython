from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    izquierda = 0
    suma_ventana = 0
    longitud_minima = float("inf")
    for derecha in range(len(nums)):
        suma_ventana += nums[derecha]
        while suma_ventana >= target:
            longitud_minima = min(longitud_minima, derecha - izquierda + 1)
            suma_ventana -= nums[izquierda]
            izquierda += 1
    return 0 if longitud_minima == float("inf") else longitud_minima
print(minSubArrayLen( target = 7, nums = [2,3,1,2,4,3]))
print(minSubArrayLen(target = 4, nums = [1,4,4]))
print(minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))