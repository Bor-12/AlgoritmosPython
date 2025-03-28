"""Implementa una función que encuentre un "pico" en un array de números enteros.

Un pico se define como un elemento que es mayor o igual que sus vecinos.

Para los extremos del array, solo se considera el vecino disponible.

Si hay múltiples picos, la función puede devolver cualquiera de ellos."""

def buscar_pico_array(numeros):
    if not numeros:
        return None

    mitad = len(numeros) // 2

    if (mitad == 0 or numeros[mitad] >= numeros[mitad - 1]) and \
            (mitad == len(numeros) - 1 or numeros[mitad] >= numeros[mitad + 1]):
        return numeros[mitad]  # Devuelve el valor del pico

    elif mitad > 0 and numeros[mitad - 1] > numeros[mitad]:
        return buscar_pico_array(numeros[:mitad])  # Izquierda

    else:
        return buscar_pico_array(numeros[mitad + 1:])  # Derecha



# Prueba
numeros = [1, 3, 20, 4, 1, 0]

print(buscar_pico_array(numeros))
numeros = []
print(buscar_pico_array(numeros))

numeros = [10, 2, 1, 0]
print(buscar_pico_array(numeros))

