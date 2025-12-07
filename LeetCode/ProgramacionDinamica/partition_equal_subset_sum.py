from typing import List
def canPartition(nums: List[int]) -> bool:
    suma_nums =  sum(nums)
    if suma_nums % 2  == 1:
        return False
    target = suma_nums  // 2
    dp = [False] * (target + 1)
    dp[0]= True
    for x in  range(len(dp)):
        for num in nums:
            if dp[x - num]:
                dp[x] = True
    return dp[target]
print(canPartition( nums = [1,5,11,5]))
print(canPartition(nums = [1,2,3,5]))