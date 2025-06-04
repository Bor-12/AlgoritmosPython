#Problema 707
class Node:
    def __init__(self, val: int):
        self.elemento = val
        self.siguiente = None
        self.anterior = None
class MyLinkedList:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.longitud = 0

    def get(self, index: int) -> int:
        if index >= self.longitud or index < 0:
            return -1
        actual = self.inicio
        while index:
            actual = actual.siguiente
            index -= 1
        return actual.elemento

    def addAtHead(self, val: int) -> None:
        nuevoNodo = Node(val)
        if self.inicio:
            self.inicio.anterior = nuevoNodo
            nuevoNodo.siguiente  = self.inicio
        else:
            self.final = nuevoNodo
        self.inicio = nuevoNodo
        self.longitud += 1

    def addAtTail(self, val: int) -> None:
        nuevoNodo = Node(val)
        if self.final:
            self.final.siguiente = nuevoNodo
            nuevoNodo.anterior = self.final
        else:
            self.inicio = nuevoNodo
        self.final = nuevoNodo
        self.longitud += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.longitud:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.longitud:
            self.addAtTail(val)
            return
        nuevoNodo = Node(val)
        actual = self.inicio
        while index:
            actual = actual.siguiente
            index -= 1
        nuevoNodo.siguiente = actual
        nuevoNodo.anterior = actual.anterior
        actual.anterior.siguiente = nuevoNodo
        actual.anterior = nuevoNodo
        self.longitud += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.longitud or index < 0:
            return
        actual = self.inicio
        while index:
            actual = actual.siguiente
            index  -= 1
        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        else:
            self.inicio = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        else:
            self.final = actual.anterior

        actual.siguiente = None
        actual.anterior = None
        actual = None

        self.longitud -= 1


myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)     # linked list becomes 1->2->3
print(myLinkedList.get(1))        # returns 2
myLinkedList.deleteAtIndex(1)     # now the linked list is 1->3
print(myLinkedList.get(1))        # returns 3
