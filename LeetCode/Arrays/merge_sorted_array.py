#Problema 88
"""
       Do not return anything, modify nums1 in-place instead.
"""
from typing  import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    copia_nums1 = nums1[:]
    i = j = k = 0
    while i < m and j < n:
        if copia_nums1[i] < nums2[j]:
            nums1[k] = copia_nums1[i]
            i += 1
        else:
            nums1[k] =  nums2[j]
            j += 1
        k += 1
    while i < m:
        nums1[k] = copia_nums1[i]
        i += 1
        k += 1
    while j < n:
        nums1[k] =  nums2[j]
        j += 1
        k += 1
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
merge(nums1, m, nums2, n)
print(nums1)
nums1 = [4,5,6,0,0,0]
nums2 = [1,2,3]
merge(nums1, m, nums2, n)
print(nums1)
#se puede mejorar
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    ultimo_indice = m + n - 1
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[ultimo_indice] = nums1[m - 1]
            m -= 1
        else:
            nums1[ultimo_indice] =  nums2[n -1]
            n -= 1
        ultimo_indice -= 1

    # Solo es necesario procesar los elementos restantes de nums2.
    # Si quedan elementos en nums1, ya están en su posición correcta, ya que esta ordenado.
    while n > 0:
        nums1[ultimo_indice] = nums2[n - 1]
        n -= 1
        ultimo_indice -= 1
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
merge(nums1, m, nums2, n)
print(nums1)
nums1 = [4,5,6,0,0,0]
nums2 = [1,2,3]
merge(nums1, m, nums2, n)
print(nums1)