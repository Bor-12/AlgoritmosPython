"""
Alfombra Roja

En casi todos los eventos, o al menos en los más importantes, hay una alfombra roja por
la que pasan las personalidades más relevantes. Esperando en la alfombra se encuentran
ciertos periodistas para fotografiar y entrevistar a las personas más relevantes que pasen
por ahí. Sin embargo, estos periodistas están yendo demasiado lento y deben ordenar
urgentemente a las siguientes personas que van a ser entrevistadas, ya que hay algunas
que si esperan mucho se van a ir del evento y esto no conviene a la organización de este.

Para poder asegurarnos de que las personas “más importantes” sean fotografiadas y
entrevistadas y que el evento sea todo un éxito, debemos ayudarles implementando un
algoritmo. Para ello, tenemos que saber que el orden será determinado teniendo en cuenta
tanto la amabilidad del famoso como su fama. Es importante ser consciente de que cuanto
más famosa es una persona, mayor prioridad de ser atendida; y cuanto más amable sea,
menor prioridad tiene ya que entiende que debe esperar. Tenemos que diseñar un orden
que optimice la combinación de fama y amabilidad para garantizar una correcta atención.

Entrada:
La primera línea contiene un entero 𝑁 que indica el número de famosos esperando. Las
siguientes 𝑁 líneas contienen una cadena 𝑆 con el nombre de cada famoso además de un
entero 𝑀 con el grado de amabilidad del individuo, un entero 𝐿 con el grado de fama de
este, y un entero 𝑇 con el tiempo que va a ser entrevistado.

Salida:
La salida será el nombre de cada uno de los famosos ordenados según el orden
determinado por nuestro algoritmo. Por último, se imprimirá el número de minutos que
deberá esperar el famoso cuyo nombre sea el primero alfabéticamente.

Ejemplo de entrada:
5
Rivers 80 50 6
Ibai 65 60 7
KanyeWest 10 2 1
TaylorSwift 90 95 10
Chiara 85 20 4

Ejemplo de salida:
TaylorSwift
Ibai
Rivers
Chiara
KanyeWest
23
"""
def mejor_candidato(candidatos, lista_fama, lista_amabilidad):
    maximo = -1
    indice_mejor = -1
    for i in candidatos:
        prioridad = lista_fama[i] / lista_amabilidad[i]  # División real
        if maximo < prioridad:
            maximo = prioridad
            indice_mejor = i
    return indice_mejor


def alfombra_roja():
    n = int(input())

    lista_nombres = []
    lista_fama = []
    lista_amabilidad = []
    lista_tiempo = []

    candidatos = set()
    solucion = []

    for i in range(n):
        string = input().split()

        nombre = string[0]
        amabilidad = int(string[1])
        fama = int(string[2])
        tiempo = int(string[3])

        lista_nombres.append(nombre)
        lista_amabilidad.append(amabilidad)
        lista_fama.append(fama)
        lista_tiempo.append(tiempo)
        candidatos.add(i)

    tiempo_total = 0
    tiempo_espera = {}

    while candidatos:
        indice_mejor_candidato = mejor_candidato(candidatos, lista_fama, lista_amabilidad)

        nombre = lista_nombres[indice_mejor_candidato]
        solucion.append(nombre)

        tiempo_espera[nombre] = tiempo_total

        tiempo_total += lista_tiempo[indice_mejor_candidato]

        candidatos.remove(indice_mejor_candidato)

    primer_famoso_lista_alfabetica = min(solucion)  # min() obtiene el menor alfabéticamente
    tiempo_primero = tiempo_espera[primer_famoso_lista_alfabetica]

    for nombre in solucion:
        print(nombre)


    print(tiempo_primero)


alfombra_roja()