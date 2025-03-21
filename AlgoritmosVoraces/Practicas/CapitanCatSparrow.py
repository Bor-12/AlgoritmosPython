def capturar_datos():
    entrada = input().split()
    numero_de_camas = int(entrada[0])
    numero_de_conexiones_entre_camas = int(entrada[1])

    grafo = {i: [] for i in range(numero_de_camas)}

    for i in range(numero_de_conexiones_entre_camas):
        entrada = input().split()
        origen = int(entrada[0])
        destino = int(entrada[1])
        distancia = int(entrada[2])

        grafo[origen].append((destino, distancia))
        grafo[destino].append((origen, distancia))

    entrada = input().split()
    vertice_inicial = int(entrada[0])
    vertice_final = int(entrada[1])

    return numero_de_camas, grafo, vertice_inicial, vertice_final


def capitanCatSparrow():
    numero_de_camas, grafo, vertice_inicial, vertice_final = capturar_datos()

    cola_con_prioridad = [(vertice_inicial, 0)]

    distancias = [float('inf')] * numero_de_camas
    distancias[vertice_inicial] = 0


    camino = [-1] * numero_de_camas

    while cola_con_prioridad:
        nodo_actual, distancia_actual = cola_con_prioridad.pop(0)

        if distancia_actual > distancias[nodo_actual]:
            continue

        if vertice_final == nodo_actual:
            break

        for nodo_destino, distancia_al_nodo_destino in grafo[nodo_actual]:
            nueva_distancia = distancias[nodo_actual] + distancia_al_nodo_destino
            if nueva_distancia < distancias[nodo_destino]:
                distancias[nodo_destino] = nueva_distancia
                camino[nodo_destino] = nodo_actual
                cola_con_prioridad.append((nodo_destino, nueva_distancia))

        cola_con_prioridad = sorted(cola_con_prioridad, key=lambda x: x[1])

    print(distancias[vertice_final])

    # Reconstruir camino
    recorrido = []
    actual = vertice_final
    while actual != -1:
        recorrido.append(actual)
        actual = camino[actual]
    recorrido.reverse()

    print(' '.join(map(str, recorrido))) #poner en el fomato que pide el DomJudge



capitanCatSparrow()

