from icecream import ic
#ic.disable() #desactiva los ic

def palindromo_mas_grande(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    max_len = 1
    start = 0

    # solo 1 letra
    for i in range(n):
        dp[i][i] = True
    ic("Después de palíndromos de 1 letra:")
    for fila in dp:
        ic(["T" if x else "." for x in fila])
    ic("---------------------------------")

    # solo 2 letras
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    ic("Después de palíndromos de 2 letras:")
    for fila in dp:
        ic(["T" if x else "." for x in fila])
    ic("---------------------------------")

    # palíndromos de 3 o más letras
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length
    ic("Después de palíndromos de 3 o más letras:")
    for fila in dp:
        ic(["T" if x else "." for x in fila])
    ic("---------------------------------")

    return s[start:start + max_len]

print(palindromo_mas_grande("forgeeksskeegfor"))
