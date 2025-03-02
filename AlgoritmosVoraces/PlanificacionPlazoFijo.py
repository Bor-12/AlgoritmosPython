def indice_mayor_beneficio(candidatos, beneficios):
    indice_mayor_beneficio = -1
    mayor_beneficio = -1
    for i in candidatos:
        if beneficios[i] > mayor_beneficio:
            mayor_beneficio = beneficios[i]
            indice_mayor_beneficio = i
    return indice_mayor_beneficio
def es_factible(indice, fechas_tope, agenda):
    """Busca el último hueco disponible antes de la fecha tope."""
    for t in range(fechas_tope[indice] - 1, -1, -1):  # De atrás hacia adelante
        if agenda[t] == -1:
            return t  # Devuelve la posición libre
    return -1  # No hay espacio disponible
def planificacion_plazo_fijo(beneficios: list[int], fechas_tope: list[int], numero_de_trabajos) -> list[int]:
    candidatos = set()
    for i in range(numero_de_trabajos):
        candidatos.add(i)
    agenda = [-1] * numero_de_trabajos
    while candidatos:
        indice = indice_mayor_beneficio(candidatos, beneficios)
        posicion_en_la_agenda = es_factible(indice, fechas_tope, agenda)
        if posicion_en_la_agenda != -1:
            agenda[posicion_en_la_agenda] = indice
        candidatos.remove(indice)
    return agenda

beneficios  = [50, 10, 15, 30]
fechas_tope = [2, 1, 2, 1]
solucion = planificacion_plazo_fijo(beneficios, fechas_tope, numero_de_trabajos = len(beneficios))
print(solucion)
