"""
Operación Fracaso

Llegados a estas alturas del concurso, en Operación Fracaso califican con una nota a cada
concursante, evaluando su paso por el programa. Esta nota repercutirá en la cantidad de
fans que tiene cada concursante, ya que los espectadores confían en el criterio del jurado.

Sabiendo que la nota va de 1 a 10, debemos calcular la cantidad de fans del concursante
en cuestión. Si la puntuación que recibe es de 1, el concursante será su propio fan.
Por otro lado, si la puntuación recibida es de 2, le admirarán todas sus personas cercanas
(familiares y amigos). Si el jurado le evaluase con un 3, sus familiares y amigos hablarían
con sus contactos y estos se convertirían también en fans. Hay que tener en cuenta que el
concursante es siempre el identificado como 0 en la entrada.

Entrada
- La primera línea contiene un número entero N que representa el número de concursantes
  que van a ser evaluados.
- Por cada concursante, hay una línea con tres enteros M, K y C que representan:
    - M: la nota obtenida por el concursante
    - K: el número de potenciales fans
    - C: el número de relaciones entre ellos
- A continuación, hay C líneas, cada una con dos enteros A y B que indican una relación
  entre dos personas del grupo de fans.

Salida
- Por cada concursante, se debe imprimir en una línea el número de personas que le admiran.

Ejemplo de entrada:
1
2 8 7
0 1
0 2
1 3
1 4
1 5
2 6
6 7

Ejemplo de salida:
3

Límites:
- 0 ≤ N ≤ 60
- 1 ≤ M ≤ 10
- 30 ≤ K ≤ 200
- 50 < C < 1500
"""

def capturar_datos():
    numero_concursantes = int(input())
    info_concursantes = []

    for _ in range(numero_concursantes):
        linea = input().split()
        nota = int(linea[0])
        potenciales_fans = int(linea[1])
        numero_de_relaciones_entre_fans = int(linea[2])
        relaciones_entre_fans = []

        for _ in range(numero_de_relaciones_entre_fans):
            linea = input().split()
            origen = int(linea[0])
            destino = int(linea[1])
            relaciones_entre_fans.append((origen, destino))

        info_concursantes.append((nota, potenciales_fans, relaciones_entre_fans))

    return numero_concursantes, info_concursantes


def numero_admiradores(nota, num_fans, lista_relacines_entre_fans):
    grafo = {i: [] for i in range(num_fans)}

    for a, b in lista_relacines_entre_fans:
        grafo[a].append(b)
        grafo[b].append(a)

    if nota == 1:
        return 1

    visitados = [False] * num_fans
    cola = [(0, 0)]  # (nodo, nivel)
    visitados[0] = True
    contador = 1

    while cola:
        actual, nivel = cola.pop(0)

        if nivel >= nota - 1:
            continue

        for vecino in grafo[actual]:
            if not visitados[vecino]:
                visitados[vecino] = True
                contador += 1
                cola.append((vecino, nivel + 1))

    return contador


def operacion_fracaso():
    numero_concursantes, info_concursantes = capturar_datos()

    for nota, fans, relaciones in info_concursantes:
        print(numero_admiradores(nota, fans, relaciones))


operacion_fracaso()
