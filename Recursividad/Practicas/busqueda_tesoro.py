def capturar_datos():
    string = input()
    lista = eval(string)
    return lista


def busqueda_tesoro():

    lista_tesoros = capturar_datos()

    def recursividad(lista_tesoro):

        n = len(lista_tesoro)
        suma_total_monedas = 0
        numero_total_de_monedas = 0

        for i in range(n):
            moneda = 0
            numero_de_cofres = 0

            if isinstance(lista_tesoro[i] , list):
                moneda, numero_monedas = recursividad(lista_tesoro[i])
                numero_total_de_monedas += numero_monedas
            else:
                numero_total_de_monedas += 1
                moneda = lista_tesoro[i]

            suma_total_monedas += moneda

        return suma_total_monedas, numero_total_de_monedas

    return recursividad(lista_tesoros)

print(busqueda_tesoro())