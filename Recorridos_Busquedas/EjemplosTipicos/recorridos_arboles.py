def crear_nodo(valor):
    return {"valor": valor, "izquierda": None, "derecha": None}

def insertar(arbol, valor):
    if arbol is None:
        return crear_nodo(valor)
    if valor < arbol["valor"]:
        arbol["izquierda"] = insertar(arbol["izquierda"], valor)
    else:
        arbol["derecha"] = insertar(arbol["derecha"], valor)
    return arbol

def imprimir_inorden(arbol):
    if arbol is not None:
        imprimir_inorden(arbol["izquierda"])
        print(arbol["valor"], end=" ")
        imprimir_inorden(arbol["derecha"])

def imprimir_posorden(arbol):
    if arbol is not None:
        imprimir_posorden(arbol["izquierda"])
        imprimir_posorden(arbol["derecha"])
        print(arbol["valor"], end=" ")

def imprimir_preorden(arbol):
    if arbol is not None:
        print(arbol["valor"], end=" ")
        imprimir_preorden(arbol["izquierda"])
        imprimir_preorden(arbol["derecha"])

# Construcción del árbol
arbol = None
for v in [10, 5, 15, 3, 7, 12, 18]:
    arbol = insertar(arbol, v)

# Mostrar los tres recorridos
print("Recorrido INORDEN:")
imprimir_inorden(arbol)  # Esperado: 3 5 7 10 12 15 18

print("\n\nRecorrido PREORDEN:")
imprimir_preorden(arbol)  # Esperado: 10 5 3 7 15 12 18

print("\n\nRecorrido POSORDEN:")
imprimir_posorden(arbol)  # Esperado: 3 7 5 12 18 15 10
