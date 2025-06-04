#Problema 7
import math
def reverse(x: int) -> int:
    MIN = -2 ** 31
    MAX  = 2 ** 31 -1
    resultado = 0
    while x != 0:
        digito = int(math.fmod(x, 10)) #-1 % 10 = 9
        x  = int(x / 10)               # -1 // 10 = -1
        if resultado > MAX // 10 or resultado == MAX // 10 and digito >= MAX % 10 or resultado < MIN // 10 or resultado == MIN // 10 and digito <= MIN % 10:
            return 0
        resultado = resultado * 10 + digito

    return resultado
def reverse2(x: int) -> int:
    MIN = -2 ** 31
    MAX  = 2 ** 31 -1
    resultado = 0
    negativo = False
    if x < 0:
        negativo = True
    x = abs(x)
    while x != 0:
        digito = x % 10
        x  = int(x / 10)
        if resultado > MAX // 10 or resultado == MAX // 10 and digito >= MAX % 10 or resultado < MIN // 10 or resultado == MIN // 10 and digito <= MIN % 10:
            return 0
        resultado = resultado * 10 + digito
    if negativo:
        resultado = -1 * resultado
    return resultado
print(reverse(123456))
print(reverse(-123456))
print(reverse2(123456))
print(reverse2(-123456))