from typing import List
def maxSubArray(self, nums: List[int]) -> int:
    maxima_suma = nums[0]
    suma_actual = 0
    for numero  in nums:
        if  suma_actual < 0:
            suma_actual = 0
        suma_actual += numero
        maxima_suma  = max(maxima_suma, suma_actual)
    return maxima_suma