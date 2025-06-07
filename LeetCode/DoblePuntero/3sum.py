#Problema 15
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    soluciones = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        izquierda = i + 1
        derecha = len(nums) - 1
        while izquierda < derecha:
            total = nums[i] + nums[izquierda] + nums[derecha]
            if total == 0:
                soluciones.append([nums[i], nums[izquierda], nums[derecha]])
                izquierda += 1
                derecha -= 1
                while izquierda < derecha and nums[izquierda] == nums[izquierda - 1]:
                    izquierda += 1
                while izquierda < derecha and nums[derecha] == nums[derecha + 1]:
                    derecha -= 1
            elif total < 0:
                izquierda += 1
            else:
                derecha -= 1
    return soluciones
nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
print(f"Output: {result}")