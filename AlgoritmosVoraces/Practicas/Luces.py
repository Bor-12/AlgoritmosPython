"""
Que se enciendan las luces

En un programa de televisión en el que queremos maximizar las veces que se encienden
las luces de la tentación de cada concursante, nos han pedido que diseñemos un algoritmo
capaz de decidir qué persona es una mayor tentación dependiendo de los gustos de cada
concursante. Para conseguir encender la luz de un concursante, este debe ser seducido.

Los datos con los que contamos son, por un lado, la característica que más valora el
concursante en una pareja, y por otro, qué valor tiene cada persona en cada una de las
características. Además, se debe tener en cuenta que hay un límite de tiempo, por lo que
nos facilitarán el tiempo que necesita cada persona para seducir al concursante. Si a la
última persona no le da tiempo a seducir por completo al concursante, el beneficio
obtenido será proporcional al tiempo que ha podido dedicar a su seducción.

Entrada:
La primera línea contiene un número entero 𝑁 que representa el número de concursantes
que hay en el programa, y a los que vamos a tener que buscar parejas.

La siguiente línea contiene una cadena 𝐶 que nos indica la cualidad que más valora ese
concursante en una pareja. 𝐶 puede variar entre “kindness”, “intelligence” o “beauty”.

Por cada concursante, se nos dará la siguiente información: un número entero 𝑀, que
corresponde al tiempo máximo que le queda en el programa, un número entero 𝑇 que
determina el número de posibles parejas que hay para él/ella, y 𝑇 líneas.

Las 𝑇 líneas contienen una cadena 𝑂 y cuatro enteros 𝑏, 𝑖, 𝑘 y 𝑡, separados por un espacio,
que indican el nombre de la persona, su nivel de belleza, su nivel de inteligencia, su nivel
de amabilidad y el tiempo que requiere para seducir al concursante respectivamente.

Salida:
Por cada concursante, se debe imprimir en una línea separado por espacios las personas
que le consiguen seducir antes de llegar al límite de tiempo en orden de selección. En la
siguiente línea se debe imprimir con dos decimales el beneficio obtenido con esta
selección.

Ejemplo de entrada:
1
kindness
100
4
Saul 70 100 30 5
Jara 100 60 100 50
Ivan 20 80 100 70
Rosa 20 100 70 100

Ejemplo de salida:
Saul Jara Ivan
194.29

Límites:
• 1 ≤ 𝑁 ≤ 133
• 4 ≤ 𝑇 ≤ 100
• 100 ≤ 𝑀 ≤ 6666
• 1 ≤ 𝑏, 𝑖, 𝑘, 𝑡 < 100
"""
def capturar_datos():
    n = int(input())  # Número de concursantes
    lista_cualidades_buscadas = []
    lista_tiempo_maximo = []
    lista_parejas = []
    num_pretendientes_por_concursante = []
    lista_candidatos = []
    for i in range(n):
        cualidad_buscada = input()
        tiempo_maximo = int(input())
        numero_pretendientes = int(input())

        nombres = []
        belleza = []
        inteligencia = []
        amabilidad = []
        tiempos_seduccion = []
        candidatos = set()
        for j in range(numero_pretendientes):
            string = input().split()
            nombres.append(string[0])
            belleza.append(int(string[1]))
            inteligencia.append(int(string[2]))
            amabilidad.append(int(string[3]))
            tiempos_seduccion.append(int(string[4]))
            candidatos.add(j)
        lista_cualidades_buscadas.append(cualidad_buscada)
        lista_tiempo_maximo.append(tiempo_maximo)
        num_pretendientes_por_concursante.append(numero_pretendientes)
        lista_parejas.append((nombres, belleza, inteligencia, amabilidad, tiempos_seduccion))
        lista_candidatos.append(candidatos)


    return n, lista_cualidades_buscadas, lista_tiempo_maximo,num_pretendientes_por_concursante, lista_parejas, lista_candidatos


def mejor_candidato(participante, lista_candidatos, lista_parejas, cualidad):
    max_ratio = -1
    indice_mejor = -1

    _, belleza, inteligencia, amabilidad, tiempos_seduccion = lista_parejas[participante]

    for i in lista_candidatos[participante]:
        if cualidad == "beauty":
            valor = belleza[i]
        elif cualidad == "intelligence":
            valor = inteligencia[i]
        else:
            valor = amabilidad[i]

        ratio = valor / tiempos_seduccion[i]

        if ratio > max_ratio:
            max_ratio = ratio
            indice_mejor = i

    return indice_mejor


def es_factible(tiempo_restante, lista_parejas, indice_candidato, participante):
    _, _, _, _ , tiempo_para_seducir = lista_parejas[participante]
    return tiempo_para_seducir[indice_candidato] <= tiempo_restante


def luces():
    n, lista_cualidades_buscadas, lista_tiempo_maximo, num_pretendientes_por_concursante, lista_parejas, lista_candidatos = capturar_datos()

    for i in range(n):
        tiempo_restante = lista_tiempo_maximo[i]
        esta_resuelto = True
        nombres_pretendientes_seleccionados = []
        beneficio_total = 0.0
        while lista_candidatos[i] and esta_resuelto:
            indice_mejor_candidato = mejor_candidato(i,lista_candidatos, lista_parejas, lista_cualidades_buscadas[i])
            nombres, bellezas, inteligencias, simpatias, tiempo_para_seducir = lista_parejas[i]
            nombres_pretendientes_seleccionados.append(nombres[indice_mejor_candidato])
            cualidad = lista_cualidades_buscadas[i]
            if es_factible(tiempo_restante, lista_parejas, indice_mejor_candidato, i):
                tiempo_restante -= tiempo_para_seducir[indice_mejor_candidato]
                if cualidad == "beauty":
                    beneficio_total += bellezas[indice_mejor_candidato]
                elif cualidad == "intelligence":
                    beneficio_total += inteligencias[indice_mejor_candidato]
                else:
                    beneficio_total += simpatias[indice_mejor_candidato]
            else:
                fraccion_tiempo = tiempo_restante / tiempo_para_seducir[indice_mejor_candidato]
                if cualidad == "beauty":
                    beneficio_total += bellezas[indice_mejor_candidato] * fraccion_tiempo
                elif cualidad == "intelligence":
                    beneficio_total += inteligencias[indice_mejor_candidato] * fraccion_tiempo
                else:  # "kindness"
                    beneficio_total += simpatias[indice_mejor_candidato] * fraccion_tiempo
                esta_resuelto =  False
            lista_candidatos[i].remove(indice_mejor_candidato)
        # Imprimir resultados
        print(" ".join(nombres_pretendientes_seleccionados))
        print(f"{beneficio_total:.2f}")

luces()
