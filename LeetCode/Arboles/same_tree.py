#Problema 100
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import Optional

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    elif not p and q or p and not q:
        return False
    else:
        return p.val == q.val and isSameTree(p.right, q.right) and isSameTree(p.left, q.left)
