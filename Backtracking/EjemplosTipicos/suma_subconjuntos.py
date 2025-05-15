def suma_subconjuntos(elementos, target):
    sol = [0] * len(elementos)
    suma_subconjuntos_recursivo(0, sol, 0,elementos,target)
def mostrar_conjunto(solucion, elementos):
    for i in range(len(elementos)):
        if solucion[i] == 1:
            print(elementos[i], end=" ")
    print()

def suma_subconjuntos_recursivo(i, sol, suma_actual,elementos,target):
    if suma_actual == target:
            mostrar_conjunto(sol, elementos)
    elif i < len(elementos):
        for k in range(2):
            if suma_actual + k*elementos[i] <= target:
                suma_actual += k*elementos[i]
                sol[i] = k
                suma_subconjuntos_recursivo(i + 1, sol, suma_actual, elementos, target)

elementos = [1,2,3, 5, 6, 7, 9]
target = 13
suma_subconjuntos(elementos, target)
print()

def suma_subconjuntos2(elementos, target):
    sol = [0] * len(elementos)
    suma_subconjuntos_recursivo2(0, sol, 0,elementos,target)
def mostrar_conjunto2(solucion, elementos):
    for i in range(len(elementos)):
        if solucion[i] == 1:
            print(elementos[i], end=" ")
    print()

def suma_subconjuntos_recursivo2(i, sol, suma_actual,elementos,target):
    if i == len(elementos):
        if suma_actual == target:
            mostrar_conjunto(sol, elementos)
    else:
        for k in range(2):
            if suma_actual + k*elementos[i] <= target:
                suma_actual += k*elementos[i]
                sol[i] = k
                suma_subconjuntos_recursivo2(i + 1, sol, suma_actual, elementos, target)
elementos = [1,2,3, 5, 6, 7, 9]
target = 13
suma_subconjuntos2(elementos, target)

#devuelve true si  hay alguna suma que de igual al target
def suma_subconjuntos_recursivo_booleano(elementos, target):
    return suma_subconjuntos_recursivo_booleano_recursivo(0, 0, elementos, target)

def suma_subconjuntos_recursivo_booleano_recursivo(i, suma_actual, elementos, target):
    if i == len(elementos):
        return suma_actual == target
    else:
        for k in range(2):
            nueva_suma = suma_actual + k * elementos[i]
            if nueva_suma <= target:
                if suma_subconjuntos_recursivo_booleano_recursivo(i + 1, nueva_suma, elementos, target):
                    return True
        return False

elementos = [1,2,3, 5, 6, 7, 9]
target = 13

print(suma_subconjuntos_recursivo_booleano(elementos, target))