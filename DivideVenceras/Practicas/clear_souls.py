"""
Clear Souls

El Caballero de Astora se enfrenta a oleadas de enemigos con distintos niveles.
Como solo quiere luchar contra enemigos con nivel igual o inferior al suyo,
tu misión es decir cuántos enemigos puede derrotar y qué puntuación total obtendría
(sumando los niveles de esos enemigos).

Entrada:
- Un número N: cantidad de enemigos.
- N números enteros: los niveles de los enemigos (ordenados y sin repetidos).
- Un número M: cantidad de casos de prueba.
- M líneas con un entero Q: nivel actual del Caballero de Astora en cada caso.

Salida:
- Por cada caso de prueba, imprime dos enteros:
  1. La cantidad de enemigos que puede derrotar (nivel ≤ Q)
  2. La suma total de sus niveles

Ejemplo de entrada:
7
1 2 3 4 5 6 7
3
3
10
2

Ejemplo de salida:
3 6
7 28
2 3

Límites:
• 7 ≤ N ≤ 100000
• 1 ≤ L ≤ N * 10
• 1 ≤ M ≤ 10000
• 1 ≤ Q ≤ N * 10
"""
def capturar_datos():
    numero_enemigos = int(input())
    string_nivel = input().split()
    lista_niveles = [0] * numero_enemigos
    for i in range(numero_enemigos):
        lista_niveles[i] = int(string_nivel[i])
    numero_casos_prueba = int(input())
    lista_casos_prueba = []
    for _ in range(numero_casos_prueba):
        lista_casos_prueba.append(int(input()))
    return numero_enemigos, lista_niveles, numero_casos_prueba, lista_casos_prueba


def buscar_ultimo_menor_igual(niveles, valor, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(niveles) - 1

    if izquierda > derecha:
        return derecha  # cuando se pasa, el último válido está en derecha

    medio = (izquierda + derecha) // 2

    if niveles[medio] <= valor:
        return buscar_ultimo_menor_igual(niveles, valor, medio + 1, derecha)
    else:
        return buscar_ultimo_menor_igual(niveles, valor, izquierda, medio - 1)


def clear_souls():
    _, lista_niveles, _ , lista_casos_prueba = capturar_datos()
    suma_acumulada = [0] * (len(lista_niveles) + 1)
    for i in range(len(lista_niveles)):
        suma_acumulada[i + 1] = suma_acumulada[i] + lista_niveles[i]

    for nivel in lista_casos_prueba:
        indice = buscar_ultimo_menor_igual(lista_niveles, nivel)
        cantidad = indice + 1
        puntos = suma_acumulada[cantidad]
        print(cantidad, puntos)


clear_souls()