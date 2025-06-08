#Problema 217
from typing import List
def hasDuplicate(nums: List[int]) -> bool:
    numeros = set()
    for numero in nums:
        if numero in numeros:
            return True
        numeros.add(numero)
    return False


