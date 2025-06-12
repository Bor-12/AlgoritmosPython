#Problema 143
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

#O(n) en espacio
def reorderList(self, head: Optional[ListNode]) -> None:

    if not head or not head.next:
        return

    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next

    i, j = 0, len(nodes) - 1
    while i < j:
        nodes[i].next = nodes[j]
        i += 1
        if i == j:
            break
        nodes[j].next = nodes[i]
        j -= 1

    nodes[i].next = None
#O(1) en espacio
def reorderList(head: Optional[ListNode]) -> None:
    """
           Do not return anything, modify head in-place instead.
    """
    lento = head
    rapido = head

    #Consigo la mitad de la lista
    while rapido and rapido.next:
        lento = lento.next
        rapido = rapido.next.next
    #divido la lista en 2
    # lento esta en la mitad de la lista
    segunda_lista = lento.next
    lento.next = None

    #invierto la mitad derecha de la lista
    #anterior tendra el principio de la lista
    anterior = None
    while segunda_lista:
        auxiliar = segunda_lista.next
        segunda_lista.next = anterior
        anterior = segunda_lista
        segunda_lista = auxiliar

    #junto las dos listas
    primero, segundo =head, anterior
    while segundo:
        temporal1, temporal2 = primero.next, segundo.next
        primero.next = segundo
        segundo.next = temporal1
        primero, segundo = temporal1, temporal2



