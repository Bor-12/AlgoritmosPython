#Problema 76
def minimum_window_substring(s: str, t: str) -> str:
    if t == "": return ""

    letras_t, ventana = {}, {}

    for letra in t:
        if letra not in letras_t:
            letras_t[letra] = 0
        letras_t[letra] += 1
    tengo, necesito = 0, len(letras_t)
    resultado, longitud_resultado = [-1, -1], float('inf')
    izquierda = 0
    for derecha in range(len(s)):
        letra_s = s[derecha]
        if letra_s not in ventana:
            ventana[letra_s] = 0
        ventana[letra_s] += 1

        if letra_s in letras_t and ventana[letra_s] == letras_t[letra_s]:
            tengo += 1
        while tengo == necesito:
            if derecha - izquierda + 1 < longitud_resultado:
                resultado = [izquierda, derecha]
                longitud_resultado = derecha - izquierda + 1
            ventana[s[izquierda]] -= 1
            if s[izquierda] in letras_t and ventana[s[izquierda]] < letras_t[s[izquierda]]:
                tengo -= 1
            izquierda += 1
    izquierda, derecha = resultado[0], resultado[1]
    return s[izquierda:derecha +1] if longitud_resultado != float('inf') else ""


print(minimum_window_substring("ADOBECODEBANC","ABC"))