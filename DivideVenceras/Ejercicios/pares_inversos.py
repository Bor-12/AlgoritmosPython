"""
EJERCICIO: Contar pares inversos en una lista (Divide y Vencerás - Merge Sort)

Dada una lista de números enteros, se pide contar cuántos pares inversos contiene.

Un **par inverso** es un par de índices (i, j) tal que:
    - i < j
    - lista[i] > lista[j]

Además de contar el número total de pares inversos, la función también debe devolver
la lista completa de dichos pares.

El algoritmo debe estar basado en la técnica de Merge Sort (divide y vencerás),
con una complejidad de O(n log n), y sin necesidad de comparar todos los pares uno a uno.

Salida esperada:
    - La lista ordenada
    - El número total de pares inversos
    - Una lista con todos los pares inversos encontrados
"""
def pares_inversos(lista):
    if len(lista) <= 1:
        return lista, 0, []

    mitad = len(lista) // 2
    parte_izquierda, inv_izq, lista_pares_izq = pares_inversos(lista[:mitad])
    parte_derecha, inv_der, lista_pares_der= pares_inversos(lista[mitad:])

    i = j = k = 0
    numero_pares_inversos = inv_izq + inv_der
    lista_ordenada = [0] * len(lista)
    lista_de_pares = lista_pares_izq + lista_pares_der
    while i < len(parte_izquierda) and j < len(parte_derecha):
        if parte_izquierda[i] <= parte_derecha[j]:
            lista_ordenada[k] = parte_izquierda[i]
            i += 1
        else:
            lista_ordenada[k] = parte_derecha[j]
            # Sumamos todos los elementos restantes en parte_izquierda (desde i hasta el final)
            # porque todos ellos son mayores que parte_derecha[j], y forman pares inversos.
            numero_pares_inversos += len(parte_izquierda) - i
            for x in parte_izquierda[i:]:
                lista_de_pares.append((x, parte_derecha[j]))

            j += 1
        k += 1

    while i < len(parte_izquierda):
        lista_ordenada[k] = parte_izquierda[i]
        i += 1
        k += 1

    while j < len(parte_derecha):
        lista_ordenada[k] = parte_derecha[j]
        j += 1
        k += 1

    return lista_ordenada, numero_pares_inversos, lista_de_pares



listas = [
    [1, 2, 3],
    [1, 2, 5, 6, 7, 9],
    [5, 4, 3, 2, 1],
    [2, 4, 1, 3, 5],
    [3, 1, 2],
    [5, 2, 9, 1, 7, 6]
]

for l in listas:
    _, inversos, lista_inversos = pares_inversos(l)
    print(f"Número de pares inversos de la lista {l}: {inversos}")
    print(f"Inversos: {lista_inversos}")
