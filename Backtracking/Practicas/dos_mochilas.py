# Ejercicio - Dos mochilas de máximo peso (5 puntos)
#
# Implementar un algoritmo basado en la técnica de BACKTRACKING.
#
# Nos vamos de camping, y tenemos n productos que podemos llevar.
# Cada producto i tiene un peso pi (para i = 1, ..., n).
#
# Disponemos de dos mochilas:
# - Mochila 1 con capacidad máxima C1 kilos
# - Mochila 2 con capacidad máxima C2 kilos
#
# El objetivo es **maximizar el peso total** que podemos transportar entre las dos mochilas,
# respetando que:
# - El peso en la mochila 1 no puede superar C1
# - El peso en la mochila 2 no puede superar C2
# - Un mismo objeto no se puede meter en las dos mochilas a la vez
#
# Es decir, queremos maximizar:
#    suma(pesos de los objetos en mochila 1) + suma(pesos de los objetos en mochila 2)
#
# Entrada:
# - Primera línea: un entero n (el número de objetos)
# - Segunda línea: n números enteros separados por espacios, representando los pesos pi
# - Tercera línea: dos números enteros C1 y C2 separados por un espacio
#
# Salida:
# - Un único número entero: el peso máximo total que se puede transportar.
#
# Ejemplo de entrada:
# 5
# 2 7 8 9 5
# 9 11
#
# Ejemplo de salida:
# 19
#
def capturar_datos():
    n = int(input())
    lista_pesos = list(map(int, input().split()))
    capacidad_maxima1, capacidad_maxima2 = map(int, input().split())
    return n, lista_pesos, capacidad_maxima1, capacidad_maxima2


def dos_mochilas():
    n, lista_pesos, capacidad_maxima1, capacidad_maxima2 = capturar_datos()
    solucion_parcial = [0] * n
    solucion_optima = [0] * n
    mejor_peso = dos_mochilas_recursivo(0, 0, 0, 0, solucion_parcial, solucion_optima, -1, lista_pesos,
                                        capacidad_maxima1, capacidad_maxima2)
    print(mejor_peso)


def dos_mochilas_recursivo(i, peso1_actual, peso2_actual, peso_total_actual, solucion_parcial, solucion_optima,
                           mejor_peso, pesos, capacidad1, capacidad2):
    if i == len(pesos):
        if peso_total_actual > mejor_peso:
            mejor_peso = peso_total_actual
            for k in range(len(pesos)):
                solucion_optima[k] = solucion_parcial[k]
    else:
        # Intentar meter el objeto en mochila 1
        if peso1_actual + pesos[i] <= capacidad1:
            solucion_parcial[i] = 1
            mejor_peso = dos_mochilas_recursivo(
                i + 1,
                peso1_actual + pesos[i],
                peso2_actual,
                peso_total_actual + pesos[i],
                solucion_parcial,
                solucion_optima,
                mejor_peso,
                pesos,
                capacidad1,
                capacidad2
            )

        # Intentar meter el objeto en mochila 2
        if peso2_actual + pesos[i] <= capacidad2:
            solucion_parcial[i] = 2
            mejor_peso = dos_mochilas_recursivo(
                i + 1,
                peso1_actual,
                peso2_actual + pesos[i],
                peso_total_actual + pesos[i],
                solucion_parcial,
                solucion_optima,
                mejor_peso,
                pesos,
                capacidad1,
                capacidad2
            )

        # No meter el objeto
        solucion_parcial[i] = 0
        mejor_peso = dos_mochilas_recursivo(
            i + 1,
            peso1_actual,
            peso2_actual,
            peso_total_actual,
            solucion_parcial,
            solucion_optima,
            mejor_peso,
            pesos,
            capacidad1,
            capacidad2
        )

    return mejor_peso


dos_mochilas()
