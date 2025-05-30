#Problema 1
from typing import List
def two_sum(nums: List[int], target: int )-> List[int]:
    """
    Encuentra dos índices de números en `nums` que suman `target`.

    Args:
        nums (List[int]): Lista de enteros.
        target (int): Objetivo de la suma.

    Returns:
        List[int]: Índices de los dos números que suman el objetivo.

    Raises:
        ValueError: Si no se encuentra una solución válida.
    """
    numeros_vistos = {}
    for indice,  numero in enumerate(nums):
        complemento = target - numero
        if complemento in numeros_vistos:
            return indice, numeros_vistos[complemento]
        numeros_vistos[numero] = indice
    raise ValueError("No se encontró una combinación valida")

numeros = [2,7,11,15]
objetivo = 9
print(two_sum(numeros, objetivo))
numeros = [1, 2, 5, 9]
objetivo = 20
print(two_sum(numeros, objetivo))

