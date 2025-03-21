
def fibonacci_con_memorizacion(n):
    memo = {0: 0, 1: 1}
    def f(x):
        if x in memo:
            return memo[x]
        memo[x] = f(x-1) + f(x-2)
        return memo[x]

    return f(n)

print(fibonacci_con_memorizacion(n = 10))
def fibonacci_con_tabulacion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    tb = [0] * (n+1)
    tb[1] = 1
    for i in range(2, n+1):
        tb[i] = tb[i-1] + tb[i-2]
    return tb[-1]
print(fibonacci_con_tabulacion(n = 10))
def fibonacci_con_tabulacion_mejora(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    anterior = 0
    actual = 1
    for i in range(2, n +1):
        anterior, actual = actual, anterior + actual
    return actual
print(fibonacci_con_tabulacion_mejora(n = 10))