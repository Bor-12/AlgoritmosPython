#Problema 112
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import Optional

def dfs(arbol, suma_acumulada, suma_objetivo):
    if not arbol:
        return False
    suma_acumulada +=  arbol.val
    if not arbol.left and not arbol.right and suma_acumulada == suma_objetivo:
        return True

    return dfs(arbol.left, suma_acumulada, suma_objetivo) or dfs(arbol.right, suma_acumulada, suma_objetivo)



def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    return dfs(root, 0, targetSum)
