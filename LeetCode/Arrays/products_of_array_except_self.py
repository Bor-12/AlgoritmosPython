#Problema 238
from typing import List
def productExceptSelf(nums: List[int]) -> List[int]:
    resultado = [1] * len(nums)
    prefix = []
    producto = 1
    for num in nums:
        producto *= num
        prefix.append(producto)

    postfix = [1] * len(nums)
    producto = 1
    for i in range(len(nums) - 1, -1, -1):
        producto *= nums[i]
        postfix[i] = producto

    for i in range(len(nums)):
        izquierda = prefix[i - 1] if i -1 >= 0 else 1
        derecha = postfix[i + 1] if i + 1 < len(nums) else 1
        resultado[i] = izquierda * derecha
    return resultado
print(productExceptSelf([1,2,4,6]))
print(productExceptSelf([-1,1,0,-3,3]))
#Se puede hacer mucho mejor
def productExceptSelf2(nums: List[int]) -> List[int]:
    resultado = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        resultado[i] *= prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        resultado[i] *= postfix
        postfix *= nums[i]
    return resultado
print(productExceptSelf2([1,2,4,6]))
print(productExceptSelf2([-1,1,0,-3,3]))