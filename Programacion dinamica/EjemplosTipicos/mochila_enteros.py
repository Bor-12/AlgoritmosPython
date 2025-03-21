def es_factible(peso, peso_restante):
    return peso <= peso_restante
def mochila_memorizacion(valores: list[int], pesos: list[int], peso_maximo_mochila: int) -> list[float]:
    n = len(valores)
    memo = {}

    def dp(indice, peso_restante):
        if indice == n or peso_restante == 0:
            return 0, [0] * n
        if (indice, peso_restante) in memo:
            return memo[(indice, peso_restante)]
        if not es_factible(pesos[indice], peso_restante):
            return dp(indice + 1, peso_restante)
        valor1, sel1 = dp(indice + 1, peso_restante)
        valor2, sel2 = dp(indice + 1, peso_restante - pesos[indice])
        valor2 += valores[indice]
        max_valor = 0
        if valor1 > valor2:
            return valor1, sel1
        else:
            sel2 = sel2.copy()
            sel2[indice] = 1
            resultado = (valor2, sel2)
        memo[(indice, peso_restante)] = resultado
        return resultado

    return dp(0, peso_maximo_mochila)

print(mochila_memorizacion(valores = [20, 30, 66, 40, 60], pesos = [10, 20, 30, 40, 50], peso_maximo_mochila = 100))
def mochila_tabulacion(valores: list[int], pesos: list[int], peso_maximo_mochila: int) -> tuple[int, list[int]]:
    n = len(valores)


    dp = [[0] * (peso_maximo_mochila + 1) for _ in range(n + 1)]


    for i in range(1, n + 1):
        for w in range(1, peso_maximo_mochila + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],  # no coger
                    valores[i - 1] + dp[i - 1][w - pesos[i - 1]]  # coger
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Reconstruir la solución
    seleccion = [0] * n
    w = peso_maximo_mochila
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # significa que se cogió el objeto i-1
            seleccion[i - 1] = 1
            w -= pesos[i - 1]

    return dp[n][peso_maximo_mochila], seleccion

print(mochila_tabulacion(valores=[20, 30, 66, 40, 60], pesos=[10, 20, 30, 40, 50], peso_maximo_mochila=100))