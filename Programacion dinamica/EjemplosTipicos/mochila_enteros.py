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
        if valor1 > valor2:
            resultado = (valor1, sel1)
        else:
            sel2 = sel2.copy()
            sel2[indice] = 1
            resultado = (valor2, sel2)
        memo[(indice, peso_restante)] = resultado
        return resultado

    return dp(0, peso_maximo_mochila)

def mochila_tabulacion(valores: list[int], pesos: list[int], peso_maximo_mochila: int) -> tuple[int, list[int]]:
    n = len(valores)
    dp = [[0] * (peso_maximo_mochila + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, peso_maximo_mochila + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    valores[i - 1] + dp[i - 1][w - pesos[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    seleccion = [0] * n
    w = peso_maximo_mochila
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            seleccion[i - 1] = 1
            w -= pesos[i - 1]

    return dp[n][peso_maximo_mochila], seleccion

peso = [3, 6, 9, 5]
valor = [7, 2, 10, 4]
capacidad = 15

print("Memorización:")
print(mochila_memorizacion(valores=valor, pesos=peso, peso_maximo_mochila=capacidad))

print("\nTabulación:")
print(mochila_tabulacion(valores=valor, pesos=peso, peso_maximo_mochila=capacidad))
