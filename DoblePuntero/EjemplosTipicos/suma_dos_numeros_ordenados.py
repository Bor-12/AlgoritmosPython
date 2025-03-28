#Dado un array ordenado y un número target, encuentra si hay dos elementos cuya suma sea igual al target.

#Pasamos de una implementacion O(n^2) a O(n) (si esta ordenado el array)
def suma_dos_numero_ordenados(numeros, target):
    n = len(numeros)
    principio = 0
    final = n - 1
    while principio < final:
        suma_actual = 0
        suma_actual += numeros[principio] + numeros[final]
        if(suma_actual == target):
            return True
        if(suma_actual < target):
            principio += 1
        else:
            final -= 1
    return False

nums = [1, 2, 4, 7, 11, 18]
target = 15

print(suma_dos_numero_ordenados(nums, target))
nums = [8, 9, 11, 15]
target = 15
print(suma_dos_numero_ordenados(nums, target))