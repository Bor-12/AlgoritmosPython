import heapq
from queue import PriorityQueue

from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        piedras = [-s for s in stones]
        heapq.heapify(piedras)
        while len(piedras) > 1:
            primera_piedra = -heapq.heappop(piedras)
            segunda_piedra = -heapq.heappop(piedras)
            if primera_piedra > segunda_piedra:
                heapq.heappush(piedras, primera_piedra - segunda_piedra)
        piedras.append(0)
        return abs(piedras[0])

s = Solution()
print(s.lastStoneWeight([1]))
print(s.lastStoneWeight([2,3,6,2,4]))
