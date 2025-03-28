#Dado un número entero base a y un exponente no negativo n, calcula el valor de a^n (es decir, "a elevado a la n") de forma eficiente.

def exponenciacion_rapida(base, exponente):
    """
    Estrategia:
    - Si el exponente es par:
        a^n = (a^(n/2))^2
    - Si el exponente es impar:
        a^n = a * (a^((n-1)/2))^2
    Esto reduce el problema a exponentes más pequeños, dividiendo entre 2 cada vez.
    """


    if exponente == 0:
        return 1


    if exponente == 1:
        return base

    # Dividimos el problema a la mitad:
    # Calculamos a^(n//2) recursivamente
    mitad = exponenciacion_rapida(base, exponente // 2)

    if exponente % 2 == 0:
        # Si el exponente es par, simplemente devolvemos mitad * mitad
        return mitad * mitad
    else:
        # Si el exponente es impar, hay que multiplicar una vez más por 'base'
        # porque exponente = 2k + 1 → a^n = base * (a^k)^2
        return base * mitad * mitad


# Ejemplo de uso
base = 5
exponente = 10
print(exponenciacion_rapida(base, exponente))  # Resultado: 9765625