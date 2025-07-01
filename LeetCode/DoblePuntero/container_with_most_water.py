from typing import List
#por fuerza bruta
def maxArea(height: List[int]) -> int:
    area_maxima = 0
    for izquierda in range(len(height)):
        for derecha in range(izquierda + 1, len(height)):
            altura = min(height[izquierda], height[derecha])
            base = derecha - izquierda
            area = altura * base
            area_maxima = max(area_maxima, area)
    return area_maxima
print(maxArea([1,7,2,5,4,7,3,6]))
def maxArea2(height: List[int]) -> int:
    izquierda = 0
    derecha = len(height) - 1
    area_maxima = -1
    while izquierda < derecha:
        area_actual = (derecha - izquierda) * min(height[izquierda], height[derecha])
        area_maxima = max(area_maxima, area_actual)
        if height[izquierda] < height[derecha]:
            izquierda += 1
        else:
            derecha -= 1
    return area_maxima
print(maxArea2([1,7,2,5,4,7,3,6]))