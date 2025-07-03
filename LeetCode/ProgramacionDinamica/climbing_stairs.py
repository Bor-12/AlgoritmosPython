class Solution:
    def dp(self, n, memo):
        if n in memo:
            return memo[n]
        memo[n] = self.dp(n - 1, memo) + self.dp(n - 2, memo)
        return memo[n]
    #memoriacacion
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}
        return self.dp(n, memo)
    #lo hago ahora  con espacio O(1) hago un bottom up aproach
    def climbStairs2(self,  n: int)-> int:
        uno, dos = 1, 1
        for i in range(n - 1):
            dos, uno = uno , uno + dos
        return uno
sol = Solution()


print(sol.climbStairs(2))
print(sol.climbStairs(3))
print(sol.climbStairs(5))

print(sol.climbStairs2(2))
print(sol.climbStairs2(3))
print(sol.climbStairs2(5))
