"""
Problema: Second Dates

Descripción:
Se va a estrenar el programa "Second Dates", donde los participantes de "First Dates"
que no tuvieron éxito quieren volver a intentarlo. Para esta segunda oportunidad,
los organizadores han decidido cambiar la mecánica y en lugar de formar parejas directamente,
dividen a los participantes en dos grupos en dos salas distintas.

El programa nos indicará cuántos participantes tendrá uno de los grupos, mientras que
el otro grupo tendrá el resto de los participantes.

El objetivo es que un grupo sea de los "jóvenes" y el otro de los "no-tan-jóvenes",
maximizando la diferencia entre la suma de edades de ambos grupos.

----------------------------------------------------------------------------------------

Entrada:
- La primera línea contiene dos enteros N y K:
  * N (5 ≤ N ≤ 50): Número total de participantes.
  * K (2 ≤ K ≤ N - 2): Tamaño de uno de los grupos.

- Las siguientes N líneas contienen:
  * Un string C (nombre del participante, sin espacios).
  * Un entero A (18 ≤ A ≤ 100): Edad del participante.

----------------------------------------------------------------------------------------

Salida:
- La primera línea debe contener los nombres de los participantes que irán al grupo de los jóvenes.
- La segunda línea debe contener los nombres de los participantes que irán al grupo de los no-tan-jóvenes.
- En ambos casos, los participantes deben estar ordenados por edad de manera ascendente.

----------------------------------------------------------------------------------------

Ejemplo de Entrada:
5 2
JamesLineberger 55
JeanetteMaurey 73
ChristieDangelo 29
HeatherTrew 78
LeolaSwift 30

Ejemplo de Salida:
ChristieDangelo LeolaSwift
JamesLineberger JeanetteMaurey HeatherTrew

----------------------------------------------------------------------------------------

Restricciones:
- 5 ≤ N ≤ 50
- 2 ≤ K ≤ N - 2
- 18 ≤ A ≤ 100
"""

def capturar_datos():
    string = input().split()
    numero_participantes = int(string[0])
    tamano_grupo = int(string[1])

    lista_participantes = []

    for i in range(numero_participantes):
        datos = input().split()
        nombre = datos[0]
        edad = int(datos[1])
        lista_participantes.append((nombre, edad))

    return numero_participantes, tamano_grupo, lista_participantes

def ordenar_por_edad(participante):
    return participante[1]


def second_dates():
    _, tamano_grupo, lista_participantes = capturar_datos()

    lista_participantes_ordenada = sorted(lista_participantes, key=ordenar_por_edad)

    grupo_jovenes = lista_participantes_ordenada[:tamano_grupo] #va desde el inicio hasta tam_grupo
    grupo_mas_mayores = lista_participantes_ordenada[tamano_grupo:] #va desde el tam_grupo hasta el final

    print(" ".join(nombre for nombre, _ in grupo_jovenes))
    print(" ".join(nombre for nombre, _ in grupo_mas_mayores))

second_dates()


