"""
problema del mínimo número de plataformas

se tiene un conjunto de llegadas y salidas de trenes en una estación, donde cada tren requiere una plataforma desde su llegada hasta su salida.
si un tren llega mientras otro todavía está en la estación, se necesita una plataforma adicional.

el objetivo es determinar el número mínimo de plataformas necesarias para que ningún tren tenga que esperar debido a la falta de espacio.

entrada:
- `llegadas`: lista de tiempos de llegada de los trenes.
- `salidas`: lista de tiempos de salida de los trenes.

salida:
- el número mínimo de plataformas necesarias para manejar los trenes sin colisiones.

estrategia:
- ordenar los eventos (llegadas y salidas) en orden cronológico.
- recorrer los eventos y llevar un contador de plataformas en uso.
- actualizar el máximo número de plataformas utilizadas en cualquier momento.
"""

from queue import PriorityQueue
from typing import List

def numero_minimo_plataformas_tren(llegadas: list[int], salidas: list[int]) -> int:
    """
    calcula el número mínimo de plataformas necesarias para que ningún tren espere.

    :param llegadas: lista de tiempos de llegada de los trenes.
    :param salidas: lista de tiempos de salida de los trenes.
    :return: el número mínimo de plataformas requeridas.
    """
    pq = PriorityQueue()

    for i in range(len(llegadas)):
        pq.put((llegadas[i], "llega"))
        pq.put((salidas[i], "sale"))

    plataformas_actuales = 0
    plataformas_maximas = 0

    while not pq.empty():
        tiempo, tipo = pq.get()
        if tipo == "llega":
            plataformas_actuales += 1
            plataformas_maximas = max(plataformas_maximas, plataformas_actuales)
        else:
            plataformas_actuales -= 1

    return plataformas_maximas

llegadas = [900, 940, 950, 1100, 1500, 1800]
salidas = [910, 1200, 1120, 1130, 1900, 2000]

print(numero_minimo_plataformas_tren(llegadas, salidas))

