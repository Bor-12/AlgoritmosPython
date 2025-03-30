"""
Euclides

Se requiere implementar una función recursiva que, dados dos números
enteros positivos a y b, determine su Máximo Común Divisor (MCD)
utilizando el algoritmo de Euclides. La función debe realizar el cálculo de
manera estrictamente recursiva, sin el uso de estructuras iterativas (como
bucles for o while).

Recuerda que no se deben utilizar bucles iterativos, sino únicamente
funciones recursivas.

Entrada:
Dos enteros positivos a y b separados por un espacio.

Salida:
Un entero que represente el Máximo Común Divisor de a y b.

Ejemplo de entrada:
48 18

Ejemplo de salida:
6

Límites:
• 1 ≤ a
• 1 ≤ b
"""
def euclides():

    string = input().split()
    entero_a = int(string[0])
    entero_b = int(string[1])

    def recursividad(a, b):
        if (b == 0):
            return a
        return recursividad(b, a % b)

    return recursividad(entero_a, entero_b)

print(euclides())