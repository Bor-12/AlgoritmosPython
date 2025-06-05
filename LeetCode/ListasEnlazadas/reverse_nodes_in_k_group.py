#Problema 25
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

def invertir(inicio, k):
    anterior = None
    actual = inicio
    while k:
        auxiliar = actual.next
        actual.next = anterior
        anterior = actual
        actual = auxiliar
        k -= 1
    return anterior
def se_puede_agrupar(inicio, grupo):
    contador = 0
    actual = inicio
    while actual and contador < grupo:
        actual = actual.next
        contador += 1
    return contador == grupo
def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head
    anterior_grupo = dummy
    while se_puede_agrupar(anterior_grupo.next, k):
        inicio = anterior_grupo.next
        final = inicio
        pasos = k - 1
        while pasos:
            final = final.next
            pasos -= 1
        siguiente_grupo = final.next

        # usar la función reverse
        nuevo_inicio = invertir(inicio, k)

        # reconectar
        anterior_grupo.next = nuevo_inicio
        inicio.next = siguiente_grupo
        anterior_grupo = inicio
    return dummy.next
# Crear la lista
n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

# Ejecutar función
k = 2
res = reverseKGroup(n1, k)

# Imprimir resultado
def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

print_list(res)