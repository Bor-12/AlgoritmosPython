#Problema 3
def longest_substring_without_repeating_characters(s: str) -> int:
    inicio = 0
    fin = 0
    maximo = 0
    caracteres_ocupados = set()
    while fin < len(s):
        while s[fin] in caracteres_ocupados:
            caracteres_ocupados.remove(s[inicio])
            inicio += 1
        caracteres_ocupados.add(s[fin])
        fin += 1
        maximo = max(maximo, fin - inicio)
    return maximo
longest_substring_without_repeating_characters("pwwkew")