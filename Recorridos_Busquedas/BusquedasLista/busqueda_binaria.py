def busqueda_ordenada(lista_ordenada, entero_buscado):
    inicio =  0
    fin = len(lista_ordenada) - 1
    while inicio <= fin:
        mitad = (inicio + fin) // 2
        if lista_ordenada[mitad] == entero_buscado:
            return mitad
        elif lista_ordenada[mitad] < entero_buscado:
            inicio = mitad +1
        else:
            fin = mitad -1
    return -1
print(busqueda_ordenada([1,2,3,5,6,9,100], 9))
print(busqueda_ordenada([1,2,3,5,6,9,100], 88))