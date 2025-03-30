"""
Mirror on the walls

El espejo encantado puede invertir cualquier palabra, ¡pero sólo funciona
mediante recursividad! Tu tarea consiste en escribir una función recursiva
que tome una cadena como entrada y devuelva su inversa, sin utilizar
ningún bucle.

Recuerda que no se deben utilizar bucles iterativos, sino únicamente
funciones recursivas.

Entrada:
Una palabra S (string).

Salida:
La palabra invertida.

Ejemplo de entrada:
dog

Ejemplo de salida:
god

Límites:
• 1 ≤ |S| ≤ 100
"""
def espejo():
    string = input()

    def recursividad(cadena):
        if len(cadena) <= 1:
            return cadena
        # Recursión: tomamos el último carácter y lo agregamos a la inversión del resto
        return cadena[-1] + recursividad(cadena[:-1])

    nueva_cadena = recursividad(string)

    return nueva_cadena

print(espejo())

