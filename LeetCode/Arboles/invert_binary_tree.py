class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import Optional
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)

    return root
#dfs
def invertTree2(root: Optional[TreeNode]) -> Optional[TreeNode]:
    pila = [root]
    while pila:
        nodo = pila.pop()
        if nodo:
            pila.append(nodo.left)
            pila.append(nodo.right)
            nodo.left, nodo.right = nodo.right, nodo.left
    return root
