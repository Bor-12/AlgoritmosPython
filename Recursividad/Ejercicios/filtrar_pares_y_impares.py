"""Implementa un algoritmo recursivo que reciba una lista de elementos (se pueden considerar
números reales) y genere dos listas. La primera contendrá los elementos que se encuentren
en índices pares, mientras que la segunda contendrá los elementos que se encuentran en
índices impares. Suponed que el primer índice de una lista es el 0. """
def filtrar_lista(lista):
    n = len(lista)

    if n == 0:
        return ([], [])
    elif n == 1:
        return (lista, [])
    else:
        lista_pares, lista_impares = filtrar_lista(lista[:n-1])
        if n % 2 == 0:
            return (lista_pares, lista_impares + [lista[n - 1]])
        else:
            return (lista_pares + [lista[n - 1]], lista_impares)

lista = [3, 6, 5, 7, 0, 9, 2]
print(filtrar_lista(lista))