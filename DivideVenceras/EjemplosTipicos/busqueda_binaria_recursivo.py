def busqueda_binaria_recursivo(numeros, valor_buscado):
    mitad = len(numeros) // 2
    if numeros[mitad] == valor_buscado:
        return True
    if len(numeros) == 1:
        return False
    if numeros[mitad] > valor_buscado:
        return busqueda_binaria_recursivo(numeros[:mitad], valor_buscado)
    else:
        return busqueda_binaria_recursivo(numeros[mitad:], valor_buscado)
lista = [1,3,5,6,12,15,66]
target = 15
print(busqueda_binaria_recursivo(lista, target))
target = 30
print(busqueda_binaria_recursivo(lista, target))