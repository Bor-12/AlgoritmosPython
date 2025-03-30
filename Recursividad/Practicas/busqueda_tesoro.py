"""
Capitán Recursión y el tesoro de los cofres anidados

En alta mar, el Capitán Recursión ha descubierto un antiguo mapa que señala la ubicación
de un tesoro legendario. Según la leyenda, el tesoro está repartido en múltiples cofres;
algunos de ellos contienen monedas de oro (números enteros) y otros cofres esconden,
a su vez, más cofres. Para conocer el botín total, el capitán debe sumar todas las monedas,
sin importar cuán profundamente estén anidadas dentro de los cofres.

Ayuda al Capitán Recursión a abrir cada cofre y a sumar todas las monedas usando una
solución recursiva que procese listas anidadas. Recuerda que no se deben utilizar bucles
iterativos, sino únicamente funciones recursivas.

Entrada:
La entrada consiste en una única línea que representa la estructura anidada de los cofres
en formato de lista. Cada elemento de la lista es, o bien, un entero (la cantidad de monedas
en ese cofre) o bien otra lista (un cofre que contiene más monedas o cofres).
Los elementos se separan por comas y la estructura se delimita con corchetes.

Salida:
La salida debe mostrar una dupla: un entero, que es la suma total de todas las monedas
encontradas en todos los cofres, sin importar el nivel de anidamiento y, el número de
monedas.

Ejemplo de entrada:
[1,[2,3],4,[5,[6,7],8],9]

Ejemplo de salida:
(45, 9)

Límites:
• La lista anidada contendrá entre 0 y 100,000 elementos en total.
• Cada valor entero estará en el rango de -10⁹ a 10⁹.
• La profundidad de anidamiento no excederá los 100 niveles.
"""
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