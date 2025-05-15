"""
Haz un programa que genere todas las combinaciones posibles (variaciones con repetición)
de una lista de n elementos.

Cada combinación debe tener la misma longitud que la lista original,
y se permite repetir elementos. El orden importa.

RESTRICCIÓN: No se permiten dos elementos iguales consecutivos en la combinación.
Por ejemplo, si la lista es [1, 4, 3], combinaciones como [1, 1, 4] o [3, 3, 1] deben excluirse.
"""

def variaciones_con_repeticion(lista):
    repeticion = [len(lista)] * len(lista)
    solucion = [None] * len(lista)
    variciones_con_repeticion_recursivo(0, solucion, lista,repeticion)
def variciones_con_repeticion_recursivo(i, solucion,lista, repeticion):
    if  i == len(lista):
        print(solucion)
    else:
        for k in range(len(lista)):
            if repeticion[k] > 0 :
                repeticion[k] -= 1
                solucion[i] =  lista[k]
                variciones_con_repeticion_recursivo(i +1 , solucion, lista, repeticion)
                repeticion[k] += 1


def variaciones_con_repeticion_filtrada(lista):
    repeticion = [len(lista)] * len(lista)
    solucion = [None] * len(lista)
    variciones_con_repeticion_recursivo_filtrada(0, solucion, lista,repeticion, lista[-1])#meto lista[-1] porque empiezo por el primero
def variciones_con_repeticion_recursivo_filtrada(i, solucion,lista, repeticion, ultimo_elemento_anadido):
    if  i == len(lista):
        print(solucion)
    else:
        for k in range(len(lista)):
            if (repeticion[k] > 0 and ultimo_elemento_anadido != lista[k]) or len(lista) == 1:
                repeticion[k] -= 1
                solucion[i] =  lista[k]
                variciones_con_repeticion_recursivo_filtrada(i +1 , solucion, lista, repeticion, lista[k])
                repeticion[k] += 1
print("Variaciones con repetición:")
variaciones_con_repeticion([1, 4, 3])

print("Variaciones con la restricción:")
variaciones_con_repeticion_filtrada([1, 4, 3])

