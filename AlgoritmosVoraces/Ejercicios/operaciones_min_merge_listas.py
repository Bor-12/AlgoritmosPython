"""Este problema est´a relacionado con la eficiencia de una generalizaci´on del algoritmo de ordenaci´on mergesort, en el que la lista original a ordenar
se descompone en varias sublistas de tama˜nos diferentes. El algoritmo emplea un
m´etodo para combinar las sublistas mezclando parejas de ´estas progresivamente
hasta ordenar la lista original.
Este ejercicio consiste implementar un m´etodo para hallar el numero mınimo
de operaciones que necesitar´ıa una estrategia (voraz) ´optima para ordenar la lista
original, cuando se desea mezclar n listas ordenadas, las cuales pueden tener tama˜nos
diferentes. Se supondr´a que se realiza una operaci´on por cada elemento a ordenar
de una pareja de sublistas."""

def indice_menor(len_listas, candidatos):
    """Devuelve el índice del candidato con la lista más pequeña"""
    indice_mejor = -1
    menor_valor = float('inf')
    for c in candidatos:
        if len_listas[c] < menor_valor:
            menor_valor = len_listas[c]
            indice_mejor = c
    return indice_mejor

def operaciones_minimas_merge(len_listas: list[int]) -> int:
    candidatos = set(range(len(len_listas)))
    numero_de_operaciones = 0
    while len(candidatos) > 1:
        # Seleccionamos los dos índices con las listas más pequeñas
        indice1 = indice_menor(len_listas, candidatos)
        candidatos.remove(indice1)
        indice2 = indice_menor(len_listas, candidatos)
        candidatos.remove(indice2)

        # Fusionamos ambas listas y sumamos el costo de la operación
        nuevo_tamano = len_listas[indice1] + len_listas[indice2]
        numero_de_operaciones += nuevo_tamano

        # Agregamos la nueva lista fusionada a la estructura
        len_listas.append(nuevo_tamano)
        candidatos.add(len(len_listas) - 1)  # Nuevo índice de la lista fusionada

    return numero_de_operaciones

# Prueba con un conjunto de listas
len_listas = [8, 5, 7, 4]
operaciones = operaciones_minimas_merge(len_listas)
print("Número mínimo de operaciones:", operaciones)

