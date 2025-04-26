# Ejercicio 3 - Examen mayo 2022-23
#
# Considérese una expresión matemática con n parejas de paréntesis – uno abierto '(' y otro cerrado ')'.
#
# Se pide implementar un algoritmo basado en la técnica de backtracking
# que imprima por pantalla todas las secuencias válidas que se puedan formar
# con n parejas de paréntesis.
#
# Además, la función deberá retornar el número total de estas secuencias válidas.
#
# Por ejemplo, para n = 3, hay 5 secuencias válidas:
#
# ((()))
# (()())
# (())()
# ()(())
# ()()()

#Hay que hacer una permutación 0 representa ( y 1 )
def secuencias_validas_parentesis(numero_parentesis):
    solucion = [None] * (numero_parentesis * 2)
    return secuencias_validas_parentesis_recursivo(0, solucion, 0, numero_parentesis)

def secuencias_validas_parentesis_recursivo(indice_actual, solucion_parcial, abiertos, n):
    if indice_actual == n * 2:
        imprimir_solucion(solucion_parcial)
        return 1
    contador_soluciones = 0
    for k in range(2):
        nuevo_abiertos = abiertos + (1 - k)
        cerrados = indice_actual + 1 - nuevo_abiertos
        if nuevo_abiertos >= cerrados and nuevo_abiertos <= n:
            solucion_parcial[indice_actual] = k
            contador_soluciones += secuencias_validas_parentesis_recursivo(indice_actual + 1, solucion_parcial, nuevo_abiertos, n)
    return contador_soluciones

def imprimir_solucion(solucion):
    resultado = ''
    for x in solucion:
        if x == 0:
            resultado += '('
        else:
            resultado += ')'
    print(resultado)

n = 3
print("Total de soluciones:", secuencias_validas_parentesis(n))
