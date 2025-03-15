"""
Road to La Velada del Año IV

Los participantes de la Velada del Año IV ya han sido anunciados. Ahora que es oficial,
nos han pedido que les ayudemos con la organización de su nueva rutina, ya que necesitan
cambiar muchos de sus hábitos.

Los streamers nos han facilitado una lista con todas las actividades que quieren hacer y
el momento del día en el que pueden hacerlo. Debido a que, de momento, los humanos
no son capaces de hacer dos cosas correctamente y a la vez, las actividades no pueden
solaparse en el horario que establezcamos. Sabiendo todo esto, tenemos que hacer un
programa capaz de organizar el horario del boxeador y calcular cuál es la mayor cantidad
de actividades que puede realizar en un día (en la mayoría de las ocasiones no podrán
hacer todo lo que quieren).

Entrada:
La primera línea contendrá un número 𝑁 que representa el número de actividades que
quieren realizar. Las siguientes 𝑁 líneas contendrán: el nombre de la actividad, el instante
de tiempo de inicio 𝐼 y el instante de finalización 𝐹.

Salida:
La salida será el máximo número de actividades que el streamer puede realizar ese día.

Ejemplo de entrada:
5
Vacunarse 20 30
BaniarAlPez 35 40
Entrenar 31 60
PonerTweets 10 15
LlamadaConIbai 80 100

Ejemplo de salida:
4

Límites:
• 5 ≤ 𝑁 ≤ 10
• 0 ≤ 𝐼 ≤ 𝐹 ≤ 10000
"""

def capturar_datos():
    n = int(input())
    lista_tareas = []
    lista_inicio = []
    lista_fin = []
    candidatos = set()
    for i in range(n):
        string = input().split()
        tarea = string[0]
        inicio = int(string[1])
        fin = int(string[2])
        lista_tareas.append(tarea)
        lista_inicio.append(inicio)
        lista_fin.append(fin)
        candidatos.add(i)
    return n, lista_tareas, lista_inicio, lista_fin, candidatos
def mejor_candidato(candidatos,lista_fin):
    min = float('inf')
    indice_minimo = -1
    for i in candidatos:
        if min > lista_fin[i]:
            min = lista_fin[i]
            indice_minimo = i
    return indice_minimo
def es_factible(indice, lista_inicio, fin_ultima_actividad):
    return lista_inicio[indice] >= fin_ultima_actividad
def velada():
    n, lista_tareas, lista_inicio, lista_fin, candidatos = capturar_datos()
    solucion = 0
    fin_ultima_actividad = -1
    while candidatos:
        indice_mejor_candidato = mejor_candidato(candidatos, lista_fin)
        if es_factible(indice_mejor_candidato, lista_inicio,fin_ultima_actividad):
            fin_ultima_actividad = lista_fin[indice_mejor_candidato]
            solucion += 1
        candidatos.remove(indice_mejor_candidato)
    print(solucion)
velada()