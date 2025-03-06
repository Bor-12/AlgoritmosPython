import numpy as np
from typing import List

def calcular_longitud_circuito(circuito: List[int], matriz_distancias: np.ndarray) -> int:
    """Recibe un circuito como una lista de ciudades (índices) y una matriz de distancias,
    y devuelve la longitud total del circuito.

    Parámetros:
    -----------
    - circuito (List[int]): Lista de ciudades en orden de visita.
    - matriz_distancias (np.ndarray): Matriz de distancias entre ciudades.

    Retorno:
    --------
    - int: Longitud total del circuito según la matriz de distancias.
    """
    long_total = 0
    distancias = []
    for i in range(len(circuito) - 1):
        distancias.append(matriz_distancias[circuito[i], circuito[i+1]])

    return np.array(distancias).sum()

def tsp_voraz(matriz_distancias: np.ndarray, ciudad_inicial: int = 0) -> List[int]:
    """Implementa un algoritmo voraz (greedy) para resolver una aproximación
    del Problema del Viajante de Comercio (TSP).

    Parámetros:
    -----------
    - matriz_distancias (np.ndarray): Matriz de distancias entre ciudades.
    - ciudad_inicial (int, opcional): Ciudad donde comienza el recorrido (por defecto 0).

    Retorno:
    --------
    - List[int]: Lista con el orden de las ciudades en el recorrido.
    """
    num_ciudades = matriz_distancias.shape[0]
    circuito = [ciudad_inicial]

    while len(circuito) < num_ciudades:
        ciudad_actual = circuito[-1]

        # Ordenar las ciudades contiguas a la actual por distancia
        opciones = list(np.argsort(matriz_distancias[ciudad_actual]))

        for ciudad in opciones:
            if ciudad not in circuito:
                circuito.append(int(ciudad))  # Convertir np.int64 a int nativo de Python
                break

    return circuito + [ciudad_inicial]


matriz_distancias = np.array([
    [0, 624, 995, 350],
    [624, 0, 506, 357],
    [995, 506, 0, 653],
    [350, 357, 653, 0]
])

circuito = tsp_voraz(matriz_distancias)
print("Circuito recorrido:", circuito)
longitud_total = calcular_longitud_circuito(circuito, matriz_distancias)
print("Longitud total del circuito:", longitud_total)
