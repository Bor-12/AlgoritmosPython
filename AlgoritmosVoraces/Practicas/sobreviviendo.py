"""
Sobreviviendo

En el nuevo programa de Teleseis, Sobreviviendo, los concursantes tienen que pasar
varios meses en una isla desierta y sobrevivir buscando sus propios alimentos, haciendo
fuego, etc. Cada concursante suele ser especialista en una tarea, pero todos los años suele
haber bastantes discusiones y terminan formándose grupos aislados de gente. Nuestro
objetivo como concursantes este año es evitar que el grupo se divida y, para ello,
queremos estrechar lazos entre todos los concursantes realizando el mínimo esfuerzo
posible.

Sabemos qué concursantes tienen relación entre ellos y lo que cuesta mantener esa
relación, y lo que queremos es construir una red de relaciones entre concursantes de
manera que el esfuerzo total necesario para mantenerla sea mínimo. Para ello,
necesitamos saber, de cada concursante, cuál será el esfuerzo total que debe hacer, que se
calcula como la suma de esfuerzos de las relaciones que formarán parte de la red.

Entrada
La primera línea contiene dos enteros N y M que indican el número de concursantes de
la edición y el número de relaciones que existen, respectivamente.
Las siguientes M líneas contienen 3 enteros C1, C2, E que indican que hay una relación
entre los concursantes C1 y C2 y que el esfuerzo de mantener esa relación será de E.

Salida
Las primeras N líneas contendrán, para cada concursante, la cadena “C{i} -> {Ei}”,
donde {i} será el identificador del concursante y {Ei} será el esfuerzo total de ese
concursante. Los concursantes se imprimirán en orden lexicográfico.
La última línea debe contener la cadena “Esfuerzo realizado -> {Et}”, donde
{Et} representa el esfuerzo total necesario para mantener la red de relaciones.

Límites
• 10 ≤ N ≤ 1000
• 11 ≤ M ≤ 200000
• 0 ≤ C < 2000000

Ejemplo de entrada
10 13
0 2 68
0 8 63
1 4 53
1 7 110
2 7 11
3 5 107
3 9 30
4 7 97
5 7 38
5 9 31
6 8 67
7 8 24
7 9 41

Ejemplo de salida
C0 -> 63
C1 -> 53
C2 -> 11
C3 -> 30
C4 -> 150
C5 -> 69
C6 -> 67
C7 -> 170
C8 -> 154
C9 -> 61
Esfuerzo realizado -> 414
"""

def capturar_datos():
    entrada = input().split()
    numero_de_concursantes = int(entrada[0])
    numero_de_conexiones_entre_concursantes = int(entrada[1])

    aristas = []

    for _ in range(numero_de_conexiones_entre_concursantes):
        entrada = input().split()
        origen = int(entrada[0])
        destino = int(entrada[1])
        relacion = int(entrada[2])
        aristas.append((relacion, origen, destino))  # (peso, nodo1, nodo2)

    return numero_de_concursantes, aristas


def find(vertice, conjunto_disjunto):
    indice = vertice
    while(conjunto_disjunto[indice] >= 0):
        indice = conjunto_disjunto[indice]
    return indice


def union(vertice1, vertice2, conjunto_disjunto):
    if conjunto_disjunto[vertice1] < conjunto_disjunto[vertice2]:
        # vertice1 tiene un conjunto más grande
        conjunto_disjunto[vertice2] = vertice1
    elif conjunto_disjunto[vertice2] < conjunto_disjunto[vertice1]:
        # vertice2 tiene un conjunto más grande
        conjunto_disjunto[vertice1] = vertice2
    else:
        # Ambos tienen el mismo tamaño, unimos y aumentamos tamaño
        conjunto_disjunto[vertice2] = vertice1
        conjunto_disjunto[vertice1] -= 1


def sobreviviendo():
    numero_de_concursantes, lista_aristas = capturar_datos()

    lista_aristas = sorted(lista_aristas, key=lambda x: x[0])


    conjunto_disjunto = [-1] * numero_de_concursantes
    solucion = []
    esfuerzo_por_concursante = [0] * numero_de_concursantes
    esfuerzo_total = 0
    aristas_usadas = 0
    seguir = True

    while lista_aristas and seguir:
        relacion, origen, destino = lista_aristas.pop(0)
        x = find(origen, conjunto_disjunto)
        y = find(destino, conjunto_disjunto)
        if x != y:
            union(x, y, conjunto_disjunto)
            esfuerzo_por_concursante[origen] += relacion
            esfuerzo_por_concursante[destino] += relacion
            esfuerzo_total += relacion
            aristas_usadas += 1
            if aristas_usadas == numero_de_concursantes - 1:
                seguir = False

    for i in range(numero_de_concursantes):
        print(f"C{i} -> {esfuerzo_por_concursante[i]}")
    print(f"Esfuerzo realizado -> {esfuerzo_total}")


sobreviviendo()

