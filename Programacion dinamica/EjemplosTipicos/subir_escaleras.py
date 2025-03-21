# Problema:
# Estás al pie de una escalera con 'n' escalones.
# En cada paso, puedes subir 1 o 2 escalones.
# La pregunta es: ¿de cuántas maneras distintas puedes llegar al escalón número 'n'?
# Ejemplo 1:
# n = 1
# Solo hay una forma: subir 1 escalón → [1]
# Resultado esperado: 1

# Ejemplo 2:
# n = 2
# Dos formas posibles: [1, 1] y [2]
# Resultado esperado: 2

# Ejemplo 3:
# n = 3
# Tres formas:
# - [1, 1, 1]
# - [1, 2]
# - [2, 1]
# Resultado esperado: 3
def subir_escaleras_memorizacion(n):
    memo = {0: 1, 1: 1}
    def dp(n):
        if n in memo:
            return memo[n]
        memo[n] = dp(n -1) + dp(n - 2)
        return memo[n]
    return dp(n)
print(subir_escaleras_memorizacion(8))
def subir_escaleras_tabulacion(n):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n +1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]
print(subir_escaleras_tabulacion(8))