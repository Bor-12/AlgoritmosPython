def indice_mejor_valor_por_peso(valores: list[int], pesos: list[int], candidatos: set) -> int:
    indice_mejor_candidato = -1
    valor_mejor_candidato = -1
    for c in candidatos:
        valor_actual = valores[c] / pesos[c]
        if valor_actual > valor_mejor_candidato:
            valor_mejor_candidato = valor_actual
            indice_mejor_candidato = c
    return indice_mejor_candidato
def es_factible(indice: int, pesos: list[int], peso_restante: int)-> bool:
    return pesos[indice] <= peso_restante
def mochila_voraz(valores: list[int], pesos: list[int], peso_maximo_mochila: int) -> list[float]:
    """Algoritmo voraz para resolver el problema de la mochila fraccionaria.

    Args:
        profit (List[int]): Lista con los beneficios de los objetos.
        weight (List[int]): Lista con los pesos de los objetos.
        max_weight (int): Capacidad máxima de la mochila.

    Returns:
        List[float]: Lista con la fracción de cada objeto tomado.
    """

    n = len(valores)
    sol = [0] * n
    candidatos = set()
    for i in range(n):
        candidatos.add(i)
    peso_restante = peso_maximo_mochila
    esta_resuelto = False
    while not esta_resuelto and candidatos:
        indice = indice_mejor_valor_por_peso(valores, pesos, candidatos)
        candidatos.remove(indice)
        if es_factible(indice, pesos, peso_restante):
            sol[indice] = 1.0
            peso_restante -= pesos[indice]
        else:
            sol[indice] = peso_restante /  pesos[indice]
            esta_resuelto = True
    return sol

solution = mochila_voraz(valores = [20, 30, 66, 40, 60], pesos = [10, 20, 30, 40, 50], peso_maximo_mochila = 100)
print(solution)  # [1.0, 1.0, 1.0, 0, 0.8]


