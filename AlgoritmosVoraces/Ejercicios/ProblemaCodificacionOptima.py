"""
problema de la codificación óptima utilizando el algoritmo de huffman.

dado un conjunto de caracteres y sus respectivas frecuencias de aparición en un documento,
se construye un árbol de huffman para asignar códigos binarios óptimos a cada carácter,
minimizando la longitud total del mensaje codificado.

el algoritmo de huffman es un método de compresión basado en la construcción de un árbol
binario donde los caracteres menos frecuentes están más profundos y los más frecuentes
están más cerca de la raíz.

salida esperada:
- un árbol de huffman estructurado.
- un diccionario con los códigos huffman para cada carácter.
"""

from anytree import Node, RenderTree
from typing import List, Dict, Set


def menor_frecuencia(frecuencias: List[int], candidatos: Set[int]) -> int:
    """
    encuentra el índice del candidato con la menor frecuencia en la lista dada.

    :param frecuencias: lista de frecuencias de cada carácter.
    :param candidatos: conjunto de índices de los caracteres aún disponibles.
    :return: índice del carácter con la menor frecuencia.
    """
    min_valor = float('inf')
    indice_min = -1
    for i in candidatos:
        if frecuencias[i] < min_valor:
            min_valor = frecuencias[i]
            indice_min = i
    return indice_min


def huffman(caracteres: List[str], frecuencias: List[int]) -> Node:
    """
    construye el árbol de huffman a partir de una lista de caracteres y sus frecuencias.

    :param caracteres: lista de caracteres.
    :param frecuencias: lista de frecuencias asociadas a cada carácter.
    :return: nodo raíz del árbol de huffman.
    """
    n = len(caracteres)
    candidatos = set(range(n))
    arbol_huffman = [Node(caracteres[i]) for i in range(n)]

    while len(candidatos) > 1:
        indice_mejor_candidato_1 = menor_frecuencia(frecuencias, candidatos)
        candidatos.remove(indice_mejor_candidato_1)
        indice_mejor_candidato_2 = menor_frecuencia(frecuencias, candidatos)
        candidatos.remove(indice_mejor_candidato_2)

        nuevo_nodo1 = arbol_huffman[indice_mejor_candidato_1]
        nuevo_nodo2 = arbol_huffman[indice_mejor_candidato_2]

        nodo_padre = Node(f"{frecuencias[indice_mejor_candidato_1] + frecuencias[indice_mejor_candidato_2]}")
        nuevo_nodo1.parent = nodo_padre
        nuevo_nodo2.parent = nodo_padre

        arbol_huffman.append(nodo_padre)
        frecuencias.append(frecuencias[indice_mejor_candidato_1] + frecuencias[indice_mejor_candidato_2])
        candidatos.add(len(frecuencias) - 1)

    return arbol_huffman[-1]


def generar_codigos(nodo: Node, codigo_actual: str = "", codigos_huffman: Dict[str, str] = {}) -> Dict[str, str]:
    """
    recorre el árbol de huffman en preorden y asigna códigos binarios a cada carácter.

    :param nodo: nodo actual del árbol
    :param codigo_actual: código binario acumulado hasta el nodo actual
    :param codigos_huffman: diccionario donde se almacenan los códigos de cada carácter
    :return: diccionario con los códigos de cada carácter
    """
    if nodo.is_leaf:
        codigos_huffman[nodo.name] = codigo_actual
    else:
        if nodo.children:
            generar_codigos(nodo.children[0], codigo_actual + "0", codigos_huffman)
        if len(nodo.children) > 1:
            generar_codigos(nodo.children[1], codigo_actual + "1", codigos_huffman)

    return codigos_huffman


caracteres = ['a', 'b', 'c', 'd']
frecuencias = [5, 9, 12, 13]
raiz = huffman(caracteres, frecuencias)
for pre, _, node in RenderTree(raiz):
    print(f"{pre}{node.name}")
codigos = generar_codigos(raiz)
for caracter, codigo in codigos.items():
    print(f"{caracter} → {codigo}")
caracteres = ['x', 'y', 'z', 'w', 'v', 'u']
frecuencias = [30, 12, 8, 20, 15, 10]

raiz = huffman(caracteres, frecuencias)

for pre, _, node in RenderTree(raiz):
    print(f"{pre}{node.name}")

codigos = generar_codigos(raiz)

for caracter, codigo in codigos.items():
    print(f"{caracter} → {codigo}")
