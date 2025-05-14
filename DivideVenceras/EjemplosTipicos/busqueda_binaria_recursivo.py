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
    """Devuleve el indice donde se encuentra el numero buscado, si no lo encuentra devuelve -1 o la logitud de la lista  - 1"""
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
#se puede utilizar por ejemplo para saber donde insertar un valor en una lista ordenada, devolvermos la posicion donde se deveria de insertar
def busqueda_binaria_recursivo_insertar(numeros, valor, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(numeros) - 1

    if izquierda > derecha:
        return izquierda

    medio = (izquierda + derecha) // 2

    if numeros[medio] >= valor:
        return busqueda_binaria_recursivo_insertar(numeros, valor, izquierda, medio - 1)
    else:
        return busqueda_binaria_recursivo_insertar(numeros, valor, medio + 1, derecha)

def busqueda_binaria_recursivo_insertar(numeros, valor, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(numeros) - 1

    if izquierda > derecha:
        return izquierda

    medio = (izquierda + derecha) // 2

    if numeros[medio] >= valor:
        return busqueda_binaria_recursivo_insertar(numeros, valor, izquierda, medio - 1)
    else:
        return busqueda_binaria_recursivo_insertar(numeros, valor, medio + 1, derecha)


lista = [1, 3, 5, 6, 12, 15, 66]
test_values = [5, 1, 4, 6, 7, 15, 30, 70]

print("Insertar en lista:", lista)
for val in test_values:
    idx = busqueda_binaria_recursivo_insertar(lista, val)
    print(f"Insertar {val} en posición {idx}")
