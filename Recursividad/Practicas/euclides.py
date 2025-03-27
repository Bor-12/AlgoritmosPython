def euclides():

    string = input().split()
    entero_a = int(string[0])
    entero_b = int(string[1])

    def recursividad(a, b):
        if (b == 0):
            return a
        return recursividad(b, a % b)

    return recursividad(entero_a, entero_b)

print(euclides())