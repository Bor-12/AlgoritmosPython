"""
Problema: Vuelta al Mundo

Descripción:
Flex, nuestro youtuber favorito, quiere dar la vuelta al mundo como Willy Fog. Para ello,
necesita organizar bien los países que visitará. Sin embargo, debido a restricciones
climáticas, no puede estar en algunos países durante ciertos meses.

Después de una exhaustiva planificación, ha definido los meses en los que quiere estar
en cada país. Pero ha sido demasiado ambicioso, y es **imposible visitar todos los países
que quiere en los meses que ha indicado**.

Tu tarea es ayudar a Flex a determinar **cuántos países podrá visitar como máximo**,
**sin estar en dos países al mismo tiempo**.

----------------------------------------------------------------------------------------

Entrada:
- La primera línea contiene un entero `V` (1 ≤ V ≤ 100), que indica el número de posibles
  **itinerarios** que ha planificado.

- Cada itinerario consta de:
  1. Una línea con un entero `P` (1 ≤ P ≤ 1000), que representa la cantidad de países que
     ha incluido en el itinerario.
  2. Una línea con `2 * P` enteros, donde cada par `(Xi, Yi)` indica:
     - `Xi` (1 ≤ Xi ≤ Yi ≤ 10000): **Mes en el que Flex llega** al país `i`.
     - `Yi` (1 ≤ Yi ≤ 10000): **Mes en el que Flex se va** del país `i`.

----------------------------------------------------------------------------------------

Salida:
- Se imprimirán `V` líneas, donde cada línea contiene un entero que representa el
  **máximo número de países** que Flex puede visitar en esa vuelta al mundo,
  **sin estar en dos países a la vez**.

----------------------------------------------------------------------------------------

Ejemplo de Entrada:
3
3
2 5 1 3 4 6
2
3 4 2 3
4
2 3 1 5 3 5 5 8

Ejemplo de Salida:
2
2
3
----------------------------------------------------------------------------------------

Restricciones:
- `1 ≤ V ≤ 100`  → Flex puede planificar hasta 100 vueltas al mundo.
- `1 ≤ P ≤ 1000` → Un itinerario puede incluir hasta 1000 países.
- `1 ≤ Xi ≤ Yi ≤ 10000` → Los meses están en un rango de 1 a 10000.
"""
def capturar_datos():
    numero_itinerarios = int(input())

    lista_itinerarios = []
    for _ in range(numero_itinerarios):
        numero_paises = int(input())
        linea = input().split()
        lista_itinerario = []
        for j in range(0, len(linea), 2):
            llegada_al_pais = int(linea[j])
            salida_del_pais = int(linea[j + 1])
            lista_itinerario.append((llegada_al_pais,salida_del_pais))
        lista_itinerarios.append(lista_itinerario)
    return numero_itinerarios, lista_itinerarios

def es_factible(ultima_salida, llegada):
    return ultima_salida <= llegada

def vuelta_al_mundo():
    numero_itinerarios, lista_itinerarios = capturar_datos()
    for i in range(numero_itinerarios):
        lista_ordenada_pais_que_antes_sale = sorted(lista_itinerarios[i], key=lambda x: x[1])
        solucion = 0
        ultima_salida = -1
        for llegada, salida in lista_ordenada_pais_que_antes_sale:
            if es_factible(ultima_salida, llegada):
                ultima_salida = salida
                solucion += 1
        print(solucion)

vuelta_al_mundo()