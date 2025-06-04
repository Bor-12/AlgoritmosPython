#Problema 141
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
def hasCycle(head: Optional[ListNode]) -> bool:
    rapido = head
    lento = head
    while rapido and rapido.next:
        rapido = rapido.next.next
        lento = lento.next
        if rapido == lento:
            return True
    return False