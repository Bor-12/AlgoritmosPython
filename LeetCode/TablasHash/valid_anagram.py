#Problema 242
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    numero_letras_s, numero_letras_t = {}, {}
    for i in range(len(s)):
        numero_letras_s[s[i]] = 1 + numero_letras_s.get(s[i], 0)
        numero_letras_t[t[i]] = 1 + numero_letras_t.get(t[i], 0)
    for letra in numero_letras_s:
        if numero_letras_s[letra] != numero_letras_t.get(letra, 0):
            return False
    return True