#Problema 26
from typing import List
def removeDuplicates(nums: List[int]) -> int:
    izquierda = 1
    for derecha in range(1, len(nums)):
        if nums[derecha] != nums[derecha - 1]:
            nums[izquierda] = nums[derecha]
            izquierda += 1
    return izquierda
print(removeDuplicates([1,1,2]))