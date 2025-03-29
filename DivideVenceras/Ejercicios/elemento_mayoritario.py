#Dado un array de tamaño n, encuentra si hay un elemento que aparece más de n/2 veces usando divide y vencerás.
def elemento_mayoritario(lista):
    def contar(lista, x):
        return sum(1 for i in lista if i == x)

    n = len(lista)
    if len(lista) == 1:
        return lista[0]

    mitad = n // 2
    candidato_1 = elemento_mayoritario(lista[:mitad])
    candidato_2 = elemento_mayoritario(lista[mitad:])

    if candidato_1 == candidato_2:
        return candidato_1

    # contar cuántas veces aparece cada candidato
    cuenta_1 = contar(lista, candidato_1) if candidato_1 is not None else 0
    cuenta_2 = contar(lista, candidato_2) if candidato_2 is not None else 0

    if cuenta_1 > n // 2:
        return candidato_1
    elif cuenta_2 > n // 2:
        return candidato_2
    else:
        return None

print(elemento_mayoritario(lista = [1,2,1,2,2,3,3,4,1,1,1,1,1,1]))
