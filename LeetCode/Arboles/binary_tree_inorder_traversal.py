from collections import deque
from typing import Deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorden(node, solucion):
    if node:
        inorden(node.left, solucion)
        solucion.append(node.val)
        inorden(node.right, solucion)
    return solucion

def inorderTraversal(root):
    solucion = []
    inorden(root, solucion)
    return solucion

def inorderTraversal2(root):
    resultado = []
    pila = deque()
    actual = root

    while pila or actual:
        while actual:
            # Bajar a la izquierda lo más posible
            pila.append(actual)
            actual = actual.left
        # Subir un nivel y procesar nodo
        actual = pila.pop()
        resultado.append(actual.val)
        # Ir a la derecha
        actual = actual.right

    return resultado


#         4
#       /   \
#      2     6
#     / \   / \
#    1   3 5   7

nodo1 = TreeNode(1)
nodo3 = TreeNode(3)
nodo5 = TreeNode(5)
nodo7 = TreeNode(7)
nodo2 = TreeNode(2, left=nodo1, right=nodo3)
nodo6 = TreeNode(6, left=nodo5, right=nodo7)
nodo4 = TreeNode(4, left=nodo2, right=nodo6)


resultado1 = inorderTraversal(nodo4)
print("Recorrido inorden (recursivo):", resultado1)

resultado2 = inorderTraversal2(nodo4)
print("Recorrido inorden (iterativo):", resultado2)
