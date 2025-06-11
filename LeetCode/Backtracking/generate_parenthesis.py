from typing import List
def generar_parentesis_recurisivo(i, candidatos, solucion_parcial, parentesis_abierto, soluciones, n):
    if i == len(solucion_parcial):
        soluciones.append("".join(solucion_parcial))
    else:
        for k in range(len(candidatos)):
            nuevo_abiertos = parentesis_abierto if  k == 1 else parentesis_abierto + 1 #si k es igaul a 0 se añade 1 parentesis abierto  '('
            cerrados = i - nuevo_abiertos + 1
            if nuevo_abiertos >= cerrados and nuevo_abiertos <= n:
                solucion_parcial[i] = candidatos[k]
                generar_parentesis_recurisivo(i + 1, candidatos, solucion_parcial, nuevo_abiertos, soluciones, n)

def generateParenthesis(n: int) -> List[str]:
    posibles_parentesis = ["(", ")"]
    solucion_parcial = [None] * 2 * n
    soluciones = []
    generar_parentesis_recurisivo(0, posibles_parentesis, solucion_parcial,  0, soluciones, n)
    return soluciones
print(generateParenthesis(3))