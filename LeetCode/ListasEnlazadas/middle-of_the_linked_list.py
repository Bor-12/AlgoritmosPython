#Problema 876
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    rapido = head
    lento = head
    while rapido and rapido.next:
        rapido = rapido.next.next
        lento = lento.next
    return lento