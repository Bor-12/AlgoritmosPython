"""
Implementa una función que, dado un array de números enteros, devuelva una lista donde cada posición i 
indique cuántos elementos menores hay a la derecha del elemento en esa posición.

Es decir, para cada elemento del array, debes contar cuántos números más pequeños aparecen después de él.

La solución debe ser eficiente (tiempo O(n log n)), por lo que no se permite el uso de dos bucles anidados.

Ejemplo:
Entrada: [5, 2, 6, 1]
Salida:  [2, 1, 1, 0]

Explicación:
- El 5 tiene a su derecha a [2, 6, 1] → 2 menores (2 y 1)
- El 2 tiene a su derecha a [6, 1]    → 1 menor (1)
- El 6 tiene a su derecha a [1]      → 1 menor (1)
- El 1 no tiene ningún número a la derecha → 0
"""



def contar_menores_derecha(lista):
    """
    Para cada número en la lista, cuenta cuántos números menores hay a su derecha.
    Devuelve una lista con esos conteos.
    """

    lista_con_indices = list(enumerate(lista))
    conteo_menores = [0] * len(lista)

    def merge_sort(sublista):
        if len(sublista) <= 1:
            return sublista

        mitad = len(sublista) // 2
        mitad_izquierda = merge_sort(sublista[:mitad])
        mitad_derecha = merge_sort(sublista[mitad:])

        mezcla_ordenada = []
        puntero_izq = puntero_der = 0
        menores_a_la_derecha = 0

        while puntero_izq < len(mitad_izquierda) and puntero_der < len(mitad_derecha):
            indice_derecha, valor_derecha = mitad_derecha[puntero_der]
            indice_izquierda, valor_izquierda = mitad_izquierda[puntero_izq]

            if valor_izquierda > valor_derecha:
                # El de la derecha es menor y pasa delante del de la izquierda
                menores_a_la_derecha += 1
                mezcla_ordenada.append((indice_derecha, valor_derecha))
                puntero_der += 1
            else:
                # El de la izquierda ve pasar X menores a su derecha
                conteo_menores[indice_izquierda] += menores_a_la_derecha
                mezcla_ordenada.append((indice_izquierda, valor_izquierda))
                puntero_izq += 1

        # Lo que queda de la izquierda también ha visto pasar menores
        while puntero_izq < len(mitad_izquierda):
            indice_izquierda, valor_izquierda = mitad_izquierda[puntero_izq]
            conteo_menores[indice_izquierda] += menores_a_la_derecha
            mezcla_ordenada.append((indice_izquierda, valor_izquierda))
            puntero_izq += 1


        while puntero_der < len(mitad_derecha):
            mezcla_ordenada.append(mitad_derecha[puntero_der])
            puntero_der += 1

        return mezcla_ordenada

    lista_con_indices_ordenada = merge_sort(lista_con_indices)
    return conteo_menores, lista_con_indices_ordenada

entrada = [5, 2, 6, 1]
print(contar_menores_derecha(entrada))  # → [2, 1, 1, 0]
