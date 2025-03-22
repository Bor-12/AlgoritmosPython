"""
Cada vez es más difícil copiar

Los profesores están cada vez más entrenados para evitar que los estudiantes copien, así
que estos tienen que mejorar sus habilidades si quieren conseguir copiar en un examen.
En cada clase están distribuidos los profesores para poder vigilar todo el examen, así que
los estudiantes quieren encontrar cuántos de ellos tienen que estudiar para poder superar
entre todos el examen.

Los estudiantes saben que, si hay un profesor entre ellos no pueden comunicarse, así que
quieren saber cuántos grupos de estudiantes pueden comunicarse entre ellos sin que les
vea ningún profesor. La información que transmite un estudiante llega a cualquiera de su
grupo, así que buscamos encontrar el mínimo número de grupos donde circulará la
información.

Entrada
La primera línea contiene dos números enteros N y M que representan el número de
estudiantes de la clase y el número de pares de estudiantes que pueden transmitir
información entre ellos.
Las siguientes M líneas contienen dos enteros A y B que indican que los estudiantes
número A y B no tienen a un profesor en medio.

Salida
Se deberá imprimir un entero indicando el número de grupos mínimo que necesitamos
para transmitir toda la información.

Ejemplo de entrada
10 5
0 1
1 5
2 4
3 9
4 9

Ejemplo de salida
5

Límites
• 10 ≤ N ≤ 10 000
• 3 ≤ M ≤ 15 000
• 0 ≤ a, b < N
"""

def capturar_datos():
    entrada = input().split()
    numero_estudiantes = int(entrada[0])
    numero_conexiones = int(entrada[1])

    grafo_comunicacion = {i: [] for i in range(numero_estudiantes)}

    for _ in range(numero_conexiones):
        estudiante_a, estudiante_b = map(int, input().split())
        grafo_comunicacion[estudiante_a].append(estudiante_b)
        grafo_comunicacion[estudiante_b].append(estudiante_a)

    return numero_estudiantes, grafo_comunicacion


def bfs(inicio, grafo, visitados):
    cola = [inicio]
    visitados[inicio] = True
    while cola:
        actual = cola.pop(0)
        for vecino in grafo[actual]:
            if not visitados[vecino]:
                visitados[vecino] = True
                cola.append(vecino)


def es_dificil_copiar():
    numero_estudiantes, grafo = capturar_datos()
    visitados = [False] * numero_estudiantes
    grupos = 0
    for estudiante in range(numero_estudiantes):
        if not visitados[estudiante]:
            bfs(estudiante, grafo, visitados)
            grupos += 1
    print(grupos)


es_dificil_copiar()