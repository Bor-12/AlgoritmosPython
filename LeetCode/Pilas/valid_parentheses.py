def isValid(s: str) -> bool:
    pila = []
    for letra in s:
        if letra == '(' :
            pila.append(')')
        elif letra == '{':
            pila.append('}')
        elif letra == '[':
            pila.append(']')
        else:
            if not pila or pila.pop() != letra:
                return False
    return False if pila else True
#Solucion video:
def isValid2(s: str) -> bool:
    pila = []
    correspondecias = {")":"(", "]": "[", "}": "{"}
    for letra in s:
        if letra not in correspondecias:
            pila.append(letra)
        else:
            if not pila or pila.pop() != correspondecias[letra]:
                return False
    return False if pila else True
print(isValid("([{}])"))
print(isValid("["))
print(isValid("]"))
print(isValid2("([{}])"))
print(isValid2("["))
print(isValid2("]"))