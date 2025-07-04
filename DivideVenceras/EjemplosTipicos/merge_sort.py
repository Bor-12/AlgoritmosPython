def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        parte_izquierda_ordenada = merge_sort(lista[:mitad])
        parte_derecha_ordenada = merge_sort(lista[mitad:])
        i = j = k = 0

        while i < len(parte_izquierda_ordenada) and j < len(parte_derecha_ordenada):
            if parte_izquierda_ordenada[i] < parte_derecha_ordenada[j]:
                lista[k] = parte_izquierda_ordenada[i]
                i += 1
            else:
                lista[k] = parte_derecha_ordenada[j]
                j += 1
            k += 1
        while i < len(parte_izquierda_ordenada):
            lista[k] = parte_izquierda_ordenada[i]
            i += 1
            k += 1
        while j < len(parte_derecha_ordenada):
            lista[k] = parte_derecha_ordenada[j]
            j += 1
            k += 1
    return lista
lista = [5, 2, 2, 9, 1, 7, 6]
ordenada = merge_sort(lista)
print(ordenada)
#SE PUEDE DETECTAR CUANDO NO HACEN FALTA MEZCLAR
def merge_sort_optimizado(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        parte_izquierda_ordenada = merge_sort_optimizado(lista[:mitad])
        parte_derecha_ordenada = merge_sort_optimizado(lista[mitad:])
        i = j = k = 0
        # Verificamos si ya están ordenadas
        if parte_izquierda_ordenada[-1] <= parte_derecha_ordenada[0]:
            return parte_izquierda_ordenada + parte_derecha_ordenada
        while i < len(parte_izquierda_ordenada) and j < len(parte_derecha_ordenada):
            if parte_izquierda_ordenada[i] < parte_derecha_ordenada[j]:
                lista[k] = parte_izquierda_ordenada[i]
                i += 1
            else:
                lista[k] = parte_derecha_ordenada[j]
                j += 1
            k += 1
        while i < len(parte_izquierda_ordenada):
            lista[k] = parte_izquierda_ordenada[i]
            i += 1
            k += 1
        while j < len(parte_derecha_ordenada):
            lista[k] = parte_derecha_ordenada[j]
            j += 1
            k += 1
    return lista
lista = [5, 2, 2, 9, 1, 7, 6]
ordenada = merge_sort_optimizado(lista)
print(ordenada)

