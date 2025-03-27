def decimal_a_binario_positivo(numero):
    if (numero == 0):
        return '0'

    resto = numero % 2
    if(resto == 0):
        return decimal_a_binario_positivo(numero // 2) + '0'
    if(resto == 1):
        return decimal_a_binario_positivo(numero // 2) + '1'

print(decimal_a_binario_positivo(10))

def decimal_a_binario(numero):

    if(numero >= 0):
        if (numero == 0):
            return '0'
        resto = numero % 2
        if(resto == 0):
            return decimal_a_binario_positivo(numero // 2) + '0'
        if(resto == 1):
            return decimal_a_binario_positivo(numero // 2) + '1'

    #lo pongo en complemento a 2
    numero_binario_puro = decimal_a_binario_positivo(abs(numero))
    #invierto todos los bits

    numero_complemento_a_uno = [''] * len(numero_binario_puro)

    for i in range(len(numero_binario_puro)):
        if (numero_binario_puro[i] == '0'):
            numero_complemento_a_uno[i] = '1'
        else:
            numero_complemento_a_uno[i] = '0'

    def sumar_binario_recursivo(bin1, bin2, acarreo=0):
        if not bin1 and not bin2:
            return ['1'] if acarreo else []

        # Tomamos el último bit de cada lista o 0 si ya no hay más
        bit1 = int(bin1[-1]) if bin1 else 0
        bit2 = int(bin2[-1]) if bin2 else 0

        suma = bit1 + bit2 + acarreo
        bit_resultado = str(suma % 2)
        nuevo_acarreo = suma // 2

        # Llamada recursiva con el resto
        resultado_restante = sumar_binario_recursivo(bin1[:-1], bin2[:-1], nuevo_acarreo)

        return resultado_restante + [bit_resultado]

    # Le sumo 1 para pasar de complemento a 1 a complemento a 2 :)
    numero_uno = ['0'] * len(numero_complemento_a_uno)
    numero_uno[-1] = '1'
    numero_complemento_a_dos = sumar_binario_recursivo(numero_complemento_a_uno, numero_uno)
    return ''.join(numero_complemento_a_dos)

print(decimal_a_binario(10))
print(decimal_a_binario(-10))