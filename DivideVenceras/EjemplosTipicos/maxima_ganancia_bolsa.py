def maximo_subarray(array):
    def resolver(array, inicio, fin):
        if inicio == fin:
            return array[inicio]

        medio = (inicio + fin) // 2

        max_izquierda = resolver(array, inicio, medio)
        max_derecha = resolver(array, medio + 1, fin)
        max_centro = cruzando_centro(array, inicio, medio, fin)

        return max(max_izquierda, max_derecha, max_centro)

    def cruzando_centro(array, inicio, medio, fin):
        mejor_izquierda = float('-inf')
        suma = 0
        for i in range(medio, inicio - 1, -1):
            suma += array[i]
            mejor_izquierda = max(mejor_izquierda, suma)

        mejor_derecha = float('-inf')
        suma = 0
        for i in range(medio + 1, fin + 1):
            suma += array[i]
            mejor_derecha = max(mejor_derecha, suma)

        return mejor_izquierda + mejor_derecha

    return resolver(array, 0, len(array) - 1)

arr = [-3, 1, -8, 12, -2, 5, -6]
print("Máxima suma de lista:", maximo_subarray(arr))  # Debería imprimir 15
