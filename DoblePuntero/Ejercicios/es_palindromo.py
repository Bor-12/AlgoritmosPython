def es_palindromo(string):
    lista = list(string)
    n = len(string)
    principio = 0
    final = n -1
    while principio < final:
        if lista[principio] != lista[final]:
            return False
        principio += 1
        final -= 1
    return True

print(es_palindromo("reconocer"))
print(es_palindromo("borrrrrrrrrr"))