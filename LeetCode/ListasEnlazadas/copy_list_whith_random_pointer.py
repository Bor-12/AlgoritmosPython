#Problema  138
from pyparsing import any_close_tag


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional
def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return None
    actual = head
    original_a_copia = {}
    while actual:
        nuevoNodo = Node(actual.val)
        original_a_copia[actual] = nuevoNodo
        actual = actual.next
    actual = head
    while actual:
        nuevoNodo = original_a_copia[actual]
        if actual.next:
            nuevoNodo.next = original_a_copia[actual.next]
        if actual.random:
            nuevoNodo.random = original_a_copia[actual.random]
        actual  = actual.next
    return original_a_copia[head]
