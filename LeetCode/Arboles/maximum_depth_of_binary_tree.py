#Problema 104
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import Optional

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    else:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
#Se puede hacer sin recursividad
#bfs
from collections import deque
def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    nivel = 0
    cola = deque([root])
    while cola:
        for i in range(len(cola)):
            nodo = cola.popleft()
            if nodo.left:
                cola.append(nodo.left)
            if nodo.right:
                cola.append(nodo.right)
        nivel += 1
    return nivel
#dfs
def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    pila = [[root, 1]]
    resultado = 1
    while pila:
        nodo, nivel = pila.pop()
        if nodo:
            resultado = max(resultado, nivel)
            pila.append([nodo.left, nivel + 1])
            pila.append([nodo.right, nivel + 1])
    return resultado