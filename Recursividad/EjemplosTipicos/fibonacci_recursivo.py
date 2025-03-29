def fibonacci_recursivo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n -2)
print(fibonacci_recursivo(4))