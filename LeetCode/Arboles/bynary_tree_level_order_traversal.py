#Problema 102
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import Optional
from typing import List
#bfs
from collections import deque
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    cola = deque([root])
    niveles = []
    while cola:
        nivel = []
        for _ in range(len(cola)):
            nodo = cola.popleft()
            nivel.append(nodo.val)
            if nodo.left:
                cola.append(nodo.left)
            if nodo.right:
                cola.append(nodo.right)
        niveles.append(nivel)
    return niveles