def espejo():
    string = input()

    def recursividad(cadena):
        if len(cadena) <= 1:
            return cadena
        # Recursión: tomamos el último carácter y lo agregamos a la inversión del resto
        return cadena[-1] + recursividad(cadena[:-1])

    nueva_cadena = recursividad(string)

    return nueva_cadena

print(espejo())

