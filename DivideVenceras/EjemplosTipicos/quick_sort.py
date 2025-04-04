def particion(lista, izquierda, derecha):
    pivote = lista[izquierda]
    i = izquierda + 1
    j = derecha
    while i <= j:
        if lista[i] <= pivote:
            i += 1
        elif lista[j] > pivote:
            j -= 1
        else:
            lista[i], lista[j] = lista[j] , lista[i]
            i += 1
            j -= 1
    lista[izquierda] , lista[j] = lista[j], lista[izquierda]
    return j
def quicksort(lista):
    quicksort_recursivo(lista, 0, len(lista) - 1)
def quicksort_recursivo(lista, izquierda, derecha):
    if izquierda >= derecha:
        return
    if izquierda < derecha:
        mitad = particion(lista, izquierda, derecha)
        quicksort_recursivo(lista, izquierda, mitad -1)
        quicksort_recursivo(lista, mitad + 1, derecha)
lista = [5, 2, 9, 1, 7, 6]
quicksort(lista)
print(lista)