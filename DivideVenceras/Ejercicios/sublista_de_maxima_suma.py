"""Se pide implementar un algoritmo basado en la estrategia de divide y vencerás para resolver
el problema de la sublista de máxima suma. Dada una lista de números el objetivo es hallar
una sublista de elementos contiguos cuya suma sea máxima. Por ejemplo, dada la lista
[−1, −4, 5, 2, −3, 4, 2, −5], la lista óptima es [5, 2, −3, 4, 2], cuyos elementos suman 10. Se
asumirá que la lista inicial no es vacía, y está compuesta de números enteros.
"""
def sublista_de_maxima_suma(lista):
    n = len(lista)
    if n == 1:
        return lista[0] #asumimos que no es vacia

    mitad = n // 2
    maxima_suma_izquierda = sublista_de_maxima_suma(lista[:mitad])
    maxima_suma_derecha = sublista_de_maxima_suma(lista[mitad:])
    # suma máxima de las listas de la mitad izquierda
    # que contienen el índice (mitad-1)

    max_izq = -float('inf')
    aux_suma = 0
    for i in range(mitad - 1, -1, -1):
        aux_suma = aux_suma + lista[i]
        max_izq = max(max_izq, aux_suma)
    aux_suma = 0
    max_der = -float('inf')
    for i in range(mitad, n):
        aux_suma = aux_suma + lista[i]
        max_der = max(max_der, aux_suma)
    return max(maxima_suma_izquierda, maxima_suma_derecha, max_izq+max_der)


lista = [-1, -4, 5, 2, -3, 4, 2, -5]
print(sublista_de_maxima_suma(lista))