# Ejercicio 8.1 - Selección de actividades con máxima compatibilidad

# Tenemos un conjunto de n actividades {a0, a1, ..., an-1}
# Cada actividad usa un recurso común (ejemplo: una sala de reuniones).
# El recurso solo puede ser usado por una actividad a la vez.

# Cada actividad tiene:
# - Un instante de comienzo ci
# - Un instante de finalización fi
# - Se cumple que 0 ≤ ci < fi < ∞

# Una actividad ai se desarrolla en el intervalo [ci, fi).
# Dos actividades ai y aj son compatibles si NO se solapan:
# Esto ocurre si ci >= fj o cj >= fi.

# Objetivo:
# Encontrar el subconjunto de actividades compatibles que maximice la cantidad seleccionada.
def mejor_candidato(final_actividades, candidatos):
    minimo = max(final_actividades) + 1
    indice = -1
    for i in candidatos:
        if final_actividades[i] < minimo:
            minimo = final_actividades[i]
            indice = i
    return indice
def es_factible(indice_mejor_candidato, inicio_actividades, final_actividades, solucion):
    for i in solucion:
        if not (inicio_actividades[indice_mejor_candidato] >= final_actividades[i] or inicio_actividades[i] >= final_actividades[indice_mejor_candidato]):
            return False
    return True
def ej_8_1(inicio_actividades, final_actividades):
    n = len(inicio_actividades)
    candidatos = set(range(n))

    solucion = []
    while candidatos:
        indice_mejor_candidato = mejor_candidato(final_actividades, candidatos)
        if es_factible(indice_mejor_candidato, inicio_actividades, final_actividades, solucion):
            solucion.append(indice_mejor_candidato)
        candidatos.remove(indice_mejor_candidato)
    return solucion
inicio_actividades = [1, 2, 0, 5, 8, 5, 6, 8, 3, 3, 12]
final_actividades = [4, 13, 6, 7, 12, 9, 10, 11, 8, 5, 14]
#el que menos dura de tiempo

print(ej_8_1(inicio_actividades, final_actividades))
# Ejemplo de subconjuntos óptimos:
# - {a0, a3, a7, a10}
# - {a9, a3, a4, a10}

