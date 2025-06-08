def numTrees2(n):
    memo = {}

    def count_trees(nodes):
        if nodes in memo:
            return memo[nodes]
        if nodes <= 1:
            return 1
        total = 0
        for root in range(1, nodes + 1):
            izquierda = root - 1
            derecha = nodes - root
            total += count_trees(izquierda) * count_trees(derecha)
        memo[nodes] = total
        return total

    return count_trees(n)

def numTrees(n):
    memo = [1] * (n + 1)
    for nodes in range(2, n + 1):
        resultado = 0
        for root in  range(1, nodes + 1):
            izquierda = root - 1
            derecha = nodes  - root
            resultado += memo[izquierda] * memo[derecha]
        memo[nodes] = resultado
    return memo[n]
print(numTrees(1))
print(numTrees(3))
print(numTrees(5))
print(numTrees2(1))
print(numTrees2(3))
print(numTrees2(5))