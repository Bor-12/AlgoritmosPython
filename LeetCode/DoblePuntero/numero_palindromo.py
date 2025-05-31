#Problema  9
def isPalindrome(x: int) -> bool:
    lista_digitos = list(str(x))
    izquierda = 0
    derecha = len(lista_digitos) - 1
    while izquierda < derecha:
        if lista_digitos[izquierda] != lista_digitos[derecha]:
            return False
        izquierda += 1
        derecha -= 1
    return True


def isPalindrome2(x: int) -> bool:
    if x < 0: return False
    potencia_mayor = 1
    while x >= 10 * potencia_mayor:
        potencia_mayor *= 10
    while x:
        digito_derecha = x % 10
        digito_izquierda = x // potencia_mayor

        if digito_izquierda != digito_derecha:
            return False
        x = (x % potencia_mayor) // 10
        potencia_mayor //= 100  # porque se eliminan 2 dígitos
print(isPalindrome(121))
print(isPalindrome2(71217))