#Ejercicio  55
#Priemro pense en hacerlo por recursividad ya que salia facil
from typing import List
def canJump1(nums: List[int]) -> bool:
    n = len(nums)

    def backtracking(posicion_actual):
        if posicion_actual >= n - 1:
            return True
        salto_maximo = posicion_actual + nums[posicion_actual]
        for salto in range(posicion_actual + 1, salto_maximo + 1):
            if backtracking(salto):
                return True

        return False

    return backtracking(0)
#Lo mejore con programcion dinamica haciendo memorizacion de soluciones pero no era suficiente
def canJump2(nums: List[int]) -> bool:
    n = len(nums)
    memo = {}  # posicion -> booleano, guardo los que  no llegan a nada que ya tengo calculados

    def backtracking(posicion_actual):
        if posicion_actual >= n - 1:
            return True
        if posicion_actual in memo:
            return memo[posicion_actual]
        salto_maximo = posicion_actual + nums[posicion_actual]
        for salto in range(posicion_actual + 1, salto_maximo + 1):
            if backtracking(salto):
                return True

        memo[posicion_actual] = False
        return False

    return backtracking(0)

#Como me daba time limit , llegue a la conclusion de que tenia mas complejidad mi solucion de la que deberia
#Por ultimo probe un  enfoque greedy y  aqui si salio
def canJump3(nums: List[int]) -> bool:
    maximo_salto = 0
    for i, salto in enumerate(nums):
        if i > maximo_salto:
            return False
        maximo_salto = max(maximo_salto, salto + i)
    return True

ejemplos = [
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4],
        [0],
        [1, 0, 2],
        [2, 0, 0],
        [1, 1, 0, 1]
    ]

for nums in ejemplos:
    print("\n==============================")
    print(f"Probando: {nums}")
    print("==============================")

    print("canJump1 (recursiva):", canJump1(nums))
    print("canJump2 (DP memo):  ", canJump2(nums))
    print("canJump3 (greedy):   ", canJump3(nums))