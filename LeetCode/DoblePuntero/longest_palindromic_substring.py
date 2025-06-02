#Problema 5
def expandir_desde_centro(s: str, izquierda: int, derecha: int, resultado: str, longitud_resultado: int) -> tuple[str, int]:
    while izquierda >= 0 and derecha < len(s) and s[izquierda] == s[derecha]:
        if (derecha - izquierda + 1) > longitud_resultado:
            resultado = s[izquierda: derecha + 1]
            longitud_resultado = derecha - izquierda + 1
        izquierda -= 1
        derecha += 1
    return resultado, longitud_resultado

def longestPalindrome(s: str) -> str:
    resultado = ""
    longitud_resultado = 0

    for i in range(len(s)):
        # Longitud impar
        resultado, longitud_resultado = expandir_desde_centro(s, i, i, resultado, longitud_resultado)

        # Longitud par
        resultado, longitud_resultado = expandir_desde_centro(s, i, i + 1, resultado, longitud_resultado)

    return resultado
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))

