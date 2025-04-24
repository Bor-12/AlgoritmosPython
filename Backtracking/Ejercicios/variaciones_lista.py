def variaciones_con_repeticion(lista):
    soluciones = []
    def backtrack(lista_actual):
        if len(lista_actual) == len(lista):
            soluciones.append(lista_actual[:])
            return
        for i in range(len(lista)):
            lista_actual.append(lista[i])
            backtrack(lista_actual)
            lista_actual.pop()
    backtrack([])
    return soluciones

def variaciones_filtradas_por_primero(lista):
    soluciones = []
    def backtrack(lista_actual):
        if len(lista_actual) == len(lista):
            soluciones.append(lista_actual[:])
            return
        for i in range(len(lista)):
            if len(lista_actual) == 0 and lista[i] == 3:
                continue
            lista_actual.append(lista[i])
            backtrack(lista_actual)
            lista_actual.pop()
    backtrack([])
    return soluciones

print("Variaciones con repetición:")
print(variaciones_con_repeticion([1, 4, 3]))

print("Variaciones sin que empiecen por 3:")
print(variaciones_filtradas_por_primero([1, 4, 3]))
