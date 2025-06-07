#Problema 167
def twoSum(numbers, target):
    for izquierda in range(len(numbers) - 1):
        derecha = len(numbers) - 1
        while izquierda < derecha:
            total = numbers[izquierda] + numbers[derecha]
            if total == target:
                return [izquierda + 1, derecha + 1]
            elif total < target:
                izquierda += 1
            else:
                derecha -= 1
    return []
#Merjor enfoque
def twoSum2(numbers, target):
    izquierda = 0
    derecha = len(numbers) - 1
    while izquierda < derecha:
        total = numbers[izquierda] + numbers[derecha]
        if total == target:
            return [izquierda + 1, derecha + 1]
        elif total < target:
            izquierda += 1
        else:
            derecha -= 1
    return []
numbers = [2, 7, 11, 15]
target = 9
result = twoSum(numbers, target)
print(f"Output: {result}")
result = twoSum2(numbers, target)
print(f"Output: {result}")