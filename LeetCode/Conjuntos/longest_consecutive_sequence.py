from typing import List
def longestConsecutive(nums: List[int]) -> int:
    resultado = 0
    conjunto = set(nums)
    for numero in conjunto:
        actual = 0
        if numero - 1 not in conjunto:
            while numero + actual in conjunto:
                actual += 1
            if actual > resultado:
                resultado = actual
    return resultado
print(longestConsecutive([2,20,4,10,3,4,5]))