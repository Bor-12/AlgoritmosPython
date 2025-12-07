from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        contador_ventana = 0
        izquierda = 0
        derecha = 0
        frecuencias_frutas = {}
        contador_frutas_distintas = 0
        maximo = 0
        while derecha < len(fruits):
            frecuencias_frutas[fruits[derecha]] = frecuencias_frutas.get(fruits[derecha], 0) + 1
            if frecuencias_frutas[fruits[derecha]] == 1:
                contador_frutas_distintas += 1

            while contador_frutas_distintas > 2:
                frecuencias_frutas[fruits[izquierda]] -= 1
                if frecuencias_frutas[fruits[izquierda]] == 0:
                    del frecuencias_frutas[fruits[izquierda]]
                    contador_frutas_distintas -= 1
                izquierda += 1
            maximo = max(maximo, derecha - izquierda + 1)
            derecha += 1

        return maximo

s = Solution()
print(s.totalFruit(fruits = [1,2,1]))
print(s.totalFruit(fruits = [1,2,3,2,2]))
print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))

