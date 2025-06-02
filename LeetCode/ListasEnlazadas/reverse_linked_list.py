#Problema 2
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    while head != None:
        nuevoNodo = ListNode(head.val, dummy.next)
        head = head.next
        dummy.next = nuevoNodo
    return dummy.next
#Si queremos que el espacio sea O(1):
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    actual = head
    anterior = None
    while actual != None:
        auxiliar = actual.next
        actual.next = anterior
        anterior = actual
        actual = auxiliar
    return anterior

