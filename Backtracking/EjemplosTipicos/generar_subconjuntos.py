


def subconjuntos(elementos):
    solucion = [None] * len(elementos)
    subconjuntos_recursivo(0, solucion, elementos)

def mostrar_subconjunto(sol, elementos):
    ha_imprimido_alguno = False
    print('{', end='')
    for i in range(len(sol)):
        if sol[i] == 1:
            if ha_imprimido_alguno:
                print(',', elementos[i], sep='', end='')
            else:
                print(elementos[i], sep='', end='')
                ha_imprimido_alguno = True
    print('}')


def subconjuntos_recursivo(i, actual, elementos):
    if i == len(elementos):
        mostrar_subconjunto(actual, elementos)
    else:
        for k in range(2):
            actual[i] = k
            subconjuntos_recursivo(i + 1, actual, elementos)


lista = ["a", "b", "c"]
subconjuntos(lista)

#ahora utilizando los indices en vez de una lista con 0 y con 1 para representar la solucion
def subconjuntos2(elementos):
    soluciones = [None] * len(elementos)
    subconjuntos_recursivo2(0,-1, soluciones, elementos)

def mostrar_subconjunto2(sol, n_elementos, elementos):
    print('{', end='')
    for i in range(n_elementos - 1):
        print(elementos[sol[i]], ',', sep='', end='')
    if n_elementos > 0:
        print(elementos[sol[n_elementos - 1]], end='')
    print('}')

def subconjuntos_recursivo2(i, j,actual, elementos):
    mostrar_subconjunto2(actual, i, elementos)
    for k in range(j+1, len(elementos)):
        actual[i] = k
        subconjuntos_recursivo2(i + 1, k, actual, elementos)
print()
subconjuntos2(lista)
#otra forma de hacerlo seria:
def subconjunto3(elementos):
    solucion = [None] * len(elementos)
    subconjuntos_recursivo3(0, solucion, elementos)

def subconjuntos_recursivo3(i, solucion, elementos):
    mostrar_subconjunto2(solucion, i , elementos)
    if i == 0:
        inicio = 0
    else:
        inicio = solucion[i - 1]  + 1 #hay que empezar por el ultimo añadido + 1
    for k in range(inicio, len(elementos)):
        solucion[i] = k
        subconjuntos_recursivo3(i + 1, solucion, elementos)
print()
subconjunto3(lista)

