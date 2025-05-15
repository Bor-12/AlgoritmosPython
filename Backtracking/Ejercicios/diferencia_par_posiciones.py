"""
Dado un conjunto de números enteros y un número entero `k`,
haz un programa que genere todos los subconjuntos de tamaño `k`
formados por elementos que aparecen en orden (como en la lista original),
y que cumplan la siguiente condición:

La diferencia entre cada par de elementos consecutivos del subconjunto debe ser un número par.

En otras palabras, si el subconjunto es de la forma [a₁, a₂, ..., aₖ],
entonces (a₂ - a₁), (a₃ - a₂), ..., (aₖ - aₖ₋₁) deben ser todos números pares.

El orden de los elementos debe respetar el orden original de la lista de entrada
(no se pueden reordenar), y no se pueden repetir elementos.

Ejemplo:

elementos = [1, 3, 5, 6, 8], k = 3

Subconjunto válido: [1, 3, 5]  → diferencias: 2, 2 → ambas pares
 Subconjunto inválido: [3, 5, 6] → diferencias: 2, 1 → 1 es impar
"""


def diferencia_par_posiciones(lista,  k):

    solucion = [None] * k

    diferencia_par_posiciones_recursivo(0, -1,solucion, lista, -1)
def diferencia_par_posiciones_recursivo(i, j,solucion_parcial, lista, ultimo_valor):
    if i == len(solucion_parcial):
        print(solucion_parcial)
    else:
        for k  in range(j + 1,len(lista)):
            """
                par -  par ->  par
                par  - impar  -> impar
                impar - par   - >  impar
                impar - impar ->  par
            """
            esPar = (lista[k] - ultimo_valor) % 2 == 0


            if i  == 0 or esPar:
                solucion_parcial[i] = lista[k]
                diferencia_par_posiciones_recursivo(i +1,k, solucion_parcial, lista, lista[k])
lista = [1, 3, 5, 6, 8]
k = 3
diferencia_par_posiciones(lista, k)