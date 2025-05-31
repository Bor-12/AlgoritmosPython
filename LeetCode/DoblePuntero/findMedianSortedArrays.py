#Problema 4
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    total = m + n
    mitad = total // 2

    izquierda, derecha = 0, m
    while True:
        i = (izquierda + derecha) // 2
        j = mitad - i

        izquierda_lista1 = nums1[i - 1] if i > 0 else float('-inf')
        derecha_lista1 = nums1[i] if i < m else float('inf')
        izquierda_lista2 = nums2[j - 1] if j > 0 else float('-inf')
        derecha_lista2 = nums2[j] if j < n else float('inf')

        if izquierda_lista1 <= derecha_lista2 and izquierda_lista2 <= derecha_lista1:
            if total % 2 == 1:
                return min(derecha_lista1, derecha_lista2)
            return (max(izquierda_lista1, izquierda_lista2) + min(derecha_lista1, derecha_lista2)) / 2
        elif izquierda_lista1 > derecha_lista2:
            derecha = i - 1
        else:
            izquierda = i + 1


print(findMedianSortedArrays([1,3], [2]))  # Esperado: 2.0
