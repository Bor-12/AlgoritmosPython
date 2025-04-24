
# Dado un entero n y un entero k,
# genera todas las combinaciones posibles de tamaño k
# con números del 1 al n (ambos incluidos), sin repetir elementos y en orden creciente.
# Cada combinación debe tener exactamente k números distintos.
# El orden dentro de la lista no importa, pero debe estar en orden creciente
# para que no se repitan combinaciones como [2,1] si ya existe [1,2].


def conbinaciones_enteros(n, k):
    solucion = []
    def backtrack(combinacion_actual):
        if len(combinacion_actual) == k:
            solucion.append(combinacion_actual[:])
            return
        for i in range(1, n + 1):
            combinacion_actual.append(i)
            backtrack(combinacion_actual)
            combinacion_actual.pop()
    backtrack([])
    return solucion

print(conbinaciones_enteros(n=4, k=2))
def conbinaciones_enteros_con_restriccion(n, k):
    solucion = []
    def backtrack(combinacion_actual, inicio):
        if len(combinacion_actual) == k:
            solucion.append(combinacion_actual[:])
            return
        for i in range(inicio, n + 1):  # Empieza desde 'inicio' para mantener orden creciente
            combinacion_actual.append(i)
            backtrack(combinacion_actual, i + 1)  # El siguiente número debe ser mayor
            combinacion_actual.pop()

    backtrack([], 1)
    return solucion

print(conbinaciones_enteros_con_restriccion(n=4, k=2))