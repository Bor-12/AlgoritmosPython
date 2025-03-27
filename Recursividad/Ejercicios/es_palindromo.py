def es_palindromo_recursivo(string):
    lista = list(string)
    n = len(string)
    if (n <= 1):
        return True
    return string[-1] == string[0] and es_palindromo_recursivo(lista[1:-1])
print(es_palindromo_recursivo("reconocer"))
print(es_palindromo_recursivo("borrrrrrrrrr"))