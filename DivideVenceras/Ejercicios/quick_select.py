"""
    EJERCICIO: Algoritmo QuickSelect (Selección rápida)

    Dado un arreglo desordenado de números enteros y un número k (1 ≤ k ≤ longitud del arreglo),
    utiliza un algoritmo basado en la técnica "divide y vencerás", similar al algoritmo QuickSort,
    para encontrar el k-ésimo elemento más pequeño del arreglo SIN ORDENARLO COMPLETAMENTE.

    El algoritmo debe ser eficiente, con una complejidad promedio esperada mejor que O(n log n).

    Parámetros de entrada:
        arr -> Lista de números enteros.
        k   -> Número entero que representa la posición del elemento buscado (1-based index).

    Salida esperada:
        El k-ésimo elemento más pequeño del arreglo.

    Ejemplo:
        Entrada: arr = [7, 10, 4, 3, 20, 15], k = 3
        Salida: 7

    Nota: el arreglo original no tiene que quedar ordenado tras la ejecución.
    """
def particion(lista, izquierda, derecha):
    pivote = lista[izquierda]
    i = izquierda + 1
    j = derecha
    while i <= j:
        if pivote >= lista[i]:
            i += 1
        elif pivote < lista[j]:
            j -= 1
        else:
            lista[i], lista[j] = lista[j] , lista[i]
            i += 1
            j -= 1

    lista[izquierda], lista[j] = lista[j] ,  lista[izquierda]

    return j

def quick_select(lista, k):

    return quick_select_recursivo(lista, k - 1, 0, len(lista) - 1)
def quick_select_recursivo(lista, k  , izquierda, derecha):
    if izquierda == derecha:
        return lista[izquierda]
    pivote_indice = particion(lista, izquierda, derecha)
    if pivote_indice == k:
        return lista[pivote_indice]
    # Si el pivote está a la derecha de la posición que buscamos, buscamos en la izquierda
    elif pivote_indice > k:
        return quick_select_recursivo(lista, k,izquierda, pivote_indice - 1)

    # Si está a la izquierda, buscamos en la derecha
    else:
        return quick_select_recursivo(lista, k,pivote_indice + 1, derecha)

arr = [7, 10, 4, 3, 20, 15]
k = 3
resultado = quick_select(arr, k)
print(f"El {k}-ésimo elemento más pequeño es: {resultado}")

arr = [22, 5, 16, 8, 12, 99, 1, 3, 44, 17]
k = 5

resultado = quick_select(arr, k)
print(f"El {k}-ésimo elemento más pequeño es: {resultado}")
#para conseguir el k esimo elemento mas grande
def quick_select_grande(lista, k):
    return quick_select_recursivo(lista, len(lista) - k, 0, len(lista) - 1)
arr = [22, 5, 16, 8, 12, 99, 1, 3, 44, 17]
k = 5

resultado = quick_select_grande(arr, k)
print(f"El {k}-ésimo elemento más grande es: {resultado}")
