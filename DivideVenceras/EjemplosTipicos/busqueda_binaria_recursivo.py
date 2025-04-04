from networkx.algorithms.isomorphism.matchhelpers import numerical_edge_match


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

def busqueda_binaria_recursivo_indice(numeros, valor_buscado, izquierda = 0, derecha = None):
    """Devuleve el indice donde se encuentra el numero buscado, si no lo encuentra devuelve -1 o la logitud de la lista dada"""
    if derecha == None:
        derecha = len(numeros) - 1
    if izquierda > derecha:
        return derecha # cuando se pasa, el último válido está en derecha
    medio = (izquierda + derecha) // 2

    if numeros[medio] <= valor_buscado:
        return busqueda_binaria_recursivo_indice(numeros, valor_buscado, medio + 1, derecha)
    else:
        return busqueda_binaria_recursivo_indice(numeros, valor_buscado, izquierda, medio - 1)



lista = [1,3,5,6,12,15,66]
target = 15
print(busqueda_binaria_recursivo_indice(lista, target))
target = -3
print(busqueda_binaria_recursivo_indice(lista, target))
target = 17
print(busqueda_binaria_recursivo_indice(lista, target))
target = 88
print(busqueda_binaria_recursivo_indice(lista, target))