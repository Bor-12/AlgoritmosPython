#Problema 567
def checkInclusion(s1: str, s2: str) -> bool:
    frecuencias_letras = {}

    for letra in s1:
        frecuencias_letras[letra] = frecuencias_letras.get(letra, 0) + 1
    frecuencias_ventana = {}
    izquierda = 0
    for derecha in range(len(s2)):
        frecuencias_ventana[s2[derecha]] = frecuencias_ventana.get(s2[derecha], 0) + 1
        if derecha - izquierda + 1 > len(s1):
            frecuencias_ventana[s2[izquierda]] -= 1
            if frecuencias_ventana[s2[izquierda]] == 0:
                del frecuencias_ventana[s2[izquierda]]
            izquierda += 1
        if frecuencias_ventana == frecuencias_letras:
            return True
    return False

print(checkInclusion("ab", "eidbaooo"))  # True
print(checkInclusion("ab", "eidboaoo"))  # False




