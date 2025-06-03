#Problema 150
from typing import List
def evalRPN(tokens: List[str]) -> int:
    pila = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            a = pila.pop()
            b = pila.pop()
            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(b - a)
            elif token == '*':
                pila.append(a * b)
            else:
                pila.append(int(b / a)) #int(b / a) para que trunque en 0, si hiciese b // a truncaria hacia abajo
        else:
            pila.append(int(token))
    return pila.pop()
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))