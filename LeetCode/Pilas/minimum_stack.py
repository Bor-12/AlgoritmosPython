
class MinStack:

    def __init__(self):
        self.pila = []
        self.minimoPila = []
    def push(self, val: int) -> None:
        self.pila.append(val)
        val = min(val, self.minimoPila[-1] if self.minimoPila else val)
        self.minimoPila.append(val)
    def pop(self) -> None:
        self.pila.pop()
        self.minimoPila.pop()
    def top(self) -> int:
        return self.pila[-1]
    def getMin(self) -> int:
        return self.minimoPila[-1]