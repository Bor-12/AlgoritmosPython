#Problema 1456
def maxVowels(s: str, k: int) -> int:
    inicio = 0
    fin = 0
    vocales = set("aeiou")
    contador_vocales = 0

    while fin < k:
        if s[fin] in vocales:
            contador_vocales += 1
        fin += 1
    maximo = contador_vocales
    while fin < len(s):
        if s[fin] in vocales:
            contador_vocales += 1
        if s[inicio] in vocales:
            contador_vocales -= 1
        maximo = max(maximo, contador_vocales)
        inicio += 1
        fin += 1
    return maximo
print(maxVowels("abciiidef", k = 3))
print(maxVowels("aeiou", k = 2))
print(maxVowels("leetcode", k = 3))
