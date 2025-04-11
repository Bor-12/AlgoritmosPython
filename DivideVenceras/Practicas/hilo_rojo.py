"""
Hilo Rojo

Existe una leyenda oriental que dice que las personas destinadas a compartir su vida están
unidas por un hilo rojo. Este hilo puede estirarse hasta el infinito, pero nunca
desaparecerá. Sin embargo, en la mayoría de las ocasiones no es fácil encontrar dónde se
encuentra el otro extremo del hilo.

Para facilitar la búsqueda, queremos implementar un algoritmo que, dados dos conjuntos
de personas, situados cada uno en una posición, sea capaz de decirnos en qué posición de
cada conjunto se encuentran los dos extremos del hilo rojo.

Entrada:
- Un número N: cantidad de personas del grupo 1.
- N números enteros: identificadores del grupo 1 (ordenados de forma ascendente).
- Un número M: cantidad de personas del grupo 2.
- M números enteros: identificadores del grupo 2 (ordenados de forma ascendente).
- Un número P: número de parejas conectadas.
- P líneas con dos enteros cada una: identificadores de dos personas unidas por el hilo rojo.

Salida:
- Por cada pareja, imprime dos enteros indicando la posición (índice) de cada persona en su grupo.
- Si alguno de los miembros de la pareja no se encuentra en su grupo, imprime "SIN DESTINO".

Ejemplo de entrada:
6
5 21 32 42 87 92
4
10 50 78 97
3
87 97
21 10
32 40

Ejemplo de salida:
4 3
1 0
SIN DESTINO

Límites:
• 1 ≤ N, M ≤ 1_000_000
• Los identificadores están ordenados y son únicos en cada grupo
"""



def capturar_datos():

    numero_personas_grupo1 = int(input())
    lista_identificadores_grupo1 = list(map(int, input().split()))


    numero_personas_grupo2 = int(input())
    lista_identificadores_grupo2 = list(map(int, input().split()))

    numero_parejas_conectadas = int(input())
    lista_parejas_conectadas = []
    for _ in range(numero_parejas_conectadas):
        a, b = map(int, input().split())
        lista_parejas_conectadas.append((a, b))

    return (numero_personas_grupo1, lista_identificadores_grupo1, numero_personas_grupo2, lista_identificadores_grupo2,
            numero_parejas_conectadas, lista_parejas_conectadas)

def busqueda_binaria(lista,  valor_buscado, izquierda = 0, derecha = None):

    if derecha == None:
        derecha = len(lista) - 1

    if izquierda > derecha:
        return -1

    medio = (izquierda + derecha) // 2
    if lista[medio] == valor_buscado:
        return medio

    if lista[medio] < valor_buscado:
        return busqueda_binaria(lista, valor_buscado,medio + 1, derecha)
    else:
        return busqueda_binaria(lista, valor_buscado,izquierda,medio - 1)

def hilo_rojo():

    (numero_personas_grupo1, lista_identificadores_grupo1, numero_personas_grupo2, lista_identificadores_grupo2,
    numero_parejas_conectadas, lista_parejas_conectadas) = capturar_datos()

    for i in range(numero_parejas_conectadas):

        valor_buscado1, valor_buscado2 = lista_parejas_conectadas[i]
        indice1 = busqueda_binaria(lista_identificadores_grupo1, valor_buscado1)
        if indice1 == -1:
            print("SIN DESTINO")
            continue
        else:
            indice2 = busqueda_binaria(lista_identificadores_grupo2, valor_buscado2)
        if indice2 == -1:
            print("SIN DESTINO")
        else:
            print(indice1, indice2)

hilo_rojo()