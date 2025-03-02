from typing import Tuple


def indice_mejor_candidato(tareas: list[int], candidatos: set[int]) -> int:
    indice_mejor_candidato = -1
    menor_valor = float('inf')

    for i in candidatos:
        if tareas[i] < mejor_candidato:
            mejor_candidato = tareas[i]
            indice_mejor_candidato = i

    return indice_mejor_candidato

def tiempo_espera_voraz(tareas: list[int], numero_de_candidatos: int) -> Tuple[list[int], int, float]:
    """Calcula el orden óptimo de ejecución para minimizar el tiempo de espera promedio.

        Args:
            tareas (List[int]): Lista con los tiempos de ejecución de cada tarea.
            numero_de_candidatos (int): Número total de tareas a ejecutar.

        Returns:
            Tuple[List[int], int, float]:
                - Orden de ejecución óptimo de las tareas.
                - Tiempo total de espera.
                - Tiempo medio de espera.
        """
    candidatos = set(range(numero_de_candidatos))
    orden_ejecucion = []

    while candidatos:
        indice = indice_mejor_candidato(tareas, candidatos)
        orden_ejecucion.append(indice)
        candidatos.remove(indice)

    tiempo_total_espera = 0
    tiempo_acumulado = 0

    for tarea in orden_ejecucion:
        tiempo_acumulado += tareas[tarea]
        tiempo_total_espera += tiempo_acumulado

    tiempo_medio_espera = tiempo_total_espera / numero_de_candidatos

    return orden_ejecucion, tiempo_total_espera, tiempo_medio_espera


tareas = [3, 10, 5]
solucion, tiempo_total, tiempo_medio = tiempo_espera_voraz(tareas, numero_de_candidatos=len(tareas))

print("Orden óptimo de ejecución:", solucion)
print("Tiempo total de espera:", tiempo_total)
print("Tiempo medio de espera:", round(tiempo_medio, 2))

