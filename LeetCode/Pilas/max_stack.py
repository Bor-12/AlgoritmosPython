from sortedcontainers import SortedList

class MaxStack:
    class Nodo:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    class Lista:
        def __init__(self):
            self.head = MaxStack.Nodo(0)
            self.tail = MaxStack.Nodo(0)
            self.head.next = self.tail
            self.tail.prev = self.head

        def append(self, val):
            nodo = MaxStack.Nodo(val)
            nodo.next = self.tail
            nodo.prev = self.tail.prev
            nodo.prev.next = nodo
            self.tail.prev = nodo
            return nodo

        def remove(self, nodo):
            nodo.prev.next = nodo.next
            nodo.next.prev = nodo.prev

        def top(self):
            return self.tail.prev.val

        def pop(self):
            nodo = self.tail.prev
            self.remove(nodo)
            return nodo

    def __init__(self):
        self.lista = MaxStack.Lista()
        self.sorted = SortedList(key=lambda nodo: nodo.val)

    def push(self, x):
        nodo = self.lista.append(x)
        self.sorted.add(nodo)

    def pop(self):
        nodo = self.lista.pop()
        self.sorted.remove(nodo)
        return nodo.val

    def top(self):
        return self.lista.top()

    def peekMax(self):
        return self.sorted[-1].val

    def popMax(self):
        nodo = self.sorted.pop()
        self.lista.remove(nodo)
        return nodo.val
