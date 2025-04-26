#Es un problema de optimizacion, podo el arbol si ya se ha pasado de peso o si no puede llegar a una solucion mejor
def mochila_01(peso, valor, capacidad):
    solucion = [0] * len(peso)
    sol_optima = [0] * len(peso)
    valor_total  = mochila_01_recursivo(0, capacidad, 0, sum(valor),solucion, sol_optima, -1, peso, valor)
    return valor_total , sol_optima
def mochila_01_recursivo(i, capacidad_actual, valor_actual, valor_maximo,solucion_parcial, solucion_optima, valor_optimo, peso, valor):
    if i == len(solucion_parcial):
        if valor_actual > valor_optimo:
            valor_optimo = valor_actual
            for k in range(len(solucion_parcial)):
                solucion_optima[k] = solucion_parcial[k]
    else:
        for k in range(2):
            if capacidad_actual - k * peso[i] >= 0: #podamos por peso
                nuevo_valor_maximo = valor_maximo  - (1 - k) * valor[i] #si no cogemos el objeto lo restamos
                if nuevo_valor_maximo > valor_optimo: #podamos por no poder llegar al valor optimo
                    nuevo_valor_actual = valor_actual + k * valor[i]
                    nuevo_capacidad_actual = capacidad_actual - k * peso[i]
                    solucion_parcial[i] = k
                    valor_optimo = mochila_01_recursivo(i + 1 , nuevo_capacidad_actual, nuevo_valor_actual, nuevo_valor_maximo, solucion_parcial,solucion_optima, valor_optimo,
                                         peso, valor)
    return valor_optimo
peso = [3, 6, 9, 5]
valor = [7, 2, 10, 4]
capacidad = 15
print(mochila_01(peso, valor, capacidad)) #1 se coge el objeto 0 no se coge