# Ejercicio 3 [5 puntos] [Duración: 50 minutos]
#
# Implementa un algoritmo basado en la técnica de BACKTRACKING para generar
# combinaciones con repetición de n elementos tomados de m en m.
#
# Los datos de entrada son:
# - una lista a = [a0, a1, ..., an-1] de n elementos distintos
# - un entero m (1 <= m <= n)
#
# Las combinaciones con repetición son secuencias de m elementos de a,
# en las que se pueden repetir los elementos,
# y el orden en que aparecen los elementos NO importa.
#
# Por ejemplo, para a = ['a', 'b', 'c', 'd'] y m = 3, las combinaciones son:
#
# a a a     a a b     a a c     a a d
# a b b     a b c     a b d     a c c
# a c d     a d d     b b b     b b c
# b b d     b c c     b c d     b d d
# c c c     c c d     c d d     d d d
#
# Observad que la combinación (a b) es la misma que (b a).
# Es decir: no importa el orden interno,
# por eso NO se deben generar secuencias como (b a) o (c a) si ya has generado (a b).
#
# El método a desarrollar debe:
# - Imprimir todas las combinaciones con repetición.
# - Calcular el número C de combinaciones generadas,
#   y mostrarlo al final.
#
# La fórmula para comprobar que C es correcto es:
#
#            (n + m - 1)!
#   C = -------------------
#        (m!) * (n - 1)!
#
# En el ejemplo, C = 6! / (3! * 3!) = 20 combinaciones.
#
# Se valorará el uso de estructuras de datos eficientes
# para acelerar la comprobación de validez de las soluciones parciales.

def combinaciones_suma_enteros(elementos, m):
    solucion = [None] * m
    numero_soluciones = combinaciones_suma_enteros_recursivo(0, 0,solucion, elementos)
    return numero_soluciones
def combinaciones_suma_enteros_recursivo(indice_actual, indice_ultimo_anadido,solucion_parcial, elementos):
    n = len(elementos)
    m = len(solucion_parcial)
    if indice_actual == m:
        for i in range(0, m):
            print(solucion_parcial[i], ' ', end='')
        print()
        return 1
    else:
        contador = 0
        for k in range(indice_ultimo_anadido, n):
            solucion_parcial[indice_actual] = elementos[k]
            contador = contador + combinaciones_suma_enteros_recursivo(indice_actual + 1, k, solucion_parcial, elementos)
        return contador
elementos = ['a', 'b', 'c', 'd']
print(combinaciones_suma_enteros(elementos, 3))