#Problema 282
from typing import List, Dict, Tuple

def addOperators(num: str, target: int) -> List[str]:
    soluciones = []
    backtracking_operaciones(soluciones, "", num, target, 0, 0, 0)
    return soluciones

def backtracking_operaciones(
        soluciones: List[str],
        solucion_parcial: str,
        cadena_numeros: str,
        suma_objetivo: int,
        posicion_cadena_numeros: int,
        suma_actual: int,
        ultimo_valor: int
):
    if posicion_cadena_numeros == len(cadena_numeros):
        if suma_actual == suma_objetivo:
            soluciones.append(solucion_parcial)
    else:

        for i in range(posicion_cadena_numeros, len(cadena_numeros)):
            # Evitar números con ceros a la izquierda
            if i != posicion_cadena_numeros and cadena_numeros[posicion_cadena_numeros] == '0':
                break

            segmento = cadena_numeros[posicion_cadena_numeros:i + 1]
            numero_actual = int(segmento)

            if posicion_cadena_numeros == 0:
                # Primer número, se agrega sin operador
                backtracking_operaciones(
                    soluciones, segmento, cadena_numeros, suma_objetivo,
                    i + 1, numero_actual, numero_actual
                )
            else:
                # Suma
                backtracking_operaciones(
                    soluciones, solucion_parcial + "+" + segmento, cadena_numeros,
                    suma_objetivo, i + 1, suma_actual + numero_actual, numero_actual
                )
                # Resta
                backtracking_operaciones(
                    soluciones, solucion_parcial + "-" + segmento, cadena_numeros,
                    suma_objetivo, i + 1, suma_actual - numero_actual, -numero_actual
                )
                # Multiplicación
                backtracking_operaciones(
                    soluciones, solucion_parcial + "*" + segmento, cadena_numeros,
                    suma_objetivo, i + 1,
                                suma_actual - ultimo_valor + ultimo_valor * numero_actual,
                                ultimo_valor * numero_actual
                )


print(addOperators("123", 6))         # ['1+2+3', '1*2*3']
print(addOperators("105", 5))         # ['1*0+5', '10-5']
print(addOperators("3456237490", 9191))  # []
#Lo hago mas moduladizable:
def addOperators2(cadena: str, objetivo: int) -> List[str]:
    soluciones = []

    from typing import Callable

    operaciones: Dict[str, Callable[[int, int, int], Tuple[int, int]]] = {
        '+': lambda res, ult, num: (res + num, num),
        '-': lambda res, ult, num: (res - num, -num),
        '*': lambda res, ult, num: (res - ult + ult * num, ult * num)
    }

    backtracking_operaciones2(soluciones, "", cadena, objetivo, 0, 0, 0, operaciones)
    return soluciones

def backtracking_operaciones2(
        soluciones: List[str],
        expresion_actual: str,
        cadena: str,
        objetivo: int,
        posicion: int,
        resultado_actual: int,
        ultimo_valor: int,
        operaciones: Dict[str, callable]
):
    if posicion == len(cadena):
        if resultado_actual == objetivo:
            soluciones.append(expresion_actual)
        return

    for i in range(posicion, len(cadena)):
        if i != posicion and cadena[posicion] == '0':
            break

        segmento = cadena[posicion:i + 1]
        numero_actual = int(segmento)

        if posicion == 0:
            backtracking_operaciones2(
                soluciones, segmento, cadena, objetivo, i + 1,
                numero_actual, numero_actual, operaciones
            )
        else:
            for operador, funcion in operaciones.items():
                nuevo_resultado, nuevo_ultimo = funcion(resultado_actual, ultimo_valor, numero_actual)
                nueva_expresion = expresion_actual + operador + segmento
                backtracking_operaciones2(
                    soluciones, nueva_expresion, cadena, objetivo, i + 1,
                    nuevo_resultado, nuevo_ultimo, operaciones
                )



print(addOperators2("123", 6))         # ['1+2+3', '1*2*3']
print(addOperators2("105", 5))         # ['1*0+5', '10-5']
print(addOperators2("3456237490", 9191))  # []
