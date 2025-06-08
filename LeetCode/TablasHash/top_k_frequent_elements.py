#Problema 347
from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
    contador_numeros = {}
    frecuencias = [[] for i in range(len(nums) + 1)]
    for numero in nums:
        contador_numeros[numero] = 1 + contador_numeros.get(numero, 0)
    for numero, contador  in contador_numeros.items():
        frecuencias[contador].append(numero)
    resultado = []
    for i in range(len(frecuencias) - 1, 0, -1):
        for numero in frecuencias[i]:
            resultado.append(numero)
            if len(resultado) == k:
                return resultado



print(topKFrequent([1,2,2,1,1,3,3,3,2,34,4,5], 2))