#Problema 16
def threeSumClosest(nums, target):
    """
            :type nums: List[int]
            :type target: int
            :rtype: int
    """
    nums.sort()
    mas_cercano = float('inf')
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        izquierda = i + 1
        derecha = len(nums) - 1
        while izquierda < derecha:
            total = nums[i] + nums[izquierda] + nums[derecha]
            if abs(target - total) < abs(target - mas_cercano):
                mas_cercano = total
            elif total < target:
                izquierda += 1
            else:
                derecha -= 1
    return mas_cercano


nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))  # Output esperado: 2