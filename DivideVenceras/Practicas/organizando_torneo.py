"""
Organizador de torneos

Eres el encargado de organizar un torneo de ajedrez entre tus amigos. El torneo tiene un
formato de liga, en el que todos juegan contra todos. Después de cada partida se asignan
puntuaciones a los jugadores, y tu tarea es determinar cuán "desorganizada" está la
clasificación final.

La clasificación se representa con una lista de puntuaciones. Un jugador está descolocado
si hay otro jugador con mayor puntuación **después de él** en la lista. Es decir, queremos
contar cuántas veces un valor más alto aparece **antes** que un valor más bajo: esto se
traduce en contar los **intercambios necesarios** para ordenar la lista de mayor a menor.

Entrada:
- Un número N: cantidad total de puntuaciones.
- N números enteros: las puntuaciones finales de los jugadores.

Salida:
- Un único número: el total de intercambios necesarios para ordenar la clasificación de forma descendente.

Ejemplo de entrada:
4
4 3 2 1

Ejemplo de salida:
6

Explicación:
- En este ejemplo, la lista está completamente invertida respecto al orden correcto (de mayor a menor),
  por lo que se requieren 6 intercambios (inversiones) para dejarla ordenada.

Límites:
• 1 ≤ N ≤ 200_000
• 1 ≤ Puntuación ≤ 200_000
"""

def capturar_datos():

    n = int(input())
    string = input().split()
    lista = []
    for i in range(n):
        lista.append(int(string[i]))

    return n, lista

def pares_inversos(lista):

    if len(lista) > 1:

        mitad = len(lista) // 2
        parte_izquierda_ordenada, contador_izquierda = pares_inversos(lista[:mitad])
        parte_derecha_ordenada, contador_derecha = pares_inversos(lista[mitad:])

        i = j = k = 0
        contador = contador_izquierda + contador_derecha

        while i < len(parte_izquierda_ordenada) and j < len(parte_derecha_ordenada):
            if parte_izquierda_ordenada[i] <= parte_derecha_ordenada[j]:
                lista[k] = parte_izquierda_ordenada[i]
                i += 1
            else:
                lista[k] = parte_derecha_ordenada[j]
                j += 1
                # Sumamos todos los elementos restantes en parte_izquierda (desde i hasta el final)
                # porque todos ellos son mayores que parte_derecha[j], y forman pares inversos.
                contador += len(parte_izquierda_ordenada) - i

            k += 1

        while i < len(parte_izquierda_ordenada):
            lista[k] = parte_izquierda_ordenada[i]
            i += 1
            k += 1

        while j < len(parte_derecha_ordenada):
            lista[k] = parte_derecha_ordenada[j]
            j += 1
            k += 1

        return lista, contador

    else:

        return lista, 0


def organizando_torneo():
    n, lista = capturar_datos()
    lista_ordenada, contador = pares_inversos(lista)
    print(contador)

organizando_torneo()

