

def imprimir_subconjunto(sol, n_elementos, elementos):
    print('{', end='')
    for i in range(0, n_elementos - 1):
        print(elementos[sol[i]], ',', sep='', end='')
    if n_elementos > 0:
        print(elementos[sol[n_elementos - 1]], sep='', end='')
    print('}')

def generar_permutaciones(elementos):
    sol = [None] * len(elementos)
    generar_permutaciones_recursivo(0, sol, elementos)

def generar_permutaciones_recursivo(i, sol, elementos):

    if i == len(elementos):
        imprimir_subconjunto(sol, i, elementos)
    else:
        for k in range(len(elementos)):
            if k not in sol[:i]:
                sol[i] = k
                generar_permutaciones_recursivo(i + 1 , sol, elementos)
elementos = ["a", "b", "c"]
generar_permutaciones(elementos)
#Se puede mejorar la eficiencia del algoritmo utilizando un array para indicar si una posicion ha sido utilizada ya
def generar_permutaciones2(elementos):
    sol = [None] * len(elementos)
    libres = [True] * len(elementos)
    generar_permutaciones_recursivo2(0,libres, sol, elementos)
def generar_permutaciones_recursivo2(i, libres, sol, elementos):
    if i == len(elementos):
        imprimir_subconjunto(sol, i , elementos)
    else:
        for k in range(len(elementos)):
            if libres[k]: #O(1) para comprobar si ya se ha utilizado un elemento
                libres[k] = False
                generar_permutaciones_recursivo2(i +1 , libres, sol, elementos)
                libres[k] = True
print()
elementos = ["a", "b", "c"]
generar_permutaciones(elementos)
def generar_permutaciones_con_repeticion(elementos, repeticiones):
    total = sum(repeticiones)  # longitud real de la solución
    sol = [None] * total
    generar_permutaciones_con_repeticion_recursivo(0, sol, elementos, repeticiones)

def generar_permutaciones_con_repeticion_recursivo(i, sol, elementos, libres):
    if i == len(sol):
        imprimir_subconjunto(sol, i, elementos)
    else:
        for k in range(len(elementos)):
            if libres[k] > 0:
                sol[i] = k
                libres[k] -= 1
                generar_permutaciones_con_repeticion_recursivo(i + 1, sol, elementos, libres)
                libres[k] += 1

print("Con repeticion:")
elementos = ["a", "b", "c"]
repeticiones = [2, 1, 1]
generar_permutaciones_con_repeticion(elementos, repeticiones)
