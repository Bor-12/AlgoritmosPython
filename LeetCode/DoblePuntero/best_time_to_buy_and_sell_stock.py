from typing import List

def maxProfit(prices: List[int]) -> int:
    beneficio_maximo = 0
    izquierda = 0
    derecha = 1

    while derecha < len(prices):
        # si podemos sacar beneficio vendiendo en 'derecha' tras comprar en 'izquierda'
        if prices[derecha] - prices[izquierda] > 0:
            beneficio_maximo = max(beneficio_maximo,
                                   prices[derecha] - prices[izquierda])
        else:
            izquierda = derecha

        derecha += 1

    return beneficio_maximo

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
