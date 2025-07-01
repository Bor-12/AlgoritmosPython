#Problema 19
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    primero = segundo = dummy

    for _ in range(n + 1):
        primero = primero.next

    while primero:
        primero = primero.next
        segundo = segundo.next

    segundo.next = segundo.next.next

    return dummy.next