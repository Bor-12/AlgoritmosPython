#Problema 101
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import Optional
def dfs(arbol_izquierdo, arbol_derecho):
    if not arbol_izquierdo and not arbol_derecho:
        return True
    elif not arbol_derecho or not arbol_izquierdo:
        return False
    else:
        return (
                arbol_izquierdo.val == arbol_derecho.val and
                dfs(arbol_izquierdo.left, arbol_derecho.right) and
                dfs(arbol_izquierdo.right, arbol_derecho.left)
            )
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    return dfs(root.left, root.right)

