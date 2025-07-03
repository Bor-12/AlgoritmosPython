def characterReplacement(s: str, k: int) -> int:
    contador_letras = {}

    longitud_maxima = 0
    izquierda = 0

    frecuencia_maxima = 0
    for derecha in range(len(s)):
        contador_letras[s[derecha]] = 1 + contador_letras.get(s[derecha], 0)
        frecuencia_maxima = max(frecuencia_maxima, contador_letras[s[derecha]])
        while derecha - izquierda + 1 - frecuencia_maxima > k:
            contador_letras[s[izquierda]] -= 1
            izquierda += 1
        longitud_maxima = max(longitud_maxima, derecha - izquierda + 1)
    return longitud_maxima
print(characterReplacement(s = "XYYX", k = 2))
print(characterReplacement(s = "AAABABB", k = 1))
print(characterReplacement(s="AAAA", k=2))