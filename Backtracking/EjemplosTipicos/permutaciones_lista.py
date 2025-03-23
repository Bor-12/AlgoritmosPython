def permutaciones_lista(lista):
    soluciones = []
    def backtrack(lista_actual):
        if len(lista_actual) == len(lista):
            return soluciones.append(lista_actual[:])

        for i in range(len(lista)):
            lista_actual.append(lista[i])
            backtrack(lista_actual)
            lista_actual.pop()
    backtrack([])
    return soluciones
def permutaciones_lista_sin_repeticion(lista):
    soluciones = []
    def backtrack(lista_actual):
        if (len(lista_actual) == len(lista)):
            return soluciones.append(lista_actual[:])
        for i in range(len(lista)):
            #quito las que empiezan por 3
            if len(lista_actual) == 0 and lista[i] == 3:
                continue
            lista_actual.append(lista[i])
            backtrack(lista_actual)
            lista_actual.pop()
    backtrack([])
    return soluciones
print(permutaciones_lista([1,4,3]))
print(permutaciones_lista_sin_repeticion([1,4,3]))