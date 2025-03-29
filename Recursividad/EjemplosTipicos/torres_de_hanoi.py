"""Implemente una función recursiva llamada torres_de_hanoi que, dado un número de discos y tres postes (origen, auxiliar y destino),
 imprima los pasos necesarios para mover todos los discos del poste de origen al poste destino, siguiendo estas reglas:

-Solo se puede mover un disco a la vez.

-Solo se puede mover el disco superior de una pila.

-No se puede colocar un disco más grande sobre uno más pequeño.

"""

def torres_de_hanoi(n, origen, auxiliar, destino):
    """
       n: número de discos
       origen: el poste desde donde se mueven los discos (por ejemplo, 'A')
       auxiliar: el poste auxiliar (por ejemplo, 'B')
       destino: el poste objetivo (por ejemplo, 'C')
       """
    if n == 1:
        print(f"Mover disco de {origen} a {destino}")
        return

    torres_de_hanoi(n - 1, origen, destino, auxiliar)
    print(f"Mover disco de {origen} a {destino}")
    torres_de_hanoi(n - 1, auxiliar, origen, destino)



torres_de_hanoi(10, 'A', 'B', 'C')