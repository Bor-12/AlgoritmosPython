#Problema 143
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
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



