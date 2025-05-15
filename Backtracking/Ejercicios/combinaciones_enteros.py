
# Dado un entero n y un entero k,
# genera todas las combinaciones posibles de tamaño k
# con números del 1 al n (ambos incluidos), sin repetir elementos y en orden creciente.
# Cada combinación debe tener exactamente k números distintos.
# El orden dentro de la lista no importa, pero debe estar en orden creciente
# para que no se repitan combinaciones como [2,1] si ya existe [1,2].

#es un problema de subconjuntos , hay que frenar el arbol recursivo  cuando  sea igual a k
def combinaciones_enteros(n, k):
    solucion = [None]  * k
    combinaciones_enteros_recursivo(0, -1,solucion, n, k)
def combinaciones_enteros_recursivo(i, j,solucion_parcial, n, k):
    if i == k:
        print(solucion_parcial)
    else:
        for r in range(j +1, n  + 1):
            solucion_parcial[i] = r
            combinaciones_enteros_recursivo(i +1, r,solucion_parcial, n, k)
combinaciones_enteros(n=4, k=2)
