#genera todos los numeros binarios de 2 ^n
def generar_binarios(n):
    resultados = []
    def backtrack(cadena_actual):
        if len(cadena_actual) == n:
            resultados.append(cadena_actual)
            return
        backtrack(cadena_actual + '0')
        backtrack(cadena_actual + '1')

    backtrack('')
    return resultados

print(generar_binarios(n = 4))
#restriccion , no se puede mas de 2 unos seguidos
def generar_binarios_sin11(n):
    resultados = []
    def backtrack(cadena_actual):
        if len(cadena_actual) == n:
            resultados.append(cadena_actual)
            return
        backtrack(cadena_actual + '0')
        if len(cadena_actual) == 0 or cadena_actual[-1] != '1':
            backtrack(cadena_actual + '1')
    backtrack('')
    return resultados
print(generar_binarios_sin11(n = 4))