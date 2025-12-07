#Meotodo voraz
def cabe (moneda, monto):
    return monto // moneda != 0


def cambio_voraz(valores_monedas: list[int], monto_objetivo: int) -> list[int]:
    """ Algoritmo voraz para descomponer un monto en monedas de mayor a menor valor.

    Args:
        valores_monedas (List[int]): Lista con los valores de las monedas disponibles.
        monto_objetivo (int): Cantidad de dinero a descomponer en monedas.

    Returns:
        List[int]: Lista con la cantidad de cada moneda utilizada.
    """
    solucion_cambio = [0] * len(valores_monedas)
    indice = 0
    while indice < len(valores_monedas):
        if not cabe(valores_monedas[indice], monto_objetivo):
            indice += 1
        else:
            solucion_cambio[indice] += 1
            monto_objetivo -= valores_monedas[indice]
    return solucion_cambio
def  monedas_que_caben(moneda, monto):
    return  monto // moneda
def cambio_voraz_mejorado(valor_monedas: list[int], monto_objetivo: int) -> list [int]:
    """ Algoritmo voraz para descomponer un monto en monedas de mayor a menor valor.

       Args:
           valores_monedas (List[int]): Lista con los valores de las monedas disponibles.
           monto_objetivo (int): Cantidad de dinero a descomponer en monedas.

       Returns:
           List[int]: Lista con la cantidad de cada moneda utilizada.
       """
    indice = 0
    solucion_cambio = [0] * len(valor_monedas)
    while indice < len(valor_monedas):
        moneda = monedas_que_caben(valor_monedas[indice], monto_objetivo)
        if moneda > 0:
            solucion_cambio[indice] = moneda
            monto_objetivo -= moneda * valor_monedas[indice]
        indice += 1
    return solucion_cambio

valor_monedas = [500, 200, 100, 50, 20 , 10 , 5, 2 , 1]
monto_objetivo =  33
solucion_cambio = cambio_voraz(valor_monedas, monto_objetivo)
print(solucion_cambio)
solucion_cambio = cambio_voraz_mejorado(valor_monedas, monto_objetivo)
print(solucion_cambio)
