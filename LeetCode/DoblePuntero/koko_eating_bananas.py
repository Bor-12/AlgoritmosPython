from typing import List
import math
def minEatingSpeed(piles: List[int], h: int) -> int:
    izquierda = 1
    derecha  = max(piles)
    resultado  = derecha
    while izquierda <= derecha:
        k =  (izquierda + derecha) // 2
        horas = 0
        for platano in piles:
            horas += math.ceil(platano / k) #redondea hacia arriba
        if horas <= h:
            resultado = min(resultado, k)
            derecha = k - 1
        else:
            izquierda  = k +  1
    return resultado

piles = [1,4,3,2]
h = 9
print(minEatingSpeed(piles,  h))
piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles,h))


