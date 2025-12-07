from typing import List
"""
    Este problema NO se puede resolver con un algoritmo greedy (voraz),
    porque elegir siempre la moneda más grande que cabe NO garantiza una solución óptima.

    Ejemplo que rompe el método voraz:
        coins = [1, 3, 4], amount = 6
    Greedy escogería primero 4 y luego dos monedas de 1 → total 3 monedas.
    Pero la solución óptima es 3 + 3 → solo 2 monedas.

    La razón es que en un sistema arbitrario de monedas, una decisión localmente buena
    (usar la moneda más grande posible) puede impedir llegar a la solución mínima.

    Por eso se usa PROGRAMACIÓN DINÁMICA:
    ----------------------------------------------------------
    dp[x] = mínimo número de monedas para formar la cantidad x

    - dp[0] = 0    (0 monedas para hacer 0)
    - dp[x] se calcula probando todas las monedas:
          dp[x] = min(dp[x], dp[x - moneda] + 1)
      siempre que x - moneda >= 0

    Así se construyen todas las soluciones pequeñas y se usan para formar cantidades
    más grandes, garantizando el ÓPTIMO GLOBAL.
    ----------------------------------------------------------

"""

def coinChange(coins: List[int], amount: int) -> int:
    memo = {}
    resultado = dp(amount, coins,  amount, memo)
    return resultado if resultado != float("inf") else -1

def dp(restante,monedas, cantidad_objetivo, memo):
    if restante == 0:
        return 0
    if restante < 0:
        return float("inf")
    if restante in memo:
        return memo[restante]
    mejor = float("inf")
    for moneda in monedas:
        mejor = min(mejor, dp(restante - moneda, monedas, cantidad_objetivo, memo) + 1)
    memo[restante] = mejor
    return mejor
print(coinChange(coins = [1,2,5], amount = 11))
print(coinChange(coins = [1, 3, 4], amount = 6))
print(coinChange(coins = [2], amount = 3))
# Otro enfoque el el bottom up
def coinChange2(coins: List[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for x in range(1, amount + 1):
        for moneda in coins:
            if moneda <= x:
                dp[x] = min(dp[x], dp[x - moneda] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1
print(coinChange2(coins = [1,2,5], amount = 11))
print(coinChange2(coins = [1, 3, 4], amount = 6))

print(coinChange2(coins = [2], amount = 3))

