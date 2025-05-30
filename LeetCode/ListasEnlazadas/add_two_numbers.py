#Problema 2
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Devuelve una lista enlazada con la suma dígito a dígito de l1 y l2, considerando el acarreo.

    Args:
        l1 (Optional[ListNode]): Primera lista enlazada que representa un número en orden inverso.
        l2 (Optional[ListNode]): Segunda lista enlazada que representa un número en orden inverso.

    Returns:
        Optional[ListNode]: Lista enlazada resultante de sumar l1 y l2.
    """
    dummy = ListNode()
    actual = dummy
    acarreo = 0
    while l1 != None or l2 != None or acarreo > 0:
        #asignar valores l1 y l2 , si es None se asigna 0
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        suma = val1 + val2 + acarreo
        acarreo = suma // 10

        nuevo_nodo = ListNode(suma % 10)
        actual.next = nuevo_nodo
        actual = actual.next

        # avanzar l1 y l2 si no son None
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next