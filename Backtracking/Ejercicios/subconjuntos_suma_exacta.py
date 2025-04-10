"""
Se pide implementar un algoritmo basado en la técnica de backtracking para resolver
el siguiente problema.

Dada una lista L de números enteros no negativos (almacenada en un simple
array/lista), y otro número entero no negativo s, se desea hallar un conjunto de
números de L tal que su suma sea igual a s, y que además dicho conjunto sea el de
menor cardinalidad de entre todos los posibles que cumplan la restricción asociada
a la suma. El conjunto se especificará mediante un vector de booleanos de la misma
longitud que L.

En el siguiente ejemplo hay varios conjuntos de elementos de L tal que su suma
sea igual a 13 (s). El algoritmo devolvería el conjunto {6, 7} al ser el de menor
cardinalidad (es el que tiene el menor número de elementos):

    L = [1, 2, 3, 5, 6, 7, 9]
    s = 13

    Posibles combinaciones:
    - 13 = 6 + 7                ←  mínima cardinalidad (2 elementos)
    - 13 = 2 + 5 + 6
    - 13 = 1 + 5 + 7
    - 13 = 1 + 3 + 9
    - 13 = 1 + 2 + 3 + 7

    Entonces, una posible solución válida sería el subconjunto [6, 7].

    Esto se representaría con el siguiente vector booleano:
    → [False, False, False, False, True, True, False]

NOTA: la solución no tiene por qué ser única. Si hay varios subconjuntos que cumplan
que la suma de sus elementos es s, y además tienen la misma mínima cardinalidad,
basta con devolver cualquiera de esos conjuntos.
"""

#Se puede hacer mucho mas eficiente :/
def suma_subconjuntos_exacta(lista, target):
    soluciones = []

    def back_tracking(start, numeros_elegidos, suma_actual):
        if suma_actual == target:
            soluciones.append(numeros_elegidos[:])
            return
        if suma_actual > target:
            return
        for i in range(start, len(lista)):
            numeros_elegidos.append(lista[i])
            back_tracking(i + 1, numeros_elegidos, suma_actual + lista[i])
            numeros_elegidos.pop()

    back_tracking(0, [], 0)

    if not soluciones:
        return None


    mejor = min(soluciones, key=len)


    vector_bool = [False] * len(lista)

    for i, num in enumerate(lista):
        if num in mejor:
            vector_bool[i] = True
    return vector_bool

L = [1, 2, 3, 5, 6, 7, 9]
s = 13
print(suma_subconjuntos_exacta(L, s))